# QCM Anki IFSI — journal complet de la conversation de conception

> Ce document garde **toutes** les décisions prises pendant la conversation de conception du skill `qcm-anki-ifsi` (10-12 novembre 2026), y compris les petites : organisation des fichiers, livraison, outils, réglages, ce qui a été essayé et abandonné.
> Les **règles importantes** sont résumées et numérotées (D01…) dans `QCM Anki - Historique et décisions.md`. Ce journal-ci donne le **détail chronologique** : qui a décidé, pourquoi, et si la décision tient toujours.
> Les retours détaillés sur le paquet AVC sont dans `QCM Anki - Retours paquet AVC (R-1 à R-19).md`.

**Légende** (les numéros ne sont pas continus : ils ont été attribués par bloc)
- **Qui** : É = l'étudiant ; C = proposition de Claude acceptée ou appliquée ; T = constat fait lors d'un test.
- **Statut** : ✓ en vigueur ; ↻ remplacée (par la décision indiquée) ; ✗ abandonnée.

---

## 1. Cadrage (10 novembre, matin)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J01 | Créer un système qui transforme chaque PDF de cours en QCM importables dans Anki, en fichant **toutes** les connaissances | Créer et relire les fiches à la main prend trop de temps (2e année d'IFSI, réserviste, secouriste, triathlète) | É | ✓ |
| J02 | 4 niveaux d'importance : 0 instinctif ; 1 quelques secondes ; 2 spécialité ou stage ; 3 propre à l'UE et à l'examen | Réviser selon le contexte (entre les examens, en stage) | É | ↻ J140 (grille D52) puis J160 (D72) |
| J03 | Carte = question (courte ou longue, image possible) + 4 réponses, QCS ou QCM, + champs Source, Contexte, Infos complémentaires avec l'image du PDF | Format de révision voulu | É | ✓ |
| J04 | Par défaut, uniquement le PDF ; web ponctuel sur des sources fiables, ou question à l'étudiant si le PDF ne suffit pas | Rester fidèle au cours, combler ses trous | É | ✓ |
| J05 | Exécution dans Claude avec accès au Drive, livraison d'un fichier prêt à importer | Choix proposé, retenu par l'étudiant | É | ✓ |
| J06 | Type de note : le type existant **QCMs** (add-on Multiple Choice) plutôt qu'un type sur mesure | Déjà utilisé par l'étudiant | É | ✓ |
| J07 | QCS, QCM et Kprim mélangés ; une connaissance peut revenir dans plusieurs formats ; QCS « reconnaître la bonne liste parmi 4 » | Formats de la fac et variété | É | ✓ |
| J08 | **Pas de tags** autres que l'importance (pas de spécialité, de type de source, de « à vérifier ») | « Ne t'occupe pas des tags » | É | ✓ |
| J09 | Nombre de questions selon l'importance ; **aucune limite** ; ~50 pour un cours léger, plus s'il y a du vocabulaire ; on peut demander le volume voulu en phase 1 | Exhaustivité | É | ✓ |
| J10 | Sources : PDF du CM + prises de notes (OneNote ou annotations dans le PDF) + web fiable cité dans le champ Sources | Choix de l'étudiant | É | ✓ |
| J11 | Champs Source et Contexte au même format que dans la collection de l'étudiant | Cohérence avec ses cartes existantes | É | ✓ |
| J12 | Mauvaises réponses : connaissances hors PDF autorisées, très plausibles mais fausses sans ambiguïté | Des distracteurs crédibles demandent plus que le cours | É | ✓ |
| J13 | Cours test : **CM6 AVC** (UE 2.8, S3) | L'étudiant le connaît déjà, il peut juger les cartes | É | ✓ |
| J14 | Modèle conseillé : **Claude Opus** ; Sonnet moins fiable sur les mauvaises réponses médicales, Fable sans gain ici | Exactitude médicale = moins de relecture | C | ✓ |
| J15 | Champs du type QCMs : Question, Titre, Mode (0 Kprim / 1 QCM / 2 QCS), Réponses, Sources, Contexte, Infos complémentaires, Réponse 1 à 12 ; rien après Réponse 12 | Lu dans la collection + réponse de l'étudiant | É | ✓ |
| J16 | Importance stockée en **tag** `PSB::Importance::I0`…`I3` | Tags déjà utilisés par l'étudiant | É | ✓ |
| J17 | Le prompt v1.0 est écrit dans `Anki\Prompts` et remplace v0.1/v0.2 (cartes Basic/Cloze) | Passage aux QCM | C | ↻ J101 (skill) |
| J18 | Rapport de phase 1 : variables, plan, inventaire avec importance, estimation, figures, incohérences, recherches, questions ; puis attente de validation | Valider avant de rédiger | C | ✓ |

## 2. Phase 1 du cours AVC (10 novembre)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J19 | Fautes de frappe corrigées sans trace (urée croate → urée-créatinine, PTCA → TP-TCA, phlébite carcérale → cérébrale…) | Évidentes, sans changement de sens | C, validé É | ✓ |
| J20 | Toute **modification** par rapport au cours est notée dans les infos complémentaires (`✎`) | Savoir ce qui diffère de son cours | É | ✓ |
| J21 | Les vérifications de contenu se font **en phase 1** ; en phase 2, le web ne sert plus qu'aux distracteurs | Valider les corrections avant la rédaction | É | ✓ |
| J22 | Info écrite dans le cours mais non confirmée → **gardée** avec `⚠ Non confirmé` (ex. anémie sévère comme contre-indication à la thrombolyse) | L'examen porte sur le cours, l'étudiant doit connaître l'écart | É | ✓ |
| J23 | Mortalité de l'hématome : 50 % en phase aiguë (note) et 50 % à 6 mois (diapo) sont cohérents → les deux sont gardés, chacun avec son repère de temps | « Si 50 % en phase aiguë, il reste 50 % pour après » | É | ✓ |
| J24 | UNV −20 % (note) et −30 % (diapo) → **2 questions distinctes** | Ce ne sont pas les mêmes chiffres ni les mêmes critères | É | ✓ |
| J25 | Alcool : valeur de la diapo gardée + repère actuel de Santé publique France en `Complément` | Diapo ancienne | É | ✓ |
| J26 | Seuils du NIHSS « pas à connaître par cœur » : quand même fichés en I3, vérifiés en ligne, une question par seuil | Ne rien laisser de côté | É | ✓ |
| J27 | Note « gaucher = hémisphère droit » reformulée ; note « scanner normal = moins de 4h30 » corrigée (`✎`) | Erreurs du cours vérifiées en ligne | C, validé É | ✓ |
| J28 | Cours AVC = CM SSU ; paquet, contexte et importances proposés validés ; images d'imagerie dans la question | Réponses de l'étudiant | É | ✓ |
| J29 | Pas de message grand public « VITE » (absent du cours) | Rester sur le cours | É | ✓ |
| J30 | Rapport numéroté **INC-** / **Q-** / **D-** ; toute décision attendue, dont le nombre de cartes, est dans la liste Q- | Répondre sans ambiguïté | É | ✓ |
| J31 | Le prompt garde un historique de versions en tête | Traçabilité | C | ↻ J101 (journal séparé) |

## 3. Livraison et premier paquet (10 novembre)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J32 | Images **intégrées au .apkg** (Anki les range lui-même) plutôt qu'en base64 ou copiées à la main | Base64 : ~30 Mo de texte, édition pénible ; copie manuelle : travail en plus | É (idée) + C | ✓ |
| J33 | Le .apkg contient **exactement** le type de note QCMs de l'étudiant (même id), récupéré une fois depuis un export d'une note | Sinon Anki crée une copie « QCMs-1 » | C | ✓ |
| J34 | Un seul .apkg par cours, import en double-clic | Simplicité | C | ✓ |
| J35 | Chaque connaissance a **au moins une question**, I3 compris ; seuls les objectifs et les illustrations décoratives sont exclus | Question de l'étudiant sur la couverture | É + C | ✓ |
| J36 | **Contrôle de couverture bloquant** + tableau connaissance → page → questions joint au paquet | « Pour que tu n'aies pas à me croire sur parole » | C, validé É | ✓ |
| J37 | Estimer le volume à partir de l'**inventaire détaillé** | 180 questions estimées, 267 produites | T | ✓ |
| J38 | Pas d'image de page dans la question quand ses légendes donnent la réponse ; la page entière reste dans les infos complémentaires | Légendes « Hyperdensité », « Ne pas traiter » | T | ✓ |
| J39 | Test de réimport dans une collection contenant le type QCMs : bon type, images, tags | Vérifier avant de livrer | T | ✓ |
| J40 | Explications **sans renvoi par numéro** de proposition | L'add-on mélange les propositions | T | ✓ |
| J41 | Noms d'images **en minuscules** | Anki met les noms en minuscules ; sinon l'image ne s'affiche plus | T | ✓ |
| J42 | `Type de note QCMs.apkg` et scripts de construction rangés dans `Anki\Prompts\Outils\` | Reproduire la chaîne sur les cours suivants | C | ↻ J120 (type de note dans `exemple CM6 AVC`) |
| J43 | **Recadrage autorisé** pour les questions d'imagerie | Demande de l'étudiant | É | ✓ |
| J44 | Recadrage sur le cliché seul, depuis l'image source du PDF ; ni titre ni légende ; flèche sans texte tolérée ; vérifié à l'œil ; cliché coupé ou illisible écarté | Ne pas donner la réponse, rester lisible | C | ✓ |
| J45 | Nom des clichés : `<ue>_<cours>_img-<description>.jpg` | Noms uniques et stables | C | ✓ |
| J46 | « J'aime bien les QCM générés » ; paquet Anki rangé en `IFSI::QCM::Semestre <n>::UE <n°> - <intitulé>::<Cours>` | Choix de l'étudiant | É | ✓ |
| J47 | Après un changement de paquet, déplacer les cartes déjà importées (Changer de paquet) | La réimportation ne change pas le paquet d'une carte | C | ✓ |

## 4. Vocabulaire, glossaire, chiffres (10 novembre)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J48 | **Glossaire** en bas de chaque carte **et** questions de vocabulaire dédiées pour les termes non définis par le cours | « Les définitions de ces mots » manquaient (athérome, lacune…) | É | ✓ |
| J49 | Questions de définition : mauvaises réponses = définitions de **mots proches** | Demande de l'étudiant | É | ✓ |
| J50 | Définitions hors cours marquées « Complément : définition hors cours » ; termes en section Vocabulaire (V01…) | Savoir ce qui ne vient pas du cours | C | ✓ (sources : J146) |
| J51 | Distracteurs chiffrés **proches** entre eux (« c'est plus dur si les chiffres sont similaires ») | Demande de l'étudiant | É | ✓ |
| J52 | Valeurs proches ou mêmes valeurs permutées ; jamais aberrantes ; jamais une valeur juste selon une autre source (ex. HbA1c < 7 % HAS) | Un distracteur doit être faux sans ambiguïté | C | ✓ |
| J53 | Glossaire automatique (`glossaire.py` : terme → motif → définition) appliqué à toutes les cartes | Ne rien oublier, ne pas écrire à la main | C | ✓ |
| J54 | **GUID stables** (`ifsiqcm-` + hash) ; test de double import ; versions antérieures à supprimer une fois | Réimporter met à jour au lieu de créer des doublons | T + C | ✓ |

## 5. Audit « jury d'examen » et prompt v1.1 (10 novembre, soir)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J55 | Prompt montré en entier sur demande | Demande de l'étudiant | É | ✓ |
| J56 | Audit « jury » : chercher les bonnes pratiques et **proposer sans modifier** le prompt | Demande de l'étudiant | É | ✓ |
| J57 | Références : NBME, 31 règles de Haladyna, guides McGill, Ottawa, Lorraine ; audit automatique du paquet | Comparer à des standards reconnus | C | ✓ |
| J58 | Vignettes oui, mais **crédibles** : présentation typique, réponse issue d'une phrase du cours, pas d'interprétation de Claude | « Attention à ne pas faire des cas incorrects » | É | ✓ |
| J59 | La bonne réponse ne se distingue pas par la forme ; les mauvaises ressemblent aux bonnes | 92 QCS sur 208 avaient une bonne réponse plus longue | É | ✓ |
| J60 | Termes absolus permis comme pièges, mais pas comme indice | « Ça peut être des pièges, mais attention » | É | ✓ |
| J61 | Position de la bonne réponse : non traitée | L'add-on mélange les propositions | É | ✓ |
| J62 | Chaque mauvaise réponse cible une confusion ; test du bon sens | Proposition validée | É | ✓ |
| J63 | Pas de règle « l'énoncé doit se lire sans les propositions » | Le but est des QCM rapides ; les cartes détaillées servent au rappel | É | ✓ |
| J64 | Fuites entre questions : non traitées | Anki mélange les cartes | É | ✓ |
| J65 | `⛔` erreurs dangereuses signalées ; question en I0 | Équivalent des réponses inacceptables de l'EDN | É | ↻ J142 (au moins I1) |
| J66 | Phase 4 : analyse des statistiques Anki après 2-3 semaines | Repérer les cartes trop faciles ou ambiguës | É | ✓ |
| J67 | **Phase 2b** : sous-agent séparé qui répond sans les clés et vérifie l'exactitude médicale | Ne pas noter son propre travail | É | ✓ |
| J68 | Mélange des propositions gardé | « Ça m'évite d'avoir une mémoire visuelle » | É | ✓ |
| J69 | Proportions de formats : s'appuyer sur les recommandations (EDN) | L'étudiant ne sait pas trancher | É | ✓ |
| J70 | Pas de mini-cas progressifs | Les cartes sont affichées dans un ordre aléatoire | É | ✓ |
| J71 | Repères : EDN dominé par les QRM ; questions à réponse unique plus faciles et sujettes aux indices ; pas de proportion officielle | Recherche (CNG, littérature) | C | ✓ |
| J72 | Kprim supprimé (absent des examens de la fac) | Réponse de l'étudiant au point 8 | É | ↻ J79 |
| J73 | Vignettes ≥ 40 % des I0/I1, gabarits orientés rôle infirmier ; en cas de doute, pas de vignette | Tester l'application, pas seulement le rappel | C | ✓ (cible : J156) |
| J74 | Longueur de la bonne réponse : contrôle automatique | Indice le plus classique | C | ↻ J91 (seuil ajusté) |
| J75 | Termes de fréquence vagues (« souvent », « peut ») à éviter | Ambiguïté | C | ✓ |
| J76 | Discordances de la relecture corrigées ou justifiées dans `relecture.md` | Traçabilité | C | ✓ |
| J77 | Énoncé de type étiquette accepté ; titre et contexte affichés au recto ne contiennent jamais la réponse | Révision rapide | C | ✓ |
| J78 | Nouvelle version du prompt = nouveau fichier, l'ancienne est gardée | Pouvoir comparer | C | ✓ |
| J79 | **Kprim réintégré** en minorité : QCM ≈ 50 %, QCS 35-40 %, Kprim 10-15 % ; règles strictes (affirmations absolument vraies ou fausses, pas de terme vague, même objet, 0 à 4 vraies) | « J'aimais bien les Kprim, ça change » | É | ✓ (cibles : J156) |
| J80 | Ne rien lancer avant d'avoir reçu tous les retours | « Attends, j'ai d'autres retours » | É | ✓ |

## 6. Retours sur téléphone et prompt v1.2 (10 novembre, soir)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J81 | Pas de triple répétition contexte / titre / question | Carte « AVC — Épidémiologie — Épidémiologie » | É | ↻ J136 (l'autonomie de la question prime) |
| J82 | **Question en gras**, titre discret | « En gras mettre la question, pas le titre » | É | ✓ |
| J83 | Le gras du titre vient du modèle de carte : réglage CSS à faire **une fois** par l'étudiant ; « yes / no » du Kprim → « Vrai / Faux » | Le paquet ne doit jamais modifier le type de note, partagé avec d'autres paquets | C | ✓ (à faire par l'étudiant) |
| J84 | **Mot discriminant souligné** quand des cartes ne diffèrent que d'un mot, ou pour un mot décisif ; deux mots au plus | Ex. lobe <u>pariétal</u> ; habitude de l'étudiant | É | ✓ |
| J85 | Consignes **générales**, exemples variés (pharmaco, cardio, diabéto…), au plus un exemple AVC | « Toutes les consignes doivent être générales » | É | ✓ |
| J86 | Changements du prompt montrés **façon git** (page HTML colorée + fichier `.diff` dans `Historique\`) | Demande de l'étudiant | É + C | ✓ |
| J87 | « Régénère » le paquet AVC avec la v1.2 | Demande de l'étudiant | É | ✓ |
| J88 | Questions réparties en fichiers r1-r4 ; corrections dans des dictionnaires appliqués par le script (`fixprops.py`) | Corriger sans réécrire | C | ✓ |
| J89 | Relecture 2b par **3 sous-agents** (lots de ~100, dossier sans clés ni sources) ; 298/300 concordants ; ~40 questions corrigées | Taille du paquet | C | ✓ |
| J90 | Signalements gardés volontairement et justifiés (anémie ⚠, NIHSS ✎, alcool, ⛔ volontaires) | Décisions déjà prises en phase 1 | C | ✓ |
| J91 | Contrôle de longueur : bloque seulement une bonne réponse > 1,3 × la moyenne des mauvaises (si ≥ 12 caractères) ; une bonne réponse plus courte est seulement signalée | Faux positifs au test | T | ✓ |
| J92 | Avant d'importer une version au contenu réécrit sur les mêmes identifiants, supprimer l'ancien paquet | Sinon la progression passe sur une autre question | C | ✓ |
| J93 | Écarts aux cibles (formats 34/53/13, vignettes 22 %) signalés plutôt que forcés | Faits uniques → QCS ; vignettes seulement si étayées | C | ✓ (voir J156) |

## 7. Skill, journal, archivage (10 novembre, nuit)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J94 | Un document retrace **toutes les décisions et l'historique** | Alléger le prompt | É | ✓ |
| J95 | En sortie : un **skill Claude** | « Ce sera plus simple » | É | ✓ |
| J96 | Le skill ne garde que le « quoi faire » ; le « pourquoi » vit dans le journal | Skill court | C | ✓ |
| J97 | Script de construction **générique** (`build.py`) + un `cours.py` de paramètres par cours ; vérifié identique à l'ancien | Réutiliser sur tous les cours | C | ✓ |
| J98 | Journal dans le Drive **et** dans le projet Claude | Accessible partout | C | ✓ |
| J99 | Les tests de génération se feront dans d'autres conversations (reliées au PC, avec Opus) | Choix de l'étudiant | É | ✓ |
| J100 | Copie du skill et exemple complet (`Outils\exemple CM6 AVC\`) dans le Drive | Reproduire | C | ✓ |
| J101 | Le prompt devient le skill `qcm-anki-ifsi` ; le prompt v1.2 part dans `Historique\` | Un seul support | C | ✓ |
| J102 | Anciens fichiers 2025 dans `Anki\Archive 2025\` ; versions remplacées en 2026 dans les dossiers `Historique` | « Transfère tous les anciens trucs dans une archive 2025 » | É + C | ✓ |
| J103 | Fichiers > ~25 Mo et suppressions impossibles par Claude → liste de gestes manuels fournie | Limite du pont avec le PC | T | ✓ |
| J104 | Skill emballé en `qcm-anki-ifsi.zip` (dans `Anki\Prompts`) ; installation via Personnaliser → Skills si la carte échoue ; exécution de code requise | Le skill n'apparaissait pas : jamais enregistré | C | ✓ |
| J105 | Claude ne peut pas installer seul un skill : l'étudiant valide la carte « Enregistrer » | Règle de la plateforme | C | ✓ |
| J106 | Structure de travail d'un cours : `k.py` (inventaire, EXCLUS), fichiers de questions, `cours.py`, `glossaire_cours.py` optionnel ; `build.py --report-only` jusqu'à zéro blocage | Méthode reproductible | C | ✓ |
| J107 | Catégories de signalement des relecteurs : erreur médicale, ambigu, hors cours, vignette non crédible, distracteur faible, indice, formulation | Comparer les relectures | C | ✓ |
| J108 | **Récapitulatif consolidé** de tous les points ouverts à la fin de chaque message qui attend une réponse ; numéros stables ; points tranchés rappelés une fois ; aucune question en dehors | « Je ne dois pas avoir à switcher entre deux messages » | É | ✓ (D47) |
| J109 | À chaque mise à jour du skill : carte à enregistrer + copie du SKILL.md + zip + journal (Drive et projet) | Garder tout synchronisé | C | ✓ |

## 8. Rangement de `Anki\Prompts` (10-11 novembre)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J110 | Racine de `Anki\Prompts` minimale : anciennes versions dans `Historique\`, type de note dans l'exemple | « Beaucoup trop de choses » | É | ✓ (D49) |
| J111 | Dossier de sortie dans `Anki\Decks` **avec le semestre** dans le nom | Retrouver les paquets par semestre | É | ✓ |
| J112 | Rangement par l'Explorateur Windows (clics seulement) | Seul moyen de supprimer | C | ✗ trop lent (« ça me saoule ») |
| J113 | Le pont ne sait que lire et écrire des copies ; Claude écrit les copies, l'étudiant supprime les originaux | Limite constatée | T | ✓ |
| J114 | Racine cible : `Historique\`, `Outils\`, le journal, le zip du skill | Racine minimale | C | ✓ |
| J115 | Ancien SKILL.md gardé dans `Historique\` sous un nom versionné | Historique des versions | C | ✓ |
| J116 | Extension Filesystem (déplacement de fichiers) activée par l'étudiant | Éviter l'Explorateur | É | ✗ elle reste limitée à `C:\Git\anki-psb-rebuild` |
| J117 | Si un jour Filesystem marche : regrouper les doublons dans `_à supprimer` | Elle ne sait pas supprimer | C | en attente |
| J118 | **D48** : dossier `Anki\Decks\S<n> - <UE> - <Cours>\` (ex. `S3 - UE 2.8 - CM6 AVC`) | « Premier nom » | É | ✓ |
| J119 | Renommage du dossier AVC existant fait par l'étudiant | Claude ne peut pas renommer | C | ✓ |
| J120 | Type de note de référence dans `Outils\exemple CM6 AVC\` | Racine minimale | É + C | ✓ |
| J121 | Renommer la conversation : impossible pour Claude ; nom suggéré « Skill QCM Anki IFSI – conception (AVC test) » | Pas d'outil | C | à faire par l'étudiant |
| J122 | Vérifier que le skill installé est la dernière version en le comparant à la copie synchronisée ; D47 manquait → nouvelle carte | Question de l'étudiant | É + C | ✓ |

## 9. Retours sur les cartes (11 novembre)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J130 | **Glossaire : un terme, une définition, une ligne** ; termes de l'explication inclus ; entrée groupée bloquante | « Hypoesthésie / paresthésie » lus comme des synonymes | É | ✓ (D50) |
| J131 | En vocabulaire, l'explication nomme le terme de chaque mauvaise proposition | Pour que le glossaire les définisse tous | C | ✓ |
| J132 | Importer directement les versions corrigées (GUID stables) ; reprendre aussi le nouveau `questions.tsv` si un site de révision le lit | Mise à jour sans doublon | C | ✓ |
| J136 | **La question se comprend seule** (nomme la maladie, la situation, l'objet) ; l'autonomie prime sur la non-répétition | « Si on traite quoi ? » | É | ✓ (D51) |
| J140 | Grille d'importance : I0 réflexe vital ; I1 vital non réflexe, souvent transversal ; I2 important non vital ; I3 examen | « Hémiplégie droite → hémisphère gauche : ça ne me sert pas à grand-chose » ; rappels anatomiques → I2 | É | ↻ J160 (affinée par la collection) |
| J141 | Vital, propre au cours, non réflexe (ex. contre-indications à la thrombolyse) → I1 | Réponse de l'étudiant | É | ✓ (D53) |
| J142 | `⛔` ⇒ **au moins I1** (I0 seulement si réflexe) | Trop de cartes en I0 | É | ✓ (D54) |
| J143 | Calibrer l'importance sur les cartes déjà taguées de la collection | Proposition de l'étudiant | É | ✓ (fait le 12/11 : J160) |
| J146 | **Toute définition ou tout complément hors cours porte sa source** (organisme, URL) ; seules les sources effectivement lues sont citées | « Je veux la source de la définition » | É | ✓ (D55) |
| J147 | Règles du skill **numérotées** ; codes jamais réattribués ; règles principales listées dans le champ Sources avec la version du skill | « Je veux les numéros des règles principales » | É | ✓ (D56) |
| J148 | 24 retours R-1 à R-24 transformés en règles générales (D57-D69) : domaine en tête (« AVC – »), pas de provenance, pas de renvoi à une autre carte, titre neutre, mots sans ambiguïté, « (s) » en QCM, propositions composées équilibrées, répartitions à 100 %, distracteurs faux partout, glossaire des mauvaises réponses avec leur intérêt, sigles définis, chaque élément de liste testé, vocabulaire hors cours dans le paquet du cours, vocabulaire technique dans les vignettes | Retours de l'étudiant (détail : doc « Retours paquet AVC ») | É | ✓ |
| J149 | Réponses aux choix : préfixe « AVC – » ; grille OK avec D53 = I1 ; ⛔ ⇒ au moins I1 ; vocabulaire hors cours dans le paquet du cours | Choix de l'étudiant | É | ✓ |
| J150 | Relecture à l'aveugle de la v1.6 : 3 erreurs de clé trouvées (E09, H33, H34) et corrigées | Nouvelles propositions vraies sans mise à jour de la clé | T | ✓ |
| J151 | Paquet AVC v1.6 : 343 questions, 118 termes de glossaire sourcés, zéro blocage, double import OK | Résultat | T | ✓ |

## 10. 12 novembre

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J155 | Lire la collection dans Anki pour calibrer l'importance (« passe par Anki toi-même ») | Demande de l'étudiant | É | ✓ fait via l'export (J160) |
| J156 | **Pas de QCM créés seulement pour atteindre une proportion** ; les proportions sont des repères (règle F6) | « Pas besoin de faire des QCM pour faire des QCM si ça n'apporte rien » | É | ✓ (D71) |
| J157 | Importer et synchroniser le paquet AVC | Demande de l'étudiant | É | en attente : écrans noirs (PC verrouillé) ; le paquet v1.6 (343 notes) est déjà dans la collection exportée le 12/11 |
| J158 | Schéma du skill : phases, vérifications, sous-agents | Demande de l'étudiant | É | ✓ |
| J159 | Les décisions ne reposent jamais sur la seule conversation : elles sont écrites (numéro, décision, pourquoi, qui) dans le journal du projet « QCM IFSI » et dans la copie du Drive, avant la fin de la conversation | « Je veux que les décisions de ce chat ne soient pas uniquement portées par la conversation » | É | ✓ (D74) |
| J160 | Grille d'importance **calibrée sur la collection** (87 cartes taguées I0-I3, 772 cartes `Priorité::P0-P3`, paquets `_🌟Important`) : I0 = à avoir en tête en permanence (réflexe vital, normes du quotidien, carte d'identité de la maladie, bases réglementaires) ; I1 = cœur du cours ; I2 = comprendre et détailler ; I3 = examen | Demande de l'étudiant ; détail dans le journal principal (§ Calibrage) | É + C | ✓ (D72) |
| J161 | Nouvelles règles P10-P13 : hiérarchie notion > détails ; transversalité = un niveau de plus ; chiffres selon leur usage ; répartition de contrôle ≈ 10 / 35-40 / 35 / 10-15 % sans forcer | Tirées de la collection | C | ✓ (D73) |
| J162 | Ce journal complet de la conversation, en plus du journal des décisions importantes | « Il faut un journal pour l'ensemble de la conversation, pas uniquement les importantes » | É | ✓ |

## 11. Points ouverts

- J157 : réglé (J167).
- J121 : renommer la conversation (à faire par l'étudiant).
- J83 : réglage CSS et « Vrai / Faux » du type de note (à faire par l'étudiant, une fois).
- Nettoyage manuel du Drive : anciens originaux à la racine de `Prompts\` et de `Outils\`, anciens paquets du 11/11.
- J156 : cibles de formats et de vignettes devenues de simples repères (J156).
- Écarts entre la collection et la grille : tranchés (J164, J165). Reclassement du paquet AVC : dans la conversation dédiée (J166).

## 12. Réponses du 12 novembre, 15 h 51

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J163 | Skill v1.7 enregistré | Réponse « Q1 ok » | É | ✓ |
| J164 | « Nombre de morts par an » → **I2** ; règle générale : volumes annuels, rangs et proportions en I2, seul le chiffre qui décrit le patient type (âge médian) en I1 | Réponse « I2 » (le message disait « Q3 I2 » ; compris comme la réponse à Q-2, la question sur ce chiffre) | É | ✓ (D75) |
| J165 | Lobes et leurs fonctions en I1, anatomie fine en I2 : grille validée | Réponse « Q3 ok » | É | ✓ (D75) |
| J166 | Le reclassement du paquet AVC se fait dans la conversation dédiée au paquet AVC, avec un prompt fourni ; on ne mélange pas conception du skill et travail sur un cours | « Ce sera pour le canal QCM AVC, on ne mélange pas » | É | ✓ (D76) |
| J167 | Import et synchronisation AnkiWeb du paquet AVC v1.6 faits par l'étudiant | Réponse « tout fait » | É | ✓ (J157 réglé) |

## 13. Organisation (12 novembre, soir)

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J168 | Retours R-25 à R-37 reçus ; le skill doit être mis à jour avant toute régénération | Document de retours de la conversation AVC | É | à faire dans « Skill – conception » |
| J169 | Organisation validée : conversation « Skill – conception », une conversation par cours, échanges par documents de retours ; un rôle par document ; « Lisez-moi » dans le projet | « Ce chat devient un peu fourre-tout » | É | ✓ (D93) |
| J170 | Traçabilité retour → décision → règle → contrôle | Ne rien perdre, skill léger | É | ✓ (D94) |
| J171 | Skill en dossier (SKILL.md court + references/ + scripts/), mis à jour par import du zip ; correction d'une erreur antérieure : un skill peut contenir plusieurs fichiers | Skill plus léger, scripts livrés avec | É | ✓ (D95) |
| J172 | D77-D91 déplacées vers les journaux des cours AVC et BPCO | Réponse « Q3 ok » | É | ✓ (D92) |
| J173 | La conception du skill continue dans Claude Code ; R-25 à R-37 y sont intégrés ; cette conversation s'arrête là pour le skill | Proposition de l'étudiant | É | ✓ (D96) |

## 14. Conversation « Skill – conception » dans Claude Code (12 novembre, nuit) — skill v1.8

| # | Décision | Pourquoi | Qui | Statut |
|---|---|---|---|---|
| J174 | Dépôt git `C:\Git\qcm-anki-ifsi` ; trois commits : v1.7 importée telle quelle, restructuration D95, v1.8 | Garder l'état v1.7 exact et prouver la migration | É | ✓ (D97) |
| J175 | Migration vérifiée par script : 66 codes v1.7 tous présents dans `references/regles.md` ; chaque ligne v1.7 recherchée dans les fichiers v1.8, les lignes reformulées listées dans le tableau de correspondance | « Sans perdre une seule règle » | É | ✓ (`Historique\Correspondance skill v1.7-v1.8.md`) |
| J176 | Contrôles mesurés sur le paquet AVC v1.7 (356 cartes) avant validation : X1 356, R7 36, R5 21, M11 7 (J16, C20, C21, I18, L07, L15b, J15), M8 2 (N05, A05), R11 0 grâce au titre neutre (45 vignettes) ; X3 signale 75 cartes, 49 termes | « Montre-moi combien de cartes chaque nouveau contrôle bloque » | É | ✓ |
| J177 | Premier essai du contrôle R5 (« l'attribut souligné apparaît dans d'autres questions ») abandonné : 72 cartes, il confondait attribut et sujet (« <u>AIT</u> ») ; remplacé par une liste générale de mots d'attribut (21 cartes) ; « moyen » retiré de la liste (« étage moyen ») | Faux positifs | C | ✓ |
| J178 | Doublon du glossaire signalé quand un sigle et son terme complet se définissent l'un l'autre (le sigle commence par le terme, le terme cite le sigle) ; deux essais plus larges abandonnés (« Dissection ≈ Hématome », « Anticoagulant cite AVK » : faux positifs). Entrée « Échocardiographie » de `glossaire.py` ramenée à « Exploration du cœur par ultrasons. » : ETT et ETO gardent leur définition propre | R-34 (N17) ; sur l'ancien glossaire, le contrôle trouve exactement ETT et ETO | C | ✓ |
| J179 | Rendu : ✔ / ✘ devant chaque proposition et sa justification ; sources en `<sup>` ; liste des sources après les images de page | R-27, R-28 | C | ✓ |
| J180 | Corrections de `build.py` hors retours : chemins de `cours.py` relatifs au dossier du cours ; `REF_APKG` facultatif (type de note dans `Outils/`) ; `stats.json` écrit en UTF-8 (plantage sous Windows) | Défauts trouvés en testant | C | ✓ |
| J181 | Tests automatiques `tests/run_tests.py` (un cours fautif, un cours correct construit jusqu'au `.apkg`) et `tests/make_zip.py`, hors du zip | Vérifier chaque contrôle à chaque version | C | ✓ |
| J182 | Q-1 à Q-10 validés tels que proposés ; R7 bloquant strict (exception `ok`) ; doublons de sigles seulement signalés | « Oui, tout valider » | É | ✓ (D98-D107) |
| J183 | Q-10 : d'abord reporté, puis fait tout de suite à la demande de l'étudiant (v1.8.1) : 22 entrées « CM6 AVC » déplacées dans `glossaire_cours.py` de l'exemple AVC, remplacement par terme, glossaire trié ; comparaison carte par carte : 0 différence sur 356 cartes | « Q10 je comprends pas la demande » puis « A maintenant » | É | ✓ (D108) |
| J184 | Anciens fichiers archivés : `Historique\Skill qcm-anki-ifsi v1.7 - SKILL.md`, `Historique\Outils v1.7\` ; zip et `Outils\` remplacés par la v1.8 | D49 | C | ✓ |
| J185 | Le journal du projet Claude « QCM IFSI » n'est pas accessible depuis Claude Code : l'étudiant recopie `Historique et décisions` et ce journal dans le projet | D74 | É | à faire par l'étudiant |
