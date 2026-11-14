"""Construit dist/qcm-anki-ifsi.zip (SKILL.md, references/, scripts/) à importer dans Personnaliser → Skills."""
import os, zipfile
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SRC = os.path.join(ROOT, "qcm-anki-ifsi")
out = os.path.join(ROOT, "dist", "qcm-anki-ifsi.zip"); os.makedirs(os.path.dirname(out), exist_ok=True)
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
    for top in ("SKILL.md", "references", "scripts"):
        p = os.path.join(SRC, top)
        files = [p] if os.path.isfile(p) else sorted(os.path.join(d, f) for d, _, fs in os.walk(p) for f in fs if "__pycache__" not in d)
        for f in files: z.write(f, "qcm-anki-ifsi/" + os.path.relpath(f, SRC).replace(os.sep, "/"))
print("\n".join(zipfile.ZipFile(out).namelist()))
