# Quickstart — validation

Prérequis : Node 22, `uv` (fournit Python).

1. Tests de notation :
   ```
   node --test "tests/*.test.mjs"
   ```
   Attendu : tous verts.
2. Conversion des paquets :
   ```
   uv run --with zstandard python tools/convert_apkg.py
   ```
   Attendu : `site/data/index.json` et un dossier par cours ; un message par cours avec le nombre
   de questions.
3. Site en local :
   ```
   uv run python -m http.server 8000 -d site
   ```
   Ouvrir http://localhost:8000, saisir le mot de passe, cocher CM6 - AVC, 5 questions, lancer,
   répondre, vérifier la correction et le bilan (spec, US1 à US5).
4. Reprise : répondre à 2 questions, fermer l'onglet, rouvrir → « Reprendre ».
5. Publication : push sur `main` → l'Action « Publier » teste, convertit et déploie.
