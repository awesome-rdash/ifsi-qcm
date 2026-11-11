# Feature Specification: Site de révision QCM IFSI

**Feature Branch**: `001-site-revision-qcm`

**Created**: 2026-11-11

**Status**: Draft

**Input**: User description: « Site de révision de QCM pour les étudiants en soins infirmiers (IFSI),
à partir des questions générées pour des paquets Anki. Il permet à quelqu'un qui n'utilise pas Anki
de s'entraîner, de connaître sa note et de savoir quels cours retravailler. » (texte complet fourni
à `/speckit-specify`, repris ci-dessous en exigences).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Entrer sur le site (Priority: P1)

L'étudiant saisit le mot de passe de la promotion. Le site s'en souvient sur cet appareil jusqu'à
ce qu'il se déconnecte.

**Why this priority**: porte d'entrée de tout le reste.

**Independent Test**: ouvrir le site, saisir un mauvais puis le bon mot de passe, recharger.

**Acceptance Scenarios**:

1. **Given** un appareil jamais connecté, **When** l'étudiant ouvre le site, **Then** seul l'écran
   de mot de passe est visible.
2. **Given** l'écran de mot de passe, **When** il saisit un mauvais mot de passe, **Then** un
   message d'erreur s'affiche et il reste sur l'écran.
3. **Given** le bon mot de passe saisi, **When** il recharge la page plus tard, **Then** il arrive
   directement à l'accueil.
4. **Given** un étudiant connecté, **When** il se déconnecte, **Then** l'écran de mot de passe
   revient.

---

### User Story 2 - Composer une session (Priority: P1)

L'étudiant voit l'arbre Semestre → UE → Cours, avec le nombre de questions disponibles à chaque
niveau. Il coche un cours, une UE, un semestre ou tout. Pour chaque cours retenu, il choisit le
nombre de questions (20 par défaut, « toutes » possible) ou applique un même nombre à tous les cours
cochés. Il peut filtrer par importance (I0 à I3) et choisit le mode de correction (après chaque
question ou à la fin). Le total de la session est affiché avant de commencer.

**Why this priority**: sans session, pas de révision.

**Independent Test**: cocher une UE, régler les nombres et l'importance, vérifier le total affiché
puis lancer la session.

**Acceptance Scenarios**:

1. **Given** l'accueil, **When** l'étudiant coche une UE, **Then** tous ses cours sont cochés et
   le total se met à jour.
2. **Given** un filtre « I0 et I1 », **When** il regarde l'arbre, **Then** les compteurs ne
   comptent que les questions I0 et I1.
3. **Given** un cours de 300 questions et un nombre demandé de 20, **When** la session démarre,
   **Then** 20 questions de ce cours sont tirées au hasard.
4. **Given** plusieurs cours, **When** la session démarre, **Then** les questions sont mélangées
   entre cours et les propositions de chaque question sont mélangées.
5. **Given** un nombre demandé supérieur au disponible, **When** la session démarre, **Then**
   toutes les questions disponibles du cours sont retenues.

---

### User Story 3 - Répondre (Priority: P1)

Une question par écran : contexte, titre, question, image éventuelle, 4 propositions. QCS : choix
unique. QCM : cases à cocher. Kprim : Vrai/Faux pour chaque affirmation. L'étudiant valide ou passe,
et voit sa progression (question n / total).

**Why this priority**: cœur de l'entraînement.

**Independent Test**: lancer une session de 3 questions (une de chaque format) et y répondre.

**Acceptance Scenarios**:

1. **Given** une question QCS, **When** l'étudiant choisit une proposition, **Then** les autres
   sont désélectionnées.
2. **Given** une question Kprim, **When** il valide, **Then** chaque affirmation a un jugement
   Vrai, Faux ou aucun.
3. **Given** n'importe quelle question, **When** il appuie sur « Passer », **Then** elle compte 0
   et la suivante s'affiche.
4. **Given** le mode « correction après chaque question », **When** il valide, **Then** la
   correction s'affiche avant la question suivante.
5. **Given** le mode « correction à la fin », **When** il valide, **Then** la question suivante
   s'affiche sans correction.

---

### User Story 4 - Correction d'une question (Priority: P1)

Pour chaque proposition : si elle est vraie ou fausse (la couleur suit la vérité de la
proposition, pas la réponse de l'étudiant), ce que l'étudiant a répondu, et ses erreurs signalées
à part (barre, symbole et texte : « cochée à tort », « oubliée »). Puis les points obtenus, les
informations complémentaires (explication, signalements ⛔ mis en évidence, ✎ et ⚠, glossaire),
la page du cours en image et les sources.

**Why this priority**: c'est là que l'étudiant apprend.

**Independent Test**: répondre faux à une question signalée ⛔ et vérifier la correction.

**Acceptance Scenarios**:

1. **Given** une question corrigée, **When** l'écran s'affiche, **Then** chaque proposition montre
   « vraie » ou « fausse », la réponse donnée, et un verdict ✓/✗ en texte.
2. **Given** une bonne réponse que l'étudiant n'a pas cochée, **When** la correction s'affiche,
   **Then** la proposition apparaît comme vraie (vert) avec l'erreur « oubliée » signalée à part.
3. **Given** une question dont les informations contiennent ⛔, **When** la correction s'affiche,
   **Then** le signalement est mis en évidence.
4. **Given** une question avec page de cours, **When** la correction s'affiche, **Then** l'image de
   la page est affichée sans action de l'étudiant ; elle n'est pas téléchargée avant la correction.

---

### User Story 5 - Bilan de fin de session (Priority: P1)

Note globale sur 20 et points sur le nombre de questions ; détail par semestre, par UE et par cours
(note, nombre de questions, cours les plus faibles et les plus forts mis en évidence) ; détail par
importance et par format ; liste des questions ratées ou partiellement réussies avec leur
correction ; bouton « Refaire mes erreurs ».

**Why this priority**: répond à « quels cours retravailler ».

**Independent Test**: finir une session de 5 questions avec des réponses connues et vérifier les
notes affichées.

**Acceptance Scenarios**:

1. **Given** 4 questions à 1 point et 1 à 0, **When** le bilan s'affiche, **Then** la note est
   16,00/20 et « 4 / 5 points ».
2. **Given** des questions ratées, **When** l'étudiant clique « Refaire mes erreurs », **Then** une
   nouvelle session démarre avec exactement les questions à moins de 1 point.
3. **Given** une session sur 3 cours, **When** le bilan s'affiche, **Then** le cours à la note la
   plus basse et celui à la note la plus haute sont signalés.

---

### User Story 6 - Reprendre une session interrompue (Priority: P2)

Si l'onglet est fermé en cours de session, l'étudiant peut la reprendre sur le même appareil.

**Why this priority**: confort ; les révisions sur téléphone sont souvent interrompues.

**Independent Test**: répondre à 2 questions, fermer l'onglet, rouvrir, reprendre.

**Acceptance Scenarios**:

1. **Given** une session en cours, **When** l'étudiant rouvre le site, **Then** l'accueil propose
   de reprendre ou d'abandonner la session.
2. **Given** une reprise, **When** la session continue, **Then** les réponses déjà données et la
   position sont conservées.

---

### User Story 7 - Historique (Priority: P3)

Les bilans des sessions passées sont conservés sur l'appareil, avec l'évolution de la note par
cours. L'étudiant peut tout effacer.

**Why this priority**: utile mais non indispensable.

**Independent Test**: faire deux sessions sur un même cours, ouvrir l'historique, effacer.

**Acceptance Scenarios**:

1. **Given** deux sessions terminées, **When** l'étudiant ouvre l'historique, **Then** il voit les
   deux bilans et les notes successives de chaque cours.
2. **Given** l'historique, **When** il choisit « Tout effacer » et confirme, **Then** l'historique,
   la session en cours et les préférences sont supprimés de l'appareil.

---

### User Story 8 - Ajouter un cours (Priority: P1, mainteneur)

Le mainteneur dépose le paquet Anki (`.apkg`) d'un cours dans le dossier prévu du dépôt et pousse.
La publication convertit le paquet et met à jour l'arbre et les compteurs sans autre intervention.

**Why this priority**: sans contenu, le site est vide.

**Independent Test**: déposer un `.apkg`, lancer la conversion, vérifier que le cours apparaît.

**Acceptance Scenarios**:

1. **Given** un nouveau `.apkg` dans le dossier, **When** la publication tourne, **Then** le cours
   apparaît dans l'arbre à sa place (semestre, UE) avec ses compteurs.
2. **Given** deux paquets du même cours (ancien et régénéré), **When** la conversion tourne,
   **Then** seul le plus récent est publié, sans doublon de question.
3. **Given** un paquet contenant une note d'un autre type que QCMs, **When** la conversion tourne,
   **Then** elle échoue avec un message qui nomme le paquet, et rien n'est publié.

### Edge Cases

- QCM où rien n'est coché : 0 point (pas d'erreur bloquante, l'étudiant peut valider à vide).
- Kprim avec un jugement manquant : 0 point.
- Filtre d'importance qui ne laisse aucune question : le bouton « Commencer » est désactivé.
- Stockage local indisponible (navigation privée) : le site fonctionne, sans mémoriser connexion,
  reprise ni historique.
- Propositions contenant « < » (ex. « < 160/90 mmHg ») : affichées telles quelles.
- Nouvelle publication pendant une session en cours : les questions déjà chargées restent valables ;
  une question disparue est retirée de la reprise.
- Hors connexion pendant une session : les questions déjà chargées restent utilisables ; les images
  non chargées affichent un message.

## Requirements *(mandatory)*

### Functional Requirements

**Accès**

- **FR-001**: Le site MUST demander le mot de passe de la promotion avant tout contenu et le
  comparer à une empreinte SHA-256 ; le mot de passe en clair MUST NOT figurer dans le dépôt.
- **FR-002**: Le site MUST mémoriser la connexion sur l'appareil et proposer « Se déconnecter ».

**Composition**

- **FR-010**: Le site MUST afficher l'arbre Semestre → UE → Cours avec le nombre de questions à
  chaque niveau, recalculé selon le filtre d'importance.
- **FR-011**: L'étudiant MUST pouvoir cocher un cours, une UE, un semestre ou tout.
- **FR-012**: Pour chaque cours coché, l'étudiant MUST pouvoir choisir un nombre de questions
  (défaut 20, « toutes » possible) et appliquer un même nombre à tous les cours cochés.
- **FR-013**: L'étudiant MUST pouvoir filtrer par importance (I0, I1, I2, I3, combinables).
- **FR-014**: L'étudiant MUST choisir le mode de correction : après chaque question ou à la fin.
- **FR-015**: Le total de la session MUST être affiché avant de commencer.
- **FR-016**: Les questions MUST être tirées au hasard dans chaque cours, puis mélangées entre
  cours ; les propositions de chaque question MUST être mélangées.

**Réponse et correction**

- **FR-020**: Une question par écran : contexte, titre, question, image éventuelle, 4 propositions,
  progression « n / total ».
- **FR-021**: QCS en choix unique, QCM en cases à cocher, Kprim en Vrai/Faux par affirmation.
- **FR-022**: L'étudiant MUST pouvoir valider ou passer ; une question passée vaut 0.
- **FR-023**: La correction MUST montrer, pour chaque proposition, si elle est vraie ou fausse
  (couleur selon la vérité de la proposition), la réponse donnée, et les erreurs de l'étudiant
  signalées séparément par symbole et texte.
- **FR-024**: La correction MUST montrer les points obtenus, les informations complémentaires
  telles quelles (⛔ mis en évidence), et les sources.
- **FR-025**: La page du cours en image MUST être affichée dans chaque correction ; elle n'est
  téléchargée qu'à l'affichage de la correction.
- **FR-026**: Le contenu des questions MUST être affiché sans réécriture ; le HTML est assaini
  (liste blanche de balises) avant affichage.

**Notation (type Sorbonne)** — chaque question vaut au plus 1 point.

- **FR-030**: QCS : 1 si la bonne réponse est choisie, 0 sinon.
- **FR-031**: QCM : au moins une proposition fausse cochée → 0 ; toutes les bonnes cochées et
  aucune fausse → 1 ; incomplète sans fausse cochée → 0,25 si une seule bonne cochée, 0,5 si deux
  ou plus ; rien coché → 0.
- **FR-032**: Kprim : 1 si les 4 jugements sont justes, 0 dès qu'un jugement est faux ou manquant.
- **FR-033**: Note sur 20 = (somme des points / nombre de questions) × 20, arrondie au centième.
- **FR-034**: Les règles FR-030 à FR-033 MUST être couvertes par des tests automatisés, cas
  limites compris.

**Bilan**

- **FR-040**: Le bilan MUST afficher la note globale sur 20 et « points / questions ».
- **FR-041**: Le bilan MUST détailler par semestre, UE et cours (note, nombre de questions) et
  signaler le cours le plus faible et le plus fort.
- **FR-042**: Le bilan MUST détailler par importance (I0 à I3) et par format (QCS, QCM, Kprim).
- **FR-043**: Le bilan MUST lister les questions à moins de 1 point avec leur correction.
- **FR-044**: « Refaire mes erreurs » MUST lancer une session avec exactement ces questions.

**Persistance**

- **FR-050**: Une session en cours MUST pouvoir être reprise sur le même appareil après fermeture.
- **FR-051**: Les bilans terminés MUST être conservés sur l'appareil (100 derniers), avec
  l'évolution de la note par cours.
- **FR-052**: L'étudiant MUST pouvoir effacer toutes les données conservées.
- **FR-053**: Aucune donnée MUST NOT quitter le navigateur.

**Contenu**

- **FR-060**: Les questions MUST provenir uniquement des paquets `.apkg` déposés dans le dépôt.
- **FR-061**: Semestre, UE et cours MUST être lus dans le nom du paquet Anki
  (`IFSI::QCM::Semestre <n>::UE <n°> - <intitulé>::<Cours>`), l'importance dans les étiquettes
  (`PSB::Importance::I0` à `I3`).
- **FR-062**: Chaque question MUST garder un identifiant stable (GUID Anki) ; un paquet régénéré
  remplace l'ancien sans doublon.
- **FR-063**: La conversion MUST échouer clairement si un paquet contient une note d'un autre type
  que QCMs.

### Key Entities

- **Cours** : semestre, UE (numéro, intitulé), nom, contexte, version et date de génération,
  questions.
- **Question** : GUID, format (QCS/QCM/Kprim), importance, titre, question, 4 propositions avec leur
  valeur vrai/faux, image éventuelle, informations complémentaires, pages du cours, sources,
  indicateur ⛔.
- **Session** : questions tirées (ordre et ordre des propositions), mode de correction, réponses,
  position.
- **Bilan** : date, note globale, points par question, détails par niveau, importance et format.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Un étudiant compose et lance une session de 20 questions en moins de 30 secondes.
- **SC-002**: Sur téléphone en 4G, l'accueil s'affiche en moins de 3 secondes.
- **SC-003**: Toutes les règles de notation ont un test automatisé ; 100 % passent avant chaque
  publication.
- **SC-004**: Ajouter un cours ne demande aucune modification de code : déposer, commit, push.
- **SC-005**: Tout l'usage est possible sur un écran de 360 px, au clavier, et avec un lecteur
  d'écran.

## Assumptions

- Nombre de questions par cours par défaut : 20.
- « Refaire mes erreurs » reprend les questions à moins de 1 point (ratées et partielles).
- Une question passée peut être validée à vide ; elle n'est pas reproposée dans la session.
- Si deux paquets décrivent le même cours, le plus récemment modifié est retenu.
- L'historique garde les 100 dernières sessions.
- Les étudiants utilisent un navigateur récent (moins de 2 ans).
- Le texte d'aide des questions (« une seule réponse », « une ou plusieurs ») fait partie du
  contenu et est affiché tel quel.

## Out of Scope

Comptes, classement entre étudiants, synchronisation entre appareils, répétition espacée,
édition des questions sur le site.
