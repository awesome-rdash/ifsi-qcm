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

    def __post_init__(self):
        self.ks = self.ks.split()
        self.w = self.w or []
