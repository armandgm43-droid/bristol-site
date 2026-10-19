# NUMC1 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/numc1/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | NUMC1 (EEL7-NUMC1 ; anciens codes : EN208 « technologie », EN201 « circuits FPGA ») |
| UE | EEL7FE-UEB Électronique Numérique |
| Enseignants | Sylvie Renaud (technologie des CI) ; Bertrand Le Gal (circuits FPGA, VHDL) ; énoncés de TD VHDL : C. Jégo |
| Année | 2026-2027 (supports datés de 2024) |
| Examen | épreuve commune « CI / VHDL » (sujet 2025-2026 dans `annales/`) |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/circuits-fpga-le-gal.pdf` | 110 | 37,6 Mo |
| `support/conception-circuits-integres-2024.pdf` | 35 | 4,5 Mo |
| `support/conception-circuits-integres-ancienne-version.pdf` | 35 | 3,7 Mo |
| `support/memoires-2024.pdf` | 10 | 2,4 Mo |
| `support/technologies-familles-logiques-2024.pdf` | 22 | 3,0 Mo |
| `support/test-ci-numeriques-2024.pdf` | 13 | 1,6 Mo |

### `td/` — énoncés de TD

| Fichier | Pages | Taille |
|---|---|---|
| `td/tcin-td01-propagation-cmos-eeprom.pdf` | 2 | 46 ko |
| `td/tcin-td02-bicmos.pdf` | 1 | 0,1 Mo |
| `td/tcin-test-testabilite.pdf` | 3 | 0,3 Mo |
| `td/td01-vhdl-machine-etats.pdf` | 2 | 0,1 Mo |
| `td/td03-vhdl-placement-routage.pdf` | 4 | 46 ko |
| `td/td04-vhdl-synthese-additionneur-fpga.pdf` | 5 | 0,1 Mo |

### `notes/` — notes de cours

| Fichier | Pages | Taille |
|---|---|---|
| `notes/2023-notes-cours-vhdl.pdf` | 68 | 5,9 Mo |

### `corriges/` — corrigés et comptes rendus

| Fichier | Pages | Taille |
|---|---|---|
| `corriges/2023-td-m-egal-2.pdf` | 6 | 0,7 Mo |
| `corriges/2023-td-machine-de-moore.pdf` | 1 | 0,7 Mo |
| `corriges/2023-td01-machine-etats.pdf` | 5 | 3,4 Mo |
| `corriges/2023-td03-vhdl-placement-routage.pdf` | 4 | 0,8 Mo |
| `corriges/2023-td04-synthese-additionneur-fpga.pdf` | 4 | 0,6 Mo |
| `corriges/2023-td05-testabilite.pdf` | 3 | 0,8 Mo |
| `corriges/td01-vhdl-machine-etats-correction-ancienne-version.pdf` | 16 | 2,0 Mo |
| `corriges/td01-vhdl-machine-etats-correction.pdf` | 16 | 2,0 Mo |

### `annales/` — sujets d'examen

| Fichier | Pages | Taille |
|---|---|---|
| `annales/2016-2017-partiel.pdf` | 2 | 0,7 Mo |
| `annales/2017-2018-partiel.pdf` | 2 | 0,4 Mo |
| `annales/2019-2020-partiel.pdf` | 3 | 2,3 Mo |
| `annales/2022-2023-partiel-p1.jpg` |  | 1,8 Mo |
| `annales/2022-2023-partiel-question-fin-sujet.docx` |  | 6 ko |
| `annales/2025-2026-partiel.pdf` | 4 | 2,4 Mo |

## 3. Plan proposé

Plan proposé à partir des supports reçus (un support = un chapitre). L'ordre réel des séances est à confirmer.

1. **Technologies et familles logiques** — `techno` (Renaud) ; TD TCIN 1 et 2
2. **Mémoires** — `memoires` (Renaud)
3. **Conception de circuits intégrés numériques** — `conception` (Renaud)
4. **Test et testabilité des circuits intégrés numériques** — `test` (Renaud) ; TD test et testabilité
5. **Circuits FPGA** — `fpga` (Le Gal) : circuits reconfigurables, architecture, configuration ; TD 3 et 4
6. **Description VHDL et synthèse** — TD 1 (machine à états, banc de test) et sa correction ; pas de support de cours dans l'archive

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/numc1/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/VHDL/TD m= 2.pdf` | `corriges/2023-td-m-egal-2.pdf` |
| `S7/S7/VHDL/TD/Machine de Moore.pdf` | `corriges/2023-td-machine-de-moore.pdf` |
| `S7/S7/VHDL/TD/TD1 - Machine à états finie.pdf` | `corriges/2023-td01-machine-etats.pdf` |
| `S7/S7/VHDL/TD/TD 3 - Du VHDL au placement-routage.pdf` | `corriges/2023-td03-vhdl-placement-routage.pdf` |
| `S7/S7/VHDL/TD/TD4 Synthèse d’additionneur dans un circuit FPGA.pdf` | `corriges/2023-td04-synthese-additionneur-fpga.pdf` |
| `S7/S7/VHDL/TD/TD5 - Testabilité des circuits intégrés numériquescgc.pdf` | `corriges/2023-td05-testabilite.pdf` |
| `S7/S7/VHDL/TD/EN201-TD1-VHDL-Correction.pdf` | `corriges/td01-vhdl-machine-etats-correction-ancienne-version.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/EN208-TD1-VHDL-Correction.pdf` | `corriges/td01-vhdl-machine-etats-correction.pdf` |
| `S7/S7/VHDL/Cours/Cours VHDL.pdf` | `notes/2023-notes-cours-vhdl.pdf` |
| `S7/S7/VHDL/Cours/Les circuits FPGA.pdf` | `support/circuits-fpga-le-gal.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/2024-EN208-Conception Circuits Intégrés.pdf` | `support/conception-circuits-integres-2024.pdf` |
| `S7/S7/VHDL/Cours/Intro au circuit FPGA.pdf` | `support/conception-circuits-integres-ancienne-version.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/2024-EN208-Mémoires.pdf` | `support/memoires-2024.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/2024-EN208-Technologies et familles logiques-Version polycopié.pdf` | `support/technologies-familles-logiques-2024.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/2024-EN201-Test CI Numériques.pdf` | `support/test-ci-numeriques-2024.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/TCIN-EEPROM NAND NOR.pdf` | `td/tcin-td01-propagation-cmos-eeprom.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/TCIN-TD2-BiCMOS.pdf` | `td/tcin-td02-bicmos.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/TCIN-Test et Testabilité.pdf` | `td/tcin-test-testabilite.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/EN208-TD1-VHDL.pdf` | `td/td01-vhdl-machine-etats.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/EN208_TD2_VHDL.pdf` | `td/td03-vhdl-placement-routage.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMC1 Technologie des circuits numériques/EN208_TD3_VHDL.pdf` | `td/td04-vhdl-synthese-additionneur-fpga.pdf` |
