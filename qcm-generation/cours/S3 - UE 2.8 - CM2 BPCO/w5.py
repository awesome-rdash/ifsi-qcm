# Corrections de la relecture 2b (v1.8.1) : relecteur des règles (229 KO) et relecteur à l'aveugle.
# Chaque entrée part de la carte telle qu'elle est après w1-w4 et fmt, puis remplace les champs indiqués.
import importlib, copy, cours as C

_BASE = {}
for _m in C.QFILES:
    for _q in importlib.import_module(_m).QS:
        _BASE[_q.id] = copy.deepcopy(_q)
for _mod, _d in C.CORRECTIONS:
    if _mod == "w5": break
    _D = getattr(importlib.import_module(_mod), _d)
    for _id, _v in _D.items():
        if _id not in _BASE: continue
        if isinstance(_v, list): _BASE[_id].props = _v
        else:
            for _k, _x in _v.items(): setattr(_BASE[_id], _k, _x)

W = {}
def E(i, props=None, sub=None, **kw):
    """props : {index: (proposition, justification)} ; sub : [(ancien, nouveau)] appliqué à l'explication."""
    b = _BASE[i]; d = W.setdefault(i, {})
    if props:
        P = list(d.get("props", b.props)); Y = list(d.get("why", b.why))
        for k, (p, y) in props.items(): P[k] = p; Y[k] = y
        d["props"], d["why"] = P, Y
    if sub:
        e = d.get("expl", b.expl)
        for a, n in sub:
            assert a in e, (i, a)
            e = e.replace(a, n)
        d["expl"] = e
    d.update(kw)

def X(i):  # champ x d'une autre carte
    return _BASE[i].x

# --- A ---
E("A03", q="Mesure(s) réalisée(s) lors d'un bilan d'explorations fonctionnelles respiratoires ?",
  props={2: ("Les échanges gazeux", "Vrai : les gaz du sang, qui complètent les EFR, évaluent l'échange entre alvéoles et capillaires (p. 2)."),
         3: ("La pression artérielle pulmonaire", "Faux : elle se mesure par échographie du cœur ou par une sonde poussée jusqu'au cœur droit, pas par les EFR.")},
  sub=[("(elle se mesure par échographie cardiaque ou cathétérisme)", "(elle se mesure par échographie du cœur ou par une sonde poussée jusqu'au cœur droit)")])
E("A06", x=X("B01"))
E("A07", props={3: ("Le statut tabagique", "Faux : le tabac abaisse le VEMS mesuré, mais la valeur normale (prédite) ne dépend que du sexe, de l'âge, de la taille et de l'origine.")},
  sub=[("Le groupe sanguin n'intervient pas.", "Le tabagisme abaisse le VEMS mesuré, pas la valeur prédite.")])
E("A09", props={2: ("Son seuil d'obstruction est de 70 % chez l'adulte", "Vrai : obstruction si VEMS/CV < 70 % chez l'adulte (p. 4).")})
E("A16", props={2: ("CV = CPT + VR", "Faux : la CV est contenue dans la CPT : CV = CPT − VR (p. 3)."),
                3: ("CRF = VRI + VR", "Faux : la CRF additionne le VRE (et non le VRI) et le VR : CRF = VRE + VR (p. 3).")})
E("A17", q="Valeur normale du rapport VR/CPT chez le <u>sujet jeune</u> ?",
  props={1: ("Environ 1/10", "Faux : aucune valeur du cours ; le VR représente environ un tiers de la CPT."),
         3: ("Environ 2/3", "Faux : un VR aux deux tiers de la CPT traduirait une distension majeure (air piégé) ; le rapport augmente avec l'âge et la distension.")})
# --- B ---
E("B02", props={0: ("Trouble ventilatoire obstructif", "Vrai : rapport 62 % < 70 % = obstruction, chez un fumeur de 58 ans (terrain de BPCO) ; VEMS 75 % = stade II, modéré (50-80 %, p. 5, 34).")},
  sub=[("(ici, VEMS ≥ 50 % : obstruction peu sévère)", "(ici, VEMS 75 % : stade II, modéré, grille p. 34)")])
E("B05", q="Cause(s) <u>extra-pulmonaire(s)</u> de trouble ventilatoire <u>restrictif</u> ?",
  props={2: ("Fibrose", "Faux : cause parenchymateuse (cicatrice qui rigidifie le poumon) (p. 5).")})
E("B06", q="Paramètre qui sert à classer la sévérité d'un trouble ventilatoire obstructif ?",
  props={0: ("Le VEMS, en % de la valeur prédite", "Vrai : la sévérité du TVO se classe selon la valeur du VEMS (p. 5, 34)."),
         1: ("Le rapport VEMS/CV", "Faux : le rapport fait le diagnostic du TVO, il ne classe pas sa sévérité (p. 8)."),
         2: ("La capacité pulmonaire totale", "Faux : la CPT sert au diagnostic de restriction (p. 5)."),
         3: ("Le volume résiduel", "Faux : le VR augmenté traduit une distension, pas la sévérité de l'obstruction (p. 33).")},
  expl="Cours p. 5 : la sévérité du TVO se classe selon la valeur du VEMS (léger, sévère, très sévère) ; la grille de référence, plus complète, est celle des stades I à IV (p. 34). Le rapport VEMS/CV fait le diagnostic ; la CPT juge la restriction.")
E("B08", q="Maladie(s) qui donne(nt) un trouble ventilatoire <u>obstructif</u>, parmi les suivantes ?")
E("B09", q="Prévalence de la <u>BPCO</u> chez l'adulte et chez le fumeur ?",
  props={2: ("5-7 % des adultes, 35 % des fumeurs", "Faux : 5-7 % est la prévalence de l'asthme (p. 6) ; chez le fumeur, c'est 20 %.")})
E("B10", q="Prévalence de l'<u>asthme</u> chez l'adulte ?")
E("B11", props={3: ("Obstructif réversible : l'obésité rend l'obstruction réversible", "Faux : la réversibilité dépend de la maladie (asthme), pas du poids ; l'obstruction de la BPCO reste fixée (p. 7).")})
E("B12", q="Cause(s) <u>parenchymateuse(s)</u> de trouble ventilatoire <u>restrictif</u> ?")
# --- C ---
E("C01", props={3: ("S'aggrave avec le temps, de façon continue", "Faux : l'aggravation progressive caractérise la BPCO (p. 7).")}, truth="1110")
E("C02", props={0: ("S'aggrave avec le temps", "Vrai : elle s'aggrave au cours du temps (p. 7)."),
                1: ("S'aggrave plus vite si le patient continue à fumer", "Vrai : d'autant plus si le patient continue à fumer (p. 7)."),
                2: ("Levée par les corticoïdes inhalés", "Faux : l'obstruction de la BPCO est fixée ; les corticoïdes inhalés ne la font pas disparaître (p. 7, 40).")},
  truth="1101", sub=[("« Absente en dehors des crises » décrit l'asthme.", "Les corticoïdes inhalés ne lèvent pas cette obstruction fixée.")])
E("C03", props={3: ("La capacité pulmonaire totale", "Faux : la CPT juge la restriction (p. 5) ; elle ne distingue pas ces deux maladies obstructives.")},
  sub=[("(VEMS/CV abaissé, VEMS diminué, atteinte des bronches)", "(VEMS/CV abaissé, VEMS diminué)")])
E("C04", props={0: ("Le bronchodilatateur utilisé est d'action rapide (ex. Ventoline)", "Vrai : on fait inhaler un bronchodilatateur d'action rapide (Ventoline) entre les deux spirométries (p. 6-7).")})
E("C05", props={3: ("Dilatation des bronches", "Faux : elle peut donner un TVO (p. 6), mais on attendrait une toux avec expectoration abondante et des infections répétées.")},
  sub=[("Dans la BPCO, le VEMS ne redevient jamais normal (p. 7).", "Dans la BPCO, le VEMS ne redevient jamais normal (p. 7) ; la dilatation des bronches donne surtout une expectoration abondante et des infections.")])
E("C06", mode=1, titre="Cas clinique", truth="1110",
  q="EFR : VEMS/CVF 43 %, VEMS à 27 % de la valeur prédite avant et à 28 % après Ventoline. Interprétation(s) exacte(s) ?",
  props={0: ("Trouble ventilatoire obstructif", "Vrai : rapport 43 % < 70 % = TVO (p. 5)."),
         1: ("Obstruction très sévère", "Vrai : VEMS 27 % < 30 % = très sévère, stade IV (p. 34)."),
         2: ("Obstruction non réversible", "Vrai : VEMS quasi inchangé après Ventoline = pas de réversibilité (p. 6-7)."),
         3: ("Profil évocateur d'un asthme", "Faux : l'asthme donne une obstruction réversible ; ce profil fixé évoque une BPCO (p. 6-7).")},
  expl="Cours p. 7 (et notes) : rapport 43 % < 70 % = trouble obstructif ;<br>VEMS 27 % < 30 % = très sévère ;<br>pas de gain après Ventoline = non réversible, donc BPCO et non asthme.")
E("C07", props={3: ("Vasculaire", "Faux : les maladies vasculaires (embolie, hypertension artérielle pulmonaire) n'obstruent pas les bronches.")},
  ok={"R7": "« obstructive » est lisible dans le sigle BPCO imposé en tête de chaque question (R8) ; la carte interroge aussi l'asthme, qui n'a pas ce sigle."})
E("C08", ok={"R7": "racine « bronch- » commune au nom de la maladie (BPCO, imposé en tête par R8) et à la seule réponse anatomique juste ; non contournable sans fausser la question."})
E("C09", x=X("B01"))
E("C10", props={2: ("Le rapport mesure la distension ; le VEMS mesure la réversibilité", "Faux : la distension se voit sur les volumes non mobilisables, et la réversibilité se juge en comparant le VEMS avant et après bronchodilatateur."),
                3: ("Le rapport juge la restriction ; le VEMS fait le diagnostic", "Faux : la restriction se juge sur la CPT, et c'est le rapport qui fait le diagnostic d'obstruction.")})
E("C11", q="EFR dans l'asthme et dans la BPCO : vrai ou faux ?", truth="1110",
  props={0: ("Chez l'asthmatique, l'obstruction est absente en dehors des crises", "Vrai : des EFR normales hors crise sont possibles chez l'asthmatique (quiz p. 14)."),
         1: ("Chez le patient BPCO, les EFR sont toujours pathologiques", "Vrai : obstruction fixée, toujours présente (notes p. 7, quiz p. 14)."),
         2: ("Chez l'asthmatique, les bronchodilatateurs agissent sur l'obstruction", "Vrai : l'obstruction de l'asthme est sensible aux bronchodilatateurs (quiz p. 14)."),
         3: ("Chez le patient BPCO, les EFR se font de préférence pendant une exacerbation", "Faux : les EFR ne se font pas en urgence, mais à l'état stable (p. 1).")},
  expl="Quiz p. 13-14 : on peut être asthmatique et avoir un jour des EFR normales (obstruction absente hors crise) ;<br>pas en cas de BPCO, où toutes les EFR sont pathologiques (notes p. 7) ;<br>les bronchodilatateurs ont un effet sur l'obstruction de l'asthmatique. Les EFR ne se font pas en urgence (p. 1).")
# --- D ---
E("D02", q="Effectifs en France de la bronchite chronique, de la BPCO et de l'insuffisance respiratoire chronique ?",
  props={3: ("Bronchite chronique 3 500 000 ; BPCO 250 000 ; IRC 100 000", "Faux : BPCO sous-estimée et IRC surestimée ; la pyramide est 2 500 000 / 800 000 / 40 000.")})
E("D05", props={3: ("Le diagnostic nécessite un scanner thoracique", "Faux : le diagnostic repose sur les EFR (p. 16, 30).")},
  sub=[("Les symptômes sont tardifs (p. 19).", "Le diagnostic repose sur les EFR (p. 30).")])
E("D06", props={1: ("Toux et dyspnée ≥ 2 mois par an pendant ≥ 3 ans", "Faux : c'est l'expectoration, pas la dyspnée, qui accompagne la toux ; et les durées sont 3 mois par an pendant 2 ans."),
                2: ("Toux et dyspnée ≥ 3 mois par an pendant ≥ 3 ans", "Faux : la dyspnée ne fait pas partie de la définition ; et la durée est d'au moins 2 ans."),
                3: ("Expectoration et dyspnée ≥ 2 mois par an pendant ≥ 2 ans", "Faux : il faut une toux, pas une dyspnée ; et au moins 3 mois par an.")})
_CHRON = "✎ Modifié par rapport au cours : notes p. 7 « tousse et crache > 3 mois/an depuis > 2 ans, pas besoin d'EFR » donné comme définition de la BPCO → c'est la définition de la bronchite chronique (diapo p. 16) ; la BPCO exige un trouble obstructif aux EFR."
E("D07", x=_CHRON, q="M. C., 52 ans, fumeur, tousse et crache chaque matin, 4 mois par an depuis 3 ans ; EFR normales. Diagnostic le plus probable ?")
E("D08", x=_CHRON, props={2: ("Destruction des parois des alvéoles pulmonaires", "Faux : c'est l'emphysème.")})
E("D09", props={2: ("Réversible sous corticoïdes inhalés", "Faux : l'obstruction est fixée ; la réversibilité caractérise l'asthme."),
                3: ("D'origine allergique", "Faux : l'origine allergique évoque l'asthme ; la BPCO est due au tabac dans 85 % des cas (p. 17).")},
  sub=[("elle n'est ni intermittente, ni réversible, ni stable (elle s'aggrave avec le temps).", "elle n'est ni réversible ni d'origine allergique (asthme).")])
E("D10", props={1: ("Rapport VEMS/CVF < 0,80 avant bronchodilatateur", "Faux : seuil de 0,70, mesuré après bronchodilatateur pour éliminer un asthme."),
                2: ("VEMS < 0,70 L avant bronchodilatateur", "Faux : le VEMS se lit en % de la valeur prédite et mesure la sévérité, pas le diagnostic."),
                3: ("VEMS < 80 % de la valeur prédite avant bronchodilatateur", "Faux : le VEMS mesure la sévérité (stade II si 50-80 %), pas le diagnostic.")})
E("D11", props={0: ("Élargissement anormal et permanent des espaces aériens situés après les plus petites bronches (bronchioles terminales)", "Vrai : définition anatomique de l'emphysème (p. 16).")}, lenok=True,
  sub=[("au-delà d'une bronchiole terminale", "situés après les plus petites bronches (bronchioles terminales)")])
E("D15", props={1: ("Dilatation des bronches", "Faux : c'est une autre maladie, qui peut donner un TVO (p. 6), pas l'évolution commune."),
                2: ("Asthme sévère", "Faux : l'asthme est une autre maladie (obstruction réversible), pas une évolution."),
                3: ("Fibrose pulmonaire", "Faux : la fibrose est une cause de restriction (p. 5).")})
E("D18", props={3: ("L'obstruction siège d'abord dans les alvéoles", "Faux : l'obstruction siège dans les bronches ; l'atteinte des alvéoles, c'est l'emphysème (quiz p. 9-10).")})
# --- E, F ---
E("E02", q="Effet de l'arrêt du tabac sur le déclin du VEMS d'un fumeur « sensible » (dont le VEMS baisse vite) ?",
  props={3: ("Ne protège que s'il a lieu avant 45 ans", "Faux : bénéfice aussi pour un arrêt à 65 ans (courbe de Fletcher, p. 28).")})
E("E03", props={0: ("L'arrêt ralentit le déclin du souffle, quel que soit le moment de l'arrêt", "Vrai : sevrage = seul traitement qui ralentit le déclin du VEMS, bénéfice même à 65 ans (p. 19, 37).")})
E("E04", truth="0010",
  props={1: ("Un emphysème au scanner suffit à affirmer une BPCO", "Faux : la BPCO se définit aux EFR ; un emphysème peut se voir sans TVO (p. 20)."),
         2: ("La bronchite chronique se définit sur des critères cliniques", "Vrai : toux et expectoration ≥ 3 mois par an pendant ≥ 2 ans (p. 16).")},
  sub=[("et son absence n'élimine pas une BPCO ;", "; la bronchite chronique est une définition clinique (p. 16) ;")])
E("F01", q="Place de l'insuffisance respiratoire chronique grave dans l'évolution de la BPCO ?",
  props={3: ("Étape intermédiaire entre la bronchite chronique et l'emphysème", "Faux : bronchite chronique, BPCO et emphysème évoluent tous vers l'IRC, qui vient en dernier (p. 17).")})
E("F02", props={0: ("Par 2 gaz du sang à l'état stable, à au moins 3 semaines d'intervalle", "Vrai : gaz du sang répétés (intervalle ≥ 3 semaines), à l'état stable (p. 20, quiz p. 25)."),
                1: ("Par 2 gaz du sang à l'état stable, à 24 h d'intervalle", "Faux : il faut au moins 3 semaines entre les mesures (p. 20)."),
                2: ("Par 2 gaz du sang dont 1 lors d'une exacerbation", "Faux : il faut être à distance d'un épisode aigu (p. 20)."),
                3: ("Par un seul gaz du sang, au repos", "Faux : un seul prélèvement ne suffit pas : mesures répétées (p. 20).")})
E("F03", props={3: ("À jeun", "Faux : le jeûne n'est pas une condition ; les conditions sont air ambiant, repos, état stable (p. 20).")},
  sub=[("Sous oxygène, la PaO2 serait faussement rassurante.", "Le jeûne n'est pas exigé ; sous oxygène, la PaO2 serait faussement rassurante.")])
E("F05", x="Complément : l'Assurance maladie retient PaO2 ≤ 55 mmHg, ou 56-59 mmHg avec une polyglobulie (globules rouges > 55 % du volume sanguin), des signes d'insuffisance cardiaque droite due aux poumons, une hypertension artérielle pulmonaire ou une baisse de la saturation pendant le sommeil.")
E("F08", q="Seuil de PaCO2 de l'hypercapnie associé aux critères d'insuffisance respiratoire chronique grave ?")
E("F09", props={1: ("L'hypercapnie dilate les vaisseaux pulmonaires et épuise le cœur droit", "Faux : c'est l'hypoxémie qui contracte (et non dilate) les vaisseaux pulmonaires."),
                2: ("L'hypoxémie dilate les vaisseaux pulmonaires et surcharge le cœur gauche", "Faux : l'hypoxémie contracte les vaisseaux pulmonaires, et c'est le cœur droit qui envoie le sang aux poumons."),
                3: ("La polyglobulie rend le sang visqueux et bloque le cœur gauche", "Faux : c'est le cœur droit qui est touché, par la contraction des vaisseaux pulmonaires.")},
  sub=[("entraîne une vasoconstriction des vaisseaux pulmonaires", "entraîne une contraction des vaisseaux pulmonaires")])
# --- G ---
E("G01", props={3: ("Examen moins coûteux que l'oxymétrie de pouls", "Faux : l'oxymètre de pouls est peu coûteux et réutilisable ; les gaz du sang demandent une ponction et une analyse.")},
  sub=[("mesurent la pression artérielle en O2 et en CO2", "mesurent la pression de l'oxygène (PaO2) et du gaz carbonique (PaCO2) dans le sang artériel")])
E("G03", dz={3: "attendre 85 % pour s'inquiéter retarde l'alerte devant une hypoxémie (cours p. 21)"},
  props={3: ("< 85 %", "Faux : seuil trop bas : on alerte dès 90 % (⛔).")})
E("G04", q="Saturation tolérée chez un patient <u>BPCO</u> ?",
  dz={1: "viser une saturation haute chez le BPCO aggrave l'hypercapnie (cours p. 54)", 2: "une SpO2 à 100 % sous oxygène chez le BPCO fait baisser la commande respiratoire (bradypnée, hypercapnie)", 3: "82-86 % expose à l'hypoxie profonde et à l'arrêt cardiaque hypoxique (cours p. 54)"},
  props={3: ("82 à 86 %", "Faux : trop bas, risque d'hypoxie profonde et d'arrêt cardiaque (⛔, p. 54).")})
E("G06", q="Saturation visée chez un <u>asthmatique</u> en crise ?",
  props={1: ("Entre 88 et 92 %", "Faux : cible du patient BPCO ; trop basse chez l'asthmatique (⛔)."),
         2: ("Entre 85 et 88 %", "Faux : trop bas, hypoxémie (⛔)."),
         3: ("Entre 80 et 85 %", "Faux : hypoxémie franche (⛔).")},
  dz={1: "viser 88-92 % chez l'asthmatique en crise l'expose à l'hypoxémie (notes p. 21)", 2: "une SpO2 de 85-88 % est une hypoxémie (cours p. 21)", 3: "une SpO2 de 80-85 % est une hypoxémie grave (cours p. 21)"})
# --- H ---
E("H03", q="Proportion de l'ensemble des fumeurs qui développeront un trouble ventilatoire obstructif ?",
  props={2: ("35 %", "Faux : surestimation ; c'est 20 % (p. 27).")})
E("H07", q="Survie à <u>70 ans</u> chez les fumeurs comparée aux non-fumeurs (étude des médecins britanniques) ?",
  props={1: ("94 % contre 97 %", "Faux : chiffres de survie à 50 ans (p. 28)."),
         2: ("26 % contre 59 %", "Faux : chiffres de survie à 80 ans (p. 28)."),
         3: ("4 % contre 24 %", "Faux : chiffres de survie à 90 ans (p. 28).")})
E("H08", q="Années de vie gagnées par un arrêt du tabac vers <u>35-44 ans</u> ?")
E("H11", props={2: ("La BPCO apparaît le plus souvent avant 30 ans", "Faux : la BPCO augmente avec l'âge (quiz p. 36)."),
                3: ("Le symptôme le plus important est la dyspnée chronique", "Vrai : dyspnée chronique, symptôme le plus important (p. 30).")})
E("H13", props={0: ("À l'effort le plus souvent, pas toujours bien corrélée aux gaz du sang", "Vrai : le plus souvent à l'effort, pas toujours bien corrélée aux gaz du sang (p. 31)."),
                2: ("Limitée aux exacerbations", "Faux : elle est permanente, le plus souvent à l'effort ; l'exacerbation est une aggravation aiguë (p. 31, 46)."),
                3: ("Surtout la nuit, en position couchée", "Faux : la dyspnée en position couchée (orthopnée) n'est pas la définition ; la dyspnée chronique est le plus souvent d'effort (p. 31).")},
  sub=[("pas toujours bien corrélée à la gazométrie", "pas toujours bien corrélée aux gaz du sang")])
E("H14", props={3: ("Présente seulement aux efforts importants", "Faux : c'est une dyspnée chronique peu gênante (stade 0 de l'échelle MRC), pas une dyspnée aiguë.")})
E("H18", truth="0010",
  props={0: ("Un examen physique normal élimine une BPCO", "Faux : l'examen peut être normal en période stable, surtout dans les formes peu sévères (p. 32)."),
         1: ("Le frein expiratoire est un signe des formes peu sévères", "Faux : il fait partie du tableau de l'emphysémateux sévère (p. 32).")})
E("H19", props={3: ("Bradypnée de repos", "Faux : la bradypnée est un signe d'épuisement (p. 49), pas un signe de l'emphysémateux stable.")})
E("H20", q="Radiographie de thorax de profil d'un patient BPCO sévère : anomalie que mesure la double flèche jaune ?",
  props={0: ("Distension", "Vrai : diamètre antéro-postérieur augmenté, mesuré par la double flèche jaune (p. 32).")},
  sub=[("(flèche jaune)", "(double flèche jaune)")])
E("H21", q="Statut pondéral associé à un <u>mauvais pronostic</u> chez le patient BPCO ?")
E("H22", props={2: ("Réversibilité de l'obstruction après bronchodilatateur absente ou incomplète", "Vrai : pas de réversibilité ou réversibilité incomplète (p. 33).")}, lenok=True)
E("H23", q="Anomalie des volumes aux EFR qui définit la distension thoracique du patient BPCO ?",
  props={3: ("Volume courant augmenté", "Faux : la distension touche les volumes non mobilisables (air piégé), pas le volume courant.")})
# --- I, J ---
E("I02", props={3: ("Insuffisance rénale", "Faux : non citée parmi les causes de décès (p. 33).")})
E("I03", q="Stade de sévérité d'une BPCO avec VEMS à 45 % de la valeur prédite, <u>sans insuffisance respiratoire</u> ?")
E("I04", q="Définition du <u>stade IV</u> (très sévère) de la BPCO ?",
  props={2: ("VEMS < 35 %, et seulement en cas d'insuffisance respiratoire associée", "Faux : 35 % est une borne de la grille simplifiée p. 5 (sévère 35-50 %) ; le stade IV exige < 30 %, ou < 50 % avec retentissement.")})
E("I05", q="Valeur du VEMS du <u>stade II</u> (modéré) de la BPCO ?",
  props={3: ("< 30 %", "Faux : stade IV.")})
E("I06", q="Symptômes habituels du <u>stade IV</u> (très sévère) de la BPCO ?")
E("I08", q="Facteur(s) de mauvais pronostic dans la BPCO, parmi les suivants ?")
E("I09", props={1: ("Dyspnée → hyperventilation → hypercapnie → plus de dyspnée chaque jour", "Faux : l'hyperventilation fait baisser le CO2 ; le cercle du cours passe par la perte musculaire."),
                2: ("Toux → fatigue → dénutrition → plus de toux et d'expectoration", "Faux : confond avec la dénutrition, facteur de mauvais pronostic (p. 32), qui n'est pas ce cercle."),
                3: ("Exacerbation → antibiotiques → résistance → plus d'exacerbations", "Faux : la résistance aux antibiotiques existe, mais le cercle du déconditionnement passe par l'inactivité.")})
E("I10", q="M. G., BPCO, ne sort plus de chez lui depuis des mois en raison d'une dyspnée d'effort ; fonte musculaire des membres. Prise en charge qui cible ce problème ?")
E("I11", props={3: ("Oui, chez ceux qui fument depuis plus de 10 ans", "Faux : même chez le fumeur, la BPCO apparaît surtout après 50 ans (p. 30).")})
E("I12", q="Statut pondéral <u>le moins défavorable</u> au pronostic d'un patient BPCO ?",
  props={3: ("Poids normal", "Faux : la réponse du cours est le surpoids : « mieux vaut être en surpoids que dénutri » (quiz p. 36).")},
  x="✎ Modifié par rapport au cours : notes « ni l'un ni l'autre (mais encore pire dénutri) » → réponse de la diapo : surpoids ; « ni l'un ni l'autre » n'est pas proposé, pour éviter l'ambiguïté.")
E("J03", props={2: ("Tuberculose (BCG)", "Faux : il protège de la tuberculose ; il n'est pas cité pour prévenir les surinfections de la BPCO."),
                3: ("Hépatite B", "Faux : il protège d'une infection du foie, pas des surinfections respiratoires.")})
E("J08", props={3: ("Corticothérapie orale au long cours", "Faux : non citée ; les corticoïdes oraux ne sont pas un traitement de fond de la BPCO (p. 40).")})
# --- K ---
E("K02", q="Médicaments qui composent le traitement de fond de la <u>BPCO</u> ?",
  props={2: ("Bronchodilatateurs de courte durée seuls, à heure fixe", "Faux : les courte durée servent à la crise (p. 43)."),
         3: ("Bronchodilatateurs de longue durée ± corticoïdes oraux", "Faux : on associe des corticoïdes inhalés, pas oraux (p. 40).")})
E("K03", props={3: ("Bronchodilatateurs de longue durée seuls", "Faux : le traitement de fond de l'asthme repose sur les corticoïdes inhalés (p. 40).")})
E("K05", props={2: ("Confusion entre l'inhalateur quotidien et celui de crise", "Vrai : mauvaise compréhension fond/crise (p. 41).")})
E("K06", dz={2: "doubler les doses expose au surdosage et aux effets indésirables"},
  props={2: ("Vous pouvez doubler les doses pour obtenir un effet plus rapide", "Faux : doubler les doses n'accélère pas l'effet et expose aux effets indésirables (⛔).")})
E("K07", props={0: ("Poudre en réservoir ou en disque", "Vrai : système cité (p. 41)."),
                1: ("Gélules de poudre", "Vrai : système cité (p. 41)."),
                3: ("Comprimé à sucer", "Faux : un comprimé passe par la bouche et le tube digestif, ce n'est pas un système d'inhalation.")},
  sub=[("Le patch n'est pas une voie inhalée.", "Un comprimé n'est pas une voie inhalée.")])
E("K08", q="Ordre des étapes de prise d'un inhalateur de <u>poudre</u> ?")
E("K09", q="Technique de prise d'un inhalateur de poudre : vrai ou faux ?")
E("K11", props={0: ("Éviter une mycose de la gorge", "Vrai : les corticoïdes affaiblissent localement les défenses : risque de mycose de la bouche et de la gorge (notes p. 42).")})
E("K12", props={0: ("Absence de rinçage après la prise", "Vrai : dépôts blancs = mycose, due au corticoïde non rincé (p. 42).")})
E("K13", q="Ordre des étapes de prise d'un <u>spray</u> (aérosol doseur) ?",
  props={3: ("Presser en l'air pour vérifier, inspirer lentement, apnée 1 s", "Faux : on secoue le spray et on vide les poumons avant ; l'apnée dure 5 s.")})
E("K15", q="Traitement de crise de la BPCO <u>à domicile</u> ?")
E("K16", q="Forme du traitement de crise de la BPCO <u>à l'hôpital</u> ?",
  props={1: ("Perfusion de bronchodilatateurs de longue durée", "Faux : les longue durée relèvent du fond ; à l'hôpital, la crise se traite par nébulisation (p. 43)."),
         3: ("Comprimé de bronchodilatateur de courte durée", "Faux : à l'hôpital, le traitement de crise passe par la nébulisation, pas par la voie orale (p. 43).")})
# --- L ---
E("L05", q="Nature des signes de gravité d'une exacerbation de BPCO ?",
  props={2: ("Ceux d'une infection grave (fièvre, frissons)", "Faux : une infection peut déclencher l'exacerbation, mais les signes de gravité sont ceux de l'insuffisance respiratoire aiguë (p. 46).")})
E("L06", props={2: ("Alcalose respiratoire", "Faux : l'alcalose vient d'une baisse du CO2 (hyperventilation) ; dans l'exacerbation de BPCO, le CO2 monte."),
                3: ("Hyperkaliémie", "Faux : trouble du potassium, qui menace surtout l'insuffisant rénal ; non cité dans l'exacerbation de BPCO.")})
E("L07", dz={1: "une exacerbation grave impose d'alerter sans attendre (cours p. 46)", 2: "les anxiolytiques (benzodiazépines) sont dépresseurs respiratoires (cours p. 52)", 3: "à plat, le patient en détresse respiratoire respire moins bien"},
  props={3: ("Mettre le patient à plat pour le faire reposer", "Faux : on installe le patient assis ; à plat, il respire moins bien (⛔).")})
E("L08", props={1: ("Alerter le médecin", "Vrai : rôle infirmier (p. 47).")})
E("L10", q="Seuil de fréquence <u>respiratoire</u> qui signe la gravité chez l'adulte ?",
  props={3: ("> 35/min", "Faux : seuil trop haut : on alerte dès 30/min (⛔).")},
  dz={3: "attendre 35/min retarde l'alerte entre 30 et 35/min (cours p. 48)"})
E("L11", dz={1: "la polypnée > 30/min impose d'alerter, même avec une SpO2 dans la cible (cours p. 48)", 2: "une fréquence de 34/min est un signe de gravité (cours p. 48)"},
  props={1: ("Situation rassurante : la SpO2 est dans la cible", "Faux : la SpO2 est dans la cible, mais la fréquence respiratoire impose d'alerter (⛔)."),
         2: ("Situation rassurante : la fréquence est normale pour une BPCO", "Faux : on attendrait 10-16/min (p. 48) ; 34/min est un signe de gravité (⛔).")})
E("L12", q="Fréquence respiratoire normale de l'adulte au repos ?",
  props={1: ("26 à 32 cycles/min", "Faux : polypnée ; au-delà de 30/min, signe de gravité (p. 48)."),
         2: ("34 à 40 cycles/min", "Faux : polypnée grave (> 30/min, p. 48).")})
E("L13", q="Méthode rapide de mesure de la fréquence respiratoire ?",
  props={1: ("Compter les cycles pendant 10 secondes et multiplier par 10", "Faux : erreur de calcul : 10 s × 6 donnerait la minute.")})
E("L14", props={0: ("La polypnée est une donnée objective et reproductible", "Vrai : objective et reproductible (p. 48)."),
                1: ("La polypnée superficielle est plus subjective que la polypnée", "Vrai : plus subjective (p. 48).")})
E("L15", props={3: ("Intercostaux internes", "Faux : ce sont des muscles de l'expiration forcée, pas des inspiratoires accessoires.")})
E("L17", props={2: ("Leur mise en jeu signe toujours une hypercapnie", "Faux : ils signent la lutte ; l'hypercapnie a ses propres signes (sueurs, céphalées, confusion, p. 50)."),
                3: ("Leur mise en jeu signe une infection", "Faux : c'est un signe de lutte respiratoire, quelle qu'en soit la cause (p. 48).")})
E("L18", props={3: ("Entre les omoplates", "Faux : le tirage se voit sur les creux et les espaces de la face avant du thorax (p. 49).")})
E("L19", q="Signe(s) d'<u>épuisement</u> au cours d'une exacerbation de BPCO ?")
E("L21", props={1: ("Amélioration : poursuivre la surveillance horaire", "Faux : on attendrait une baisse de fréquence avec disparition des signes de lutte et patient éveillé (⛔)."),
                2: ("Endormissement normal : le laisser dormir", "Faux : la somnolence est un trouble de la vigilance (⛔)."),
                3: ("Effet attendu de la nébulisation : la renouveler", "Faux : la nébulisation ne donne ni somnolence ni sueurs.")})
E("L22", props={2: ("Fréquence respiratoire qui passe de 40 à 15 avec disparition des signes de lutte, patient bien éveillé", "Faux : c'est une amélioration (quiz p. 52).")}, lenok=True)
E("L23", q="Signe d'<u>hypoxémie</u> ?")
E("L25", q="Signe(s) d'<u>hypercapnie</u> ?")
E("L26", q="Signe(s) neurologique(s) d'<u>hypercapnie</u> ?",
  props={3: ("Hémiplégie", "Faux : signe d'accident vasculaire cérébral.")})
E("L27", q="Mme L., BPCO, sous oxygène, devient confuse et somnolente, avec céphalées et sueurs ; glycémie capillaire normale. Trouble à suspecter ?",
  props={1: ("Hypoglycémie", "Faux : la glycémie capillaire, à contrôler devant toute confusion, est normale.")})
E("L28", q="Signe(s) d'<u>insuffisance cardiaque droite</u> ?")
E("L29", q="Signe(s) de <u>choc</u> ?")
E("L30", q="Seuil de fréquence <u>cardiaque</u> qui signe un retentissement hémodynamique grave ?",
  props={1: ("> 110/min", "Faux : seuil trop bas ; le seuil de gravité est 120/min (p. 51)."),
         3: ("> 140/min", "Faux : seuil trop haut : on alerte dès 120/min (⛔).")},
  dz={3: "attendre 140/min retarde l'alerte entre 120 et 140/min (cours p. 51)"})
E("L31", props={3: ("Hémiplégie", "Faux : signe d'accident vasculaire cérébral.")})
# --- M, N ---
E("M03", props={3: ("Hypothyroïdie", "Faux : non citée parmi les causes d'exacerbation (p. 52).")},
  sub=[("Le paracétamol n'est pas un dépresseur respiratoire (quiz p. 55).", "L'hypothyroïdie n'est pas citée.")])
E("M04", props={3: ("Paracétamol", "Faux : pas dépresseur respiratoire (quiz p. 55).")},
  sub=[("pneumothorax.", "pneumothorax. Le paracétamol n'est pas un dépresseur respiratoire (quiz p. 55).")])
E("N03", props={2: ("Air enrichi en oxygène", "Faux : chez le BPCO, on nébulise à l'air seul ; l'oxygène aggrave l'hypercapnie (p. 53)."),
                3: ("Oxygène ou air, indifféremment", "Faux : le gaz dépend de la maladie : air chez le BPCO, oxygène chez l'asthmatique (⛔, p. 53).")},
  dz={1: "nébuliser à l'oxygène à 6-8 L/min chez le BPCO aggrave l'hypercapnie (cours p. 53-54)", 3: "nébuliser à l'oxygène chez le BPCO aggrave l'hypercapnie (cours p. 53-54)"})
E("N04", props={2: ("Air enrichi en oxygène", "Faux : chez l'asthmatique, le gaz est l'oxygène (p. 53)."),
                3: ("Oxygène ou air, indifféremment", "Faux : le gaz dépend de la maladie : oxygène chez l'asthmatique, air chez le BPCO (p. 53).")})
E("N05", props={1: ("Prise d'oxygène murale, 10 L/min, à la place de l'oxygène nasal", "Faux : oxygène à fort débit chez le BPCO : hypercapnie (⛔).")})
E("N06", props={1: ("Bricanyl + Atrovent : 3 nébulisations en 24 h", "Faux : en exacerbation, les 3 nébulisations se font sur 1 h (p. 53), pas sur une journée."),
                2: ("Ventoline + Atrovent : 1 nébulisation par jour", "Faux : rythme d'entretien, pas d'exacerbation ; le cours prescrit 3 nébulisations en 1 h."),
                3: ("Bricanyl seul : 6 nébulisations en 1 h", "Faux : surdosage ; le cours associe Bricanyl et Atrovent, 3 fois en 1 h.")})
E("N07", props={2: ("L'oxygène assèche les sécrétions et bouche les bronches", "Faux : l'oxygène non humidifié assèche les muqueuses, mais ce n'est pas le mécanisme du risque d'hypercapnie."),
                3: ("L'oxygène fait baisser la pression artérielle", "Faux : l'oxygène ne fait pas baisser la pression artérielle ; le risque est la baisse de la ventilation.")},
  x="Complément : d'autres mécanismes s'ajoutent à la suppression de la « commande hypoxique » : les zones mal ventilées du poumon sont de nouveau irriguées, et l'hémoglobine chargée d'oxygène transporte moins de CO2 (effet Haldane) ; la conduite pratique ne change pas (cible 88-92 %). Source : Sarkar et al., Monaldi Arch Chest Dis 2023, https://www.monaldi-archives.org/macd/article/view/2399")
E("N08", props={1: ("Une hypoxie profonde non corrigée expose à l'arrêt cardiaque", "Vrai : risque d'arrêt cardiaque hypoxique (p. 54)."),
                3: ("Une SpO2 à 85 % sous oxygène est suffisante", "Faux : 85 % est trop bas ; la cible est ≈ 90 % (⛔).")},
  dz={2: "viser 100 % chez le BPCO : bradypnée et hypercapnie (cours p. 54)", 3: "se satisfaire d'une SpO2 à 85 % expose à l'hypoxie profonde (cours p. 54)"})
E("N09", dz={1: "une saturation de 95 % chez le BPCO sévère expose à l'hypercapnie (cours p. 54)", 2: "une saturation de 98 % chez le BPCO sévère expose à l'hypercapnie (cours p. 54)", 3: "une saturation de 85 % expose à l'hypoxie profonde (cours p. 54)"},
  props={1: ("Environ 95 %", "Faux : trop haut, risque d'hypercapnie ; > 95 % = asthme (⛔).")})
E("N10", props={0: ("Débuter l'oxygène nasal à faible débit, alerter et faire préciser la cible", "Vrai : SpO2 84 % = hypoxémie grave : oxygène à faible débit, alerte, cible (p. 47, 53-54).")}, lenok=True)
E("N11", dz={1: "oxygène à haute concentration chez le BPCO hypercapnique : aggravation de l'hypercapnie (cours p. 54)", 2: "benzodiazépine : dépresseur respiratoire (cours p. 52)"},
  props={1: ("Oxygène au masque à haute concentration", "Faux : aggrave l'hypercapnie (⛔)."),
         2: ("Benzodiazépine pour diminuer l'agitation", "Faux : dépresseur respiratoire (⛔, p. 52).")})
E("N12", props={2: ("Prise en charge nutritionnelle", "Vrai : nutrition (p. 54).")})
_GOLD = "⚠ Non confirmé : les recommandations internationales (GOLD 2026) proposent des corticoïdes par voie générale, jusqu'à 5 jours, dans les exacerbations modérées à sévères ; le cours les réserve à certains cas (« parfois »). Source : rapport GOLD 2026, https://goldcopd.org/2026-gold-report-and-pocket-guide/ (résumé : Medical Independent, 17/04/2026)."
E("N13", dz={1: "viser > 95 % chez le BPCO expose à l'hypercapnie (cours p. 54)"},
  props={1: ("La saturation cible doit être > 95 %", "Faux : cible ≈ 90 % (⛔, quiz p. 56).")},
  x=_BASE["N13"].x + "<br>" + _GOLD)
E("N14", x=_GOLD)
E("N15", props={2: ("Il est réservé aux douleurs intenses", "Faux : c'est un antalgique des douleurs légères à modérées.")})
# --- O, P ---
E("O01", props={2: ("Troisième cause", "Faux : c'est la première (p. 57)."), 3: ("Cause rare", "Faux : pathologie très fréquente (p. 57).")})
E("O03", props={1: ("Le diététicien", "Faux : non habilité à prescrire des substituts nicotiniques."),
                2: ("Le psychologue", "Faux : non habilité à prescrire des substituts nicotiniques."),
                3: ("Le préparateur en pharmacie", "Faux : non habilité à prescrire des substituts nicotiniques.")})
E("O04", q="Rôle infirmier dans la prise en charge du tabagisme : vrai ou faux ?",
  props={0: ("La prise en charge du tabac est réservée au médecin", "Faux : l'infirmier aborde le tabac (4 A : demander, conseiller, aider, organiser le suivi) (quiz p. 59)."),
         1: ("Un infirmier a le droit de prescrire des substituts nicotiniques", "Vrai : prescription autorisée (quiz p. 59).")},
  sub=[("(4 A, compétence 5)", "(4 A : demander, conseiller, aider, organiser le suivi ; compétence 5)")])
E("O06", props={3: ("Sirop", "Faux : forme non citée ; les formes orales sont gommes, pastilles et comprimés (p. 58).")})
E("O07", q="Forme(s) de substituts nicotiniques disponible(s), parmi les suivantes ?",
  props={3: ("Gel cutané", "Faux : forme non citée ; la voie cutanée, c'est le patch (p. 58).")})
E("O08", props={0: ("Timbres forte + moyenne dose + forme orale", "Vrai : > 30 cigarettes et < 5 min après le lever : timbres forte + moyenne dose + forme orale (p. 58)."),
                2: ("Timbre moyenne dose seul", "Faux : dose adaptée à une dépendance moyenne, insuffisante ici.")})
E("O09", q="Prise en charge des substituts nicotiniques par l'Assurance maladie depuis 2018 ?",
  props={1: ("30 %, sans prise en charge en ALD", "Faux : 30 % est un autre taux de remboursement de la Sécurité sociale ; les substituts sont à 65 % (p. 58).")})
E("O10", props={0: ("Ask, Advise, Assist, Arrange", "Vrai : Ask, Advise, Assist, Arrange (p. 58)."),
                1: ("Assess, Advise, Assist, Arrange", "Faux : « Assess » (évaluer) appartient aux 5 A ; les 4 A commencent par Ask (demander)."),
                2: ("Ask, Advise, Accept, Abandon", "Faux : après le conseil viennent l'aide (Assist) et le suivi (Arrange)."),
                3: ("Alert, Act, Avoid, Arrange", "Faux : seul Arrange appartient aux 4 A ; les autres sont Ask, Advise, Assist.")})
E("O11", q="Étape « Assist » des 4 A de l'aide au sevrage tabagique ?",
  props={2: ("Conseiller l'arrêt du tabac", "Faux : c'est Advise.")})
E("O12", titre="Cas clinique",
  props={0: ("Conseiller le sevrage, proposer des substituts nicotiniques et organiser le suivi", "Vrai : les 4 A et la prescription infirmière des substituts (p. 57-58)."),
         3: ("Laisser le médecin seul aborder le tabac, qui n'est pas de la compétence infirmière", "Faux : l'infirmier peut aborder le tabac et prescrire (p. 57).")}, lenok=True)
E("P01", props={2: ("Sous oxygène", "Faux : l'oxygène ne modifie pas le rapport VEMS/CVF ; seule l'inhalation d'un bronchodilatateur est exigée."),
                3: ("Juste après un effort", "Faux : les EFR se font au repos ; seule l'inhalation d'un bronchodilatateur est exigée.")})
E("P02", props={2: ("Le tabac est la seule cause de BPCO", "Faux : il en cause 85 % ; d'autres expositions existent (pollution, expositions professionnelles, p. 17, 27).")})
E("P03", q="M. Y., 55 ans, fumeur depuis 35 ans, dyspnée d'effort depuis 2 ans ; il ne tousse pas. Examen qui confirmera une BPCO ?")
E("P04", q="Mme T., 45 ans, <u>sans antécédent respiratoire</u>, au lendemain d'une chirurgie : SpO2 89 % en air ambiant. Interprétation ?")
E("P09", truth="0001",
  props={3: ("Les signes de gravité sont ceux de l'insuffisance respiratoire aiguë", "Vrai : non spécifiques de la BPCO (p. 46).")},
  dz={0: "se rassurer sur une SpO2 à 98 % fait manquer une polypnée grave (quiz p. 52)", 1: "prendre une baisse de fréquence avec somnolence pour une amélioration fait manquer un épuisement (quiz p. 52)"})
E("P10", truth="1110",
  props={2: ("Une hypoxie profonde non corrigée expose à l'arrêt cardiaque", "Vrai : arrêt cardiaque hypoxique (p. 54)."),
         3: ("Les nébulisations de bronchodilatateurs se font à l'oxygène", "Faux : chez le BPCO, nébulisation à l'air 6-8 L/min (⛔, p. 53).")},
  dz={3: "nébuliser à l'oxygène chez le BPCO aggrave l'hypercapnie (cours p. 53-54)"})
E("P12", q="M. W., BPCO sévère : turgescence jugulaire, reflux hépato-jugulaire, œdèmes des chevilles. Retentissement en cause ?",
  props={1: ("Insuffisance cardiaque gauche", "Faux : on attendrait un essoufflement en position couchée (orthopnée) et des signes d'œdème pulmonaire."),
         3: ("Hypertension artérielle", "Faux : on attendrait une pression artérielle élevée, sans œdèmes ni turgescence jugulaire.")})
E("P14", props={2: ("La nutrition relève du seul médecin", "Faux : la prise en charge nutritionnelle fait partie de la réhabilitation, pluridisciplinaire (p. 38).")})
E("V01", x=X("V02"))
E("V06", q="Terme qui désigne des pertes brèves et répétées du tonus des mains, bras tendus (« battement d'ailes »), signe d'hypercapnie ?",
  sub=[("secousses brusques et irrégulières lors du maintien d'une attitude", "pertes brèves et répétées du tonus lors du maintien d'une attitude (« battement d'ailes »)")])

# --- itération 2 (contrôles de build.py) ---
E("B06", props={0: ("Le VEMS", "Vrai : la sévérité du TVO se classe selon la valeur du VEMS, en % de la valeur prédite (p. 5, 34).")})
E("D06", props={2: ("Expectoration et dyspnée ≥ 3 mois par an pendant ≥ 3 ans", "Faux : il faut une toux, pas une dyspnée ; et la durée est d'au moins 2 ans.")})
E("D15", props={1: ("Dilatation chronique des bronches", "Faux : c'est une autre maladie, qui peut donner un TVO (p. 6), pas l'évolution commune."),
                2: ("Asthme sévère chronique", "Faux : l'asthme est une autre maladie (obstruction réversible), pas une évolution."),
                3: ("Fibrose pulmonaire chronique", "Faux : la fibrose est une cause de restriction (p. 5).")})
E("E03", props={0: ("L'arrêt ralentit le déclin du souffle, même tardif", "Vrai : sevrage = seul traitement qui ralentit le déclin du VEMS, bénéfice même à 65 ans (p. 19, 37).")})
E("F01", props={2: ("Complication propre à la BPCO, absente des autres maladies respiratoires", "Faux : d'autres maladies respiratoires y aboutissent (p. 20).")})
E("F02", props={0: ("Par 2 gaz du sang à l'état stable, à ≥ 3 semaines d'intervalle", "Vrai : gaz du sang répétés (intervalle ≥ 3 semaines), à l'état stable (p. 20, quiz p. 25)."),
                2: ("Par 2 gaz du sang à 3 semaines d'intervalle, dont 1 lors d'une exacerbation", "Faux : il faut être à distance d'un épisode aigu (p. 20)."),
                3: ("Par un seul gaz du sang, en air ambiant et au repos", "Faux : un seul prélèvement ne suffit pas : mesures répétées (p. 20).")})
E("H11", props={2: ("La BPCO est plus fréquente chez les 20-30 ans qu'après 65 ans", "Faux : la BPCO augmente avec l'âge (quiz p. 36).")})
E("H13", props={0: ("D'effort le plus souvent, pas toujours liée aux gaz du sang", "Vrai : le plus souvent à l'effort, pas toujours bien corrélée aux gaz du sang (p. 31)."),
                2: ("Limitée aux exacerbations de la maladie", "Faux : elle est permanente, le plus souvent à l'effort ; l'exacerbation est une aggravation aiguë (p. 31, 46).")})
E("J03", props={2: ("Tuberculose", "Faux : ce vaccin protège de la tuberculose ; il n'est pas cité pour prévenir les surinfections de la BPCO.")})
E("O04", props={0: ("La prise en charge du tabac est réservée au médecin, pas à l'infirmier", "Faux : l'infirmier aborde le tabac (4 A : demander, conseiller, aider, organiser le suivi) (quiz p. 59).")})
E("O08", props={1: ("Forme orale seule, à la demande", "Faux : pour une faible dépendance."),
                2: ("Timbre moyenne dose seul, sans forme orale", "Faux : dose adaptée à une dépendance moyenne, insuffisante ici.")})
E("O10", ok={"M8": "séquence de 4 mots fixée par le cours : la bonne valeur de chaque rang est forcément commune à plusieurs propositions ; chaque distracteur cible une confusion nommée (5 A, étapes inventées) ; à valider par l'étudiant"})
E("H13", props={0: ("D'effort, pas toujours corrélée aux gaz du sang", "Vrai : le plus souvent à l'effort, pas toujours bien corrélée aux gaz du sang (p. 31)."),
                3: ("Surtout la nuit, au repos, en position couchée", "Faux : la dyspnée en position couchée (orthopnée) n'est pas la définition ; la dyspnée chronique est le plus souvent d'effort (p. 31).")})

E("B06", expl="Cours p. 5 : la sévérité du TVO se classe selon la valeur du VEMS (léger, sévère, très sévère) ;<br>la grille de référence, plus complète, est celle des stades I à IV (p. 34) ;<br>le rapport VEMS/CV fait le diagnostic ;<br>la CPT juge la restriction.")
E("E04", expl="Cours p. 20 : l'« étape » bronchite chronique n'est pas obligatoire ;<br>la bronchite chronique est une définition clinique (p. 16) ;<br>un emphysème au scanner peut exister sans TVO aux EFR, il ne suffit donc pas à affirmer une BPCO ;<br>quiz p. 23 : emphysème et BPCO ne sont pas synonymes.")

# --- 2e relecture ---
E("O08", props={0: ("Timbres forte + moyenne dose ± forme orale", "Vrai : > 30 cigarettes et < 5 min après le lever : timbres forte + moyenne dose ± forme orale (tableau p. 58).")},
  sub=[("timbres forte + moyenne dose + forme orale.", "timbres forte + moyenne dose ± forme orale.")])
_ADV = "✎ Modifié par rapport au cours : « Advice » (nom anglais, diapo p. 58) → « Advise » (verbe), comme les 3 autres étapes des 4 A."
E("O10", x=_ADV)
E("O11", x=_ADV)
E("I12", props={3: ("Perte de poids involontaire", "Faux : elle mène à la dénutrition, facteur de mauvais pronostic (p. 32).")})
E("C02", props={3: ("Rapport VEMS/CV jamais normalisé par un bronchodilatateur", "Vrai : un effet des bronchodilatateurs est possible, mais l'obstruction ne disparaît jamais (p. 7).")},
  x="✎ Modifié par rapport au cours : « le VEMS ne redevient jamais normal » (p. 7) → « rapport VEMS/CV jamais normalisé » : au stade I, le VEMS est ≥ 80 % de la valeur prédite (p. 34) ; c'est l'obstruction (rapport < 70 %) qui persiste.")
E("J03", pg=[37])
E("K07", props={3: ("Spray nasal", "Faux : un spray nasal agit dans le nez ; les sprays inhalés se prennent par la bouche (p. 41-42).")},
  sub=[("Un comprimé n'est pas une voie inhalée.", "Un spray nasal n'est pas un système d'inhalation bronchique.")])

# --- 2e relecture, règles lot 2 ---
E("I03", q="Stade de sévérité d'une BPCO avec VEMS à 45 % de la valeur prédite, <u>sans insuffisance respiratoire ni cardiaque droite</u> ?", lenok=True)
E("I12", q="Entre surpoids et dénutrition, statut pondéral <u>le moins défavorable</u> au pronostic d'un patient BPCO ?",
  props={2: ("Les deux sont équivalents", "Faux : la dénutrition est de mauvais pronostic (p. 32) ; « mieux vaut être en surpoids que dénutri » (quiz p. 36)."),
         3: ("Aucun des deux n'influence le pronostic", "Faux : le poids et l'état nutritionnel comptent pour le pronostic (p. 34).")})
E("K05", props={2: ("Confusion entre le traitement quotidien et celui de crise", "Vrai : mauvaise compréhension fond/crise (p. 41).")})
E("K02", props={3: ("Corticoïdes oraux au long cours seuls", "Faux : les corticoïdes oraux ne sont pas un traitement de fond de la BPCO (p. 40).")})
E("L11", props={3: ("Hypercapnie certaine : arrêter l'oxygène", "Faux : rien n'affirme une hypercapnie, et arrêter l'oxygène expose à l'hypoxie profonde (⛔, p. 54).")},
  dz={1: "la polypnée > 30/min impose d'alerter, même avec une SpO2 dans la cible (cours p. 48)", 2: "une fréquence de 34/min est un signe de gravité (cours p. 48)", 3: "arrêter l'oxygène expose à l'hypoxie profonde et à l'arrêt cardiaque hypoxique (cours p. 54)"})
E("L10", props={1: ("> 16/min", "Faux : 16/min est la borne haute de la normale du cours (p. 48), pas le seuil de gravité."),
                2: ("> 20/min", "Faux : polypnée, mais pas le seuil de gravité du cours (p. 48).")})
E("H21", props={3: ("Le poids normal", "Faux : un poids normal n'est pas un facteur de mauvais pronostic ; c'est la dénutrition (p. 32).")})
E("L13", props={1: ("Compter inspirations et expirations sur 15 s, multiplier par 4", "Faux : un cycle = une inspiration + une expiration ; les compter séparément double la fréquence.")})
E("H18", props={1: ("Le thorax est toujours normal à l'examen", "Faux : le patient emphysémateux sévère a un thorax distendu (p. 32).")})
E("L06", q="Trouble des gaz du sang particulièrement à craindre chez le patient BPCO en exacerbation ?")
E("I12", ok={"R7": "l'énoncé pose la comparaison du cours (surpoids contre dénutrition) ; les deux termes sont des propositions, la dénutrition étant la mauvaise réponse"})

# --- 2e relecture, règles lot 1 ---
E("A16", q="Formule(s) exacte(s) reliant les volumes pulmonaires ?",
  props={2: ("CV = VRE + VR", "Faux : VRE + VR = CRF ; la CV additionne le volume courant et les volumes de réserve inspiratoire et expiratoire (p. 3)."),
         3: ("CRF = CV − VRI", "Faux : CV − VRI = volume courant + VRE ; la CRF = VRE + VR (p. 3).")})
E("B06", q="Paramètre qui sert à classer la <u>sévérité</u> d'un trouble ventilatoire obstructif ?",
  x="⚠ Non confirmé : la grille de la diapo p. 5 est incomplète (pas de stade modéré, intervalles non jointifs) ; la grille de référence (Société de pneumologie de langue française, recommandations internationales) est celle des stades I à IV (p. 34) : léger ≥ 80 %, modéré 50-80 %, sévère 30-50 %, très sévère < 30 %.")
E("C09", q="Paramètre qui doit être diminué pour poser le <u>diagnostic</u> de trouble ventilatoire obstructif ?")
E("B12", props={0: ("Chirurgie (exérèse)", "Vrai : cause parenchymateuse (p. 5)."), 2: ("Fibrose", "Vrai : cause parenchymateuse (p. 5).")})
E("C01", props={3: ("Mise en évidence par une baisse de la CPT", "Faux : la CPT juge la restriction ; l'obstruction se voit sur le rapport VEMS/CV (p. 4-5).")})
E("C02", props={1: ("Persiste en dehors des exacerbations", "Vrai : obstruction permanente, présente même à l'état stable (p. 7, 18).")})
E("C03", q="Critère des EFR qui distingue l'asthme <u>en crise</u> de la BPCO ?")
E("C06", truth="1110", props={3: ("Capacité pulmonaire totale forcément abaissée", "Faux : la CPT juge la restriction ; elle n'est pas mesurée ici et la BPCO tend plutôt à l'augmenter (distension, p. 33).")},
  expl="Cours p. 7 (et notes) : rapport 43 % < 70 % = trouble obstructif ;<br>VEMS 27 % < 30 % = très sévère ;<br>pas de gain après Ventoline = non réversible, donc BPCO et non asthme ;<br>la CPT juge la restriction (p. 5).")
E("C07", q="Type de maladie respiratoire chronique auquel appartient l'asthme ?")
E("D06", q="Définition clinique de la <u>bronchite chronique</u> ?")
E("D08", q="Définition de la <u>BPCO</u> en une phrase ?")
E("D11", q="Définition de l'<u>emphysème</u> ?")
E("D07", q="M. C., 52 ans, fumeur, toux avec expectoration chaque matin, 4 mois par an depuis 3 ans ; EFR normales. Diagnostic le plus probable ?")
E("D09", q="Qualificatif(s) exact(s) de l'obstruction des voies aériennes dans la <u>BPCO</u> ?",
  props={2: ("D'origine infectieuse", "Faux : les infections déclenchent des exacerbations (p. 52), mais l'obstruction est due au tabac dans 85 % des cas (p. 17).")},
  sub=[("elle n'est ni réversible ni d'origine allergique (asthme).", "elle n'est ni d'origine infectieuse ni allergique (asthme).")])
E("E04", truth="0110", props={1: ("L'emphysème est une lésion anatomique vue au scanner", "Vrai : définition anatomique et radiologique de l'emphysème (p. 16-17).")})
E("F02", props={1: ("Par 1 gaz du sang sous oxygène, au repos", "Faux : un seul prélèvement ne suffit pas, et l'oxygène fausse la PaO2 (p. 20)."),
                2: ("Par 3 gaz du sang lors d'une exacerbation, à 24 h d'intervalle", "Faux : il faut être à distance d'un épisode aigu, avec ≥ 3 semaines entre les mesures (p. 20)."),
                3: ("Par 2 spirométries à l'état stable, à 3 semaines d'intervalle", "Faux : la spirométrie diagnostique la BPCO ; l'IRC se juge sur la PaO2, aux gaz du sang (p. 20).")})
E("F05", mode=2, truth="1000", q="Seuils de <u>PaO2</u> de l'insuffisance respiratoire chronique grave ?",
  props={0: ("< 55 mmHg, ou < 60 mmHg avec retentissement", "Vrai : PaO2 < 55 mmHg, ou < 60 mmHg si retentissement cardiaque droit ou polyglobulie (p. 20, quiz p. 26)."),
         1: ("< 60 mmHg, ou < 65 mmHg avec retentissement", "Faux : 60 mmHg est le seuil avec retentissement, pas le seuil simple (p. 20)."),
         2: ("< 50 mmHg, ou < 55 mmHg avec retentissement", "Faux : 55 mmHg est le seuil simple, pas le seuil avec retentissement (p. 20)."),
         3: ("< 58 mmHg, ou < 62 mmHg avec retentissement", "Faux : 58 et 62 mmHg ne sont pas des seuils du cours ; les seuils sont 55 et 60 mmHg.")})
E("F08", q="Seuil de <u>PaCO2</u> de l'hypercapnie associé aux critères d'insuffisance respiratoire chronique grave ?", lenok=True,
  x=_BASE["F08"].x.replace("(HAS, Assurance maladie)", "(Haute Autorité de santé, Assurance maladie)"))
E("F09", props={2: ("L'hypercapnie contracte les vaisseaux pulmonaires et surcharge le cœur gauche", "Faux : c'est l'hypoxémie qui contracte les vaisseaux pulmonaires, et c'est le cœur droit qui envoie le sang aux poumons.")})
E("G03", q="Seuil de SpO2 en dessous duquel la saturation est inquiétante chez un patient <u>sans insuffisance respiratoire chronique</u> ?", lenok=True)
E("G06", props={3: ("Entre 90 et 92 %", "Faux : trop bas pour un asthmatique en crise (⛔).")},
  dz={1: "viser 88-92 % chez l'asthmatique en crise l'expose à l'hypoxémie (notes p. 21)", 2: "une SpO2 de 85-88 % est une hypoxémie (cours p. 21)", 3: "viser 90-92 % chez l'asthmatique en crise l'expose à l'hypoxémie (notes p. 21)"})

# --- 2e relecture, règles lot 3 ---
E("A03", props={3: ("La pression artérielle pulmonaire", "Faux : elle se mesure par échographie du cœur ou par une sonde poussée jusque dans l'artère pulmonaire, pas par les EFR.")},
  sub=[("par une sonde poussée jusqu'au cœur droit)", "par une sonde poussée jusque dans l'artère pulmonaire)")])
E("N06", props={1: ("Ventoline + Atrovent : 1 nébulisation en 1 h", "Faux : le cours associe Bricanyl (et non Ventoline) et Atrovent, 3 fois en 1 h (p. 53)."),
                2: ("Bricanyl + Atrovent : 1 nébulisation en 24 h", "Faux : en exacerbation, 3 nébulisations sur 1 h, pas 1 par jour (p. 53)."),
                3: ("Ventoline + Atrovent : 3 nébulisations en 24 h", "Faux : le cours associe Bricanyl et Atrovent, 3 nébulisations sur 1 h et non sur 24 h (p. 53).")})
E("P02", props={2: ("L'arrêt du tabac est inutile après 65 ans", "Faux : la courbe de Fletcher montre un bénéfice même pour un arrêt à 65 ans (p. 28).")})
E("N07", q="Mécanisme du risque d'hypercapnie de l'oxygène à fort débit chez le patient BPCO ?")
E("L31", q="Signe(s) de retentissement <u>neurologique</u> d'une détresse respiratoire ?")
E("N09", q="Saturation « cible » habituelle d'un patient <u>BPCO sévère</u> sous oxygène ?")
E("P14", props={0: ("La dénutrition aggrave le pronostic", "Vrai : perte de 6 kg en 6 mois et IMC à 17 = dénutrition, facteur de mauvais pronostic ; la nutrition fait partie de la réhabilitation (p. 32, 38)."),
                2: ("Un régime hypocalorique est indiqué", "Faux : chez cette patiente dénutrie, on vise au contraire la reprise de poids (quiz p. 36).")})
E("N05", props={3: ("Prise d'air murale, 15 L/min, à la place de l'oxygène nasal", "Faux : on nébulise à 6-8 L/min, et l'oxygène nasal, nécessaire contre l'hypoxémie, est maintenu à part (⛔, p. 53-54).")},
  dz={1: "oxygène à 10 L/min chez le BPCO : risque d'hypercapnie (cours p. 53-54)", 2: "oxygène à haut débit chez le BPCO : bradypnée et hypercapnie (cours p. 54)", 3: "retirer l'oxygène nasal pendant la nébulisation expose à l'hypoxémie (cours p. 54)"})
E("O01", props={1: ("Deuxième cause, après l'asthme", "Faux : la BPCO est la première cause d'IRC (p. 57)."),
                2: ("Deuxième cause, après la fibrose pulmonaire", "Faux : la BPCO est la première cause d'IRC (p. 57)."),
                3: ("Troisième cause", "Faux : la BPCO est la première cause d'IRC (p. 57).")})
E("N04", dz={1: "nébuliser à l'air un asthmatique en crise le prive de l'oxygène dont il a besoin (cours p. 53)", 3: "nébuliser à l'air un asthmatique en crise le prive de l'oxygène dont il a besoin (cours p. 53)"},
  props={1: ("Air", "Faux : c'est le gaz du patient BPCO ; chez l'asthmatique, l'oxygène (⛔, p. 53)."),
         3: ("Oxygène ou air, indifféremment", "Faux : le gaz dépend de la maladie : oxygène chez l'asthmatique, air chez le BPCO (⛔, p. 53).")})
E("N12", x=_GOLD)

# --- 3e relecture ---
E("L13", props={1: ("Compter à part chaque inspiration et chaque expiration sur 15 s, × 4", "Faux : un cycle = une inspiration + une expiration ; les compter séparément double la fréquence.")}, lenok=True)
E("P02", props={3: ("L'arrêt du tabac fait récupérer tout le VEMS perdu", "Faux : on récupère difficilement ce qu'on a perdu (p. 19).")})

# --- 3e relecture, règles ---
E("B06", q="Paramètre qui sert à classer la <u>sévérité</u> d'un <u>trouble ventilatoire obstructif</u> ?")
E("C09", q="Paramètre qui doit être diminué pour poser le <u>diagnostic</u> de <u>trouble ventilatoire obstructif</u> ?", lenok=True)
E("L31", q="Signe(s) de retentissement <u>neurologique</u> d'une <u>détresse respiratoire</u> ?")
E("P14", q="Mme S., BPCO sévère, a perdu 6 kg en 6 mois ; son IMC est à 17. Intérêt d'une prise en charge diététique ?")
E("K07", props={3: ("Gouttes nasales", "Faux : elles agissent dans le nez ; ce n'est pas un système d'inhalation bronchique.")},
  sub=[("Un spray nasal n'est pas un système d'inhalation bronchique.", "Les gouttes nasales ne sont pas un système d'inhalation.")])
E("L06", q="Trouble biologique particulièrement à craindre chez le patient BPCO en exacerbation ?",
  props={2: ("Hyperoxémie", "Faux : excès d'oxygène dans le sang ; le patient en exacerbation en manque, et l'excès d'O2 apporté aggrave l'hypercapnie (p. 54).")})
E("F09", props={2: ("L'hypoxémie dilate les vaisseaux pulmonaires et freine le cœur droit", "Faux : l'hypoxémie contracte (et non dilate) les vaisseaux pulmonaires, ce qui augmente le travail du cœur droit."),
                3: ("L'hypercapnie contracte les bronches et surcharge le cœur droit", "Faux : le mécanisme passe par les vaisseaux pulmonaires, contractés par l'hypoxémie, pas par les bronches.")})
E("O10", ok={}, props={1: ("Assess, Alert, Assist, Approve", "Faux : « Assess » (évaluer) appartient aux 5 A ; la 1re étape des 4 A est Ask (demander)."),
                       2: ("Ask, Alert, Act, Approve", "Faux : après Ask viennent Advise (conseiller), Assist (proposer un traitement) et Arrange (suivi)."),
                       3: ("Assess, Advise, Act, Arrange", "Faux : la 1re étape est Ask (demander) et la 3e Assist (proposer un traitement).")})
_ADV2 = "✎ Modifié par rapport au cours : « Advic&#101; » (nom anglais, diapo p. 58) → « Advise » (verbe), comme les 3 autres étapes des 4 A."
E("O10", x=_ADV2); E("O11", x=_ADV2)
E("N06", props={1: ("Bricanyl + Atrovent : 1 nébulisation en 24 h", "Faux : en exacerbation, 3 nébulisations sur 1 h, pas 1 par jour (p. 53)."),
                2: ("Bricanyl seul : 3 nébulisations en 24 h", "Faux : le cours associe l'Atrovent, et les 3 nébulisations se font sur 1 h (p. 53)."),
                3: ("Atrovent seul : 6 nébulisations en 1 h", "Faux : le cours associe un bronchodilatateur de courte durée (Bricanyl ou Ventoline), 3 fois et non 6 (p. 53).")})
E("G03", props={1: ("< 88 %", "Faux : 88 % est la borne basse tolérée chez le BPCO ; chez un patient sans insuffisance respiratoire, on s'inquiète dès 90 % (⛔).")},
  dz={1: "attendre 88 % chez un patient sans insuffisance respiratoire retarde l'alerte (cours p. 21)", 3: "attendre 85 % pour s'inquiéter retarde l'alerte devant une hypoxémie (cours p. 21)"})
E("I03", q="Stade de sévérité d'une BPCO avec VEMS à 45 % de la valeur prédite, <u>sans insuffisance respiratoire ni insuffisance cardiaque droite</u> ?")
E("C06", q="EFR : VEMS/CVF 43 %, VEMS à 27 % de la valeur prédite avant et à 32 % après Ventoline. Interprétation(s) exacte(s) ?")
E("F09", props={3: ("L'hypercapnie contracte les bronches et épuise le cœur droit", "Faux : le mécanisme passe par les vaisseaux pulmonaires, contractés par l'hypoxémie, pas par les bronches.")})
E("O10", props={2: ("Ask, Alert, Accept, Approve", "Faux : après Ask viennent Advise (conseiller) et Assist (proposer un traitement)."),
                3: ("Assess, Advise, Accept, Analyse", "Faux : la 1re étape est Ask (demander) et la dernière Arrange (organiser le suivi).")})
