"""Tests de build.py : python run_tests.py (avec anki, pymupdf, openpyxl, pillow installés).
ko/ : chaque contrôle v1.8 bloque la carte attendue ; ok/ : paquet construit, champ Informations complémentaires conforme."""
import os, re, sys, shutil, subprocess, tempfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "..", "qcm-anki-ifsi", "scripts", "build.py")
run = lambda d, *a: subprocess.run([sys.executable, BUILD, d, *a], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})

# 1. cartes fautives
r = run(os.path.join(HERE, "ko"), "--report-only")
assert r.returncode == 1, r.stdout + r.stderr
got = collections.defaultdict(set)
for line in r.stdout.splitlines():
    m = re.match(r"(\w+): .*\(([A-Z]\d+)", line)
    if m: got[m.group(2)].add(m.group(1))
want = {"M8": {"B01"}, "R5": {"B01"}, "M11": {"B02"}, "R7": {"B03"}, "X1": {"B03"}, "R11": {"B04"}, "S3": {"B05"}, "S9": {"B05"}}
for rule, ids in want.items(): assert got[rule] == ids, (rule, got[rule], r.stdout)

# 2. cartes correctes : construction complète
tmp = tempfile.mkdtemp(); ok = os.path.join(tmp, "ok"); shutil.copytree(os.path.join(HERE, "ok"), ok)
import pymupdf
doc = pymupdf.open(); doc.new_page().insert_text((72, 72), "Cours de test"); doc.save(os.path.join(ok, "test.pdf"))
r = run(ok)
assert r.returncode == 0, r.stdout + r.stderr
tsv = next(f for f in os.listdir(os.path.join(ok, "out")) if f.endswith("questions.tsv"))
rows = {l.split("\t")[0]: l for l in open(os.path.join(ok, "out", tsv), encoding="utf-8") if not l.startswith("#")}
a2 = next(v for k, v in rows.items() if "thrombose" in k.lower() and "Cause" in k)
assert "✔ <b>Thrombophilie</b> — Trouble de la coagulation." in a2 and "✘ <b>Tabagisme isolé</b>" in a2, a2   # X1
assert re.search(r"<i>Thrombophilie</i> : .*?<sup>\d", a2), a2                     # R-27 : renvoi numéroté
assert re.search(r'<small>1\. .*<br>2\. <a href="http', a2), a2                                 # R-27 : liste en fin de champ
assert 'text-align:left' in a2                                                         # glossaire aligné à gauche
src = a2.split("\t")[4]                                                                 # S3, S9, X5 : sources libellées, dans l'ordre cours → cité → Collège → Web
i_cite, i_col, i_web = src.index("(cité par le support de cours, p. 1)"), src.index("Collège — Neurologie, 7e édition, 2025, chap. « Accidents vasculaires cérébraux », item 340, p. 300 du PDF d'origine"), src.index("Web — HAS")
assert src.index("CM IFSI — test.pdf") < i_cite < i_col < i_web, src
SV = re.search(r'SKILL_VERSION = "([^"]+)"', open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "qcm-anki-ifsi", "scripts", "build.py"), encoding="utf-8").read()).group(1)
assert re.search(r"Règles du skill qcm-anki-ifsi v" + re.escape(SV) + " : .*S3.*S9", src), src
a3 = next(v for k, v in rows.items() if "Mme T." in k)
assert "\tCas clinique\t" in a3, a3                                                    # R11 : titre neutre par défaut
assert any(f.endswith(".apkg") for f in os.listdir(os.path.join(ok, "out")))
shutil.rmtree(tmp)
print("OK")

# 3. glossaire commun sans page de cours ; une entrée du cours remplace l'entrée commune du même terme (D108)
sys.path.insert(0, os.path.join(HERE, "..", "qcm-anki-ifsi", "scripts")); import glossaire
try: glossaire._check([("X", "x", "déf.", [("CM1 Test, p. 1", None)])], commun=True); raise AssertionError("page de cours acceptée dans le commun")
except ValueError: pass
glossaire._check([("Y", "y", "déf.", [("Collège — Neurologie, 7e édition, 2025, chap. « AVC », p. 300 du PDF d'origine", None)])], commun=True)   # S9 : Collège permis dans le commun
glossaire.add([("IRM", r"\bIRM\b", "Définition du cours.", [("CM1 Test, p. 2", None)])])
assert [d for t, d, s in glossaire.gloss("une IRM") if t == "IRM"] == ["Définition du cours."]
print("OK glossaire")
