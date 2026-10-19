# EANA2 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/eana2/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | EANA2 (EEL7-EANA2 ; ancien code : EA233) |
| UE | EEL7FE-UEA Circuits et Systèmes Analogiques |
| Enseignants | François Rivet (conversion analogique-numérique) ; Thierry Taris (bruit en électronique) |
| Année | 2026-2027 (supports : CAN, septembre 2025 ; bruit, 2014 mis à jour) |
| Évaluation (support CAN, p. 3) | épreuve terminale sans document, 1 h 20 |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/cours-conversion-analogique-numerique-rivet.pdf` | 150 | 17,7 Mo |
| `support/cours-initiation-bruit-taris.pdf` | 44 | 2,1 Mo |
| `support/ressources/adc-survey-murmann.zip` |  | 10,3 Mo |
| `support/ressources/lien-video-adc-basics.txt` |  | 1 ko |

### `td/` — énoncés de TD

| Fichier | Pages | Taille |
|---|---|---|
| `td/td-bruit.pdf` | 4 | 0,4 Mo |

### `tp/` — énoncés et fichiers de TP

| Fichier | Pages | Taille |
|---|---|---|
| `tp/tp-bruit.pdf` | 13 | 0,6 Mo |

### `annales/` — sujets d'examen

| Fichier | Pages | Taille |
|---|---|---|
| `annales/2015-2016-partiel-initiation-bruit.pdf` | 2 | 0,4 Mo |
| `annales/2016-2017-partiel-initiation-bruit.pdf` | 2 | 0,4 Mo |

## 3. Plan proposé

Plan tiré des sommaires des deux supports. Le premier objectif annoncé (« principe du conditionnement analogique d'un signal ») n'a pas de support dans l'archive.

1. **Principe et caractéristiques de la conversion analogique-numérique** — `can`, parties 1 et 2 : contexte, discrétisation, grandeurs caractéristiques, repliement
2. **Limitations de la conversion** — `can`, partie 3 : gain, offset, erreurs
3. **Architectures des convertisseurs** — `can`, partie 4 : CNA, Flash, intégration, pipeline, SAR, ΣΔ, entrelacement, état de l'art
4. **Bruit en électronique : outils et types de bruit** — `bruit` : introduction, outils de traitement, types de bruit
5. **Bruit des composants, rapport signal à bruit et facteur de bruit** — `bruit` : modélisation des composants, facteur de bruit ; TD et TP bruit

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/eana2/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `Annales 2A élec/Annales 2A élec/Initiation aux bruits/Partiel 2015-2016.pdf` | `annales/2015-2016-partiel-initiation-bruit.pdf` |
| `Annales 2A élec/Annales 2A élec/Initiation aux bruits/Partiel 2016-2017.pdf` | `annales/2016-2017-partiel-initiation-bruit.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EANA2 Chaine d'acquisition et conditionnement du signal analogique/EA233_Conversion.pdf` | `support/cours-conversion-analogique-numerique-rivet.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EANA2 Chaine d'acquisition et conditionnement du signal analogique/EA233_Cours_Student.pdf` | `support/cours-initiation-bruit-taris.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EANA2 Chaine d'acquisition et conditionnement du signal analogique/ADC-survey-main.zip` | `support/ressources/adc-survey-murmann.zip` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EANA2 Chaine d'acquisition et conditionnement du signal analogique/Analog-to-Digital Converter (ADC) - Basics.txt` | `support/ressources/lien-video-adc-basics.txt` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EANA2 Chaine d'acquisition et conditionnement du signal analogique/EA233_TD_Bruit.pdf` | `td/td-bruit.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EANA2 Chaine d'acquisition et conditionnement du signal analogique/EA233_TP.pdf` | `tp/tp-bruit.pdf` |
