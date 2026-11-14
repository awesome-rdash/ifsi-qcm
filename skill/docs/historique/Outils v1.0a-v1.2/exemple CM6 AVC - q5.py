# Questions de vocabulaire : termes employés dans le cours sans y être définis.
# Distracteurs = définitions de termes proches.
from common import Q
QS = []
a = QS.append
HC = "Complément : définition hors cours (le terme est employé dans le cours sans y être défini)."
a(Q("V01","V01",2,"<b>Athérome</b> — définition ?",
 ["Plaque de dépôts lipidiques dans la paroi interne d'une artère","Caillot sanguin formé dans un vaisseau","Élément circulant qui obstrue un vaisseau à distance","Dilatation localisée de la paroi d'une artère"],"1000",
 "Athérome = plaque lipidique de la paroi artérielle. Caillot formé sur place = thrombus ; élément circulant = embole ; dilatation = anévrisme.","Athérome",x=HC))
a(Q("V02","V02",2,"<b>Thrombus</b> — définition ?",
 ["Plaque de dépôts lipidiques dans la paroi d'une artère","Caillot sanguin formé dans un vaisseau ou une cavité cardiaque","Collection de sang hors des vaisseaux, dans un tissu","Élément circulant qui obstrue un vaisseau à distance"],"0100",
 "Thrombus = caillot formé sur place. S'il se détache et migre, il devient un embole. Sang hors des vaisseaux = hématome.","Thrombus",x=HC))
a(Q("V03","V03",2,"<b>Embolie</b> — définition ?",
 ["Formation d'un caillot sur place dans un vaisseau","Rétrécissement du calibre d'une artère","Obstruction d'un vaisseau par un élément circulant venu d'ailleurs (embole)","Rupture de la paroi d'une artère"],"0010",
 "Embolie = obstruction par un embole venu d'ailleurs (ex. caillot de l'oreillette en cas de FA). Caillot sur place = thrombose ; rétrécissement = sténose.","Embolie",x=HC))
a(Q("V04","V02 V03",2,"Caillot formé dans l'oreillette au cours d'une FA, qui migre et bouche une artère cérébrale. <b>Mécanisme</b> ?",
 ["Thrombose in situ de l'artère cérébrale","Embolie (cardio-embolie)","Sténose athéromateuse","Dissection artérielle"],"0100",
 "Le caillot (thrombus) se forme dans le cœur puis migre (embole) : c'est une embolie d'origine cardiaque.","Embolie",x=HC))
a(Q("V05","V04",2,"<b>Lacune</b> (infarctus lacunaire) — définition ?",
 ["Grand infarctus de tout le territoire d'une artère cérébrale","Petit infarctus profond par occlusion d'une petite artère perforante","Petite hémorragie profonde","Dilatation des ventricules cérébraux"],"0100",
 "Lacune : petit infarctus profond (classiquement < 15 mm) lié à la maladie des petites artères. Dilatation des ventricules = hydrocéphalie.","Lacune",x=HC))
a(Q("V06","V05",2,"<b>Sténose</b> artérielle — définition ?",
 ["Rétrécissement du calibre d'une artère","Obstruction complète d'une artère","Dilatation localisée d'une artère","Déchirure de la paroi d'une artère"],"1000",
 "Sténose = rétrécissement ; occlusion = obstruction complète ; anévrisme = dilatation ; dissection = déchirure de la paroi.","Sténose",x=HC))
a(Q("V07","V06",2,"<b>Endartériectomie</b> — définition ?",
 ["Retrait du caillot par cathéter","Ablation chirurgicale de la plaque d'athérome après ouverture de l'artère","Pose d'une pince au collet d'un anévrisme","Ouverture d'une partie de la boîte crânienne"],"0100",
 "Endartériectomie = chirurgie de la plaque (sténose carotidienne sévère). Cathéter = thrombectomie ; pince = clip ; ouverture du crâne = craniectomie.","Endartériectomie",x=HC))
a(Q("V08","V07",2,"<b>HTIC</b> — définition ?",
 ["Hypertension artérielle sévère avec atteinte d'organe","Augmentation de la pression à l'intérieur de la boîte crânienne","Augmentation de la pression à l'intérieur de l'œil","Augmentation de la pression dans les veines jugulaires"],"0100",
 "HTIC = hypertension intracrânienne (céphalées, vomissements, troubles de la vigilance). HTA sévère avec atteinte d'organe = HTA maligne ; pression oculaire = glaucome.","HTIC",x=HC))
a(Q("V09","V08",2,"<b>Hydrocéphalie</b> — définition ?",
 ["Accumulation d'eau dans le tissu cérébral","Accumulation de LCR avec dilatation des ventricules cérébraux","Collection de sang entre la dure-mère et le cerveau","Présence de sang dans les espaces sous-arachnoïdiens"],"0100",
 "Hydrocéphalie = trop de LCR dans les ventricules. Eau dans le tissu = œdème cérébral ; sang sous-arachnoïdien = hémorragie méningée.","Hydrocéphalie",x=HC))
a(Q("V10","V09",2,"<b>Œdème cérébral</b> — définition ?",
 ["Accumulation d'eau dans le tissu cérébral","Accumulation de LCR dans les ventricules","Collection de sang dans le parenchyme","Zone de tissu cérébral nécrosé"],"1000",
 "Œdème = eau dans le tissu (gonflement) ; LCR dans les ventricules = hydrocéphalie ; sang = hématome ; nécrose = infarctus.","Œdème",x=HC))
a(Q("V11","V10",2,"<b>Apraxie</b> — définition ?",
 ["Trouble de la coordination des mouvements","Paralysie partielle d'un membre","Incapacité à réaliser des gestes volontaires malgré une motricité conservée","Trouble du langage"],"0010",
 "Apraxie : on ne sait plus « faire le geste » alors que la force est là. Coordination = ataxie ; paralysie partielle = parésie ; langage = aphasie.","Apraxie",x=HC))
a(Q("V12","V11",2,"<b>Négligence</b> (héminégligence) — définition ?",
 ["Perte de la même moitié du champ visuel des deux yeux","Défaut de prise en compte d'une moitié de l'espace et du corps, non expliqué par un déficit moteur ou visuel","Perte de la sensibilité d'un hémicorps","Paralysie d'un hémicorps"],"0100",
 "Négligence (souvent gauche, atteinte de l'hémisphère droit) : le patient « ignore » un côté. Moitié du champ visuel = HLH ; sensibilité = hypoesthésie ; paralysie = hémiplégie.","Négligence",x=HC))
a(Q("V13","V12",2,"<b>Diplopie</b> — définition ?",
 ["Vision floue d'un œil","Vision double","Perte de la moitié du champ visuel","Perte totale de la vision d'un œil"],"0100",
 "Diplopie = vision double. Moitié du champ visuel = hémianopsie ; perte d'un œil = cécité monoculaire.","Diplopie",x=HC))
a(Q("V14","V13",2,"<b>Ptosis ; myosis ; énophtalmie</b> — définitions dans l'ordre ?",
 ["Chute de la paupière supérieure ; pupille rétrécie ; œil enfoncé dans l'orbite","Chute de la paupière supérieure ; pupille dilatée ; œil saillant","Pupille rétrécie ; chute de la paupière ; œil saillant","Paupière rétractée ; pupille dilatée ; œil enfoncé"],"1000",
 "Ptosis = paupière qui tombe ; myosis = petite pupille (≠ mydriase) ; énophtalmie = œil enfoncé (≠ exophtalmie). Triade du Claude Bernard-Horner.","CBH",x=HC))
a(Q("V15","V14",2,"<b>Mydriase</b> — définition ?",
 ["Rétrécissement de la pupille","Dilatation de la pupille","Chute de la paupière supérieure","Inégalité de taille entre les deux pupilles"],"0100",
 "Mydriase = pupille dilatée ; myosis = pupille rétrécie ; ptosis = paupière qui tombe ; anisocorie = pupilles inégales.","Mydriase",x=HC))
a(Q("V16","V15",2,"<b>Spasticité</b> — définition ?",
 ["Paralysie avec perte du tonus musculaire (flasque)","Raideur par augmentation du tonus, accrue à l'étirement rapide du muscle","Raccourcissement fixé d'un tendon","Tremblement au repos"],"0100",
 "Spasticité = hypertonie qui augmente avec la vitesse d'étirement. Paralysie flasque = perte du tonus ; raccourcissement fixé = rétraction tendineuse.","Spasticité",x=HC))
a(Q("V17","V16",2,"<b>Algoneurodystrophie</b> — définition ?",
 ["Syndrome douloureux régional complexe : douleur, troubles vasomoteurs et raideur d'un membre","Infection d'une articulation","Fonte musculaire liée à l'immobilisation","Raccourcissement fixé d'un tendon"],"1000",
 "Algoneurodystrophie (SDRC) : douleur, œdème, troubles vasomoteurs et raideur (souvent épaule-main après AVC). Fonte musculaire = amyotrophie ; tendon raccourci = rétraction.","Algoneurodystrophie",x=HC))
a(Q("V18","V17",2,"<b>Thrombophilie</b> — définition ?",
 ["Tendance aux saignements","Diminution du nombre de plaquettes","Tendance, héréditaire ou acquise, à faire des thromboses","Augmentation du nombre de plaquettes"],"0010",
 "Thrombophilie = tendance à coaguler (thromboses). Tendance aux saignements = diathèse hémorragique ; plaquettes basses = thrombopénie ; élevées = thrombocytose.","Thrombophilie",x=HC))
a(Q("V19","V18",2,"<b>Thrombopénie</b> — définition ?",
 ["Diminution du nombre de plaquettes","Augmentation du nombre de plaquettes","Diminution de l'hémoglobine","Tendance à faire des thromboses"],"1000",
 "Thrombopénie = plaquettes basses (contre-indication à la thrombolyse). Plaquettes élevées = thrombocytose ; hémoglobine basse = anémie ; tendance aux thromboses = thrombophilie.","Thrombopénie",x=HC))
a(Q("V20","V19",2,"<b>Hématome</b> — définition ?",
 ["Caillot formé à l'intérieur d'un vaisseau","Collection de sang hors des vaisseaux, dans un tissu","Dilatation localisée d'une artère","Accumulation d'eau dans un tissu"],"0100",
 "Hématome = sang sorti des vaisseaux et collecté dans un tissu (ex. hématome intraparenchymateux). Caillot dans un vaisseau = thrombus ; dilatation = anévrisme ; eau = œdème.","Hématome",x=HC))
