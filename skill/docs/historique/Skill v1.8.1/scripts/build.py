"""Construction d'un paquet QCM Anki (skill qcm-anki-ifsi).
Usage : python3 build.py <dossier_du_cours> [--report-only]
Le dossier du cours contient : cours.py (paramètres), k.py (inventaire K + EXCLUS),
les fichiers de questions listés dans cours.QFILES, et facultativement corrections.py (dict CORR id -> attributs).
Les scripts communs (build.py, common.py, glossaire.py) restent dans le dossier Outils."""
import sys, os, re, shutil, collections, datetime, hashlib, json, importlib, statistics as st
TOOLS = os.path.dirname(os.path.abspath(__file__))
COURSE = os.path.abspath(next((a for a in sys.argv[1:] if not a.startswith("--")), "."))
sys.path[:0] = [COURSE, TOOLS]
import cours as C
from k import K, EXCLUS
from glossaire import gloss
if os.path.exists(os.path.join(COURSE, "glossaire_cours.py")):
    from glossaire_cours import EXTRA; import glossaire as _g; _g.add(EXTRA)

PDF, PDFNAME, TYPE, CONTEXTE, DECK, PREFIX = os.path.join(COURSE, C.PDF), C.PDFNAME, C.TYPE, C.CONTEXTE, C.DECK, C.PREFIX
MODEL = getattr(C, "MODEL", "Claude")
VERSION = getattr(C, "VERSION", "1.2")
DATE = datetime.date.today().isoformat()
OUT = os.path.join(COURSE, "out")
REF_APKG = os.path.join(COURSE, getattr(C, "REF_APKG", os.path.join(TOOLS, "Type de note QCMs.apkg")))   # chemins relatifs au dossier du cours
BASENAME = f"{C.NOM} - QCM - skill v{VERSION} - {DATE}"
SUFFIX = {0: " <i>(vrai ou faux pour chaque affirmation)</i>", 1: " <i>(une ou plusieurs réponses)</i>", 2: " <i>(une seule réponse)</i>"}

KD = {k[0]: k for k in K}
QS = [q for m in C.QFILES for q in importlib.import_module(m).QS]
# corrections successives (ordre : dicts listés dans cours.CORRECTIONS, chacun id -> {attribut: valeur} ; "props" seul accepté en liste)
for modname, dname in getattr(C, "CORRECTIONS", []):
    D = getattr(importlib.import_module(modname), dname)
    for _q in QS:
        v = D.get(_q.id)
        if v is None: continue
        if isinstance(v, list): _q.props = v
        else:
            for _k, _v in v.items(): setattr(_q, _k, _v)
strip = lambda s: re.sub(r"<[^>]+>", "", s)
# remplacements de texte (sigles écrits en toutes lettres, etc.) appliqués à tous les champs
for _a, _b in getattr(C, "TEXT_REPL", []):
    for _q in QS:
        _q.q = re.sub(_a, _b, _q.q); _q.props = [re.sub(_a, _b, x) for x in _q.props]
        _q.expl = re.sub(_a, _b, _q.expl)
        if _q.x: _q.x = re.sub(_a, _b, _q.x)

def pages_of(kid):
    out = []
    for part in KD[kid][1].split(","):
        if "-" in part:
            x, y = map(int, part.split("-")); out += list(range(x, y + 1))
        else:
            out.append(int(part))
    return out

DOMAINE = getattr(C, "DOMAINE", "")
TITRE_VIGNETTE = getattr(C, "TITRE_VIGNETTE", "Cas clinique")
def qtext(q):
    t = q.q.strip()
    dom = getattr(C, "DOMAINE_VOCAB", DOMAINE) if q.id.startswith("V") else DOMAINE
    if dom and not strip(t).startswith(dom + " –"):   # R8 : domaine en tête de chaque question
        t = f"{dom} – {t}"
    if q.mode == 0:  # le suffixe Kprim remplace « vrai ou faux »
        t = re.sub(r"\s*(:\s*)?\(?vrai ou faux\)?\s*\??\s*$", "", t, flags=re.I).rstrip(" :") + " ?"
        t = t.replace("? ?", "?")
    return t

def title(q):
    if getattr(q, "titre", None): return q.titre   # R11 : titre neutre imposé (ex. vignette dont la section donnerait la réponse)
    if q.vign: return TITRE_VIGNETTE   # R11 : titre neutre par défaut pour une vignette
    sec = KD[q.ks[0]][3]
    if not q.notion or q.notion == sec or (sig(q.notion) & sig(sec)): return sec   # R2 : pas de section répétée dans la notion
    # la notion n'est ajoutée que si elle apporte une information absente de la question
    if sig(q.notion) & sig(qtext(q)): return sec
    return f"{sec} — {q.notion}"

# ---------- contrôles ----------
STOP = set("""dans avec pour sans entre selon chez cette cours leurs leur après avant quel quelle quels quelles
lequel laquelle lesquels lesquelles comme aussi elles ils plus moins tous toutes faire fait sont être était quoi
parmi patient patiente première premier""".split())
def sig(text):
    words = re.findall(r"[A-Za-zÀ-ÿœŒ0-9]+", strip(text))
    out = set()
    for w in words:
        if w.isupper() and len(w) >= 3: out.add(w.lower())
        elif len(w) >= 5 and w.lower() not in STOP: out.add(re.sub(r"(s|x)$", "", w.lower()))
    return out

SIGLES_OK = set(getattr(C, "SIGLES_OK", [])) | {"AVC", "IFSI", "UE", "CM", "SSU"}
ABS = r"\b(toujours|jamais|systématique\w*|uniquement|seulement|aucun\w*|tous|toutes|quoi qu'il arrive)\b"
VAGUE = r"\b(souvent|parfois|rarement|habituellement|peut|peuvent|associée?s?)\b"

# racines des mots (R7, R5, R11) : 6 premières lettres sans accent, pour rapprocher « bronches » et « bronchique » ; sigles gardés entiers
FOLD = str.maketrans("àâäéèêëîïôöùûüçœ", "aaaeeeeiioouuuco")
def roots(text):
    out = set()
    for w in re.findall(r"[A-Za-zÀ-ÿœŒ0-9]+", strip(text)):
        if w.isupper() and len(w) >= 2: out.add(w)
        elif len(w) >= 5 and w.lower() not in STOP: out.add(w.lower().translate(FOLD)[:6])
    return out
DOM_ROOTS = roots(DOMAINE + " " + getattr(C, "DOMAINE_VOCAB", ""))
# R5 : mots qui désignent un attribut commun à plusieurs maladies (début du segment souligné)
ATTRIBUTS = r"(élément|gravité|terrain|cause|complication|forme|mode|signe|symptôme|examen|traitement|objectif|durée|délai|mécanisme|famille|classe|situation|paramètre|mortalité|handicap|fréquence|définition|facteur|risque|indication|contre-indication|surveillance|localisation|siège|âge|évolution|pronostic|prévention|bilan)"

# propositions composées (M8, M11) : éléments séparés par « ; », « , », « / » ou « et » (pas « 0 et 30 », pas « 1/4 »)
SEP = re.compile(r"\s*;\s*|,\s+|\s+/\s+|(?<!\d)\s+et\s+(?!\d)")
def parts(p): return [re.sub(r"^[≈~]\s*", "", x.strip().lower()) for x in SEP.split(strip(p)) if x.strip()]

# X3 : mots techniques à définir (repérage approximatif : suffixes médicaux et noms propres) ; signalés, non bloquants
TECH = re.compile(r"(ite|ose|ome|émie|urie|pathie|plégie|parésie|phasie|algie|ectomie|tomie|graphie|scopie|philie|pénie|lyse|trophie|plastie|stase|esthésie|opsie|praxie|gnosie|rragie|rrhée)s?$", re.I)
COURANTS = set("""limite limites suite ensuite conduite site visite petite réussite faite droite gratuite chose choses dose doses pose propose
rose cause somme comme homme hommes forme formes norme normes volume dépose expose suppose impose dispose risque note notes vite
reste suite écrite inscrite dite produite réduite habite évite mérite unité qualité quantité priorité sécurité activité mobilité
gravité spécialité totalité majorité minorité capacité continuité extrémité diversité nécessité intensité fragilité stabilité santé
syndrome symptôme analyse diagnose prise surprise reprise petites traite traitée facilite repose
hémorragie hémorragies glycémie hyperglycémie hypoglycémie hypoglycémies ischémie anémie nécrose anatomie radiographie échographie""".split())   # mots courants ou connus en 2e année
def a_definir(text):
    import glossaire
    plain, out = strip(text), set()
    for m in re.finditer(r"[A-Za-zÀ-ÿœŒ]+(?:-[A-Za-zÀ-ÿœŒ]+)*", plain):
        w, before = m.group(), plain[:m.start()].rstrip()
        tech = len(w) >= 5 and TECH.search(w) and w.lower() not in COURANTS
        propre = before and (before[-1].isalnum() or before[-1] in ",'’") and len(w) >= 4 and w[0].isupper() and w[1:].islower()   # nom propre en milieu de phrase
        if (tech or propre) and not any(rx.search(w) for _t, rx, _d, _s in glossaire._C): out.add(w)
    return out

def checks():
    block, report = [], collections.defaultdict(list)
    ids = collections.Counter(q.id for q in QS)
    block += [f"id dupliqué {i}" for i, n in ids.items() if n > 1]
    tx = collections.Counter((title(q) + " | " + strip(qtext(q))).lower() for q in QS)
    block += [f"énoncé dupliqué : {t}" for t, n in tx.items() if n > 1]
    cs = sig(CONTEXTE)
    for q in QS:
        P = q.props
        if len(P) != 4 or len(set(P)) != 4: block.append(f"{q.id}: 4 propositions différentes requises")
        if not re.fullmatch(r"[01]{4}", q.truth): block.append(f"{q.id}: vérité invalide")
        n1 = q.truth.count("1")
        if q.mode == 2 and n1 != 1: block.append(f"{q.id}: QCS avec {n1} bonnes")
        if q.mode == 1 and n1 < 1: block.append(f"{q.id}: QCM sans bonne réponse")
        for kid in q.ks:
            if kid not in KD: block.append(f"{q.id}: connaissance inconnue {kid}")
        if re.search(r"\b[1-4]\. (Vrai|Faux)", q.expl): block.append(f"{q.id}: renvoi numéroté")
        # répétitions Contexte / Titre / Question
        ts, qs_ = sig(title(q)), sig(qtext(q))
        allow = {re.sub(r"(s|x)$", "", w.lower()) for w in q.allow}
        # D51 : l'énoncé doit se comprendre seul (sans titre ni contexte) ; la répétition ne bloque qu'entre contexte et titre
        rep = (cs & ts) - allow
        if rep: block.append(f"{q.id}: mot répété entre contexte et titre : {sorted(rep)} | T={title(q)}")
        if len(qs_) < 2 and q.id[0] != "V": block.append(f"{q.id}: énoncé non autonome (moins de 2 mots porteurs de sens) : {strip(qtext(q))}")
        if (ts & qs_) - allow: report["titre_repete_dans_question"].append(f"{q.id}:{sorted((ts & qs_) - allow)}")
        Q = strip(qtext(q))
        # R9 : pas de provenance dans la question (on n'a pas le cours sous les yeux)
        if re.search(r"\b(notes?|tableau|diapos?|sch[ée]ma|graphique|cit[ée]e?s? dans|selon le cours|du cours)\b", Q, re.I):
            block.append(f"{q.id}: provenance dans la question (R9) : {Q}")
        # R10 : pas de renvoi à une autre carte
        if re.search(r"m[êe]me patient|carte pr[ée]c[ée]dente|ci-dessus|question pr[ée]c[ée]dente", Q, re.I):
            block.append(f"{q.id}: renvoi à une autre carte (R10) : {Q}")
        # F5 : « (s) » dans un QCM
        if q.mode == 1 and "(s)" not in Q: block.append(f"{q.id}: QCM sans « (s) » (F5) : {Q}")
        # R11 : le titre ne donne pas la réponse
        tru = set().union(*[sig(p) for i, p in enumerate(P) if q.truth[i] == "1"])
        fal = set().union(*[sig(p) for i, p in enumerate(P) if q.truth[i] == "0"])
        leak = (ts & tru) - fal - qs_ - allow
        if leak: (block if q.mode == 2 else report["titre_dans_bonnes_reponses"]).append(f"{q.id}: le titre donne la réponse (R11) {sorted(leak)} | T={title(q)}")
        # R11 : un titre de vignette ne nomme ni le diagnostic ni la situation : aucune racine commune avec une proposition, bonne ou mauvaise
        if q.vign and q.titre and "R11" not in q.ok:   # le titre par défaut (TITRE_VIGNETTE) est neutre
            vl = (roots(title(q)) & roots(" ".join(P))) - roots(Q)
            if vl: block.append(f"{q.id}: titre de vignette qui nomme une proposition (R11) {sorted(vl)} | T={title(q)}")
        # M8 / M11 : propositions composées
        PP = [parts(p) for p in P]
        if all(len(x) >= 2 for x in PP):
            same = len({len(x) for x in PP}) == 1
            if q.mode == 2 and "M8" not in q.ok:
                k_ = q.truth.index("1"); key = PP[k_]
                # composant par composant : la bonne valeur n'est jamais la seule plus fréquente
                for j in range(len(key) if same else 0):
                    c = collections.Counter(x[j] for x in PP)
                    if len(c) == 1: continue
                    if c[key[j]] > 1 and c[key[j]] == max(c.values()) and list(c.values()).count(c[key[j]]) == 1:
                        block.append(f"{q.id}: composant {j+1} de la bonne réponse le plus fréquent (M8) : {key[j]}")
                # vote majoritaire : la bonne réponse n'est pas la seule à réunir les éléments les plus fréquents
                c = collections.Counter(e for x in PP for e in set(x))
                sc = [sum(c[e] for e in set(x)) / len(set(x)) for x in PP]
                if sc[k_] == max(sc) and sc.count(max(sc)) == 1 and c.most_common(1)[0][1] > 1:
                    block.append(f"{q.id}: la bonne réponse réunit les éléments majoritaires (M8, vote) : {strip(P[k_])}")
            # 2 × 2 : chaque élément qui varie ne prend que 2 valeurs → choix binaires devinables
            if same and "M11" not in q.ok:
                var = [n for n in (len({x[j] for x in PP}) for j in range(len(PP[0]))) if n > 1]
                if len(var) >= 2 and all(n == 2 for n in var):
                    block.append(f"{q.id}: propositions composées à 2 valeurs par élément (M11) : {' | '.join(strip(p) for p in P)}")
        # X1 : chaque proposition, vraie ou fausse, est justifiée en une ligne (champ why, cité avec sa proposition)
        if "X1" not in q.ok and (len(q.why) != 4 or not all(str(w_).strip() for w_ in q.why)):
            block.append(f"{q.id}: justification manquante pour une ou plusieurs propositions (X1) : why={len(q.why)}/4")
        # M9 : pourcentages d'une répartition = 100
        for p_ in P:
            pc = [float(x.replace(",", ".")) for x in re.findall(r"(\d+(?:,\d+)?)\s*%", p_)]
            if len(pc) >= 3 and "répartition" in Q.lower() and abs(sum(pc) - 100) > 0.5:
                block.append(f"{q.id}: répartition qui ne totalise pas 100 % (M9) : {p_}")
        # X3 : tout sigle des propositions, de l'énoncé et de l'explication est défini dans le glossaire
        from glossaire import _C as _GC
        txt = " ".join([Q, *P, q.expl])
        for sg in set(re.findall(r"\b[A-Z][A-Za-z0-9]*[A-Z][A-Za-z0-9]*\b", txt)):
            if sg in SIGLES_OK: continue
            if not any(rx.search(sg) for _t, rx, _d, _s in _GC): block.append(f"{q.id}: sigle non défini dans le glossaire (X3) : {sg}")
        # longueur de la bonne réponse (QCS)
        if q.mode == 2 and not q.lenok:
            key = len(P[q.truth.index("1")]); m = st.mean(len(p) for i, p in enumerate(P) if q.truth[i] == "0")
            if m >= 12 and key > 1.3 * m:
                block.append(f"{q.id}: bonne réponse trop longue {key} vs moyenne {m:.0f} : {P[q.truth.index('1')]}")
            elif m >= 12 and key < 0.7 * m:
                report["cle_courte"].append(q.id)
        # termes vagues
        if q.mode == 0 and any(re.search(VAGUE, p, re.I) for p in P): block.append(f"{q.id}: terme vague en Kprim")
        elif any(re.search(VAGUE, p, re.I) for p in P): report["vague"].append(q.id)
        # absolus uniquement dans les fausses
        f_abs = any(re.search(ABS, p, re.I) and q.truth[i] == "0" for i, p in enumerate(P))
        t_abs = any(re.search(ABS, p, re.I) and q.truth[i] == "1" for i, p in enumerate(P))
        if f_abs and not t_abs: report["absolus_faux_seulement"].append(q.id)
        # R7 : mot de l'énoncé (comparé par racine) repris seulement dans les bonnes réponses, tous formats
        if "0" in q.truth and "1" in q.truth and "R7" not in q.ok:
            tr_ = set().union(*[roots(p) for i, p in enumerate(P) if q.truth[i] == "1"])
            fr_ = set().union(*[roots(p) for i, p in enumerate(P) if q.truth[i] == "0"])
            clue = ((roots(Q) - DOM_ROOTS) & tr_) - fr_
            if clue: block.append(f"{q.id}: mot de l'énoncé repris seulement dans les bonnes réponses (R7) {sorted(clue)} : {Q}")
        # X3 : mots techniques sans entrée de glossaire, y compris dans les définitions affichées (signalés)
        segs = [q.q, *P, q.expl, *map(str, q.why), q.x or ""]
        txt3 = " ".join(segs)
        nd = set().union(*map(a_definir, segs))
        for t_, d_, s_ in gloss(txt3): nd |= a_definir(d_)
        if nd: report["X3_termes_sans_definition"].append(f"{q.id}:{sorted(nd)}")
        gq = gloss(txt3)
        dup = [f"{t1} ≈ {t2}" for t1, d1, _ in gq for t2, d2, _ in gq if t1 != t2 and t1.isupper()   # sigle et terme complet qui se définissent l'un l'autre
               and d1.lower().startswith(t2.lower()) and re.search(rf"\b{re.escape(t1)}\b", d2)]
        if dup: report["X3_doublons_glossaire"].append(f"{q.id}:{dup}")
        if q.expl.count(";") >= 2 and "<br>" not in q.expl: report["X1_liste_sur_une_ligne"].append(q.id)   # R-28 : une ligne par élément
        if q.ok: report["exceptions"].append(f"{q.id}:{q.ok}")
    # R5 : un attribut souligné seul (gravité, terrain…) vaut pour plusieurs maladies : souligner aussi le sujet
    for q in QS:
        und = re.findall(r"<u>(.*?)</u>", q.q)
        if len(und) == 1 and re.match(ATTRIBUTS, strip(und[0]), re.I) and "R5" not in q.ok:
            block.append(f"{q.id}: attribut souligné sans son sujet (R5) : {strip(qtext(q))}")
    # soulignement des mots discriminants
    toks = {q.id: re.findall(r"\w+", strip(qtext(q)).lower()) for q in QS}
    for i, q in enumerate(QS):
        for q2 in QS[i + 1:]:
            A, B = toks[q.id], toks[q2.id]
            if len(A) == len(B) and len(A) >= 5:
                diff = [j for j in range(len(A)) if A[j] != B[j]]
                if 1 <= len(diff) <= 2 and len(diff) <= len(A) / 3:
                    for qq, T in ((q, A), (q2, B)):
                        und = " ".join(re.findall(r"<u>(.*?)</u>", qq.q)).lower()
                        miss = [T[j] for j in diff if T[j] not in und]
                        if miss: block.append(f"{qq.id}: mot discriminant non souligné {miss} (voisine {q2.id if qq is q else q.id})")
    # couverture
    cov = collections.defaultdict(list)
    for q in QS:
        for kid in q.ks: cov[kid].append(q.id)
    miss = [k[0] for k in K if not cov[k[0]]]
    if miss: block.append("Connaissances sans question : " + ", ".join(miss))
    return block, report, cov

def importance(q):
    lv = min(KD[k][2] for k in q.ks)
    return min(lv, 1) if q.dz else lv   # P7 (D54) : ⛔ ⇒ au moins I1

block, report, cov = checks()
if block:
    print("BLOQUANT :", len(block)); print("\n".join(block))
    par = collections.defaultdict(set)   # nombre de cartes bloquées par règle
    for b in block: par[(re.findall(r"\(([A-Z]\d+)", b) or ["autre"])[-1]].add(b.split(":")[0])
    print("Cartes bloquées par règle :", {r_: len(v) for r_, v in sorted(par.items())})
    sys.exit(1)

# ---------- statistiques ----------
N = len(QS)
fmt = collections.Counter(q.mode for q in QS)
qcm_n = collections.Counter(q.truth.count("1") for q in QS if q.mode == 1)
kp_n = collections.Counter(q.truth.count("1") for q in QS if q.mode == 0)
imp = collections.Counter(importance(q) for q in QS)
i01 = [q for q in QS if importance(q) <= 1]
vg = sum(1 for q in i01 if q.vign)
stats = {
 "questions": N, "connaissances": len(K),
 "formats": {"QCM": f"{fmt[1]} ({fmt[1]/N:.0%})", "QCS": f"{fmt[2]} ({fmt[2]/N:.0%})", "Kprim": f"{fmt[0]} ({fmt[0]/N:.0%})"},
 "QCM_nb_bonnes": dict(sorted(qcm_n.items())), "Kprim_nb_vraies": dict(sorted(kp_n.items())),
 "importance": {f"I{k}": v for k, v in sorted(imp.items())},
 "vignettes_I0_I1": f"{vg}/{len(i01)} ({vg/len(i01):.0%})", "vignettes_total": sum(q.vign for q in QS),
 "questions_avec_erreur_dangereuse": sum(1 for q in QS if q.dz),
 "rapport": {k: v for k, v in report.items()},
}
print(json.dumps(stats, ensure_ascii=False, indent=1))
if "--report-only" in sys.argv: sys.exit(0)

# ---------- images ----------
import pymupdf
from PIL import Image
os.makedirs(OUT + "/media", exist_ok=True)
doc = pymupdf.open(PDF)
img_name = lambda p: f"{PREFIX}_p{p:03d}.jpg"
def pages(q): return sorted({p for k in q.ks for p in pages_of(k)} | set(q.pg))
used = sorted({p for q in QS for p in pages(q)})
for p in used:
    fn = os.path.join(OUT, "media", img_name(p))
    if not os.path.exists(fn): doc[p - 1].get_pixmap(dpi=150).save(fn, jpg_quality=80)
crops = {}
for q in QS:
    if q.img:
        xref, box, nm = q.img
        pix = pymupdf.Pixmap(doc, xref)
        if pix.n - pix.alpha > 3: pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
        im = Image.frombytes("RGBA" if pix.alpha else "RGB", (pix.width, pix.height), pix.samples).convert("RGB").crop(box)
        fn = f"{PREFIX}_{nm}.jpg"; im.save(os.path.join(OUT, "media", fn), quality=88); crops[q.id] = fn

# ---------- règles du skill appliquées (D55) ----------
SKILL_VERSION = "1.8.1"
ORDRE = "S P C F R V M E X G".split()
def regles(q, g):
    r = {"S1", "R1", "R7", "R8", "M1", "M3", "M12", "X1"}
    r.add({1: "F1", 2: "F2", 0: "F3"}[q.mode])
    if q.mode == 1: r.add("F5")
    if getattr(q, "titre", None) or q.vign: r.add("R11")
    if all(len(parts(p)) >= 2 for p in q.props): r |= {"M8", "M11"}
    if "répartition" in q.q.lower(): r.add("M9")
    if q.vign: r |= {"V1", "V2"}
    if q.dz: r |= {"E1", "P7"}
    if q.x and "✎" in q.x: r.add("S6")
    if q.x and "⚠" in q.x: r.add("S5")
    if q.w: r.add("S3")
    if "<u>" in q.q: r.add("R5")
    if g: r.add("X3")
    if any(u for _t, _d, s in g for _a, u in s): r.add("S8")
    if q.img: r.add("G2")
    if any(re.search(r"\d", p) for p in q.props): r.add("M4")
    if q.id.startswith("V") or re.search(r"d[ée]finition", q.q, re.I): r |= {"M5", "C3"}
    return " · ".join(sorted(r, key=lambda c: (ORDRE.index(c[0]), int(c[1:]))))

# ---------- champs ----------
def fields(q):
    pg = pages(q)
    pr = f"p. {pg[0]}" if len(pg) == 1 else (f"p. {pg[0]}-{pg[-1]}" if pg == list(range(pg[0], pg[-1] + 1)) else "p. " + ", ".join(map(str, pg)))
    info = [q.expl]
    # X1 : une ligne par proposition, citée avec sa justification
    info.append("<br>".join(f"{'✔' if q.truth[i] == '1' else '✘'} <b>{strip(p)}</b> — {w_}" for i, (p, w_) in enumerate(zip(q.props, q.why))))
    for i, why in sorted(q.dz.items()):
        info.append(f"⛔ Erreur dangereuse : « {q.props[i]} » — {why}.")
    if q.x: info.append(q.x)
    g = gloss(" ".join([q.q, *q.props, q.expl, *map(str, q.why), q.x or ""]))  # termes de l'énoncé, des propositions et de l'explication (D50)
    refs = []   # R-27 : sources numérotées dans le glossaire, liste en fin de champ
    def num(s):
        if s not in refs: refs.append(s)
        return str(refs.index(s) + 1)
    if g: info.append("<b>Glossaire</b><br>" + "<br>".join(f"<i>{t}</i> : {d}<sup>{','.join(num(s) for s in src)}</sup>" for t, d, src in g))
    info = ['<div style="text-align:left">' + "<br><br>".join(x for x in info if x) + "</div>"]   # X3 : aligné à gauche (débordement si centré)
    info.append("<br>".join(f'<img src="{img_name(p)}">' for p in pg))
    if refs: info.append("<small>" + "<br>".join(f'{i}. <a href="{u}">{a}</a>' if u else f"{i}. {a}" for i, (a, u) in enumerate(refs, 1)) + "</small>")
    src = [f"{TYPE} — {PDFNAME}, {pr}"] + list(q.w) + [f"Généré par Claude ({MODEL}) — skill v{VERSION} — {DATE} — {q.id}",
                                                       f"Règles du skill qcm-anki-ifsi v{SKILL_VERSION} : {regles(q, g)}"]
    f = {"Question": f"<b>{qtext(q)}</b>{SUFFIX[q.mode]}" + (f'<br><img src="{crops[q.id]}">' if q.id in crops else ""),
         "Titre": title(q), "Mode (0=kprim, 1=qcm, 2=qcu)": str(q.mode), "Réponses (0=faux, 1=vrai)": " ".join(q.truth),
         "Sources": "<br>".join(src), "Contexte": CONTEXTE, "Informations complémentaires": "<br><br>".join(info)}
    for i in range(12): f[f"Réponse {i+1}"] = q.props[i] if i < 4 else ""
    return f, pg

rows = [(q, *fields(q), importance(q)) for q in QS]

# ---------- apkg ----------
from anki.collection import Collection, ImportAnkiPackageRequest, ImportAnkiPackageOptions, ExportAnkiPackageOptions, DeckIdLimit
work = os.path.join(OUT, "work"); shutil.rmtree(work, ignore_errors=True); os.makedirs(work)
col = Collection(os.path.join(work, "c.anki2"))
col.import_anki_package(ImportAnkiPackageRequest(package_path=REF_APKG, options=ImportAnkiPackageOptions(with_scheduling=False)))
col.remove_notes(col.find_notes(""))
m = col.models.by_name("QCMs"); assert m["id"] == 1604570191317
did = col.decks.id(DECK)
for fn in [img_name(p) for p in used] + list(crops.values()):
    assert col.media.add_file(os.path.join(OUT, "media", fn)) == fn
for q, f, pg, imp_ in rows:
    n = col.new_note(m)
    for k_, v in f.items(): n[k_] = v
    n.guid = "ifsiqcm-" + hashlib.sha1(f"{PREFIX}-{q.id}".encode()).hexdigest()[:12]
    n.tags = [f"PSB::Importance::I{imp_}"]
    col.add_note(n, did)
apkg = os.path.join(OUT, BASENAME + ".apkg")
col.export_anki_package(out_path=apkg, options=ExportAnkiPackageOptions(with_scheduling=False, with_media=True, legacy=False), limit=DeckIdLimit(did))
col.close()

# ---------- tsv + couverture ----------
FIELDS = list(rows[0][1].keys())
with open(os.path.join(OUT, BASENAME + " - questions.tsv"), "w", encoding="utf-8") as fh:
    fh.write(f"#separator:tab\n#html:true\n#notetype:QCMs\n#deck:{DECK}\n#tags column:{len(FIELDS)+1}\n")
    for q, f, pg, imp_ in rows: fh.write("\t".join(f[k_] for k_ in FIELDS) + f"\tPSB::Importance::I{imp_}\n")
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
wb = Workbook(); ws = wb.active; ws.title = "Couverture"
ws.append(["K-id", "Page(s)", "Section", "Connaissance", "Importance", "Nb questions", "Questions"])
for k in K: ws.append([k[0], k[1], k[3], k[4], f"I{k[2]}", len(cov[k[0]]), ", ".join(cov[k[0]])])
ws.append([]); ws.append(["Exclus (pas des connaissances)"])
for p, t in EXCLUS: ws.append(["—", p, "", t])
for c in ws[1]: c.font = Font(bold=True, color="FFFFFF"); c.fill = PatternFill("solid", fgColor="2F5496")
for c_, w in zip("ABCDEFG", [8, 9, 26, 80, 11, 12, 30]): ws.column_dimensions[c_].width = w
for r in ws.iter_rows(min_row=2):
    for c in r: c.alignment = Alignment(wrap_text=True, vertical="top")
ws.freeze_panes = "A2"
ws2 = wb.create_sheet("Questions")
ws2.append(["Id", "Importance", "Format", "Vignette", "⛔", "Titre", "Question", "R1", "R2", "R3", "R4", "Réponses", "Connaissances", "Pages"])
for q, f, pg, imp_ in rows:
    ws2.append([q.id, f"I{imp_}", {0: "Kprim", 1: "QCM", 2: "QCS"}[q.mode], "oui" if q.vign else "", "oui" if q.dz else "", title(q), strip(qtext(q)), *q.props, " ".join(q.truth), " ".join(q.ks), ", ".join(map(str, pg))])
for c in ws2[1]: c.font = Font(bold=True)
ws2.freeze_panes = "A2"
wb.save(os.path.join(OUT, BASENAME + " - couverture.xlsx"))
json.dump(stats, open(os.path.join(OUT, "stats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("apkg", os.path.getsize(apkg) // 1024, "Ko")
