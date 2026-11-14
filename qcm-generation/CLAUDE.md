# Rôle « génération d'un cours » (D93)

Générer un paquet de QCM Anki avec le skill `qcm-anki-ifsi`, le corriger, noter les retours.
Une session par cours. Lire aussi `../CLAUDE.md` (règles communes).

## Permis
- `cours/<S<n> - <UE> - <Cours>>/` : fichiers de travail du cours (`cours.py`, `k.py`, `q*.py`,
  `glossaire_cours.py`, `sources.md`, `refs/`, rapports de relecture).
- Écrire le `.apkg` livré dans `G:\Mon Drive\FOR\IFSI\Anki\Decks\S<n> - <UE> - <Cours>\`.
- Écrire les retours sur le skill (R-xx) dans `../skill/docs/retours/`.
- Décisions propres au cours : journal du cours (D92).

## Interdit
- **Modifier le skill** (`../skill/`, sauf `docs/retours/`) : un problème du skill devient un retour R-xx,
  traité dans une session « Skill – conception ».
- Modifier le site (`../qcm-website/`).
- Modifier `colleges/` : c'est une copie du Drive.

## Collèges
`colleges/` est une copie locale de `G:\Mon Drive\FOR\Médecine\Arc EXTERNES 👺\Collèges découpés\`
(1 087 PDF, un par chapitre). Elle est **exclue de git**, sauf `_Index des collèges.md`. Après une
mise à jour sur le Drive, recopier :
```
robocopy "G:\Mon Drive\FOR\Médecine\Arc EXTERNES 👺\Collèges découpés" colleges /E /XF desktop.ini
```

## Commandes
Scripts du skill appelés depuis `..\skill\qcm-anki-ifsi\scripts\` (voir `references/fichiers.md`).
