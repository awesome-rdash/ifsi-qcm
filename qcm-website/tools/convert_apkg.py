"""Convertit les paquets Anki de decks/*.apkg en JSON pour le site (site/data/).

Usage : python tools/convert_apkg.py [dossier_decks] [dossier_sortie]
Dépendance : zstandard (format de paquet récent, collection.anki21b).
Contrat de sortie : specs/001-site-revision-qcm/contracts/donnees.md
"""
import json
import re
import shutil
import sqlite3
import sys
import tempfile
import unicodedata
import zipfile
from collections import Counter
from pathlib import Path

import zstandard

RACINE = Path(__file__).resolve().parent.parent
ZSTD_MAGIC = b"\x28\xb5\x2f\xfd"
MOTIF_PAQUET = re.compile(r"^IFSI::QCM::Semestre (\d+)::(UE [\d.]+) - (.+?)::(.+)$")
MOTIF_IMPORTANCE = re.compile(r"(?:^|\s)PSB::Importance::(I[0-3])(?:\s|$)")
MOTIF_IMG = re.compile(r'<img\b[^>]*?\bsrc\s*=\s*"([^"]+)"[^>]*>', re.I)
MOTIF_PAGE = re.compile(r"_p\d+\.\w+$", re.I)
MOTIF_FICHIER = re.compile(r"prompt v([\w.]+) - (\d{4}-\d{2}-\d{2})")


class ErreurPaquet(Exception):
    pass


def dezstd(data):
    return zstandard.ZstdDecompressor().decompressobj().decompress(data)


def varint(buf, i):
    n = shift = 0
    while True:
        b = buf[i]
        i += 1
        n |= (b & 0x7F) << shift
        if b < 0x80:
            return n, i
        shift += 7


def champs_protobuf(buf):
    """Itère (numéro de champ, valeur) d'un message protobuf ; seuls varint et longueur."""
    i = 0
    while i < len(buf):
        cle, i = varint(buf, i)
        num, typ = cle >> 3, cle & 7
        if typ == 0:
            val, i = varint(buf, i)
        elif typ == 2:
            n, i = varint(buf, i)
            val, i = buf[i:i + n], i + n
        else:
            raise ErreurPaquet(f"protobuf : type de champ {typ} inattendu")
        yield num, val


def table_medias(z):
    """Nom de membre du zip -> nom du média."""
    brut = z.read("media")
    if brut.startswith(ZSTD_MAGIC):
        brut = dezstd(brut)
    try:
        return {k: v for k, v in json.loads(brut.decode("utf-8")).items()}
    except (UnicodeDecodeError, json.JSONDecodeError):
        pass
    noms = {}
    for num, entree in champs_protobuf(brut):
        if num != 1:
            continue
        nom = next((v.decode("utf-8") for n, v in champs_protobuf(entree) if n == 1), None)
        if nom:
            noms[str(len(noms))] = nom
    return noms


def ouvrir_collection(z, dossier_tmp):
    for nom, compresse in (("collection.anki21b", True), ("collection.anki21", False),
                           ("collection.anki2", False)):
        if nom in z.namelist():
            data = z.read(nom)
            chemin = Path(dossier_tmp) / "collection.db"
            chemin.write_bytes(dezstd(data) if compresse else data)
            return sqlite3.connect(chemin)
    raise ErreurPaquet("aucune collection Anki dans le paquet")


def tables(db):
    return {r[0] for r in db.execute("select name from sqlite_master where type='table'")}


def types_de_note(db):
    if "notetypes" in tables(db):
        return {i: n for i, n in db.execute("select id, name from notetypes")}
    modeles = json.loads(db.execute("select models from col").fetchone()[0])
    return {int(k): v["name"] for k, v in modeles.items()}


def noms_paquets(db):
    if "decks" in tables(db):
        return {i: n.replace("\x1f", "::") for i, n in db.execute("select id, name from decks")}
    paquets = json.loads(db.execute("select decks from col").fetchone()[0])
    return {int(k): v["name"] for k, v in paquets.items()}


def slug(texte):
    t = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def nom_media(nom):
    return re.sub(r"\s+", "-", nom.strip().lower())


def sans_br_final(html):
    return re.sub(r"(\s*<br\s*/?>\s*)+$", "", html.strip(), flags=re.I)


def extraire_images(html, garder):
    """Retire du HTML les <img> dont garder(nom) est faux ; réécrit les autres en media/.

    Renvoie (html, [noms retirés], {noms utilisés}).
    """
    retires, utilises = [], set()

    def remplacer(m):
        nom = nom_media(m.group(1))
        utilises.add(m.group(1))
        if garder(nom):
            return m.group(0).replace(m.group(1), f"media/{nom}")
        retires.append(nom)
        return ""

    return sans_br_final(MOTIF_IMG.sub(remplacer, html)), retires, utilises


def lire_paquet(chemin):
    """Renvoie une liste de cours {meta, questions, medias(set), mod}."""
    with zipfile.ZipFile(chemin) as z, tempfile.TemporaryDirectory() as tmp:
        db = ouvrir_collection(z, tmp)
        try:
            modeles = types_de_note(db)
            paquets = noms_paquets(db)
            notes = db.execute("select id, guid, mid, mod, tags, flds from notes").fetchall()
            paquet_de_note = {}
            for nid, did in db.execute("select nid, did from cards"):
                paquet_de_note.setdefault(nid, Counter())[did] += 1
        finally:
            db.close()
        if not notes:
            raise ErreurPaquet("aucune note")

        m = MOTIF_FICHIER.search(chemin.name)
        version, genere_le = (m.group(1), m.group(2)) if m else (None, None)
        cours = {}
        for nid, guid, mid, mod, tags, flds in notes:
            if modeles.get(mid) != "QCMs":
                raise ErreurPaquet(f"note {guid} de type « {modeles.get(mid)} » au lieu de QCMs")
            f = flds.split("\x1f")
            if len(f) < 11:
                raise ErreurPaquet(f"note {guid} : {len(f)} champs au lieu de 19")
            nom_paquet = paquets.get(paquet_de_note[nid].most_common(1)[0][0], "")
            mp = MOTIF_PAQUET.match(nom_paquet)
            if not mp:
                raise ErreurPaquet(f"nom de paquet inattendu : « {nom_paquet} »")
            imp = MOTIF_IMPORTANCE.search(tags)
            if not imp:
                raise ErreurPaquet(f"note {guid} sans étiquette PSB::Importance::I0..I3")
            mode = f[2].strip()
            if mode not in ("0", "1", "2"):
                raise ErreurPaquet(f"note {guid} : mode « {mode} » inconnu")
            reponses = f[3].split()
            props = f[7:11]
            if len(reponses) != 4 or set(reponses) - {"0", "1"} or not all(p.strip() for p in props):
                raise ErreurPaquet(f"note {guid} : réponses « {f[3]} » ou propositions invalides")

            sem, ue, ue_int, nom = int(mp.group(1)), mp.group(2), mp.group(3), mp.group(4)
            cid = f"s{sem}-{slug(ue).replace('ue-', 'ue')}-{slug(nom)}"
            c = cours.setdefault(cid, {
                "meta": {"id": cid, "semestre": sem, "ue": ue, "ue_intitule": ue_int, "nom": nom,
                         "contexte": None, "version": version, "genere_le": genere_le},
                "questions": [], "medias": set(), "mod": 0, "contextes": Counter()})
            c["mod"] = max(c["mod"], mod)
            c["contextes"][f[5]] += 1

            question, q_imgs, u1 = extraire_images(f[0], lambda n: False)
            infos, pages, u2 = extraire_images(f[6], lambda n: not MOTIF_PAGE.search(n))
            # shortcut: une seule image de question est isolée ; les suivantes restent en ligne.
            if len(q_imgs) > 1:
                question += "".join(f'<br><img src="media/{n}">' for n in q_imgs[1:])
            c["medias"] |= u1 | u2
            c["questions"].append({
                "id": guid, "guid": guid, "mode": int(mode), "importance": imp.group(1),
                "titre": f[1], "question": question, "propositions": props,
                "reponses": [int(r) for r in reponses],
                "image": f"media/{q_imgs[0]}" if q_imgs else None,
                "infos": infos, "page_cours": [f"media/{p}" for p in pages],
                "sources": f[4], "danger": "⛔" in f[6]})

        noms = table_medias(z)
        par_nom = {v: k for k, v in noms.items()}
        for c in cours.values():
            c["meta"]["contexte"] = c.pop("contextes").most_common(1)[0][0]
            fichiers = {}
            for nom in c["medias"]:
                if nom not in par_nom:
                    print(f"  ! média absent du paquet : {nom}", file=sys.stderr)
                    continue
                data = z.read(par_nom[nom])
                fichiers[nom_media(nom)] = dezstd(data) if data.startswith(ZSTD_MAGIC) else data
            c["medias"] = fichiers
        return list(cours.values())


def convertir(dossier_decks, sortie):
    retenus = {}
    paquets = sorted(Path(dossier_decks).glob("*.apkg"))
    for chemin in paquets:
        try:
            for c in lire_paquet(chemin):
                cid = c["meta"]["id"]
                ancien = retenus.get(cid)
                if ancien and ancien[1]["mod"] >= c["mod"]:
                    print(f"  ! {chemin.name} ignoré : {ancien[0].name} est plus récent pour {cid}")
                    continue
                if ancien:
                    print(f"  ! {ancien[0].name} remplacé par {chemin.name} pour {cid}")
                retenus[cid] = (chemin, c)
        except (ErreurPaquet, zipfile.BadZipFile, sqlite3.Error, KeyError) as e:
            raise SystemExit(f"ERREUR {chemin.name} : {e}")

    sortie = Path(sortie)
    if sortie.exists():
        shutil.rmtree(sortie)
    index = []
    for cid, (chemin, c) in sorted(retenus.items()):
        dossier = sortie / cid
        (dossier / "media").mkdir(parents=True)
        for nom, data in c["medias"].items():
            (dossier / "media" / nom).write_bytes(data)
        qs = c["questions"]
        (dossier / "questions.json").write_text(json.dumps(
            {"format": 1, "cours": c["meta"], "questions": qs}, ensure_ascii=False), "utf-8")
        m = c["meta"]
        index.append({"id": cid, "semestre": m["semestre"], "ue": m["ue"],
                      "ue_intitule": m["ue_intitule"], "nom": m["nom"],
                      "fichier": f"data/{cid}/questions.json", "total": len(qs),
                      "par_importance": dict(sorted(Counter(q["importance"] for q in qs).items()))})
        print(f"{chemin.name} -> {cid} : {len(qs)} questions, {len(c['medias'])} images")
    sortie.mkdir(parents=True, exist_ok=True)
    (sortie / "index.json").write_text(
        json.dumps({"format": 1, "cours": index}, ensure_ascii=False, indent=1), "utf-8")
    print(f"{len(index)} cours publiés dans {sortie}")


if __name__ == "__main__":
    convertir(sys.argv[1] if len(sys.argv) > 1 else RACINE / "decks",
              sys.argv[2] if len(sys.argv) > 2 else RACINE / "site" / "data")
