# AUTO1 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/auto1/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | AUTO1 (EEL7-AUTO1 ; ancien code : AU201, sigle CSLTCD) |
| UE | EEL7FE-UEC Automatique et Signal |
| Enseignant | Pierre Melchior (note de cours) ; auteurs des énoncés de TD : P. Melchior, « amarque » (métadonnées PDF, nom complet à confirmer) |
| Année | 2026-2027 (note de cours : versions v01 et v03, plus une version d'une année antérieure) |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/implantation-correcteurs.pdf` | 13 | 0,1 Mo |
| `support/note-de-cours-melchior-ancienne-version.pdf` | 91 | 5,8 Mo |
| `support/note-de-cours-melchior-v01.pdf` | 75 | 1,1 Mo |
| `support/note-de-cours-melchior-v03.pdf` | 75 | 1,1 Mo |
| `support/synthese-frequentielle-correcteurs.pdf` | 9 | 0,9 Mo |
| `support/table-transformees-z.pdf` | 4 | 0,3 Mo |

### `td/` — énoncés de TD

| Fichier | Pages | Taille |
|---|---|---|
| `td/recueil-td-melchior-ancienne-version.pdf` | 28 | 1,4 Mo |
| `td/td01-1-synthese-pi.pdf` | 7 | 0,3 Mo |
| `td/td01-2-synthese-pd.pdf` | 3 | 0,2 Mo |
| `td/td02-abaque-nichols.pdf` | 1 | 0,3 Mo |
| `td/td03-suite-cdc-pi-pid.pdf` | 4 | 0,2 Mo |

### `notes/` — notes de cours

| Fichier | Pages | Taille |
|---|---|---|
| `notes/2023-fiche-synthese.pdf` | 20 | 4,0 Mo |
| `notes/2023-notes-synthese-pd.pdf` | 3 | 2,3 Mo |
| `notes/2023-table-transformee-z.pdf` | 6 | 0,7 Mo |

### `corriges/` — corrigés et comptes rendus

| Fichier | Pages | Taille |
|---|---|---|
| `corriges/2023-partiel-2016-2017-session-1.pdf` | 4 | 0,7 Mo |
| `corriges/2023-partiel-2019-2020-session-1.pdf` | 6 | 0,8 Mo |
| `corriges/2023-td-commande-pidf-moteur.pdf` | 5 | 0,8 Mo |
| `corriges/2023-td01.pdf` | 3 | 2,8 Mo |
| `corriges/2023-td02-transformee-z.pdf` | 3 | 0,6 Mo |
| `corriges/2023-td03-enceinte-thermique.pdf` | 7 | 1,3 Mo |
| `corriges/2023-td04-boucle-de-commande.pdf` | 3 | 0,7 Mo |

### `annales/` — sujets d'examen

| Fichier | Pages | Taille |
|---|---|---|
| `annales/2013-2014-partiel-commande-lineaire.pdf` | 2 | 1,8 Mo |
| `annales/2014-2015-partiel-commande-lineaire.pdf` | 2 | 0,4 Mo |
| `annales/2015-2016-partiel-temps-discret.pdf` | 1 | 35 ko |
| `annales/2016-2017-partiel-commande-lineaire.pdf` | 3 | 1,0 Mo |
| `annales/2016-2017-partiel-temps-discret.pdf` | 2 | 0,8 Mo |
| `annales/2017-2018-partiel-commande-lineaire.pdf` | 3 | 0,6 Mo |
| `annales/2017-2018-partiel-temps-discret.pdf` | 2 | 0,4 Mo |

## 3. Plan proposé

Plan tiré du sommaire de la note de cours (`cours-v03`), commun aux trois versions reçues. Proposition à valider : un chapitre Bristol par bloc cohérent du sommaire.

1. **Introduction, modélisation et représentations fréquentielles** — § 1 à 3
2. **Analyse de la commande en boucle fermée** — § 4 : précision, rejet de perturbation, stabilité, rapidité, sensibilité, filtrage
3. **Synthèse d'un régulateur PIDF en temps continu** — § 5 et 6 : P, PI, PD, PIDF ; TD 1 et TD 3
4. **Signaux échantillonnés et transformée en Z** — § 7 à 9 ; table des transformées en Z
5. **Commande à temps discret et synthèse fréquentielle d'un régulateur discret** — § 10 et 11 : transformations en W (bilinéaire) et de Tustin ; support « Synthèse fréquentielle »
6. **Implantation d'un régulateur numérique** — § 12 et 13 ; support « Implantation d'un correcteur numérique »

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/auto1/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/Automatique/2016-2017 Session 1.pdf` | `corriges/2023-partiel-2016-2017-session-1.pdf` |
| `S7/S7/Automatique/2019-2020 Session 1.pdf` | `corriges/2023-partiel-2019-2020-session-1.pdf` |
| `S7/S7/Automatique/TD Autom/Commande d’un PIDF d’un moteur.pdf` | `corriges/2023-td-commande-pidf-moteur.pdf` |
| `S7/S7/Automatique/TD Autom/TD 1.pdf` | `corriges/2023-td01.pdf` |
| `S7/S7/Automatique/TD Autom/TD 2 - Transformée en z d’un signal connu sous forme d’une séquence d’échantillons  et transformée inverse.pdf` | `corriges/2023-td02-transformee-z.pdf` |
| `S7/S7/Automatique/TD Autom/TD3 - Commande d’une enceinte thermique.pdf` | `corriges/2023-td03-enceinte-thermique.pdf` |
| `S7/S7/Automatique/TD Autom/TD 4 - Boucle de commande.pdf` | `corriges/2023-td04-boucle-de-commande.pdf` |
| `S7/S7/Automatique/Cours Autom/Fiche Autom.pdf` | `notes/2023-fiche-synthese.pdf` |
| `S7/S7/Automatique/Cours Autom/Synthèse d’un PD.pdf` | `notes/2023-notes-synthese-pd.pdf` |
| `S7/S7/Automatique/Cours Autom/Transformée en Z table.pdf` | `notes/2023-table-transformee-z.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/3-ImplantationCorrecteurs.pdf` | `support/implantation-correcteurs.pdf` |
| `S7/S7/Automatique/Cours Autom/Cours Commande des systèmes linéaires à temps continue et discret.pdf` | `support/note-de-cours-melchior-ancienne-version.pdf` |
| `Automatique et signal/4-AUTO1-AU201-CSLTCD-01-09-25.pdf` | `support/note-de-cours-melchior-v01.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/4-AUTO1-AU201-CSLTCD-03-09-29.pdf` | `support/note-de-cours-melchior-v03.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/2-SyntheseFrequentielleCorrecteurs.pdf` | `support/synthese-frequentielle-correcteurs.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/4-TableTransformeesZ.pdf` | `support/table-transformees-z.pdf` |
| `S7/S7/Automatique/TD Autom/TD Autom sujet.pdf` | `td/recueil-td-melchior-ancienne-version.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/TD1-1-SynthesePI.pdf` | `td/td01-1-synthese-pi.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/TD1-2-SynthesePD.pdf` | `td/td01-2-synthese-pd.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/TD2-Nichols1.pdf` | `td/td02-abaque-nichols.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO1 Commande des Systèmes Linéaires à Temps Continu et Discret/TD3-SuiteCDC-PI-PID.pdf` | `td/td03-suite-cdc-pi-pid.pdf` |
