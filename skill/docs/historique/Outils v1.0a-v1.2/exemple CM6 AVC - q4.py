# Questions d'imagerie avec image recadrée (sans légendes)
from common import Q
QS = []
a = QS.append
a(Q("F10","K060 K061",2,"Même patient (hémiplégie gauche depuis 4 h) : scanner (à gauche), IRM FLAIR (au centre), IRM de diffusion (à droite). <b>Que montre cette comparaison</b> ?",
 ["Le scanner montre mieux l'infarctus que l'IRM","La diffusion montre l'infarctus alors que le scanner est quasi normal","Les trois examens sont normaux","Il s'agit d'une hémorragie visible sur les trois coupes"],"0100",
 "IRM >> TDM à la phase aiguë : la diffusion est la séquence la plus précocement positive (hypersignal blanc), le scanner est souvent normal au début.","Imagerie",
 img=(79,(52,172,1070,515),"img-tdm-flair-dwi")))
a(Q("F11","K061",2,"IRM de diffusion d'un patient avec hémiplégie gauche brutale. <b>La large zone blanche</b> correspond à ?",
 ["Une hémorragie","Un aspect normal","Un infarctus cérébral récent (hypersignal)","Un œdème lié à une tumeur"],"0010",
 "Hypersignal (blanc) en diffusion = infarctus récent (tissu déjà nécrosé). Une hémorragie apparaît en hyposignal (noir) en T2*.","Imagerie",
 img=(79,(727,172,1070,515),"img-dwi")))
a(Q("F12","K065",2,"Angio-IRM (ARM) du polygone de Willis chez un patient avec infarctus aigu. <b>La flèche</b> montre ?",
 ["Un anévrisme","Une malformation artério-veineuse","L'absence d'une artère : occlusion artérielle","Un saignement actif"],"0010",
 "ARM : l'artère occluse n'apparaît pas. Une occlusion est retrouvée dans environ 80 % des infarctus aigus selon la diapo.","Imagerie",
 img=(79,(785,527,1088,735),"img-arm")))
a(Q("F13","K063 K123",2,"Scanner cérébral <b>sans injection</b> chez un patient avec hémiplégie brutale. <b>Interprétation</b> ?",
 ["Hématome intraparenchymateux (hyperdensité spontanée)","Infarctus cérébral constitué (hypodensité)","Scanner normal","Hémorragie méningée isolée"],"1000",
 "Hémorragie = hyperdensité (blanc) spontanée au scanner sans injection. → Pas de thrombolyse.","Imagerie",
 img=(145,(72,290,365,640),"img-tdm-hematome"), pg=[23]))
a(Q("F14","K063",2,"IRM <b>T2*</b> du même patient (hématome). <b>La zone noire</b> correspond à ?",
 ["Un infarctus récent","Du liquide céphalorachidien","L'hémorragie (hyposignal)","Un artefact"],"0010",
 "T2* : l'hémorragie apparaît en hyposignal (noir). Infarctus récent = hypersignal en diffusion.","Imagerie",
 img=(145,(757,370,1045,705),"img-t2-hematome"), pg=[23]))
a(Q("F15","K064 K068",2,"Déficit brutal depuis 2 h, aucune contre-indication connue. Scanner sans injection ci-dessous. <b>Conduite</b> ?",
 ["Ne pas traiter : hémorragie","Pas de saignement visible : thrombolyse IV possible (< 4h30)","Attendre une IRM à J1 avant toute décision","Aspirine seule"],"0100",
 "Scanner sans sang + délai < 4h30 depuis le début des symptômes + pas de CI → rt-PA (± angioTDM pour rechercher une occlusion proximale → thrombectomie).","Imagerie",
 img=(84,(462,250,640,515),"img-tdm-normal")))
