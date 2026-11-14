# PROMPT DE GÉNÉRATION DE QCM ANKI — v1.2

> À utiliser à chaque génération, **pour tout cours et toute UE**. Remplace les prompts v0.1 / v0.2 (cartes Basic/Cloze), v1.0 et v1.1.
> Toutes les consignes sont **générales** ; les exemples viennent de domaines variés et ne doivent pas orienter le contenu d'un cours particulier.
> Historique :
> - v1.0 (2026-11-10) création.
> - v1.0a (2026-11-10, test CM6 AVC) : vérifications web en phase 1 ; traçabilité des modifications et avertissements ; chiffres diapo/notes distincts ; numérotation INC-/Q-/D- ; livraison .apkg (type QCMs + images) ; contrôle de couverture bloquant ; propositions mélangées par l'add-on ; noms d'images en minuscules ; recadrage des clichés d'imagerie ; glossaire ; vocabulaire non défini ; distracteurs chiffrés proches ; GUID stables. Retour d'expérience : estimation de phase 1 à 180 questions, résultat 267-293 → estimer à partir de l'inventaire détaillé.
> - v1.1 (2026-11-10) : bonnes pratiques de rédaction (NBME, Haladyna, guides de docimologie, EDN) : Kprim conservé en format minoritaire (variété, absent des examens de la fac) ; répartition des formats ; vignettes cliniques crédibles ; longueur de la bonne réponse ; termes absolus ; distracteurs ciblant une confusion ; erreurs dangereuses ⛔ ; phase 2b de relecture par un agent séparé ; contrôles automatiques ; analyse après usage.
> - v1.2 (2026-11-10, retours sur téléphone) : Contexte / Titre / Question sans répétition ; question en gras, titre discret (réglage du modèle de carte) ; mot discriminant souligné ; consignes et exemples rendus généraux (plus centrés sur un seul cours) ; en-têtes Kprim « Vrai / Faux ».
> Exécution prévue : Claude avec accès au dossier `G:\Mon Drive\FOR\IFSI` (lecture des PDF, rendu des pages en image, écriture des fichiers d'import).

---

## 1. PROFIL ET CONTRAINTES

- **Qui** : étudiant infirmier en 2e année d'IFSI (L2). Également réserviste militaire, secouriste à la Protection Civile (Paris) et triathlète → **temps de travail personnel très limité**.
- **Enseignements** :
  - CM majoritairement délivrés par la faculté de médecine (« CM SSU »), parfois par l'IFSI (« CM IFSI ») ; souvent plus denses que le niveau attendu d'un infirmier.
  - TD / TPG pilotés par les formateurs IFSI, centrés sur le métier.
- **Finalités** : examens semestriels (QCS et QCM ; le Kprim n'est pas utilisé par la fac mais est gardé en minorité pour varier les révisions), stages, pratique professionnelle.
- **Ancienne méthode** : fiches Anki manuelles → trop chronophage à créer et relire.
- **Objectif du système** : à partir d'un cours, produire un paquet de QCM **prêt à importer**, qui couvre **toutes** les connaissances du cours, classées par importance, **difficiles à réussir par simple ruse** (sans indice), avec un minimum de relecture.
- Les cartes sont révisées **dans un ordre aléatoire** par Anki et les propositions sont **mélangées à chaque affichage** : chaque carte doit se suffire à elle-même.

---

## 2. SOURCES — HIÉRARCHIE ET RÈGLES

1. **PDF du CM** : source principale. Il peut contenir les diapos ET les prises de notes de l'étudiant (texte tapé, annotations PDF, notes intercalées entre les diapos). Lire **le texte ET les images** de chaque page (le contenu des diapos est souvent uniquement en image).
2. **Prises de notes** (OneNote exporté, annotations dans le PDF, fichier joint) : complément. En cas de contradiction avec la diapo → le signaler en phase 1, ne pas trancher seul.
3. **Recherche Internet** : autorisée **ponctuellement**, uniquement sur des sources fiables, pour :
   - combler une information incomplète, ambiguë ou manifestement erronée dans le cours ;
   - vérifier qu'une réponse est juste ;
   - construire des distracteurs plausibles mais faux et des vignettes cliniques crédibles.
   Sources acceptées (par ordre de préférence) : HAS, ANSM, Santé publique France, Légifrance, sociétés savantes (SFNV, SFC, SFMU, SPLF…), Collèges des enseignants (ex. CEN), Vidal / base de données publique des médicaments, référentiels IFSI officiels, manuels universitaires. **Pas** de forums, blogs, sites de fiches non sourcés, Wikipédia comme seule source.
   Toute info tirée d'Internet est **citée dans le champ Sources** (organisme, titre, URL).
4. **Questions à l'étudiant** : si un point reste douteux après recherche, poser la question (en phase 1) plutôt que deviner.
5. **Interdit** : inventer une connaissance. Les **bonnes réponses** viennent du cours (ou d'une source web citée et validée en phase 1). Les **mauvaises réponses** peuvent utiliser des connaissances hors cours (cf. §7).
6. **Quand faire les vérifications** : toutes les vérifications web portant sur le **contenu** (incohérences, chiffres douteux, seuils, corrections) se font **en phase 1**, et leur résultat est présenté dans le rapport de phase 1. En phase 2, la recherche web ne sert plus qu'à valider des **distracteurs** et des éléments de **vignettes**.
7. **Information du cours non confirmée** : si une information écrite dans le cours (diapo ou notes) n'est pas retrouvée ou est contredite par les sources fiables, on la **garde** telle qu'elle est écrite, avec un avertissement dans les Informations complémentaires : `⚠ Non confirmé : <ce que disent les sources consultées>`.
8. **Toute modification par rapport au cours** (correction d'une erreur, reformulation qui change le sens, chiffre complété ou mis à jour) est **tracée dans les Informations complémentaires** : `✎ Modifié par rapport au cours : « <texte du cours> » → « <texte retenu> » (<source>)`. Seules les fautes de frappe évidentes sont corrigées sans trace.
9. **Chiffres différents entre la diapo et les notes** (ex. −20 % vs −30 %) : vérifier s'ils portent sur des choses différentes (critère, délai, population) ; si oui, **une question distincte pour chacun**, chacune précisant ce que mesure le chiffre ; sinon, le signaler en incohérence.

---

## 3. ÉCHELLE D'IMPORTANCE (tag `PSB::Importance::I0` à `I3`)

| Niveau | Définition | Exemples de connaissances |
|---|---|---|
| **I0** | À connaître **par cœur**, rappel **instinctif** pour tout étudiant infirmier, quel que soit le service. | Normes des constantes, signes d'alerte d'une urgence vitale, gestes et réflexes de sécurité, définitions fondamentales, règles d'administration, contre-indications majeures. |
| **I1** | Important pour tout infirmier, mais on peut prendre **quelques secondes à quelques dizaines de secondes** pour s'en rappeler. | Mécanismes physiopathologiques de base, principaux examens et leur but, complications fréquentes, surveillance infirmière courante. |
| **I2** | Connaissance **de spécialité** : indispensable dans un service donné (stage de cardio, neuro, pneumo…), non attendue ailleurs (ex. EHPAD). | Délais d'un traitement d'urgence spécialisé, scores propres à un service, traitements spécialisés, surveillance spécifique (ex. surveillance post-coronarographie en cardio). |
| **I3** | Spécifique à l'**UE et à l'examen à venir** ; pas besoin de la réviser entre les examens. | Chiffres épidémiologiques précis, détails anatomiques fins, éponymes, classifications détaillées, détails cités « pour l'examen ». |

Règles :
- En cas d'hésitation entre deux niveaux, choisir le **plus important** (le plus petit chiffre) si une erreur sur cette connaissance peut mettre un patient en danger ; sinon le moins important.
- Une mention du professeur du type « pas à connaître par cœur » → I3 (et le signaler) ; la connaissance est **quand même** fichée. Si ce sont des seuils ou une classification, les vérifier en ligne en phase 1 et faire une question par seuil.
- Une même connaissance garde le même niveau dans toutes ses questions.
- **Toute question qui contient une erreur dangereuse** (proposition ⛔, cf. §7) est classée **I0**, quel que soit le niveau de la connaissance.

---

## 4. PROCESSUS

### PHASE 1 — ANALYSE ET DIALOGUE (OBLIGATOIRE, attendre la validation)

1. Lire **intégralement** le PDF : texte de chaque page **et** rendu visuel de chaque page (diapos, schémas, tableaux, imagerie), ainsi que les notes jointes.
2. Présenter à l'étudiant :
   - **Variables du cours** proposées : `[UE]`, `[Cours]`, `[Type de cours]` (CM SSU / CM IFSI / TD), `[Contexte]`, `[Paquet]`, `[Spécialité]`.
     Format du paquet : `IFSI::QCM::Semestre <n>::UE <n°> - <intitulé UE>::<Cours>` (ex. `IFSI::QCM::Semestre 3::UE 2.8 - Processus obstructifs::CM6 - AVC` ; `IFSI::QCM::Semestre 2::UE 2.11 - Pharmacologie et thérapeutiques::CM2 - Anticoagulants`).
   - **Résumé structuré** du cours (plan par sections, avec n° de pages).
   - **Inventaire des connaissances** par section, avec l'**importance proposée** (I0–I3), sous forme de tableau compact.
   - **Estimation du nombre de questions**, au total et par importance, **calculée à partir de l'inventaire détaillé** (aucune limite a priori).
   - **Tableaux / figures / imagerie** : lesquels transformer en questions, lesquels utiliser (recadrés) comme image dans la question.
   - **Situations cliniques envisagées** pour les vignettes (cf. §7), avec leur source (exemple du cours ou référence fiable).
   - **Incohérences, erreurs ou trous** détectés, **déjà vérifiés en ligne** : pour chacun, ce que disent les sources (citées) et le traitement proposé (corrigé et tracé, gardé avec avertissement, ou question distincte).
   - **Doutes** sur l'utilité d'une info pour un infirmier ou pour l'examen.
   - **Questions** à l'étudiant, y compris le **nombre de questions souhaité** pour ce cours.
3. **Numérotation du rapport** : chaque liste a son propre préfixe pour que l'étudiant puisse répondre sans ambiguïté :
   - incohérences : `INC-1`, `INC-2`… ;
   - questions à l'étudiant : `Q-1`, `Q-2`… (toute décision attendue de l'étudiant figure dans cette liste, rien n'est demandé ailleurs dans le rapport) ;
   - doutes : `D-1`, `D-2`….
   Ne pas utiliser `I1`, `I2`… (réservés à l'importance).
4. **Attendre** la validation et les compléments avant la phase 2.

### PHASE 2 — GÉNÉRATION

1. Établir l'inventaire détaillé (§5) et le glossaire du cours.
2. Rédiger les QCM selon les règles ci-dessous, **dans l'ordre du cours** (ordre des pages). Pour chaque distracteur, savoir quelle confusion il cible (§7).
3. Rendre les pages utilisées en images, recadrer les clichés d'imagerie (§8).
4. Lancer les **contrôles automatiques** (§11) ; corriger tant qu'un contrôle bloquant échoue.

### PHASE 2b — RELECTURE INDÉPENDANTE (OBLIGATOIRE)

Un **agent séparé** (sous-agent qui n'a pas rédigé les questions ; au-delà de ~100 questions, plusieurs sous-agents en parallèle, un lot de ~100 chacun, dans un dossier qui ne contient ni les clés ni les sources des questions) reçoit :
- le PDF du cours (texte + pages en image) et les images jointes aux questions ;
- les questions **sans les réponses ni les explications** (titre + énoncé + 4 propositions + format).

Il doit, pour chaque question :
1. **Répondre** comme un étudiant qui connaît le cours.
2. Signaler : plusieurs réponses défendables, bonne réponse absente, erreur médicale, vignette non crédible ou interprétation non étayée par le cours, distracteur éliminable par bon sens, indice (longueur, mot répété, terme absolu, grammaire).
3. Indiquer les questions auxquelles il a pu répondre **sans le cours** grâce à un indice.

Puis comparer ses réponses aux clés : toute **discordance** ou tout signalement est corrigé, ou justifié par écrit dans le rapport de phase 3. Les questions corrigées repassent les contrôles automatiques.

### PHASE 3 — LIVRAISON ET RETOUR

- Résumé : nombre de questions par importance et par format, part de vignettes, nombre de ⛔, points `✎` / `⚠`, sources web utilisées, résultat de la phase 2b (taux de concordance, questions corrigées, justifications).
- Après les retours de l'étudiant : proposer des **améliorations du prompt**, en le gardant **universel** (toutes matières, tous cours).

### PHASE 4 — ANALYSE APRÈS USAGE (2 à 3 semaines après l'import)

- L'étudiant exporte les statistiques Anki du paquet (nombre d'échecs, facilité, intervalle par carte).
- Cartes **jamais ratées** et à intervalle long → vérifier si elles sont trop faciles à cause d'un indice ou d'un distracteur faible ; les durcir.
- Cartes **ratées en boucle** → vérifier ambiguïté, formulation, erreur ; les corriger.
- Réimporter (les GUID stables mettent à jour les cartes sans perdre la progression) et reporter les leçons dans le prompt.

---

## 5. COUVERTURE

- **Toutes** les connaissances du cours sont fichées, y compris I3.
- Nombre de questions par connaissance, selon l'importance :
  - **I0** : 2 à 3 questions sous des **angles différents** (sens direct, sens inverse, vignette clinique, format différent).
  - **I1** : 1 à 2 questions.
  - **I2 / I3** : 1 question.
- Le **vocabulaire** (définitions, sigles, termes médicaux) fait l'objet de questions dédiées — y compris les termes **employés dans le cours sans y être définis** : définition hors cours (connaissance générale ou source fiable), marquée `Complément : définition hors cours` ; ces termes ont leur propre ligne dans l'inventaire (section « Vocabulaire », identifiants `V01`…), importance I0 à I3 selon l'usage infirmier.
- Une même connaissance peut apparaître en QCS puis être réutilisée dans un QCM ou un Kprim : c'est souhaité.
- Pas de « cas progressifs » enchaînés sur plusieurs cartes (les cartes sont révisées dans un ordre aléatoire).
- Le nombre final est validé avec l'étudiant en phase 1.

### Contrôle de couverture (obligatoire, bloquant)
- L'inventaire **détaillé** des connaissances (une ligne par connaissance, identifiant `K001`, `K002`…) est établi avant la rédaction ; le tableau de la phase 1 peut être condensé, pas celui-ci.
- Chaque question porte la (ou les) connaissance(s) qu'elle teste.
- Avant livraison, produire le **tableau de couverture** : `K-id | page | connaissance | importance | questions (ids)`. Toute connaissance sans question **bloque la livraison**.
- Seuls les éléments qui ne sont pas des connaissances (diapo « Objectifs », illustrations décoratives) sont exclus, et listés comme tels en bas du tableau.

---

## 6. FORMATS DE QUESTION (champ `Mode`)

L'add-on Multiple Choice gère trois modes, tous utilisés. Toujours **4 propositions** (Réponse 1 à 4 ; Réponse 5 à 12 laissées vides).

| Format | `Mode` | Règle | Quand l'utiliser |
|---|---|---|---|
| **QCM** (réponses multiples, équivalent QRM de l'EDN) | `1` | 1 à 4 bonnes réponses ; le nombre n'est **pas** annoncé. | Format **majoritaire** : listes, critères, signes, causes, surveillances, contre-indications, conduites à tenir. |
| **QCS** (réponse unique, équivalent QRU) | `2` | Exactement 1 bonne réponse (la meilleure). | Fait unique (valeur, délai, seuil, définition, localisation, mécanisme), **liste complète** (4 listes, une seule correcte), interprétation d'une image, « que faites-vous en premier ? ». |
| **Kprim** | `0` | 4 affirmations, chacune à juger vraie ou fausse ; il faut juger les 4 correctement. | Format **minoritaire**, pour varier : plusieurs caractéristiques d'un même objet (un médicament, une pathologie, un examen) où chaque affirmation se juge isolément. |

**Règles propres au Kprim** (format le plus exposé aux ambiguïtés) :
- chaque affirmation est **absolument vraie ou absolument fausse** dans le cadre du cours, sans zone grise ;
- **aucun terme de fréquence vague** (« souvent », « parfois », « peut », « est associé à ») : chiffre, condition ou comparaison précise à la place ;
- les affirmations portent sur le **même objet** et sont de longueur comparable ;
- varier le nombre d'affirmations vraies (de 0 à 4).

**Répartition cible** (pas de quota officiel publié ; repères tirés de l'EDN, où le QRM domine, et de la littérature, où les questions à réponse unique s'avèrent plus faciles et plus sujettes aux indices que les formats à réponses multiples) :
- **QCM ≈ 50 %**, **QCS ≈ 35-40 %**, **Kprim ≈ 10-15 %** du paquet (tolérance ±10 points selon le cours).
- Dans les QCM, **varier le nombre de bonnes réponses** : viser grossièrement 1 bonne : 15 % · 2 : 35 % · 3 : 35 % · 4 : 15 %. Jamais une majorité écrasante d'un même nombre (ex. « toujours 3 bonnes sur 4 » se devine).

Champ `Réponses` : une valeur par proposition, dans l'ordre, séparées par un espace : `1 0 0 1` (1 = vrai, 0 = faux). En QCS, exactement un `1`.

⚠ Le modèle de carte de l'add-on **mélange l'ordre des propositions à l'affichage** (souhaité : évite la mémoire visuelle) : ne jamais désigner une proposition par son numéro dans les Informations complémentaires ; la citer par son texte (« « … » → faux : … »).

---

## 7. RÉDACTION

### Contexte, Titre, Question : trois niveaux, aucune répétition
Le recto affiche, dans l'ordre : `Contexte` (le cours), `Titre` (la partie du cours), `Question`. Chaque niveau apporte une information **nouvelle** :
- **Contexte** : le cours (cf. format ci-dessous). Ne pas le répéter ailleurs.
- **Titre** : la **section** du cours, suivie de la **notion** seulement si elle est différente de la section : `<Section>` ou `<Section> — <Notion>`. **Jamais** le nom du cours ni un mot déjà présent dans le Contexte.
- **Question** : uniquement ce qui est demandé, **sans reprendre** le nom du cours ni les mots du Titre (sauf le mot testé lui-même, ex. le nom d'un lobe ou d'un médicament).
- Exemples :
  - ✗ Titre « AVC — Épidémiologie — Épidémiologie » + Question « AVC en France — épidémiologie »
  - ✓ Titre « Épidémiologie » + Question « Rang parmi les causes de décès et de démence en France ? »
  - ✓ Titre « Anticoagulants — Surveillance » + Question « Examen biologique de surveillance d'un traitement par <u>AVK</u> ? »
- Contrôle automatique : un même mot significatif (≥ 5 lettres, hors mots outils) présent dans deux des trois niveaux est signalé et corrigé.

### Question (énoncé)
- Courte (fait isolé) ou longue (**vignette clinique**) ; peut contenir une **image** quand l'image est le support de la question (cf. §8).
- **Toute la question est en gras** (`<b>…</b>`) : c'est l'élément principal du recto ; le Titre est affiché de façon discrète (cf. §9, réglage du modèle).
- **Mot discriminant souligné** (`<u>…</u>`) : quand plusieurs cartes ont un énoncé identique à un mot près (frontal/pariétal, droit/gauche, hypo/hyper, adulte/enfant, AVK/héparine, membre supérieur/inférieur…), ce mot est souligné ; de même pour un mot **décisif** (négation, côté, délai, population, voie d'administration). Un ou deux mots soulignés au maximum par question. Contrôle automatique : les énoncés qui ne diffèrent que d'un ou deux mots doivent avoir ces mots soulignés.
- Le suffixe de format est ajouté automatiquement : « (une seule réponse) » / « (une ou plusieurs réponses) » / « (vrai ou faux pour chaque affirmation) ».
- **Ancre sémantique** : toute condition numérique/temporelle dit de quoi elle parle (« délai depuis la dernière prise », « délai depuis le début des symptômes », pas « délai »).
- **Anti-fuite** : aucun mot de l'énoncé ne doit se retrouver **seulement** dans la bonne réponse ; pas d'indice grammatical (accord, article) entre l'énoncé et une seule proposition.
- **Unicité** : deux questions du paquet ne doivent pas avoir le même énoncé pour des réponses différentes.
- Pas de double négation ; une négation éventuelle (« ne fait PAS partie ») en **gras majuscules**, avec des propositions courtes.
- HTML autorisé : `<b>`, `<i>`, `<u>`, `<br>`, `<img>`.

### Vignettes cliniques (tester l'application, pas seulement le rappel)
- **Objectif** : au moins **40 %** des questions portant sur des connaissances **I0 et I1** sont des vignettes (situation de patient → décision ou interprétation).
- **Crédibilité médicale stricte** — une vignette n'est **pas** une interprétation de Claude :
  - chaque élément clinique (âge, signes, délai, constantes, résultats) est **compatible avec le cours** ou avec une référence fiable citée ; la présentation est **typique**, pas un cas limite ;
  - la bonne réponse **découle directement d'une affirmation du cours** (ou d'une source citée), que l'explication cite ; aucun raisonnement diagnostique ou thérapeutique qui irait au-delà du cours ;
  - les valeurs chiffrées sont réalistes et cohérentes entre elles ; ne pas ajouter de données qui changeraient la réponse sans que le cours le dise ;
  - en cas de doute sur la crédibilité, ne pas faire la vignette (garder une question directe) ; la phase 2b vérifie chaque vignette.
- Préférer les exemples de patients **présents dans le cours** (ex. cas illustrés sur les diapos).
- **Angle infirmier** privilégié (rôle propre et sur prescription) — gabarits :
  - « M./Mme X, <âge>, <contexte>, présente <signes>. Quelle surveillance est prioritaire ? »
  - « … Quel élément vous fait appeler le médecin immédiatement ? »
  - « … Quelle est votre première action ? »
  - « … Avant d'administrer <traitement>, que vérifiez-vous ? »
  - « … Quelle installation / quel positionnement ? »
  - « … Quel signe évoque une complication ? »

### Propositions (Réponse 1 à 4)
- **Homogènes** : même registre, même nature (4 délais, 4 molécules, 4 signes…).
- **La bonne réponse ne se distingue pas par la forme** : **longueur** comparable (entre 0,7 et 1,3 fois la longueur moyenne des mauvaises réponses), **même niveau de précision et de nuance**. Si la bonne réponse a besoin d'une précision, en donner une de même ampleur aux mauvaises réponses. Contrôle automatique.
- **Chaque mauvaise réponse cible une confusion identifiée** : chiffre d'une autre diapo, autre type de pathologie, côté inversé, notion voisine, ancienne règle, erreur fréquente d'étudiant. **Test du bon sens** : si un étudiant qui n'a pas suivi le cours peut l'éliminer par simple bon sens, la remplacer. Les mauvaises réponses doivent **ressembler aux bonnes**.
- **Distracteurs chiffrés** : valeurs **proches** de la bonne (ex. 10/15/20/25 % ; 4/6/8/12 h ; 0,5/1/1,5/2 g ; 3,5/4/5/5,5 mmol/L) ou **mêmes valeurs permutées** pour les listes chiffrées ; jamais une valeur aberrante. Éviter toute valeur juste selon une autre source reconnue (ex. HbA1c < 7 % HAS) ou un autre passage du cours, sauf si l'énoncé précise le contexte.
- **Questions de définition** : les distracteurs sont les définitions de **termes proches** (même famille, même préfixe, notions souvent confondues, ex. : hypoxie/hypoxémie/hypercapnie ; dyspnée/dysphagie/dysphonie ; oligurie/anurie/dysurie ; tachycardie/tachypnée/tachyarythmie ; hypokaliémie/hyperkaliémie/hyponatrémie ; thrombus/embole/hématome ; myosis/mydriase).
- **Termes absolus** (« toujours », « jamais », « systématique », « uniquement », « tous », « aucun ») : autorisés, y compris comme **pièges légitimes**, mais **pas comme indice** :
  - à l'échelle du paquet, ils doivent apparaître aussi dans des propositions **vraies** (ex. « Jamais de KCl en IV directe », « Pas de sondage urinaire systématique ») ;
  - dans une même question, un terme absolu présent **uniquement** dans les mauvaises réponses doit être justifié (piège classique du cours) ; le contrôle automatique liste ces cas, la phase 2b les revoit.
- **Termes de fréquence vagues** (« souvent », « parfois », « rarement », « peut ») : à éviter dans les propositions ; les remplacer par un chiffre, une condition ou une comparaison.
- Interdits : « toutes les réponses », « aucune réponse », propositions absurdes ou humoristiques.
- Une proposition vraie l'est **dans le cadre du cours** ; si elle dépend d'une nuance, la préciser (et nuancer de la même façon les autres propositions).

### Erreurs dangereuses ⛔
- Une mauvaise réponse qui, appliquée en pratique, **mettrait le patient en danger** (équivalent des propositions « inacceptables » de l'EDN) est signalée dans les Informations complémentaires : `⛔ Erreur dangereuse : « <proposition> » — <pourquoi>` (ex. injecter du chlorure de potassium en IV directe, administrer de l'insuline sans contrôle glycémique, faire boire un patient dont la déglutition n'a pas été évaluée, injecter par voie IV un produit prévu pour la voie SC, donner un AINS à un patient sous anticoagulant sans avis médical).
- La question est alors classée **I0** (cf. §3).
- Inclure de telles propositions **volontairement** pour les gestes de sécurité du cours (ce sont les pièges les plus utiles pour un futur infirmier).

### Titre
- Court, sans la réponse, **sans le nom du cours** : `<Section>` ou `<Section> — <Notion>` si la notion diffère de la section (ex. « Prise en charge en urgence — Reperfusion », « Surveillance », « Effets indésirables — Hypokaliémie »). Affiché au recto, de façon discrète (cf. §9).

### Informations complémentaires
- **Explication** : le point clé à retenir (en citant l'affirmation du cours), puis pourquoi chaque proposition fausse est fausse quand ce n'est pas évident, en citant la proposition par son texte (jamais par son numéro, cf. §6).
- `⛔ Erreur dangereuse : …` (cf. ci-dessus).
- `✎ Modifié par rapport au cours : …` pour toute modification du contenu du cours (cf. §2.8).
- `⚠ Non confirmé : …` pour une information du cours gardée telle quelle mais non retrouvée ou contredite par les sources (cf. §2.7).
- `Complément : …` si une note de l'étudiant ou une source donne une autre valeur, une mise à jour utile ou une définition hors cours.
- **Glossaire** : une ligne de définition courte pour chaque terme technique ou sigle présent dans l'énoncé ou les propositions (`<b>Glossaire</b>` puis `<i>terme</i> : définition`). Maintenir un glossaire du cours (terme → motif de détection → définition) appliqué automatiquement à toutes les cartes.
- **Image de la page entière** du PDF d'où vient la connaissance (cf. §8).

### Sources
- Format (celui de la collection) : `<Type de cours> — <nom du fichier PDF>, p. <n>` (ex. `CM SSU — CM4 Insuffisance cardiaque.pdf, p. 13`) ; plusieurs pages : `p. 12-13` ; notes : `Notes perso (OneNote) — <titre>`.
- Source web : `Web — <Organisme>, <titre>, <URL>` (une par ligne, `<br>` entre les lignes).
- Dernière ligne : `Généré par Claude (<modèle>) — prompt v<version> — <AAAA-MM-JJ> — <id question>`.

### Contexte
- Format de la collection : `IFSI - UE <n° UE> <intitulé UE> - <type de cours> <intitulé du cours>` (ex. `IFSI - UE 2.11 Pharmacologie et thérapeutiques - CM IFSI Anticoagulants`). Affiché au recto : ne contient jamais la réponse.

---

## 8. IMAGES

- **Informations complémentaires** : toujours la **page entière** du PDF d'où vient la connaissance, en JPEG ~150 dpi. Une page = un seul fichier, réutilisé par toutes les questions qui en dépendent.
- Noms de fichiers uniques et stables, **en minuscules** (Anki met les noms de médias en minuscules ; une majuscule casse le lien), sans espaces ni accents : `<ue>_<cours>_p<NNN>.jpg` (ex. `ue2-11_cm2-anticoagulants_p013.jpg`).
- **Question** : une image de page entière seulement si elle ne contient pas la réponse (légendes, titres de diapo).
- **Questions d'imagerie** (scanner, IRM, ARM, ECG, radio, schéma à légender…) : **recadrage autorisé** sur le cliché seul, depuis l'image source intégrée au PDF (meilleure résolution), en excluant titres, légendes et annotations textuelles qui donnent la réponse (une flèche sans texte peut rester). Vérifier visuellement chaque recadrage. Nom : `<ue>_<cours>_img-<description>.jpg`. Ne pas utiliser un cliché coupé ou illisible.

---

## 9. FICHIERS DE SORTIE

**Type de note Anki : `QCMs`**. Ordre exact des champs :

| # | Champ | Contenu |
|---|---|---|
| 1 | Question | Énoncé (HTML) + éventuelle image |
| 2 | Titre | Titre court (affiché au recto) |
| 3 | Mode (0=kprim, 1=qcm, 2=qcu) | `0`, `1` ou `2` |
| 4 | Réponses (0=faux, 1=vrai) | ex. `1 0 0 1` |
| 5 | Sources | cf. §7 |
| 6 | Contexte | cf. §7 (affiché au recto) |
| 7 | Informations complémentaires | Explication, ⛔/✎/⚠/Complément, glossaire, image page entière |
| 8–11 | Réponse 1 à Réponse 4 | Propositions |
| 12–19 | Réponse 5 à Réponse 12 | vides |
| 20 | Tags | `PSB::Importance::I0` … `I3` |

**Réglage du modèle de carte QCMs** (à faire **une fois** par l'étudiant dans Anki sur PC : Outils → Gérer les types de notes → QCMs → Cartes ; s'applique à toutes les cartes QCMs) :
- *Style* — ajouter à la fin :
  ```css
  #myH1 { font-weight: normal; font-size: 16px; color: #555; }
  #myH1 + p { font-weight: bold; }
  ```
  (titre discret, question en gras même sans balise `<b>`).
- *Modèle recto* — en-têtes Kprim en français : remplacer `<tr><th>yes</th><th>no</th><th></th></tr>` par `<tr><th>Vrai</th><th>Faux</th><th></th></tr>`.
- Ne **jamais** modifier ce type de note depuis le paquet généré (il est partagé avec les autres paquets de l'étudiant).

**Livrable principal : un paquet Anki `.apkg`** contenant les notes **et les images** (Anki range lui-même les images dans `collection.media` ; double-clic pour importer).
- Le paquet réutilise **exactement** le type de note `QCMs` de l'étudiant (id `1604570191317`). Référence : `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Type de note QCMs.apkg`.
- Construction (bibliothèque Python `anki` ; scripts de référence dans `Anki\Prompts\Outils\`) : nouvelle collection → import du `.apkg` de référence → suppression de la note exemple → ajout des notes dans `[Paquet]` avec le tag d'importance → ajout des images → export `.apkg` avec médias, sans planification.
- **GUID stable** par note (ex. `ifsiqcm-` + hash de `<préfixe>-<id>`) : réimporter un paquet corrigé met à jour les cartes sans perdre la progression.
- Notes dans l'ordre du cours ; pas de retour à la ligne brut dans les champs (`<br>`).
- Nom : `<UE> - <Cours> - QCM - prompt v<version> - AAAA-MM-JJ.apkg` ; emplacement : `G:\Mon Drive\FOR\IFSI\Anki\Decks\<UE> - <Cours>\`.

**Fichiers joints** (même dossier) :
- `… - couverture.xlsx` : tableau de couverture (§5) + onglet des questions.
- `… - questions.tsv` : export texte (relecture rapide, secours ; en-têtes `#separator:tab`, `#html:true`, `#notetype:QCMs`, `#deck:<Paquet>`, `#tags column:20`).
- `… - relecture.md` : rapport de la phase 2b (concordance, signalements, corrections, justifications).

---

## 10. EXEMPLES

*(Contexte affiché au-dessus de chaque carte, non répété ici. Les exemples sont volontairement pris dans des domaines différents.)*

**QCS (fait unique)** — Mode `2` — `PSB::Importance::I0`
Titre : « Paramètres vitaux »
Q : « <b>Fréquence respiratoire normale de l'<u>adulte</u> au repos ?</b> »
R : 8 à 12 /min · **12 à 20 /min** · 20 à 25 /min · 25 à 30 /min *(valeurs proches, pas d'aberration ; « adulte » souligné car une carte voisine porte sur l'enfant)*

**QCS (liste complète)** — Mode `2` — `PSB::Importance::I0`
Titre : « Évaluation neurologique »
Q : « <b>Les 3 composantes du score de Glasgow ?</b> »
R : Ouverture des yeux ; réponse verbale ; réflexe pupillaire · Réponse motrice ; réponse verbale ; réflexe pupillaire · **Ouverture des yeux ; réponse verbale ; réponse motrice** · Ouverture des yeux ; réponse motrice ; tonus musculaire *(chaque élément de la bonne liste apparaît aussi dans les autres)*

**QCM (2 bonnes sur 4)** — Mode `1` — `PSB::Importance::I0`
Titre : « Hypoglycémie — Signes cliniques »
Q : « <b>Signes <u>adrénergiques</u> ?</b> »
R : **Sueurs** · **Palpitations** · Polyurie · Soif intense
Infos : « « Polyurie » et « Soif intense » → faux : signes d'hyperglycémie (confusion hypo/hyper ciblée). »

**Kprim** — Mode `0` — `PSB::Importance::I0`
Titre : « Antalgiques de palier 1 »
Q : « <b><u>Paracétamol</u> : vrai ou faux ?</b> »
R : **Antalgique de palier 1** (V) · **Antipyrétique** (V) · Anti-inflammatoire aux doses usuelles (F) · **Hépatotoxique en cas de surdosage** (V)

**Vignette (QCS, angle infirmier)** — Mode `2` — `PSB::Importance::I0`
Titre : « Hypoglycémie — Conduite à tenir »
Q : « <b>M. D., 62 ans, diabétique sous insuline, présente des sueurs et des tremblements avant le repas. Il est conscient et avale normalement ; glycémie capillaire : 0,50 g/L. Votre <u>première</u> action ?</b> »
R : Injecter l'insuline prévue avant le repas · **Resucrage oral (15 g de sucre rapide) puis contrôle de la glycémie à 15 min** · Injection de glucagon en IM · Attendre le repas prévu dans 30 min
Infos : « Cours p. X : « patient conscient → resucrage per os, contrôle à 15 min ». Le glucagon est réservé au patient inconscient ou qui ne peut pas avaler. ⛔ Erreur dangereuse : « Injecter l'insuline prévue avant le repas » — aggrave l'hypoglycémie. » *(la vignette ne contient que des éléments cohérents avec le cours ; la réponse découle d'une phrase du cours citée)*

---

## 11. CONTRÔLES AUTOMATIQUES ET CHECKLIST

**Bloquants** (le script de construction refuse de produire le paquet) :
- [ ] Chaque connaissance de l'inventaire a au moins une question.
- [ ] 4 propositions, toutes différentes ; `Réponses` cohérent avec le `Mode` (QCS = un seul `1`, QCM ≥ un `1`, Kprim : 0 à 4 `1`).
- [ ] Pas d'énoncé dupliqué ; pas de renvoi à une proposition par son numéro dans les explications.
- [ ] Longueur de la bonne réponse (QCS) ≤ 1,3 fois la longueur moyenne des mauvaises, quand celles-ci font au moins 12 caractères (exception justifiée et listée) ; une bonne réponse nettement plus courte est seulement rapportée (ce n'est pas l'indice classique).
- [ ] Aucun mot significatif répété entre Contexte, Titre et Question (hors mot testé) ; le Titre ne contient pas le nom du cours.
- [ ] Question entièrement en gras ; énoncés qui ne diffèrent que d'un ou deux mots → ces mots soulignés ; au plus deux mots soulignés par question.

**Rapportés** (listés dans le rapport de phase 3, revus en phase 2b) :
- [ ] Termes absolus présents uniquement dans les mauvaises réponses d'une question ; équilibre vrai/faux des termes absolus sur le paquet.
- [ ] Termes de fréquence vagues dans les propositions.
- [ ] Mot de l'énoncé repris uniquement dans la bonne réponse.
- [ ] Répartition des formats (≈ 50 % QCM / 35-40 % QCS / 10-15 % Kprim) et du nombre de bonnes réponses dans les QCM et Kprim.
- [ ] Termes de fréquence vagues dans les Kprim (bloquant pour le Kprim).
- [ ] Part de vignettes parmi les questions I0/I1 (≥ 40 %).
- [ ] Questions avec ⛔ toutes en I0.

**Checklist de rédaction** :
- [ ] Bonnes réponses conformes au cours (ou à une source citée) ; distracteurs faux sans ambiguïté, chacun ciblant une confusion.
- [ ] Vignettes crédibles, réponse découlant d'une affirmation du cours citée dans l'explication.
- [ ] Chaque modification tracée (`✎`), chaque info non confirmée signalée (`⚠`), chaque erreur dangereuse signalée (`⛔`).
- [ ] Pas de fuite de la réponse dans l'énoncé, le titre ou le contexte.
- [ ] Importance cohérente et identique pour toutes les questions d'une même connaissance (sauf passage en I0 pour ⛔).
- [ ] Sources (fichier + page) et Contexte au bon format ; image page entière présente ; recadrages vérifiés.
- [ ] Phase 2b réalisée ; discordances corrigées ou justifiées.
- [ ] `.apkg` testé (réimport dans une collection vierge : bon type de note, bon paquet, images présentes, pas de doublon à la réimportation).
