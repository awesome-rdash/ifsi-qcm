# QCM Anki — pourquoi la génération consomme autant de tokens (analyse du 2026-11-13)

> Analyse des conversations « QCM BPCO » et « Correction QCM anti-AVC » (12/11/2026), pour la conversation « Skill – conception ». Les compteurs exacts de tokens ne sont pas accessibles : les chiffres ci-dessous viennent du déroulé des conversations (nombre d'appels, de sous-agents, taille des fichiers écrits). Les ordres de grandeur en tokens sont des **estimations**.

## Ce qui a été mesuré

| | BPCO (génération v1.7 puis v1.8.1) | AVC (régénération v1.8.1) |
|---|---|---|
| Cartes | 253 | 371 |
| Pages du cours lues en image par l'agent principal | 33 (+ 2 clichés) | 29 |
| Appels d'outils dans un seul message | 125 (génération), 88 (corrections) | plusieurs centaines sur la conversation (122 tours) |
| Texte écrit par l'agent (fichiers de questions, corrections) | ≈ 158 000 + 62 000 + 46 000 caractères | fichiers de corrections fx00 à fx29 + justification de ≈ 1 500 propositions |
| Recherches web | 18 + 36 + 16 + 6 lectures de pages (surtout pour sourcer le glossaire) | nombreuses (glossaire, R-1 à R-37) |
| Sous-agents relecteurs | 12 (tour 1 : 3 aveugles + 2 règles ; tour 2 : 5 ; tour 3 : 2) | **29** (tour 1 : 4 aveugles + 8 règles ; tour 2 : 4 + 8 ; tour 3 : 2 + 3) |
| Défauts trouvés par le relecteur des règles | — | **857 KO** au tour 1, 206 au tour 2 |

## Les causes, par ordre d'importance

1. **Les relectures multiplient le cours.** Chaque sous-agent repart de zéro : il relit tout le cours (texte + 29 à 60 images de pages, souvent 60 000 à 100 000 tokens), les règles (`regles.md`) et son lot de cartes, puis écrit son rapport. 29 sous-agents pour l'AVC, c'est le cours relu 29 fois. C'est probablement le premier poste de dépense.
2. **La génération ne respecte pas les règles du premier coup.** 857 non-conformités au tour 1 sur 371 cartes : il a fallu 3 tours de relecture et des dizaines de fichiers de corrections. Chaque défaut que `build.py` ne détecte pas coûte un aller-retour avec un sous-agent.
3. **Le contexte de l'agent principal grossit et est renvoyé à chaque appel.** Les images de pages lues au début (≈ 1 500 tokens chacune) et les résultats d'outils restent dans le contexte. Chacun des 100 à 200 appels suivants renvoie tout ce contexte. Le cache réduit le coût, mais l'usage reste compté.
4. **Tout est écrit par le modèle.** Fichiers de questions, justification de chaque proposition (règle X1, ≈ 1 000 à 1 500 justifications par paquet), corrections : ce sont des tokens de sortie, les plus chers.
5. **Le glossaire est sourcé à neuf pour chaque cours.** Des dizaines de recherches et de lectures web par paquet, dont les résultats entrent dans le contexte.
6. **Une seule conversation longue pour tout.** La conversation AVC a mélangé 37 retours, la mise à jour des règles et la régénération (122 tours) : la régénération tourne avec tout cet historique en contexte.

## Pistes, de la plus rentable à la moins rentable

1. **Transcrire le cours une fois.** Une étape unique transforme le PDF en `cours.md` (texte de chaque page + description des schémas et tableaux). L'agent principal et tous les relecteurs lisent ce fichier ; les images ne servent plus qu'aux questions d'imagerie et aux vérifications ponctuelles.
2. **Moins de sous-agents, des lots plus gros.** Le coût d'un relecteur vient surtout de la lecture du cours, pas du nombre de cartes : 2 relecteurs (un à l'aveugle, un des règles) pour tout le paquet au lieu de 12. Le relecteur des règles n'a pas besoin des images, seulement du texte.
3. **Plus de contrôles automatiques dans `build.py`, moins de relecture par IA.** Tout ce qui se vérifie par programme (vote majoritaire, 2 × 2, mots de la question repris dans la réponse, proposition non justifiée, terme technique hors glossaire, titre qui nomme la réponse) est bloquant dans le script, gratuit et immédiat. Le relecteur des règles ne garde que ce qui demande un jugement.
4. **Générer juste du premier coup.** Rédiger section par section avec la grille de relecture sous les yeux, et lancer `build.py --report-only` après chaque section plutôt qu'à la fin.
5. **Limiter les tours.** Un 2e tour seulement sur les cartes corrigées et seulement pour le type de défaut corrigé ; pas de 3e tour sauf erreur médicale.
6. **Modèle plus léger pour les relecteurs.** Le relecteur à l'aveugle peut tourner sur un modèle moins coûteux (paramètre `model` des sous-agents) ; garder Opus pour la rédaction et les mauvaises réponses.
7. **Glossaire commun à tous les cours.** Les définitions sourcées vont dans le glossaire général (`glossaire.py`) et sont réutilisées ; seuls les termes nouveaux sont recherchés. Les référentiels déposés dans le Drive (collèges) peuvent remplacer une partie des recherches web.
8. **Mises à jour incrémentales.** Quand une règle change, `build.py` liste les cartes concernées et on ne réécrit que celles-là (GUID stables), au lieu de régénérer tout le paquet.
9. **Conversations courtes.** Les retours se discutent dans une conversation, la régénération se fait dans une conversation neuve qui part du document de retours (D93).
