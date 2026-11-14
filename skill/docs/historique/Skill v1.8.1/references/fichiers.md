# Fichiers d'un paquet : espace de travail, k.py, Q(...), cours.py, glossaire_cours.py

## Espace de travail
```
Outils/                      ← copie du dossier scripts/ du skill (build.py, common.py, glossaire.py, Type de note QCMs.apkg)
<cours>/                     ← un dossier par cours : PDF + notes, cours.py, k.py, fichiers de questions
```
- Modèle complet : `G:\Mon Drive\FOR\IFSI\Anki\Prompts\Outils\exemple CM6 AVC\`.
- Les chemins de `cours.py` sont relatifs au dossier du cours.
- Commande : `python3 Outils/build.py <cours> [--report-only]`.
- `pip install anki pymupdf openpyxl --break-system-packages` si ces bibliothèques manquent.

## k.py — inventaire détaillé
- `K = [(id, pages, importance, section, texte), …]` : une ligne par connaissance, **dans l'ordre du cours**.
  - `id` : `K001…` ; les termes employés sans être définis sont `V01…`, en section « Vocabulaire ».
  - `pages` : `"12"`, `"12-14"` ou `"12,15"`.
  - `importance` : 0 à 3 (grille P).
- `EXCLUS = [(pages, texte), …]` : ce qui n'est pas une connaissance (ex. diapo « Objectifs »).

## Fichiers de questions — `QS = [Q(...)]`
Un ou plusieurs fichiers Python (`from common import Q`), dans l'ordre du cours. Champs de `Q` :
- `id`, `ks` (connaissances testées, séparées par des espaces) ;
- `mode` : 0 = Kprim, 1 = QCM, 2 = QCS ;
- `q`, `props` (4 propositions), `truth` (ex. `"0110"`) ;
- `expl`, `notion` ;
- `x` (`✎` / `⚠` / `Complément`), `w` (sources web) ;
- `img` (cliché recadré : xref, cadre, nom), `pg` (pages en plus) ;
- `dz` (erreurs dangereuses : `{index: raison}`) ;
- `allow`, `lenok` (exceptions justifiées), `vign` (vignette), `titre` (titre neutre imposé, R11) ;
- `why` : 4 justifications d'une ligne, dans l'ordre de `props` (X1, obligatoire) ;
- `ok` : exceptions validées à un contrôle bloquant, `{code: raison}` (ex. `ok={"M11": "validée par l'étudiant (R-25)"}`) ; elles apparaissent dans le rapport (`exceptions`).

## Corrections
`CORRECTIONS = [(module, dictionnaire), …]` dans `cours.py` : chaque dictionnaire associe un id à `{attribut: valeur}` (ou à une liste, qui remplace `props`). Ils s'appliquent dans l'ordre de la liste.

## cours.py — paramètres du cours
`NOM`, `PDF`, `PDFNAME`, `TYPE`, `CONTEXTE`, `DECK`, `PREFIX` (minuscules, sans espace : préfixe des images et des GUID), `MODEL`, `VERSION` (= version du skill), `REF_APKG` (facultatif : par défaut `Type de note QCMs.apkg` du dossier `Outils/`), `QFILES`, `CORRECTIONS`, `DOMAINE` (préfixe R8), `DOMAINE_VOCAB`, `TEXT_REPL` (sigles écrits en toutes lettres), `SIGLES_OK`, `TITRE_VIGNETTE` (facultatif : titre neutre des vignettes, « Cas clinique » par défaut, R11).

## Rapport de build.py
- `BLOQUANT` : liste des blocages, puis le nombre de cartes bloquées par règle. Corriger jusqu'à zéro.
- Rapport (non bloquant) à traiter : `X3_termes_sans_definition`, `X3_doublons_glossaire`, `X1_liste_sur_une_ligne`, `titre_repete_dans_question`, `titre_dans_bonnes_reponses`, `vague`, `absolus_faux_seulement`, `cle_courte`, `exceptions`.

## glossaire_cours.py — termes propres au cours (facultatif)
`EXTRA = [(terme, motif, définition, [(source, URL ou None)])]` : un seul terme par entrée, source obligatoire, sinon `build.py` bloque.
- Une page du cours s'écrit `("<cours>, p. <n>", None)` ; elle n'est permise qu'ici, jamais dans `glossaire.py` commun (bloquant).
- Une entrée du même terme qu'une entrée de `glossaire.py` la **remplace** pour ce cours.
- Le glossaire d'une carte s'affiche par ordre alphabétique.

## Sorties de build.py (sans `--report-only`)
- `.apkg`, avec les images et le type de note QCMs d'id `1604570191317` ;
- `- questions.tsv` ;
- `- couverture.xlsx` ;
- `stats.json`.

## Type de note QCMs (à ne jamais modifier depuis le paquet)
- Ordre des champs :
  - Question, Titre, Mode (0=kprim, 1=qcm, 2=qcu), Réponses (0=faux, 1=vrai), Sources, Contexte, Informations complémentaires ;
  - Réponse 1 à Réponse 12 ;
  - Tags.
- Réglage à faire **une fois** par l'étudiant dans Anki (Outils → Gérer les types de notes → QCMs → Cartes) :
  - *Style* : ajouter `#myH1 { font-weight: normal; font-size: 16px; color: #555; }` et `#myH1 + p { font-weight: bold; }` ;
  - *Modèle recto* : remplacer `<th>yes</th><th>no</th>` par `<th>Vrai</th><th>Faux</th>`.
