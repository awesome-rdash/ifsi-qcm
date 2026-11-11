# Contrat — fichiers produits par `tools/convert_apkg.py`

## `site/data/index.json`

```json
{
  "format": 1,
  "cours": [
    {
      "id": "s3-ue2-8-cm6-avc",
      "semestre": 3,
      "ue": "UE 2.8",
      "ue_intitule": "Processus obstructifs",
      "nom": "CM6 - AVC",
      "fichier": "data/s3-ue2-8-cm6-avc/questions.json",
      "total": 300,
      "par_importance": { "I0": 120, "I1": 90, "I2": 50, "I3": 40 }
    }
  ]
}
```

Le site construit l'arbre Semestre → UE → Cours à partir de cette liste plate.

## `site/data/<id>/questions.json`

```json
{
  "format": 1,
  "cours": {
    "id": "s3-ue2-8-cm6-avc", "semestre": 3, "ue": "UE 2.8",
    "ue_intitule": "Processus obstructifs", "nom": "CM6 - AVC",
    "contexte": "IFSI - UE 2.8 Processus obstructifs - CM SSU AVC",
    "version": "1.2", "genere_le": "2026-11-10"
  },
  "questions": [
    {
      "id": "ifsiqcm-3f30b903fee1", "guid": "ifsiqcm-3f30b903fee1",
      "mode": 2, "importance": "I1", "titre": "Épidémiologie",
      "question": "<b>…</b> <i>(une seule réponse)</i>",
      "propositions": ["1re", "2e", "3e", "4e"],
      "reponses": [1, 0, 0, 0],
      "image": null,
      "infos": "Cours p. 1 : …",
      "page_cours": ["media/ue2-8_cm6-avc_p001.jpg"],
      "sources": "CM SSU – CM6 AVC.pdf, p. 1<br>…",
      "danger": false
    }
  ]
}
```

- `mode` : 0 Kprim, 1 QCM, 2 QCS. `reponses` : 1 vrai, 0 faux, dans l'ordre de `propositions`.
- `image`, `page_cours` : chemins relatifs au dossier du cours.
- `version`, `genere_le` : lus dans le nom du fichier (`prompt v1.2 - 2026-11-10`), `null` sinon.
- Écart avec le brouillon initial : `id` = GUID (stable) ; `type` omis (non utilisé).

## `site/data/<id>/media/`

Images référencées, noms en minuscules, espaces remplacées par `-`.
