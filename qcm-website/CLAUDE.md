# Rôle « Site QCM »

Site statique de révision des QCM (GitHub Pages, https://ifsi-github.jrouzier.fr). Lire aussi
`../CLAUDE.md` (règles communes) et `README.md` (ajout d'un cours, mot de passe, version).

## Permis
- Tout `qcm-website/` : `site/`, `tools/`, `tests/`, `decks/`, `specs/`, `.specify/`, `.claude/`.
- `../.github/workflows/publier.yml` (l'Action reste à la racine du dépôt).

## Interdit
- Modifier le skill (`../skill/`) ou les fichiers de travail des cours (`../qcm-generation/`).
- Publier autre chose que `qcm-website/site` : l'Action travaille dans `qcm-website/` et ne
  téléverse que `qcm-website/site`.

## Spec Kit
`.specify/` et `specs/` sont dans `qcm-website/`, pas à la racine du dépôt git : les scripts de
Spec Kit trouvent leur racine en remontant jusqu'au dossier `.specify`. Lancer Claude Code (et les
commandes `/speckit.*`) depuis `qcm-website/`.

## Commandes (depuis `qcm-website/`)
```
node --test "tests/*.test.mjs"
uv run --with zstandard python tools/convert_apkg.py
uv run python tools/version.py
uv run python -m http.server 8000 -d site
```
`tools/version.py` ne compte que les commits du site (premier parent, hors `skill/` et
`qcm-generation/`).
