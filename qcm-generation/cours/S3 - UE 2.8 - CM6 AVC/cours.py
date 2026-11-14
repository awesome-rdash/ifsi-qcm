# Paramètres du cours (un fichier par cours)
NOM = "UE 2.8 - CM6 AVC"
PDF = "CM6 AVC.pdf"   # PDF copié dans le dossier du cours (espace de travail)
PDFNAME = "CM6 AVC.pdf"
TYPE = "CM SSU"
CONTEXTE = "IFSI - UE 2.8 Processus obstructifs - CM SSU AVC"
DECK = "IFSI::QCM::Semestre 3::UE 2.8 - Processus obstructifs::CM6 - AVC"
PREFIX = "ue2-8_cm6-avc"          # minuscules, sans espace : préfixe des images et des GUID
MODEL = "Claude Opus 5.5"
VERSION = "1.7"
REF_APKG = "../Type de note QCMs.apkg"   # copié depuis Anki\Prompts\Outils\exemple CM6 AVC
QFILES = ["r1", "r2", "r3", "r4", "r5", "r6"]
CORRECTIONS = [("fixprops", "FIX"), ("fixprops", "CONV"), ("fixprops", "RELECTURE"), ("autonomie", "AUTO"), ("v13", "FIX"), ("v17", "FIX")]

DOMAINE = "AVC"   # R8 : préfixe de chaque question
DOMAINE_VOCAB = "Vocabulaire"   # R8 : domaine des cartes de vocabulaire
# Sigles écrits en toutes lettres quand ils n'apportent rien (X3)
TEXT_REPL = [
    (r"\b(SatO2|SaO2)\b", "SpO2"), (r"\bTA\b", "PA"), (r"\bHGT\b", "glycémie capillaire"), (r"\bdextro\b", "glycémie capillaire"),
    (r"\bCI\b", "contre-indication"), (r"\bFDR\b", "facteurs de risque"), (r"\bMS\b", "membre supérieur"), (r"\bMI\b", "membre inférieur"),
    (r"\bSE\b", "seringue électrique"), (r"\bCAT\b", "conduite à tenir"), (r"\b(TAS|PAS)\b", "pression systolique"), (r"\b(TAD|PAD)\b", "pression diastolique"),
    (r"\bDSC\b", "débit sanguin cérébral"), (r"\b2 VVP\b", "2 voies veineuses périphériques"), (r"\bVVP\b", "voie veineuse périphérique"),
    (r"\bSSR\b", "soins de suite et de réadaptation"), (r"\bIII douloureux", "atteinte douloureuse du nerf oculomoteur"),
    (r"\(dont la PICA\)", "(dont la cérébelleuse postéro-inférieure)"), (r"\(PICA\)", "(cérébelleuse postéro-inférieure)"), (r"\(PICA…\)", "(cérébelleuse postéro-inférieure…)"),
]
SIGLES_OK = ["II"]   # « angiotensine II »
