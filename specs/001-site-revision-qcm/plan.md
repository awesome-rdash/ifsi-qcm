# Implementation Plan: Site de révision QCM IFSI

**Branch**: `001-site-revision-qcm` | **Date**: 2026-11-11 | **Spec**: [spec.md](spec.md)

**Input**: Feature specification from `specs/001-site-revision-qcm/spec.md`

## Summary

Site statique (HTML, CSS, modules ES sans framework) publié sur GitHub Pages. Un script Python
convertit les paquets Anki de `decks/` en JSON léger (`site/data/`) à chaque publication. Le
navigateur charge le catalogue, puis seulement les cours retenus. La notation, le tirage et le bilan
sont des fonctions pures testées avec `node --test`.

## Technical Context

**Language/Version**: JavaScript ES2022 (modules natifs) ; Python 3.12 pour la conversion.

**Primary Dependencies**: aucune côté site ; `zstandard` côté conversion (format `anki21b`).

**Storage**: `localStorage` (connexion, session en cours, historique, préférences), sous try/catch.

**Testing**: `node --test` (Node 22, sans dépendance) pour la notation, le tirage et le bilan ;
la conversion du vrai paquet dans l'Action sert de test de bout en bout du script.

**Target Platform**: navigateurs récents, mobile d'abord (360 px), GitHub Pages.

**Project Type**: site web statique + script de conversion.

**Performance Goals**: accueil < 3 s en 4G ; catalogue < 10 ko ; un cours ≈ 200 ko de JSON.

**Constraints**: aucun service tiers, aucune étape de build pour le code du site, images à la
demande (`loading="lazy"` et pages de cours chargées au clic).

**Scale/Scope**: quelques dizaines de cours de ~300 questions ; une promotion (~100 étudiants).

## Constitution Check

| Principe | Statut |
|---|---|
| I. Fidélité | OK : champs copiés tels quels ; seul l'assainissement HTML retire des balises hors liste blanche. Le surlignage ⛔ ajoute une mise en forme, pas de texte. |
| II. Source unique | OK : `data/` produit depuis `decks/*.apkg`, non versionné. |
| III. Statique | OK. Écart : un module ES et `fetch` ne marchent pas en `file://` ; le site demande un serveur statique, même local (voir research.md R5). |
| IV. Simplicité | OK : 4 fichiers JS, 1 CSS, 1 script Python, 1 dépendance Python. |
| V. Mobile | OK : mise en page une colonne, boutons pleine largeur, `prefers-color-scheme`. |
| VI. Accessibilité | OK : vrais `input`/`label`, `fieldset`/`legend`, focus visible, ✓/✗ + texte. |
| VII. Vie privée | OK : aucune requête hors du site ; bouton « Effacer mes données ». |
| VIII. Mot de passe | OK : empreinte SHA-256 dans `site/js/config.js`. |
| IX. Notation testée | OK : `tests/core.test.mjs`. |
| X. Français | OK. |

## Project Structure

### Documentation (this feature)

```text
specs/001-site-revision-qcm/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/donnees.md
└── tasks.md
```

### Source Code (repository root)

```text
decks/                    # paquets .apkg déposés (source unique)
tools/convert_apkg.py     # .apkg → site/data/
site/                     # racine publiée par Pages
├── index.html
├── CNAME
├── css/app.css
├── js/config.js          # empreinte du mot de passe
├── js/core.js            # notation, tirage, bilan (pur, testé)
├── js/app.js             # écrans, stockage, assainissement
└── data/                 # produit par la conversion, non versionné
tests/core.test.mjs
.github/workflows/publier.yml
```

**Structure Decision**: un seul projet ; `site/` est publié tel quel, `data/` y est ajouté par
l'Action.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Pas d'ouverture depuis le disque (`file://`) | Chargement paresseux des cours par `fetch` (exigé par le plan) | Tout embarquer dans un `.js` : téléchargement complet à chaque visite |
