# Paramètres du cours (un fichier par cours)
NOM = "UE 2.8 - CM2 BPCO"
PDF = "CM SSU 2 BPCO - export onenote.pdf"
PDFNAME = "CM SSU 2 BPCO - export onenote.pdf"
TYPE = "CM SSU"
CONTEXTE = "IFSI - UE 2.8 Processus obstructifs - CM SSU CM2 BPCO"
DECK = "IFSI::QCM::Semestre 3::UE 2.8 - Processus obstructifs::CM2 BPCO"
PREFIX = "ue2-8_cm2-bpco"
MODEL = "Claude Opus 5.5"
VERSION = "1.8.1"
REF_APKG = "../Outils/Type de note QCMs.apkg"
QFILES = ["q1", "q2", "q3", "q4", "q5", "qv"]
CORRECTIONS = [("w1", "W"), ("w2", "W"), ("w3", "W"), ("w4", "W"), ("fmt", "W"), ("w5", "W")]

DOMAINE = "BPCO"
DOMAINE_VOCAB = "Vocabulaire"
TEXT_REPL = [(r"\bAdvice\b", "Advise"), 
    (r"\bGDS\b", "gaz du sang"), (r"\bSN\b", "substituts nicotiniques"), (r"\b(SatO2|SaO2)\b", "SpO2"),
    (r"\bEP\b", "embolie pulmonaire"), (r"\bOAP\b", "œdème pulmonaire"), (r"\bVNI\b", "ventilation non invasive"),
    (r"\bBDLA\b", "bronchodilatateurs de longue durée d'action"), (r"\bBDCA\b", "bronchodilatateurs de courte durée d'action"),
    (r"\bCSI\b", "corticoïdes inhalés"), (r"\bIVD\b", "insuffisance cardiaque droite"), (r"\bFR\b", "fréquence respiratoire"),
    (r"\bOMI\b", "œdèmes des membres inférieurs"), (r"\bPO\b", "per os"),
]
SIGLES_OK = ["BPCO", "IV", "II", "III", "I", "IDE", "O2", "CO2", "MRC"]
