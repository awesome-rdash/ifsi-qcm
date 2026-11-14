# ifsi-tools

Outils de révision IFSI de l'étudiant : le skill qui génère les QCM Anki, les fichiers de travail
de chaque cours et le site de révision. Interface et documents en français.

## Dossiers
| Dossier | Rôle | Session Claude Code |
|---|---|---|
| `skill/` | le skill `qcm-anki-ifsi` (règles, scripts, tests, journal des décisions) | « Skill – conception » |
| `qcm-generation/` | génération d'un paquet de cours ; copie locale des Collèges | « génération d'un cours » |
| `qcm-website/` | site de révision publié sur GitHub Pages | « Site QCM » |

Chaque dossier a son `CLAUDE.md` : lancer Claude Code **dans** le dossier du rôle.

## Règles communes
- **Une session = un rôle** (D93) : on ne modifie que le dossier de son rôle. Un besoin pour un autre
  rôle s'écrit dans un document de retours (R-xx), jamais dans la seule conversation.
- Chaque message qui attend une réponse se termine par le **récapitulatif consolidé** de tous les
  points ouverts, y compris ceux des messages précédents ; numéros stables (D47).
- Toute décision est écrite (numéro, décision, pourquoi, qui) dans
  `skill/docs/Historique et décisions - QCM Anki IFSI.md` avant la fin de la session (D74, D123).
- Traçabilité : retour R-xx → décision Dxx → règle du skill → contrôle du script (D94).
- Ne jamais supprimer un fichier hors de ce dépôt (Drive, autres dossiers) sans l'accord de l'étudiant :
  copier, jamais déplacer.
- En fin de session : rappeler à l'étudiant de recopier dans le projet Claude « QCM IFSI » les
  documents de `skill/docs/` modifiés.

## Hors du dépôt
- PDF des cours : `G:\Mon Drive\FOR\IFSI\UE\…` (chemin dans le `cours.py` du cours).
- Originaux des Collèges : `G:\Mon Drive\FOR\Médecine\Arc EXTERNES 👺\Collèges découpés\`.
- Paquets livrés pour Anki : `G:\Mon Drive\FOR\IFSI\Anki\Decks\S<n> - <UE> - <Cours>\`.
