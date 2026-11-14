from common import Q
QS = []
a = QS.append
NIHSS_X="✎ Modifié par rapport au cours : la note de cours donnait « 0-5 mineur, 5-15 moyen, ≥ 15 sévère » (bornes qui se chevauchent, « pas à connaître par cœur ») → échelle de référence : 0 pas de symptôme, 1-4 mineur, 5-15 modéré, 16-20 modéré à sévère, 21-42 sévère."
NIHSS_W=["Web — WikEM, NIH Stroke Scale (FR), https://wikem.org/wiki/NIH_Stroke_Scale/fr"]

# ---------- Symptômes ----------
a(Q("D01","K037",1,"Signes d'alerte de survenue brutale ?",
 ["Difficulté à parler","Faiblesse d'une moitié du corps","Douleur thoracique constrictive","Toux fébrile"],"1100",
 "Cours p. 8 : parole, moitié du corps, vision, équilibre, céphalée soudaine violente. La douleur thoracique évoque un syndrome coronarien.","Signes d'alerte"))
a(Q("D02","K037",0,"Apparu brutalement, est-ce un signe d'alerte ? (vrai ou faux)",
 ["Trouble de la vision","Trouble de l'équilibre","Mal de tête soudain et violent","Douleur abdominale"],"1110",
 "Cours p. 8 : vision, équilibre et céphalée soudaine violente font partie des signes d'alerte.","Signes d'alerte"))
a(Q("D03","K037",2,"En poste de secours, un homme de 60 ans présente brutalement une bouche déviée et ne peut plus lever le bras droit. Conduite ?",
 ["Appeler le 15 immédiatement","Lui conseiller de voir son médecin dans la journée","Lui donner de l'aspirine et attendre","L'allonger et le réévaluer dans une heure"],"1000",
 "Cours p. 8 : signes d'alerte → urgence, appel du 15.","Signes d'alerte",
 dz={2:"antiagrégant avant l'imagerie : risque d'aggraver une hémorragie",3:"perte de temps : « time is brain »"},vign=True))
a(Q("D04","K038",2,"<u>Hémiplégie</u> et <u>hémiparésie</u> : définitions ?",
 ["Hémiplégie = paralysie complète d'un hémicorps ; hémiparésie = partielle","Hémiplégie = paralysie partielle d'un hémicorps ; hémiparésie = complète","Hémiplégie = paralysie d'un hémicorps ; hémiparésie = perte de sensibilité","Hémiplégie = paralysie des deux jambes ; hémiparésie = d'un hémicorps"],"1000",
 "Cours p. 8 : hémiplégie = paralysie complète ; hémiparésie = paralysie partielle (face, MS, MI).","Vocabulaire moteur"))
a(Q("D05","K038",2,"Mme L. bouge son bras et sa jambe droits, mais avec une force nettement diminuée. Terme exact ?",
 ["Hémiparésie droite","Hémiplégie droite","Paraparésie","Hypoesthésie droite"],"1000","Déficit moteur partiel d'un hémicorps = hémiparésie (p. 8).","Vocabulaire moteur",vign=True))
a(Q("D06","K038",2,"M. N. ne peut plus du tout bouger le bras ni la jambe gauches. Terme exact ?",
 ["Hémiparésie gauche","Hémiplégie gauche","Monoplégie gauche","Paraplégie"],"0100","Paralysie complète d'un hémicorps = hémiplégie (p. 8).","Vocabulaire moteur",vign=True))
a(Q("D07","K039",2,"Définition des <u>paresthésies</u> ?",
 ["Fourmillements, picotements","Perte totale de la sensibilité","Diminution de la sensibilité","Sensibilité exagérée au toucher"],"1000","Cours p. 8 : paresthésies = fourmillements ; hypoesthésie = diminution ; anesthésie = perte totale.","Vocabulaire sensitif"))
a(Q("D08","K039",2,"Définition de l'<u>hypoesthésie</u> ?",
 ["Fourmillements, picotements","Perte totale de la sensibilité","Diminution de la sensibilité","Sensibilité exagérée au toucher"],"0010","Hypoesthésie = diminution ; anesthésie = perte totale.","Vocabulaire sensitif"))
a(Q("D09","K040",2,"<u>Aphasie</u> et <u>dysarthrie</u> : définitions ?",
 ["Aphasie = trouble du langage ; dysarthrie = trouble de l'articulation","Aphasie = trouble de l'articulation ; dysarthrie = trouble du langage","Aphasie = trouble du langage ; dysarthrie = trouble de la déglutition","Aphasie = perte de la voix ; dysarthrie = trouble de l'articulation"],"1000",
 "Cours p. 9 : aphasie = langage (hémisphère dominant) ; dysarthrie = articulation, souvent avec un déficit moteur.","Langage et parole"))
a(Q("D10","K040",2,"M. S. articule mal, sa parole est « pâteuse », mais ses phrases sont correctes et il comprend tout. Trouble ?",
 ["Aphasie de compréhension","Aphasie d'expression","Dysarthrie","Apraxie"],"0010","Langage normal, articulation altérée = dysarthrie (p. 9).","Langage et parole",vign=True))
a(Q("D11","K040",1,"Manifestations d'une <u>aphasie</u> décrites dans le cours ?",
 ["Perte de la compréhension","Mutisme","Jargon","Voix nasonnée"],"1110","Cours p. 9 : perte de compréhension, mutisme, jargon. La voix nasonnée relève de l'articulation.","Langage et parole"))
a(Q("D12","K041",0,"Trouble de l'équilibre d'origine vasculaire : vrai ou faux ?",
 ["Perte soudaine de l'équilibre, avec ou sans vertiges","Démarche ébrieuse (ataxie)","Perte de la moitié du champ visuel","Incoordination des membres"],"1101","Cours p. 9 ; la perte de la moitié du champ visuel est une hémianopsie (trouble visuel).","Équilibre"))
a(Q("D13","K041",2,"Définition de l'<u>ataxie</u> ?",
 ["Trouble de la coordination des mouvements","Incapacité à réaliser un geste appris","Paralysie partielle d'un membre","Trouble du langage"],"1000","Ataxie = incoordination. Geste appris impossible = apraxie ; paralysie partielle = parésie ; langage = aphasie.","Équilibre"))
a(Q("D14","K042",2,"Mme M. perd brutalement la vue de l'œil droit pendant quelques minutes. Artère en cause ?",
 ["Artère ophtalmique","Artère cérébrale postérieure","Tronc basilaire","Artère cérébrale antérieure"],"1000","Cours p. 9 : cécité monoculaire = artère ophtalmique (branche de la carotide interne) ou rétine.","Troubles visuels",vign=True))
a(Q("D15","K043",2,"M. R. ne voit plus la moitié gauche de l'espace, avec ses deux yeux. Terme exact ?",
 ["Hémianopsie latérale homonyme gauche","Cécité monoculaire gauche","Diplopie","Négligence gauche"],"1000",
 "Cours p. 9 : hémianopsie latérale homonyme = moitié du champ visuel amputée, du même côté pour les deux yeux.","Troubles visuels",vign=True))
a(Q("D16","K044",2,"Mme D. voit double depuis ce matin. Origine la plus probable dans un contexte vasculaire ?",
 ["Nerfs crâniens oculomoteurs","Lobe frontal","Rétine","Lobe temporal"],"1000","Cours p. 9 : diplopie = atteinte des nerfs crâniens oculomoteurs.","Troubles visuels",vign=True))

# ---------- Évaluation clinique ----------
a(Q("D17","K045",0,"Élément à évaluer en premier : vrai ou faux ?",
 ["Vigilance et pupilles","Constantes et glycémie capillaire","Respiration, encombrement, fausses routes","Ponction lombaire"],"1110","Cours p. 9 : neurologique (gravité, déficit), constantes + glycémie capillaire, respiration.","Examen initial"))
a(Q("D18","K046",2,"Pourquoi faire la glycémie capillaire en priorité ?",
 ["Une hypoglycémie peut mimer un déficit neurologique","Une hyperglycémie contre-indique l'imagerie","La glycémie entre dans le calcul du NIHSS","La glycémie fixe la dose du thrombolytique"],"1000","Cours p. 9 : glycémie capillaire en priorité, car une hypoglycémie peut donner le même tableau.","Examen initial"))
a(Q("D19","K046",2,"Mme T., diabétique sous insuline, hémiparésie droite brutale ; glycémie capillaire 0,40 g/L. Conduite ?",
 ["Resucrer puis réévaluer le déficit","Transférer sans corriger la glycémie","Faire l'injection d'insuline prévue","Attendre la régression spontanée du déficit"],"1000",
 "Cours p. 9 : une hypoglycémie peut mimer un accident vasculaire → la corriger et réévaluer (sans retarder la filière si le déficit persiste).","Examen initial",
 dz={2:"l'insuline aggrave l'hypoglycémie"},vign=True))
a(Q("D20","K047",2,"Étendue du score NIHSS ?",
 ["0 à 24","0 à 36","0 à 42","0 à 48"],"0010","Cours p. 10 : NIHSS de 0 à 42 (le Glasgow va de 3 à 15).","NIHSS"))
a(Q("D21","K047",1,"Utilisations du NIHSS ?",
 ["Mesurer la sévérité à l'entrée","Suivre l'évolution chaque jour","Distinguer ischémie et hémorragie","Remplacer l'imagerie si le score est faible"],"1100","Cours p. 10 : sévérité initiale puis suivi quotidien. Seule l'imagerie distingue ischémie et hémorragie.","NIHSS"))
a(Q("D22","K047",2,"Un NIHSS élevé signifie ?",
 ["Un déficit plus sévère","Un meilleur état neurologique","Une hémorragie probable","Une meilleure vigilance"],"1000","Plus le score est élevé, plus le déficit est sévère.","NIHSS"))
a(Q("D23","K048",1,"Items évalués par le NIHSS ?",
 ["Conscience et orientation","Champ visuel","Paralysie faciale","Glycémie capillaire"],"1110","Cours p. 10 : la glycémie n'est pas un item.","NIHSS"))
a(Q("D24","K048",0,"Item du NIHSS : vrai ou faux ?",
 ["Dysarthrie","Réflexes ostéotendineux","Aphasie","Fréquence cardiaque"],"1010","Cours p. 10 : dysarthrie, aphasie, extinction et négligence sont des items ; pas les réflexes ni les constantes.","NIHSS"))
a(Q("D25","K048",2,"NIHSS : durée de maintien demandée au membre <u>supérieur</u> ?",
 ["5 secondes","10 secondes","15 secondes","20 secondes"],"0100","Cours p. 10 : membre supérieur 10 s ; membre inférieur 5 s.","NIHSS"))
a(Q("D26","K048",2,"NIHSS : durée de maintien demandée au membre <u>inférieur</u> ?",
 ["5 secondes","10 secondes","15 secondes","20 secondes"],"1000","Membre inférieur 5 s ; membre supérieur 10 s.","NIHSS"))
a(Q("D27","K049",2,"NIHSS de <u>1 à 4</u> : sévérité ?",
 ["Mineur","Modéré","Modéré à sévère","Sévère"],"1000","1-4 : mineur.","NIHSS",x=NIHSS_X,w=NIHSS_W))
a(Q("D28","K049",2,"NIHSS de <u>5 à 15</u> : sévérité ?",
 ["Mineur","Modéré","Modéré à sévère","Sévère"],"0100","5-15 : modéré.","NIHSS",x=NIHSS_X,w=NIHSS_W))
a(Q("D29","K049",2,"NIHSS de <u>21 à 42</u> : sévérité ?",
 ["Mineur","Modéré","Modéré à sévère","Sévère"],"0001","21-42 : sévère (16-20 : modéré à sévère).","NIHSS",x=NIHSS_X,w=NIHSS_W))

# ---------- Alerte thrombolyse ----------
a(Q("E01","K050",2,"Que signifie « time is brain » ?",
 ["Chaque minute de retard détruit des neurones de façon irréversible","Chaque minute de retard augmente le risque d'hémorragie méningée","Chaque minute de retard rend l'imagerie moins fiable","Chaque minute de retard fausse le score NIHSS"],"1000","Cours p. 10 : chaque seconde compte, la perte neuronale est irréversible.","Urgence"))
a(Q("E02","K051",2,"Question fondamentale à poser au patient ou aux témoins ?",
 ["Heure de début des symptômes","Heure du dernier repas","Date du dernier bilan sanguin","Antécédents familiaux"],"1000","Cours p. 11 : l'heure de début des symptômes conditionne la reperfusion.","Heure de début"))
a(Q("E03","K051",2,"Pourquoi l'heure de début des symptômes est-elle capitale ?",
 ["Elle conditionne l'accès aux traitements de reperfusion","Elle permet de distinguer ischémie et hémorragie","Elle détermine le score NIHSS","Elle détermine le choix entre IRM et scanner"],"1000","Thrombolyse < 4h30, thrombectomie jusqu'à 6-24 h : sans heure de début, pas de décision de reperfusion.","Heure de début",allow=["heure","début","symptômes"]))
a(Q("E04","K052 K053",0,"Mesure prise à l'arrivée du patient : vrai ou faux ?",
 ["Pose de 2 voies veineuses périphériques","Bilan sanguin en urgence","ECG","Sondage urinaire à demeure"],"1110","Cours p. 10-11 : 2 VVP, bilan, ECG. Pas de sondage systématique (p. 18 : dépister un globe).","Accueil"))
a(Q("E05","K053",1,"Examens du bilan biologique d'urgence ?",
 ["NFS-plaquettes","TP-TCA","D-dimères","Lipasémie"],"1100","Cours p. 11 : NFS-plaquettes, TP-TCA (INR si AVK), fibrinogène, glycémie, βHCG, groupe-RAI, iono-urée-créatinine.","Bilan d'urgence"))
a(Q("E06","K053",0,"Prélèvement à réaliser en urgence : vrai ou faux ?",
 ["βHCG chez la femme jeune","Groupe sanguin, Rhésus, RAI","Hémocultures","Ionogramme, urée, créatinine"],"1101","Les hémocultures ne font pas partie du bilan d'alerte.","Bilan d'urgence"))
a(Q("E07","K053",2,"M. U., 74 ans, en fibrillation atriale sous antivitamine K, arrive pour un déficit brutal. Examen à ajouter au bilan sanguin ?",
 ["INR","Troponine","Anti-Xa","D-dimères"],"1000","Cours p. 11 : INR si traitement par AVK (un anticoagulant efficace contre-indique la thrombolyse, p. 14).","Bilan d'urgence",vign=True))
a(Q("E08","K054",2,"Orientation du patient à son arrivée ?",
 ["Transfert direct en radiologie pour l'imagerie","Passage par le box d'urgences pour un bilan complet","Hospitalisation directe en cardiologie","Admission en neurologie pour observation"],"1000","Cours p. 10 : transfert direct en radiologie (IRM-ARM +++, ou scanner).","Accueil"))
a(Q("E09","K055",0,"Évaluation par l'équipe UNV : vrai ou faux ?",
 ["Interrogatoire : antécédents, traitements, allergies","Constantes : TA, FC, glycémie","Score NIHSS","Électroencéphalogramme"],"1110","Cours p. 11 : interrogatoire, constantes (TA +++), NIHSS.","Accueil"))
a(Q("E10","K056",2,"Trois critères du choix du traitement ?",
 ["Heure ; sévérité ; terrain","Heure ; âge ; sexe","Sévérité ; poids ; groupe sanguin","Terrain ; température ; taille"],"1000","Cours p. 11 : selon l'heure, la sévérité et le terrain.","Décision"))
a(Q("E11","K057 K079",0,"Filière de soins : vrai ou faux ?",
 ["L'amont comprend SAMU, pompiers et urgences","Le patient est hospitalisé en UNV ou USINV","L'aval comprend les SSR","La rééducation commence après la sortie d'UNV"],"1110","Cours p. 11 et 15 : la rééducation commence dès le départ en UNV.","Filière"))
a(Q("E12","K058",2,"Hospitalisation en UNV : réduction de la <u>mortalité</u> selon la note de cours ?",
 ["10 %","15 %","20 %","25 %"],"0010","Note p. 11 : −20 % de mortalité. (Diapo p. 15 : −30 % de mortalité et handicap, autre critère.)","Filière"))

# ---------- Imagerie ----------
a(Q("F01","K060",2,"Examen de référence ?",
 ["Scanner sans injection","IRM cérébrale","Écho-doppler cervical","Radiographie du crâne"],"0100","Cours p. 12 : IRM ++++ > scanner.","Choix de l'examen"))
a(Q("F02","K061",2,"Séquence IRM la plus précocement positive dans l'infarctus ?",
 ["FLAIR","T2*","Diffusion","Angio-IRM"],"0010","Cours p. 12 : la diffusion est la plus rapidement positive.","Séquences"))
a(Q("F03","K061",2,"Aspect d'un infarctus récent en <u>diffusion</u> ?",
 ["Hyposignal (noir)","Hypersignal (blanc)","Normal pendant 24 h","Hyperdensité"],"0100","Infarctus récent : hypersignal (blanc) en diffusion. « Densité » = scanner.","Séquences"))
a(Q("F04","K062",2,"Délai à partir duquel l'infarctus devient visible en <u>FLAIR</u> ?",
 ["Environ 3 h","Environ 4h30","Environ 6 h","Environ 9 h"],"0100","Cours p. 12 : hypersignal FLAIR à partir d'environ 4h30.","Séquences"))
a(Q("F05","K062",2,"M. V. est découvert au réveil avec une hémiplégie (heure de début inconnue). IRM : hypersignal en diffusion, FLAIR normale. Interprétation ?",
 ["Infarctus probablement de moins de 4h30","Infarctus de plus de 4h30, trop tard","Hémorragie intracérébrale","AIT sans lésion"],"1000","Cours p. 12 : diffusion positive + FLAIR négative = infarctus récent, probablement < 4h30.","Séquences",vign=True))
a(Q("F06","K063",2,"Aspect d'une hémorragie intracérébrale ?",
 ["Scanner : hyperdensité ; IRM T2* : hyposignal","Scanner : hypodensité ; IRM T2* : hypersignal","Scanner : hyperdensité ; IRM T2* : hypersignal","Scanner : hypodensité ; IRM T2* : hyposignal"],"1000","Cours p. 12 : hémorragie blanche au scanner, noire en T2*.","Hémorragie"))
a(Q("F07","K064",2,"Mme W., déficit brutal ; scanner sans injection normal. Ce que cela permet de dire ?",
 ["Pas d'hémorragie : thrombolyse possible si délai < 4h30","Pas d'accident vasculaire","Accident de moins de 4h30 de façon certaine","Hémorragie méningée définitivement exclue"],"1000",
 "Le scanner élimine l'hémorragie mais ne date pas l'infarctus (souvent invisible au début) ; le délai vient de l'heure de début. Le scanner est négatif dans 10 % des hémorragies méningées (p. 26).","Scanner",
 x="✎ Modifié par rapport au cours : la note « si on voit rien au scanner ça veut dire < 4h30 » est inexacte → un scanner normal élimine une hémorragie ; le délai se juge sur l'heure de début des symptômes (diapo : « traiter par rt-PA si < 4h30 »).",vign=True))
a(Q("F08","K064",2,"Comment voir l'occlusion artérielle au scanner ?",
 ["Sans injection","Avec injection (angioscanner)","Par une séquence de diffusion","Par une radiographie standard"],"0100","Cours p. 13 : séquence injectée (angioTDM) pour voir les vaisseaux.","Scanner"))
a(Q("F09","K065",2,"Séquence IRM qui montre l'occlusion du polygone de Willis ?",
 ["Diffusion","FLAIR","T2*","Angio-IRM (ARM)"],"0001","Cours p. 12 : l'ARM visualise l'occlusion.","Séquences"))
a(Q("F10","K060 K061",2,"Même patient, hémiplégie gauche depuis 4 h : scanner (à gauche), FLAIR (au centre), diffusion (à droite). Que montre la comparaison ?",
 ["La diffusion montre l'infarctus, le scanner est quasi normal","Le scanner montre mieux l'infarctus que l'IRM","Les trois examens sont normaux","Une hémorragie est visible sur les trois coupes"],"1000",
 "IRM >> scanner à la phase aiguë : la diffusion est la plus précoce (hypersignal), le scanner souvent normal au début.","Clichés",img=(79,(52,172,1070,515),"img-tdm-flair-dwi"),vign=True))
a(Q("F11","K061",2,"IRM de diffusion d'un patient avec hémiplégie gauche brutale. La large zone blanche correspond à ?",
 ["Une hémorragie","Un aspect normal","Un infarctus récent","Un œdème tumoral"],"0010","Hypersignal en diffusion = infarctus récent ; une hémorragie est en hyposignal en T2*.","Clichés",img=(79,(727,172,1070,515),"img-dwi"),vign=True))
a(Q("F12","K065",2,"Angio-IRM d'un patient avec infarctus aigu. La flèche montre ?",
 ["Un anévrisme","Une malformation artério-veineuse","Une artère occluse","Un saignement actif"],"0010","ARM : l'artère occluse n'apparaît pas (diapo : occlusion artérielle dans 80 % des cas).","Clichés",img=(79,(785,527,1088,735),"img-arm")))
a(Q("F13","K063 K123",2,"Scanner <u>sans injection</u>, hémiplégie brutale. Interprétation ?",
 ["Hématome intraparenchymateux","Infarctus constitué","Scanner normal","Hémorragie méningée isolée"],"1000","Hyperdensité spontanée au scanner sans injection = hémorragie → pas de thrombolyse.","Clichés",img=(145,(72,290,365,640),"img-tdm-hematome"),pg=[23],vign=True))
a(Q("F14","K063",2,"IRM <u>T2*</u> d'un patient avec hématome. La zone noire correspond à ?",
 ["Un infarctus récent","Du liquide céphalorachidien","L'hémorragie","Un artefact"],"0010","T2* : hémorragie en hyposignal (noir).","Clichés",img=(145,(757,370,1045,705),"img-t2-hematome"),pg=[23]))
a(Q("F15","K064 K068",2,"Déficit brutal depuis 2 h, aucune contre-indication connue. Scanner sans injection ci-dessous. Conduite ?",
 ["Pas de saignement : thrombolyse IV possible","Hémorragie : pas de thrombolyse","Attendre une IRM à J1 avant de décider","Aspirine seule, sans thrombolyse"],"1000",
 "Scanner sans sang + délai < 4h30 + pas de CI → thrombolyse (± angioTDM à la recherche d'une occlusion proximale).","Clichés",img=(84,(462,250,640,515),"img-tdm-normal"),vign=True))
