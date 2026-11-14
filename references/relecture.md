# Phase 2b — Relecture indépendante (obligatoire)

Deux relecteurs, chacun dans des **sous-agents séparés** qui n'ont pas écrit les cartes. **Tous les deux relisent toutes les cartes du paquet à chaque génération ou régénération**, pas seulement les cartes nouvelles ou modifiées. La relecture se fait après `build.py --report-only` sans blocage.

## 1. Relecteur à l'aveugle — répond aux questions
- Lots d'environ 100 questions. Il reçoit, dans un dossier isolé :
  - le texte du cours, les pages en image et les clichés des questions ;
  - les questions **sans clés ni explications** : titre (tel qu'il s'affiche), énoncé, propositions, format.
- Il répond à chaque question et signale : `erreur_medicale`, `ambigu`, `hors_cours`, `vignette_non_credible`, `distracteur_faible`, `indice`, `formulation`, `mauvaise_reponse_peut_etre_juste`, `devinable` (réponse trouvée sans connaissance : élimination, vote majoritaire, titre, mot repris).
- Comparer ses réponses aux clés.

## 2. Relecteur des règles — vérifie chaque carte complète
- Lots d'environ 50 cartes. Il reçoit `references/regles.md`, le texte du cours, `sources.md` et le texte des chapitres de `refs/` (S9 : pas de nouvelle recherche, sauf point non couvert), et les cartes **complètes** : titre affiché, énoncé, propositions, clés, explication, justifications, ⛔ / ✎ / ⚠ / Complément, glossaire affiché.
- Pour **chaque carte**, il coche **chaque règle** de la liste ci-dessous : `OK`, ou `KO` avec le motif en une phrase. Il ne saute aucune règle, même si la carte semble correcte.

| Règle | Ce qu'il vérifie |
|---|---|
| S4 | Bonne réponse conforme au cours ; mauvaises réponses fausses sans ambiguïté |
| S3, S9-S12 | Chaque source hors cours est libellée et pertinente (Collège avant web) ; bonne réponse tirée d'un collège seulement si validée en phase 1 ; chiffre d'un collège « scan + OCR » vérifié sur l'image ; aucune donnée d'un collège ancien contredite par une recommandation plus récente |
| R1, R12 | Question compréhensible seule ; mots sans ambiguïté (verbe et complément, organe, point de départ des délais) |
| R5 | Mot discriminant souligné ; sujet souligné aussi quand l'attribut vaut pour plusieurs maladies |
| R7 | Aucun mot de l'énoncé (même racine) seulement dans les bonnes réponses ; critère de découpage d'une liste absent de la question |
| R11 | Le titre ne donne ni n'oriente la réponse ; titre de vignette neutre |
| V2, V3 | Vignette crédible, réponse qui découle du cours, vocabulaire technique |
| M1 | Propositions de même nature et de même niveau de détail |
| M3, M10 | Chaque mauvaise réponse cible une confusion ; aucune n'est juste ailleurs |
| M8, M11 | Pas de devinette par élimination, vote majoritaire ou schéma 2 × 2 |
| M12 | Propositions indépendantes : aucune n'inclut, n'implique ou n'exclut une autre |
| F3 | Kprim : chaque affirmation absolument vraie ou fausse, aucun terme vague |
| E1 | Erreur dangereuse présente sur les gestes de sécurité et signalée |
| X1 | Chaque proposition justifiée (mécanisme ou correspondance) ; vignette : rôle de chaque signe, signes attendus pour chaque mauvaise réponse |
| X3 | Tout terme qu'un étudiant de 2e année peut ne pas connaître est défini, y compris dans la bonne réponse et dans les définitions ; aucun doublon |

- Sortie : un tableau `id | règle | OK/KO | motif`, une ligne par carte et par règle.

## Traitement
- Chaque discordance du relecteur à l'aveugle, chaque signalement de fond et chaque `KO` du relecteur des règles est **corrigé** (dans un dictionnaire de corrections listé dans `CORRECTIONS`) ou **justifié** dans `… - relecture.md`.
- Après correction, relancer `build.py --report-only` ; les cartes corrigées repassent chez les deux relecteurs.
- `… - relecture.md` contient : la concordance du relecteur à l'aveugle, le nombre de `KO` par règle, et la décision prise pour chacun.
