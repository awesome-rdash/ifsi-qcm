from common import Q, cite, college, web
QS = [
Q("A01", "K001", 2, "<u>Terrain</u> de l'<u>hémorragie méningée</u> ?",
  ["30-60 ans, femmes > hommes", "20-40 ans, hommes > femmes", "60-80 ans, hommes > femmes", "40-70 ans, femmes > hommes"], "1000",
  "Cours p. 1.", why=["Âge et sexe du cours.", "Terrain d'autres maladies.", "Sujet plus âgé.", "Tranche décalée."]),
Q("A02", "K002", 1, "Cause(s) de <u>thrombose veineuse cérébrale</u> ?",
  ["Thrombophilie", "Cancer", "Thrombolyse récente", "Tabagisme isolé"], "1100",
  "Cours p. 1.", why=["Trouble de la coagulation.", "Hypercoagulabilité.", "Traitement, pas une cause.", "Facteur de risque artériel."],
  w=[web("HAS", "Thrombose veineuse cérébrale", "https://www.has-sante.fr/"),
     college("Neurologie", "7e édition", 2025, "Accidents vasculaires cérébraux", 300, item=340),
     cite("Étude ISCVT, Stroke 2004", 1)]),
Q("A03", "K002", 2, "Mme T., 30 ans, céphalées depuis 3 jours, sous contraception orale. Diagnostic à évoquer ?",
  ["Thrombose veineuse cérébrale", "Migraine", "Méningite", "Hémorragie méningée"], "1000",
  "Cours p. 1.", vign=True, lenok=True, ok={"R7": "test d'exception"},
  why=["Céphalées subaiguës + contraception.", "Pas de facteur hormonal requis.", "Fièvre attendue.", "Début brutal attendu."]),
]
