# Constitution — Site de révision QCM IFSI

Site web de révision des QCM d'IFSI (soins infirmiers), publié sur GitHub Pages à l'adresse
`ifsi-github.jrouzier.fr`. Il permet à des étudiants qui n'utilisent pas Anki de faire les QCM
générés pour Anki.

## Core Principles

### I. Fidélité au contenu

Les questions, propositions, réponses, explications, signalements (⛔ erreur dangereuse, ✎ modifié
par rapport au cours, ⚠ non confirmé) et sources MUST être affichés tels qu'ils sont dans les
données exportées. Le site MUST NOT réécrire, corriger ni générer de contenu médical.

### II. Une seule source de vérité

Les questions viennent des paquets Anki (`.apkg`, type de note QCMs) produits par le générateur ;
le site les lit tels quels, sans export intermédiaire à maintenir. Le dépôt MUST NOT contenir de
question écrite à la main. Ajouter un cours = déposer son `.apkg` dans le dépôt, sans modifier le
code.

### III. Site statique

HTML, CSS et JavaScript servis par GitHub Pages. Pas de serveur, pas de base de données, pas de
compte utilisateur, pas de service tiers (ni analytics, ni CDN obligatoire, ni police externe).
Le site MUST fonctionner depuis n'importe quel hébergement statique.

### IV. Simplicité et faible maintenance

Le moins de dépendances possible ; JavaScript moderne sans framework tant que c'est suffisant.
Pas d'étape de construction obligatoire pour le code du site. Le mainteneur est un étudiant avec
très peu de temps : toute complexité ajoutée MUST être justifiée.

### V. Mobile d'abord

La plupart des révisions se font sur téléphone : tout MUST être utilisable d'une main sur un écran
de 360 px, puis s'adapter au PC. Le mode sombre suit le réglage du système.

### VI. Accessibilité

Navigation au clavier, contrastes suffisants, libellés lisibles par un lecteur d'écran, cibles
tactiles d'au moins 44 px. L'information MUST NOT être portée par la couleur seule (bonne/mauvaise
réponse indiquée aussi par un symbole ou un texte).

### VII. Vie privée

Aucune donnée ne quitte le navigateur. Les seules données conservées (session en cours,
préférences, historique) restent dans le stockage local du navigateur et MUST pouvoir être effacées
par l'utilisateur.

### VIII. Accès par mot de passe partagé

Un écran d'entrée demande le mot de passe de la promotion. C'est une porte d'entrée, pas une
protection : le dépôt est privé, mais les fichiers publiés par Pages sont publics, et c'est assumé.
Le mot de passe MUST NOT apparaître en clair dans le dépôt ni sur le site (seulement son empreinte
SHA-256).

### IX. Notation exacte et testée

Le calcul des scores suit strictement la règle de notation de la spécification et MUST être couvert
par des tests automatisés, cas limites compris. Toute modification de la règle met à jour les tests.

### X. Interface en français

Interface en français, avec le vocabulaire de l'IFSI (UE, CM, TD, semestre).

## Contraintes techniques

- Publication par GitHub Actions vers GitHub Pages, domaine personnalisé via le fichier `CNAME`.
- Les `.apkg` sont convertis en JSON par un script lancé par l'Action avant chaque publication ;
  les fichiers produits (`data/`) ne sont pas versionnés.
- Toute dépendance retenue est copiée dans le dépôt (pas de CDN).

## Flux de travail

- Les tests de notation tournent à chaque push ; un échec bloque la publication.
- Ajouter un cours : copier son `.apkg` dans `decks/`, commit, push.

## Governance

Cette constitution prime sur les autres pratiques du projet. Toute modification passe par
`/speckit-constitution`, avec incrément de version : MAJOR pour un principe retiré ou redéfini,
MINOR pour un principe ajouté ou étendu, PATCH pour une reformulation. Chaque plan Spec Kit vérifie
sa conformité aux principes ci-dessus.

**Version**: 1.0.0 | **Ratified**: 2026-11-11 | **Last Amended**: 2026-11-11
