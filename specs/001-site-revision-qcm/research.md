# Research — Site de révision QCM IFSI

Constats faits sur le paquet réel `UE 2.8 - CM6 AVC - QCM - prompt v1.2 - 2026-11-10.apkg`.

## R1. Format du paquet

- **Decision**: lire `collection.anki21b` (SQLite compressé zstd) quand il existe, sinon
  `collection.anki21`, sinon `collection.anki2`. Le fichier `media` est soit du JSON
  (`{"0": "nom.jpg"}`), soit un protobuf compressé zstd (`MediaEntries { repeated MediaEntry
  entries = 1 }`, `MediaEntry { string name = 1; … }`), où l'indice de l'entrée est le nom du
  fichier dans le zip. Les médias du format récent sont eux-mêmes compressés zstd (détectés par
  l'en-tête `28 B5 2F FD`).
- **Rationale**: le paquet réel est au format récent (`meta` = version 3) avec un `collection.anki2`
  factice. Un décodeur protobuf de 20 lignes évite la bibliothèque `anki` (lourde).
- **Alternatives considered**: bibliothèque `anki` (≈ 100 Mo de dépendances, versions liées à
  Anki).

## R2. Où lire semestre, UE, cours, importance

- **Decision**: nom du paquet des cartes (`decks.name`, séparateur `\x1f` en anki21b, `::` en
  ancien format) : `IFSI::QCM::Semestre 3::UE 2.8 - Processus obstructifs::CM6 - AVC`. Importance :
  étiquette `PSB::Importance::I0..I3`. Une note sans importance ou un paquet hors de ce motif fait
  échouer la conversion.
- **Rationale**: conforme à la spec (FR-061) et au paquet réel.

## R3. Images

- **Decision**: une image dans le champ Question devient `image` (retirée du HTML) ; les images de
  page de cours (`…_pNNN.jpg`) dans les Informations complémentaires deviennent `page_cours` ; toute
  autre image reste en ligne, chemin réécrit en `media/…`. Seules les images référencées sont
  copiées. Pas de recompression : les images du paquet font 12 à 220 ko.
- **Rationale**: le paquet réel a 6 questions avec cliché (`img-…`) et des pages `_p001` à `_p029`.

## R4. Propositions contenant « < »

- **Decision**: les champs sont traités comme du HTML (comme Anki) et assainis par un `<template>`
  inerte ; `< 160/90 mmHg` y reste du texte.

## R5. Ouverture depuis le disque

- **Decision**: non prise en charge ; un serveur statique local suffit
  (`python -m http.server -d site`).
- **Rationale**: les navigateurs bloquent modules ES et `fetch` en `file://`. Le chargement
  paresseux par cours l'emporte (plan).

## R6. Paquets en double

- **Decision**: si deux paquets donnent le même cours, celui dont les notes ont la date de
  modification la plus récente est retenu, avec un avertissement dans le journal.
- **Rationale**: les noms de fichier changent à chaque régénération (`prompt v1.0a`, `v1.2`) ;
  oublier de supprimer l'ancien ne doit pas créer de doublon.

## R7. Mot de passe

- **Decision**: empreinte SHA-256 hexadécimale dans `site/js/config.js`, comparée via
  `crypto.subtle.digest` ; la saisie est rognée (espaces de début et de fin). L'appareil garde
  l'empreinte : changer le mot de passe déconnecte tout le monde.
