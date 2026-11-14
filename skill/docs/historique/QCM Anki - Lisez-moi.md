# QCM Anki IFSI — lisez-moi

> Où se fait quoi, et où trouver quoi. À lire en premier par toute conversation qui travaille sur les QCM Anki.

## Conversations (D93)

| Conversation | Rôle | Écrit dans |
|---|---|---|
| **Skill – conception** (Claude Code, D96) | Modifier le skill `qcm-anki-ifsi` et ses scripts, et rien d'autre | `QCM Anki - Historique et décisions.md` |
| **Une par cours** (ex. « QCM AVC », « QCM BPCO ») | Phase 1, génération, corrections, phase 4 du paquet de ce cours | `QCM Anki - Journal paquet <cours>.md` ; si un défaut vaut pour tous les cours : `QCM Anki - Retours … (R-xx).md` |
| **Site QCM** | Site web de révision | `Site QCM - entrées Spec Kit.md` |

Une conversation de cours ne modifie jamais le skill. Elle écrit ses constats dans un document de retours ; la conversation « Skill – conception » les transforme en règles.

## Documents du projet

| Document | Contenu |
|---|---|
| `QCM Anki - Historique et décisions.md` | Décisions sur le skill (Dxx), avec le pourquoi ; chronologie des versions ; emplacements des fichiers |
| `QCM Anki - Journal paquet CM6 AVC.md`, `… CM2 BPCO.md` | Décisions et déroulé propres à chaque paquet |
| `QCM Anki - Retours paquet AVC (R-1 à R-19).md`, `… v1.7 (R-25 à R-37).md` | Retours de l'étudiant sur les cartes, à transformer en règles |
| `QCM Anki - Journal complet de la conversation.md` | Archive figée de la conversation de conception du 10 au 12/11/2026 (toutes les décisions, même petites) |

## Traçabilité (D94)

Retour R-xx → décision Dxx → règle du skill (ex. M11) → contrôle de `build.py`. Un document de retours indique, pour chaque retour, la version et la règle qui l'ont intégré.

## Fichiers

- Skill : dossier `qcm-anki-ifsi` (D95) — `SKILL.md`, `references/`, `scripts/` ; installé dans Claude par import du zip. Sources, tests et historique git : `C:\Git\qcm-anki-ifsi` (D97), hors Drive.
- Drive : `G:\Mon Drive\FOR\IFSI\Anki\Prompts\` (journal, zip du skill, `Historique\`, `Outils\`) ; paquets dans `Anki\Decks\S<n> - <UE> - <Cours>\`.
