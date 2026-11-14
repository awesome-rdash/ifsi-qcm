from common import Q
QS = []
a = QS.append

# ---------- G. UNV et recanalisation ----------
a(Q("G01","K068",2,"Thrombolyse IV — <b>délai maximal</b> après le début des symptômes ?",
 ["1 heure","4h30","6 heures","24 heures"],"0100","Thrombolyse IV (rt-PA/TNK-pa) : infarctus < 4h30.","Thrombolyse"))
a(Q("G02","K068",2,"Thrombolyse IV — <b>pourquoi pas au-delà du délai</b> ?",
 ["Le caillot est déjà dissous spontanément","Le produit devient inactif","La thrombectomie devient contre-indiquée","Le risque hémorragique l'emporte sur le bénéfice"],"0001","Au-delà de 4h30, le risque hémorragique augmente et dépasse le bénéfice.","Thrombolyse"))
a(Q("G03","K068 K069",2,"Infarctus cérébral — <b>2 moyens de déboucher l'artère</b> ?",
 ["Héparine IV ; aspirine","Thrombolyse IV ; thrombectomie mécanique","Thrombolyse IV ; endartériectomie","Craniectomie ; thrombectomie mécanique"],"0100","Recanalisation : thrombolyse IV (< 4h30) et thrombectomie mécanique (jusqu'à 6-24 h).","Recanalisation"))
a(Q("G04","K068",2,"Femme de 70 ans, aphasie et hémiplégie droite depuis 1 h ; scanner : pas de sang ; aucune contre-indication. <b>Traitement de reperfusion</b> à envisager en premier ?",
 ["Thrombolyse IV","Aspirine seule","Héparine à dose curative","Abstention et surveillance"],"1000","< 4h30, pas de sang, pas de CI → thrombolyse IV (± thrombectomie si occlusion proximale).","Thrombolyse"))
a(Q("G05","K069",2,"Thrombectomie mécanique — <b>délai maximal</b> chez des patients sélectionnés ?",
 ["4h30","1 heure","24 heures","72 heures"],"0010","Thrombectomie : jusqu'à 6-24 h après le début des symptômes chez des patients sélectionnés.","Thrombectomie"))
a(Q("G06","K069",2,"Thrombectomie mécanique — <b>qui la réalise</b> ?",
 ["Neurochirurgien par craniotomie","Neuroradiologue interventionnel","Cardiologue en salle de coronarographie","Anesthésiste-réanimateur au lit"],"0100","Neuroradiologie interventionnelle : cathéter jusqu'au caillot, aspiration ou stent.","Thrombectomie"))
a(Q("G07","K070",1,"Thrombectomie — <b>indications</b> ?",
 ["Occlusion proximale (carotide interne, cérébrale moyenne, tronc basilaire)","En complément de la thrombolyse quand elle est indiquée","D'emblée en cas de contre-indication à la thrombolyse","Occlusion d'une petite artère distale (lacune)"],"1110","Il faut une grosse artère bouchée (occlusion proximale) ; sinon trop petit.","Thrombectomie"))
a(Q("G08","K070",0,"Thrombectomie mécanique",
 ["Elle est réalisée le plus rapidement possible dès que l'indication est posée","Tous les centres de neurologie la pratiquent","Elle consiste à retirer le caillot par cathéter (aspiration ou stent)","Elle est efficace jusqu'à 24 h chez des patients sélectionnés"],"1011","2. Faux : tous les centres ne font pas de thrombectomie.","Thrombectomie"))
a(Q("G09","K071",2,"Thrombectomie — <b>lieu et anesthésie</b> selon la note de cours ?",
 ["Bloc de neurochirurgie, sous anesthésie générale","Au lit en USINV, sans anesthésie","Bloc de radiologie, sans anesthésie générale","Salle de coronarographie, sous anesthésie générale"],"0010",
 "Note de cours : au bloc de radiologie, sans anesthésie générale.","Thrombectomie",
 x="Complément : en pratique, la thrombectomie se fait sous sédation légère ou sous anesthésie générale selon le patient et le centre ; « sans anesthésie générale » n'est pas une règle absolue."))
a(Q("G10","K072",2,"Infarctus cérébral sans thrombolyse ni thrombectomie — <b>traitement</b> ?",
 ["Anticoagulant à dose curative d'emblée","Thrombolyse retardée","Antiagrégant plaquettaire","Aucun traitement antithrombotique"],"0010","Si aucun des deux : antiagrégant plaquettaire.","Antiagrégation"))
a(Q("G11","K072",2,"Après un infarctus cérébral (hors thrombolyse) — <b>molécule de 1re intention</b> ?",
 ["Héparine","Aspirine","Antivitamine K","Paracétamol"],"0100","Traitement de 1re intention après un AVC ischémique (et à H24 d'une thrombolyse) : aspirine.","Antiagrégation"))
a(Q("G12","K073",2,"IRM de diffusion — <b>l'hypersignal correspond à</b> ?",
 ["Du tissu déjà nécrosé","La zone de pénombre récupérable","Une hémorragie","Du tissu sain œdématié"],"1000","Hypersignal en diffusion : tissu déjà nécrosé (trop tard pour lui).","Pénombre"))
a(Q("G13","K073",2,"<b>Pénombre ischémique</b> — définition ?",
 ["Zone déjà nécrosée","Zone hypoperfusée mais pas encore nécrosée, encore sauvable","Zone hémorragique autour de l'infarctus","Zone saine bien vascularisée"],"0100","Pénombre : hypoperfusée mais pas nécrosée.","Pénombre"))
a(Q("G14","K073",2,"rt-PA / TNK-pa — <b>objectif</b> ?",
 ["Dissoudre un hématome","Réduire l'œdème cérébral","Faire régresser la nécrose","Sauver la pénombre par recanalisation et reperfusion"],"0001","Objectif : sauver la pénombre (recanalisation, reperfusion).","Pénombre"))
a(Q("G15","K074",1,"Thrombolyse — <b>contre-indications</b> citées ?",
 ["Sang à l'imagerie cérébrale","Infarctus massif","Traitement anticoagulant en cours","Âge supérieur à 65 ans"],"1110","Bénéfice >> risque seulement si respect des CI. L'âge > 65 ans n'est pas une CI.","Contre-indications"))
a(Q("G16","K074",1,"Thrombolyse — autres <b>contre-indications</b> citées dans la note de cours ?",
 ["Chirurgie récente","Thrombopénie","Anémie sévère","HTA ancienne bien contrôlée"],"1110","Une HTA ancienne contrôlée n'est pas une CI ; il faut seulement une PA < 185/105 au moment du traitement.","Contre-indications",
 x="⚠ Non confirmé : « anémie sévère » ne figure pas dans les contre-indications classiques retrouvées (sang à l'imagerie, plaquettes < 100 000, anticoagulant efficace, chirurgie majeure récente, PA non contrôlée, glycémie extrême). Gardé tel qu'écrit dans la note.",
 w=["Web — GPnotebook, Thrombolyse dans les AVC ischémiques, https://gpnotebook.com/fr/pages/neurologie/thrombolyse-dans-les-accidents-vasculaires-cerebraux-ischemiques"]))
a(Q("G17","K075",2,"rt-PA IV (altéplase) — <b>modalités d'administration</b> ?",
 ["0,25 mg/kg en bolus unique","0,9 mg/kg (max 90 mg) en bolus unique","9 mg/kg sur 24 h","0,9 mg/kg (max 90 mg) : 10 % en bolus puis le reste sur 1 h"],"0001","rt-PA : 0,9 mg/kg, max 90 mg, 10 % en bolus, seringue électrique sur 1 h. 0,25 mg/kg en bolus = TNK-pa.","Doses"))
a(Q("G18","K075",2,"TNK-pa IV (ténectéplase) — <b>modalités d'administration</b> ?",
 ["Bolus unique de 0,25 mg/kg","0,9 mg/kg sur 1 h","Perfusion continue sur 24 h","Bolus de 90 mg quel que soit le poids"],"1000","TNK-pa : bolus IV unique de 0,25 mg/kg.","Doses"))
a(Q("G19","K076",1,"Pendant une thrombolyse — <b>surveillance et conduite</b> ?",
 ["Surveillance neurologique","Surveillance de la TA +++","Arrêt de la perfusion si suspicion de complication","Poursuite de la perfusion quoi qu'il arrive"],"1110","Surveillance neuro et générale (TA +++) ; arrêt de la SE si complication.","Surveillance thrombolyse"))
a(Q("G20","K076",1,"Thrombolyse — <b>complications imposant l'arrêt</b> ?",
 ["Hémorragie cérébrale","Hémorragie systémique","Œdème oro-lingual (allergie)","Bradycardie sinusale isolée asymptomatique"],"1110","Arrêt si hémorragie cérébrale, hémorragie systémique, allergie (œdème oro-lingual, 1 %).","Surveillance thrombolyse"))
a(Q("G21","K076",2,"Thrombolyse — <b>qui donne le feu vert</b> ?",
 ["L'infirmier d'accueil","Le radiologue seul","Un médecin ayant une expertise neurovasculaire","Le médecin traitant"],"0010","Feu vert par un médecin avec expertise en neurovasculaire.","Surveillance thrombolyse"))
a(Q("G22","K077",2,"Thrombolyse — <b>seuil de PA</b> à respecter (cours) ?",
 ["< 185/105 mmHg","< 140/90 mmHg","< 220/120 mmHg","< 120/80 mmHg"],"1000","Contrôle de l'HTA < 185/105 mmHg. 220/120 = seuil de traitement hors thrombolyse.","PA et thrombolyse"))
a(Q("G23","K078",2,"Après une thrombolyse — <b>antithrombotiques</b> ?",
 ["Aspirine immédiatement après la perfusion","Héparine curative immédiate","Aucun pendant 24 h, puis aspirine à H24 après un scanner de contrôle","Aucun pendant 7 jours"],"0010","Pas d'antithrombotique dans les 24 premières heures ; aspirine à H24 après TDM.","Après thrombolyse"))
a(Q("G24","K078",2,"Aspirine à H24 d'une thrombolyse — <b>examen préalable</b> ?",
 ["Scanner cérébral de contrôle","ECG","NFS","EEG"],"1000","TDM cérébral pour éliminer une complication hémorragique avant l'aspirine.","Après thrombolyse"))
a(Q("G25","K066",1,"USINV (soins intensifs neurovasculaires) — <b>caractéristiques</b> ?",
 ["Monitoring cardio-respiratoire","Surveillance régulière à la phase aiguë","Prévention des complications","Réservée aux AVC hémorragiques"],"1110","Lits de soins intensifs pour tous les AVC à la phase aiguë.","USINV"))
a(Q("G26","K067",2,"AVC à la phase aiguë — <b>fréquence de l'aggravation précoce</b> ?",
 ["≈ 3 %","≈ 30 %","≈ 60 %","≈ 90 %"],"0100","30 % d'aggravation précoce : d'où la surveillance en USINV.","USINV"))
a(Q("G27","K079",0,"Hospitalisation en UNV — équipe",
 ["La rééducation débute dès le départ","L'équipe comprend un orthophoniste","La prise en charge est aussi sociale et psychologique","La kinésithérapie n'intervient qu'en SSR"],"1110","4. Faux : kinésithérapie en UNV dès le départ.","Équipe"))
a(Q("G28","K080",2,"UNV — <b>réduction de la mortalité et du handicap</b> grâce à la prévention, au diagnostic et au traitement des complications (diapo) ?",
 ["5 %","15 %","30 %","60 %"],"0010","Diapo p. 15 : −30 % de mortalité et handicap. (Note p. 11 : −20 % de mortalité, autre critère.)","Équipe"))

# ---------- H. Surveillance et complications ----------
a(Q("H01","K081",1,"AVC à la phase aiguë — <b>situations à éviter</b> grâce à la surveillance ?",
 ["Hypotension","Hypoxie","Hyperthermie","Hypertension modérée"],"1110","À éviter : hypotension, hypoxie, hyperglycémie, hyperthermie. Une HTA modérée est tolérée.","Surveillance"))
a(Q("H02","K081",0,"Surveillance en UNV",
 ["FC, PA et SaO2 sous scope","Température","Glycémie capillaire (HGT)","Pression intracrânienne par capteur chez tous"],"1110","4. Faux : pas de capteur de PIC systématique.","Surveillance"))
a(Q("H03","K082",2,"Surveillance neurologique en UNV — <b>scores utilisés</b> ?",
 ["Glasgow et APGAR","NIHSS et Glasgow","NIHSS et Norton","EVA et Braden"],"0100","Surveillance neurologique : NIHSS et Glasgow.","Surveillance"))
a(Q("H04","K083",1,"Complications <b>neurologiques</b> post-AVC ?",
 ["Crise d'épilepsie","Transformation hémorragique","Œdème cérébral avec HTIC","Escarres"],"1110","Les escarres sont une complication générale.","Complications"))
a(Q("H05","K083",1,"Autres complications <b>neurologiques</b> post-AVC ?",
 ["Récidive ischémique","Hydrocéphalie","Démence","Embolie pulmonaire"],"1110","L'embolie pulmonaire est une complication générale.","Complications"))
a(Q("H06","K084",2,"Crises d'épilepsie post-AVC — <b>fréquence</b> (cours) ?",
 ["< 1 %","10-40 %","60-80 %","Constante"],"0100","Épilepsie : 10-40 % ; œdème cérébral : 10-20 %.","Complications"))
a(Q("H07","K084",2,"Œdème cérébral post-AVC — <b>fréquence</b> (cours) ?",
 ["1-2 %","10-20 %","40-60 %","80-90 %"],"0100","Œdème cérébral : 10-20 %.","Complications"))
a(Q("H08","K084 K086",2,"Décès après AVC — <b>part des complications neurologiques et générales</b> ?",
 ["Neurologiques 90 % ; générales 10 %","Neurologiques 10 % ; générales 90 %","Neurologiques 50 % ; générales 50 %","Neurologiques 30 % ; générales 20 %"],"0010","Complications neurologiques : 50 % des décès ; générales : 50 % des décès.","Complications"))
a(Q("H09","K085",1,"Complications <b>générales</b> post-AVC ?",
 ["Troubles de la déglutition, pneumopathie","Thrombose veineuse, embolie pulmonaire","Escarres","Hydrocéphalie"],"1110","L'hydrocéphalie est neurologique.","Complications"))
a(Q("H10","K085",1,"Autres complications <b>générales</b> post-AVC ?",
 ["Infection et rétention urinaire","Déshydratation, dénutrition","Dépression","Transformation hémorragique"],"1110","La transformation hémorragique est neurologique.","Complications"))
a(Q("H11","K085",1,"Complications <b>générales</b> post-AVC (suite et fin) ?",
 ["Rétractions tendineuses, spasticité","Algoneurodystrophie","Infarctus du myocarde, arythmie","Crise d'épilepsie"],"1110","L'épilepsie est neurologique.","Complications"))
a(Q("H12","K087",2,"AVC — <b>rythme de surveillance de la PA</b> ?",
 ["Toutes les heures jusqu'à H24, puis toutes les 2 h pendant 24 h, puis toutes les 4 h","Toutes les 4 h dès l'admission","Toutes les 15 min pendant 7 jours","Une fois par équipe (toutes les 8 h)"],"1000","Surveillance horaire jusqu'à H24, puis /2 h pendant 24 h, puis /4 h.","Pression artérielle"))
a(Q("H13","K087",2,"PA élevée chez un patient AVC — <b>avant toute décision</b> ?",
 ["Traiter immédiatement","Faire un ECG","Recontrôler : 2e mesure systématique à 10 min","Asseoir le patient"],"0010","Vérifier la TA : 2e mesure systématique à 10 min.","Pression artérielle"))
a(Q("H14","K088",2,"AVC ischémique (hors thrombolyse) — <b>seuil de traitement de la PA</b> ?",
 ["> 140/90 mmHg","> 185/105 mmHg","> 160/100 mmHg","PAS > 220 ou PAD > 120 mmHg"],"0001","Ne traiter que si PAS > 220 ou PAD > 120. 185/105 = seuil en cas de thrombolyse.","Pression artérielle"))
a(Q("H15","K088",2,"AVC ischémique — <b>pourquoi tolère-t-on une HTA</b> ?",
 ["Elle prévient les crises d'épilepsie","Elle maintient le débit sanguin cérébral","Elle diminue le risque hémorragique","Elle facilite la thrombectomie"],"0100","HTA fréquente = adaptation pour maintenir le débit sanguin cérébral (DSC).","Pression artérielle"))
a(Q("H16","K088",0,"PA après un AVC ischémique",
 ["On préfère une hypertension à une hypotension","Il faut se méfier des hypotensions","On normalise rapidement la PA à 120/80 mmHg","Les seuils sont différents en cas de thrombolyse"],"1101","3. Faux : abaisser la PA aggraverait l'ischémie.","Pression artérielle"))
a(Q("H17","K089",2,"PA élevée chez un patient AVC — <b>facteurs favorisants à rechercher</b> ?",
 ["Globe vésical ; douleur","Anémie ; hypokaliémie","Déshydratation ; hyponatrémie","Hypothermie ; hypoglycémie"],"1000","Vérifier les facteurs augmentant la PA : globe vésical, douleur.","Pression artérielle"))
a(Q("H18","K090",2,"AVC — <b>température à partir de laquelle</b> on traite par paracétamol ?",
 ["37,5 °C","38,5 °C","39 °C","40 °C"],"1000","Traitement par paracétamol dès 37,5 °C.","Hyperthermie"))
a(Q("H19","K090",0,"Hyperthermie à la phase aiguë de l'AVC",
 ["Elle est associée à un mauvais pronostic","Elle concerne environ 30 % des AVC","Il faut en rechercher la cause (poumon, urines)","On attend 39 °C avant de la traiter"],"1110","4. Faux : paracétamol dès 37,5 °C.","Hyperthermie"))
a(Q("H20","K091",2,"AVC avec hyperglycémie — <b>soluté de perfusion</b> ?",
 ["Sérum glucosé 5 %","Sérum glucosé 10 %","Sérum physiologique","Sérum glucosé 30 %"],"0010","Perfusion de sérum physiologique, jamais de sérum glucosé.","Hyperglycémie"))
a(Q("H21","K091",1,"Hyperglycémie à la phase aiguë — <b>prise en charge</b> ?",
 ["HGT toutes les heures puis toutes les 4 h","Protocole d'insuline (Actrapid) adapté au dextro","Traiter les hypoglycémies","Apport de sérum glucosé"],"1110","Jamais de sérum glucosé.","Hyperglycémie"))
a(Q("H22","K092",2,"Phase aiguë de l'AVC ischémique — <b>position au lit</b> (cours) ?",
 ["Position assise à 90°","Repos strict au lit, tête entre 0 et 30°","Trendelenburg","Fauteuil dès l'admission"],"0100","Repos strict au lit (0-30°) puis position adaptée à l'hémodynamique cérébrale.","Installation"))
a(Q("H23","K092",2,"Patient avec occlusion carotidienne que l'on assoit rapidement au bord du lit. <b>Risque principal</b> ?",
 ["Hémorragie méningée","HTA maligne","Chute de PA avec hypoperfusion et aggravation de l'AVC","Embolie pulmonaire"],"0010","Relever trop vite → hypotension, hypoperfusion → aggravation de l'AVC.","Installation"))
a(Q("H24","K093",2,"AVC — <b>seuil de SpO2</b> en dessous duquel on administre de l'oxygène ?",
 ["98 %","95 %","92 %","85 %"],"0010","O2 si SatO2 < 92 %.","Voies aériennes"))
a(Q("H25","K093",1,"Liberté des voies aériennes et lutte contre l'hypoxie — <b>mesures</b> ?",
 ["Aspiration des sécrétions si besoin","Oxygène si SatO2 < 92 %","Intubation systématique","Oxygène à haut débit chez tous"],"1100","Intubation très rarement discutée ; O2 seulement si besoin.","Voies aériennes"))
a(Q("H26","K094",2,"AVC — <b>alimentation à l'admission</b> ?",
 ["Alimentation normale dès que le patient a faim","Eau gélifiée sans test préalable","À jeun jusqu'au dépistage des troubles de la déglutition","Sonde nasogastrique systématique"],"0010","Laisser à jeun jusqu'au dépistage des troubles de la déglutition.","Déglutition"))
a(Q("H27","K094",1,"Troubles de la déglutition — <b>facteurs qui les favorisent</b> ?",
 ["Déficit moteur ou sensitif","Trouble de la praxie bucco-faciale","Troubles de la vigilance","Hémianopsie latérale homonyme"],"1110","Déficit moteur, sensitif, praxie de la sphère bucco-faciale et du carrefour, troubles de la vigilance.","Déglutition"))
a(Q("H28","K094",1,"Troubles de la déglutition avérés — <b>adaptations</b> ?",
 ["Texture adaptée","SNG si besoin, alimentation entérale","Assurer un bon équilibre nutritionnel","Alimentation normale sous surveillance"],"1110","Texture adaptée, SNG si besoin, bon équilibre nutritionnel.","Déglutition"))
a(Q("H29","K094",2,"Patient admis en UNV à 11 h qui réclame son repas ; le test de déglutition n'a pas encore été fait. <b>Conduite</b> ?",
 ["Servir un repas mixé","Donner de l'eau plate en petite quantité","Maintenir à jeun jusqu'au dépistage","Servir le repas normal en position assise"],"0010","À jeun tant que les troubles de la déglutition n'ont pas été dépistés (risque de fausse route, pneumopathie).","Déglutition"))
a(Q("H30","K095",2,"AVC — <b>hydratation et surveillance</b> associée ?",
 ["Sérum glucosé ; glycémie","Sérum physiologique ; ionogramme sanguin et diurèse","Restriction hydrique ; poids","Hydratation orale libre ; aucune surveillance"],"0100","Hydratation au sérum physiologique ; surveillance iono sang, diurèse.","Hydratation"))
a(Q("H31","K096",1,"Prévention des <b>thromboses veineuses</b> ?",
 ["HBPM préventive SC","Mobilisation","Bas de contention sur prescription","Anticoagulation curative chez tous"],"1110","HBPM préventive, mobilisation, bas sur prescription.","Prévention"))
a(Q("H32","K097",1,"Prévention des <b>escarres</b> ?",
 ["Matelas anti-escarres","Changements de position","Nursing (massage des points de pression)","Immobilisation stricte prolongée"],"1110","Matelas, nursing, changements de position.","Prévention"))
a(Q("H33","K097",2,"Prévention des <b>rétractions, périarthrites, luxations</b> ?",
 ["Kinésithérapie et mobilisation","Immobilisation du membre","Antalgiques seuls","Contention permanente"],"1000","Rétractions, périarthrites, luxations : kinésithérapie, mobilisation.","Prévention"))
a(Q("H34","K098",2,"AVC — <b>surveillance de la diurèse</b> ?",
 ["Sondage à demeure systématique","Pas de sondage systématique ; dépister un globe au bladder-scan","Sondage évacuateur toutes les 6 h","Étui pénien systématique"],"0100","Pas de sondage systématique ; dépister un globe vésical (bladder-scan).","Diurèse"))
a(Q("H35","K098 K089",2,"Patient AVC agité, hypertendu, sans miction depuis 6 h. <b>Premier geste</b> ?",
 ["Antihypertenseur IV","Sédation","Pose d'une sonde à demeure sans évaluation","Bladder-scan à la recherche d'un globe vésical"],"0001","Le globe vésical augmente la PA et agite : le rechercher avant de traiter la PA.","Diurèse"))
a(Q("H36","K099",1,"Mobilisation et rééducation en UNV ?",
 ["Mise au fauteuil dès que l'état hémodynamique le permet","Kinésithérapie passive et active","Orthophonie (déglutition, langage)","Repos au lit strict jusqu'à la sortie"],"1110","Mobilisation précoce et rééducation dès le départ.","Rééducation"))
a(Q("H37","K099",2,"Patient AVC qui se plaint de céphalées — <b>conduite</b> (cours) ?",
 ["Ne rien donner pour ne pas masquer l'évolution","Antalgique (lutte contre la douleur)","Morphine systématique","Arrêt de toute mobilisation"],"0100","Lutte contre la douleur : antalgiques si céphalées.","Douleur"))
a(Q("H38","K100",0,"Intervenants en UNV",
 ["L'assistante sociale intervient pour le 100 %, l'ALD, la structure de soins de suite","Le psychologue accompagne le patient et la famille","Un tabacologue peut intervenir","Le diététicien n'intervient qu'en cas de diabète"],"1110","4. Faux : diététicienne pour tous (dénutrition, troubles de déglutition).","Équipe"))
a(Q("H39","K101",2,"Infarctus sylvien droit — <b>tableau</b> ?",
 ["Hémiplégie droite avec aphasie","Hémiplégie gauche avec aphasie","Hémiplégie gauche avec négligence","Cécité monoculaire droite isolée"],"0010","Atteinte droite → déficit gauche + négligence (hémisphère mineur).","Installation"))
a(Q("H40","K101",2,"Hémiplégie gauche avec négligence — <b>côté de la sonnette</b> ?",
 ["À gauche","À droite","Au pied du lit","Au choix du patient"],"0100","Sonnette, urinoir, téléphone du côté sain (droit) pour qu'il les trouve.","Installation"))
a(Q("H41","K101",0,"Installation d'un patient (infarctus sylvien droit, hémiplégie gauche + négligence)",
 ["Urinoir et sonnette du côté droit","Photos et objets personnels du côté gauche, pour stimuler","Repas présentés par l'équipe soignante","L'entourage se place uniquement à droite"],"1110","4. Faux : entourage et équipe soignante aussi côté gauche (stimulation du côté négligé).","Installation"))
a(Q("H42","K102",2,"Positionnement et alimentation du patient AVC — <b>modalité de décision</b> ?",
 ["Décidés une fois pour toutes à l'admission","Décidés par le médecin seul","Réévalués chaque jour pour chaque patient, de façon collégiale","Décidés par la famille"],"0010","Questions posées quotidiennement pour chaque patient, de manière collégiale.","Installation"))
