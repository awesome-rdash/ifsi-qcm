# Data Model — Site de révision QCM IFSI

Fichiers produits : voir [contracts/donnees.md](contracts/donnees.md).

## Cours
`id` (ex. `s3-ue2-8-cm6-avc`), `semestre` (entier), `ue` (`UE 2.8`), `ue_intitule`, `nom`,
`contexte`, `version`, `genere_le`, questions.

## Question
`id` = `guid` (GUID Anki, stable), `mode` (0 Kprim, 1 QCM, 2 QCS), `importance` (I0–I3), `titre`,
`question` (HTML), `propositions` (4, HTML), `reponses` (4 × 0/1), `image`, `infos` (HTML),
`page_cours` (liste), `sources` (HTML), `danger` (⛔ présent).

Validation (conversion) : 4 propositions non vides, 4 réponses 0/1, mode 0/1/2, importance
présente, type de note QCMs.

## Session (localStorage `ifsi.session`)
```
{ v: 1, correction: "chaque" | "fin",
  items: [ { cours, guid, ordre: [perm des 4 indices], choix: null | [4], statut: null | "repondu" | "passe" } ] }
```
La position courante est le premier item sans `statut`. `choix` est indexé dans l'ordre d'origine des propositions : QCS/QCM `true/false`, Kprim
`true/false/null`. Transitions : `null` → `repondu` | `passe`. Fin quand tous les items ont un `statut` ;
la session est alors supprimée et le bilan ajouté à l'historique.

## Bilan (localStorage `ifsi.historique`, 100 derniers)
```
{ date, points, n, note, parCours: [ { cle, nom, points, n, note } ],
  parImportance: […], parFormat: […] }
```

## Préférences (localStorage `ifsi.prefs`)
`{ importances: ["I0", …], correction, nombres: { <idCours>: n | null }, coches: [idCours] }`
