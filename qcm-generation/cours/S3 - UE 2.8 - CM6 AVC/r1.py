from common import Q
QS = []
a = QS.append
GAUCHER_X = "✎ Modifié par rapport au cours : « gaucher : hémisphère majeur droit » → « gauche chez la majorité des gauchers » (la dominance droite ne concerne qu'une minorité de gauchers)."
GAUCHER_W = ["Web — Techno-Science, Préférence manuelle et langage : existe-t-il un hémisphère dominant ?, https://www.techno-science.net/fr/actualites/preference-manuelle-et-langage-existe-t-il-un-hemisphere-dominant-12938"]

# ---------- Épidémiologie ----------
a(Q("A01","K002",2,"Rang comme cause de <u>handicap</u> acquis de l'adulte en France ?",
 ["1re","2e","3e","4e"],"1000","Cours p. 1 : 1re cause de handicap de l'adulte, 2e cause de démence, 3e cause de décès."))
a(Q("A02","K003 K004",0,"Rang en France : vrai ou faux ?",
 ["2e cause de démence","3e cause de décès","1re cause de décès chez la femme","1re cause de décès chez l'homme"],"1110",
 "Diapo p. 1 : 2e cause de démence, 3e cause de décès. Note de cours : 1re cause de décès chez la femme ; ce n'est pas le cas chez l'homme."))
a(Q("A03","K001",2,"Nombre de cas par an en France ?",
 ["80 000","150 000","250 000","400 000"],"0100","Cours p. 1 : 150 000 par an."))
a(Q("A04","K005",1,"Âge des patients ?",
 ["Âge médian d'environ 75 ans","Environ 10 % ont moins de 45 ans","Âge médian d'environ 65 ans","Environ 25 % ont moins de 45 ans"],"1100",
 "Cours p. 1 : âge médian 75 ans ; 10 % ont moins de 45 ans."))
a(Q("A05","K006",2,"Devenir à 1 an (graphique du cours) ?",
 ["≈ 1/2 décès, 1/4 handicap, 1/4 autonomie","≈ 1/4 décès, 1/2 handicap, 1/4 autonomie","≈ 1/4 décès, 1/4 handicap, 1/2 autonomie","≈ 1/3 décès, 1/3 handicap, 1/3 autonomie"],"0100",
 "Graphique p. 1 : environ un quart de décès, la moitié avec handicap, un quart autonome."))
a(Q("A06","K007",2,"Filière de soins spécialisée ?",
 ["Pré-hospitalier ; unité neurovasculaire ; rééducation","Pré-hospitalier ; réanimation ; rééducation","Urgences ; cardiologie ; rééducation","Pré-hospitalier ; unité neurovasculaire ; EHPAD"],"1000",
 "Cours p. 1 : filière pré-hospitalier → UNV → rééducation.","Filière"))

# ---------- Définitions ----------
a(Q("A07","K008",2,"Part des formes <u>ischémiques</u> parmi les accidents artériels ?",
 ["≈ 60 %","≈ 70 %","≈ 85 %","≈ 95 %"],"0010","Cours p. 1 : artère qui se bouche = 85 % ; artère qui se rompt = 15 %.","Types"))
a(Q("A08","K008",1,"Mécanismes décrits dans le cours ?",
 ["Rupture d'une artère","Occlusion d'une artère","Occlusion d'une veine","Compression d'un nerf crânien"],"1110",
 "Cours p. 1 : artère qui se rompt (hémorragie), artère qui se bouche (ischémie), plus rarement veine qui se bouche (thrombose veineuse cérébrale).","Types"))
a(Q("A09","K008",2,"Mécanisme d'une <u>hémorragie</u> cérébrale ?",
 ["Occlusion d'une artère","Rupture d'une artère","Occlusion d'une veine","Spasme d'une artère"],"0100","Hémorragie = artère qui se rompt.","Types"))
a(Q("A10","K009",1,"Conséquences directes de l'occlusion d'une artère cérébrale ?",
 ["Défaut d'apport en oxygène","Défaut d'apport en glucose","Saignement dans le parenchyme","Dilatation des ventricules"],"1100",
 "Cours p. 2 : insuffisance d'apport en O2 et glucose → nécrose (infarctus). Le saignement = hémorragie ; la dilatation des ventricules = hydrocéphalie.","Ischémie"))
a(Q("A11","K009",2,"Nom de la zone de nécrose due à l'occlusion artérielle ?",
 ["Pénombre","Infarctus cérébral","Hématome","Œdème"],"0100",
 "Cours p. 2 : la zone nécrosée est l'infarctus cérébral. La pénombre est la zone hypoperfusée encore sauvable (p. 14).","Ischémie"))
a(Q("A12","K010",2,"Définition de l'<u>AIT</u> ?",
 ["Occlusion artérielle temporaire, sans lésion constituée","Occlusion définitive d'une petite artère perforante","Petite hémorragie résorbée spontanément","Occlusion veineuse temporaire, sans lésion constituée"],"1000",
 "Cours p. 2 : AIT = l'artère se débouche, sans lésion ischémique constituée. Occlusion définitive d'une petite artère perforante = lacune.","Ischémie"))
a(Q("A13","K009 K010",0,"Accidents ischémiques cérébraux : vrai ou faux ?",
 ["Ils regroupent infarctus cérébral et AIT","Dans l'AIT, l'occlusion est définitive","L'infarctus correspond à une zone de nécrose","Ils représentent environ 15 % des cas"],"1010",
 "L'occlusion de l'AIT est temporaire ; les accidents ischémiques représentent 85 % des cas (15 % = hémorragies).","Ischémie"))
a(Q("A14","K013",2,"Principale cause d'hémorragie cérébrale ?",
 ["Fibrillation atriale","Athérome carotidien","Hypertension artérielle","Dissection cervicale"],"0010",
 "Cours p. 2 : principale cause = HTA. FA, athérome et dissection sont des causes d'infarctus.","Hémorragie"))
a(Q("A15","K013",2,"M. A., 68 ans, hypertendu mal équilibré, hémiplégie brutale. Le scanner montre un saignement dans le parenchyme. Cause la plus probable ?",
 ["Fibrillation atriale","Dissection vertébrale","Hypertension artérielle","Athérome carotidien"],"0010",
 "Cours p. 2 et 23 : l'HTA est la principale cause d'hémorragie cérébrale (≈ 80 % des hématomes non traumatiques).","Hémorragie",vign=True))
a(Q("A16","K014",1,"Formes hémorragiques citées dans le cours ?",
 ["Hémorragie intracérébrale","Hémorragie méningée","Hématome sous-dural","Thrombose veineuse cérébrale"],"1100",
 "Cours p. 2 : intracérébrale et méningée. Le sous-dural est traumatique ; la thrombose veineuse est une occlusion veineuse.","Hémorragie",allow=["hémorragie"]))
a(Q("A17","K011",0,"Cause d'infarctus cérébral : vrai ou faux ?",
 ["Athérome","Maladie des petites artères (lacunes)","Angiopathie amyloïde","Embolie d'origine cardiaque"],"1101",
 "Causes d'infarctus (p. 2) : athérome, lacunes, embolies cardiaques, causes rares, sans cause. L'angiopathie amyloïde est une cause d'hématome (p. 23).","Étiologies"))
a(Q("A18","K012",2,"Répartition des causes d'infarctus cérébral ?",
 ["Athérome 20 % ; lacunes 25 % ; cardio-embolies 20 % ; sans cause 30 %","Athérome 25 % ; lacunes 20 % ; cardio-embolies 20 % ; sans cause 30 %","Athérome 20 % ; lacunes 20 % ; cardio-embolies 25 % ; sans cause 30 %","Athérome 30 % ; lacunes 25 % ; cardio-embolies 20 % ; sans cause 20 %"],"1000",
 "Schéma p. 2 : athérome 20 %, lacunes 25 %, embolies cardiaques 20 %, causes rares 5 %, sans cause 30 %.","Étiologies"))

# ---------- Démarche diagnostique ----------
a(Q("B01","K016",2,"Caractéristiques du déficit qui doivent faire suspecter un accident vasculaire ?",
 ["Brutal et focal","Progressif et focal","Brutal et diffus","Progressif et diffus"],"1000",
 "Cours p. 3 : déficit neurologique brutal et focal (selon la zone atteinte)."))
a(Q("B02","K016",1,"Présentations à considérer comme un accident vasculaire jusqu'à preuve du contraire ?",
 ["Faiblesse du bras et de la face droits apparue en quelques secondes","Trouble de la parole survenu brutalement pendant le repas","Faiblesse des quatre membres installée en trois semaines","Confusion progressive sur trois jours avec fièvre"],"1100",
 "Déficit brutal + focal. Une installation sur des semaines ou un tableau fébrile progressif orientent ailleurs.",vign=True))
a(Q("B03","K015",2,"Pourquoi aucun traitement spécifique avant l'imagerie ?",
 ["Seule l'imagerie distingue ischémie et hémorragie","Seule l'imagerie permet d'évaluer la sévérité","Seule l'imagerie permet de dater les symptômes","Seule l'imagerie fixe la dose du thrombolytique"],"1000",
 "Cours p. 3 : impossible de distinguer ischémie et hémorragie sans imagerie. La sévérité se mesure par le NIHSS, le délai par l'interrogatoire, la dose par le poids.","Imagerie avant traitement"))
a(Q("B04","K015",2,"M. P., 66 ans, hémiparésie gauche brutale depuis 40 min. Son épouse veut lui donner l'aspirine de l'armoire à pharmacie en attendant les secours. Que lui dites-vous ?",
 ["De ne rien donner : le type d'accident n'est connu qu'après l'imagerie","De donner l'aspirine pour limiter l'extension du caillot","De lui donner un grand verre d'eau pour l'hydrater","De donner l'aspirine seulement s'il a des antécédents cardiaques"],"1000",
 "Cours p. 3 : aucun traitement sans imagerie (une hémorragie est possible). Ne rien donner par la bouche avant l'évaluation de la déglutition (p. 17).","Imagerie avant traitement",
 dz={1:"un antiagrégant aggrave une hémorragie cérébrale, impossible à exclure sans imagerie",2:"risque de fausse route : à jeun jusqu'au dépistage des troubles de la déglutition",3:"même risque hémorragique, quel que soit le terrain"},vign=True,lenok=True))
a(Q("B05","K017",1,"Étapes de la prise en charge ?",
 ["Rechercher la cause","Prévenir les récidives selon la cause","Attendre 24 h l'évolution spontanée","Débuter un antithrombotique avant l'imagerie"],"1100",
 "Cours p. 3 : diagnostic et type, traitement immédiat, étiologie, pronostic, prévention des récidives.","Démarche",
 dz={3:"un antithrombotique avant l'imagerie peut aggraver une hémorragie"}))
a(Q("B06","K018",2,"Vaisseau le plus souvent en cause ?",
 ["Artère","Veine","Sinus veineux","Capillaire"],"1000","Cours p. 3 : lésion d'un vaisseau cérébral : artère >> veine.","Démarche"))

# ---------- Rappels anatomiques ----------
a(Q("C01","K020",2,"Fonction principale du lobe <u>pariétal</u> ?",
 ["Sensibilité","Motricité","Vision","Mémoire"],"1000","Cours p. 4 : pariétal = sensibilité ; frontal = motricité ; occipital = vision ; temporal = mémoire, langage.","Lobes"))
a(Q("C02","K021",2,"Fonction principale du lobe <u>occipital</u> ?",
 ["Sensibilité","Motricité","Vision","Mémoire"],"0010","Cours p. 4 : occipital = vision.","Lobes"))
a(Q("C03","K019",1,"Fonctions du lobe <u>frontal</u> ?",
 ["Motricité","Fonctions exécutives","Vision","Sensibilité"],"1100","Cours p. 4 : frontal = motricité et fonctions exécutives.","Lobes"))
a(Q("C04","K023",1,"Fonctions du lobe <u>temporal</u> ?",
 ["Motricité","Fonctions exécutives","Mémoire","Langage"],"0011","Cours p. 4 : temporal = mémoire, langage.","Lobes"))
a(Q("C05","K022",2,"Fonction principale du <u>cervelet</u> ?",
 ["Coordination du mouvement","Sensibilité","Vision","Mémoire"],"1000","Cours p. 4 : cervelet = coordination du mouvement (équilibre).","Lobes"))
a(Q("C06","K022",2,"Mme B., 58 ans : instabilité brutale à la marche, gestes maladroits et mal coordonnés, force normale. Structure atteinte ?",
 ["Cervelet","Lobe occipital","Lobe pariétal","Lobe temporal"],"1000","Coordination et équilibre = cervelet (p. 4). La force normale écarte une atteinte motrice.","Lobes",vign=True))
a(Q("C07","K020 K028",2,"M. F. ne sent plus le contact sur son bras gauche ; la force est normale. Zone atteinte ?",
 ["Lobe pariétal droit","Lobe pariétal gauche","Lobe frontal droit","Lobe occipital droit"],"1000",
 "Sensibilité = lobe pariétal (p. 4) ; les voies sensitives croisent → déficit controlatéral (p. 5).","Lobes",vign=True))
a(Q("C08","K024",0,"Fonction assurée au niveau du tronc cérébral : vrai ou faux ?",
 ["Mouvements des yeux","Déglutition","Reconnaissance des couleurs","Centres cardiaques et respiratoires"],"1101",
 "Tronc (p. 4) : nerfs crâniens (oculomotricité, face, déglutition, équilibre) et centres végétatifs. La vision consciente relève du cortex occipital.","Tronc cérébral"))
a(Q("C09","K024",2,"Nombre de paires de nerfs crâniens ?",
 ["10","12","14","16"],"0100","Cours p. 4 : 12 paires.","Tronc cérébral"))
a(Q("C10","K025",2,"Étages du tronc cérébral, de haut en bas ?",
 ["Mésencéphale ; protubérance ; bulbe","Bulbe ; protubérance ; mésencéphale","Protubérance ; mésencéphale ; bulbe","Mésencéphale ; bulbe ; protubérance"],"1000","Cours p. 4 : mésencéphale, protubérance, bulbe.","Tronc cérébral",allow=["tronc"]))
a(Q("C11","K026",2,"Trajet de la voie <u>motrice</u> (faisceau pyramidal) ?",
 ["Cortex frontal → capsule interne → tronc → moelle","Cortex pariétal → thalamus → tronc → moelle","Moelle → tronc → capsule interne → cortex frontal","Cortex frontal → thalamus → cervelet → moelle"],"1000",
 "Cours p. 5 : cortex frontal → capsule interne → tronc cérébral → moelle → muscles.","Voies nerveuses"))
a(Q("C12","K027",2,"Lésion de l'hémisphère <u>gauche</u> : côté du déficit moteur ?",
 ["Hémicorps droit","Hémicorps gauche","Les deux hémicorps","La face seule, des deux côtés"],"1000","Cours p. 5 : les voies motrices croisent au bulbe → déficit controlatéral.","Voies nerveuses"))
a(Q("C13","K027",2,"M. G., 71 ans, hémiplégie <u>gauche</u> brutale. Hémisphère probablement atteint ?",
 ["Droit","Gauche","Les deux","Aucun : atteinte du cervelet"],"1000","Déficit controlatéral (p. 5) : hémiplégie gauche → hémisphère droit.","Voies nerveuses",vign=True))
a(Q("C14","K027",2,"Lieu de croisement de la voie <u>motrice</u> ?",
 ["Bulbe","Chiasma optique","Capsule interne","Thalamus"],"1000","Cours p. 5 : croisement (décussation) au niveau du bulbe ; 80 % des fibres croisent.","Voies nerveuses"))
a(Q("C15","K028",0,"Voies <u>sensitives</u> ascendantes : vrai ou faux ?",
 ["Elles remontent de la moelle vers le cortex pariétal","Elles font relais dans le thalamus","Le déficit est du même côté que la lésion","Elles croisent la ligne médiane"],"1101",
 "Cours p. 5 : moelle → cortex pariétal, relais thalamique ; croisement → déficit controlatéral.","Voies nerveuses"))
a(Q("C16","K029",2,"Trajet des voies <u>visuelles</u> ?",
 ["Nerf optique → chiasma → cortex occipital","Nerf optique → thalamus → cortex frontal","Chiasma → nerf optique → cortex pariétal","Nerf optique → chiasma → cortex temporal"],"1000","Cours p. 6 : nerf optique → chiasma (croisement) → cortex occipital.","Voies nerveuses"))
a(Q("C17","K029",2,"Lieu de croisement des voies <u>visuelles</u> ?",
 ["Bulbe","Chiasma optique","Capsule interne","Thalamus"],"0100","Cours p. 6 : croisement au chiasma optique.","Voies nerveuses"))
a(Q("C18","K030",2,"Hémisphère du langage chez un <u>droitier</u> ?",
 ["Gauche","Droit","Les deux à égalité","Variable, une fois sur deux"],"1000","Cours p. 6 : l'hémisphère dominant porte le langage ; gauche chez le droitier.","Langage"))
a(Q("C19","K030",2,"Hémisphère du langage chez la majorité des <u>gauchers</u> ?",
 ["Gauche","Droit","Les deux à égalité","Variable, une fois sur deux"],"1000","Environ 70 % des gauchers ont aussi le langage à gauche.","Langage",x=GAUCHER_X,w=GAUCHER_W))
a(Q("C20","K031",2,"Aire de <u>Broca</u> : localisation ; trouble en cas d'atteinte ?",
 ["Cortex frontal ; aphasie d'expression","Cortex temporal ; aphasie de compréhension","Cortex frontal ; aphasie de compréhension","Cortex temporal ; aphasie d'expression"],"1000","Cours p. 6 : Broca = frontal, expression ; Wernicke = temporal, compréhension.","Langage"))
a(Q("C21","K031",2,"Aire de <u>Wernicke</u> : localisation ; trouble en cas d'atteinte ?",
 ["Cortex frontal ; aphasie d'expression","Cortex temporal ; aphasie de compréhension","Cortex frontal ; aphasie de compréhension","Cortex temporal ; aphasie d'expression"],"0100","Cours p. 6 : Wernicke = temporal, compréhension.","Langage"))
a(Q("C22","K031",2,"M. H. comprend les consignes mais trouve difficilement ses mots et parle peu. Aire atteinte ?",
 ["Aire de Wernicke","Aire de Broca","Cervelet","Cortex occipital"],"0100","Compréhension conservée, expression altérée = aphasie d'expression = aire de Broca (p. 6).","Langage",vign=True))
a(Q("C23","K031",2,"Mme J. parle sans effort mais ses propos sont incohérents et elle ne comprend pas les consignes simples. Aire atteinte ?",
 ["Aire de Broca","Aire de Wernicke","Cervelet","Capsule interne"],"0100","Trouble de la compréhension avec jargon = aphasie de compréhension = aire de Wernicke (p. 6, 9).","Langage",vign=True))
a(Q("C24","K032",0,"Fonctions des hémisphères : vrai ou faux ?",
 ["Le gauche gère le langage et le geste","Une atteinte gauche donne aphasies et apraxies","Le droit gère l'espace et l'attention","Une atteinte droite donne surtout une aphasie"],"1110",
 "Cours p. 7 : une atteinte droite donne un syndrome de l'hémisphère mineur (négligence de la partie gauche).","Fonctions cognitives"))
a(Q("C25","K032",2,"Après un infarctus de l'hémisphère <u>droit</u>, M. K. ne mange que la moitié droite de son assiette et ignore les personnes placées à sa gauche. Trouble ?",
 ["Négligence de l'espace gauche","Hémianopsie latérale droite","Aphasie de compréhension","Apraxie bucco-faciale"],"1000",
 "Cours p. 7 : atteinte droite → difficulté à prendre en compte la partie gauche du corps et de l'espace (syndrome de l'hémisphère mineur).","Fonctions cognitives",vign=True))
a(Q("C26","K033",2,"Les 4 axes artériels du cerveau ?",
 ["2 carotides internes + 2 vertébrales","2 carotides internes + 2 sous-clavières","2 carotides internes + 2 carotides externes","2 vertébrales + 2 cérébrales postérieures"],"1000","Cours p. 7 : 2 carotides (circulation antérieure) + 2 vertébrales (circulation postérieure).","Vascularisation"))
a(Q("C27","K033",2,"Artères de la circulation <u>postérieure</u> ?",
 ["Les 2 vertébrales, réunies en tronc basilaire","Les 2 carotides internes","Les 2 cérébrales antérieures","Les 2 carotides externes"],"1000","Cours p. 7 : circulation postérieure = vertébrales → tronc basilaire.","Vascularisation"))
a(Q("C28","K034",1,"Branches de la carotide <u>interne</u> ?",
 ["Artère ophtalmique","Artère cérébrale postérieure","Artère cérébrale moyenne","Artère cérébrale antérieure"],"1011",
 "Cours p. 7 : ophtalmique, cérébrale moyenne, cérébrale antérieure, choroïdienne antérieure. Les cérébrales postérieures viennent du tronc basilaire.","Vascularisation"))
a(Q("C29","K035",2,"Artères issues du <u>tronc basilaire</u> ?",
 ["Cérébrales antérieures","Cérébrales moyennes","Ophtalmiques","Cérébrales postérieures"],"0001","Cours p. 7 : le tronc basilaire donne les 2 cérébrales postérieures.","Vascularisation"))
a(Q("C30","K035",2,"Branches de l'artère <u>vertébrale</u> ?",
 ["Tronc basilaire et artères cérébelleuses","Artère ophtalmique et cérébrale moyenne","Cérébrale antérieure et communicante antérieure","Choroïdienne antérieure et cérébrale moyenne"],"1000","Cours p. 7 : vertébrale → tronc basilaire, cérébelleuses (PICA).","Vascularisation"))
a(Q("C31","K036",0,"Polygone de Willis : vrai ou faux ?",
 ["Il permet des suppléances en cas d'occlusion","La communicante antérieure relie les deux cérébrales antérieures","Les communicantes postérieures relient circulation antérieure et postérieure","Sa configuration est identique chez tous les individus"],"1110",
 "Cours p. 8 : suppléances hétérogènes et variables selon les individus.","Vascularisation"))
