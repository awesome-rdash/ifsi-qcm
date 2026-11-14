# X1/X6 : une ligne par élément dans les explications qui énumèrent (« ; »)
import importlib, cours as C
W = {}
for m in [f for f in C.QFILES]:
    for q in importlib.import_module(m).QS:
        if q.expl.count(";") >= 2 and "<br>" not in q.expl:
            W[q.id] = {"expl": q.expl.replace(" ; ", " ;<br>")}
