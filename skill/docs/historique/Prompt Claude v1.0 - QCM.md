# PROMPT DE GÉNÉRATION DE QCM ANKI — v1.0

> À utiliser à chaque génération. Remplace les prompts v0.1 / v0.2 (cartes Basic/Cloze).
> Historique : v1.0 (2026-11-10) création · v1.0a (2026-11-10, test CM6 AVC) vérifications web en phase 1, traçabilité des modifications et avertissements, chiffres diapo/notes distincts, numérotation INC-/Q-/D- du rapport ; livraison en .apkg (type QCMs + images) ; contrôle de couverture bloquant ; propositions mélangées par l'add-on (pas de renvoi par numéro) ; noms d'images en minuscules. Retour d'expérience CM6 AVC (29 pages) : estimation de phase 1 à 180 questions, résultat 267 une fois l'inventaire détaillé (151 connaissances) → en phase 1, estimer à partir de l'inventaire détaillé, pas du tableau condensé.
> Exécution prévue : Claude avec accès au dossier `G:\Mon Drive\FOR\IFSI` (lecture des PDF, rendu des pages en image, écriture des fichiers d'import).

---

## 1. PROFIL ET CONTRAINTES

- **Qui** : étudiant infirmier en 2e année d'IFSI (L2). Également réserviste militaire, secouriste à la Protection Civile (Paris) et triathlète → **temps de travail personnel très limité**.
- **Enseignements** :
  - CM majoritairement délivrés par la faculté de médecine (« CM SSU »), parfois par l'IFSI (« CM IFSI ») ; souvent plus denses que le niveau attendu d'un infirmier.
  - TD / TPG pilotés par les formateurs IFSI, centrés sur le métier.
- **Finalités** : examens semestriels (QCS, QCM, Kprim), stages, pratique professionnelle.
- **Ancienne méthode** : fiches Anki manuelles → trop chronophage à créer et relire.
- **Objectif du système** : à partir d'un cours, produire un paquet de QCM **prêt à importer**, qui couvre **toutes** les connaissances du cours, classées par importance, avec un minimum de relecture.

---

## 2. SOURCES — HIÉRARCHIE ET RÈGLES

1. **PDF du CM** : source principale. Il peut contenir les diapos ET les prises de notes de l'étudiant (texte tapé, annotations PDF, notes intercalées entre les diapos). Lire **le texte ET les images** de chaque page (le contenu des diapos est souvent uniquement en image).
2. **Prises de notes** (OneNote exporté, annotations dans le PDF, fichier joint) : complément. En cas de contradiction avec la diapo → le signaler en phase 1, ne pas trancher seul.
3. **Recherche Internet** : autorisée **ponctuellement**, uniquement sur des sources fiables, pour :
   - combler une information incomplète, ambiguë ou manifestement erronée dans le cours (faute de frappe, chiffre manquant) ;
   - vérifier qu'une réponse est juste ;
   - construire des distracteurs plausibles mais faux.
   Sources acceptées (par ordre de préférence) : HAS, ANSM, Santé publique France, Légifrance, sociétés savantes (SFNV, SFC, SFMU, SPLF…), Collèges des enseignants (ex. CEN), Vidal/base de données publique des médicaments, référentiels IFSI officiels, manuels universitaires. **Pas** de forums, blogs, sites de fiches non sourcés, Wikipédia comme seule source.
   Toute info tirée d'Internet est **citée dans le champ Sources** (organisme, titre, URL).
4. **Questions à l'étudiant** : si un point reste douteux après recherche, poser la question (en phase 1) plutôt que deviner.
5. **Interdit** : inventer une connaissance. Les **bonnes réponses** viennent du cours (ou d'une source web citée et validée en phase 1). Les **mauvaises réponses** peuvent utiliser des connaissances hors cours (voir §7).
6. **Quand faire les vérifications** : toutes les vérifications web portant sur le **contenu** (incohérences, chiffres douteux, seuils, corrections) se font **en phase 1**, et leur résultat est présenté dans le rapport de phase 1. En phase 2, la recherche web ne sert plus qu'à valider des **distracteurs**.
7. **Information du cours non confirmée** : si une information écrite dans le cours (diapo ou notes) n'est pas retrouvée ou est contredite par les sources fiables, on la **garde** telle qu'elle est écrite, avec un avertissement dans les Informations complémentaires : `⚠ Non confirmé : <ce que disent les sources consultées>`.
8. **Toute modification par rapport au cours** (correction d'une erreur, reformulation qui change le sens, chiffre complété ou mis à jour) est **tracée dans les Informations complémentaires** : `✎ Modifié par rapport au cours : « <texte du cours> » → « <texte retenu> » (<source>)`. Seules les fautes de frappe évidentes sont corrigées sans trace.
9. **Chiffres différents entre la diapo et les notes** (ex. −20 % vs −30 %) : vérifier s'ils portent sur des choses différentes (critère, délai, population) ; si oui, **une question distincte pour chacun**, chacune précisant ce que mesure le chiffre ; sinon, le signaler en incohérence.

---

## 3. ÉCHELLE D'IMPORTANCE (tag `PSB::Importance::I0` à `I3`)

| Niveau | Définition | Exemples de connaissances |
|---|---|---|
| **I0** | À connaître **par cœur**, rappel **instinctif** pour tout étudiant infirmier, quel que soit le service. | Normes des constantes, signes d'alerte d'une urgence vitale, gestes et réflexes de sécurité, définitions fondamentales, règles d'administration, contre-indications majeures. |
| **I1** | Important pour tout infirmier, mais on peut prendre **quelques secondes à quelques dizaines de secondes** pour s'en rappeler. | Mécanismes physiopathologiques de base, principaux examens et leur but, complications fréquentes, surveillance infirmière courante. |
| **I2** | Connaissance **de spécialité** : indispensable dans un service donné (stage de cardio, neuro, pneumo…), non attendue ailleurs (ex. EHPAD). | Délais de thrombolyse en neuro, scores spécifiques d'un service, traitements spécialisés, surveillance spécifique. |
| **I3** | Spécifique à l'**UE et à l'examen à venir** ; pas besoin de la réviser entre les examens. | Chiffres épidémiologiques précis, détails anatomiques fins, éponymes, classifications détaillées, détails cités « pour l'examen ». |

Règles :
- En cas d'hésitation entre deux niveaux, choisir le **plus important** (le plus petit chiffre) si une erreur sur cette connaissance peut mettre un patient en danger ; sinon le moins important.
- Une mention du professeur du type « pas à connaître par cœur » → I3 (et le signaler) ; la connaissance est **quand même** fichée. Si ce sont des seuils ou une classification, les vérifier en ligne en phase 1 et faire une question par seuil.
- Une même connaissance garde le même niveau dans toutes ses questions.

---

## 4. PROCESSUS

### PHASE 1 — ANALYSE ET DIALOGUE (OBLIGATOIRE, attendre la validation)

1. Lire **intégralement** le PDF : texte de chaque page **et** rendu visuel de chaque page (diapos, schémas, tableaux, imagerie), ainsi que les notes jointes.
2. Présenter à l'étudiant :
   - **Variables du cours** proposées : `[UE]`, `[Cours]`, `[Type de cours]` (CM SSU / CM IFSI / TD), `[Contexte]`, `[Paquet]`, `[Spécialité]`.
     Format du paquet : `IFSI::QCM::Semestre <n>::UE <n°> - <intitulé UE>::<Cours>` (ex. `IFSI::QCM::Semestre 3::UE 2.8 - Processus obstructifs::CM6 - AVC`).
   - **Résumé structuré** du cours (plan par sections, avec n° de pages).
   - **Inventaire des connaissances** par section, avec l'**importance proposée** (I0–I3) pour chacune, sous forme de tableau compact.
   - **Estimation du nombre de questions**, au total et par importance (aucune limite a priori : un cours riche en vocabulaire peut demander beaucoup de questions ; un cours léger peut n'en donner que ~50).
   - **Tableaux / figures / imagerie** : lesquels transformer en questions, lesquels utiliser comme image dans la question.
   - **Incohérences, erreurs ou trous** détectés (chiffres manquants, contradictions notes/diapo, informations douteuses), **déjà vérifiés en ligne** : pour chacun, ce que disent les sources (citées) et le traitement proposé (corrigé et tracé, gardé avec avertissement, ou question distincte).
   - **Doutes** sur l'utilité d'une info pour un infirmier ou pour l'examen.
   - **Questions** à l'étudiant, y compris le **nombre de questions souhaité** pour ce cours.
3. **Numérotation du rapport** : chaque liste a son propre préfixe pour que l'étudiant puisse répondre sans ambiguïté :
   - incohérences : `INC-1`, `INC-2`… ;
   - questions à l'étudiant : `Q-1`, `Q-2`… (toute décision attendue de l'étudiant figure dans cette liste, rien n'est demandé ailleurs dans le rapport) ;
   - doutes : `D-1`, `D-2`….
   Ne pas utiliser `I1`, `I2`… (réservés à l'importance).
4. **Attendre** la validation et les compléments avant la phase 2.

### PHASE 2 — GÉNÉRATION

1. Générer les QCM selon les règles ci-dessous, **dans l'ordre du cours** (ordre des pages).
2. Rendre les pages utilisées en images (cf. §8).
3. Produire les fichiers d'import (cf. §9).
4. Passer la **checklist** (§11) sur chaque question ; corriger avant livraison.

### PHASE 3 — LIVRAISON ET RETOUR

- Résumé : nombre de questions par importance et par mode, points signalés `À VÉRIFIER`, sources web utilisées.
- Après les retours de l'étudiant : proposer des **améliorations du prompt**, en le gardant **universel** (toutes matières, tous cours).

---

## 5. COUVERTURE

- **Toutes** les connaissances du cours sont fichées, y compris I3.
- Nombre de questions par connaissance, selon l'importance :
  - **I0** : 2 à 3 questions sous des **angles différents** (sens direct, sens inverse, mini situation clinique, format différent).
  - **I1** : 1 à 2 questions.
  - **I2 / I3** : 1 question.
- Le **vocabulaire** (définitions, sigles, termes médicaux) fait l'objet de questions dédiées — y compris les termes **employés dans le cours sans y être définis** : définition hors cours (connaissance générale ou source fiable), marquée `Complément : définition hors cours` ; ces termes ont leur propre ligne dans l'inventaire (section « Vocabulaire », identifiants `V01`…), importance I0 à I3 selon l'usage infirmier.
- Une même connaissance peut apparaître en QCS puis être réutilisée dans un QCM ou un Kprim : c'est souhaité.
- Le nombre final est validé avec l'étudiant en phase 1.

### Contrôle de couverture (obligatoire, bloquant)
- L'inventaire **détaillé** des connaissances (une ligne par connaissance, identifiant `K-001`, `K-002`…) est établi avant la rédaction ; le tableau de la phase 1 peut être condensé, pas celui-ci.
- Chaque question porte la (ou les) connaissance(s) qu'elle teste.
- Avant livraison, produire le **tableau de couverture** : `K-id | page | connaissance | importance | questions (ids)`. Toute connaissance sans question **bloque la livraison** : ajouter la question manquante.
- Seuls les éléments qui ne sont pas des connaissances (diapo « Objectifs », illustrations décoratives) sont exclus, et listés comme tels en bas du tableau.

---

## 6. FORMATS DE QUESTION (champ `Mode`)

L'add-on Multiple Choice gère trois modes. Toujours **4 propositions** (Réponse 1 à 4 ; Réponse 5 à 12 laissées vides).

| Mode | Valeur | Règle | Quand l'utiliser |
|---|---|---|---|
| **Kprim** | `0` | 4 propositions, chacune vraie ou fausse ; il faut juger les 4 correctement. | Caractéristiques multiples d'un même objet (indications, effets, signes) où chaque proposition compte. |
| **QCM** | `1` | 1 à 4 bonnes réponses. | Listes, critères, signes, causes, facteurs de risque. |
| **QCS / QCU** | `2` | Exactement 1 bonne réponse. | Fait unique (valeur, délai, définition, localisation), **ou liste complète** : 4 listes différentes, une seule est correcte. |

Répartition : variée, sans quota fixe, en choisissant le format qui teste le mieux la connaissance. Varier les formats sur l'ensemble du paquet (les examens de la fac mélangent QCS, QCM et Kprim).

Champ `Réponses` : une valeur par proposition, dans l'ordre, séparées par un espace : `1 0 0 1` (1 = vrai, 0 = faux). En QCS, exactement un `1`. Varier la position de la bonne réponse.

⚠ Le modèle de carte de l'add-on **mélange l'ordre des propositions à l'affichage** : ne jamais désigner une proposition par son numéro (« 2. Faux ») dans les Informations complémentaires ; la citer par son texte (« « … » → faux : … »).

---

## 7. RÉDACTION

### Question (énoncé)
- Peut être courte ou longue (vignette clinique) ; peut contenir une **image** (schéma, imagerie, tableau) quand l'image est le support de la question.
- Commence par un **contexte** non ambigu : `<Thème> — <aspect testé>` (ex. « AVC ischémique — Thrombolyse : délai maximal après le début des symptômes ? »).
- Indiquer la nature de la réponse attendue si utile : « (une seule réponse) », « (une ou plusieurs réponses) », « vrai/faux pour chaque proposition ».
- **Ancre sémantique** : toute condition numérique/temporelle dit de quoi elle parle (« délai depuis le début des symptômes », pas « délai »).
- **Anti-fuite** : aucun mot de l'énoncé ne doit désigner la bonne réponse ; pas d'indice grammatical (accord, article) entre l'énoncé et une seule proposition.
- **Unicité** : deux questions du paquet ne doivent pas avoir le même énoncé pour des réponses différentes.
- Pas de double négation ; une négation éventuelle (« ne fait PAS partie ») en **gras majuscules**.
- HTML autorisé : `<b>`, `<i>`, `<u>`, `<br>`, `<img>`. Mettre en gras l'aspect testé.

### Propositions (Réponse 1 à 4)
- **Homogènes** : même registre, même longueur approximative, même nature (4 délais, 4 molécules, 4 signes…).
- **Distracteurs** : plausibles, idéalement tirés du **même cours** ou de notions voisines (confusions classiques : ischémique/hémorragique, droite/gauche, hyper/hypo, valeurs proches, délais voisins). Ils peuvent s'appuyer sur des connaissances hors PDF, mais doivent être **faux sans aucune ambiguïté** au regard du cours et des sources fiables.
- **Distracteurs chiffrés** (pourcentages, délais, seuils, doses, rangs) : valeurs **proches** de la bonne (ex. 10/15/20/25 %, 3 h/4h30/6 h/9 h) ou **mêmes valeurs permutées** pour les listes chiffrées ; jamais une valeur aberrante qui s'élimine d'un coup d'œil. Éviter toute valeur qui serait juste selon une autre source reconnue (ex. HbA1c < 7 % HAS) ou un autre passage du cours, sauf si l'énoncé précise clairement le contexte.
- **Questions de définition** : les distracteurs sont les définitions de **termes proches** (même famille, même préfixe, notions souvent confondues : thrombus/embole/athérome/hématome ; myosis/mydriase ; thrombopénie/thrombophilie/thrombocytose ; ataxie/apraxie/aphasie).
- Interdits : « toutes les réponses », « aucune réponse », propositions absurdes, absolus révélateurs (« toujours », « jamais ») utilisés seulement dans les fausses réponses.
- Une proposition vraie l'est **dans le cadre du cours** ; si elle dépend d'une nuance, la préciser.

### Titre
- Court, sans la réponse : `<Cours> — <section> — <notion>` (ex. « AVC — Prise en charge en urgence — Thrombolyse »).

### Informations complémentaires
- **Explication** : le point clé à retenir, puis pourquoi chaque proposition fausse est fausse quand ce n'est pas évident, en citant la proposition par son texte (jamais par son numéro, cf. §6).
- Si une info vient d'Internet : le dire explicitement (« Complément web : … »).
- **Glossaire** : une ligne de définition courte pour chaque terme technique ou sigle présent dans l'énoncé ou les propositions (`<b>Glossaire</b>` puis `<i>terme</i> : définition`). Maintenir un glossaire du cours (terme → motif de détection → définition) appliqué automatiquement à toutes les cartes.
- **Image de la page entière** du PDF d'où vient la connaissance (cf. §8).
- `✎ Modifié par rapport au cours : …` pour toute modification du contenu du cours (cf. §2.8).
- `⚠ Non confirmé : …` pour une information du cours gardée telle quelle mais non retrouvée ou contredite par les sources (cf. §2.7).
- `Complément : …` si une note de l'étudiant ou une source donne une autre valeur ou une mise à jour utile (ex. repère actuel différent d'une diapo ancienne).

### Sources
- Format (reprendre celui de la collection) : `<Type de cours> — <nom du fichier PDF>, p. <n>`
  ex. `CM SSU — CM6 AVC.pdf, p. 13`
- Plusieurs pages : `p. 12-13`. Notes : `Notes perso (OneNote) — <titre>`.
- Source web : `Web — <Organisme>, <titre>, <URL>` (une par ligne, `<br>` entre les lignes).
- Dernière ligne : `Généré par Claude (<modèle>) — prompt v1.0 — <AAAA-MM-JJ>`.

### Contexte
- Format de la collection : `IFSI - UE <n° UE> <intitulé UE> - <type de cours> <intitulé du cours>`
  ex. `IFSI - UE 2.8 Processus obstructifs - CM SSU AVC`

---

## 8. IMAGES

- Toujours la **page entière** du PDF (pas de recadrage), rendue en image.
- Format : JPEG ~150 dpi (lisible sur téléphone, poids raisonnable).
- Nom de fichier unique et stable, **en minuscules** (Anki met les noms de médias en minuscules à l'ajout ; une majuscule casse le lien), sans espaces ni accents : `<ue>_<cours>_p<NNN>.jpg` (ex. `ue2-8_cm6-avc_p013.jpg`).
- Dans `Informations complémentaires` : `<img src="ue2-8_cm6-avc_p013.jpg">`.
- Image dans la `Question` : seulement si la page entière ne contient pas la réponse (légendes, titres de diapo). Sinon, pas d'image de page dans la question.
- **Exception — questions d'imagerie** (scanner, IRM, ARM, ECG, radio…) : **recadrage autorisé** sur le cliché seul, en excluant titres, légendes et annotations textuelles qui donnent la réponse (une flèche sans texte peut rester). Recadrer depuis l'image source intégrée au PDF (meilleure résolution), vérifier visuellement chaque recadrage. Nom : `<ue>_<cours>_img-<description>.jpg`. La page entière reste dans les Informations complémentaires. Ne pas utiliser un cliché coupé ou illisible.
- Dans `Question` : seulement si l'image est le support (schéma à interpréter, imagerie, tableau) ; même image page entière.
- Une page = un seul fichier image, réutilisé par toutes les questions qui en dépendent.

---

## 9. FICHIERS DE SORTIE

**Type de note Anki : `QCMs`**. Ordre exact des champs :

| # | Champ | Contenu |
|---|---|---|
| 1 | Question | Énoncé (HTML) |
| 2 | Titre | Titre court |
| 3 | Mode (0=kprim, 1=qcm, 2=qcu) | `0`, `1` ou `2` |
| 4 | Réponses (0=faux, 1=vrai) | ex. `1 0 0 1` |
| 5 | Sources | cf. §7 |
| 6 | Contexte | cf. §7 |
| 7 | Informations complémentaires | Explication + image page entière |
| 8–11 | Réponse 1 à Réponse 4 | Propositions |
| 12–19 | Réponse 5 à Réponse 12 | vides |
| 20 | Tags | `PSB::Importance::I0` … `I3` |

Note : le modèle de carte affiche `Titre` et `Contexte` **au recto** → ils ne doivent jamais contenir la réponse.

**Livrable principal : un paquet Anki `.apkg`** contenant les notes **et les images** (Anki range lui-même les images dans `collection.media` à l'import ; double-clic pour importer).
- Le paquet réutilise **exactement** le type de note `QCMs` de l'étudiant (id `1604570191317`), pour que les notes s'ajoutent au type existant et non à une copie. Référence du type : `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Type de note QCMs.apkg` (export d'une note QCMs).
- Construction (bibliothèque Python `anki`) : nouvelle collection → import du `.apkg` de référence → suppression de la note exemple → ajout des notes dans le paquet `[Paquet]` avec le tag d'importance → ajout des images au dossier média → export `.apkg` avec médias, sans planification.
- Une ligne de note = une question, dans l'ordre du cours ; pas de retour à la ligne brut dans les champs (`<br>`).
- Nom : `<UE> - <Cours> - QCM - prompt v<version> - AAAA-MM-JJ.apkg`
- Emplacement : `G:\Mon Drive\FOR\IFSI\Anki\Decks\<UE> - <Cours>\`.

**Fichiers joints** (même dossier) :
- `… - couverture.xlsx` : tableau de couverture (cf. §5).
- `… - questions.tsv` : export texte des questions (relecture rapide, secours en cas de problème d'import ; en-têtes Anki `#separator:tab`, `#html:true`, `#notetype:QCMs`, `#deck:<Paquet>`, `#tags column:20`).

---

## 10. EXEMPLES

**QCS (fait unique)** — Mode `2` — Réponses `0 1 0 0` — `PSB::Importance::I0`
Q : « Paramètres vitaux — <b>Fréquence respiratoire normale</b> chez l'adulte au repos ? (une seule réponse) »
R1 : 6 à 10 /min · R2 : 12 à 20 /min · R3 : 22 à 30 /min · R4 : 30 à 40 /min

**QCS (liste complète)** — Mode `2` — Réponses `0 0 1 0` — `PSB::Importance::I0`
Q : « Score de Glasgow — <b>3 composantes évaluées</b> ? (une seule réponse) »
R1 : Ouverture des yeux ; réponse verbale ; réflexe pupillaire
R2 : Réponse motrice ; réponse verbale ; fréquence respiratoire
R3 : Ouverture des yeux ; réponse verbale ; réponse motrice
R4 : Ouverture des yeux ; réponse motrice ; tonus musculaire

**QCM (une ou plusieurs)** — Mode `1` — Réponses `1 1 0 1` — `PSB::Importance::I0`
Q : « Hypoglycémie — <b>signes adrénergiques</b> évocateurs ? (une ou plusieurs réponses) »
R1 : Sueurs · R2 : Tremblements · R3 : Polyurie · R4 : Palpitations
Infos : « 3. Faux : la polyurie évoque l'hyperglycémie. »

**Kprim** — Mode `0` — Réponses `1 1 0 1` — `PSB::Importance::I0`
Q : « Paracétamol — vrai ou faux pour chaque proposition ? »
R1 : Antalgique de palier 1 · R2 : Antipyrétique · R3 : Anti-inflammatoire · R4 : Hépatotoxique en cas de surdosage

---

## 11. CHECKLIST AVANT LIVRAISON

- [ ] Toutes les connaissances de l'inventaire validé en phase 1 sont couvertes.
- [ ] Chaque question a exactement 4 propositions ; `Réponses` a 4 valeurs cohérentes avec le `Mode` (QCS = un seul `1`).
- [ ] Bonnes réponses conformes au cours (ou à une source web citée) ; distracteurs faux sans ambiguïté.
- [ ] Chaque modification par rapport au cours est tracée (`✎`) et chaque info non confirmée signalée (`⚠`) dans les Informations complémentaires.
- [ ] Pas de fuite de la réponse dans l'énoncé ni dans le titre.
- [ ] Propositions homogènes ; position de la bonne réponse variée.
- [ ] Importance cohérente avec l'échelle et identique pour toutes les questions d'une même connaissance.
- [ ] Sources (fichier + page) et Contexte remplis au bon format ; image page entière présente.
- [ ] Tableau de couverture complet : aucune connaissance sans question.
- [ ] Ordre des notes = ordre du cours ; `.apkg` testé (réimport dans une collection vierge : bon type de note, bon paquet, images présentes).
