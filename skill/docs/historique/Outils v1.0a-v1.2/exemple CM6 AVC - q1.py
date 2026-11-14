# Questions A-F. Q(id, ks, mode, énoncé, [4 propositions], vérité, explication, notion, x=avertissement/modif, w=sources web)
# mode : 0 = Kprim, 1 = QCM, 2 = QCS
from common import Q
QS = []
a = QS.append

# ---------- A. Épidémiologie, définitions ----------
a(Q("A01","K008",2,"AVC artériels — <b>répartition</b> entre ischémiques et hémorragiques ?",
 ["50 % ischémiques / 50 % hémorragiques","15 % ischémiques / 85 % hémorragiques","85 % ischémiques / 15 % hémorragiques","70 % ischémiques / 30 % hémorragiques"],"0010",
 "Artère qui se bouche (ischémie) : 85 % ; artère qui se rompt (hémorragie) : 15 %.","Types d'AVC"))
a(Q("A02","K008",2,"AVC hémorragique — <b>mécanisme</b> ?",
 ["Une artère qui se bouche","Une artère qui se rompt","Une veine qui se bouche","Un spasme artériel transitoire"],"0100",
 "Hémorragie = artère qui se rompt. Artère qui se bouche = ischémie ; veine qui se bouche = thrombose veineuse cérébrale (plus rare).","Types d'AVC"))
a(Q("A03","K008",2,"AVC — forme <b>plus rare</b> citée en plus des deux types artériels ?",
 ["Une veine qui se bouche","Un anévrisme qui se rompt","Une artère qui se dilate","Un capillaire qui se rompt"],"1000",
 "En plus de l'ischémie (85 %) et de l'hémorragie (15 %), le cours cite une forme plus rare : la veine qui se bouche (thrombose veineuse cérébrale).","Types d'AVC"))
a(Q("A04","K009",1,"Infarctus cérébral — <b>conséquences</b> de l'occlusion artérielle ?",
 ["Insuffisance d'apport en oxygène","Insuffisance d'apport en glucose","Zone de nécrose du tissu cérébral","Saignement dans le parenchyme"],"1110",
 "L'occlusion prive le cerveau d'O2 et de glucose → nécrose (zone d'infarctus). Le saignement correspond à l'hémorragie.","Ischémie"))
a(Q("A05","K010",2,"Accident ischémique transitoire (AIT) — <b>définition</b> ?",
 ["Occlusion artérielle définitive d'une petite artère","Petite hémorragie résorbée spontanément","Occlusion veineuse transitoire","Occlusion artérielle temporaire sans lésion ischémique constituée"],"0001",
 "AIT : l'artère se débouche, sans lésion ischémique constituée autour de l'artère bouchée.","AIT"))
a(Q("A06","K009 K010",0,"Accident ischémique cérébral (AIC) — affirmations",
 ["L'infarctus cérébral et l'AIT sont deux formes d'AIC","Dans l'AIT, l'occlusion artérielle est définitive","L'infarctus cérébral correspond à une zone de nécrose","Les AIC représentent environ 15 % des AVC"],"1010",
 "2. Faux : l'occlusion de l'AIT est temporaire. 4. Faux : les AIC représentent 85 % des AVC (15 % = hémorragies).","Ischémie"))
a(Q("A07","K013",2,"Hémorragie cérébrale — <b>principale cause</b> ?",
 ["Fibrillation atriale","Hypertension artérielle","Athérome carotidien","Dissection carotidienne"],"0100",
 "La principale cause d'hémorragie cérébrale est l'HTA. FA, athérome et dissection sont des causes d'infarctus.","Hémorragie"))
a(Q("A08","K013",2,"Homme de 68 ans, HTA mal équilibrée, hémiplégie brutale. Scanner : hémorragie intraparenchymateuse. <b>Facteur étiologique le plus probable</b> ?",
 ["Fibrillation atriale","Dissection de l'artère vertébrale","Hypertension artérielle","Athérome carotidien"],"0010",
 "HTA = principale cause d'hémorragie cérébrale (≈ 80 % des hématomes non traumatiques, p. 23).","Hémorragie"))
a(Q("A09","K014",1,"AVC hémorragiques — <b>formes</b> citées dans le cours ?",
 ["Hémorragie intracérébrale","Hémorragie méningée","Hématome sous-dural","Thrombose veineuse cérébrale"],"1100",
 "Hémorragiques (15 %) : intracérébrale et méningée. Le sous-dural est traumatique ; la TVC est une occlusion veineuse.","Hémorragie"))
a(Q("A10","K002",2,"AVC en France — <b>rang comme cause de handicap acquis</b> de l'adulte ?",
 ["1re cause","2e cause","3e cause","5e cause"],"1000",
 "AVC : 1re cause de handicap de l'adulte, 2e cause de démence, 3e cause de décès.","Épidémiologie"))
a(Q("A11","K003 K004",0,"AVC en France — épidémiologie",
 ["2e cause de démence","3e cause de décès","1re cause de décès chez la femme","1re cause de décès chez l'homme"],"1110",
 "Diapo : 2e cause de démence, 3e cause de décès. Note de cours : 1re cause de décès chez la femme. 4. Faux : pas chez l'homme.","Épidémiologie"))
a(Q("A12","K001",2,"AVC — <b>nombre de cas par an</b> en France ?",
 ["15 000","50 000","150 000","500 000"],"0010","150 000 AVC par an en France.","Épidémiologie"))
a(Q("A13","K005",1,"AVC — <b>âge des patients</b> selon le cours ?",
 ["Âge médian d'environ 75 ans","Environ 10 % ont moins de 45 ans","Âge médian d'environ 55 ans","Moins de 1 % ont moins de 45 ans"],"1100",
 "Âge médian 75 ans, mais 10 % des patients ont moins de 45 ans.","Épidémiologie"))
a(Q("A14","K006",2,"AVC — <b>devenir à 1 an</b> (graphique du cours) ?",
 ["≈ 1/2 décès, 1/4 handicap, 1/4 autonomie","≈ 1/4 décès, 1/2 handicap, 1/4 autonomie","≈ 1/10 décès, 1/4 handicap, 2/3 autonomie","≈ 1/4 décès, 1/4 handicap, 1/2 autonomie"],"0100",
 "Graphique « Devenir des AVC à 1 an » : environ un quart de décès, la moitié avec handicap, un quart autonome.","Épidémiologie"))
a(Q("A15","K007",2,"AVC — <b>filière de soins spécialisée</b> ?",
 ["Médecin traitant ; urgences ; EHPAD","Pré-hospitalier ; Unité Neuro-Vasculaire ; rééducation","Pré-hospitalier ; réanimation ; domicile","Urgences ; cardiologie ; rééducation"],"0100",
 "Filière : pré-hospitalier → UNV → rééducation.","Filière"))
a(Q("A16","K011",1,"Infarctus cérébral — <b>causes</b> ?",
 ["Athérome","Maladie des petites artères (lacunes)","Embolie d'origine cardiaque","Angiopathie amyloïde"],"1110",
 "Causes d'infarctus : athérome, lacunes, embolies cardiaques, causes rares, sans cause. L'angiopathie amyloïde est une cause d'hématome (p. 23).","Étiologies"))
a(Q("A17","K012",2,"Infarctus cérébral — <b>répartition des causes</b> ?",
 ["Athérome 20 % ; lacunes 25 % ; embolies cardiaques 20 % ; sans cause 30 %","Athérome 50 % ; lacunes 5 % ; embolies cardiaques 40 % ; sans cause 5 %","Athérome 30 % ; lacunes 20 % ; embolies cardiaques 45 % ; sans cause 5 %","Athérome 10 % ; lacunes 10 % ; embolies cardiaques 10 % ; sans cause 70 %"],"1000",
 "Schéma p. 2 : athérome 20 %, lacunes 25 %, embolies cardiaques 20 %, causes rares 5 %, sans cause 30 %.","Étiologies"))

# ---------- B. Démarche ----------
a(Q("B01","K016",2,"Suspicion d'AVC — <b>3 caractéristiques du déficit</b> ?",
 ["Déficit ; progressif ; diffus","Douleur ; brutale ; focale","Déficit ; brutal ; focal","Déficit ; brutal ; bilatéral et symétrique"],"0010",
 "On suspecte un AVC devant un déficit neurologique BRUTAL et FOCAL (selon la zone du cerveau atteinte).","Suspicion"))
a(Q("B02","K016",2,"Suspicion d'AVC — <b>présentation la plus évocatrice</b> ?",
 ["Faiblesse des 4 membres installée sur plusieurs semaines","Faiblesse du bras et de la face droits apparue en quelques secondes","Confusion progressive sur 3 jours avec fièvre","Fourmillements des deux mains et des lèvres lors d'une crise d'angoisse"],"0100",
 "Déficit brutal (quelques secondes) et focal (un hémicorps) = AVC jusqu'à preuve du contraire.","Suspicion"))
a(Q("B03","K015",2,"Suspicion d'AVC — <b>pourquoi aucun traitement spécifique avant l'imagerie</b> ?",
 ["Le traitement est le même quel que soit le type d'AVC","L'imagerie sert seulement à évaluer la sévérité","Le NIHSS doit d'abord être inférieur à 5","Seule l'imagerie distingue ischémie et hémorragie"],"0001",
 "La clinique ne distingue pas ischémie et hémorragie ; un antithrombotique ou un thrombolytique serait dangereux en cas d'hémorragie.","Imagerie avant traitement"))
a(Q("B04","K015 K016",0,"AVC — démarche initiale",
 ["La clinique ne permet pas de distinguer ischémie et hémorragie","Un antithrombotique peut être débuté avant l'imagerie si le déficit est franc","L'AVC est une urgence vitale et fonctionnelle","L'imagerie cérébrale est indispensable pour orienter le traitement"],"1011",
 "2. Faux : aucun traitement antithrombotique tant que l'hémorragie n'est pas éliminée par l'imagerie.","Imagerie avant traitement"))
a(Q("B05","K017",1,"AVC — <b>étapes de la démarche</b> diagnostique et thérapeutique ?",
 ["Rechercher la cause (étiologie)","Attendre 24 h l'évolution spontanée avant de décider","Affirmer le diagnostic et le type d'AVC","Traiter pour éviter les récidives, selon la cause"],"1011",
 "Étapes : diagnostic et type ; traitement immédiat ; étiologie ; amélioration du pronostic ; prévention des récidives. Attendre est l'inverse du « time is brain ».","Démarche"))
a(Q("B06","K018",2,"AVC — <b>vaisseau le plus souvent en cause</b> ?",
 ["Une veine","Un sinus veineux","Une artère","Un capillaire"],"0010",
 "Lésion d'un vaisseau cérébral : artère >> veine.","Démarche"))

# ---------- C. Rappels anatomiques ----------
a(Q("C01","K019",1,"Lobe frontal — <b>fonctions</b> ?",
 ["Motricité","Fonctions exécutives (planification, organisation)","Vision","Sensibilité"],"1100",
 "Frontal : motricité + fonctions exécutives. Vision = occipital ; sensibilité = pariétal.","Lobes"))
a(Q("C02","K020",2,"Lobe pariétal — <b>fonction principale</b> ?",
 ["Motricité","Sensibilité","Vision","Mémoire"],"0100",
 "Pariétal : sensibilité (tactile, chaud, douleur, position du corps dans l'espace).","Lobes"))
a(Q("C03","K021",2,"Lobe occipital — <b>fonction</b> ?",
 ["Langage","Coordination","Vision","Audition"],"0010","Occipital : vision.","Lobes"))
a(Q("C04","K022",2,"Cervelet — <b>fonction</b> ?",
 ["Coordination du mouvement et équilibre","Sensibilité","Mémoire","Vision"],"1000","Cervelet : coordination du mouvement (équilibre).","Lobes"))
a(Q("C05","K023",1,"Lobe temporal — <b>fonctions</b> citées ?",
 ["Mémoire","Motricité","Langage","Vision"],"1010","Temporal : mémoire et langage.","Lobes"))
a(Q("C06","K022",2,"Trouble brutal de la coordination des mouvements avec instabilité à la marche. <b>Structure</b> la plus probablement atteinte ?",
 ["Lobe occipital","Lobe temporal","Lobe pariétal","Cervelet"],"0001","Coordination/équilibre = cervelet (ataxie).","Lobes"))
a(Q("C07","K024",1,"Tronc cérébral — <b>fonctions</b> assurées (nerfs crâniens, centres) ?",
 ["Mouvements oculaires","Déglutition","Centres végétatifs (cœur, respiration)","Vision des formes et des couleurs"],"1110",
 "Tronc : nerfs crâniens (oculomotricité, motricité/sensibilité de la face, déglutition, équilibre) + centres végétatifs. La vision consciente = cortex occipital.","Tronc cérébral"))
a(Q("C08","K024",2,"Tronc cérébral — <b>nombre de paires de nerfs crâniens</b> ?",
 ["8","10","12","31"],"0010","12 paires de nerfs crâniens (31 = nerfs rachidiens).","Tronc cérébral"))
a(Q("C09","K025",2,"Tronc cérébral — <b>étages de haut en bas</b> ?",
 ["Bulbe ; protubérance ; mésencéphale","Mésencéphale ; protubérance ; bulbe","Protubérance ; mésencéphale ; bulbe","Mésencéphale ; bulbe ; protubérance"],"0100",
 "De haut en bas : mésencéphale, protubérance (pont), bulbe.","Tronc cérébral"))
a(Q("C10","K026",2,"Voie motrice (faisceau pyramidal) — <b>trajet</b> ?",
 ["Cortex pariétal → thalamus → tronc cérébral → moelle","Moelle → tronc cérébral → capsule interne → cortex frontal","Cortex occipital → chiasma → tronc cérébral → moelle","Cortex frontal → capsule interne → tronc cérébral → moelle"],"0001",
 "Voie motrice descendante : cortex frontal → capsule interne → tronc cérébral → moelle → muscles.","Voies motrices"))
a(Q("C11","K027",2,"Lésion de l'hémisphère gauche — <b>côté du déficit moteur</b> ?",
 ["Hémicorps gauche (homolatéral)","Hémicorps droit (controlatéral)","Les deux côtés de façon symétrique","Uniquement la face, des deux côtés"],"0100",
 "Les voies motrices croisent au niveau du bulbe : déficit controlatéral à la lésion.","Voies motrices"))
a(Q("C12","K027",2,"Voie motrice — <b>pourquoi le déficit est-il controlatéral</b> ?",
 ["Croisement des fibres au chiasma optique","Croisement des fibres dans le cortex frontal","Croisement des fibres au niveau du bulbe (décussation)","Croisement des fibres dans le cervelet"],"0010",
 "Décussation bulbaire : environ 80 % des fibres pyramidales croisent la ligne médiane dans le bulbe.","Voies motrices"))
a(Q("C13","K027",2,"Hémiplégie gauche brutale. <b>Hémisphère</b> probablement atteint ?",
 ["Hémisphère droit","Hémisphère gauche","Cervelet gauche","Les deux hémisphères"],"1000","Déficit controlatéral : hémiplégie gauche → lésion hémisphérique droite.","Voies motrices"))
a(Q("C14","K028",0,"Voies sensitives ascendantes",
 ["Elles remontent de la moelle vers le cortex pariétal","Elles font relais dans le thalamus","Le déficit sensitif est homolatéral à la lésion cérébrale","Les fibres croisent la ligne médiane avant d'atteindre le cortex"],"1101",
 "Moelle → cortex pariétal, relais thalamique ; les faisceaux croisent → déficit controlatéral.","Voies sensitives"))
a(Q("C15","K029",2,"Voies visuelles — <b>trajet</b> ?",
 ["Nerf optique → thalamus → cortex frontal","Nerf optique → chiasma optique → cortex occipital","Chiasma optique → nerf optique → cortex pariétal","Nerf optique → chiasma optique → cortex temporal"],"0100",
 "Nerf optique → chiasma (croisement) → cortex occipital.","Voies visuelles"))
a(Q("C16","K029",2,"Voies visuelles — <b>lieu du croisement</b> des fibres ?",
 ["Bulbe","Capsule interne","Cortex occipital","Chiasma optique"],"0001","Croisement des voies visuelles au chiasma optique.","Voies visuelles"))
a(Q("C17","K030",2,"Langage — <b>hémisphère dominant chez un droitier</b> ?",
 ["Droit","Gauche","Les deux, de façon égale","Variable : 50 % droit, 50 % gauche"],"0100",
 "L'hémisphère dominant (majeur) porte les aires du langage : gauche chez le droitier.","Langage"))
a(Q("C18","K030",2,"Langage — <b>hémisphère dominant chez la majorité des gauchers</b> ?",
 ["Droit","Toujours les deux de façon égale","Gauche","Le cervelet"],"0010",
 "Environ 70 % des gauchers ont aussi le langage latéralisé à gauche.","Langage",
 x="✎ Modifié par rapport au cours : « gaucher : hémisphère majeur droit » → « gauche chez la majorité des gauchers » (la dominance droite ne concerne qu'une minorité de gauchers).",
 w=["Web — Techno-Science, Préférence manuelle et langage : existe-t-il un hémisphère dominant ?, https://www.techno-science.net/fr/actualites/preference-manuelle-et-langage-existe-t-il-un-hemisphere-dominant-12938"]))
a(Q("C19","K031",2,"Aire de Broca — <b>localisation ; trouble en cas d'atteinte</b> ?",
 ["Cortex temporal ; aphasie de compréhension","Cortex frontal ; aphasie de compréhension","Cortex frontal ; aphasie d'expression","Cortex occipital ; cécité corticale"],"0010",
 "Broca : cortex frontal, aphasie d'expression. Wernicke : cortex temporal, aphasie de compréhension.","Langage"))
a(Q("C20","K031",2,"Aire de Wernicke — <b>localisation ; trouble en cas d'atteinte</b> ?",
 ["Cortex temporal ; aphasie de compréhension","Cortex frontal ; aphasie d'expression","Cortex temporal ; aphasie d'expression","Cortex pariétal ; dysarthrie"],"1000",
 "Wernicke : cortex temporal, aphasie de compréhension.","Langage"))
a(Q("C21","K031",2,"Patient qui comprend les consignes mais ne parvient pas à produire les mots. <b>Aire atteinte</b> ?",
 ["Aire de Wernicke","Aire de Broca","Cervelet","Cortex occipital"],"0100","Compréhension conservée, expression altérée = aphasie d'expression = aire de Broca.","Langage"))
a(Q("C22","K032",0,"Fonctions cognitives hémisphériques",
 ["L'hémisphère gauche gère le langage et le geste","Une atteinte gauche donne aphasies et apraxies","L'hémisphère droit gère l'espace, l'attention et l'émotion","Une atteinte droite donne surtout une aphasie"],"1110",
 "4. Faux : une atteinte droite donne un syndrome de l'hémisphère mineur (négligence de la partie gauche du corps et de l'espace).","Fonctions cognitives"))
a(Q("C23","K032",2,"AVC hémisphérique droit — <b>trouble cognitif typique</b> ?",
 ["Aphasie d'expression","Négligence de l'hémicorps et de l'espace gauches","Apraxie avec aphasie","Négligence de l'hémicorps droit"],"0100",
 "Atteinte droite = syndrome de l'hémisphère mineur : difficulté à prendre en compte la partie gauche du corps.","Fonctions cognitives"))
a(Q("C24","K033",2,"Vascularisation cérébrale — <b>les 4 axes artériels</b> ?",
 ["2 carotides internes + 2 sous-clavières","2 carotides internes + 2 vertébrales","4 carotides (2 internes, 2 externes)","2 vertébrales + tronc basilaire + aorte"],"0100",
 "4 axes : 2 carotides (circulation antérieure) + 2 vertébrales (→ tronc basilaire, circulation postérieure).","Territoires artériels"))
a(Q("C25","K033",2,"Circulation <b>postérieure</b> — artères qui la forment ?",
 ["Les 2 carotides internes","Les 2 cérébrales antérieures","Les 2 artères vertébrales, réunies en tronc basilaire","Les 2 carotides externes"],"0010",
 "Circulation postérieure : 2 vertébrales → tronc basilaire. Circulation antérieure : carotides.","Territoires artériels"))
a(Q("C26","K034",1,"Carotide interne — <b>branches</b> ?",
 ["Artère ophtalmique","Artère cérébrale postérieure","Artère cérébrale moyenne","Artère cérébrale antérieure"],"1011",
 "Carotide interne : ophtalmique, cérébrale moyenne, cérébrale antérieure, choroïdienne antérieure. Les cérébrales postérieures viennent du tronc basilaire.","Territoires artériels"))
a(Q("C27","K035",2,"Tronc basilaire — <b>donne les deux artères</b> ?",
 ["Cérébrales antérieures","Cérébrales moyennes","Ophtalmiques","Cérébrales postérieures"],"0001","Le tronc basilaire donne les 2 artères cérébrales postérieures.","Territoires artériels"))
a(Q("C28","K035",2,"Artères vertébrales — <b>branches citées</b> ?",
 ["Tronc basilaire et artères cérébelleuses (PICA)","Artère ophtalmique et cérébrale moyenne","Artères communicantes antérieures","Artère choroïdienne antérieure"],"1000",
 "Vertébrale : tronc basilaire, cérébelleuses (PICA…), puis cérébrales postérieures via le tronc basilaire.","Territoires artériels"))
a(Q("C29","K036",0,"Polygone de Willis",
 ["Il permet des suppléances en cas d'occlusion d'une artère","L'artère communicante antérieure relie les deux cérébrales antérieures","Les communicantes postérieures relient circulation antérieure et postérieure","Sa configuration est identique chez tous les individus"],"1110",
 "4. Faux : les suppléances sont hétérogènes et variables selon les individus.","Polygone de Willis"))

# ---------- D. Symptômes, évaluation ----------
a(Q("D01","K037",1,"AVC — <b>signes d'alerte</b> de survenue brutale ?",
 ["Difficulté à parler","Difficulté à bouger une moitié du corps","Trouble de la vision","Douleur thoracique constrictive"],"1110",
 "Signes d'alerte : parole, moitié du corps, vision, équilibre, mal de tête soudain violent. La douleur thoracique évoque un SCA.","Signes d'alerte"))
a(Q("D02","K037",1,"AVC — autres <b>signes d'alerte</b> brutaux ?",
 ["Troubles de l'équilibre","Toux fébrile","Mal de tête soudain et violent","Douleur abdominale"],"1010",
 "Troubles de l'équilibre et céphalée soudaine violente font partie des signes d'alerte.","Signes d'alerte"))
a(Q("D03","K037",2,"Signes d'alerte d'AVC — <b>conduite à tenir immédiate</b> ?",
 ["Prendre rendez-vous chez le médecin traitant dans la journée","Donner de l'aspirine et attendre","Allonger la personne et réévaluer dans 1 heure","Appeler le 15"],"0001",
 "Urgence : appel du 15 (filière SAMU → UNV). Pas d'aspirine avant l'imagerie.","Signes d'alerte"))
a(Q("D04","K038",2,"<b>Hémiplégie / hémiparésie</b> — définitions ?",
 ["Hémiplégie = paralysie complète d'un hémicorps ; hémiparésie = paralysie partielle","Hémiplégie = paralysie partielle ; hémiparésie = paralysie complète","Hémiplégie = paralysie des 2 membres inférieurs ; hémiparésie = d'un hémicorps","Hémiplégie = paralysie d'un hémicorps ; hémiparésie = trouble sensitif d'un hémicorps"],"1000",
 "Hémiplégie : complète ; hémiparésie : partielle. Peut toucher face, MS, MI.","Vocabulaire"))
a(Q("D05","K038",2,"Bras et jambe droits : mouvements possibles mais force diminuée. <b>Terme</b> ?",
 ["Hémiplégie droite","Hémiparésie droite","Paraplégie","Hypoesthésie droite"],"0100","Déficit moteur partiel d'un hémicorps = hémiparésie.","Vocabulaire"))
a(Q("D06","K039",2,"<b>Paresthésies</b> — définition ?",
 ["Sensations anormales de type fourmillements, picotements","Perte complète de la sensibilité","Paralysie partielle d'un membre","Trouble de la coordination"],"1000",
 "Paresthésies : sensibilité troublée (fourmillements, engourdissement). Perte complète = anesthésie.","Vocabulaire"))
a(Q("D07","K039",2,"<b>Hypoesthésie</b> — définition ?",
 ["Perte totale de la sensibilité","Sensibilité exagérée","Diminution de la sensibilité","Fourmillements"],"0010","Hypoesthésie = diminution ; anesthésie = perte totale.","Vocabulaire"))
a(Q("D08","K040",2,"<b>Aphasie / dysarthrie</b> — définitions ?",
 ["Aphasie = trouble de l'articulation ; dysarthrie = trouble du langage","Aphasie = trouble du langage ; dysarthrie = trouble de l'articulation","Aphasie = absence de voix ; dysarthrie = trouble de la déglutition","Aphasie = trouble de la mémoire ; dysarthrie = trouble du langage"],"0100",
 "Aphasie : trouble du langage (hémisphère dominant). Dysarthrie : trouble de l'articulation, souvent associée à un déficit moteur.","Vocabulaire"))
a(Q("D09","K040",2,"Patient qui articule mal (parole « pâteuse ») mais construit des phrases correctes et comprend tout. <b>Trouble</b> ?",
 ["Aphasie de compréhension","Aphasie d'expression","Apraxie","Dysarthrie"],"0001","Langage normal, articulation altérée = dysarthrie.","Vocabulaire"))
a(Q("D10","K040",1,"Aphasie — <b>manifestations</b> ?",
 ["Perte de la compréhension","Incapacité à parler (mutisme)","Propos incohérents (jargon)","Voix nasonnée par trouble articulatoire"],"1110",
 "Aphasie : perte de compréhension, mutisme, jargon. Le trouble articulatoire relève de la dysarthrie.","Vocabulaire"))
a(Q("D11","K041",1,"Troubles de l'équilibre d'origine vasculaire — <b>manifestations</b> ?",
 ["Perte soudaine de l'équilibre ± vertiges","Ataxie (démarche ébrieuse)","Incoordination des membres","Hémianopsie latérale homonyme"],"1110","L'hémianopsie est un trouble visuel.","Équilibre"))
a(Q("D12","K041",2,"<b>Ataxie</b> — définition ?",
 ["Perte de la vision d'un œil","Trouble de la coordination des mouvements","Paralysie d'un hémicorps","Trouble du langage"],"0100","Ataxie : difficulté de coordination du mouvement (démarche ébrieuse).","Vocabulaire"))
a(Q("D13","K042",2,"Cécité monoculaire brutale — <b>artère en cause</b> ?",
 ["Artère cérébrale postérieure","Tronc basilaire","Artère ophtalmique (branche de la carotide interne)","Artère cérébrale antérieure"],"0010",
 "Cécité monoculaire : artère ophtalmique (branche de la carotide interne) ou atteinte de la rétine.","Troubles visuels"))
a(Q("D14","K043",2,"<b>Hémianopsie latérale homonyme</b> — définition ?",
 ["Perte de la vision d'un seul œil","Perte de la même moitié du champ visuel sur les deux yeux","Vision double","Perte de la vision centrale des deux yeux"],"0100",
 "HLH : moitié du champ visuel amputée, du même côté pour les deux yeux (atteinte des voies visuelles ou du cortex occipital).","Troubles visuels"))
a(Q("D15","K044",2,"Diplopie au cours d'un AVC — <b>origine la plus probable</b> ?",
 ["Lobe frontal","Rétine","Lobe temporal","Nerfs crâniens oculomoteurs (tronc cérébral)"],"0001","Diplopie : atteinte des nerfs crâniens responsables des mouvements oculaires.","Troubles visuels"))
a(Q("D16","K045",1,"Suspicion d'AVC — éléments de l'<b>évaluation clinique initiale</b> ?",
 ["Vigilance et pupilles","Constantes vitales et glycémie capillaire","Respiration, encombrement, fausses routes","Ponction lombaire systématique"],"1110",
 "Évaluation : neurologique (gravité : vigilance, pupilles ; déficit), constantes + glycémie capillaire, respiration/encombrement/fausses routes.","Évaluation clinique"))
a(Q("D17","K046",2,"Suspicion d'AVC — <b>pourquoi la glycémie capillaire en priorité</b> ?",
 ["Une hyperglycémie contre-indique l'imagerie","La glycémie entre dans le calcul du NIHSS","Une hypoglycémie peut mimer un AVC","Pour calculer la dose d'insuline avant le scanner"],"0010",
 "Une hypoglycémie peut donner un déficit focal : la glycémie capillaire est faite avant l'examen neurologique.","Glycémie"))
a(Q("D18","K046",2,"Hémiparésie brutale ; glycémie capillaire à 0,40 g/L. <b>Conduite</b> ?",
 ["AVC certain : transfert immédiat sans corriger la glycémie","Évoquer une hypoglycémie mimant un AVC : resucrer puis réévaluer","Glycémie sans rapport avec le déficit","Attendre la régression spontanée (AIT probable)"],"0100",
 "L'hypoglycémie peut mimer un AVC : on la corrige et on réévalue le déficit (sans retarder la filière si le déficit persiste).","Glycémie"))
a(Q("D19","K047",2,"Score NIHSS — <b>étendue</b> ?",
 ["0 à 10","3 à 15","0 à 42","0 à 100"],"0010","NIHSS : 0 à 42 (3 à 15 = Glasgow).","NIHSS"))
a(Q("D20","K047",1,"Score NIHSS — <b>utilisation</b> ?",
 ["À l'examen initial, pour la sévérité de l'AVC","Tous les jours, pour suivre l'amélioration ou l'aggravation","Pour distinguer ischémie et hémorragie","Pour remplacer l'imagerie si le score est faible"],"1100",
 "NIHSS : sévérité initiale puis suivi quotidien. Seule l'imagerie distingue ischémie et hémorragie.","NIHSS"))
a(Q("D21","K047",2,"Score NIHSS — <b>un score élevé</b> signifie ?",
 ["Un meilleur état neurologique","Un déficit plus sévère","Une hémorragie","Une meilleure vigilance"],"0100","Plus le NIHSS est élevé, plus le déficit est sévère.","NIHSS"))
a(Q("D22","K048",1,"Score NIHSS — <b>items évalués</b> ?",
 ["Conscience et orientation","Champ visuel","Paralysie faciale","Glycémie capillaire"],"1110","La glycémie n'est pas un item du NIHSS.","NIHSS"))
a(Q("D23","K048",1,"Score NIHSS — autres <b>items évalués</b> ?",
 ["Dysarthrie","Aphasie","Négligence (extinction)","Réflexes ostéotendineux"],"1110","Les réflexes ostéotendineux ne font pas partie du NIHSS.","NIHSS"))
a(Q("D24","K048",2,"Score NIHSS — <b>durée de maintien demandée au membre supérieur</b> tendu ?",
 ["5 secondes","10 secondes","30 secondes","1 minute"],"0100","Membre supérieur : 10 s ; membre inférieur : 5 s.","NIHSS"))
a(Q("D25","K048",2,"Score NIHSS — <b>durée de maintien demandée au membre inférieur</b> ?",
 ["2 secondes","5 secondes","10 secondes","30 secondes"],"0100","Membre inférieur : 5 s ; membre supérieur : 10 s.","NIHSS"))
NIHSS_X="✎ Modifié par rapport au cours : la note de cours donnait « 0-5 mineur, 5-15 moyen, ≥ 15 sévère » (bornes qui se chevauchent, « pas à connaître par cœur ») → échelle de référence : 0 pas de symptôme, 1-4 mineur, 5-15 modéré, 16-20 modéré à sévère, 21-42 sévère."
NIHSS_W=["Web — WikEM, NIH Stroke Scale (FR), https://wikem.org/wiki/NIH_Stroke_Scale/fr"]
a(Q("D26","K049",2,"Score NIHSS de <b>1 à 4</b> — sévérité ?",
 ["AVC mineur","AVC modéré","AVC modéré à sévère","AVC sévère"],"1000","1-4 : AVC mineur.","NIHSS",x=NIHSS_X,w=NIHSS_W))
a(Q("D27","K049",2,"Score NIHSS de <b>5 à 15</b> — sévérité ?",
 ["AVC mineur","AVC modéré","AVC modéré à sévère","AVC sévère"],"0100","5-15 : AVC modéré.","NIHSS",x=NIHSS_X,w=NIHSS_W))
a(Q("D28","K049",2,"Score NIHSS de <b>21 à 42</b> — sévérité ?",
 ["AVC mineur","AVC modéré","AVC modéré à sévère","AVC sévère"],"0001","21-42 : AVC sévère (16-20 : modéré à sévère).","NIHSS",x=NIHSS_X,w=NIHSS_W))

# ---------- E. Alerte thrombolyse ----------
a(Q("E01","K050",2,"« <b>Time is brain</b> » — signification ?",
 ["Le cerveau récupère toujours s'il est traité dans les 24 h","L'imagerie doit attendre la stabilisation du patient","Chaque minute de retard entraîne une perte irréversible de neurones","Le NIHSS doit être répété toutes les minutes"],"0010",
 "Chaque seconde compte car la perte neuronale est irréversible.","Urgence"))
a(Q("E02","K051",2,"Alerte thrombolyse — <b>question fondamentale</b> à poser (patient, témoins) ?",
 ["Heure du dernier repas","Heure de début des symptômes","Date du dernier bilan sanguin","Antécédents familiaux d'AVC"],"0100",
 "L'heure de début des symptômes conditionne les traitements de reperfusion.","Heure de début"))
a(Q("E03","K051",2,"Alerte thrombolyse — <b>pourquoi l'heure de début est-elle capitale</b> ?",
 ["Elle détermine si l'AVC est ischémique ou hémorragique","Elle permet de calculer le NIHSS","Elle détermine le choix entre IRM et scanner","Elle conditionne la possibilité d'un traitement de reperfusion"],"0001",
 "Thrombolyse < 4h30, thrombectomie jusqu'à 6-24 h : sans heure de début, pas de décision de reperfusion.","Heure de début"))
a(Q("E04","K052 K053",1,"Alerte thrombolyse — <b>mesures à l'arrivée</b> ?",
 ["Pose de 2 voies veineuses périphériques","Bilan sanguin en urgence","ECG","Sondage urinaire systématique"],"1110",
 "2 VVP, bilan sanguin, ECG. Pas de sondage systématique (p. 18 : dépister un globe au bladder-scan).","Bilan d'urgence"))
a(Q("E05","K053",1,"Alerte thrombolyse — <b>examens biologiques</b> en urgence ?",
 ["NFS-plaquettes","TP-TCA","βHCG chez la femme jeune","Gaz du sang artériels systématiques"],"1110",
 "Bilan : NFS-plaquettes, TP-TCA (INR si AVK), fibrinogène, glycémie, βHCG si femme jeune, groupe-RAI, iono-urée-créatinine.","Bilan d'urgence"))
a(Q("E06","K053",1,"Alerte thrombolyse — autres <b>examens biologiques</b> ?",
 ["Glycémie","Groupe sanguin, Rhésus, RAI","Ionogramme, urée, créatinine","D-dimères"],"1110","Les D-dimères ne font pas partie du bilan d'alerte thrombolyse du cours.","Bilan d'urgence"))
a(Q("E07","K053",2,"Bilan d'alerte thrombolyse — <b>dans quel cas doser l'INR</b> ?",
 ["Toujours chez l'homme","Si traitement par antivitamine K","En cas d'hyperglycémie","Seulement après la thrombolyse"],"0100","INR si traitement par AVK (anticoagulant = contre-indication potentielle).","Bilan d'urgence"))
a(Q("E08","K054",2,"Procédure d'alerte thrombolyse — <b>orientation du patient à l'arrivée</b> ?",
 ["Box des urgences générales pour bilan complet","Hospitalisation en cardiologie","Transfert direct en radiologie pour imagerie cérébrale","Service de neurologie conventionnelle"],"0010",
 "Transfert direct en radiologie (IRM-ARM +++, ou scanner) pour gagner du temps.","Imagerie en urgence"))
a(Q("E09","K055",1,"Alerte thrombolyse — <b>évaluation clinique</b> par l'équipe UNV ?",
 ["Interrogatoire : antécédents, traitements, allergies","Constantes : TA, FC, glycémie capillaire","Score NIHSS","Électroencéphalogramme"],"1110","Interrogatoire, constantes (TA +++), examen neuro avec NIHSS ; critères d'inclusion/exclusion.","Évaluation"))
a(Q("E10","K056",2,"Choix du traitement de reperfusion — <b>3 critères</b> ?",
 ["Âge ; sexe ; poids","Heure ; sévérité ; terrain","Heure ; température ; groupe sanguin","Sévérité ; taille ; NIHSS de la veille"],"0100","Traitement choisi selon l'heure, la sévérité et le terrain.","Décision"))
a(Q("E11","K057 K079",0,"Filière de soins AVC",
 ["La filière d'amont comprend SAMU, pompiers et urgences","Le patient est hospitalisé en UNV ou USINV","La filière d'aval peut être un SSR (rééducation, gériatrie)","La rééducation ne commence qu'après la sortie d'UNV"],"1110",
 "4. Faux : rééducation dès le départ en UNV (p. 15).","Filière"))
a(Q("E12","K058",2,"Prise en charge dans un centre adapté (UNV) — <b>réduction du risque de mortalité</b> selon la note de cours ?",
 ["5 %","20 %","50 %","80 %"],"0100",
 "Note de cours : −20 % de mortalité en UNV. (Diapo p. 15 : −30 % de mortalité et handicap grâce à la prévention des complications, autre critère.)","Filière"))

# ---------- F. Imagerie ----------
a(Q("F01","K060",2,"AVC — <b>examen d'imagerie de référence</b> ?",
 ["Scanner cérébral sans injection","IRM cérébrale","Écho-doppler des troncs supra-aortiques","Radiographie du crâne"],"0100","IRM ++++ > scanner (TDM), mais les deux permettent de décider.","Imagerie"))
a(Q("F02","K061",2,"IRM — <b>séquence positive le plus précocement</b> dans l'infarctus ?",
 ["FLAIR","T2*","Diffusion","Angio-IRM (ARM)"],"0010","La diffusion est la plus rapidement positive (hypersignal).","Séquences IRM"))
a(Q("F03","K061",2,"IRM de diffusion — <b>aspect d'un infarctus récent</b> ?",
 ["Hyposignal (noir)","Hypersignal (blanc)","Normal pendant 24 h","Hyperdensité"],"0100","Infarctus récent : hypersignal (blanc) en diffusion. « Densité » = scanner.","Séquences IRM"))
a(Q("F04","K062",2,"IRM FLAIR — <b>délai</b> à partir duquel l'infarctus devient visible ?",
 ["Environ 30 minutes","Environ 4h30","Environ 24 heures","Environ 6 jours"],"0100","FLAIR : hypersignal à partir d'environ 4h30 après le début des symptômes.","Séquences IRM"))
a(Q("F05","K062",2,"Patient découvert au réveil avec une hémiplégie (heure inconnue). IRM : hypersignal en diffusion, FLAIR normale. <b>Interprétation</b> ?",
 ["Infarctus de plus de 4h30 : trop tard pour la thrombolyse","Hémorragie intracérébrale","AIT sans lésion","Infarctus probablement de moins de 4h30"],"0001",
 "Diffusion positive + FLAIR négative = infarctus récent, probablement < 4h30 (utile quand l'heure de début est inconnue).","Séquences IRM"))
a(Q("F06","K063",2,"Hémorragie intracérébrale — <b>aspect en imagerie</b> ?",
 ["Scanner : hyperdensité (blanc) ; IRM T2* : hyposignal (noir)","Scanner : hypodensité (noir) ; IRM T2* : hypersignal (blanc)","Scanner normal ; IRM : hypersignal en diffusion seulement","Scanner : hypodensité ; IRM T2* : normale"],"1000",
 "Hémorragie : blanche au scanner, noire en T2*. L'ischémie récente est blanche en diffusion.","Hémorragie en imagerie"))
a(Q("F07","K064",2,"Déficit brutal ; scanner cérébral sans injection normal. <b>Ce que cela permet de dire</b> ?",
 ["Il n'y a pas d'AVC","L'AVC date de façon certaine de moins de 4h30","Pas d'hémorragie : thrombolyse possible si le délai depuis le début des symptômes est < 4h30","Une hémorragie méningée est définitivement exclue"],"0010",
 "Le scanner élimine l'hémorragie mais ne date pas l'infarctus (souvent invisible au début). Le délai vient de l'heure de début. 4. Faux : le scanner est négatif dans 10 % des HSA.","Scanner",
 x="✎ Modifié par rapport au cours : la note « si on voit rien au scanner ça veut dire < 4h30 » est inexacte → un scanner normal élimine une hémorragie, le délai se juge sur l'heure de début des symptômes (diapo : « traiter par rt-PA si < 4h30 »)."))
a(Q("F08","K064",2,"Scanner — <b>pour visualiser l'occlusion artérielle</b> ?",
 ["Scanner sans injection","Injection de produit de contraste (angioscanner)","Séquence de diffusion","Radiographie standard"],"0100","Il faut une séquence injectée (angioTDM) pour voir les vaisseaux.","Scanner"))
a(Q("F09","K065",2,"IRM — <b>séquence pour visualiser l'occlusion</b> du polygone de Willis ?",
 ["Diffusion","FLAIR","T2*","Angio-IRM (ARM)"],"0001","ARM du polygone de Willis : montre l'occlusion artérielle.","Séquences IRM"))
