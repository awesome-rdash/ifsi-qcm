# Règles du skill qcm-anki-ifsi

Chaque règle porte un code stable : lettre de la section + numéro. Un code n'est **jamais réattribué** : une nouvelle règle prend le numéro suivant de sa section, une règle supprimée laisse un trou. Le pourquoi de chaque règle est dans le journal des décisions (`Historique et décisions - QCM Anki IFSI.md`), pas ici.

## S — Sources
- **S1** — **PDF du cours** = source principale. Lire **le texte ET le rendu image de chaque page** (le contenu des diapos est souvent uniquement en image).
- **S2** — **Notes** de l'étudiant = complément. Une contradiction avec la diapo se signale en phase 1.
- **S3** — **Web** : ponctuel, sources fiables uniquement (HAS, ANSM, Santé publique France, Légifrance, sociétés savantes, Collèges des enseignants, Vidal, manuels universitaires, dictionnaires médicaux ou terminologiques officiels), **citées** dans le champ Sources.
- **S4** — Ne jamais inventer une connaissance. Les **bonnes réponses** viennent du cours ou d'une source validée en phase 1. Les **mauvaises réponses** peuvent venir d'ailleurs, mais doivent être fausses sans aucune ambiguïté.
- **S5** — Information du cours non confirmée → **gardée**, avec `⚠ Non confirmé : …`.
- **S6** — Toute modification du cours → **tracée** : `✎ Modifié par rapport au cours : « … » → « … » (source)`. Seules les fautes de frappe se corrigent sans trace.
- **S7** — Chiffres différents entre la diapo et les notes qui mesurent des choses différentes → une question pour chacun.
- **S8** — **Toute définition ou tout complément absent du cours porte sa source** (organisme, titre, URL vérifiée) : dans le glossaire, chaque définition indique la page du cours qui la donne et/ou la source en ligne ; un `Complément` hors cours a sa source dans `w`. Une source se lit avant d'être citée.

## P — Importance (tag `PSB::Importance::I0` … `I3`)
Se demander : **quand en ai-je besoin, et que se passe-t-il si je ne l'ai pas ?**
- **P1** — **I0 = à avoir en tête en permanence**, réponse instantanée :
  - **réflexe vital** : l'ignorer ou hésiter peut tuer un patient (ex. déficit brutal = alerte, noter l'heure de début ; glycémie capillaire d'emblée ; à jeun avant le test de déglutition) ;
  - **normes et repères chiffrés du quotidien** : constantes, normes biologiques usuelles, unités et conversions du calcul de dose, délais d'action des antiseptiques ;
  - **carte d'identité** de la maladie ou de la notion centrale du cours : ce que veut dire son sigle, sa définition en une phrase, aiguë ou chronique, les signes qui la font suspecter ;
  - **bases réglementaires et méthodologiques de tous les jours** (types d'ordonnance, but ou objectif de soin, responsabilité professionnelle).
  Une connaissance utile mais qui ne change ni le geste immédiat ni la pratique quotidienne n'est pas I0.
- **P2** — **I1 = cœur du cours**, rappel en quelques secondes :
  - le vital **non réflexe**, souvent transversal ; le vital propre au cours aussi (ex. contre-indications à la thrombolyse) ;
  - la **définition des notions clés** du cours et leur reconnaissance (« quel concept ? ») ;
  - le **plan** de la prise en charge (étapes de la démarche) ;
  - la correspondance **structure-fonction de base** (lobes et leurs fonctions, organes sur un schéma) ;
  - les **familles** et le **traitement de première intention** ;
  - le **chiffre phare** de l'épidémiologie (âge médian, ordre de grandeur que tout soignant cite).
- **P3** — **I2 = comprendre et détailler**, propre au cours ou transversal :
  - ce que **suppose** une notion, ce **sur quoi elle repose**, à quoi elle contribue ;
  - les **mécanismes**, la pharmacocinétique, le spectre d'action ;
  - l'**anatomie fine** (voies, côté de l'hémiplégie et hémisphère atteint) ;
  - les **chiffres secondaires** (proportion avant 45 ans, rang comme cause de handicap, nombre de cas ou de décès par an) et la grande répartition (ischémique / hémorragique).
- **P4** — **I3 = examen** :
  - les **sous-répartitions** (pourcentage de chaque cause rare) ;
  - les **noms commerciaux** ;
  - les **dates historiques** ;
  - la biochimie structurale fine ;
  - les détails cités une seule fois.
- **P5** — En cas d'hésitation, choisir le niveau le plus important si une erreur peut mettre un patient en danger.
- **P6** — « Pas à connaître par cœur » → I3, mais la connaissance est quand même fichée.
- **P7** — Une question avec une erreur dangereuse ⛔ → **au moins I1** ; I0 seulement si la connaissance relève de P1.
- **P8** — Pas d'autres tags.
- **P9** — En cas de doute sur la grille, comparer avec les cartes de la collection de l'étudiant qui portent un tag d'importance (`PSB::Importance::*`) ou d'ancienne priorité (`Priorité::P0`…`P3`, équivalent I0…I3), et avec ses paquets `_🌟Important` (normes, anatomie, systèmes, gestes, calcul de dose), qui signalent les connaissances de base.
- **P10** — **Hiérarchie** : une notion est au moins aussi importante que ses détails. En général, chaque niveau de détail perd un niveau : définition I1 → composantes I2 → sous-détails I3. Un détail ne dépasse sa notion mère que s'il relève lui-même de P1.
- **P11** — **Transversalité** : une connaissance qui ressert dans d'autres UE, en stage ou au quotidien infirmier gagne un niveau, sans dépasser I1 sauf si elle relève de P1.
- **P12** — **Chiffres** :
  - norme ou seuil qui déclenche une action → I0 ou I1 ;
  - chiffre phare qui décrit le patient type (ex. âge médian) → I1 ;
  - volume annuel (cas, décès), rang, proportion → I2 ;
  - chiffre secondaire → I2 ;
  - détail de répartition, chiffre « pas à connaître » → I3.
- **P13** — **Répartition de contrôle** d'un paquet : environ I0 10 %, I1 35-40 %, I2 35 %, I3 10-15 %. Un écart de plus de 15 points sur un niveau oblige à relire le classement en phase 2. On ne force jamais une carte à changer de niveau pour coller aux chiffres.

## C — Couverture
- **C1** — **Toutes** les connaissances sont fichées, I3 compris. **Chaque élément d'une liste du cours** (causes, signes, complications, examens, branches d'une artère…) est la bonne réponse d'au moins une carte ; si 4 propositions ne suffisent pas, faire plusieurs cartes. Audit élément par élément avant la livraison.
- **C2** — Nombre de questions par connaissance : I0 → 2-3 angles (direct, inverse, vignette, autre format) ; I1 → 1-2 ; I2-I3 → 1.
- **C3** — Vocabulaire : questions dédiées, y compris pour les termes du cours non définis **et pour les termes hors cours employés dans les propositions** (médicaments, examens, signes : ex. statine, troponine, lipasémie, exophtalmie). Définition marquée « hors cours » et sourcée (S8), cartes dans le paquet du cours.
- **C4** — Pas de cas progressifs sur plusieurs cartes.
- **C5** — Le contrôle de couverture est **bloquant** ; `couverture.xlsx` relie chaque connaissance à ses pages et à ses questions.

## F — Formats (4 propositions, Réponse 5 à 12 vides)
- **F1** — **QCM** (mode 1, ≈ 50 %) : 1 à 4 bonnes réponses, nombre non annoncé et varié. Pour les listes, critères, signes, causes, surveillances, conduites à tenir.
- **F2** — **QCS** (mode 2, ≈ 35-40 %) : une seule bonne réponse. Pour un fait unique, une valeur, une définition, l'interprétation d'une image, la « première action », ou une **liste complète** (4 listes dont une seule juste).
- **F3** — **Kprim** (mode 0, ≈ 10-15 %) : chaque affirmation est à juger vraie ou fausse.
  - chaque affirmation est absolument vraie ou fausse ;
  - aucun terme vague (souvent, peut, associé à) ;
  - toutes portent sur le même objet ;
  - le nombre d'affirmations vraies varie de 0 à 4.
  - `Réponses` : `1 0 0 1`.
- **F4** — L'add-on **mélange les propositions** : ne jamais renvoyer à une proposition par son numéro.
- **F5** — Dans un QCM, l'énoncé met **« (s) »** à chaque mot qui peut être au pluriel (« Examen(s) à faire avant l'aspirine ? »). Une définition (une seule bonne réponse) est un QCS.
- **F6** — Les proportions de formats (F1-F3) et de vignettes sont des **repères**. On ne crée jamais une question, ni on ne change son format, seulement pour s'en approcher : une carte doit apporter quelque chose à l'apprentissage.

## R — Rédaction
**Recto = Contexte → Titre → Question**
- **R1** — **La Question se comprend seule**, sans lire le titre ni le contexte : elle nomme la maladie, la situation ou l'objet concerné (« Réduction du risque d'infarctus cérébral si l'AIT est traité ? », jamais « Réduction du risque si on le traite ? » ; « Définition de l'hémorragie méningée ? », jamais « Définition ? »). L'autonomie de la question prime sur l'absence de répétition.
- **R2** — Le Titre est la section, plus la notion si elle apporte une information nouvelle. Il ne contient jamais le nom du cours et ne répète pas le contexte.
- **R3** — La Question ne dit que ce qui est demandé, sans formule inutile.
- Le script supprime la notion du titre si elle est déjà dans la question, bloque les répétitions entre contexte et titre et les énoncés de moins de 2 mots porteurs de sens (sauf vocabulaire), et signale dans le rapport les mots du titre repris dans la question.

**Question**
- **R4** — Écrite **en gras** (le script l'ajoute).
- **R5** — **Mot discriminant souligné** (`<u>…</u>`) quand des cartes ne diffèrent que d'un mot, ou pour un mot décisif (négation, côté, délai, population). Quand l'attribut demandé (gravité, terrain, cause, complication, forme, examen…) vaut pour plusieurs maladies, souligner **aussi le sujet** (maladie, sigle) : « <u>Terrain</u> de l'<u>hémorragie méningée</u> ». Chaque passage souligné reste court : le mot ou le groupe nominal. Un attribut souligné sans son sujet est bloquant.
- **R6** — Ancre sémantique : « délai depuis le début des symptômes », pas seulement « délai ».
- **R7** — Pas d'indice grammatical ni lexical, **dans tous les formats** : aucun mot de l'énoncé ne se retrouve, même sous une autre forme (même racine : bronches / bronchique, méningée / méningé), seulement dans les bonnes réponses. Quand une liste est découpée en plusieurs cartes (C1), **le critère de découpage n'est pas écrit dans la question** (jamais « complication(s) touchant la déglutition ou les bronches »). Contrôle bloquant ; exception justifiée dans `ok`.
- **R8** — **Domaine en tête** de chaque question : « AVC – Position au lit à la phase aiguë d'un infarctus cérébral ? » (le script l'ajoute à partir de `DOMAINE` dans `cours.py` ; « Vocabulaire – » pour les cartes de vocabulaire).
- **R9** — **Pas de provenance** dans la question (« selon la note de cours », « cités dans le tableau », « (diapo) », « (schéma) »). La page va dans l'explication (contrôle bloquant).
- **R10** — **Aucun renvoi à une autre carte** (« même patient », « ci-dessus ») (contrôle bloquant).
- **R11** — **Le titre ne donne pas la réponse** (ex. titre « Dissection » sur une vignette dont la réponse est la dissection) : imposer un titre neutre avec `titre` (contrôle bloquant en QCS).
  - **Vignette** : le titre ne nomme **jamais** le diagnostic ni la situation à reconnaître. Titre neutre par défaut (« Cas clinique », `TITRE_VIGNETTE` dans `cours.py`). Un titre imposé ne partage aucun mot (même racine) avec **aucune** proposition, bonne ou mauvaise (contrôle bloquant), ni n'oriente vers l'une d'elles (ex. « Sujet jeune » oriente vers la dissection).
- **R12** — **Mots sans ambiguïté** : chaque verbe a son complément (« traiter l'HTA », jamais « traiter » seul) ; préciser l'organe (« infarctus cérébral », pas « infarctus ») ; un délai dit son point de départ (« après le début de la céphalée »).

## V — Vignettes
- **V1** — Objectif ≥ 40 % des questions I0/I1, angle infirmier (surveillance prioritaire, première action, ce qui fait appeler le médecin, ce qu'on vérifie avant d'administrer, installation).
- **V2** — **Crédibilité stricte** : présentation typique et cohérente ; la réponse découle d'une phrase du cours, citée dans l'explication ; aucune interprétation au-delà du cours ; en cas de doute, pas de vignette.
- **V3** — Vignettes rédigées avec le **vocabulaire technique** (ptosis, myosis, hémiparésie…), défini dans le glossaire, sauf si la question teste justement la reconnaissance du signe décrit.

## M — Propositions et mauvaises réponses
- **M1** — Elles **ressemblent aux bonnes** : **même nature** que les autres propositions (toutes des signes, toutes des examens… jamais « mortalité » parmi des signes), même niveau de détail.
- **M2** — La bonne réponse ne doit pas dépasser **1,3 fois** la longueur moyenne des mauvaises (contrôle bloquant).
- **M3** — Chacune cible une **confusion identifiée** ; si le bon sens suffit à l'éliminer, la remplacer.
- **M4** — Chiffres : **valeurs proches** ou mêmes valeurs permutées, jamais une valeur aberrante, ni une valeur juste selon une autre source ou un autre passage du cours.
- **M5** — Définitions : mauvaises réponses = définitions de **termes proches** (ex. hypoxie/hypoxémie, dyspnée/dysphagie, oligurie/anurie, myosis/mydriase).
- **M6** — Termes absolus : permis comme pièges, mais ils doivent aussi apparaître dans des propositions vraies du paquet.
- **M7** — Interdit : « toutes / aucune des réponses », les propositions absurdes.
- **M8** — Propositions composées (éléments séparés par « ; », « , », « / » ou « et ») :
  - la valeur juste de chaque composant n'est **jamais la plus fréquente** parmi les 4 propositions ;
  - la bonne réponse n'est **jamais la seule à réunir les éléments les plus fréquents** (vote majoritaire : on la devinerait sans rien savoir) ;
  - équilibrer chaque composant (contrôles bloquants en QCS).
- **M9** — Répartition en pourcentages : **toutes les catégories** du cours, total = 100 % dans chaque proposition (contrôle bloquant).
- **M10** — Vérifier qu'une mauvaise réponse n'est pas juste ailleurs : seuil d'une autre recommandation (ex. SpO2 94 %), examen fait dans certains bilans (ex. TSH). En cas de doute, la remplacer.
- **M11** — **Pas de schéma 2 × 2** : interdit, les propositions composées dont chaque élément qui varie ne prend que 2 valeurs (« frontal / temporal » × « expression / compréhension ») : ce sont des choix binaires indépendants, devinables par élimination. Faire une carte par élément, ou donner plus de valeurs à un élément. Contrôle bloquant ; une exception validée par l'étudiant s'écrit dans `ok`.
- **M12** — **Propositions indépendantes** : aucune proposition n'inclut, n'implique ou n'exclut une autre par définition (ex. « syndrome méningé non fébrile » exclut « fièvre élevée dès le début » ; « raideur de nuque » fait partie du syndrome méningé). Vérifié par le relecteur des règles (phase 2b).

## E — Erreurs dangereuses ⛔
- **E1** — Une mauvaise réponse qui mettrait un patient en danger s'il l'appliquait. Les inclure volontairement sur les gestes de sécurité du cours et les signaler dans `dz` : le script ajoute `⛔ Erreur dangereuse : « … » — raison` et applique P7.

## X — Informations complémentaires (assemblées par le script)
- **X1** — Explication : point clé, avec la page du cours, puis **chaque proposition, vraie ou fausse, justifiée en une ligne** (champ `why`) : le mécanisme pour une proposition vraie (ex. pourquoi l'œdème cérébelleux comprime le tronc cérébral) ; pour une fausse, ce à quoi elle correspond (autre maladie, autre examen, valeur inversée).
  - **Vignette** : pour la bonne réponse, pourquoi **chaque signe** de l'énoncé y oriente ; pour chaque mauvaise réponse, **les signes qu'on aurait attendus**.
  - Le script affiche chaque proposition suivie de sa justification, une par ligne. Contrôle bloquant : 4 justifications non vides.
- **X2** — ⛔ / ✎ / ⚠ / Complément (sourcé, S8).
- **X3** — Glossaire automatique des termes et sigles présents dans l'énoncé, les propositions et l'explication. **Un terme, une définition, une ligne** : jamais « A / B : déf. A / déf. B ». Pour une question de vocabulaire, l'explication nomme le terme que définit chaque mauvaise proposition, pour que le glossaire les définisse tous. **Chaque définition est sourcée** (S8) ; `glossaire.py` bloque une entrée groupée ou sans source. Les **termes des mauvaises réponses** sont aussi définis, avec **leur intérêt** (ce que l'examen mesure, à quoi sert le médicament). **Tout sigle** de l'énoncé, des propositions ou de l'explication est défini (contrôle bloquant) ; un sigle courant sans intérêt propre est écrit en toutes lettres (`TEXT_REPL` dans `cours.py`).
  - **Tout terme qu'un étudiant de 2e année peut ne pas connaître est défini**, où qu'il soit : bonne réponse comprise (ex. artériographie), vignette, justifications, et **définitions du glossaire elles-mêmes** (ex. « hémostase » dans la définition de thrombophilie). Une expression technique aussi (ex. « des 4 axes »).
  - **Pas de doublon** : un sigle renvoie au terme complet sans le redéfinir (« ETT : échocardiographie transthoracique, voir Échocardiographie »).
  - Le script signale dans le rapport les mots techniques sans entrée (`X3_termes_sans_definition`, repérage approximatif : suffixes médicaux et noms propres) et les sigles qui redéfinissent un terme affiché (`X3_doublons_glossaire`). Chaque signalement est traité ; le relecteur des règles complète.
- **X4** — Page entière du PDF en image.
- **X5** — Champ **Sources** : `<Type> — <fichier>.pdf, p. <n>` ; `Web — <Organisme>, <titre>, <URL>` ; `Généré par Claude (<modèle>) — skill v<version> — <date> — <id>` ; `Règles du skill qcm-anki-ifsi v<version> : <codes>` (règles principales appliquées à la carte, déduites par le script : S1, R1, R7, R8, M1, M3, M12, X1 toujours ; F5 en QCM ; R11 si titre imposé ou vignette ; M8 et M11 si propositions composées ; M9 si répartition ; F selon le format ; V si vignette ; E1 et P7 si ⛔ ; S5/S6/S3 si ⚠/✎/web ; R5 si mot souligné ; X3 et S8 si glossaire ; G2 si cliché ; M4 si chiffres ; M5 et C3 si définition). Mettre à jour `SKILL_VERSION` dans `build.py` à chaque version du skill.
- **X6** — **Présentation** des informations complémentaires :
  - une liste (vocabulaire, éléments, causes…) : **une ligne par élément** ;
  - **sources numérotées** : renvoi en exposant (¹ ²) dans le texte, liste des sources en fin de champ (le script le fait pour le glossaire) ;
  - texte aligné à gauche (le script le fait).

## G — Images
- **G1** — Infos complémentaires : la **page entière** (JPEG 150 dpi), un fichier par page.
- **G2** — Questions d'imagerie : **cliché recadré** depuis l'image source du PDF, sans titre ni légende qui donne la réponse (une flèche sans texte est acceptée). Vérifier chaque recadrage à l'œil.
- **G3** — Noms de fichiers **en minuscules**, sans espace.
