# Rôle « Skill – conception » (D93)

Modifier le skill `qcm-anki-ifsi`, rien d'autre. Lire aussi `../CLAUDE.md` (règles communes).

## Permis
- `qcm-anki-ifsi/` : `SKILL.md`, `references/`, `scripts/` (ce que charge Claude Code par la jonction
  `%USERPROFILE%\.claude\skills\qcm-anki-ifsi`, et ce que contient le zip).
- `tests/` : tests de `build.py` et construction du zip.
- `docs/` : journal des décisions, documents de retours (`retours/`), analyses, `historique/`.

## Interdit
- Générer ou corriger un paquet de cours (rôle « génération d'un cours », `../qcm-generation/`).
- Modifier le site (`../qcm-website/`).

## À chaque évolution
- Une décision Dxx dans le journal (colonne « Règle »), une ligne dans la chronologie, le document de
  retours concerné marqué « intégré en v1.x → règle » (D94).
- `SKILL_VERSION` dans `qcm-anki-ifsi/scripts/build.py`.
- Tests verts, puis zip reconstruit.

## Commandes
```
python tests\run_tests.py     # doit afficher OK puis OK glossaire
python tests\make_zip.py      # dist\qcm-anki-ifsi.zip (conversations claude.ai dans le cloud)
```
