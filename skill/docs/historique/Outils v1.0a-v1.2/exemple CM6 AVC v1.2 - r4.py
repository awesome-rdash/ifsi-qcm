from common import Q
QS = []
a = QS.append
ALCOOL_X = "Complément : repère actuel de Santé publique France (2019) : maximum 10 verres par semaine, 2 verres par jour, et pas tous les jours (sans distinction homme/femme)."
ALCOOL_W = ["Web — Santé publique France, Alcool et santé : améliorer les connaissances et réduire les risques, https://www.santepubliquefrance.fr/presse/2019/alcool-et-sante-ameliorer-les-connaissances-et-reduire-les-risques"]
HC = "Complément : définition hors cours (terme employé dans le cours sans y être défini)."

# ---------- Bilan étiologique ----------
a(Q("I01","K103",1,"Examens du bilan des complications ?",
 ["Troponine","Bandelette urinaire ± ECBU","PSA","Lipasémie"],"1100","Cours p. 19 : NFS, hémostase, VS, CRP, fibrinogène, iono, créatinine, bilan hépatique, glycémie, HbA1c, troponine, BU ± ECBU.","Biologie"))
a(Q("I02","K103",0,"Dosage inclus dans le bilan des complications : vrai ou faux ?",
 ["CRP et VS","Fibrinogène","Bilan hépatique","HbA1c"],"1111","Cours p. 19 : tous font partie du bilan.","Biologie"))
a(Q("I03","K104",2,"Exploration des vaisseaux cervicaux et intracrâniens ?",
 ["Écho-doppler cervical, doppler transcrânien, ARM ou angioscanner","ECG, échographie cardiaque, Holter","EEG, ponction lombaire, IRM FLAIR","Coronarographie, scintigraphie, épreuve d'effort"],"1000","Cours p. 19.","Recherche de cause"))
a(Q("I04","K104",1,"Bilan <u>cardiaque</u> étiologique ?",
 ["ECG","Échographie transthoracique ± transœsophagienne","Holter prolongé","Épreuve d'effort"],"1110","Cours p. 19 : ECG, ETT ± ETO, monitoring, Holter.","Recherche de cause"))
a(Q("I05","K104",2,"But du Holter prolongé ?",
 ["Rechercher un trouble du rythme (ex. FA)","Mesurer la PA sur 24 h","Rechercher une sténose carotidienne","Enregistrer l'activité cérébrale"],"1000","Holter = rythme cardiaque prolongé. PA sur 24 h = MAPA ; activité cérébrale = EEG.","Recherche de cause"))
a(Q("I06","K104",1,"Bilan sanguin des facteurs de risque ?",
 ["Glycémie, HbA1c","Cholestérol total, HDL, LDL, triglycérides","Dosage des PSA","Sérologie de la rougeole"],"1100","Cours p. 19.","Recherche de cause"))
a(Q("I07","K105",2,"Part des infarctus dus à l'<u>athérosclérose</u> ?",
 ["5-10 %","20-30 %","35-45 %","50-60 %"],"0100","Cours p. 20 : 20-30 %.","Athérosclérose"))
a(Q("I08","K105",2,"Traitement chirurgical d'une sténose carotidienne sévère ?",
 ["Endartériectomie","Craniectomie","Clip","Coils"],"1000","Cours p. 20.","Athérosclérose"))
a(Q("I09","K105",2,"Évolution de la lésion d'athérosclérose vers l'infarctus ?",
 ["Plaque → thrombus mural et embolies → thrombus occlusif","Plaque → rupture → hématome intracérébral","Thrombus veineux → embole → infarctus","Plaque → dissection → hématome sous-dural"],"1000","Cours p. 20 : sténoses puis occlusions.","Athérosclérose"))
a(Q("I10","K106",0,"Fibrillation atriale : vrai ou faux ?",
 ["Les battements sont rapides et anarchiques","La contraction est inefficace","La stagnation du sang favorise un thrombus","Le thrombus migre surtout vers les poumons"],"1110","Cours p. 20 : 90 % des embolies dues à la FA sont cérébrales.","Fibrillation atriale"))
a(Q("I11","K107",2,"Prévalence de la FA dans la population ?",
 ["0,1 %","1 %","3 %","5 %"],"0100","Cours p. 20 : 1 %.","Fibrillation atriale"))
a(Q("I12","K107",2,"Part des infarctus <u>cardio-emboliques</u> dus à la FA ?",
 ["1/4","1/3","1/2","3/4"],"0010","Cours p. 20 : la moitié.","Fibrillation atriale"))
a(Q("I13","K107",2,"Part des embolies de FA qui sont <u>cérébrales</u> ?",
 ["60 %","70 %","80 %","90 %"],"0001","Cours p. 20 : 90 %.","Fibrillation atriale"))
a(Q("I14","K108",0,"Signe local de dissection cervicale : vrai ou faux ?",
 ["Cervicalgie, céphalée","Claude Bernard-Horner","Acouphène pulsatile","Fièvre élevée"],"1110","Cours p. 20.","Dissection"))
a(Q("I15","K108",2,"Terrain typique de la dissection cervicale ?",
 ["Sujet jeune","Sujet très âgé","Nourrisson","Diabétique ancien"],"1000","Cours p. 20 : patient jeune ++.","Dissection"))
a(Q("I16","K108 K109",2,"Mme E., 35 ans : cervicalgie droite depuis 2 jours, paupière droite tombante et pupille droite plus petite, puis aphasie brutale. Diagnostic à évoquer ?",
 ["Dissection carotidienne","Athérome carotidien","Fibrillation atriale","Angiopathie amyloïde"],"1000","Cours p. 20 : sujet jeune, signes locaux (cervicalgie, Claude Bernard-Horner), accident ischémique.","Dissection",vign=True))
a(Q("I17","K108",0,"Dissection des artères cervicales : vrai ou faux ?",
 ["La paroi artérielle se fissure","Un caillot se forme dans la paroi","Elle se complique d'AIT ou d'infarctus","Elle touche surtout le sujet âgé"],"1110","Cours p. 20 : patient jeune ++.","Dissection"))
a(Q("I18","K109",2,"Triade de <u>Claude Bernard-Horner</u> ?",
 ["Ptosis ; myosis ; énophtalmie","Ptosis ; mydriase ; exophtalmie","Ptosis ; mydriase ; énophtalmie","Ptosis ; myosis ; exophtalmie"],"1000","Cours p. 20.","Dissection"))

# ---------- Prévention secondaire ----------
a(Q("J01","K110",2,"Risque de récidive à <u>5 ans</u> ?",
 ["10-15 %","25-30 %","40-45 %","50-55 %"],"0100","Cours p. 21 : 25-30 % à 5 ans ; 10 % à 1 an.","Récidive"))
a(Q("J02","K110",2,"Risque de récidive à <u>1 an</u> ?",
 ["5 %","10 %","15 %","20 %"],"0100","Cours p. 21 : 10 % à 1 an.","Récidive"))
a(Q("J03","K111",1,"<u>Objectifs</u> du traitement au long cours ?",
 ["Prévenir la récidive","Prévenir les autres événements cardiovasculaires","Faire disparaître les séquelles","Remplacer la rééducation"],"1100","Cours p. 21 : contrôle des FDR et traitement adapté à la cause.","Objectifs"))
a(Q("J04","K112",1,"Facteurs de risque cardiovasculaire ?",
 ["Hypertension artérielle","Diabète","Hypothyroïdie","Groupe sanguin O"],"1100","Cours p. 21 : HTA, diabète, cholestérol, tabac.","Facteurs de risque"))
a(Q("J05","K112",0,"Facteur de risque à prendre en charge : vrai ou faux ?",
 ["Tabac","Hypercholestérolémie","Sédentarité","Surpoids"],"1111","Cours p. 21 : tous figurent dans le tableau de prévention.","Facteurs de risque"))
a(Q("J06","K112",2,"M. F., 58 ans : fumeur, hypertendu, diabétique, LDL élevé. Nombre de facteurs de risque cités dans le cours ?",
 ["1","2","3","4"],"0001","Tabac, HTA, diabète, cholestérol : les 4.","Facteurs de risque",vign=True))
a(Q("J07","K113",2,"Proportion d'accidents qui pourraient être évités ?",
 ["50 %","60 %","70 %","80 %"],"0001","Cours p. 21 : 80 %.","Facteurs de risque"))
a(Q("J08","K114",2,"<u>Durée</u> du traitement au long cours ?",
 ["Le plus souvent à vie","3 mois","1 an","Jusqu'à disparition du déficit"],"1000","Cours p. 21.","Traitement",lenok=True))
a(Q("J09","K114",2,"En cas d'athérosclérose, autre atteinte à dépister ?",
 ["Coronaropathie","Cancer colorectal","Glaucome","Ostéoporose"],"1000","Cours p. 21.","Traitement"))
a(Q("J10","K115",2,"Deux familles d'antithrombotiques ?",
 ["Antiagrégants plaquettaires ou anticoagulants","Thrombolytiques ou statines","Anticoagulants ou thrombolytiques","Antiagrégants ou bêtabloquants"],"1000","Cours p. 21.","Traitement"))
a(Q("J11","K115",2,"Traitement de l'HTA cité dans le tableau ?",
 ["IEC + diurétiques","Bêtabloquant seul","Antiagrégant seul","Statine seule"],"1000","Cours p. 21 : réduire la PA +++ (IEC + diurétiques).","Traitement"))
a(Q("J12","K115",2,"Indication des statines (tableau) ?",
 ["LDL > 1 g/L, athérosclérose, diabète","LDL > 3 g/L uniquement","HDL > 0,4 g/L","Jamais après un infarctus cérébral"],"1000","Cours p. 21.","Traitement",lenok=True))
a(Q("J13","K115",2,"Objectif d'HbA1c (tableau du cours) ?",
 ["< 6 %","< 6,5 %","< 8 %","< 9 %"],"0100","Cours p. 21 : HbA1c < 6,5 %.","Traitement"))
a(Q("J14","K115",2,"Activité physique recommandée ?",
 ["30-60 min, 3 fois par semaine","10 min par semaine","2 h par jour","Contre-indiquée"],"1000","Cours p. 21.","Hygiène de vie",lenok=True))
a(Q("J15","K115",2,"Consommation d'alcool maximale (tableau du cours) ?",
 ["3 verres/j pour les hommes, 2 pour les femmes","4 verres/j pour les hommes, 3 pour les femmes","2 verres/j pour les hommes, 1 pour les femmes","3 verres/j pour les hommes, 3 pour les femmes"],"1000","Tableau p. 21.","Hygiène de vie",x=ALCOOL_X,w=ALCOOL_W))
a(Q("J16","K115",2,"Définition du surpoids (tableau) ?",
 ["IMC > 25 ; tour de taille > 88 cm (F) / 102 cm (H)","IMC > 30 ; tour de taille > 88 cm (F) / 102 cm (H)","IMC > 25 ; tour de taille > 102 cm (F) / 88 cm (H)","IMC > 27 ; tour de taille > 90 cm (F) / 100 cm (H)"],"1000","Tableau p. 21.","Hygiène de vie"))
a(Q("J17","K116",1,"M. G. sort sous antivitamine K. Points à aborder en éducation thérapeutique ?",
 ["Le carnet de suivi","L'INR cible","Les signes de saignement et la conduite à tenir","L'arrêt du traitement dès que la PA est normale"],"1110","Cours p. 22 : action, durée, AVK (carnet), objectifs (INR), auto-surveillance, effets secondaires et CAT. Traitement le plus souvent à vie.","Éducation thérapeutique",
 dz={3:"l'arrêt d'un traitement de prévention expose à la récidive"},vign=True))
a(Q("J18","K116",1,"Objectifs chiffrés à connaître par le patient ?",
 ["Cible de PA","Cible de LDL","Perte de 10 kg en un mois","Nombre de pas par jour"],"1100","Cours p. 22 : facteurs de risque (cible de PA, LDL), INR.","Éducation thérapeutique"))

# ---------- AIT ----------
a(Q("K01","K117",2,"Durée des symptômes ?",
 ["Moins de 1 h, souvent quelques minutes","Moins de 24 h, souvent plusieurs heures","Plus de 24 h","Plusieurs jours"],"1000","Cours p. 22 : < 1 h, souvent quelques minutes.","Définition"))
a(Q("K02","K117",2,"Mme H. a eu le bras droit faible pendant 10 minutes ; tout est rentré dans l'ordre. Conduite ?",
 ["Appeler le 15 : bilan et traitement urgents","Rassurer, rendez-vous dans un mois","Pas de bilan puisque tout a régressé","Aspirine et attendre une récidive"],"1000","Cours p. 22 : l'AIT est une urgence (risque immédiat d'infarctus).","Prise en charge",
 dz={2:"risque d'infarctus maximal dans les 48 premières heures"},vign=True))
a(Q("K03","K118",2,"Période de risque maximal d'infarctus ?",
 ["Les 48 premières heures","Après 6 mois","Après 1 an","Aucune période particulière"],"1000","Cours p. 22.","Risque"))
a(Q("K04","K119",1,"Données chiffrées du cours ?",
 ["10-15 % d'infarctus dans les 3 mois","1/4 des infarctus sont précédés d'un AIT","Risque nul après la 1re semaine","Moins de 1 % d'infarctus à 3 mois"],"1100","Cours p. 22 : risque à 5 ans d'AVC et d'IDM.","Risque"))
a(Q("K05","K120",2,"Prise en charge ?",
 ["Même bilan et même traitement qu'un infarctus","Aucun bilan si les symptômes ont régressé","Thrombolyse pour tous","Surveillance simple à domicile"],"1000","Cours p. 22.","Prise en charge"))
a(Q("K06","K121",2,"Réduction du risque d'infarctus si on le traite (note) ?",
 ["50 %","60 %","70 %","80 %"],"0001","Note p. 22 : −80 %.","Prise en charge"))

# ---------- Hématome intraparenchymateux ----------
a(Q("L01","K122",2,"Part de l'ensemble des accidents vasculaires cérébraux ?",
 ["5 %","10 %","15 %","20 %"],"0100","Cours p. 22 : 10 %.","Épidémiologie"))
a(Q("L02","K122",2,"Évolution de la fréquence avec l'âge ?",
 ["Elle augmente","Elle diminue","Elle est stable","Elle est maximale chez l'enfant"],"1000","Cours p. 22.","Épidémiologie"))
a(Q("L03","K123",2,"Définition ?",
 ["Saignement dans le parenchyme par rupture d'un vaisseau intracérébral","Saignement dans les espaces sous-arachnoïdiens","Occlusion d'une veine cérébrale","Collection de sang entre l'os et la dure-mère"],"1000","Cours p. 22.","Définition",lenok=True))
a(Q("L04","K124",2,"Première cause des formes non traumatiques ?",
 ["HTA","Angiopathie amyloïde","Antivitamine K","Tumeur cérébrale"],"1000","Cours p. 23 : HTA (80 %, rupture d'artériole perforante).","Causes"))
a(Q("L05","K125",1,"Autres causes ?",
 ["Angiopathie amyloïde","AVK, aspirine, thrombolyse","Alcoolisme chronique","Hypothyroïdie"],"1110","Cours p. 23.","Causes"))
a(Q("L06","K125",0,"Cause : vrai ou faux ?",
 ["Malformation vasculaire","Trouble de l'hémostase","Cocaïne, amphétamines","Fibrillation atriale non anticoagulée"],"1110","Cours p. 23. La FA non anticoagulée donne des infarctus.","Causes"))
a(Q("L07","K125",2,"Caractéristiques de l'<u>angiopathie amyloïde</u> ?",
 ["Sujet âgé ; protéine qui fragilise la paroi ; troubles cognitifs","Sujet jeune ; protéine qui fragilise la paroi ; troubles cognitifs","Sujet âgé ; caillot venu du cœur ; troubles du rythme","Tout âge ; poche sur une artère ; céphalée brutale"],"1000","Cours p. 23.","Causes"))
a(Q("L08","K126",1,"M. I., 76 ans : déficit brutal, céphalées, vomissements et somnolence. Éléments évocateurs d'une hémorragie intracérébrale ?",
 ["Déficit focal soudain","Signes d'HTIC (céphalées, vomissements, vigilance)","Pression artérielle basse","Fièvre élevée"],"1100","Cours p. 23 : déficit focal, HTIC fréquente, PA souvent élevée. Seule l'imagerie tranche.","Clinique",vign=True))
a(Q("L09","K126",2,"Signes d'HTIC ?",
 ["Troubles de la vigilance, céphalées, nausées, vomissements","Fièvre, purpura, raideur de nuque","Hypotension, bradycardie, hypothermie","Diarrhée, douleurs abdominales"],"1000","Cours p. 23.","Clinique"))
a(Q("L10","K127",1,"Mortalité ?",
 ["≈ 50 % à la phase aiguë (note)","≈ 50 % à 6 mois (diapo)","≈ 5 %","≈ 90 % dans les 24 h"],"1100","Note : 50 % à la phase aiguë ; diapo : 50 % à 6 mois.","Pronostic"))
a(Q("L11","K130",2,"Objectif tensionnel en UNV ?",
 ["TAS < 140 ou TAD < 90, rapidement","Traiter seulement si > 220/120","< 185/105","Aucun objectif"],"1000","Cours p. 24 : contrôle intensif, le plus vite possible.","Pression artérielle",lenok=True))
a(Q("L12","K130 K088",2,"Gestion de la PA : différence avec l'<u>infarctus</u> ?",
 ["Infarctus : tolérer jusqu'à 220/120 ; hématome : abaisser vite < 140/90","Infarctus : abaisser vite < 140/90 ; hématome : tolérer jusqu'à 220/120","Même objectif < 185/105 dans les deux cas","Aucun traitement de la PA dans les deux cas"],"1000","Infarctus : maintenir le débit cérébral. Hématome : limiter l'expansion.","Pression artérielle"))
a(Q("L13","K130",2,"Pourquoi abaisser rapidement la PA ?",
 ["Limiter l'expansion de l'hémorragie","Améliorer la perfusion de la pénombre","Prévenir l'épilepsie","Permettre une thrombolyse"],"1000","Cours p. 24.","Pression artérielle"))
a(Q("L14","K131",1,"Prévention des phlébites ?",
 ["HBPM dès l'admission","Compression mécanique","Massage","HBPM à partir de 24-48 h"],"0111","Cours p. 24 : HBPM seulement à 24-48 h (risque de resaignement).","Prévention",dz={0:"risque d'aggraver le saignement"}))
a(Q("L15","K132",2,"Position initiale ?",
 ["Demi-assise","À plat (0°)","Trendelenburg","Décubitus ventral"],"1000","Cours p. 24 : demi-assise ; pas de repos strict comme pour l'infarctus.","Installation"))
a(Q("L16","K133",1,"Traitement spécifique et prévention ?",
 ["Corriger un trouble de la coagulation","Prévenir la récidive selon la cause, surtout l'HTA","Thrombolyse IV","Aspirine systématique"],"1100","Cours p. 24.","Traitement",dz={2:"thrombolytique sur une hémorragie",3:"antiagrégant sur une hémorragie"}))
a(Q("L17","K129",1,"Indications de neurochirurgie ?",
 ["Hématome lobaire volumineux du sujet jeune","Hématome cérébelleux","Malformation vasculaire suspectée","Tout hématome, quelle que soit sa taille"],"1110","Cours p. 24.","Traitement"))

# ---------- Atteinte cérébelleuse ----------
a(Q("M01","K134",2,"Principal danger ?",
 ["Compression du tronc → coma, décès","Cécité","Aphasie","Hémorragie méningée"],"1000","Cours p. 24-25 : compression des centres vitaux.","Risques"))
a(Q("M02","K134",0,"Complication de l'œdème cérébelleux : vrai ou faux ?",
 ["Compression du tronc cérébral","Hydrocéphalie obstructive","Engagement des amygdales","Cécité monoculaire"],"1110","Cours p. 25.","Risques"))
a(Q("M03","K135",2,"Délai habituel de l'œdème compressif ?",
 ["J0-J1","J2-J7","J8-J14","J15-J30"],"0100","Cours p. 25.","Risques"))
a(Q("M04","K135",2,"Volume à risque d'œdème compressif ?",
 ["≥ 1/4 de l'hémisphère cérébelleux","≥ 1/3 de l'hémisphère cérébelleux","≥ 1/2 de l'hémisphère cérébelleux","≥ 2/3 de l'hémisphère cérébelleux"],"0100","Cours p. 25.","Risques"))
a(Q("M05","K136",2,"Traitement neurochirurgical ?",
 ["Craniectomie sous-occipitale ± dérivation","Thrombectomie","Embolisation par coils","Endartériectomie"],"1000","Cours p. 25.","Traitement",lenok=True))

# ---------- Hémorragie méningée ----------
a(Q("N01","K137",2,"Définition ?",
 ["Sang dans les espaces sous-arachnoïdiens","Sang dans le parenchyme cérébral","Sang entre l'os et la dure-mère","Caillot dans un sinus veineux"],"1000","Cours p. 25.","Définition"))
a(Q("N02","K138",2,"Cause majeure ?",
 ["Rupture d'anévrisme intracrânien","HTA chronique","Angiopathie amyloïde","Fibrillation atriale"],"1000","Cours p. 25.","Causes"))
a(Q("N03","K138",2,"Définition d'un <u>anévrisme</u> ?",
 ["Poche sur une paroi artérielle fragile, qui peut se rompre","Caillot dans une veine cérébrale","Communication anormale entre artère et veine","Rétrécissement d'une artère par une plaque"],"1000","Cours p. 25.","Causes"))
a(Q("N04","K139",1,"Facteurs de risque ?",
 ["Tabac","HTA","Fibrillation atriale","Hypoglycémie"],"1100","Cours p. 25.","Causes"))
a(Q("N05","K140",2,"Terrain ?",
 ["30-60 ans, femmes > hommes","30-60 ans, hommes > femmes","20-40 ans, femmes > hommes","60-80 ans, femmes > hommes"],"1000","Cours p. 25.","Causes"))
a(Q("N06","K141",0,"Gravité : vrai ou faux ?",
 ["Mortalité élevée","Séquelles neurologiques","Récidive hémorragique fréquente et grave","Évolution bénigne dans la majorité des cas"],"1110","Cours p. 25.","Gravité"))
a(Q("N07","K142",2,"Céphalée typique ?",
 ["Brutale, inhabituelle, explosive","Progressive sur plusieurs jours","Pulsatile, précédée d'une aura","Matinale, chronique"],"1000","Cours p. 26 : « coup de tonnerre ».","Clinique"))
a(Q("N08","K142",2,"Mme K., 45 ans : céphalée brutale, « la pire de sa vie », raideur de nuque, T 37 °C. Diagnostic à évoquer ?",
 ["Hémorragie méningée","Migraine","Infarctus sylvien","Méningite bactérienne"],"1000","Cours p. 26 : céphalée explosive + syndrome méningé non fébrile.","Clinique",vign=True))
a(Q("N09","K142",0,"Forme typique : vrai ou faux ?",
 ["Céphalée brutale explosive","Raideur de nuque","Fièvre élevée dès le début","Syndrome méningé non fébrile"],"1101","Cours p. 26 : syndrome méningé non fébrile (≠ méningite).","Clinique"))
a(Q("N10","K143",1,"Formes atypiques ?",
 ["Agitation, confusion, coma","Présentation pseudo-psychiatrique","III douloureux (mydriase, ptosis, diplopie)","Hémiplégie progressive sur des semaines"],"1110","Cours p. 26.","Clinique"))
a(Q("N11","K144",2,"Examen de 1re intention ?",
 ["Scanner sans injection + angioscanner","IRM de diffusion seule","Ponction lombaire d'emblée","EEG"],"1000","Cours p. 26.","Diagnostic"))
a(Q("N12","K144",2,"Aspect au scanner sans injection ?",
 ["Hyperdensité dans les espaces méningés","Hypodensité du parenchyme","Toujours normal","Hypodensité des sinus veineux"],"1000","Cours p. 26.","Diagnostic"))
a(Q("N13","K144",2,"Mme L. : céphalée en coup de tonnerre depuis 14 h ; scanner normal. Examen suivant ?",
 ["Ponction lombaire","IRM de diffusion","EEG","Écho-doppler cervical"],"1000","Cours p. 26 : scanner négatif dans 10 % des cas → PL indispensable (vers 12 h, selon la note).","Diagnostic",vign=True))
a(Q("N14","K144",2,"Proportion de scanners négatifs ?",
 ["5 %","10 %","20 %","30 %"],"0100","Cours p. 26 : 10 %.","Diagnostic"))
a(Q("N15","K144",2,"Délai de la ponction lombaire (note de cours) ?",
 ["Environ 2 h","Environ 6 h","Environ 12 h","Environ 24 h"],"0010","Note p. 26 : PL à 12 h du début.","Diagnostic"))
a(Q("N16","K145",1,"Risques avant le traitement de l'anévrisme ?",
 ["Dégradation neurologique rapide (coma, épilepsie)","Troubles neurovégétatifs","Récidive hémorragique","Transformation hémorragique d'un infarctus"],"1110","Cours p. 26.","Prise en charge"))
a(Q("N17","K145",2,"Exploration de l'anévrisme ?",
 ["Artériographie des 4 axes","Écho-doppler cervical","IRM FLAIR","Échographie cardiaque"],"1000","Cours p. 26.","Prise en charge"))
a(Q("N18","K146",2,"Traitements d'exclusion de l'anévrisme ?",
 ["Coils (neuroradiologie) ou clip (neurochirurgie)","Thrombolyse ou thrombectomie","Endartériectomie ou stent carotidien","Craniectomie ou dérivation"],"1000","Cours p. 27.","Traitement"))
a(Q("N19","K146",2,"Principe des <u>coils</u> ?",
 ["Remplir le sac par voie endovasculaire","Poser une pince au collet par chirurgie","Dissoudre le caillot par thrombolytique","Évacuer l'hématome par craniotomie"],"1000","Cours p. 27. La pince au collet = clip.","Traitement"))

# ---------- Thrombose veineuse cérébrale ----------
a(Q("O01","K147",2,"Définition ?",
 ["Occlusion d'une veine ou d'un sinus veineux","Occlusion d'une artère cérébrale","Rupture d'un anévrisme","Dissection d'une carotide"],"1000","Cours p. 27.","Définition"))
a(Q("O02","K147",2,"Vers où se draine le sang veineux cérébral ?",
 ["Les veines jugulaires","La veine cave inférieure","La veine porte","Les artères vertébrales"],"1000","Cours p. 27.","Définition"))
a(Q("O03","K148",2,"Localisation la plus fréquente (schéma) ?",
 ["Sinus latéral","Sinus caverneux","Veines profondes","Sinus droit"],"1000","Schéma p. 27 : sinus latéral 73 %, sinus sagittal supérieur 62-65 %, veines corticales 17-21 %, sinus droit 11-18 %, veines profondes 7-11 %, sinus caverneux 2 %.","Localisation"))
a(Q("O04","K148",2,"Atteinte de plusieurs sinus et veines ?",
 ["20-30 %","35-45 %","50-60 %","70-80 %"],"0010","Cours p. 27.","Localisation"))
a(Q("O05","K149",1,"Causes gynéco-obstétricales ?",
 ["Grossesse","Post-partum","Contraception","Ménopause"],"1110","Cours p. 28.","Causes"))
a(Q("O06","K149",0,"Cause : vrai ou faux ?",
 ["Thrombophilie","Lupus, Behçet","Cancer","HTA chronique"],"1110","Cours p. 28.","Causes"))
a(Q("O07","K149",2,"Situation étiologique la plus fréquente ?",
 ["Idiopathique","Infection","Cancer","Grossesse"],"1000","Cours p. 28 : idiopathique le plus souvent.","Causes"))
a(Q("O08","K150",2,"Trois types de symptômes ?",
 ["HTIC ; signes focaux ; épilepsie","Fièvre ; purpura ; raideur","HTIC ; aphasie isolée ; fièvre","Syndrome méningé ; cécité ; vertige"],"1000","Cours p. 28.","Clinique"))
a(Q("O09","K150",2,"Mode d'installation ?",
 ["Souvent subaigu, sur quelques jours","Toujours brutal, en quelques secondes","Sur plusieurs années","Uniquement la nuit"],"1000","Cours p. 28.","Clinique"))
a(Q("O10","K150",1,"Signes d'HTIC ?",
 ["Céphalées aiguës","Nausées, vomissements","Diplopie","Hyperthermie"],"1110","Cours p. 28.","Clinique"))
a(Q("O11","K151",1,"Gravité ?",
 ["HTIC","Mortalité","Cécité","Surdité"],"1110","Cours p. 28.","Clinique"))
a(Q("O12","K152",2,"Examen diagnostique ?",
 ["IRM-ARM ou scanner avec injection","Scanner sans injection seul","EEG","Échographie cardiaque"],"1000","Cours p. 29.","Diagnostic"))
a(Q("O13","K153",2,"Traitement antithrombotique ?",
 ["Héparine puis AVK pendant 6 mois","Aspirine seule à vie","Thrombolyse IV puis rien","AVK pendant 1 semaine"],"1000","Cours p. 29.","Traitement"))
a(Q("O14","K153",1,"Traitements étiologique et symptomatique ?",
 ["Arrêt de la contraception orale","Traitement de l'épilepsie","Traitement de l'HTIC et des céphalées","Thrombectomie systématique"],"1110","Cours p. 29.","Traitement"))

# ---------- Vocabulaire ----------
def V(i,k,term,props,truth,expl): a(Q(i,k,2,f"Définition : <u>{term}</u> ?",props,truth,expl,"",x=HC))
V("V01","V01","athérome",["Plaque lipidique dans la paroi d'une artère","Caillot formé dans un vaisseau","Élément circulant qui bouche un vaisseau","Dilatation localisée d'une artère"],"1000","Caillot sur place = thrombus ; élément circulant = embole ; dilatation = anévrisme.")
V("V02","V02","thrombus",["Plaque lipidique dans la paroi d'une artère","Caillot formé dans un vaisseau","Sang collecté hors des vaisseaux","Élément circulant qui bouche un vaisseau"],"0100","S'il migre, il devient un embole. Sang hors des vaisseaux = hématome.")
V("V03","V03","embolie",["Formation d'un caillot sur place","Rétrécissement d'une artère","Obstruction par un élément venu d'ailleurs","Rupture de la paroi d'une artère"],"0010","Caillot sur place = thrombose ; rétrécissement = sténose.")
a(Q("V04","V02 V03",2,"Caillot formé dans l'oreillette au cours d'une FA, qui migre et bouche une artère cérébrale. Mécanisme ?",
 ["Embolie","Thrombose sur place","Sténose athéromateuse","Dissection"],"1000","Thrombus formé dans le cœur qui migre = embole → embolie.","",x=HC,vign=True))
V("V05","V04","lacune",["Grand infarctus de tout un territoire","Petit infarctus profond (petite artère perforante)","Petite hémorragie profonde","Dilatation des ventricules"],"0100","Classiquement < 15 mm. Dilatation des ventricules = hydrocéphalie.")
V("V06","V05","sténose",["Rétrécissement d'une artère","Obstruction complète d'une artère","Dilatation localisée d'une artère","Déchirure de la paroi d'une artère"],"1000","Occlusion = complète ; anévrisme = dilatation ; dissection = déchirure.")
V("V07","V06","endartériectomie",["Retrait du caillot par cathéter","Ablation chirurgicale de la plaque","Pose d'une pince sur un anévrisme","Ouverture d'une partie du crâne"],"0100","Cathéter = thrombectomie ; pince = clip ; ouverture du crâne = craniectomie.")
V("V08","V07","HTIC",["Hypertension artérielle sévère","Hausse de la pression intracrânienne","Hausse de la pression oculaire","Hausse de la pression jugulaire"],"0100","HTA sévère avec atteinte d'organe = HTA maligne ; pression oculaire = glaucome.")
V("V09","V08","hydrocéphalie",["Eau en excès dans le tissu cérébral","LCR en excès, ventricules dilatés","Sang entre dure-mère et cerveau","Sang dans les espaces sous-arachnoïdiens"],"0100","Eau dans le tissu = œdème ; sang sous-arachnoïdien = hémorragie méningée.")
V("V10","V09","œdème cérébral",["Eau en excès dans le tissu cérébral","LCR en excès, ventricules dilatés","Sang collecté dans le parenchyme","Tissu cérébral nécrosé"],"1000","LCR = hydrocéphalie ; sang = hématome ; nécrose = infarctus.")
V("V11","V10","apraxie",["Trouble de la coordination","Paralysie partielle d'un membre","Incapacité à faire un geste appris","Trouble du langage"],"0010","Force conservée. Coordination = ataxie ; paralysie partielle = parésie ; langage = aphasie.")
V("V12","V11","négligence",["Perte de la moitié du champ visuel","Moitié de l'espace et du corps ignorée","Perte de sensibilité d'un hémicorps","Paralysie d'un hémicorps"],"0100","Non expliquée par un déficit moteur ou visuel. Moitié du champ visuel = hémianopsie.")
V("V13","V12","diplopie",["Vision floue d'un œil","Vision double","Perte de la moitié du champ visuel","Perte de la vision d'un œil"],"0100","Moitié du champ visuel = hémianopsie ; perte d'un œil = cécité monoculaire.")
V("V14","V13","ptosis ; myosis ; énophtalmie",["Paupière tombante ; petite pupille ; œil enfoncé","Paupière tombante ; grande pupille ; œil saillant","Petite pupille ; paupière tombante ; œil saillant","Paupière rétractée ; grande pupille ; œil enfoncé"],"1000","Myosis ≠ mydriase ; énophtalmie ≠ exophtalmie. Triade de Claude Bernard-Horner.")
V("V15","V14","mydriase",["Pupille rétrécie","Pupille dilatée","Paupière tombante","Pupilles inégales"],"0100","Myosis = rétrécie ; ptosis = paupière ; anisocorie = inégales.")
V("V16","V15","spasticité",["Paralysie avec perte du tonus","Raideur accrue à l'étirement rapide","Tendon raccourci de façon fixe","Tremblement au repos"],"0100","Paralysie flasque = perte du tonus ; tendon raccourci = rétraction.")
V("V17","V16","algoneurodystrophie",["Douleur régionale complexe d'un membre","Infection d'une articulation","Fonte musculaire d'immobilisation","Tendon raccourci de façon fixe"],"1000","Douleur, œdème, troubles vasomoteurs, raideur (souvent épaule-main). Fonte musculaire = amyotrophie.")
V("V18","V17","thrombophilie",["Tendance aux saignements","Plaquettes basses","Tendance aux thromboses","Plaquettes élevées"],"0010","Saignements = diathèse hémorragique ; plaquettes basses = thrombopénie ; élevées = thrombocytose.")
V("V19","V18","thrombopénie",["Plaquettes basses","Plaquettes élevées","Hémoglobine basse","Tendance aux thromboses"],"1000","Contre-indication à la thrombolyse. Hémoglobine basse = anémie.")
V("V20","V19","hématome",["Caillot dans un vaisseau","Sang collecté dans un tissu","Dilatation d'une artère","Eau en excès dans un tissu"],"0100","Caillot dans un vaisseau = thrombus ; eau = œdème.")
