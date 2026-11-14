# QCM Anki IFSI — historique et décisions

> Journal de conception du système de génération de QCM Anki à partir des cours d'IFSI.
> Il conserve le **pourquoi** de chaque règle, pour que le skill `qcm-anki-ifsi` ne contienne que le **quoi faire**.
> À compléter à chaque évolution : une ligne dans le tableau des décisions, et une entrée dans la chronologie.

---

## 1. Contexte

- Étudiant infirmier en 2e année d'IFSI. Il est aussi réserviste militaire, secouriste à la Protection Civile (Paris) et triathlète : son temps de travail est très limité.
- **Avant** : fiches Anki créées à la main après chaque cours. C'était trop long à créer et à relire.
- **Objectif** : à partir du PDF d'un cours (diapos + prises de notes), produire un paquet de QCM Anki prêt à importer. Il doit couvrir toutes les connaissances, classées par importance, avec un minimum de relecture.
- **Environnement** : Claude, avec accès au dossier `G:\Mon Drive\FOR\IFSI` de l'étudiant. Anki est utilisé sur PC et sur téléphone, avec le type de note **QCMs** de l'add-on Multiple Choice.

---

## 2. Chronologie des versions

| Version | Date | Ce qui a changé | Déclencheur |
|---|---|---|---|
| v0.1 / v0.2 | 2025-09 | Cartes Basic/Cloze en TSV, priorités P1-P4, phase de dialogue, sources | Prompts antérieurs (`Anki\Prompts`) |
| v1.0 | 2026-11-10 | Passage aux **QCM** (type QCMs), importance **I0-I3**, phase 1 complète, champs Source/Contexte/Infos | Demande initiale |
| v1.0a | 2026-11-10 | Vérifications web en phase 1 ; ✎/⚠ ; numérotation INC-/Q-/D- ; livraison **.apkg** avec images ; contrôle de couverture ; noms d'images en minuscules ; recadrage des clichés d'imagerie ; glossaire ; vocabulaire non défini ; distracteurs chiffrés proches ; GUID stables ; arborescence `IFSI::QCM::Semestre::UE::Cours` | Test sur le cours AVC + retours |
| v1.1 | 2026-11-10 | Bonnes pratiques de rédaction (NBME, Haladyna, EDN) : répartition des formats, vignettes, longueur de la bonne réponse, termes absolus, distracteurs ciblés, ⛔, relecture indépendante (phase 2b), analyse après usage (phase 4) ; Kprim gardé en minorité | Demande « jury d'examen » + recherche |
| v1.2 | 2026-11-10 | Contexte / Titre / Question sans répétition ; question en gras, titre discret ; mot discriminant souligné ; consignes générales (pas centrées sur un cours) ; « Vrai / Faux » en Kprim | Retours sur téléphone |
| skill 1.0 | 2026-11-10 | Prompt transformé en **skill** `qcm-anki-ifsi` ; historique déplacé dans ce document ; script de construction générique (`cours.py` par cours) | Allègement du prompt |
| skill 1.1 | 2026-11-10 | Récapitulatif consolidé des points ouverts à la fin de chaque message (D47) | Retour de l'étudiant |
| skill 1.2 | 2026-11-10 | Dossier de sortie préfixé par le semestre (D48) ; rangement de `Anki\Prompts` (D49) | Retour de l'étudiant |
| skill 1.3 | 2026-11-11 | Glossaire : un terme = une définition = une ligne, termes de l'explication inclus, contrôle bloquant (D50) ; paquet AVC régénéré | Retour sur la carte « paresthésies » |
| skill 1.4 | 2026-11-11 | Questions autonomes, compréhensibles sans titre ni contexte ; le contrôle de répétition ne bloque plus que contexte/titre (D51) ; 151 énoncés du paquet AVC réécrits | Retour sur la carte « si on le traite » |
| skill 1.5 | 2026-11-11 | Règles numérotées (S, P, C, F, R, V, M, E, X, G) et liste des règles appliquées dans le champ Sources (D56) ; toute définition ou tout complément hors cours sourcé, glossaire entièrement sourcé avec URL (D55) | Retour sur la carte « signe d'alerte » |
| skill 1.6 | 2026-11-12 | Grille d'importance redéfinie (D52-D54) ; 14 nouvelles règles issues des retours R-1 à R-24 (D57-D70) ; paquet AVC : 343 questions, glossaire de 118 termes sourcés | Retours R-1 à R-24 |
| skill 1.7 | 2026-11-12 | Grille d'importance calibrée sur la collection de l'étudiant (P1-P4 réécrites, P9 précisée, P10-P13) ; proportions de formats = repères, jamais de QCM « pour faire des QCM » (F6) ; décisions toujours écrites dans le journal du projet (D71-D74) ; journal complet de la conversation | Export de la collection + retours de l'étudiant |
| skill 1.8 | 2026-11-12 | Skill en dossier (`SKILL.md` court, `references/`, `scripts/`), dépôt git `C:\Git\qcm-anki-ifsi` ; règles M11, M12, X6 ; M8, R5, R7, R11, X1, X3 révisées ; phase 2b à deux relecteurs ; colonne « Règle » dans ce journal (D97-D107) | Retours R-25 à R-37 |
| skill 1.8.1 | 2026-11-12 | Glossaire commun sans page de cours ; entrées propres à un cours dans `glossaire_cours.py`, qui remplacent l'entrée commune (D108) | Question Q-10 |
| skill 1.9 | 2026-11-14 | Collèges de médecine comme source : S3 en deux ordres de sources (bonnes réponses : cours → références citées → validation en phase 1 ; tout le reste : Collèges d'abord, web ensuite) ; nouvelles règles S9-S12 ; M3, M4, M10, X1, X5, S8, V1, V2 révisées ; phase 1 : `sources.md` et `refs/` ; `build.py` : sources libellées et triées, citation de Collège contrôlée (D115-D119) | Retours R-55, R-58 à R-62 |
| skill 1.9.1 | 2026-11-14 | Génération dans **Claude Code sur le PC** (environnement par défaut) : cours et Collèges lus sur place, sans copie ; espace de travail local `%USERPROFILE%\QCM-travail\` ; S9, `fichiers.md` et commandes adaptés à Windows (D120) | Question de l'étudiant sur la copie des PDF |
| skill 1.10 | 2026-11-14 | Dépôt unique `C:\Git\ifsi-tools` (skill, génération, site) ; skill dans `skill\qcm-anki-ifsi\`, scripts appelés sur place ; espace de travail `qcm-generation\cours\<cours>\` (remplace `QCM-travail` et `Decks\…\sources\`) ; Collèges lus dans la copie locale `qcm-generation\colleges\` ; journal, retours et historique dans `skill\docs\`, plus de copie sur le Drive (D121-D123) | Fusion des dépôts |

---

## 3. Décisions

Légende de la source : **É** = décision de l'étudiant, **R** = recherche (bonnes pratiques), **T** = constat lors d'un test, **C** = calibrage sur la collection. Colonne **Règle** : code de la règle du skill qui applique la décision (D94) ; « — » si la décision ne porte pas sur une règle.

### 3.1 Contenu et sources
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D01 | Le PDF du CM est la source principale ; les notes (OneNote ou annotations) le complètent sans le contredire | Rester fidèle à ce qui sera évalué | É | S1, S2 |
| D02 | Recherche web autorisée ponctuellement, sur des sources fiables (HAS, ANSM, SPF, sociétés savantes, Collèges, Vidal…), toujours citées | Compléter un cours incomplet ou erroné | É | S3 |
| D03 | Les **vérifications de contenu se font en phase 1**, pas pendant la génération | Que l'étudiant valide les corrections avant la rédaction | É | Phase 1 |
| D04 | Info du cours non confirmée → **gardée** avec `⚠ Non confirmé` | L'examen porte sur le cours ; l'étudiant doit connaître l'écart | É | S5 |
| D05 | Toute modification du cours est **tracée** avec `✎` dans les infos complémentaires | Savoir ce qui diffère de son cours | É | S6 |
| D06 | Chiffres différents entre diapo et notes, s'ils mesurent des choses différentes → **une question chacun** | Ex. UNV −20 % de mortalité (note) vs −30 % de mortalité et handicap (diapo) | É | S7 |
| D07 | Seuils « pas à connaître par cœur » → quand même fichés en I3, vérifiés en ligne, une question par seuil | Ex. seuils du NIHSS | É | P6 |
| D08 | Mauvaises réponses : connaissances hors cours autorisées, mais elles doivent être fausses sans ambiguïté | Des distracteurs plausibles demandent plus que le cours | É | S4 |
| D09 | Les termes employés **sans être définis** dans le cours ont leurs propres questions de vocabulaire (définition hors cours, marquée) + un glossaire en bas de chaque carte | « Les définitions de ces mots » manquaient (athérome, lacune…) | É | C3, X3 |
| D10 | Consignes **générales**, exemples variés : le skill ne doit pas être centré sur un cours | Réutiliser le même outil pour toutes les UE | É | Rôle |

### 3.2 Importance
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D11 | Échelle **I0** (par cœur, instinctif) / **I1** (quelques secondes) / **I2** (spécialité, ex. stage de cardio) / **I3** (spécifique à l'UE et à l'examen) | Réviser selon le contexte (entre les examens, en stage) | É | P1-P4 |
| D12 | Stockée en tag `PSB::Importance::I0`…`I3` | Tags déjà utilisés par l'étudiant | É | P1-P4 |
| D13 | Pas d'autres tags (spécialité, type de source…) | « Ne t'occupe pas des tags » | É | P8 |
| D14 | Question contenant une erreur dangereuse ⛔ → **I0** | La sécurité du patient prime | É | P7 |

### 3.3 Couverture et volume
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D15 | **Toutes** les connaissances sont fichées ; **aucune limite** de volume (≈ 50 questions pour un cours léger, beaucoup plus s'il y a du vocabulaire) | Exhaustivité | É | C1 |
| D16 | I0 : 2-3 angles ; I1 : 1-2 ; I2-I3 : 1 | Plus de répétition pour l'essentiel | É (validé) | C2 |
| D17 | **Contrôle de couverture bloquant** + tableau `connaissance → page → questions` | Prouver que tout le cours est couvert | É | C5 |
| D18 | Estimer le volume en phase 1 **à partir de l'inventaire détaillé** | Test AVC : 180 annoncées, 267 à 300 produites | T | Phase 1 |
| D19 | Pas de cas progressifs sur plusieurs cartes | Anki présente les cartes dans un ordre aléatoire | É | C4 |

### 3.4 Formats et rédaction
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D20 | QCS, QCM et **Kprim** ; la fac n'utilise pas le Kprim, mais il est **gardé en minorité** pour varier | « J'aimais bien les Kprim, ça change » | É | F1-F3 |
| D21 | Répartition cible ≈ 50 % QCM / 35-40 % QCS / 10-15 % Kprim ; nombre de bonnes réponses varié | EDN dominé par les QRM ; les questions à réponse unique sont plus faciles et plus sujettes aux indices | R | F1-F3 |
| D22 | Une même connaissance peut revenir en QCS puis en QCM ; un QCS peut porter sur 4 listes dont une seule est juste | Formats de la fac | É | F2 |
| D23 | **Vignettes cliniques** pour l'application, mais **crédibles** : présentation typique, réponse qui découle d'une phrase du cours, pas d'interprétation de Claude | « Attention à ne pas faire des cas incorrects » | É + R | V1, V2 |
| D24 | Les mauvaises réponses **ressemblent aux bonnes** et ciblent une confusion identifiée ; test du bon sens | Défaut le plus fréquent selon les guides | É + R | M1, M3 |
| D25 | **Chiffres proches** ou permutés dans les mauvaises réponses, jamais aberrants | « C'est plus dur si les chiffres sont similaires » | É | M4 |
| D26 | Questions de définition : mauvaises réponses = définitions de **termes proches** | Ex. thrombus/embole/hématome | É | M5 |
| D27 | La bonne réponse ne doit pas être plus longue (≤ 1,3 × la moyenne) | Audit : 92 QCS sur 208 avaient une bonne réponse plus longue | R + T | M2 |
| D28 | Termes absolus permis comme pièges, mais pas comme indice (aussi dans des propositions vraies) | « Ça peut être des pièges, mais attention » | É | M6 |
| D29 | **⛔ Erreurs dangereuses** signalées (équivalent des réponses « inacceptables » de l'EDN) | Utile pour un futur infirmier | R + É | E1 |
| D30 | Position de la bonne réponse, fuites entre cartes, ordre logique des chiffres : **non traités** | L'add-on mélange les propositions et Anki mélange les cartes | É | F4 |
| D31 | Énoncé de type étiquette accepté (pas obligatoirement une vraie phrase) | Le but est des QCM rapides ; les cartes détaillées servent au rappel | É | R3 |

### 3.5 Présentation des cartes
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D32 | Contexte (cours) → Titre (section) → Question : **aucune répétition** | Carte « AVC — Épidémiologie — Épidémiologie » | É | R2 |
| D33 | **Question en gras**, titre discret (réglage CSS du type de note, fait une fois par l'étudiant) | « En gras mettre la question, pas le titre » | É | R4 |
| D34 | **Mot discriminant souligné** quand des cartes ne diffèrent que d'un mot | Ex. lobe <u>pariétal</u> | É | R5 |
| D35 | Explications sans renvoi par numéro de proposition | L'add-on mélange les propositions à l'affichage | T | F4 |
| D36 | Images : page entière dans les infos complémentaires ; **cliché recadré** autorisé pour les questions d'imagerie, sans les légendes | Les légendes donnaient la réponse | É + T | G1, G2 |
| D37 | Noms d'images **en minuscules** | Anki met les noms en minuscules : avec une majuscule, l'image ne s'affiche plus | T | G3 |

### 3.6 Processus et livraison
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D38 | Phase 1 complète (analyse + questions), puis attente de la validation | Choix de l'étudiant | É | Phase 1 |
| D39 | Rapport de phase 1 numéroté `INC-` / `Q-` / `D-` ; toutes les questions dans `Q-` | Répondre sans ambiguïté | É | Phase 1 |
| D40 | Livraison en **.apkg** avec images, qui réutilise le type de note QCMs (id `1604570191317`) | Import en double-clic, sans copie manuelle des médias, sans base64 | É + T | Phase 3 |
| D41 | **GUID stables** par question | Réimporter met à jour les cartes au lieu de créer des doublons | T | Phase 4 |
| D42 | Paquet `IFSI::QCM::Semestre <n>::UE <n°> - <intitulé>::<Cours>` | Choix de l'étudiant | É | Phase 1 |
| D43 | **Phase 2b** : relecture par des sous-agents séparés, sans les clés, par lots de ~100 questions | Ne pas noter son propre travail | É + R | Phase 2b |
| D44 | Phase 4 : analyse des statistiques Anki après 2-3 semaines | Repérer les cartes trop faciles ou ambiguës | R + É | Phase 4 |
| D45 | Modèle conseillé : **Claude Opus** (Sonnet moins fiable sur les mauvaises réponses médicales) | Exactitude médicale | — | Garde-fous |
| D46 | Le prompt devient un **skill** ; l'historique vit dans ce document | Alléger les consignes | É | — |
| D47 | Chaque message qui attend une réponse se termine par le **récapitulatif consolidé** de tous les points ouverts (INC/Q/D), y compris ceux des messages précédents et ceux qu'ajoute un nouveau document ; numéros stables ; points tranchés rappelés une fois | « Je ne dois pas avoir à switcher entre deux messages pour savoir à quoi répondre » | É | Phase 1 (récapitulatif) |
| D48 | Dossier de sortie : `Anki\Decks\S<n> - <UE> - <Cours>\` (ex. `S3 - UE 2.8 - CM6 AVC`) | Retrouver les paquets par semestre | É | Phase 3 |
| D49 | `Anki\Prompts` : racine minimale (`Historique\`, `Outils\`, ce document, zip du skill) ; anciennes versions du prompt et du SKILL.md dans `Historique\` ; type de note de référence dans `Outils\exemple CM6 AVC\` | « Il ne doit y avoir qu'un minimum de fichiers à la racine » | É | Garde-fous |
| D50 | Glossaire : **un terme, une définition, une ligne** (plus de « Hypoesthésie / paresthésie : diminution / sensations anormales ») ; le glossaire couvre aussi les termes de l'explication ; en vocabulaire, l'explication nomme le terme de chaque mauvaise proposition ; `glossaire.py` bloque toute entrée groupée | Entrées groupées lues comme des synonymes | É | X3 |
| D51 | **La question se comprend seule** (nomme la maladie, la situation ou l'objet) ; l'autonomie prime sur la non-répétition (révise D32) ; contrôles : répétition bloquante seulement entre contexte et titre, énoncé de moins de 2 mots porteurs bloquant, répétition titre/question seulement signalée | « Si on traite quoi ? Il ne faut pas partir du principe que s'il y a un mot clé dans le titre c'est logique dans la question » | É | R1, R2 |
| D55 | **Toute définition ou tout complément hors cours porte sa source** (règle S8) : chaque entrée du glossaire cite la page du cours et/ou une source fiable lue (GDT de l'OQLF, HUG, Larousse médical, HPSJ, CHUV, Académie de médecine…) avec URL ; entrée sans source bloquante | « Quand tu donnes des defs ou complément pas dans le cours, je veux la source de la définition » | É | S8 |
| D56 | Règles du skill **numérotées** par section, codes jamais réattribués ; le champ Sources liste les règles principales appliquées à la carte, avec la version du skill (règle X5) | « Dans source après le généré par Claude, je veux aussi les numéros des règles principales » | É | X5 |
| D52 | Grille d'importance : **I0** réflexe vital (instantané, peut tuer) ; **I1** vital non réflexe, souvent transversal ; **I2** important non vital (cours ou transversal) ; **I3** examen (règles P1-P4) | « Si j'ai une hémiplégie droite, ça ne me sert pas à grand-chose de savoir que c'est l'hémisphère gauche » ; rappels anatomiques utiles en neuro → I2 | É | P1-P4 |
| D53 | Vital, propre au cours, non réflexe (ex. contre-indications à la thrombolyse) → **I1** | Choix de l'étudiant | É | P2 |
| D54 | ⛔ ⇒ **au moins I1** (I0 seulement si réflexe vital) — révise P7 | Trop de cartes en I0 avec l'ancienne règle | É | P7 |
| D57 | **Domaine en tête** de chaque question (« AVC – … », « Vocabulaire – … ») (R8) | « L'utilisateur qui va vite ne lit ni le contexte ni le titre » | É | R8 |
| D58 | **Pas de provenance** dans la question (note, tableau, diapo, schéma, cours) (R9) | « On n'a pas le cours sous les yeux quand on répond » | É | R9 |
| D59 | **Aucun renvoi** à une autre carte (« même patient ») (R10) | Les cartes ne sont pas présentées dans l'ordre | É | R10 |
| D60 | **Le titre ne donne pas la réponse** ; titre neutre imposé si besoin (R11) | Titre « Dissection » sur la vignette de dissection | É | R11 |
| D61 | **Mots sans ambiguïté** : verbe avec complément (« traiter l'HTA »), organe précisé (« infarctus cérébral »), point de départ des délais (R12) | « On traite quoi ? » ; « infarctus du cœur ou du cerveau ? » | É | R12 |
| D62 | QCM : **« (s) »** sur les mots qui peuvent être au pluriel ; définition = QCS (F5) | Demande de l'étudiant | É | F5 |
| D63 | Propositions composées : la valeur juste de chaque composant n'est jamais la plus fréquente (M8) | Carte aphasie/dysarthrie devinée par recoupement | É | M8 |
| D64 | Répartitions : toutes les catégories, total 100 % (M9) | Carte des causes d'infarctus sans les causes rares | É | M9 |
| D65 | Une mauvaise réponse ne doit pas être juste ailleurs (autre recommandation, autre bilan) (M10) | TSH, SpO2 94-95 % | É | M10 |
| D66 | Glossaire : termes des **mauvaises réponses** aussi, avec leur **intérêt** (ce que mesure l'examen, à quoi sert le médicament) ; tout sigle défini (contrôle bloquant) ou écrit en toutes lettres (X3) | « Il faut expliquer ce que c'est dans le glossaire, je ne connais pas ces termes » ; « pourquoi chercher la troponine dans une biologie d'AVC ? » | É | X3 |
| D67 | **Chaque élément d'une liste du cours** est la bonne réponse d'au moins une carte ; audit élément par élément (C1) | Hyperglycémie, artères, complications de la p. 16 absentes | É | C1 |
| D68 | Cartes de vocabulaire pour les termes **hors cours** des propositions (médicaments, examens), **dans le paquet du cours** (C3) | Choix de l'étudiant | É | C3 |
| D69 | Vignettes avec le **vocabulaire technique** (ptosis, myosis…) sauf si la question teste la reconnaissance du signe (V3) | « Pourquoi le vocabulaire technique n'est-il pas utilisé ? » | É | V3 |
| D70 | Calibrer l'importance sur les cartes déjà taguées de la collection de l'étudiant (P9) — export à fournir | Proposition de l'étudiant | É | P9 |
| D71 | Les proportions de formats et de vignettes sont des **repères** : on ne crée jamais une question, ni on ne change son format, seulement pour s'en approcher (F6) | « Pas besoin de faire des QCM pour faire des QCM si ça n'apporte rien en termes d'apprentissage » | É | F6 |
| D72 | Grille d'importance **calibrée sur la collection** (§ 4 bis) : **I0** = à avoir en tête en permanence (réflexe vital, normes et repères chiffrés du quotidien, carte d'identité de la maladie ou de la notion centrale, bases réglementaires du quotidien) ; **I1** = cœur du cours (définitions des notions clés, plan de prise en charge, structure-fonction de base, familles et 1re intention, chiffre phare) ; **I2** = comprendre et détailler (ce que suppose une notion, mécanismes, anatomie fine, chiffres secondaires) ; **I3** = examen (sous-répartitions, noms commerciaux, dates historiques, biochimie fine) — précise D52 | Les tags de l'étudiant classent plus haut que la grille D52 l'identité de la maladie et les chiffres phares, et plus bas les détails | É + C | P1-P4 |
| D73 | Règles P10-P13 : **hiérarchie** (un détail perd un niveau par rapport à sa notion mère) ; **transversalité** (+1 niveau, plafond I1 hors P1) ; **chiffres** selon leur usage (seuil d'action I0-I1, chiffre phare I1, secondaire I2, répartition fine I3) ; **répartition de contrôle** ≈ I0 10 % / I1 35-40 % / I2 35 % / I3 10-15 %, écart > 15 points → relecture, sans forcer | Schémas réguliers observés dans la collection (§ 4 bis) | C | P10-P13 |
| D75 | Chiffres : volume annuel (cas, décès), rang et proportion → **I2** ; seul le chiffre qui décrit le patient type (ex. âge médian) → I1 ; lobes et leurs fonctions → I1, anatomie fine → I2 (P3, P12) | « Nombre de morts par an » : I2 ; lobes : grille validée | É | P3, P12 |
| D76 | Les travaux sur un paquet de cours (ex. reclassement du paquet AVC) se font dans la conversation dédiée à ce cours, pas dans la conversation de conception du skill | « Ce sera pour le canal QCM AVC, on ne mélange pas » | É | — |
| D92 | Les décisions propres à un cours vont dans le **journal de ce cours** (`QCM Anki - Journal paquet <cours>.md`), pas ici ; D77-D79 (AVC) et D80-D91 (BPCO) y ont été déplacées | Garder ce journal centré sur le skill | É | — |
| D93 | Organisation : une conversation **Skill – conception** (modifier le skill et les scripts, rien d'autre) ; **une conversation par cours** (génération, corrections, phase 4) ; les deux communiquent par des **documents de retours** (R-xx), jamais par la mémoire d'une conversation | « Ce chat devient un peu fourre-tout » ; ne pas perdre d'information | É | — |
| D94 | **Traçabilité** : retour R-xx → décision Dxx → règle du skill → contrôle du script ; colonne « Règle » à ajouter au tableau des décisions ; chaque document de retours indique « intégré en v1.x → règle » | Retrouver le pourquoi d'une règle sans alourdir le skill | É | — |
| D95 | Le skill devient un **dossier** : `SKILL.md` court (rôle, phases, garde-fous, index des règles) + `references/` (règles complètes, consignes de relecture, format des fichiers) + `scripts/` (build.py, common.py, glossaire.py, type de note). Mise à jour par import du zip | Skill le plus léger possible, lu par morceaux selon la phase, scripts livrés avec lui | É | Structure du skill |
| D96 | La conception du skill se fait dans **Claude Code** (dépôt git, tests des scripts, construction du zip) ; la génération des paquets reste dans les conversations de cours ; les retours R-25 à R-37 sont intégrés dans cette nouvelle conversation | Proposition de l'étudiant ; le skill devient un ensemble de fichiers et de scripts | É | — |
| D74 | Aucune décision ne repose sur la seule conversation : chaque décision est écrite (numéro, décision, pourquoi, qui) dans ce journal, dans le projet Claude « QCM IFSI » **et** dans la copie du Drive, avant la fin de la conversation ; le détail chronologique (y compris les petites décisions) est dans `QCM Anki - Journal complet de la conversation.md` | « Je veux que les décisions de ce chat ne soient pas uniquement portées par la conversation » ; « un journal pour l'ensemble de cette conversation et pas uniquement les importantes » | É | Garde-fous |
| D97 | Dépôt git `C:\Git\qcm-anki-ifsi` (hors Google Drive) avec la structure D95 ; la v1.7 y est migrée sans perte (66 codes vérifiés par script, tableau `Historique\Correspondance skill v1.7-v1.8.md`) ; justifications retirées des règles ; tests de `build.py` dans `tests/` et documents de travail dans `docs/`, hors du zip | Skill lu par morceaux, scripts testés, migration prouvée complète | É | — |
| D98 | Propositions composées découpées sur « ; », « , », « / » et « et » (pas « 0 et 30 », pas « 1/4 ») ; en QCS, blocage si la bonne valeur d'un composant est la plus fréquente **ou** si la bonne réponse est la seule à réunir les éléments les plus fréquents (vote majoritaire) | R-29 : N05 devinée par vote, non détectée car séparée par des virgules | É | M8 |
| D99 | Interdit : propositions composées dont chaque élément qui varie ne prend que 2 valeurs (schéma 2 × 2), contrôle bloquant ; exception validée par l'étudiant écrite dans le champ `ok` de la carte (ex. I18, triade de Claude Bernard-Horner) ; `ok` sert à toute exception justifiée à un contrôle bloquant et apparaît dans le rapport | R-25 : J16 devinée par élimination ; 7 cartes AVC dans ce cas (dont J15) | É | M11 |
| D100 | Chaque proposition, vraie ou fausse, est justifiée en une ligne (champ `why`, obligatoire, bloquant) : mécanisme pour une vraie, ce à quoi correspond une fausse ; vignette : pourquoi chaque signe oriente vers la réponse, signes attendus pour chaque mauvaise réponse ; le script affiche chaque proposition (✔/✘) suivie de sa justification, ce qui garantit qu'elle est citée | R-26, R-30, R-31 : mécanismes absents ; 144 explications AVC de moins de 60 caractères | É | X1 |
| D101 | Présentation : une ligne par élément de liste ; sources du glossaire numérotées en exposant, liste en fin de champ ; informations complémentaires alignées à gauche | R-27, R-28 ; glossaire centré qui débordait (« ho-doppler ») | É | X6 |
| D102 | Quand l'attribut demandé (gravité, terrain, cause, complication, forme…) vaut pour plusieurs maladies, le sujet est souligné aussi ; « deux mots au maximum » remplacé par « passages courts » ; contrôle bloquant : un mot d'attribut souligné seul (liste générale de mots d'attribut) | R-29, R-36 | É | R5 |
| D103 | Propositions indépendantes (aucune n'inclut, n'implique ou n'exclut une autre par définition), vérifiées par le relecteur des règles ; M1 précise « même nature » ; la section M devient « Propositions et mauvaises réponses » | R-31 (N09), R-36 (« mortalité » parmi des signes) ; pas de contrôle automatique fiable | É | M1, M12 |
| D104 | Titre de vignette neutre par défaut : « Cas clinique » (`TITRE_VIGNETTE` dans `cours.py`) ; un titre imposé ne partage aucune racine avec aucune proposition (bloquant) | R-33 : N13 « Hémorragie méningée — Diagnostic » donnait la réponse ; 7 vignettes AVC dans ce cas | É | R11 |
| D105 | Indice lexical contrôlé dans tous les formats, par racine (6 premières lettres sans accent : bronches / bronchique), bloquant strict avec exception `ok` ; le critère de découpage d'une liste (C1) n'est jamais écrit dans la question | R-37 : H12d ; 36 cartes AVC bloquées | É | R7 |
| D106 | Tout terme qu'un étudiant de 2e année peut ne pas connaître est défini, y compris dans la bonne réponse et dans les définitions du glossaire ; un sigle renvoie au terme complet sans le redéfinir ; le script signale (sans bloquer) les mots techniques sans entrée et les sigles qui redéfinissent un terme affiché | R-34 (artériographie), R-35 (lupus, hémostase) ; repérage automatique approximatif, complété par le relecteur des règles | É | X3 |
| D107 | Phase 2b à deux relecteurs : à l'aveugle (répond sans les clés) et relecteur des règles (carte complète, coche chaque règle importante, carte par carte) ; tous les deux relisent **toutes** les cartes à chaque génération ou régénération | R-32 : en v1.7 seules les 13 cartes ajoutées avaient été relues, à l'aveugle | É | `references/relecture.md` |
| D108 | Le glossaire commun (`glossaire.py`) ne cite que des sources en ligne ; une définition qui cite une page de cours va dans le `glossaire_cours.py` du cours, où elle remplace l'entrée commune du même terme (contrôle bloquant) ; les 22 entrées sourcées « CM6 AVC » sont passées dans `Outils\exemple CM6 AVC\glossaire_cours.py` (13 restent dans le commun avec leur source web, 9 propres à l'AVC en sortent) ; glossaire de chaque carte par ordre alphabétique ; vérifié : glossaire identique sur les 356 cartes AVC | Les cartes d'un autre cours affichaient « source : CM6 AVC, p. … » et des définitions écrites pour l'AVC (ex. FLAIR) | É | X3, S8 |

### 3.7 Référentiels (Collèges)
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D109 | Les **Collèges de médecine** deviennent une source de référence du skill, au rang fixé par R-55 (cours → références citées par le cours → Collèges → autres sources fiables) ; ils servent aux explications, aux définitions, aux mauvaises réponses et aux compléments, le cours restant la référence du niveau attendu (R-60) | « Plus simple que de chercher sur tout Internet » ; sources fixes et fiables, citations précises | É | S3, S8, S11 |
| D110 | Les collèges sont **découpés en un PDF par chapitre et compressés** (scans : images à 110 dpi, OCR conservée ; environ −50 %) dans `G:\Mon Drive\FOR\Médecine\Arc EXTERNES 👺\Collèges découpés\` ; les originaux sont **gardés** (l'étudiant les supprimera s'il le souhaite après vérification) | Sans shell sur le PC, lire un PDF impose de le copier ; un chapitre pèse quelques Mo au lieu de 300 ; le connecteur Drive n'indexe pas le texte des PDF de plusieurs centaines de Mo | É (proposé par Claude, accepté) | — |
| D111 | **Index des collèges** (collège, édition, type numérique ou scan + OCR, chapitres, items EDN, pages d'origine, mots-clés) dans le projet (`claude/Référentiels - Index des collèges.md`) et dans `Collèges découpés\_Index des collèges.md` ; inventaire fait par des **sous-agents légers (Haiku)** à partir des signets et des débuts de page, bornes contrôlées par script | « Un sous-agent dans un modèle peu consommateur pour inventorier les documents » | É | S9 |
| D112 | Collèges en scan + OCR : recherche tolérante et **chiffres vérifiés sur l'image de la page** (R-59) | 23 collèges sur 33 sont des scans ; l'OCR contient des coquilles | T | S10, M4 |
| D113 | Les 4 collèges de plus de 400 Mo (Rhumatologie 8e, Cancérologie 4e, Douleurs 6e, Médecine interne 5e) sont coupés en parties par l'étudiant (`<nom>_PartieN.pdf`, dans le dossier d'origine), recollés par Claude puis découpés par chapitre comme les autres : les 33 collèges sont indexés (2026-11-14) | La liaison avec le PC refuse les fichiers de plus de 400 Mo | É | — |
| D114 | Deux ordres de sources : les **bonnes réponses** viennent toujours du cours (S4) ; tout ce qui est inventé ou expliqué autour (mauvaises réponses / détrompeurs, justification de chaque proposition, « pourquoi » des explications, définitions du glossaire, crédibilité des vignettes) se cherche **d'abord dans les Collèges** via l'index, le web seulement si le collège ne couvre pas le point ou pour vérifier une donnée récente ; chapitres de collège relevés une fois en phase 1 (R-62) | « Aller piocher en priorité dans les collèges pour inventer les détrompeurs, les justifications, etc. » ; moins de recherches web, distracteurs plus réalistes | É | S3, M3, M4, M10, X1, S8, V1, V2 |
| D115 | Quatre nouvelles règles de sources : **S9** mode d'emploi des Collèges (chapitre trouvé dans l'index, seul ce PDF copié, jamais un collège entier, recherche par mot-clé, page d'origine = début du chapitre + rang de la page − 1, format de citation) ; **S10** collège « scan + OCR » (recherche tolérante, tout chiffre repris vérifié sur l'image de la page) ; **S11** niveau (le cours reste la référence ; connaissance d'un collège absente du cours fichée seulement si validée en phase 1) ; **S12** donnée récente (comparer l'année du collège à la dernière recommandation, la plus récente l'emporte, signalée en INC-) | R-58 à R-61 ; règles séparées pour que chaque contrôle renvoie à un code précis | É | S9, S10, S11, S12 |
| D116 | `build.py` : toute source hors cours du champ `w` porte un libellé — `<référence> (cité par le support de cours, p. n)`, `Collège — <collège>, <édition>, <année>, chap. « <titre> », item <n>, p. <n> du PDF d'origine`, `Web — <organisme>, <titre>, <URL>` — sinon blocage (S3) ; citation de Collège incomplète bloquante (S9) ; champ Sources trié cours → cité par le cours → Collège → web ; aides `cite()`, `college()`, `web()` dans `common.py` ; S3 et S9 ajoutées automatiquement à la liste des règles de la carte | R-55, R-58, R-62 ; un contrôle par script coûte moins qu'un relecteur (analyse de la consommation de tokens) | É | S3, S9, X5 |
| D117 | Phase 1 : relever les **sources de travail** une fois — références citées sur les diapos, et pour chaque partie du cours le ou les chapitres de collège correspondants (fichier + pages) — dans `sources.md` ; les chapitres sont copiés dans `<cours>/refs/` et réutilisés pendant toute la génération sans nouvelle recherche ; la phase 1 présente aussi les incohérences déjà vérifiées (Collège puis web) et les connaissances de collège absentes du cours, à valider | R-55, R-60, R-62 ; éviter de rechercher le même chapitre à chaque carte | É | Phase 1, S11 |
| D118 | Le glossaire commun (`glossaire.py`) accepte une citation de Collège en plus des sources en ligne (une page de cours y reste interdite, D108) ; ordre des sources d'une définition : page du cours, puis Collège, puis web | Un chapitre de collège est une source fixe, valable pour tous les cours | É | S8, X3 |
| D119 | Le relecteur des règles reçoit `sources.md` et le texte des chapitres de `refs/` et vérifie S3, S9-S12 : source hors cours libellée et pertinente (Collège avant web), bonne réponse tirée d'un collège seulement si validée en phase 1, chiffre d'un collège « scan + OCR » vérifié sur l'image, aucune donnée d'un collège ancien contredite par une recommandation plus récente | R-59 à R-61 ne se contrôlent pas par script | É | `references/relecture.md` |
| D120 | La génération des paquets se fait dans **Claude Code sur le PC** de l'étudiant (environnement par défaut ; précise D96) : cours, notes, index et chapitres de Collège lus **sur place** avec `pymupdf`, sans copie et sans la limite de 400 Mo ; espace de travail local hors Google Drive (`%USERPROFILE%\QCM-travail\<S<n> - <UE> - <Cours>>\`) ; le projet Claude n'étant pas accessible depuis Claude Code, les copies du Drive font foi pendant la génération et l'étudiant les recopie ensuite dans le projet ; une conversation cloud liée au PC reste possible (copie des seuls fichiers utiles, dossier à emoji ajouté par « + ») ; skill installé dans Claude Code par une jonction `%USERPROFILE%\.claude\skills\qcm-anki-ifsi` → `C:\Git\qcm-anki-ifsi` | « Je génère depuis PC, donc on peut passer sous Claude Code si plus simple » ; la copie n'était imposée que par la conversation cloud (outils de lecture des PDF dans le cloud, pas de terminal sur le PC) | É | Environnement (`SKILL.md`), S9, `references/fichiers.md` |

### 3.8 Organisation du dépôt
| # | Décision | Pourquoi | Source | Règle |
|---|---|---|---|---|
| D121 | Un seul dépôt git, `C:\Git\ifsi-tools` (dépôt GitHub privé `ifsi-qcm` renommé `ifsi-tools`), avec trois dossiers, un par rôle : `skill\`, `qcm-generation\`, `qcm-website\`, chacun avec son `CLAUDE.md` ; le skill y entre **avec son historique** (`git subtree`, choix A) ; `C:\Git\qcm-anki-ifsi` devient inutile | Skill, fichiers de travail des cours et site évoluent ensemble (D124) ; une seule copie de chaque document | É | — (`CLAUDE.md`) |
| D122 | Collèges : **copie locale** des Collèges découpés dans `qcm-generation\colleges\`, **exclue de git** sauf `_Index des collèges.md` (choix B2) ; avec Claude Code, index et chapitres lus dans cette copie ; dans le cloud, l'original du Drive | Lecture rapide sur le disque local sans versionner plusieurs Go de PDF | É | S9 |
| D123 | Documents du skill (journal des décisions, documents de retours, historique, journal complet) dans `skill\docs\` du dépôt, avec copie dans le projet Claude « QCM IFSI » ; **plus de copie sur le Drive** (révise D74 et D49) ; fichiers de travail d'un cours dans `qcm-generation\cours\<S<n> - <UE> - <Cours>>\` (remplace `%USERPROFILE%\QCM-travail\`, D120, et `Decks\…\sources\`) ; scripts appelés sur place depuis `skill\qcm-anki-ifsi\scripts\` ; livraison des `.apkg` inchangée sur le Drive | Une seule source à jour, versionnée ; plus de copies à synchroniser à la main | É | Garde-fous, `references/fichiers.md` |
| D124 | `build.py` écrira directement les données du site (`qcm-website\data\index.json`, `data\<id-cours>\questions.json`, `media\`) ; le site ne convertira plus les `.apkg` et `sync-decks.ps1` deviendra inutile. **Hors de la fusion** : deux sessions, « Skill – conception » (export dans `build.py`, tests) puis « Site QCM » | Une seule conversion, faite là où les données sont produites | É | — (à venir) |

---

## 4. Retour d'expérience — test UE 2.8 CM6 AVC (2026-11-10)

| Indicateur | v1.0a | v1.2 |
|---|---|---|
| Questions | 293 | 300 |
| Connaissances (inventaire détaillé) | 151 + 19 vocabulaire | 151 + 19 vocabulaire |
| Formats QCM / QCS / Kprim | 24 % / 71 % / 5 % | 34 % / 53 % / 13 % |
| Vignettes | ≈ 15 au total | 41 au total (22 % des I0/I1) |
| Questions avec ⛔ | 0 | 17 |
| Concordance de la relecture indépendante | — | 298 / 300 |

**Incohérences du cours détectées et traitées** : note « gaucher = hémisphère droit » (✎) ; « scanner normal = moins de 4h30 » (✎) ; anémie sévère comme contre-indication à la thrombolyse (⚠) ; seuils du NIHSS (✎) ; repère alcool ancien (Complément) ; cortex occipital comme cause de cécité monoculaire (✎) ; massage comme prévention des phlébites (⚠).

**Écarts restants aux cibles** :
- formats : beaucoup de faits uniques (chiffres, délais, seuils), d'où beaucoup de QCS ;
- vignettes : seules celles directement étayées par le cours ont été écrites.

---

## 4 bis. Calibrage de l'importance sur la collection (2026-11-12)

**Données** : export de la collection de l'étudiant (9 505 notes). Seules ses propres cartes ont servi, pas les cartes générées.
- 87 cartes taguées `PSB::Importance::I0-I3`, dont 2 cartes « test » ignorées : I0 7, I1 55, I2 20, I3 3. Elles portent sur l'AVC, l'interprofessionnalité, la BPCO, les ordonnances et les soins relationnels.
- 772 cartes avec l'ancienne échelle `Priorité::P0-P3`, lue comme I0-I3 : P0 120 (16 %), P1 309 (40 %), P2 263 (34 %), P3 80 (10 %). Elles portent sur la biologie, les antibiotiques, les groupes sociaux, la fonction digestive et le calcul de dose.
- Les paquets `_🌟Important` signalent ce que l'étudiant juge fondamental : normes biologiques, anatomie (461 cartes), systèmes (conduction cardiaque, SRAA, ECG), examens et gestes techniques, calcul de dose.

**Ce qu'on observe → règle retenue**

| Observation dans la collection | Exemples | Règle |
|---|---|---|
| Normes, constantes, unités et délais du quotidien en P0 | Normes biologiques, FC selon l'âge, débit d'O2 chez le BPCO, délais d'action des antiseptiques, unités de calcul de dose | P1 (I0, normes du quotidien) |
| Carte d'identité de la maladie en I0 | « Symptômes pour suspecter un AVC », « BPCO : aiguë ou chronique ? », « Sigle EFR » | P1 (I0, carte d'identité) |
| Bases réglementaires et méthodologiques du quotidien en I0 | 4 types d'ordonnances, but ou objectif de soin, responsabilité professionnelle | P1 (I0, bases réglementaires) |
| Définition d'un concept clé et sa reconnaissance en I1 ; ce qu'il suppose ou ce sur quoi il repose en I2 | Interprofessionnalité : définitions en I1, « repose sur… » et « que suppose… » en I2 | P2, P3, P10 (hiérarchie) |
| Plan de la prise en charge en I1 | « Étapes de la démarche diagnostique » de l'AVC | P2 |
| Fonctions des lobes et parties du cerveau sur schéma en I1 | Lobe frontal, lobe pariétal, schémas du cerveau | P2 (structure-fonction de base) |
| Chiffre phare en I1, chiffres secondaires en I2, sous-répartitions en I3 | Âge médian I1 ; % avant 45 ans et rang comme cause de handicap I2 ; % des grandes catégories d'AVC I2, sous-catégories I3 | P12 |
| Familles et 1re intention en P1, mécanismes et pharmacocinétique en P2, noms commerciaux en P3 | Antibiotiques : familles et indications P1 ; demi-vie, élimination, spectre P2 ; Oracilline®, Orbénine® P3 | P2, P3, P4 |
| Dates historiques en P2-P3 | Découverte de la pénicilline P2, prix Nobel P3 | P4 |
| Biochimie structurale fine en P3 | Affinités de l'hémoglobine R/T, liaisons des acides aminés | P4 |
| Transversal (normes, anatomie, gestes, calcul de dose) dans `_🌟Important` | — | P11 (transversalité) |

**Comparaison avec le paquet AVC v1.6** (343 cartes, avant calibrage) : I0 6 %, I1 17 %, I2 48 %, I3 29 %. Les cartes de l'étudiant sur le même cours placent plus haut l'épidémiologie (âge médian I1, contre I3 dans le paquet) et le plan de la démarche (I1, contre I3). Le paquet est donc trop bas en I1 et trop haut en I3. Reclassement fait le 2026-11-12 dans la conversation du cours (voir `QCM Anki - Journal paquet CM6 AVC.md`).

**Écarts tranchés par l'étudiant (2026-11-12)** — D75
- « AVC – nombre de morts par an », tagué I0 dans sa collection : **I2**. Les volumes annuels (cas, décès), rangs et proportions sont des chiffres secondaires ; seul le chiffre qui décrit le patient type (âge médian) est en I1.
- Lobes : **I1** pour la correspondance structure-fonction de base (lobes et leurs fonctions), **I2** pour l'anatomie fine (voies, côté de l'hémisphère atteint). Validé.

---

## 4 ter. Paquets de cours

Les décisions et le déroulé propres à chaque paquet sont dans le journal du cours (D92) :
- CM6 AVC : `QCM Anki - Journal paquet CM6 AVC.md` (D77-D79, paquet v1.7 de 356 questions) ;
- CM2 BPCO : `QCM Anki - Journal paquet CM2 BPCO.md` (D80-D91, paquet v1.7 de 253 questions).

---

## 5. Points ouverts

- Atteindre les cibles de vignettes (≥ 40 %) et de formats : autoriser des vignettes tirées de références externes citées, ou baisser les cibles ?
- Réglage du modèle de carte (CSS « question en gras », « Vrai / Faux ») : à faire par l'étudiant dans Anki.
- Phase 4 : première analyse des statistiques Anki du paquet AVC, prévue vers fin novembre 2026.
- Recopier ce journal dans le projet Claude « QCM IFSI » (D74, D123) après chaque modification faite dans Claude Code (qui n'a pas accès au projet) ; dernière copie : 2026-11-14 (D115-D120, skill 1.9.1) — à refaire pour D121-D124, skill 1.10.
- Régénérer le paquet AVC avec la v1.10, dans Claude Code, puis le paquet BPCO.
- ~~Intégrer R-55 et R-58 à R-62~~ : fait en skill v1.9 (D115-D119), le 2026-11-14.
- ~~Commit de la v1.9.1, jonction du skill (D120)~~ : fait le 2026-11-14 avec la fusion (D121) ; importer le zip (`skill\dist\`) dans claude.ai seulement pour les conversations cloud.
- D124 : export des données du site par `build.py`, puis adaptation du site (deux sessions).
- Collèges : 1 087 PDF sur le Drive le 2026-11-14 (1 071 notés au moment de D122) ; écart à expliquer.
- Recopier dans le projet Claude les documents modifiés par Claude Code (D120).
- Autres retours BPCO non intégrés : R-38 à R-54, R-56, R-57 (à traiter dans une prochaine version).

---

## 6. Emplacements

| Élément | Emplacement |
|---|---|
| Dépôt | `C:\Git\ifsi-tools` (GitHub privé `ifsi-tools`) : `skill\`, `qcm-generation\`, `qcm-website\` (D121) |
| Skill | `C:\Git\ifsi-tools\skill\qcm-anki-ifsi\` (`SKILL.md`, `references\`, `scripts\`) ; Claude Code → `%USERPROFILE%\.claude\skills\qcm-anki-ifsi` (jonction vers ce dossier) ; claude.ai → skills de l'étudiant (import du zip) ; tests dans `skill\tests\` |
| Ce document | `C:\Git\ifsi-tools\skill\docs\Historique et décisions - QCM Anki IFSI.md` + projet Claude « QCM IFSI » (`claude/QCM Anki - Historique et décisions.md`) ; plus de copie sur le Drive (D123) |
| Documents de retours (R-xx), analyses | `skill\docs\retours\`, `skill\docs\` |
| Journal complet de la conversation (toutes les décisions, même petites) | projet Claude « QCM IFSI » (`claude/QCM Anki - Journal complet de la conversation.md`) + `skill\docs\historique\Journal complet - conception skill (2026-11-10 au 12).md` |
| Scripts | dans le skill (`skill\qcm-anki-ifsi\scripts\`), appelés sur place ; scripts v1.7 dans `skill\docs\historique\Outils v1.7\` ; skill v1.8.1 complet dans `skill\docs\historique\Skill v1.8.1\` |
| Type de note de référence | `skill\qcm-anki-ifsi\scripts\Type de note QCMs.apkg` |
| Skill (fichier d'installation) | `skill\dist\qcm-anki-ifsi.zip` (`python skill\tests\make_zip.py`, non versionné) |
| Anciennes versions (prompts v0.1 à v1.2, SKILL.md v1.1, anciens scripts, diffs) | `skill\docs\historique\` |
| Fichiers de travail d'un cours (`cours.py`, `k.py`, questions, `sources.md`) | `C:\Git\ifsi-tools\qcm-generation\cours\S<n> - <UE> - <Cours>\` ; exemple complet : `S3 - UE 2.8 - CM6 AVC` |
| PDF des cours | `G:\Mon Drive\FOR\IFSI\UE\…` (chemin dans `cours.py`) |
| Paquets livrés | `G:\Mon Drive\FOR\IFSI\Anki\Decks\S<n> - <UE> - <Cours>\` |
| Collèges découpés (un PDF par chapitre) | copie locale `C:\Git\ifsi-tools\qcm-generation\colleges\` (hors git, D122) ; original `G:\Mon Drive\FOR\Médecine\Arc EXTERNES 👺\Collèges découpés\` (originaux non découpés : `Arc EXTERNES 👺\DFASM …\Collèges\` et `COLLEGES NON VUS\`) |
| Index des collèges | `qcm-generation\colleges\_Index des collèges.md` (versionné) + projet Claude « QCM IFSI » (`claude/Référentiels - Index des collèges.md`) |
| Site de révision | `C:\Git\ifsi-tools\qcm-website\` (https://ifsi-github.jrouzier.fr) |
