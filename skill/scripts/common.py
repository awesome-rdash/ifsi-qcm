from dataclasses import dataclass, field

@dataclass
class Q:
    id: str
    ks: str
    mode: int          # 0 Kprim, 1 QCM, 2 QCS
    q: str             # énoncé (sans gras global : ajouté automatiquement)
    props: list
    truth: str
    expl: str
    notion: str = ""   # vide = titre réduit à la section
    titre: str = None  # titre imposé (R11)
    x: str = None      # ✎ / ⚠ / Complément
    w: list = field(default_factory=list)
    img: tuple = None  # (xref, box, nom)
    pg: list = field(default_factory=list)
    dz: dict = field(default_factory=dict)   # {index proposition: raison} erreurs dangereuses
    allow: list = field(default_factory=list)  # mots autorisés malgré le contrôle de répétition
    lenok: bool = False  # exception justifiée au contrôle de longueur
    vign: bool = False   # vignette clinique
    why: list = field(default_factory=list)  # X1 : une justification d'une ligne par proposition, dans l'ordre de props
    ok: dict = field(default_factory=dict)   # exceptions validées : {code de règle: raison}, ex. {"M11": "validée par l'étudiant (R-25)"}

    def __post_init__(self):
        self.ks = self.ks.split()
        self.w = self.w or []


# ---------- citations du champ Sources (S3, S9, X5) : à utiliser dans w=[...] et dans les sources du glossaire ----------
def cite(reference, page):
    """Référence citée sur une diapo du cours (rang 2 des bonnes réponses, S3)."""
    return f"{reference} (cité par le support de cours, p. {page})"

def college(nom, edition, annee, chapitre, page, item=None):
    """Chapitre d'un Collège (S9) ; page = page du PDF d'origine, telle que l'index la donne."""
    it = f", item {item}" if item else ""
    return f"Collège — {nom}, {edition}, {annee}, chap. « {chapitre} »{it}, p. {page} du PDF d'origine"

def web(organisme, titre, url):
    """Source en ligne fiable (S3, rang après les Collèges)."""
    return f"Web — {organisme}, {titre}, {url}"
