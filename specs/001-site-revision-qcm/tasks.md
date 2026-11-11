# Tasks: Site de révision QCM IFSI

**Input**: [plan.md](plan.md), [spec.md](spec.md), [data-model.md](data-model.md),
[contracts/donnees.md](contracts/donnees.md)

## Phase 1: Setup

- [x] T001 Créer l'arborescence `site/`, `tools/`, `tests/`, `decks/` et `.gitignore` (ignore `site/data/`)
- [x] T002 [P] Créer `site/CNAME` (`ifsi-github.jrouzier.fr`)

## Phase 2: Foundational

- [x] T003 [US8] Script de conversion `.apkg` → JSON dans `tools/convert_apkg.py` (formats anki21b/anki21/anki2, médias JSON/protobuf, contrôle du type QCMs, motif du nom de paquet, importance, images, doublons)
- [x] T004 [P] Notation, note sur 20, tirage, mélange et bilan (fonctions pures) dans `site/js/core.js`
- [x] T005 [P] Tests de `core.js` dans `tests/core.test.mjs` (tous les cas de FR-030 à FR-033, cas limites)
- [x] T006 Page `site/index.html`, styles mobiles et sombres `site/css/app.css`

## Phase 3: US1 — Entrer sur le site (P1)

- [x] T007 [US1] Écran mot de passe, empreinte SHA-256 dans `site/js/config.js`, déconnexion, dans `site/js/app.js`

## Phase 4: US2 — Composer une session (P1)

- [x] T008 [US2] Arbre Semestre → UE → Cours avec cases tri-états, compteurs filtrés par importance, nombres par cours, « appliquer à tous », mode de correction, total, dans `site/js/app.js`
- [x] T009 [US2] Chargement paresseux des cours retenus et tirage dans `site/js/app.js`

## Phase 5: US3 + US4 — Répondre et correction (P1)

- [x] T010 [US3] Écran question (QCS radio, QCM cases, Kprim Vrai/Faux), Valider, Passer, progression
- [x] T011 [US4] Correction par proposition (✓/✗ + texte), points, infos assainies avec ⛔ ✎ ⚠ mis en évidence, sources, page de cours au clic
- [x] T012 [US4] Assainissement HTML par liste blanche dans `site/js/app.js`

## Phase 6: US5 — Bilan (P1)

- [x] T013 [US5] Bilan : note globale, détails semestre/UE/cours (plus faible, plus fort), importance, format, questions ratées avec correction, « Refaire mes erreurs »

## Phase 7: US6 — Reprise (P2)

- [x] T014 [US6] Sauvegarde de la session à chaque réponse, proposition de reprise à l'accueil

## Phase 8: US7 — Historique (P3)

- [x] T015 [US7] Historique (100 derniers bilans), évolution par cours, « Effacer mes données »

## Phase 9: Polish

- [x] T016 GitHub Action `.github/workflows/publier.yml` : tests, conversion, déploiement Pages
- [x] T017 [P] `README.md` : ajouter un cours, lancer en local, changer le mot de passe
- [x] T018 Validation selon [quickstart.md](quickstart.md) sur le paquet réel

## Dependencies

T003 et T004/T005 d'abord ; T006 → T007 → T008/T009 → T010–T012 → T013 → T014 → T015 ; T016–T018
en dernier. MVP = Phases 1 à 6.
