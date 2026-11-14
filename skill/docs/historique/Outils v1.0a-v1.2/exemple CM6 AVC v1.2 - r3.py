from common import Q
QS = []
a = QS.append

# ---------- UNV et recanalisation ----------
a(Q("G01","K068",2,"Délai maximal de la <u>thrombolyse</u> IV après le début des symptômes ?",
 ["3 heures","4h30","6 heures","9 heures"],"0100","Cours p. 13 : thrombolyse IV si infarctus < 4h30.","Thrombolyse"))
a(Q("G02","K068",2,"Pourquoi ne pas thrombolyser au-delà de ce délai ?",
 ["Le risque hémorragique dépasse le bénéfice","Le caillot s'est dissous spontanément","Le patient est alors trop stable","Le score NIHSS n'est plus fiable"],"1000","Note p. 13 : au-delà, le risque hémorragique augmente.","Thrombolyse",lenok=True))
a(Q("G03","K068 K069",2,"Deux moyens de déboucher l'artère ?",
 ["Thrombolyse IV ; thrombectomie mécanique","Thrombolyse IV ; endartériectomie","Héparine IV ; thrombectomie mécanique","Aspirine IV ; thrombolyse IV"],"1000","Cours p. 13 : thrombolyse IV et thrombectomie mécanique.","Recanalisation"))
a(Q("G04","K068",2,"Mme X., 70 ans, aphasie et hémiplégie droite depuis 1 h. Scanner : pas de sang ; aucune contre-indication. Traitement à envisager en premier ?",
 ["Thrombolyse IV","Aspirine seule","Héparine à dose curative","Surveillance simple"],"1000","< 4h30, pas de sang, pas de CI → thrombolyse IV (± thrombectomie si occlusion proximale).","Thrombolyse",vign=True))
a(Q("G05","K068",2,"M. Y., 64 ans, hémiplégie apparue il y a <u>6 h</u> ; imagerie sans sang. Thrombolyse IV selon le critère du cours ?",
 ["Non : délai dépassé","Oui : délai respecté","Oui, si le NIHSS est élevé","Oui, à demi-dose"],"1000","Cours p. 13 : thrombolyse < 4h30. À 6 h, seule la thrombectomie peut se discuter (jusqu'à 6-24 h).","Thrombolyse",vign=True,lenok=True))
a(Q("G06","K069",2,"Délai maximal de la <u>thrombectomie</u> chez des patients sélectionnés ?",
 ["6 heures","12 heures","24 heures","48 heures"],"0010","Cours p. 15 : jusqu'à 24 h chez des patients sélectionnés.","Thrombectomie"))
a(Q("G07","K069",2,"Qui réalise la thrombectomie ?",
 ["Le neurochirurgien, par craniotomie","Le neuroradiologue interventionnel","Le cardiologue, en salle de coronarographie","L'anesthésiste, au lit du patient"],"0100","Cours p. 13 : neuroradiologue interventionnel, par cathéter.","Thrombectomie",allow=["thrombectomie"]))
a(Q("G08","K070",1,"Indications de la <u>thrombectomie</u> ?",
 ["Occlusion d'une grosse artère proximale","En complément de la thrombolyse","D'emblée si la thrombolyse est contre-indiquée","Occlusion d'une petite artère perforante"],"1110","Cours p. 15 : occlusion proximale (carotide interne, cérébrale moyenne, tronc basilaire) ; sinon l'artère est trop petite.","Thrombectomie"))
a(Q("G09","K070",0,"Thrombectomie : vrai ou faux ?",
 ["Elle se fait le plus vite possible","Tous les centres la pratiquent","Elle retire le caillot par cathéter","Elle est possible jusqu'à 24 h chez des patients sélectionnés"],"1011","Cours p. 15 : tous les centres ne pratiquent pas la thrombectomie.","Thrombectomie",allow=["thrombectomie"]))
a(Q("G10","K071",2,"Lieu et anesthésie de la thrombectomie selon la note de cours ?",
 ["Bloc de radiologie, sans anesthésie générale","Bloc de neurochirurgie, sous anesthésie générale","Au lit en USINV, sans anesthésie générale","Salle de coronarographie, sous anesthésie générale"],"1000","Note de cours p. 15.","Thrombectomie",
 x="Complément : en pratique, sédation légère ou anesthésie générale selon le patient et le centre ; « sans anesthésie générale » n'est pas une règle absolue.",allow=["thrombectomie"]))
a(Q("G11","K072",2,"Infarctus sans thrombolyse ni thrombectomie : traitement ?",
 ["Antiagrégant plaquettaire","Anticoagulant à dose curative","Thrombolyse retardée","Aucun antithrombotique"],"1000","Cours p. 13 : antiagrégant si ni l'un ni l'autre.","Antiagrégation"))
a(Q("G12","K072",2,"Molécule de 1re intention après un infarctus cérébral (hors thrombolyse) ?",
 ["Héparine","Aspirine","Antivitamine K","Paracétamol"],"0100","Cours p. 15 : aspirine = traitement de 1re intention.","Antiagrégation"))
a(Q("G13","K073",2,"Que représente l'hypersignal en <u>diffusion</u> ?",
 ["Du tissu déjà nécrosé","La pénombre récupérable","Une hémorragie","Du tissu sain œdématié"],"1000","Cours p. 14 : hypersignal diffusion = tissu déjà nécrosé.","Pénombre"))
a(Q("G14","K073",2,"Définition de la <u>pénombre</u> ischémique ?",
 ["Zone hypoperfusée, pas encore nécrosée","Zone déjà nécrosée","Zone hémorragique autour de l'infarctus","Zone saine bien vascularisée"],"1000","Cours p. 14 : zone hypoperfusée mais pas nécrosée.","Pénombre"))
a(Q("G15","K073",2,"Objectif du rt-PA / TNK-pa ?",
 ["Sauver la pénombre en reperfusant","Dissoudre un hématome","Réduire l'œdème cérébral","Faire régresser la nécrose"],"1000","Cours p. 14 : sauver la pénombre (recanalisation, reperfusion).","Pénombre"))
a(Q("G16","K074",1,"Contre-indications à la <u>thrombolyse</u> ?",
 ["Sang à l'imagerie cérébrale","Traitement anticoagulant en cours","Âge supérieur à 65 ans","HTA ancienne bien contrôlée"],"1100","Cours p. 14. L'âge et une HTA contrôlée ne sont pas des contre-indications ; il faut une PA < 185/105 au moment du traitement.","Contre-indications"))
a(Q("G17","K074",1,"Contre-indications citées dans le cours et la note ?",
 ["Infarctus massif","Chirurgie récente","Thrombopénie","Anémie sévère"],"1111","Cours p. 14 (diapo et note).","Contre-indications",
 x="⚠ Non confirmé : « anémie sévère » ne figure pas dans les contre-indications classiques retrouvées (sang à l'imagerie, plaquettes < 100 000, anticoagulant efficace, chirurgie majeure récente, PA non contrôlée, glycémie extrême). Gardé tel qu'écrit dans la note.",
 w=["Web — GPnotebook, Thrombolyse dans les AVC ischémiques, https://gpnotebook.com/fr/pages/neurologie/thrombolyse-dans-les-accidents-vasculaires-cerebraux-ischemiques"]))
a(Q("G18","K075",2,"Administration du <u>rt-PA</u> (altéplase) ?",
 ["0,9 mg/kg (max 90 mg) : 10 % en bolus, le reste sur 1 h","0,9 mg/kg (max 90 mg) : tout en bolus unique","0,25 mg/kg : 10 % en bolus, le reste sur 1 h","0,25 mg/kg (max 25 mg) : tout en bolus unique"],"1000","Cours p. 14 : rt-PA 0,9 mg/kg, max 90 mg, 10 % bolus, SE sur 1 h. TNK-pa : bolus unique 0,25 mg/kg.","Doses"))
a(Q("G19","K075",2,"Administration du <u>TNK-pa</u> (ténectéplase) ?",
 ["0,9 mg/kg (max 90 mg) : 10 % en bolus, le reste sur 1 h","0,9 mg/kg (max 90 mg) : tout en bolus unique","0,25 mg/kg : 10 % en bolus, le reste sur 1 h","0,25 mg/kg : tout en bolus unique"],"0001","Cours p. 14 : TNK-pa = bolus IV unique de 0,25 mg/kg.","Doses"))
a(Q("G20","K076",0,"Pendant la thrombolyse : vrai ou faux ?",
 ["Surveillance neurologique","Surveillance de la TA","Arrêt de la perfusion si complication","Poursuite de la perfusion quoi qu'il arrive"],"1110","Cours p. 14 : surveillance neuro et TA +++ ; arrêt de la SE si complication.","Surveillance",
 dz={3:"en cas d'hémorragie ou d'allergie, la perfusion doit être arrêtée"},allow=["thrombolyse"]))
a(Q("G21","K076",2,"Pendant la perfusion de rt-PA, Mme Z. présente un gonflement de la langue et des lèvres. Première action ?",
 ["Arrêter la perfusion et alerter le médecin","Poursuivre la perfusion et surveiller","Diminuer le débit de moitié","Terminer la perfusion puis alerter"],"1000","Cours p. 14 : arrêt de la SE si complication, dont l'allergie (œdème oro-lingual, 1 %).","Surveillance",
 dz={1:"l'œdème oro-lingual peut obstruer les voies aériennes",3:"retard à l'arrêt d'un produit responsable d'une allergie grave"},vign=True))
a(Q("G22","K076",2,"Qui donne le feu vert à la thrombolyse ?",
 ["Un médecin expert en neurovasculaire","L'infirmier d'accueil","Le radiologue seul","Le médecin traitant"],"1000","Cours p. 14 : feu vert d'un médecin avec expertise neurovasculaire.","Décision",allow=["thrombolyse"]))
a(Q("G23","K077",2,"Seuil de PA à respecter pour la <u>thrombolyse</u> (cours) ?",
 ["< 160/90 mmHg","< 185/105 mmHg","< 200/110 mmHg","< 220/120 mmHg"],"0100","Cours p. 14 : < 185/105. 220/120 = seuil de traitement hors thrombolyse.","Pression artérielle"))
a(Q("G24","K078",2,"Antithrombotiques après une thrombolyse ?",
 ["Aucun pendant 24 h, puis aspirine après scanner","Aspirine dès la fin de la perfusion","Héparine curative dès la fin de la perfusion","Aucun pendant 7 jours, puis aspirine"],"1000","Cours p. 14-15 : aucun antithrombotique 24 h ; aspirine à H24 après TDM.","Après thrombolyse"))
a(Q("G25","K078",2,"Examen à faire avant l'aspirine de H24 ?",
 ["Scanner cérébral de contrôle","ECG","NFS","EEG"],"1000","Cours p. 15 : TDM pour éliminer une complication hémorragique.","Après thrombolyse"))
a(Q("G26","K066",0,"Soins intensifs neurovasculaires (USINV) : vrai ou faux ?",
 ["Monitoring cardio-respiratoire","Surveillance rapprochée à la phase aiguë","Prévention des complications","Réservés aux formes hémorragiques"],"1110","Cours p. 13 : lits de soins intensifs pour la phase aiguë de tous les patients.","Soins intensifs"))
a(Q("G27","K067",2,"Fréquence de l'aggravation précoce ?",
 ["≈ 10 %","≈ 20 %","≈ 30 %","≈ 40 %"],"0010","Cours p. 13 : 30 % d'aggravation précoce.","Soins intensifs"))
a(Q("G28","K079",0,"Équipe pluridisciplinaire : vrai ou faux ?",
 ["La rééducation débute dès le départ","L'équipe comprend un orthophoniste","La prise en charge est aussi sociale","La kinésithérapie n'intervient qu'en SSR"],"1110","Cours p. 15 : kinésithérapie dès le départ en UNV.","Équipe"))
a(Q("G29","K080",2,"Prévention des complications : réduction de la mortalité et du <u>handicap</u> (diapo) ?",
 ["10 %","20 %","30 %","40 %"],"0010","Diapo p. 15 : −30 % de mortalité et handicap. (Note p. 11 : −20 % de mortalité seule.)","Équipe"))

# ---------- Surveillance et complications ----------
a(Q("H01","K081",1,"Situations à éviter à la phase aiguë ?",
 ["Hypotension","Hypoxie","Hyperthermie","Hypertension modérée"],"1110","Cours p. 16 : éviter hypotension, hypoxie, hyperglycémie, hyperthermie. Une HTA modérée est tolérée.","Constantes"))
a(Q("H02","K081",0,"Paramètre surveillé : vrai ou faux ?",
 ["FC, PA et SaO2 sous scope","Température","Glycémie capillaire","Pression intracrânienne par capteur"],"1110","Cours p. 16 : scope, température, HGT. Pas de capteur de pression intracrânienne.","Constantes"))
a(Q("H03","K081 K088 K090",1,"M. Z., J1 d'un infarctus cérébral : T 37,8 °C ; glycémie 2,2 g/L ; PA 175/95 ; SpO2 96 %. Paramètres à corriger ?",
 ["Température","Glycémie","Pression artérielle","Saturation"],"1100",
 "Cours p. 16-17 : paracétamol dès 37,5 °C ; éviter l'hyperglycémie (insuline adaptée) ; PA tolérée jusqu'à 220/120 ; O2 seulement si SatO2 < 92 %.","Constantes",vign=True))
a(Q("H04","K082",2,"Scores de la surveillance neurologique ?",
 ["NIHSS et Glasgow","Glasgow et APGAR","NIHSS et Norton","EVA et Braden"],"1000","Cours p. 16 : NIHSS et Glasgow.","Surveillance neurologique"))
a(Q("H05","K083",1,"Lesquelles sont des complications <u>neurologiques</u> ?",
 ["Crise d'épilepsie","Transformation hémorragique","Escarres","Embolie pulmonaire"],"1100","Cours p. 16 : escarres et embolie pulmonaire sont des complications générales.","Complications"))
a(Q("H06","K083",0,"Complication <u>neurologique</u> : vrai ou faux ?",
 ["Hydrocéphalie","Démence","Algoneurodystrophie","Récidive ischémique"],"1101","Cours p. 16 : l'algoneurodystrophie est une complication générale.","Complications"))
a(Q("H07","K084",2,"Fréquence des crises d'<u>épilepsie</u> ?",
 ["1-5 %","10-40 %","40-60 %","60-80 %"],"0100","Cours p. 16 : épilepsie 10-40 % ; œdème 10-20 %.","Complications"))
a(Q("H08","K084",2,"Fréquence de l'<u>œdème</u> cérébral ?",
 ["1-5 %","10-20 %","25-35 %","40-50 %"],"0100","Cours p. 16 : œdème 10-20 %.","Complications"))
a(Q("H09","K084 K086",2,"Part des décès due à chaque type de complication ?",
 ["Neurologiques 60 % ; générales 40 %","Neurologiques 40 % ; générales 60 %","Neurologiques 50 % ; générales 50 %","Neurologiques 70 % ; générales 30 %"],"0010","Cours p. 16 : 50 % / 50 %.","Complications"))
a(Q("H10","K085",1,"Lesquelles sont des complications <u>générales</u> ?",
 ["Pneumopathie d'inhalation","Thrombose veineuse profonde","Hydrocéphalie","Transformation hémorragique"],"1100","Cours p. 16 : hydrocéphalie et transformation hémorragique sont neurologiques.","Complications"))
a(Q("H11","K085",0,"Complication <u>générale</u> : vrai ou faux ?",
 ["Rétention urinaire","Dénutrition","Épilepsie","Escarres"],"1101","Cours p. 16 : l'épilepsie est neurologique.","Complications"))
a(Q("H12","K085",1,"Complications générales décrites (cœur, locomotion, humeur) ?",
 ["Infarctus du myocarde, arythmie","Spasticité, rétractions","Algoneurodystrophie","Dépression"],"1111","Cours p. 16 : toutes font partie des complications générales.","Complications"))
a(Q("H13","K087",2,"Rythme de surveillance de la PA ?",
 ["/1 h jusqu'à H24, puis /2 h pendant 24 h, puis /4 h","/2 h jusqu'à H24, puis /4 h pendant 24 h, puis /6 h","/1 h jusqu'à H48, puis /4 h","/4 h dès l'admission"],"1000","Cours p. 17.","Pression artérielle"))
a(Q("H14","K087",2,"PA élevée : que faire avant toute décision ?",
 ["Recontrôler par une 2e mesure à 10 min","Traiter immédiatement","Faire un ECG","Asseoir le patient"],"1000","Cours p. 17 : 2e mesure systématique à 10 min.","Pression artérielle",lenok=True))
a(Q("H15","K088",2,"Seuil de traitement de la PA <u>hors thrombolyse</u> ?",
 ["> 140/90 mmHg","> 160/100 mmHg","> 185/105 mmHg","PAS > 220 ou PAD > 120 mmHg"],"0001","Cours p. 17 : ne traiter que si PAS > 220 ou PAD > 120. 185/105 = seuil en cas de thrombolyse.","Pression artérielle",lenok=True))
a(Q("H16","K088",2,"Pourquoi tolérer une HTA à la phase aiguë d'un infarctus ?",
 ["Elle maintient le débit sanguin cérébral","Elle prévient les crises d'épilepsie","Elle diminue le risque hémorragique","Elle facilite la thrombectomie"],"1000","Cours p. 17 : HTA = adaptation pour maintenir le DSC.","Pression artérielle"))
a(Q("H17","K088",2,"Mme A., infarctus sans thrombolyse : PA 190/100 confirmée à 10 min, pas de globe ni de douleur. Conduite ?",
 ["Ne pas traiter, poursuivre la surveillance","Traiter pour viser 120/80 mmHg","Traiter pour viser moins de 140/90 mmHg","Traiter car supérieure à 185/105 mmHg"],"1000",
 "Cours p. 17 : traiter seulement si > 220/120 (hors thrombolyse) ; préférer l'HTA à l'hypotension.","Pression artérielle",
 dz={1:"une baisse brutale de la PA aggrave l'ischémie"},vign=True))
a(Q("H18","K089",2,"Facteurs qui font monter la PA, à rechercher ?",
 ["Globe vésical ; douleur","Anémie ; hypokaliémie","Déshydratation ; hyponatrémie","Hypothermie ; hypoglycémie"],"1000","Cours p. 17.","Pression artérielle"))
a(Q("H19","K089 K098",2,"M. B., agité et hypertendu, n'a pas uriné depuis 6 h. Premier geste ?",
 ["Bladder-scan à la recherche d'un globe","Antihypertenseur IV","Sédation","Sonde à demeure sans évaluation"],"1000","Cours p. 17-18 : le globe fait monter la PA ; pas de sondage systématique, le dépister au bladder-scan.","Pression artérielle",vign=True))
a(Q("H20","K090",2,"Température à partir de laquelle on traite par paracétamol ?",
 ["37 °C","37,5 °C","38 °C","38,5 °C"],"0100","Cours p. 17 : dès 37,5 °C.","Hyperthermie"))
a(Q("H21","K090",0,"<u>Hyperthermie</u> à la phase aiguë : vrai ou faux ?",
 ["Elle aggrave le pronostic","Elle concerne environ 30 % des patients","Il faut en rechercher la cause","On attend 39 °C pour la traiter"],"1110","Cours p. 17 : paracétamol dès 37,5 °C.","Hyperthermie"))
a(Q("H22","K091",2,"Soluté de perfusion d'un patient hyperglycémique ?",
 ["Sérum glucosé à 5 %","Sérum glucosé à 10 %","Sérum physiologique","Sérum glucosé à 30 %"],"0010","Cours p. 17 : sérum physiologique, jamais glucosé.","Glycémie",
 dz={0:"le sérum glucosé aggrave l'hyperglycémie, délétère pour le cerveau ischémié",1:"idem",3:"idem"}))
a(Q("H23","K091",0,"<u>Hyperglycémie</u> à la phase aiguë : vrai ou faux ?",
 ["HGT toutes les heures, puis toutes les 4 h","Insuline rapide adaptée au dextro","Traitement des hypoglycémies","Apport de sérum glucosé"],"1110","Cours p. 17 : jamais de sérum glucosé.","Glycémie",dz={3:"aggrave l'hyperglycémie"}))
a(Q("H24","K092",2,"Position au lit à la phase aiguë d'un infarctus ?",
 ["Repos strict, tête entre 0 et 30°","Assis à 90°","Trendelenburg","Au fauteuil dès l'admission"],"1000","Cours p. 17 : repos strict au lit (0-30°), puis position adaptée.","Installation"))
a(Q("H25","K092",2,"M. C. a une carotide occluse. On l'assoit rapidement au bord du lit. Risque principal ?",
 ["Chute de PA, hypoperfusion et aggravation","Hémorragie méningée","Poussée hypertensive","Embolie pulmonaire"],"1000","Cours p. 17 : relever trop vite → hypotension, aggravation.","Installation",vign=True))
a(Q("H26","K093",2,"Seuil de SpO2 en dessous duquel on donne de l'oxygène ?",
 ["90 %","92 %","94 %","95 %"],"0100","Cours p. 17 : O2 si SatO2 < 92 %.","Voies aériennes"))
a(Q("H27","K093",1,"Liberté des voies aériennes et lutte contre l'hypoxie ?",
 ["Aspiration des sécrétions si besoin","Oxygène si SatO2 < 92 %","Intubation en première intention","Oxygène même si la saturation est normale"],"1100","Cours p. 17 : l'intubation est très rarement discutée.","Voies aériennes"))
a(Q("H28","K094",2,"Alimentation à l'admission ?",
 ["À jeun jusqu'au dépistage des troubles de déglutition","Alimentation normale dès que le patient a faim","Eau gélifiée sans évaluation préalable","Sonde nasogastrique pour tous"],"1000","Cours p. 17 : à jeun jusqu'au dépistage.","Déglutition",
 dz={1:"risque de fausse route et de pneumopathie d'inhalation",2:"idem : aucune prise orale avant le dépistage"}))
a(Q("H29","K094",0,"Facteur favorisant les troubles de déglutition : vrai ou faux ?",
 ["Déficit moteur ou sensitif","Trouble de la praxie bucco-faciale","Hémianopsie latérale homonyme","Troubles de la vigilance"],"1101","Cours p. 17. L'hémianopsie est un trouble visuel.","Déglutition"))
a(Q("H30","K094",1,"Troubles de déglutition avérés : adaptations ?",
 ["Texture adaptée","Sonde nasogastrique si nécessaire","Alimentation normale sous surveillance","Eau plate par petites gorgées"],"1100","Cours p. 17 : texture adaptée, SNG si besoin, équilibre nutritionnel.","Déglutition",
 dz={2:"fausse route",3:"les liquides fins sont les plus à risque de fausse route"}))
a(Q("H31","K094",2,"Mme D., admise il y a 2 h, a soif. Le dépistage de la déglutition n'est pas fait. Que faites-vous ?",
 ["La laisser à jeun jusqu'au dépistage","Lui donner de l'eau gélifiée","Lui donner un verre d'eau assise","Lui proposer une compote"],"1000","Cours p. 17 : à jeun jusqu'au dépistage des troubles de la déglutition.","Déglutition",
 dz={1:"aucune prise orale avant le dépistage",2:"fausse route, pneumopathie d'inhalation",3:"aucune prise orale avant le dépistage"},vign=True))
a(Q("H32","K095",2,"Hydratation et surveillance associée ?",
 ["Sérum physiologique ; ionogramme et diurèse","Sérum glucosé ; glycémie","Restriction hydrique ; poids","Hydratation orale libre ; aucune"],"1000","Cours p. 17.","Hydratation",lenok=True))
a(Q("H33","K096",0,"Prévention des thromboses veineuses : vrai ou faux ?",
 ["HBPM préventive","Mobilisation","Bas de contention sur prescription","Anticoagulation à dose curative"],"1110","Cours p. 18.","Prévention"))
a(Q("H34","K097",1,"Prévention des escarres ?",
 ["Matelas anti-escarres","Changements de position","Immobilisation stricte prolongée","Sonde urinaire à demeure"],"1100","Cours p. 18 : matelas, nursing, changements de position.","Prévention"))
a(Q("H35","K097",2,"Prévention des rétractions et luxations ?",
 ["Kinésithérapie et mobilisation","Immobilisation du membre","Antalgiques seuls","Attelle permanente"],"1000","Cours p. 18.","Prévention"))
a(Q("H36","K098",2,"Surveillance de la diurèse ?",
 ["Dépister un globe au bladder-scan","Sonde à demeure dès l'admission","Sondage évacuateur toutes les 6 h","Étui pénien pour tous"],"1000","Cours p. 18 : pas de sondage systématique, dépister un globe.","Diurèse"))
a(Q("H37","K099",0,"Mobilisation et rééducation : vrai ou faux ?",
 ["Fauteuil dès que l'hémodynamique le permet","Kinésithérapie passive et active","Orthophonie (déglutition, langage)","Repos au lit jusqu'à la sortie"],"1110","Cours p. 18 : mobilisation précoce.","Rééducation"))
a(Q("H38","K099",2,"Céphalées pendant l'hospitalisation : conduite (cours) ?",
 ["Antalgique","Ne rien donner pour ne pas masquer","Morphine d'emblée","Arrêt de toute mobilisation"],"1000","Cours p. 18 : lutte contre la douleur (antalgiques).","Douleur",lenok=True))
a(Q("H39","K100",0,"Intervenant : vrai ou faux ?",
 ["L'assistante sociale prépare le 100 % et les soins de suite","Le psychologue accompagne patient et famille","Un tabacologue intervient si besoin","Le diététicien ne voit que les diabétiques"],"1110","Cours p. 18 : diététicienne pour tous (dénutrition, déglutition).","Équipe"))
a(Q("H40","K101",2,"Tableau d'un infarctus sylvien <u>droit</u> ?",
 ["Hémiplégie gauche avec négligence","Hémiplégie droite avec aphasie","Hémiplégie gauche avec aphasie","Hémiplégie droite avec négligence"],"1000","Atteinte droite → déficit gauche + négligence (p. 7, 18).","Installation"))
a(Q("H41","K101",2,"Hémiplégie gauche avec négligence : où placer la sonnette ?",
 ["À droite","À gauche","Au pied du lit","Au choix du patient"],"1000","Cours p. 18 : sonnette, urinoir, téléphone du côté sain (droit).","Installation"))
a(Q("H42","K101",0,"Installation d'une patiente avec hémiplégie gauche et négligence : vrai ou faux ?",
 ["Urinoir et sonnette à droite","Photos et objets personnels à gauche","Repas présentés par l'équipe","L'entourage se place à droite"],"1110","Cours p. 18 : entourage et équipe aussi à gauche, pour stimuler le côté négligé.","Installation",vign=True))
a(Q("H43","K102",2,"Positionnement et alimentation : comment sont-ils décidés ?",
 ["Chaque jour, de façon collégiale","Une fois à l'admission","Par le médecin seul","Par la famille"],"1000","Cours p. 18.","Installation"))
