from common import Q
W = ["a", "b", "c", "d"]
QS = [
# M8 (vote et composant) + R5 (attribut souligné sans sujet)
Q("B01", "K001", 2, "<u>Terrain</u> de l'hémorragie méningée ?",
  ["30-60 ans, femmes > hommes", "30-60 ans, hommes > femmes", "20-40 ans, femmes > hommes", "60-80 ans, femmes > hommes"], "1000", "Cours p. 1.", why=W),
# M11 (2 × 2)
Q("B02", "K001", 2, "Aire de Broca : localisation ; trouble ?",
  ["Frontal ; expression", "Temporal ; compréhension", "Frontal ; compréhension", "Temporal ; expression"], "1000", "Cours p. 1.", why=W),
# R7 (racine de l'énoncé seulement dans les bonnes réponses) + X1 (justifications absentes)
Q("B03", "K002", 1, "Complication(s) touchant les bronches ?",
  ["Encombrement bronchique", "Hydrocéphalie", "Épilepsie", "Hématome"], "1000", "Cours p. 1."),
# R11 (titre imposé de vignette qui nomme une proposition)
Q("B04", "K002", 2, "Mme T., 30 ans, céphalées depuis 3 jours. Diagnostic à évoquer ?",
  ["Thrombose veineuse cérébrale", "Migraine", "Méningite", "Hémorragie méningée"], "1000", "Cours p. 1.", vign=True, titre="Thrombose — Diagnostic", why=W),
# S3 (source sans libellé) + S9 (citation de Collège incomplète)
Q("B05", "K002", 2, "Examen de première intention devant une suspicion de <u>thrombose veineuse cérébrale</u> ?",
  ["IRM avec angio-IRM", "Électroencéphalogramme", "Échographie cardiaque", "Ponction lombaire"], "1000", "Cours p. 1.", why=W,
  w=["HAS, recommandation 2020", "Collège — Neurologie, p. 12"]),
]
