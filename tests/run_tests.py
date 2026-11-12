"""Tests de build.py : python run_tests.py (avec anki, pymupdf, openpyxl, pillow installés).
ko/ : chaque contrôle v1.8 bloque la carte attendue ; ok/ : paquet construit, champ Informations complémentaires conforme."""
import os, re, sys, shutil, subprocess, tempfile, collections
HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(HERE, "..", "scripts", "build.py")
run = lambda d, *a: subprocess.run([sys.executable, BUILD, d, *a], capture_output=True, text=True, encoding="utf-8", env={**os.environ, "PYTHONIOENCODING": "utf-8"})

# 1. cartes fautives
r = run(os.path.join(HERE, "ko"), "--report-only")
assert r.returncode == 1, r.stdout + r.stderr
got = collections.defaultdict(set)
for line in r.stdout.splitlines():
    m = re.match(r"(\w+): .*\(([A-Z]\d+)", line)
    if m: got[m.group(2)].add(m.group(1))
want = {"M8": {"B01"}, "R5": {"B01"}, "M11": {"B02"}, "R7": {"B03"}, "X1": {"B03"}, "R11": {"B04"}}
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
a3 = next(v for k, v in rows.items() if "Mme T." in k)
assert "\tCas clinique\t" in a3, a3                                                    # R11 : titre neutre par défaut
assert any(f.endswith(".apkg") for f in os.listdir(os.path.join(ok, "out")))
shutil.rmtree(tmp)
print("OK")
