# Fusion des dépôts IFSI en un seul : C:\Git\ifsi-tools — prompt pour Claude Code

> Préparé le 2026-11-14 dans la conversation « Skill – conception » (décisions D121 à D124 du journal `Historique et décisions - QCM Anki IFSI.md`). À lancer depuis `C:\Git` dans Claude Code : « Lis ce fichier et exécute-le ».

## Règles pendant tout le travail
- **Ne supprimer aucun fichier ni dossier** hors du nouveau dépôt : copier, jamais déplacer depuis le Drive. À la fin, lister les originaux devenus inutiles, pour que l'étudiant les supprime lui-même.
- Avant chaque étape qui touche à git (renommage, fusion d'historique, push), vérifier que l'arbre de travail est propre (`git status`) et s'arrêter en cas de doute.
- Chaque message qui attend une réponse se termine par le récapitulatif consolidé des points ouverts (D47).
- Interface et documents en français.

## Cible
```
C:\Git\ifsi-tools\                 dépôt git unique, remote GitHub privé renommé ifsi-qcm → ifsi-tools
  CLAUDE.md                        règles communes (voir § 6)
  .gitignore
  skill\
    CLAUDE.md                      rôle « Skill – conception » : modifier le skill, rien d'autre (D93)
    qcm-anki-ifsi\                 le skill : SKILL.md, references\, scripts\ (ce que charge Claude Code, ce que contient le zip)
    tests\                         tests de build.py (ok\, ko\, run_tests.py, make_zip.py)
    docs\                          journal des décisions, journal complet, documents de retours (R-xx), analyses, historique
    dist\                          qcm-anki-ifsi.zip (pour les conversations claude.ai dans le cloud)
  qcm-generation\
    CLAUDE.md                      rôle « génération d'un cours » : générer, corriger, noter les retours ; ne modifie jamais le skill
    cours\<S<n> - <UE> - <Cours>>\ fichiers de travail d'un paquet : cours.py, k.py, q*.py, glossaire_cours.py, sources.md, rapports de relecture
    colleges\                      copie locale des Collèges découpés, EXCLUE DE GIT, sauf _Index des collèges.md (versionné)
  qcm-website\
    CLAUDE.md                      rôle « site QCM »
    (contenu actuel de C:\Git\ifsi-qcm)
```
Restent sur le Drive : les PDF des cours (`G:\Mon Drive\FOR\IFSI\UE\…`, chemin donné dans `cours.py`), les originaux des Collèges, les paquets livrés pour Anki (`G:\Mon Drive\FOR\IFSI\Anki\Decks\…`).

## Étapes

### 1. Préparer les deux dépôts
- `C:\Git\qcm-anki-ifsi` : commiter la v1.9.1 si ce n'est pas fait (« skill v1.9.1 : Collèges comme source (D115-D119), génération dans Claude Code (D120) »), lancer `python tests\run_tests.py` (doit afficher OK et OK glossaire).
- `C:\Git\ifsi-qcm` : commiter ou mettre de côté le travail en cours ; noter la branche et le remote.

### 2. Créer ifsi-tools à partir de ifsi-qcm (historique du site gardé)
- Renommer le dépôt GitHub `ifsi-qcm` en `ifsi-tools` (`gh repo rename` ou Settings) ; GitHub redirige l'ancienne adresse. Mettre à jour le remote local.
- Renommer le dossier `C:\Git\ifsi-qcm` en `C:\Git\ifsi-tools` (si un programme le bloque, cloner le dépôt dans `C:\Git\ifsi-tools` et laisser l'ancien dossier en place).
- `git mv` de tout le contenu du site dans `qcm-website\`. **Avant** : vérifier si Spec Kit (`.specify\`, `specs\`, commandes `/speckit.*`) exige d'être à la racine du dépôt git ; si oui, les laisser à la racine et l'écrire dans `qcm-website\CLAUDE.md`. Les fichiers propres à GitHub (`.github\workflows\`) restent à la racine : adapter leurs chemins pour que **seul `qcm-website` (et ses données) soit publié sur Pages**, jamais `skill\` ni `qcm-generation\`. Adapter `CNAME`, les tests (`node --test`) et `scripts\sync-decks.ps1` aux nouveaux chemins.
- Commit : « Site déplacé dans qcm-website ».

### 3. Intégrer le skill avec son historique (D121, choix A)
- `git subtree add --prefix=skill C:\Git\qcm-anki-ifsi <branche>` (sans `--squash`).
- Réorganiser : `git mv skill\SKILL.md skill\references skill\scripts skill\qcm-anki-ifsi\` ; `skill\tests`, `skill\docs`, `skill\dist` restent. Adapter `tests\run_tests.py` et `tests\make_zip.py` (le zip garde le préfixe `qcm-anki-ifsi/`). Relancer les tests.
- Commit.

### 4. Documents (D123) et dossiers de travail des cours
Copier (sans les retirer du Drive) :
- `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Historique et décisions - QCM Anki IFSI.md` → `skill\docs\` ;
- `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Historique\` (dont `Retours\`, anciennes versions du prompt et du skill, journal complet) → `skill\docs\historique\` ; les documents de retours dans `skill\docs\retours\` ;
- `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Outils\exemple CM6 AVC\` → `qcm-generation\cours\S3 - UE 2.8 - CM6 AVC\` (fichiers .py et .md ; pas les images ni les .apkg) ;
- chaque `G:\Mon Drive\FOR\IFSI\Anki\Decks\<cours>\sources\` → `qcm-generation\cours\<cours>\` (même règle) ; en cas de doublon avec l'exemple AVC, garder le plus récent et le signaler.
Commit.

### 5. Collèges (D122, choix B2)
- Copier `G:\Mon Drive\FOR\Médecine\Arc EXTERNES 👺\Collèges découpés\` dans `qcm-generation\colleges\` (plusieurs Go : prévenir l'étudiant avant, vérifier la place sur le disque ; Google Drive peut devoir télécharger les fichiers). Comparer le nombre de PDF (1 071 attendus) et la taille totale.
- `.gitignore` : `qcm-generation/colleges/*` puis `!qcm-generation/colleges/_Index des collèges.md`. Vérifier avec `git status` qu'aucun PDF n'est suivi.
- Commit (index seulement).

### 6. CLAUDE.md
- Racine : rôle de chaque dossier ; règles communes : récapitulatif consolidé des points ouverts à la fin de chaque message qui attend une réponse (D47) ; toute décision écrite (numéro, décision, pourquoi, qui) dans `skill\docs\Historique et décisions - QCM Anki IFSI.md` avant la fin de la session (D74, D123) ; traçabilité R-xx → Dxx → règle → contrôle (D94) ; une session = un rôle (D93) ; ne jamais supprimer de fichier hors du dépôt sans accord ; rappeler en fin de session de recopier dans le projet Claude « QCM IFSI » les documents de `skill\docs\` modifiés.
- `skill\CLAUDE.md`, `qcm-generation\CLAUDE.md`, `qcm-website\CLAUDE.md` : rôle, ce qui est permis et interdit, commandes utiles (tests, build).

### 7. Skill v1.10 : nouveaux chemins (rôle « Skill – conception »)
Mettre à jour `skill\qcm-anki-ifsi\` (SKILL.md, references\, scripts\) et `skill\tests\` :
- journal des décisions : `C:\Git\ifsi-tools\skill\docs\Historique et décisions - QCM Anki IFSI.md` (+ copie dans le projet Claude) ; plus de copie sur le Drive (D123, révise D74 et D49) ;
- index et chapitres des Collèges : `C:\Git\ifsi-tools\qcm-generation\colleges\` ; dans le cloud, l'original du Drive (S9) ;
- espace de travail d'un cours : `C:\Git\ifsi-tools\qcm-generation\cours\<S<n> - <UE> - <Cours>>\` (remplace `%USERPROFILE%\QCM-travail\`, D120, et `Decks\…\sources\`, D91) ; scripts appelés depuis `skill\qcm-anki-ifsi\scripts\` (plus de copie dans `Outils\`) ;
- livraison inchangée : `.apkg` dans `G:\Mon Drive\FOR\IFSI\Anki\Decks\…` ;
- `SKILL_VERSION = "1.10"`, tests verts, zip reconstruit dans `skill\dist\`.
- Écrire D121-D124 dans le journal s'ils n'y sont pas, ajouter la ligne « skill 1.10 » à la chronologie, mettre à jour § 6 « Emplacements ».
Commit.

### 8. Jonction et dépendances
```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.claude\skills" | Out-Null
New-Item -ItemType Junction -Path "$env:USERPROFILE\.claude\skills\qcm-anki-ifsi" -Target "C:\Git\ifsi-tools\skill\qcm-anki-ifsi"
pip install anki pymupdf openpyxl pillow
```
Vérifier : `Test-Path "$env:USERPROFILE\.claude\skills\qcm-anki-ifsi\SKILL.md"` → True.

### 9. Push et bilan
- `git push` ; vérifier que l'Action de publication passe et que le site publié ne contient ni `skill\` ni `qcm-generation\`.
- Bilan : ce qui a été fait ; originaux devenus inutiles (`C:\Git\qcm-anki-ifsi`, `G:\…\Anki\Prompts\Outils\`, `Historique\`, journal, zip, `Decks\…\sources\`), à supprimer par l'étudiant ; points ouverts.

## Hors de cette fusion (sessions suivantes)
- **D124** — `build.py` écrit directement les données du site (`qcm-website\data\index.json`, `data\<id-cours>\questions.json`, `media\`, format de la section 4 de `Site QCM - entrées Spec Kit.md`) ; le site ne convertit plus les `.apkg` ; `sync-decks.ps1` et la tâche planifiée deviennent inutiles. À faire en deux sessions : « Skill – conception » (export dans `build.py`, tests) puis « Site QCM » (lecture des données, suppression de la conversion et de la synchronisation, mise à jour de la spécification Spec Kit).
