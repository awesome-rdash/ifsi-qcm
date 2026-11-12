# Glossaire : (terme, motif regex, définition courte, sources). Règle X3 : un terme, une définition, une ligne ; chaque définition est sourcée
# (page du cours qui la donne et/ou source fiable en ligne, avec URL).
import re
G = [
("AIC", r"\bAIC\b", "Accident ischémique cérébral : infarctus cérébral ou AIT.", [("HPSJ, livret AVC", 'https://www.hpsj.fr/storage/2015/01/Livret_AVC_patient2024.pdf')]),
("AIT", r"\bAIT\b", "Accident ischémique transitoire : occlusion artérielle temporaire, déficit bref (< 1 h) sans lésion visible.", [("CM6 AVC, p. 2", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Algoneurodystrophie", r"algoneurodystrophie", "Autre nom de l'algodystrophie (syndrome douloureux régional complexe de type 1) : douleur durable d'un membre, sans lésion d'un nerf.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8450192/syndrome-douloureux-regional-complexe-de-type-1')]),
("Anévrisme", r"an[ée]vrism", "Dilatation localisée de la paroi d'une artère, formant une poche remplie de sang, qui peut se rompre.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8359742/anevrisme')]),
("Angiopathie amyloïde", r"angiopathie amylo", "Dépôt de protéine amyloïde dans la paroi des petites artères du sujet âgé, qui les fragilise.", [("CM6 AVC, p. 23", None)]),
("Angioscanner (angioTDM)", r"angio(scanner|TDM)", "Scanner (rayons X) avec injection de produit de contraste iodé, qui montre les artères et les veines.", [("HPSJ, fiche angioscanner", 'https://www.hpsj.fr/wp-content/uploads/2015/01/E-INFO-109-Angioscanner-et-Angio-RM.pdf')]),
("Anticoagulant", r"anticoagul", "Médicament qui retarde ou empêche la coagulation du sang (héparine, AVK, AOD).", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8372418/anticoagulant')]),
("Antiagrégant plaquettaire", r"antiagr[ée]g", "Médicament qui empêche les plaquettes de s'agréger et prévient ainsi la formation de caillots (aspirine, clopidogrel).", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8382498/antiagregant-plaquettaire')]),
("Aphasie", r"aphasi", "Trouble du langage (expression et/ou compréhension).", [("CM6 AVC, p. 6", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Apraxie", r"apraxi", "Impossibilité de réaliser volontairement des gestes pourtant connus, malgré une motricité conservée.", [("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("ARM", r"\bARM\b|angio-IRM", "Angiographie par résonance magnétique : IRM qui montre les vaisseaux.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8373134/angiographie-par-resonance-magnetique')]),
("Ataxie", r"ataxi", "Trouble de la coordination des mouvements.", [("CM6 AVC, p. 10", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Athérome", r"ath[ée]rom|ath[ée]roscl", "Plaque de dépôts de graisses (cholestérol) dans la paroi interne des grosses artères (athérosclérose = maladie correspondante).", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8874212/atherome')]),
("AVK", r"\bAVK\b|antivitamine K", "Antivitamine K : anticoagulant oral qui agit contre la vitamine K, surveillé par l'INR.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8446056/antivitamines-k')]),
("Bladder-scan", r"bladder", "Échographie portable qui mesure le volume de la vessie.", [("Vivalia, protocole sonde vésicale", 'https://www.vivalia.be/sites/default/files/2025-02/protocole-ablation-sonde-vesicale_2024_def.pdf')]),
("Claude Bernard-Horner", r"Bernard-Horner|\bCBH\b", "Ptosis + myosis + énophtalmie du même côté.", [("CM6 AVC, p. 20", None)]),
("Coils", r"\bcoils?\b", "Fils de platine en spirale, amenés par cathéter, qui remplissent l'anévrisme pour le boucher.", [("CHUV, traitement endovasculaire", 'https://www.chuv.ch/fr/neurochirurgie/nch-home/patients-et-familles/maladies-traitees/lanevrisme-cerebral/le-traitement-endovasculaire')]),
("Craniectomie", r"craniectomie", "Ablation chirurgicale d'un fragment d'os du crâne pour décomprimer le cerveau.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8448231/craniectomie')]),
("Décussation", r"d[ée]cussation", "Croisement en X, sur la ligne médiane, de fibres nerveuses qui passent du côté opposé.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8870151/decussation')]),
("Diplopie", r"diplopie", "Vision double : deux images pour un seul objet.", [("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Dissection", r"dissection", "Hématome dans la paroi d'une artère (carotide ou vertébrale), qui peut la rétrécir ou la boucher.", [("CM6 AVC, p. 20", None), ("CHUV, dissections cervicales", 'https://www.chuv.ch/fileadmin/sites/nlg/documents/dissections_cervicales_stateofart_2017_mas.pdf')]),
("Dysarthrie", r"dysarthri", "Trouble de l'articulation de la parole.", [("CM6 AVC, p. 10", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Embole", r"\bembole", "Caillot ou corps étranger transporté par le sang, qui bouche brutalement un vaisseau à distance.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8445823/embole')]),
("Embolie", r"embolie", "Obstruction brutale d'un vaisseau par un embole amené par la circulation.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17029126/embolie')]),
("Endartériectomie", r"endart[ée]riectomie", "Chirurgie qui retire la plaque d'athérome d'une artère rétrécie pour rétablir le flux.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17024765/endarteriectomie')]),
("Énophtalmie", r"[ée]nophtalmie", "Enfoncement anormal du globe oculaire dans l'orbite.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8449327/enophtalmie')]),
("FA", r"\bFA\b|fibrillation atriale", "Fibrillation atriale : trouble du rythme où les oreillettes se contractent de façon rapide, désordonnée et inefficace.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8382487/fibrillation-atriale')]),
("FLAIR", r"FLAIR", "Séquence IRM qui devient positive plus tardivement (vers 4h30) dans l'infarctus.", [("CM6 AVC, p. 12", None)]),
("HBPM", r"\bHBPM\b", "Héparine de bas poids moléculaire : anticoagulant injectable dérivé de l'héparine.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8389311/heparine-de-faible-poids-moleculaire')]),
("Hématome", r"h[ée]matome", "Collection de sang localisée dans un tissu.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8386725/hematome')]),
("Hémianopsie latérale homonyme", r"h[ée]mianopsie|\bHLH\b", "Perte de la même moitié du champ visuel sur les deux yeux.", [("CM6 AVC, p. 9", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Hémiparésie", r"h[ée]mipar[ée]sie", "Paralysie partielle (perte de force) d'une moitié du corps.", [("CM6 AVC, p. 8", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Hémiplégie", r"h[ée]mipl[ée]gi", "Paralysie complète d'une moitié du corps.", [("CM6 AVC, p. 8", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("HSA", r"\bHSA\b|sous-arachno", "Hémorragie sous-arachnoïdienne (méningée) : sang dans les espaces sous-arachnoïdiens, par rupture d'un vaisseau.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17562375/hemorragie-meningee-sous-arachnoidienne')]),
("HTIC", r"\bHTIC\b|hypertension intracr", "Hypertension intracrânienne : augmentation anormale de la pression à l'intérieur du crâne.", [("Larousse médical", 'https://www.larousse.fr/encyclopedie/medical/hypertension_intracr%C3%A2nienne/13707')]),
("Hydrocéphalie", r"hydroc[ée]phalie", "Excès de liquide céphalorachidien dans les ventricules du cerveau.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8355789/hydrocephalie')]),
("Hyperdensité", r"hyperdensit", "Au scanner : zone plus blanche que le tissu normal (ex. sang frais).", [("CM6 AVC, p. 12", None)]),
("Hypodensité", r"hypodensit", "Au scanner : zone moins dense, qui apparaît plus sombre que le tissu normal (ex. infarctus constitué).", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26572140/hypodense')]),
("Hypersignal", r"hypersignal", "En IRM : zone plus blanche que le tissu normal.", [("CM6 AVC, p. 12", None)]),
("Hyposignal", r"hyposignal", "En IRM : zone plus noire que le tissu normal.", [("CM6 AVC, p. 12", None)]),
("Anesthésie (sensibilité)", r"\banesth[ée]sie", "Perte de la sensibilité d'une partie du corps.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17013129/anesthesie')]),
("Hyperesthésie", r"hyperesth[ée]sie", "Sensibilité exagérée à toute stimulation, surtout au toucher.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26554379/hyperesthesie')]),
("Hypoesthésie", r"hypoesth[ée]sie", "Diminution de la sensibilité.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17013189/hypoesthesie')]),
("Paresthésie", r"paresth[ée]sie", "Sensibilité troublée : fourmillements, picotements.", [("CM6 AVC, p. 8", None)]),
("INR", r"\bINR\b", "Rapport international normalisé : test qui mesure le temps de coagulation d'un patient sous anticoagulant (AVK) par rapport à la normale.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8372601/rapport-international-normalise')]),
("Lacune", r"lacun", "Petite cavité (< 15 mm) profonde du cerveau, séquelle d'un petit infarctus.", [("Larousse médical", 'https://www.larousse.fr/encyclopedie/medical/lacune_c%C3%A9r%C3%A9brale/14091')]),
("Mydriase", r"mydriase", "Dilatation de la pupille.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8390754/mydriase')]),
("Myosis", r"myosis", "Contraction (rétrécissement) de la pupille.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8390747/myosis')]),
("Négligence", r"n[ée]gligence", "Méconnaissance d'un côté du corps ou de l'espace, comme s'il n'existait pas (hémi-inattention).", [("CM6 AVC, p. 10", None), ("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("NIHSS", r"NIHSS", "Score neurologique de sévérité de l'AVC, de 0 à 42.", [("CM6 AVC, p. 10", None)]),
("Œdème cérébral", r"[œo]e?d[èe]me c[ée]r[ée]bral", "Accumulation de liquide dans le tissu cérébral, qui le fait gonfler.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17011335/oedeme-cerebral')]),
("Pénombre", r"p[ée]nombre", "Zone autour du cœur de l'infarctus, moins mal irriguée : les neurones souffrent sans être morts et peuvent encore être sauvés.", [("Académie nationale de médecine", 'https://www.academie-medecine.fr/pourquoi-linfarctus-cerebral-est-une-urgence/')]),
("Ptosis", r"ptosis", "Chute de la paupière supérieure.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8408409/ptosis')]),
("Spasticité", r"spasticit", "Augmentation involontaire du tonus musculaire, qui crée une résistance au mouvement.", [("HUG, lexique AVC", 'https://www.hug.ch/accident-vasculaire-cerebral/lexique')]),
("Sténose", r"st[ée]nose", "Rétrécissement anormal et permanent du calibre d'un vaisseau ou d'un conduit.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8870133/stenose')]),
("Thrombectomie", r"thrombectomie", "Retrait mécanique du caillot par cathéter (aspiration ou stent).", [("CM6 AVC, p. 15", None), ("HPSJ, livret AVC", 'https://www.hpsj.fr/storage/2015/01/Livret_AVC_patient2024.pdf')]),
("Thrombolyse (rt-PA, TNK-pa)", r"thrombolys|rt-PA|TNK", "Traitement IV qui dissout le caillot (altéplase = rt-PA, ténectéplase = TNK-pa).", [("CM6 AVC, p. 13", None), ("HPSJ, livret AVC", 'https://www.hpsj.fr/storage/2015/01/Livret_AVC_patient2024.pdf')]),
("Thrombopénie", r"thrombop[ée]nie", "Diminution du nombre de plaquettes.", [("CM6 AVC, p. 14", None)]),
("Thrombophilie", r"thrombophilie", "Trouble de l'hémostase qui favorise les thromboses.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529744/thrombophilie')]),
("Thrombose", r"thrombose", "Formation d'un caillot dans un vaisseau ou une cavité du cœur, qui bouche partiellement ou totalement la circulation.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8389123/thrombose')]),
("Thrombus", r"thrombus", "Caillot formé dans un vaisseau ou une cavité du cœur.", [("GDT (OQLF)", 'https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8388903/thrombus')]),
("TVC", r"\bTVC\b|thrombose veineuse c[ée]r[ée]brale", "Thrombose veineuse cérébrale : caillot dans un sinus veineux ou une veine du cerveau.", [("CM6 AVC, p. 27", None), ("La Revue du Praticien", 'https://www.larevuedupraticien.fr/article/poser-le-diagnostic-de-thrombose-veineuse-cerebrale')]),
("UNV", r"\bUNV\b", "Unité neurovasculaire : service spécialisé dans la prise en charge des AVC.", [("CM6 AVC, p. 11", None), ("HPSJ, livret AVC", 'https://www.hpsj.fr/storage/2015/01/Livret_AVC_patient2024.pdf')]),
("USINV", r"\bUSINV\b", "Unité de soins intensifs neurovasculaires : partie intensive de l'UNV, pour la surveillance initiale après un AVC.", [("HPSJ, livret AVC", 'https://www.hpsj.fr/storage/2015/01/Livret_AVC_patient2024.pdf')]),
("Bandelette urinaire (BU)", r"\bBU\b|bandelette urinaire", "Bandelette réactive trempée dans l'urine, qui change de couleur au contact de certaines substances (dépistage rapide, ex. d'une infection urinaire).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8869560/bandelette-reactive")]),
("Bêtabloquant", r"b[êe]ta-?bloquant", "Médicament qui bloque les récepteurs bêta-adrénergiques : ralentit le cœur et diminue la force de ses contractions (troubles cardiovasculaires).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17034777/betabloquant")]),
("βHCG", r"βHCG|bêta-?HCG|\bhCG\b", "Hormone chorionique gonadotrophique, produite pendant la grossesse : son dosage détecte une grossesse très tôt.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8445765/hormone-chorionique-gonadotrophique")]),
("Coronarographie", r"coronarographi", "Radiographie des artères coronaires avec produit de contraste, pour diagnostiquer et traiter leurs lésions.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8445954/coronarographie")]),
("Coronaropathie", r"coronaropathi", "Maladie des artères coronaires (maladie coronarienne).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529842/coronaropathie")]),
("CRP", r"\bCRP\b", "Protéine C réactive : protéine qui augmente dans le sang lors d'une inflammation ou d'une infection aiguë.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17018241/proteine-c-reactive")]),
("Créatinine", r"cr[ée]atinin", "Déchet éliminé par le rein dans les urines : une hausse dans le sang signale une insuffisance rénale.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8390735/creatinine")]),
("D-dimères", r"D-?dim[èe]res", "Fragments libérés quand un caillot se dégrade : leur dosage sert à rechercher une thrombose (phlébite, embolie pulmonaire).", [("Manuels MSD, dosage des D-dimères", "https://www.msdmanuals.com/iframe/manual/labtests/ddimertest-fr.html")]),
("Diurétique", r"diur[ée]tique", "Médicament qui augmente le volume des urines ; traite les œdèmes, l'insuffisance cardiaque et l'hypertension.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8443690/diuretique")]),
("ECBU", r"\bECBU\b", "Examen cytobactériologique des urines : recherche au laboratoire des bactéries d'une infection urinaire.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8373612/examen-cytobacteriologique-des-urines")]),
("ECG", r"\bECG\b|[ée]lectrocardiogramme", "Électrocardiogramme : enregistrement de l'activité électrique du cœur (rythme, ischémie).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8374291/electrocardiogramme")]),
("Échocardiographie", r"[ée]chocardiograph|[ée]chographie (cardiaque )?trans", "Exploration du cœur par ultrasons.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529231/echocardiographie")]),
("ETT", r"\bETT\b|transthoracique", "Échocardiographie transthoracique : sonde posée sur le thorax.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529232/echocardiographie-transthoracique")]),
("ETO", r"\bETO\b|trans[œo]e?sophagienne", "Échocardiographie transœsophagienne : sonde passée par la bouche dans l'œsophage ; voit mieux les oreillettes (source d'un caillot) que l'ETT.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8392003/echocardiographie-transoesophagienne")]),
("Écho-doppler", r"[ée]cho-?doppler|doppler", "Échographie qui mesure la vitesse du sang : renseigne sur la circulation et l'anatomie des vaisseaux (ex. sténose d'une carotide).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8365612/echographie-doppler")]),
("EEG", r"\bEEG\b|[ée]lectroenc[ée]phalogramme", "Électroencéphalogramme : enregistrement de l'activité électrique du cerveau par des électrodes sur le cuir chevelu.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17021498/electroencephalogramme")]),
("Épreuve d'effort", r"[ée]preuve d'effort", "Enregistrement de l'ECG pendant un effort, pour dépister une maladie des coronaires.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8360297/epreuve-de-master")]),
("Exophtalmie", r"exophtalmi", "Saillie anormale de l'œil hors de son orbite.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17024707/exophtalmie")]),
("FC", r"\bFC\b", "Fréquence cardiaque : nombre de battements du cœur par minute.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8371098/frequence-cardiaque")]),
("Fibrinogène", r"fibrinog[èe]ne", "Protéine du plasma, fabriquée par le foie, transformée en fibrine lors de la coagulation.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8447984/fibrinogene")]),
("Glasgow", r"Glasgow", "Échelle de Glasgow : cote le niveau de conscience sur 3 réponses (ouverture des yeux, réponse motrice, réponse verbale).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17484899/echelle-de-glasgow")]),
("Glycémie capillaire", r"glyc[ée]mie capillaire", "Glycémie mesurée sur une goutte de sang prélevée au bout du doigt, avec un glucomètre.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8392330/mesure-de-la-glycemie-capillaire")]),
("HbA1c", r"HbA1c", "Hémoglobine glyquée : reflète la glycémie moyenne des 2 mois précédents ; sert au suivi du diabète.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8385656/hemoglobine-glyquee")]),
("HDL", r"\bHDL\b", "Cholestérol HDL : cholestérol des lipoprotéines de haute densité ; un taux bas est associé à la maladie athéromateuse.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17563497/cholesterol-hdl")]),
("Hémoculture", r"h[ée]mocultur", "Mise en culture d'un prélèvement de sang pour rechercher des microbes (infection du sang).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8447317/hemoculture")]),
("HTA", r"\bHTA\b|hypertension art[ée]rielle", "Hypertension artérielle : pression artérielle anormalement élevée (en général à partir de 140/90 mmHg).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8373363/hypertension-arterielle")]),
("IDM", r"\bIDM\b|infarctus du myocarde", "Infarctus du myocarde : nécrose d'une partie du muscle cardiaque, le plus souvent par thrombose d'une artère coronaire.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/18954674/infarctus-du-myocarde")]),
("IEC", r"\bIECA?\b", "Inhibiteur de l'enzyme de conversion : antihypertenseur qui dilate les vaisseaux en bloquant la formation d'angiotensine II.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8375331/inhibiteur-de-lenzyme-de-conversion-de-langiotensine")]),
("IMC", r"\bIMC\b", "Indice de masse corporelle : poids (kg) divisé par la taille (m) au carré.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8357771/indice-de-masse-corporelle")]),
("Ionogramme", r"ionogramme|\biono\b", "Dosage des ions du sang (sodium, potassium, chlore…).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26556283/ionogramme")]),
("IRM", r"\bIRM\b", "Imagerie par résonance magnétique : images en coupes des organes, sans rayons X.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8383254/imagerie-par-resonance-magnetique")]),
("IV", r"\bIV\b", "Intraveineux : administré dans une veine.", [("Manuels MSD, abréviations", "https://www.merckmanuals.com/fr-ca/accueil/resourcespages/abr%C3%A9viations")]),
("LCR", r"\bLCR\b|c[ée]phalorachidien", "Liquide céphalorachidien : liquide qui remplit les ventricules cérébraux et entoure le cerveau et la moelle.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8441217/liquide-cerebrospinal")]),
("LDL", r"\bLDL\b", "Cholestérol LDL (« mauvaises lipoprotéines ») : il se dépose dans les artères et forme des plaques.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17561303/cholesterol-ldl")]),
("Lipasémie", r"lipas[ée]mie", "Taux de lipase dans le sang ; la lipase pancréatique augmente lors d'une pancréatite.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26555200/lipasemie")]),
("MAPA", r"\bMAPA\b", "Mesure ambulatoire de la pression artérielle sur 24 h, pendant les activités habituelles.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8871505/monitorage-ambulatoire-de-la-pression-arterielle")]),
("NFS", r"\bNFS\b|h[ée]mogramme", "Numération formule sanguine (hémogramme) : compte des globules rouges, globules blancs et plaquettes.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26529862/hemogramme")]),
("PA", r"\bPA\b|pression art[ée]rielle", "Pression artérielle : force exercée par le sang sur la paroi des artères.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8873697/pression-arterielle")]),
("Ponction lombaire (PL)", r"\bPL\b|ponction lombaire", "Introduction d'une aiguille entre deux vertèbres lombaires pour prélever du liquide céphalorachidien.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8382477/ponction-lombaire")]),
("PSA", r"\bPSA\b", "Antigène spécifique de la prostate : marqueur des anomalies de la prostate (dépistage du cancer de la prostate).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17010705/antigene-specifique-de-la-prostate")]),
("RAI", r"\bRAI\b", "Recherche d'agglutinines irrégulières : recherche d'anticorps contre les globules rouges autres que anti-A et anti-B.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17567240/anticorps-irreguliers")]),
("SAMU", r"\bSAMU\b", "Service d'aide médicale urgente : premiers soins et transport des patients vers l'hôpital.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17565045/service-daide-medicale-durgence")]),
("SNG", r"\bSNG\b|sonde naso-?gastrique", "Sonde nasogastrique : tube souple passé par une narine jusqu'à l'estomac (alimentation ou aspiration).", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8407185/sonde-naso-gastrique")]),
("SpO2", r"SpO2|SatO2|SaO2", "Saturation du sang en oxygène mesurée au doigt par un oxymètre de pouls.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/26542361/oxymetre-de-pouls")]),
("Statine", r"statine", "Médicament qui bloque la fabrication du cholestérol et fait baisser le cholestérol sanguin.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17011862/statine")]),
("TCA", r"\bTCA\b", "Temps de céphaline activée : test de coagulation (voie endogène), allongé en cas de déficit en facteurs de coagulation ou sous héparine.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8436844/temps-de-cephaline")]),
("TDM", r"\bTDM\b|tomodensitom", "Tomodensitométrie (scanner) : imagerie en coupes par rayons X.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8359977/tomodensitometrie")]),
("TP", r"\bTP\b", "Temps de Quick, exprimé en taux de prothrombine : test de coagulation, abaissé sous antivitamine K.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8408340/temps-de-quick")]),
("Trendelenburg", r"Trendelenburg", "Position allongée sur le dos, la tête plus basse que les pieds.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8436622/position-de-trendelenburg")]),
("Triglycérides", r"triglyc[ée]ride", "Graisses formées de glycérol et de 3 acides gras ; dosées dans le bilan lipidique.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8351662/triglyceride")]),
("Troponine", r"troponine", "Protéine du muscle cardiaque ; son taux sanguin s'élève quand le cœur est lésé (infarctus du myocarde).", [("Manuels MSD, dosage de la troponine", "https://www.merckmanuals.com/iframe/manual/labtests/troponintest-fr.html")]),
("TSH", r"\bTSH\b", "Thyréostimuline : hormone de l'hypophyse qui stimule la thyroïde ; son dosage explore la fonction thyroïdienne.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/17057485/thyreostimuline")]),
("VS", r"\bVS\b", "Vitesse de sédimentation : augmente en cas d'inflammation, d'infection ou d'anémie.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/19058820/vitesse-de-sedimentation-erythrocytaire")]),
("Holter", r"[Hh]olter", "Enregistrement continu de l'ECG pendant au moins 24 h avec un appareil portatif.", [("GDT (OQLF)", "https://vitrinelinguistique.oqlf.gouv.qc.ca/fiche-gdt/fiche/8892537/enregistrement-holter")]),
]
_C = [(t, re.compile(p, re.I if not re.search(r"\\b[A-Z]", p) else 0), d, src) for t, p, d, src in G]

def _check(entries):
    """Une ligne = un terme = une définition (D50) : jamais « A / B » ni « déf. A / déf. B »."""
    for e in entries:
        if len(e) != 4 or not e[3]:
            raise ValueError(f"Glossaire : « {e[0]} » sans source (règle S8) : ajouter la page du cours ou une source fiable.")
        t, p, d, src = e
        if "/" in t or " / " in d:
            raise ValueError(f"Glossaire : « {t} » regroupe plusieurs termes ou définitions ; faire une ligne par terme (règle X3).")

_check(G)

def add(extra):
    """Ajoute des entrées (terme, motif, définition, sources) propres à un cours."""
    global _C
    _check(extra)
    G.extend(extra)
    _C = [(t, re.compile(p, re.I if not re.search(r"\\b[A-Z]", p) else 0), d, src) for t, p, d, src in G]

def gloss(text):
    """Entrées (terme, définition, sources) dont le motif apparaît dans le texte ; la mise en forme est faite par build.py."""
    plain = re.sub(r"<[^>]+>", " ", text)
    return [(t, d, src) for t, rx, d, src in _C if rx.search(plain)]
