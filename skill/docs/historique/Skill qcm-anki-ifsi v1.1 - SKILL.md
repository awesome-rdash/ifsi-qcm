---
name: qcm-anki-ifsi
description: Génère un paquet Anki de QCM (type QCMs, importance I0-I3, images) à partir d'un cours PDF d'IFSI, avec phase d'analyse, relecture indépendante et contrôles. À utiliser pour créer ou corriger des QCM Anki à partir d'un cours.
---

# QCM Anki à partir d'un cours IFSI

Produire, à partir d'un cours (PDF de diapos + prises de notes), un **paquet Anki `.apkg` prêt à importer** qui couvre **toutes** les connaissances du cours, classées par importance, et qui soit difficile à réussir par simple ruse.

L'étudiant est en 2e année d'IFSI et a très peu de temps : le résultat doit être utilisable sans retouche. Les consignes valent **pour tout cours et toute UE**.
Le **pourquoi** de chaque règle et l'historique sont dans `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Historique et décisions - QCM Anki IFSI.md` : le lire en cas de doute sur une règle, et y **ajouter une ligne** pour chaque nouvelle décision.

## Mise en place
- Dossier de l'étudiant : `G:\Mon Drive\FOR\IFSI` (cours dans `UE\Semestre <n>\…`, paquets dans `Anki\Decks\`).
- Organisation de l'espace de travail (copier depuis le Drive) :
  ```
  Outils/                      ← Anki\Prompts\Outils\ (build.py, common.py, glossaire.py)
  Type de note QCMs.apkg       ← Anki\Prompts\
  <cours>/                     ← un dossier par cours : PDF + notes, cours.py, k.py, fichiers de questions
  ```
  Modèle complet : `Anki\Prompts\Outils\exemple CM6 AVC\`. Les chemins de `cours.py` sont relatifs au dossier du cours. Commande : `python3 Outils/build.py <cours> [--report-only]`.
- `pip install anki pymupdf openpyxl --break-system-packages` si ces bibliothèques manquent.
- Modèle conseillé : Claude Opus (exactitude médicale des mauvaises réponses).

## Sources
1. **PDF du cours** = source principale. Lire **le texte ET le rendu image de chaque page** (le contenu des diapos est souvent uniquement en image).
2. **Notes** de l'étudiant = complément. Une contradiction avec la diapo se signale en phase 1.
3. **Web** : ponctuel, sources fiables uniquement (HAS, ANSM, Santé publique France, Légifrance, sociétés savantes, Collèges des enseignants, Vidal, manuels universitaires), **citées** dans le champ Sources.
4. Ne jamais inventer une connaissance. Les **bonnes réponses** viennent du cours ou d'une source validée en phase 1. Les **mauvaises réponses** peuvent venir d'ailleurs, mais doivent être fausses sans aucune ambiguïté.
5. Information du cours non confirmée → **gardée**, avec `⚠ Non confirmé : …`.
6. Toute modification du cours → **tracée** : `✎ Modifié par rapport au cours : « … » → « … » (source)`. Seules les fautes de frappe se corrigent sans trace.
7. Chiffres différents entre la diapo et les notes qui mesurent des choses différentes → une question pour chacun.

## Importance (tag `PSB::Importance::I0` … `I3`)
- **I0** : par cœur, rappel instinctif, tout service (constantes, signes d'urgence, sécurité, contre-indications majeures).
- **I1** : important, rappel en quelques secondes.
- **I2** : spécialité (indispensable dans un service donné).
- **I3** : spécifique à l'UE et à l'examen.
- En cas d'hésitation, choisir le niveau le plus important si une erreur peut mettre un patient en danger.
- « Pas à connaître par cœur » → I3, mais la connaissance est quand même fichée.
- Une question avec une erreur dangereuse ⛔ → **I0**.
- Pas d'autres tags.

## Processus

### Phase 1 — Analyse (obligatoire, attendre la validation)
Lire tout le cours, faire les vérifications web nécessaires, puis présenter :
- **les variables** :
  - UE, cours, type (`CM SSU`, `CM IFSI` ou `TD`) ;
  - Contexte : `IFSI - UE <n°> <intitulé> - <type> <cours>` ;
  - Paquet : `IFSI::QCM::Semestre <n>::UE <n°> - <intitulé>::<Cours>` ;
- **le plan** du cours, avec les pages ;
- **l'inventaire** des connaissances avec leur importance (tableau condensé) ;
- **l'estimation du nombre de questions**, calculée à partir de l'inventaire **détaillé** (aucune limite de volume) ;
- les figures et l'imagerie à exploiter ;
- les situations cliniques envisagées pour les vignettes ;
- **les incohérences, déjà vérifiées en ligne**, avec le traitement proposé ;
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
1. Inventaire détaillé dans `k.py` : une ligne par connaissance, `(id, pages, importance, section, texte)`. Les identifiants sont `K001…` ; les termes employés sans être définis sont `V01…`, en section « Vocabulaire ». Ajouter `EXCLUS` (ce qui n'est pas une connaissance, ex. diapo « Objectifs »).
2. Questions dans un ou plusieurs fichiers Python (`QS = [Q(...)]`, cf. `common.py`), **dans l'ordre du cours**. Champs de `Q` :
   - `id`, `ks` (connaissances testées, séparées par des espaces) ;
   - `mode` : 0 = Kprim, 1 = QCM, 2 = QCS ;
   - `q`, `props` (4 propositions), `truth` (ex. `"0110"`) ;
   - `expl`, `notion` ;
   - `x` (`✎` / `⚠` / `Complément`), `w` (sources web) ;
   - `img` (cliché recadré : xref, cadre, nom), `pg` (pages en plus) ;
   - `dz` (erreurs dangereuses : `{index: raison}`) ;
   - `allow`, `lenok` (exceptions justifiées), `vign` (vignette).
3. `cours.py` : NOM, PDF, PDFNAME, TYPE, CONTEXTE, DECK, PREFIX (minuscules, sans espace), MODEL, VERSION, REF_APKG, QFILES, CORRECTIONS. Si besoin, ajouter `glossaire_cours.py` avec `EXTRA = [(terme, motif, définition)]`.
4. `python3 Outils/build.py <cours> --report-only` → corriger jusqu'à **zéro blocage**, puis revoir le rapport.

### Phase 2b — Relecture indépendante (obligatoire)
- Des **sous-agents séparés** (un lot d'environ 100 questions chacun) reçoivent dans un dossier isolé :
  - le texte du cours, les pages en image et les clichés des questions ;
  - les questions **sans clés ni explications** : titre, énoncé, propositions, format.
- Chacun répond à chaque question et signale : `erreur_medicale`, `ambigu`, `hors_cours`, `vignette_non_credible`, `distracteur_faible`, `indice`, `formulation`.
- Comparer leurs réponses aux clés. Chaque discordance ou signalement de fond est corrigé (dans un dictionnaire de corrections listé dans `CORRECTIONS`) ou justifié dans `… - relecture.md`.

### Phase 3 — Livraison
- `python3 Outils/build.py <cours>` produit :
  - `.apkg`, avec les images et le type de note QCMs d'id `1604570191317` ;
  - `- questions.tsv` ;
  - `- couverture.xlsx` ;
  - `stats.json`.
- **Tester** : réimporter deux fois dans une collection vierge. Vérifier un seul type QCMs, le bon paquet, les images présentes, aucun doublon.
- Déposer tous les fichiers dans `Anki\Decks\<UE> - <Cours>\`, avec `relecture.md`.
- Faire un résumé : volume, importance, formats, vignettes, ⛔, ✎/⚠, concordance de la relecture, écarts aux cibles.
- Si le paquet remplace une version au contenu différent, dire à l'étudiant de **supprimer l'ancien paquet** avant d'importer.
- Proposer les améliorations du skill tirées des retours.

### Phase 4 — Après usage (2-3 semaines)
Analyser les statistiques Anki exportées par l'étudiant :
- cartes jamais ratées → chercher l'indice ou le distracteur faible ;
- cartes ratées en boucle → chercher l'ambiguïté ou l'erreur.

Corriger et réimporter : les GUID stables conservent la progression.

## Couverture
- **Toutes** les connaissances sont fichées, I3 compris.
- Nombre de questions par connaissance : I0 → 2-3 angles (direct, inverse, vignette, autre format) ; I1 → 1-2 ; I2-I3 → 1.
- Vocabulaire : questions dédiées, y compris pour les termes du cours non définis (définition marquée « hors cours »).
- Pas de cas progressifs sur plusieurs cartes (Anki mélange les cartes).
- Le contrôle de couverture est **bloquant** ; `couverture.xlsx` relie chaque connaissance à ses pages et à ses questions.

## Formats (4 propositions, Réponse 5 à 12 vides)
- **QCM** (mode 1, ≈ 50 %) : 1 à 4 bonnes réponses, nombre non annoncé et varié. Pour les listes, critères, signes, causes, surveillances, conduites à tenir.
- **QCS** (mode 2, ≈ 35-40 %) : une seule bonne réponse. Pour un fait unique, une valeur, une définition, l'interprétation d'une image, la « première action », ou une **liste complète** (4 listes dont une seule juste).
- **Kprim** (mode 0, ≈ 10-15 %) : chaque affirmation est à juger vraie ou fausse.
  - chaque affirmation est absolument vraie ou fausse ;
  - aucun terme vague (souvent, peut, associé à) ;
  - toutes portent sur le même objet ;
  - le nombre d'affirmations vraies varie de 0 à 4.
- `Réponses` : `1 0 0 1`.
- L'add-on **mélange les propositions** : ne jamais renvoyer à une proposition par son numéro.

## Rédaction
**Recto = Contexte → Titre → Question, sans aucune répétition**
- Le Titre est la section, plus la notion si elle apporte une information nouvelle. Il ne contient jamais le nom du cours.
- La Question ne dit que ce qui est demandé.
- Le script supprime la notion du titre si elle est déjà dans la question, et bloque les autres répétitions.

**Question**
- Écrite **en gras** (le script l'ajoute).
- **Mot discriminant souligné** (`<u>…</u>`) quand des cartes ne diffèrent que d'un mot, ou pour un mot décisif (négation, côté, délai, population). Deux mots au maximum.
- Ancre sémantique : « délai depuis le début des symptômes », pas seulement « délai ».
- Pas d'indice grammatical, pas de mot de l'énoncé repris seulement dans la bonne réponse.

**Vignettes** : objectif ≥ 40 % des questions I0/I1, angle infirmier (surveillance prioritaire, première action, ce qui fait appeler le médecin, ce qu'on vérifie avant d'administrer, installation). Leur **crédibilité est stricte** :
- présentation typique et cohérente ;
- la réponse découle d'une phrase du cours, citée dans l'explication ;
- aucune interprétation au-delà du cours ;
- en cas de doute, pas de vignette.

**Mauvaises réponses**
- Elles **ressemblent aux bonnes** : même nature, même niveau de détail.
- La bonne réponse ne doit pas dépasser **1,3 fois** la longueur moyenne des mauvaises (contrôle bloquant).
- Chacune cible une **confusion identifiée** ; si le bon sens suffit à l'éliminer, la remplacer.
- Chiffres : **valeurs proches** ou mêmes valeurs permutées, jamais une valeur aberrante, ni une valeur juste selon une autre source ou un autre passage du cours.
- Définitions : mauvaises réponses = définitions de **termes proches** (ex. hypoxie/hypoxémie, dyspnée/dysphagie, oligurie/anurie, myosis/mydriase).
- Termes absolus : permis comme pièges, mais ils doivent aussi apparaître dans des propositions vraies du paquet.
- Interdit : « toutes / aucune des réponses », les propositions absurdes.

**⛔ Erreurs dangereuses** : une mauvaise réponse qui mettrait un patient en danger s'il l'appliquait.
- Les inclure volontairement sur les gestes de sécurité du cours.
- Les signaler dans `dz` : le script ajoute `⛔ Erreur dangereuse : « … » — raison` et classe la question en I0.

**Informations complémentaires** (assemblées par le script)
- explication : point clé, avec la page du cours ;
- ⛔ / ✎ / ⚠ / Complément ;
- glossaire automatique des termes et sigles ;
- page entière du PDF en image.

**Sources** : `<Type> — <fichier>.pdf, p. <n>` ; `Web — <Organisme>, <titre>, <URL>` ; `Généré par Claude (<modèle>) — prompt v<version> — <date> — <id>`.

## Images
- Infos complémentaires : la **page entière** (JPEG 150 dpi), un fichier par page.
- Questions d'imagerie : **cliché recadré** depuis l'image source du PDF, sans titre ni légende qui donne la réponse (une flèche sans texte est acceptée). Vérifier chaque recadrage à l'œil.
- Noms de fichiers **en minuscules**, sans espace.

## Type de note QCMs (à ne jamais modifier depuis le paquet)
- Ordre des champs :
  - Question, Titre, Mode (0=kprim, 1=qcm, 2=qcu), Réponses (0=faux, 1=vrai), Sources, Contexte, Informations complémentaires ;
  - Réponse 1 à Réponse 12 ;
  - Tags.
- Réglage à faire **une fois** par l'étudiant dans Anki (Outils → Gérer les types de notes → QCMs → Cartes) :
  - *Style* : ajouter `#myH1 { font-weight: normal; font-size: 16px; color: #555; }` et `#myH1 + p { font-weight: bold; }` ;
  - *Modèle recto* : remplacer `<th>yes</th><th>no</th>` par `<th>Vrai</th><th>Faux</th>`.
