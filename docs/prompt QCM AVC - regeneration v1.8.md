Le skill `qcm-anki-ifsi` est passé en **v1.8** : il intègre les retours R-25 à R-37. Régénère le paquet **UE 2.8 – CM6 AVC** avec cette version. Ne modifie pas le skill : un défaut qui vaut pour tous les cours va dans un nouveau document de retours (R-38 et suivants).

**Avant de commencer**
1. Vérifie que le skill installé est la v1.8 (titre de `SKILL.md`). Lis `SKILL.md`, puis en entier `references/regles.md`, `references/fichiers.md` et `references/relecture.md`.
2. Lis le journal du paquet (`QCM Anki - Journal paquet CM6 AVC.md`) et `Retours paquet AVC v1.7 (R-25 à R-37).md` : chaque retour indique la règle v1.8 qui le traite.
3. Espace de travail : copie le dossier `scripts/` du skill dans `Outils/` (le type de note y est maintenant). Dans `cours.py` : `VERSION = "1.8"` et supprime la ligne `REF_APKG` (le chemin par défaut est `Outils/Type de note QCMs.apkg` ; les chemins de `cours.py` sont relatifs au dossier du cours).

**Travail sur les fichiers existants** (`k.py`, `r1` à `r6`, dictionnaires de corrections) — mets les modifications v1.8 dans un nouveau dictionnaire (ex. `v18.py`, `FIX`), en dernier dans `CORRECTIONS`.
- **X1** : ajoute `why` aux 356 cartes : 4 justifications d'une ligne, dans l'ordre des propositions. Vraie : le mécanisme. Fausse : ce à quoi elle correspond. Vignette : pourquoi chaque signe oriente vers la bonne réponse, et les signes qu'on aurait attendus pour chaque mauvaise réponse. Une liste : une ligne par élément (X6).
- Blocages mesurés sur le paquet v1.7 : R7 36 cartes, R5 21, M11 7, M8 2. Corrige jusqu'à zéro avec `python3 Outils/build.py <cours> --report-only` (le rapport donne le nombre de cartes bloquées par règle).
  - **M11** (schéma 2 × 2) : J16, C20, C21, L07, L15b, J15 → une carte par élément ou plus de valeurs. **I18 reste telle quelle** : `ok={"M11": "validée par l'étudiant (R-25)"}`.
  - **M8** : N05 (vote majoritaire), A05.
  - **R7** : réécris plutôt que d'exempter (question sans le mot, ou mauvaise réponse qui partage la racine). Exception `ok={"R7": "raison"}` seulement si la racine commune n'aide pas à deviner. H12b, H12c, H12d (et H06b, non détecté) : le critère de découpage de la liste ne doit plus être écrit dans la question.
  - **R5** : souligne aussi le sujet (« <u>Terrain</u> de l'<u>hémorragie méningée</u> »).
- **R11** : les vignettes prennent par défaut le titre « Cas clinique » ; retire tout `titre` qui nomme ou suggère le diagnostic (N13, L08, K02, K05b, A15, I16).
- **M1 / M12** (relecteur des règles) : N09 (propositions qui s'excluent ou s'incluent), O11 (« mortalité » parmi des signes).
- **X3** : traite chaque ligne de `X3_termes_sans_definition` (environ 49 termes : artériographie, hémostase, Behçet, angiographie, hémianopsie, pancréatite…) et ce que le script ne repère pas : lupus, « des 4 axes ». Une entrée par terme dans `glossaire_cours.py`, chaque source lue avant d'être citée (S8). Les définitions du glossaire ne doivent pas employer de terme non défini.

**Relecture (phase 2b, `references/relecture.md`)** : relecteur à l'aveugle **et** relecteur des règles, sur **toutes** les cartes du paquet, pas seulement celles qui ont changé. Corrige ou justifie chaque discordance et chaque `KO` dans `relecture.md`.

**Livraison (phase 3)** : paquet, `questions.tsv`, `couverture.xlsx`, `stats.json`, `relecture.md` dans `Anki\Decks\S3 - UE 2.8 - CM6 AVC\`. Résumé avec les blocages traités par règle, les exceptions `ok` et leur raison, et le nombre de `KO` par règle. Écris les décisions dans le journal du paquet AVC avant la fin de la conversation.

Termine chaque message qui attend une réponse par le récapitulatif consolidé des points ouverts.
