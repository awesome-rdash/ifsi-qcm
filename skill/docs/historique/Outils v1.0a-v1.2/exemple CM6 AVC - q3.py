from common import Q
QS = []
a = QS.append
ALCOOL_X = "Complément : repère actuel de Santé publique France (2019) : maximum 10 verres par semaine, maximum 2 verres par jour, et pas tous les jours (plus de distinction homme/femme)."
ALCOOL_W = ["Web — Santé publique France, Alcool et santé : améliorer les connaissances et réduire les risques, https://www.santepubliquefrance.fr/presse/2019/alcool-et-sante-ameliorer-les-connaissances-et-reduire-les-risques"]

# ---------- I. Bilan étiologique ----------
a(Q("I01","K103",1,"Bilan des complications de l'AVC — <b>examens</b> ?",
 ["Troponine","BU ± ECBU","HbA1c","PSA"],"1110","Bilan : NFS, hémostase, VS, CRP, fibrinogène, iono, créat, bilan hépatique, glycémie, HbA1c, troponine, BU ± ECBU.","Bilan biologique"))
a(Q("I02","K103",1,"Bilan des complications de l'AVC — autres <b>examens</b> ?",
 ["CRP et VS","Fibrinogène","Bilan hépatique","Lipasémie"],"1110","La lipasémie ne fait pas partie du bilan.","Bilan biologique"))
a(Q("I03","K104",2,"Recherche de cause — <b>exploration des vaisseaux</b> cervicaux et intracrâniens ?",
 ["ECG ; échographie cardiaque ; Holter","Écho-doppler des troncs supra-aortiques ; doppler transcrânien ; ARM ou angioTDM","EEG ; ponction lombaire","Coronarographie ; scintigraphie"],"0100","Vaisseaux : EDTSA, doppler transcrânien, ARM cervicale et du polygone (ou angioTDM).","Bilan étiologique"))
a(Q("I04","K104",1,"Recherche de cause — <b>bilan cardiaque</b> ?",
 ["ECG","Échographie cardiaque transthoracique ± transœsophagienne","Holter prolongé","Épreuve d'effort"],"1110","Cœur : ECG, ETT ± ETO, monitoring, Holter prolongé.","Bilan étiologique"))
a(Q("I05","K104",2,"Bilan étiologique de l'AVC — <b>but du Holter prolongé</b> ?",
 ["Mesurer la PA sur 24 h","Rechercher un trouble du rythme (ex. fibrillation atriale)","Rechercher une sténose carotidienne","Surveiller l'activité électrique cérébrale"],"0100","Holter : enregistrement prolongé du rythme cardiaque (recherche de FA). PA sur 24 h = MAPA.","Bilan étiologique"))
a(Q("I06","K104",1,"Recherche de cause — <b>bilan sanguin des facteurs de risque</b> ?",
 ["Glycémie, HbA1c","Cholestérol total, HDL, LDL, triglycérides","Ionogramme, créatinine","Dosage des PSA"],"1110","Bilan des FDR : glycémie, HbA1c, cholestérol (HDL, LDL), TG, iono, créat. Le reste est orienté (toxiques, coagulopathie, infection…).","Bilan étiologique"))
a(Q("I07","K105",2,"Athérosclérose — <b>part des infarctus cérébraux</b> ?",
 ["1-2 %","20-30 %","50-60 %","80-90 %"],"0100","Athérosclérose : 20-30 % des infarctus cérébraux.","Athérosclérose"))
a(Q("I08","K105",2,"Sténose carotidienne sévère — <b>traitement chirurgical possible</b> ?",
 ["Craniectomie","Clip","Endartériectomie","Thrombolyse"],"0010","Si sténose sévère : indication possible d'endartériectomie.","Athérosclérose"))
a(Q("I09","K105",2,"Athérosclérose — <b>évolution de la lésion</b> vers l'infarctus ?",
 ["Plaque d'athérome → thrombus mural et embolies → thrombus occlusif","Anévrisme → rupture → hématome","Thrombus veineux → embolie → infarctus pulmonaire","Dissection → hématome sous-dural"],"1000","Sténoses puis occlusions : plaque → thrombus mural/embolies → thrombus occlusif.","Athérosclérose"))
a(Q("I10","K106",1,"Fibrillation atriale — <b>mécanisme menant à l'AVC</b> ?",
 ["Battements rapides et anarchiques","Contraction inefficace du cœur","Stagnation du sang et formation d'un thrombus","Rupture d'un anévrisme"],"1110","FA : contraction inefficace → stagnation → thrombus → embolie (cérébrale dans 90 % des cas).","Fibrillation atriale"))
a(Q("I11","K107",2,"Fibrillation atriale — <b>prévalence</b> dans la population générale ?",
 ["0,01 %","1 %","10 %","25 %"],"0100","FA : 1 % de la population générale.","Fibrillation atriale"))
a(Q("I12","K107",2,"Fibrillation atriale — <b>part des infarctus cérébraux cardio-emboliques</b> ?",
 ["10 %","25 %","La moitié","90 %"],"0010","1/2 des IC cardio-emboliques sont dus à la FA ; 90 % des embolies dues à la FA sont cérébrales.","Fibrillation atriale"))
a(Q("I13","K107",2,"Embolies dues à la FA — <b>proportion de localisation cérébrale</b> ?",
 ["10 %","50 %","75 %","90 %"],"0001","90 % des embolies dues à la FA sont cérébrales.","Fibrillation atriale"))
a(Q("I14","K108",1,"Dissection d'une artère cervicale — <b>signes locaux</b> ?",
 ["Cervicalgies, céphalées","Claude Bernard-Horner","Acouphènes pulsatiles","Fièvre élevée"],"1110","Signes locaux : cervicalgies, céphalées, CBH, acouphènes pulsatiles ; accidents ischémiques : AIT, infarctus.","Dissection"))
a(Q("I15","K108",2,"Dissection des artères cervicales — <b>terrain typique</b> ?",
 ["Sujet très âgé","Sujet jeune","Nourrisson","Sujet diabétique ancien"],"0100","Dissection : patient jeune ++.","Dissection"))
a(Q("I16","K108",0,"Dissection des artères cervicales",
 ["La paroi artérielle se fissure","Elle favorise la formation d'un caillot","Elle peut donner un AIT ou un infarctus cérébral","C'est la cause la plus fréquente d'AVC du sujet âgé"],"1110","4. Faux : cause plus rare, typique du sujet jeune.","Dissection"))
a(Q("I17","K109",2,"Syndrome de Claude Bernard-Horner — <b>triade</b> ?",
 ["Ptosis ; mydriase ; exophtalmie","Ptosis ; myosis ; énophtalmie","Mydriase ; diplopie ; ptosis","Myosis ; exophtalmie ; nystagmus"],"0100","CBH : ptosis, myosis, énophtalmie (asymétrie pupillaire, paupière tombante).","Dissection"))

# ---------- J. Prévention secondaire ----------
a(Q("J01","K110",2,"Après un AVC — <b>risque de récidive à 5 ans</b> ?",
 ["2-3 %","25-30 %","50-60 %","80 %"],"0100","Récidive : 25-30 % à 5 ans (10 % à 1 an).","Récidive"))
a(Q("J02","K110",2,"Après un AVC — <b>risque de récidive à 1 an</b> ?",
 ["1 %","10 %","30 %","50 %"],"0100","Récidive : 10 % à 1 an.","Récidive"))
a(Q("J03","K111",1,"Prévention secondaire — <b>objectifs</b> ?",
 ["Prévenir la récidive d'AVC","Prévenir les autres événements cardiovasculaires (coronarien, mort vasculaire)","Traiter de façon adaptée à la cause","Faire disparaître les séquelles neurologiques"],"1110","Deux aspects : dépistage/contrôle des FDR et traitement adapté à la cause (bilan étiologique en UNV).","Objectifs"))
a(Q("J04","K112",1,"<b>Facteurs de risque cardiovasculaire</b> ?",
 ["Hypertension artérielle","Diabète","Tabac","Hypothyroïdie"],"1110","FDR : HTA, diabète, cholestérol, tabac.","Facteurs de risque"))
a(Q("J05","K112",1,"Autres <b>facteurs de risque</b> à prendre en charge ?",
 ["Hypercholestérolémie","Sédentarité","Surpoids","Groupe sanguin O"],"1110","Cholestérol, activité physique, surpoids, alcool font partie du tableau de prévention.","Facteurs de risque"))
a(Q("J06","K112",2,"Homme de 58 ans, fumeur, hypertendu, diabétique, LDL élevé, AVC ischémique. <b>Combien de facteurs de risque cardiovasculaire</b> cités dans le cours présente-t-il ?",
 ["1","2","3","4"],"0001","Tabac, HTA, diabète, cholestérol : les 4 FDR cités.","Facteurs de risque"))
a(Q("J07","K113",2,"AVC — <b>proportion qui pourrait être évitée</b> ?",
 ["10 %","30 %","50 %","80 %"],"0001","80 % des AVC peuvent être évités (contrôle des FDR).","Facteurs de risque"))
a(Q("J08","K114",2,"Traitement de prévention après un AVC — <b>durée</b> ?",
 ["3 mois","1 an","Le plus souvent à vie","Jusqu'à disparition du déficit"],"0010","Traitement de prévention : le plus souvent à vie.","Traitement"))
a(Q("J09","K114",2,"Après un AVC athéroscléreux — <b>autre atteinte à dépister</b> ?",
 ["Coronaropathie","Cancer colorectal","Glaucome","Ostéoporose"],"1000","Penser à dépister une coronaropathie, surtout si athérosclérose.","Traitement"))
a(Q("J10","K115",2,"Prévention secondaire — <b>2 familles d'antithrombotiques</b> ?",
 ["Thrombolytiques ou statines","Antiagrégants plaquettaires ou anticoagulants","Anticoagulants ou thrombolytiques","Antiagrégants ou bêtabloquants"],"0100","Antithrombotiques : antiagrégants plaquettaires ou anticoagulants (selon la cause).","Traitement"))
a(Q("J11","K115",2,"Prévention secondaire — <b>traitement de l'HTA</b> cité dans le tableau ?",
 ["IEC + diurétiques","Aucun traitement","Antiagrégant seul","Statine seule"],"1000","Dépistage et traitement de l'HTA ; réduire la PA +++ (IEC + diurétiques).","Traitement"))
a(Q("J12","K115",2,"Prévention secondaire — <b>indication des statines</b> (tableau) ?",
 ["Uniquement si LDL > 3 g/L","LDL > 1 g/L, athérosclérose, diabète","HDL > 0,4 g/L","Jamais après un AVC"],"0100","Statines si LDL > 1 g/L, athérosclérose, diabète + régime.","Traitement"))
a(Q("J13","K115",2,"Diabète après un AVC — <b>objectif d'HbA1c</b> ?",
 ["< 4 %","< 6,5 %","< 9 %","< 12 %"],"0100","HbA1c < 6,5 % ; régime, antidiabétiques oraux, insuline.","Traitement"))
a(Q("J14","K115",2,"Prévention secondaire — <b>activité physique</b> recommandée ?",
 ["10 minutes par semaine","30-60 minutes, 3 fois par semaine","2 heures par jour","Contre-indiquée après un AVC"],"0100","30-60 min d'exercice × 3 par semaine.","Hygiène de vie"))
a(Q("J15","K115",2,"Prévention secondaire — <b>consommation d'alcool maximale</b> indiquée dans le tableau du cours ?",
 ["5 verres/jour pour les hommes, 3 pour les femmes","3 verres/jour pour les hommes, 2 pour les femmes","1 verre/jour pour les hommes, aucun pour les femmes","Aucune restriction"],"0100","Tableau du cours : consommation modérée, max 3 verres H et 2 F.","Hygiène de vie",x=ALCOOL_X,w=ALCOOL_W))
a(Q("J16","K115",2,"Prévention secondaire — <b>définition du surpoids</b> (tableau) ?",
 ["IMC > 30 ; tour de taille > 80 cm (F) / 94 cm (H)","IMC > 25 ; tour de taille > 88 cm (F) / 102 cm (H)","IMC > 20 ; tour de taille > 70 cm (F) / 90 cm (H)","IMC > 35 ; tour de taille > 100 cm (F) / 120 cm (H)"],"0100","Surpoids : IMC > 25, TT > 88 cm F, 102 cm H → perdre l'excès de poids.","Hygiène de vie"))
a(Q("J17","K116",1,"Éducation thérapeutique après un AVC — <b>contenu</b> ?",
 ["Action de chaque médicament","Carnet de suivi et INR en cas d'AVK","Effets secondaires et conduite à tenir","Arrêt du traitement dès que la PA est normale"],"1110","ETP : action, durée, AVK (carnet), objectifs, auto-surveillance, effets secondaires et CAT. Le traitement est à vie.","ETP"))
a(Q("J18","K116",1,"Éducation thérapeutique — <b>objectifs chiffrés</b> à connaître par le patient ?",
 ["Cible de PA","Cible de LDL","INR cible si AVK","Perte de 10 kg en un mois"],"1110","Objectifs : facteurs de risque (cible de PA, LDL), INR. Observance, signes d'alarme.","ETP"))

# ---------- K. AIT ----------
a(Q("K01","K117",2,"AIT — <b>durée des symptômes</b> ?",
 ["Moins de 1 h, souvent quelques minutes","Jusqu'à 24 h, souvent plusieurs heures","Plus de 24 h","Plusieurs jours"],"1000","AIT : symptômes < 1 h, souvent quelques minutes.","AIT"))
a(Q("K02","K117",2,"Patiente : déficit du bras droit pendant 10 minutes, totalement régressé. <b>Conduite</b> ?",
 ["Rassurer, rendez-vous dans 1 mois","Pas de bilan puisque tout a régressé","Urgence : appeler le 15 pour bilan et traitement","Aspirine et attendre une éventuelle récidive"],"0010","AIT = urgence (risque immédiat d'infarctus) : même bilan et même traitement que l'AVC.","AIT"))
a(Q("K03","K118",2,"AIT — <b>période de risque maximal</b> d'infarctus cérébral ?",
 ["Les 48 premières heures","Après 6 mois","Après 1 an","Aucun risque particulier"],"1000","Risque surtout dans les 48 premières heures et les premiers jours.","AIT"))
a(Q("K04","K119",1,"AIT — <b>données chiffrées</b> du cours ?",
 ["10-15 % d'AVC dans les 3 mois","1/4 des infarctus cérébraux sont précédés d'un AIT","Risque à 5 ans d'AVC et d'IDM","Risque nul après la 1re semaine"],"1110","4. Faux : risque à 5 ans d'AVC et d'IDM.","AIT"))
a(Q("K05","K120",2,"AIT — <b>prise en charge</b> ?",
 ["Aucun bilan si les symptômes ont régressé","Thrombolyse systématique","Surveillance simple à domicile","Même bilan étiologique et même traitement qu'un infarctus cérébral"],"0001","Bilan (recherche de cause) et traitement comme un AVC.","AIT"))
a(Q("K06","K121",2,"AIT traité — <b>réduction du risque d'AVC</b> (note de cours) ?",
 ["5 %","20 %","50 %","80 %"],"0001","Note : traiter l'AIT réduit de 80 % le risque d'AVC.","AIT"))

# ---------- L. Hématome intraparenchymateux ----------
a(Q("L01","K122",2,"Hématome intraparenchymateux — <b>part de l'ensemble des AVC</b> ?",
 ["1 %","10 %","50 %","85 %"],"0100","HIP : 10 % des AVC.","HIP"))
a(Q("L02","K122",2,"Hématome intraparenchymateux — <b>fréquence selon l'âge</b> ?",
 ["Diminue avec l'âge","Augmente avec l'âge","Stable à tout âge","Maximale chez l'enfant"],"0100","Fréquence qui augmente avec l'âge +++.","HIP"))
a(Q("L03","K123",2,"Hématome intraparenchymateux — <b>définition</b> ?",
 ["Saignement dans les espaces sous-arachnoïdiens","Saignement dans le parenchyme cérébral par rupture d'un vaisseau intracérébral","Occlusion d'une veine cérébrale","Collection entre l'os et la dure-mère"],"0100","Rupture d'une artère, artériole, malformation artério-veineuse ou veine dans le parenchyme.","HIP"))
a(Q("L04","K124",2,"Hématome intraparenchymateux non traumatique — <b>1re cause</b> ?",
 ["Angiopathie amyloïde","Traitement par AVK","HTA (rupture d'artériole perforante)","Tumeur cérébrale"],"0010","HTA : étiologie la plus fréquente (80 %).","HIP"))
a(Q("L05","K125",1,"Hématome intraparenchymateux — <b>autres causes</b> ?",
 ["Angiopathie amyloïde","Médicaments : AVK, aspirine, thrombolyse","Alcoolisme chronique","Hypothyroïdie"],"1110","Autres causes : angiopathie amyloïde, médicaments, alcool, IC secondairement hémorragique, malformations…","HIP"))
a(Q("L06","K125",1,"Hématome intraparenchymateux — encore d'autres <b>causes</b> ?",
 ["Malformations vasculaires","Troubles de l'hémostase","Toxiques (amphétamines, cocaïne)","Fibrillation atriale non anticoagulée"],"1110","Aussi : endocardite (anévrismes mycotiques), tumeur hémorragique. La FA non anticoagulée donne des infarctus.","HIP"))
a(Q("L07","K125",2,"<b>Angiopathie amyloïde</b> — caractéristiques ?",
 ["Sujet jeune ; dépôt de cholestérol dans la paroi ; sans trouble cognitif","Sujet âgé ; protéine déposée dans la paroi des vaisseaux qui les fragilise ; troubles cognitifs associés","Sujet âgé ; caillot venant du cœur ; troubles du rythme","Tout âge ; poche sur la paroi artérielle ; céphalée en coup de tonnerre"],"0100","Angiopathie amyloïde : personne âgée, protéine fragilisant la paroi, associée à des troubles cognitifs.","HIP"))
a(Q("L08","K126",1,"Hématome intraparenchymateux — <b>clinique</b> ?",
 ["Déficit focal soudain","Céphalées, nausées, vomissements","Troubles de la vigilance","PA habituellement basse"],"1110","Déficit focal, HTIC fréquente, PA souvent élevée.","HIP"))
a(Q("L09","K126",2,"Hématome intraparenchymateux — <b>signes d'HTIC</b> ?",
 ["Fièvre, purpura, raideur de nuque","Troubles de la vigilance, céphalées, nausées, vomissements","Hypotension, bradycardie, hypothermie","Diarrhée, douleurs abdominales"],"0100","HTIC : troubles de la vigilance, céphalées, nausées, vomissements.","HIP"))
a(Q("L10","K127",1,"Hématome intraparenchymateux — <b>mortalité</b> ?",
 ["≈ 50 % à la phase aiguë (note de cours)","≈ 50 % à 6 mois (diapo)","≈ 5 %","≈ 90 % dans les 24 h"],"1100","Mortalité élevée : 50 % à la phase aiguë (note), 50 % à 6 mois (diapo).","HIP"))
a(Q("L11","K130",2,"Hématome intraparenchymateux en UNV — <b>objectif tensionnel</b> ?",
 ["Ne traiter que si > 220/120 mmHg","< 185/105 mmHg","TAS < 140 ou TAD < 90 mmHg, rapidement","Aucun objectif"],"0010","Contrôle intensif : TAS < 140 ou TAD < 90, le plus rapidement possible.","PA et hématome"))
a(Q("L12","K130 K088",2,"Gestion de la PA — <b>différence entre infarctus et hématome</b> ?",
 ["Infarctus : abaisser vite < 140/90 ; hématome : tolérer jusqu'à 220/120","Infarctus : tolérer jusqu'à 220/120 ; hématome : abaisser vite < 140/90","Même objectif < 185/105 dans les deux cas","Aucun traitement de la PA dans les deux cas"],"0100","Infarctus : on tolère (maintien du DSC). Hématome : on abaisse vite (limiter l'expansion).","PA et hématome"))
a(Q("L13","K130",2,"Hématome intraparenchymateux — <b>pourquoi abaisser rapidement la PA</b> ?",
 ["Limiter l'expansion de l'hémorragie","Améliorer la perfusion de la pénombre","Prévenir l'épilepsie","Permettre une thrombolyse"],"1000","Diminuer la TA pour limiter l'expansion de l'hémorragie.","PA et hématome"))
a(Q("L14","K131",1,"Hématome intraparenchymateux — <b>prévention des phlébites</b> ?",
 ["HBPM dès l'admission","Compression mécanique","Massage","HBPM à partir de 24-48 h"],"0111","Compression mécanique, massage, HBPM seulement à 24-48 h (risque de saignement).","Prévention"))
a(Q("L15","K132",2,"Hématome intraparenchymateux — <b>position initiale</b> ?",
 ["Demi-assise","Repos strict à plat (0°)","Trendelenburg","Décubitus ventral"],"1000","Position initiale demi-assise ; pas de repos strict au lit comme pour l'infarctus.","Installation"))
a(Q("L16","K133",1,"Hématome intraparenchymateux — <b>traitement spécifique et prévention</b> ?",
 ["Correction d'un trouble de la coagulation","Prévention des récidives selon la cause, surtout l'HTA","Thrombolyse IV","Aspirine systématique"],"1100","Traitement spécifique : corriger la coagulation ; prévention selon la cause (surtout HTA).","Traitement"))
a(Q("L17","K129",1,"Hématome intraparenchymateux — <b>indications de neurochirurgie</b> ?",
 ["Hématome volumineux lobaire du sujet jeune","Hématome cérébelleux","Suspicion de malformation vasculaire","Tout hématome, quelle que soit sa taille"],"1110","Neurochirurgie : hématomes volumineux lobaires du jeune, cérébelleux, malformation ; traumatique = neurochirurgie.","Neurochirurgie"))

# ---------- M. AVC cérébelleux ----------
a(Q("M01","K134",2,"AVC cérébelleux — <b>principal danger</b> ?",
 ["Cécité","Aphasie","Compression du tronc cérébral (centres vitaux) → coma, décès","Hémorragie méningée"],"0010","Quand il grossit, il comprime le tronc (centres cardio-respiratoires) → coma ou décès rapide.","Cérébelleux"))
a(Q("M02","K134",1,"Œdème d'un AVC cérébelleux — <b>complications</b> ?",
 ["Compression du tronc cérébral","Hydrocéphalie obstructive","Engagement des amygdales cérébelleuses","Cécité monoculaire"],"1110","Compression du tronc, hydrocéphalie obstructive, engagement.","Cérébelleux"))
a(Q("M03","K135",2,"Œdème d'un AVC cérébelleux — <b>délai de survenue</b> habituel ?",
 ["H1-H2","J2-J7","J30","Après 3 mois"],"0100","Souvent entre J2 et J7 ; volume ≥ 1/3 de l'hémisphère cérébelleux.","Cérébelleux"))
a(Q("M04","K135",2,"AVC cérébelleux — <b>volume à risque</b> d'œdème compressif ?",
 ["≥ 1/10 de l'hémisphère cérébelleux","≥ 1/3 de l'hémisphère cérébelleux","Tout volume","Uniquement si les 2 hémisphères sont touchés"],"0100","Volume ≥ 1/3 de l'hémisphère cérébelleux.","Cérébelleux"))
a(Q("M05","K136",2,"AVC cérébelleux compressif — <b>traitement neurochirurgical</b> ?",
 ["Thrombectomie","Embolisation par coils","Craniectomie sous-occipitale ± exérèse ± dérivation ventriculaire","Endartériectomie"],"0010","Traitement symptomatique de l'HTIC + neurochirurgie (transfert SAMU).","Cérébelleux"))

# ---------- N. Hémorragie méningée ----------
a(Q("N01","K137",2,"Hémorragie méningée (HSA) — <b>définition</b> ?",
 ["Saignement dans le parenchyme cérébral","Irruption de sang dans les espaces sous-arachnoïdiens","Saignement entre l'os et la dure-mère","Occlusion d'un sinus veineux"],"0100","HSA : sang qui se déverse dans les espaces sous-arachnoïdiens (méninges).","HSA"))
a(Q("N02","K138",2,"Hémorragie méningée — <b>cause majeure</b> ?",
 ["HTA chronique","Angiopathie amyloïde","Rupture d'un anévrisme artériel intracrânien","Fibrillation atriale"],"0010","1 cause majeure : rupture d'anévrisme artériel intracrânien.","HSA"))
a(Q("N03","K138",2,"<b>Anévrisme</b> artériel — définition ?",
 ["Caillot dans une veine cérébrale","Communication anormale entre artère et veine","Rétrécissement d'une artère par une plaque","Petite poche formée sur une paroi artérielle fragilisée, qui peut se rompre"],"0001","Anévrisme : petite poche sur une paroi plus fragile, qui peut exploser.","HSA"))
a(Q("N04","K139",1,"Hémorragie méningée — <b>facteurs de risque</b> cités ?",
 ["Tabac","Hypertension artérielle","Fibrillation atriale","Hypoglycémie"],"1100","FR : tabac, HTA.","HSA"))
a(Q("N05","K140",2,"Hémorragie méningée — <b>terrain</b> ?",
 ["30-60 ans, femmes > hommes","Plus de 80 ans, hommes > femmes","Enfants de moins de 10 ans","20-30 ans, hommes > femmes"],"1000","Terrain : 30-60 ans, F > H.","HSA"))
a(Q("N06","K141",1,"Hémorragie méningée — <b>gravité</b> ?",
 ["Mortalité élevée","Séquelles neurologiques","Risque majeur de récidive hémorragique mortelle","Évolution bénigne dans la majorité des cas"],"1110","Gravité +++ : mortalité, séquelles ; 1 risque majeur : récidive hémorragique mortelle.","HSA"))
a(Q("N07","K142",2,"Hémorragie méningée — <b>céphalée typique</b> ?",
 ["Progressive sur plusieurs jours","Pulsatile, précédée d'une aura visuelle","Brutale, inhabituelle, explosive (« coup de tonnerre »)","Matinale, chronique"],"0010","Forme typique : céphalée brutale, inhabituelle, explosive.","HSA"))
a(Q("N08","K142",2,"Femme de 45 ans : céphalée brutale « la pire de sa vie », raideur de nuque, T° 37 °C. <b>Diagnostic à évoquer</b> ?",
 ["Migraine","Hémorragie méningée","Infarctus sylvien","Méningite bactérienne"],"0100","Céphalée en coup de tonnerre + syndrome méningé non fébrile = HSA jusqu'à preuve du contraire.","HSA"))
a(Q("N09","K142",0,"Hémorragie méningée — forme typique",
 ["Céphalée brutale explosive","Raideur de nuque","Fièvre élevée dès le début","Syndrome méningé non fébrile"],"1101","3. Faux : le syndrome méningé de l'HSA est non fébrile (≠ méningite).","HSA"))
a(Q("N10","K143",1,"Hémorragie méningée — <b>formes atypiques</b> ?",
 ["Agitation, confusion, coma","Présentation pseudo-psychiatrique","Atteinte douloureuse du III (mydriase, ptosis, diplopie)","Hémiplégie progressive sur plusieurs semaines"],"1110","Atypiques : agitation/confusion/coma, pseudo-psychiatrique, céphalées minimes (épistaxis méningé), III douloureux.","HSA"))
a(Q("N11","K144",2,"Hémorragie méningée — <b>examen de 1re intention</b> ?",
 ["IRM de diffusion seule","Ponction lombaire d'emblée","Scanner cérébral sans injection + angioscanner","EEG"],"0010","Scanner sans injection (hyperdensité dans les méninges) puis injection pour trouver l'anévrisme.","Diagnostic HSA"))
a(Q("N12","K144",2,"Hémorragie méningée — <b>aspect au scanner</b> sans injection ?",
 ["Hypodensité du parenchyme","Hyperdensité dans les espaces méningés","Toujours normal","Hypodensité des sinus veineux"],"0100","Hyperdensité (sang) dans les méninges.","Diagnostic HSA"))
a(Q("N13","K144",2,"Suspicion d'HSA, scanner normal — <b>examen indispensable</b> ?",
 ["IRM de diffusion","EEG","Écho-doppler des troncs supra-aortiques","Ponction lombaire"],"0001","Scanner négatif dans 10 % des cas → PL indispensable (sang = confirmation).","Diagnostic HSA"))
a(Q("N14","K144",2,"Hémorragie méningée — <b>proportion de scanners négatifs</b> ?",
 ["1 %","10 %","50 %","90 %"],"0100","Scanner négatif dans 10 % des cas.","Diagnostic HSA"))
a(Q("N15","K144",2,"Suspicion d'HSA avec scanner normal — <b>délai de la ponction lombaire</b> (note de cours) ?",
 ["Immédiatement","1 h après le début des symptômes","Environ 12 h après le début des symptômes","Après 7 jours"],"0010","Note : PL à 12 h du début des symptômes ; du sang confirme le diagnostic.","Diagnostic HSA"))
a(Q("N16","K145",1,"Hémorragie méningée avant traitement — <b>risques</b> ?",
 ["Dégradation neurologique rapide (coma, crise d'épilepsie)","Troubles neurovégétatifs (respiratoires, cardiovasculaires)","Récidive hémorragique","Transformation hémorragique d'un infarctus"],"1110","Transfert en neurochirurgie (SAMU), bilan pré-opératoire.","Prise en charge HSA"))
a(Q("N17","K145",2,"Hémorragie méningée — <b>exploration de l'anévrisme</b> ?",
 ["Artériographie des 4 axes (neuroradiologie interventionnelle)","Écho-doppler cervical","IRM FLAIR","Échographie cardiaque"],"1000","Artériographie des 4 axes.","Prise en charge HSA"))
a(Q("N18","K146",2,"Anévrisme rompu — <b>traitements</b> d'exclusion du sac ?",
 ["Thrombolyse ou thrombectomie","Endartériectomie ou stent carotidien","Embolisation par coils ou clip neurochirurgical","Craniectomie sous-occipitale ou dérivation"],"0010","Neuroradiologie : embolisation par coils ; neurochirurgie : clip.","Anévrisme"))
a(Q("N19","K146",2,"Anévrisme — <b>principe de l'embolisation par coils</b> ?",
 ["Remplir le sac anévrismal par voie endovasculaire pour l'exclure","Poser une pince au collet par voie chirurgicale","Dissoudre le caillot par un thrombolytique","Retirer l'hématome par craniotomie"],"1000","Coils : spires introduites par cathéter dans le sac. La pince au collet = clip neurochirurgical.","Anévrisme"))

# ---------- O. Thrombose veineuse cérébrale ----------
a(Q("O01","K147",2,"Thrombose veineuse cérébrale — <b>définition</b> ?",
 ["Occlusion d'une artère cérébrale","Occlusion d'une veine ou d'un sinus veineux cérébral","Rupture d'un anévrisme","Dissection d'une artère carotide"],"0100","TVC (« phlébite cérébrale ») : occlusion des veines ou sinus veineux.","TVC"))
a(Q("O02","K147",2,"Drainage veineux cérébral — <b>se fait vers</b> ?",
 ["La veine cave inférieure","Les veines jugulaires","La veine porte","Les artères vertébrales"],"0100","Les sinus veineux se drainent dans les veines jugulaires.","TVC"))
a(Q("O03","K148",2,"Thrombose veineuse cérébrale — <b>localisation la plus fréquente</b> (schéma du cours) ?",
 ["Sinus caverneux","Veines profondes","Sinus latéral","Sinus droit"],"0010","Schéma : sinus latéral 73 %, sinus sagittal supérieur 62-65 %, veines corticales 17-21 %, sinus droit 11-18 %, veines profondes 7-11 %, sinus caverneux 2 %.","TVC"))
a(Q("O04","K148",2,"Thrombose veineuse cérébrale — <b>atteinte de plusieurs sinus et veines</b> ?",
 ["2 %","10 %","50-60 %","95 %"],"0010","Multiples sinus et veines : 50-60 % ; pas de syndrome anatomo-clinique bien défini.","TVC"))
a(Q("O05","K149",1,"Thrombose veineuse cérébrale — <b>causes gynéco-obstétricales</b> ?",
 ["Grossesse","Post-partum","Contraception","Ménopause"],"1110","Grossesse, post-partum, ± contraception.","Causes TVC"))
a(Q("O06","K149",1,"Thrombose veineuse cérébrale — <b>autres causes</b> ?",
 ["Thrombophilies (coagulopathies héréditaires)","Maladies de système (lupus, Behçet)","Cancers","HTA chronique"],"1110","Causes de phlébites, gynéco, loco-régionales, infectieuses (rares).","Causes TVC"))
a(Q("O07","K149",2,"Thrombose veineuse cérébrale — <b>situation étiologique la plus fréquente</b> ?",
 ["Cause infectieuse","Cancer","Idiopathique (aucune cause retrouvée)","Grossesse"],"0010","Idiopathique le plus souvent ; les causes infectieuses ne se voient presque plus.","Causes TVC"))
a(Q("O08","K150",2,"Thrombose veineuse cérébrale — <b>3 types de symptômes</b> ?",
 ["Fièvre ; purpura ; raideur de nuque","HTIC ; signes focaux ; crises d'épilepsie","HTIC ; aphasie isolée ; fièvre","Syndrome méningé ; cécité monoculaire ; vertige"],"0100","HTIC (céphalées, nausées/vomissements, vigilance, diplopie), signes focaux, épilepsie.","Clinique TVC"))
a(Q("O09","K150",2,"Thrombose veineuse cérébrale — <b>mode d'installation</b> ?",
 ["Toujours brutal, en quelques secondes","Souvent subaigu, sur quelques jours","Sur plusieurs années","Uniquement la nuit"],"0100","Souvent subaigu (parfois très brutal, parfois sur quelques semaines) : moins brutal que l'AVC artériel.","Clinique TVC"))
a(Q("O10","K150",1,"Thrombose veineuse cérébrale — <b>signes d'HTIC</b> ?",
 ["Céphalées aiguës","Nausées, vomissements","Diplopie (VI)","Hyperthermie"],"1110","HTIC : céphalées, nausées/vomissements, altération de la vigilance, diplopie.","Clinique TVC"))
a(Q("O11","K151",1,"Thrombose veineuse cérébrale — <b>gravité</b> ?",
 ["HTIC","Mortalité","Cécité","Surdité"],"1110","Gravité : HTIC, mortalité, cécité.","Clinique TVC"))
a(Q("O12","K152",2,"Thrombose veineuse cérébrale — <b>diagnostic</b> ?",
 ["Scanner sans injection seul","EEG","Neuro-imagerie des veines : IRM-ARM ou TDM avec injection","Échographie cardiaque"],"0010","Séquences spécifiques pour les veines : IRM-ARM ou TDM avec injection.","Diagnostic TVC"))
a(Q("O13","K153",2,"Thrombose veineuse cérébrale — <b>traitement antithrombotique</b> ?",
 ["Aspirine seule à vie","Héparine puis AVK pendant 6 mois","Thrombolyse IV puis aucun traitement","AVK pendant 1 semaine"],"0100","Héparine puis AVK (6 mois).","Traitement TVC"))
a(Q("O14","K153",1,"Thrombose veineuse cérébrale — <b>traitements étiologique et symptomatique</b> ?",
 ["Arrêt de la contraception orale","Traitement de l'épilepsie","Traitement de l'HTIC et des céphalées","Thrombectomie systématique"],"1110","Étiologique (infections, maladies générales, arrêt CO) ; symptomatique (épilepsie, HIC, céphalée).","Traitement TVC"))
