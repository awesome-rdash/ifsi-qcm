# Révisions QCM IFSI

Site statique de révision des QCM d'IFSI générés pour Anki, publié sur
https://ifsi-github.jrouzier.fr par GitHub Pages.

Spécification : [specs/001-site-revision-qcm/](specs/001-site-revision-qcm/spec.md) ·
Principes : [.specify/memory/constitution.md](.specify/memory/constitution.md).

## Ajouter ou mettre à jour un cours

1. Copier le `.apkg` depuis `G:\Mon Drive\FOR\IFSI\Anki\Decks\S<n> - <UE> - <Cours>\` vers `decks/`.
   Pour une nouvelle version d'un cours, supprimer l'ancien `.apkg` (sinon la conversion garde
   le plus récent et l'indique dans le journal).
2. `git add decks` → `git commit` → `git push`. L'Action « Publier » teste, convertit et déploie.

## En local

Prérequis : Node 22 et [uv](https://docs.astral.sh/uv/).

```
node --test "tests/*.test.mjs"
uv run --with zstandard python tools/convert_apkg.py
uv run python -m http.server 8000 -d site
```

Puis ouvrir http://localhost:8000. Le site ne marche pas en ouvrant `index.html` depuis le disque
(les navigateurs bloquent alors le chargement des cours).

## Changer le mot de passe

Le mot de passe n'est jamais écrit dans le dépôt, seulement son empreinte SHA-256 dans
`site/js/config.js`. Calculer l'empreinte (PowerShell) :

```
$p = Read-Host "Mot de passe"; -join ([Security.Cryptography.SHA256]::Create().ComputeHash([Text.Encoding]::UTF8.GetBytes($p.Trim())) | % { $_.ToString("x2") })
```

Remplacer la valeur de `EMPREINTE` par le résultat, commit, push. Tous les appareils sont alors
déconnectés. L'Action refuse de publier tant que l'empreinte vaut `A_DEFINIR`.

## Organisation

- `decks/` : paquets Anki (seule source des questions).
- `tools/convert_apkg.py` : conversion en `site/data/` (non versionné).
- `site/` : le site publié (`js/core.js` notation testée, `js/app.js` écrans).
- `tests/` : tests de la notation (`node --test`).
