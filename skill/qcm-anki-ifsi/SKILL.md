---
name: qcm-anki-ifsi
description: Génère un paquet Anki de QCM (type QCMs, importance I0-I3, images) à partir d'un cours PDF d'IFSI, avec phase d'analyse, relecture indépendante et contrôles. À utiliser pour créer ou corriger des QCM Anki à partir d'un cours.
---

# QCM Anki à partir d'un cours IFSI — skill v1.10.1

## Rôle
Produire, à partir d'un cours (PDF de diapos + prises de notes), un **paquet Anki `.apkg` prêt à importer** qui couvre **toutes** les connaissances du cours, classées par importance, et qui soit difficile à réussir par simple ruse.
L'étudiant est en 2e année d'IFSI et a très peu de temps : le résultat doit être utilisable sans retouche. Les consignes valent **pour tout cours et toute UE**.

## Fichiers du skill (à lire selon la phase)
- `references/regles.md` — **toutes les règles codées** (S, P, C, F, R, V, M, E, X, G). À lire en entier avant la phase 1 et avant la génération.
- `references/fichiers.md` — espace de travail, format de `k.py`, `Q(...)`, `cours.py`, `glossaire_cours.py`, type de note. À lire avant la phase 2.
- `references/relecture.md` — consignes de la phase 2b.
- `scripts/` — `build.py`, `common.py`, `glossaire.py`, `Type de note QCMs.apkg`. Appelés sur place avec Claude Code, copiés dans l'espace de travail dans le cloud (`references/fichiers.md`).

## Garde-fous
- Le **pourquoi** de chaque règle et l'historique sont dans le journal des décisions, `C:\Git\ifsi-tools\skill\docs\Historique et décisions - QCM Anki IFSI.md` (dans le cloud : projet Claude « QCM IFSI », `claude/QCM Anki - Historique et décisions.md`) : le lire en cas de doute sur une règle.
- **Toute décision prise en conversation y est écrite** (numéro, décision, pourquoi, qui) **avant la fin de la conversation**, dans le journal du dépôt : rien ne doit reposer sur la seule conversation. Ni copie sur le Drive, ni copie dans le projet Claude (D125). Les petites décisions (organisation, livraison, outils, essais abandonnés) vont, avec leur raison, dans le journal complet (`claude/QCM Anki - Journal complet de la conversation.md`, copie dans `skill\docs\historique\`).
- Dossier de l'étudiant : `G:\Mon Drive\FOR\IFSI` (cours dans `UE\Semestre <n>\…`, paquets livrés dans `Anki\Decks\S<n> - <UE> - <Cours>\`).
- Les documents du skill (journal, retours, historique) sont dans le dépôt `C:\Git\ifsi-tools\skill\docs\` ; ne plus rien écrire dans `Anki\Prompts\` du Drive.
- **Environnement** :
  - **Claude Code sur le PC de l'étudiant (environnement par défaut de la génération)** : lire le cours et les notes **sur place** sur le Drive, l'index et les chapitres de Collège dans la copie locale `C:\Git\ifsi-tools\qcm-generation\colleges\`, sans les copier ; extraire le texte et rendre les pages en image avec `pymupdf`. Espace de travail : `C:\Git\ifsi-tools\qcm-generation\cours\<S<n> - <UE> - <Cours>>\`. Lire les documents du dépôt (journal, documents de retours dans `skill\docs\retours\`).
  - **Conversation Claude dans le cloud, liée au PC** : copier dans l'espace de travail les seuls fichiers utiles (cours, chapitres de Collège relevés en phase 1), jamais un dossier entier ; fichier de plus de 400 Mo ou dossier dont le nom contient un emoji : demander à l'étudiant de l'ajouter par « + » → « Ajouter un dossier ».
- Modèle conseillé : Claude Opus (exactitude médicale des mauvaises réponses).
- Codes des règles : lettre de la section + numéro, **jamais réattribués**. Le script écrit dans le champ Sources de chaque carte les règles principales appliquées (X5).

## Processus

### Phase 1 — Analyse (obligatoire, attendre la validation)
Lire tout le cours, puis **relever les sources de travail** une fois pour toute la génération (S3, S9) :
- les **références citées sur les diapos** (étude, recommandation, ouvrage), avec la page ;
- pour **chaque partie du cours**, le ou les **chapitres de Collège** correspondants, trouvés dans l'index : collège, édition, année, type (numérique ou scan + OCR), fichier, pages d'origine. Noter le tableau dans `sources.md` (`references/fichiers.md`) ; dans le cloud, copier ces seuls PDF dans `refs/` du dossier du cours, avec Claude Code les lire sur place Pendant la génération et la relecture, **réutiliser ces chapitres sans rechercher à nouveau** ; le web ne sert qu'aux points que le collège ne couvre pas et aux données récentes (S12).

Faire les vérifications nécessaires (cours, références citées, Collèges, puis web), puis présenter :
- **les variables** :
  - UE, cours, type (`CM SSU`, `CM IFSI` ou `TD`) ;
  - Contexte : `IFSI - UE <n°> <intitulé> - <type> <cours>` ;
  - Paquet : `IFSI::QCM::Semestre <n>::UE <n°> - <intitulé>::<Cours>` ;
- **le plan** du cours, avec les pages ;
- **les sources de travail** : références citées par le cours et chapitres de Collège par partie (tableau de `sources.md`) ;
- **l'inventaire** des connaissances avec leur importance (tableau condensé) ;
- **l'estimation du nombre de questions**, calculée à partir de l'inventaire **détaillé** (aucune limite de volume) ;
- les figures et l'imagerie à exploiter ;
- les situations cliniques envisagées pour les vignettes ;
- **les incohérences, déjà vérifiées** (Collège puis web), avec le traitement proposé, dont les écarts entre un collège ancien et une recommandation plus récente (S12) ;
- **les connaissances des Collèges absentes du cours** qu'il serait utile de ficher, à valider (S11) ;
- les doutes ;
- les questions à l'étudiant, dont le nombre de questions souhaité.

Numérotation : `INC-1…` pour les incohérences, `Q-1…` pour les questions (toutes les décisions attendues sont dans cette liste), `D-1…` pour les doutes. Jamais `I1`, réservé à l'importance.

**Récapitulatif consolidé, à la fin de chaque message qui attend une réponse** (phase 1 et toute la suite de la conversation) :
- L'étudiant ne doit **jamais** avoir à revenir à un message précédent pour savoir à quoi répondre.
- Terminer le message par la liste **complète et à jour** de tous les points ouverts (`INC-`, `Q-`, `D-`), qu'ils viennent de ce message ou des précédents.
- Si l'étudiant ajoute un document (notes, compléments, autre support) : l'analyser, intégrer ses apports à l'inventaire, puis fusionner dans ce même récapitulatif les nouvelles incohérences, questions et doutes qu'il soulève.
- Chaque point **garde son numéro** d'un message à l'autre ; un nouveau point prend le numéro suivant.
- Les points tranchés depuis le dernier récapitulatif sont rappelés une fois, en une ligne, avec la décision retenue (« Q-3 : réglé → 300 questions »), puis retirés.
- Ne poser aucune question en dehors de ce récapitulatif.

### Phase 2 — Génération
1. Inventaire détaillé dans `k.py` (format : `references/fichiers.md`).
2. Questions dans un ou plusieurs fichiers `QS = [Q(...)]`, **dans l'ordre du cours**, en appliquant `references/regles.md`.
3. `cours.py` (et, si besoin, `glossaire_cours.py`).
4. `python <scripts>/build.py <cours> --report-only` (`<scripts>` : `references/fichiers.md`) → corriger jusqu'à **zéro blocage**, puis traiter chaque ligne du rapport (dont `X3_termes_sans_definition`).
5. Audit des listes (C1) : pour chaque connaissance qui est une liste, vérifier que chaque élément est la bonne réponse d'au moins une carte.

### Phase 2b — Relecture indépendante (obligatoire)
Suivre `references/relecture.md` : un relecteur à l'aveugle (répond aux questions) et un relecteur des règles (coche chaque règle importante, carte par carte), sur **toutes** les cartes à chaque génération ou régénération.

### Phase 3 — Livraison
- `python <scripts>/build.py <cours>` produit, dans `<cours>/out/`, le `.apkg`, `- questions.tsv`, `- couverture.xlsx` et `stats.json`.
- **Tester** : réimporter deux fois dans une collection vierge. Vérifier un seul type QCMs, le bon paquet, les images présentes, aucun doublon.
- Déposer tous les fichiers dans `Anki\Decks\S<n> - <UE> - <Cours>\` (semestre en tête, ex. `S3 - UE 2.8 - CM6 AVC`), avec `relecture.md`.
- Faire un résumé : volume, importance, formats, vignettes, ⛔, ✎/⚠, concordance de la relecture, écarts aux cibles.
- Si le paquet remplace une version au contenu différent, dire à l'étudiant de **supprimer l'ancien paquet** avant d'importer.
- Proposer les améliorations du skill tirées des retours.

### Phase 4 — Après usage (2-3 semaines)
Analyser les statistiques Anki exportées par l'étudiant :
- cartes jamais ratées → chercher l'indice ou le distracteur faible ;
- cartes ratées en boucle → chercher l'ambiguïté ou l'erreur.

Corriger et réimporter : les GUID stables conservent la progression.

## Index des règles (texte complet : `references/regles.md`)
- **S — Sources** : S1 PDF = source principale, texte et image · S2 notes = complément · S3 deux ordres de sources (bonnes réponses : cours → références citées par le cours → validé en phase 1 ; tout le reste : Collèges → web) · S4 ne rien inventer · S5 ⚠ non confirmé · S6 ✎ modification tracée · S7 chiffres différents = une question chacun · S8 toute définition hors cours sourcée · S9 Collèges : index, un PDF par chapitre, citation · S10 scan + OCR : chiffres vérifiés sur l'image · S11 le cours fixe le niveau · S12 données récentes : la plus récente l'emporte
- **P — Importance** : P1 I0 · P2 I1 · P3 I2 · P4 I3 · P5 en cas de doute, le plus important · P6 « pas à connaître » = I3 · P7 ⛔ ⇒ au moins I1 · P8 pas d'autres tags · P9 calibrer sur la collection · P10 hiérarchie · P11 transversalité · P12 chiffres · P13 répartition de contrôle
- **C — Couverture** : C1 tout, chaque élément de liste · C2 nombre d'angles · C3 vocabulaire · C4 pas de cas progressifs · C5 contrôle bloquant
- **F — Formats** : F1 QCM · F2 QCS · F3 Kprim · F4 pas de renvoi numéroté · F5 « (s) », définition = QCS · F6 proportions = repères
- **R — Rédaction** : R1 question autonome · R2 titre · R3 question sobre · R4 gras · R5 mot discriminant et sujet soulignés · R6 ancre sémantique · R7 pas d'indice, même racine, tous formats · R8 domaine en tête · R9 pas de provenance · R10 pas de renvoi à une carte · R11 le titre ne donne pas la réponse, vignette à titre neutre · R12 mots sans ambiguïté
- **V — Vignettes** : V1 objectif ≥ 40 % des I0/I1 · V2 crédibilité stricte · V3 vocabulaire technique
- **M — Propositions et mauvaises réponses** : M1 même nature que les bonnes · M2 longueur ≤ 1,3 × · M3 confusion identifiée · M4 chiffres proches · M5 termes proches · M6 absolus · M7 interdits · M8 propositions composées, vote majoritaire · M9 répartitions = 100 % · M10 pas juste ailleurs · M11 pas de schéma 2 × 2 · M12 propositions indépendantes
- **E — Erreurs dangereuses** : E1 ⛔
- **X — Informations complémentaires** : X1 explication, chaque proposition justifiée · X2 ⛔ ✎ ⚠ Complément · X3 glossaire, tout terme inconnu défini · X4 page entière · X5 champ Sources · X6 présentation (une ligne par élément, sources numérotées)
- **G — Images** : G1 page entière · G2 cliché recadré · G3 noms en minuscules
