# EARF1 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/earf1/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | EARF1 (EEL7-EARF1) |
| UE | EEL7FE-UEA Circuits et Systèmes Analogiques |
| Enseignant | Thierry Taris |
| Année | 2026-2027 |
| Volume (supports) | modulations analogiques : 2 h 40 ; modulations numériques : 1 h 20 ; 3 TD |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/cours-01-modulations-analogiques.pdf` | 54 | 12,3 Mo |
| `support/cours-02-modulations-numeriques.pdf` | 30 | 2,0 Mo |

### `td/` — énoncés de TD

| Fichier | Pages | Taille |
|---|---|---|
| `td/td01-gnuradio-modulations.docx` |  | 1,4 Mo |
| `td/td01-gnuradio-modulations.pdf` | 10 | 1,0 Mo |
| `td/td02-modulateurs.pdf` | 3 | 1,4 Mo |
| `td/td03-demodulateurs.pdf` | 3 | 1,3 Mo |

### `notes/` — notes de cours

| Fichier | Pages | Taille |
|---|---|---|
| `notes/2023-notes-modulations-analogiques.pdf` | 7 | 2,1 Mo |
| `notes/2023-notes-modulations-numeriques.pdf` | 1 | 0,4 Mo |

### `corriges/` — corrigés et comptes rendus

| Fichier | Pages | Taille |
|---|---|---|
| `corriges/2023-td01-principe-modulations.pdf` | 4 | 0,6 Mo |
| `corriges/2023-td02-modulateurs.pdf` | 4 | 0,7 Mo |
| `corriges/2023-td03-demodulateurs.pdf` | 3 | 0,7 Mo |

## 3. Plan proposé

Plan tiré des sommaires des deux supports. Matière distincte de TS227 (confirmé par Armand le 18 octobre 2026) ; les modulations numériques y sont vues côté circuits.

1. **Introduction : signaux et outils d'analyse** — `mod-ana` : introduction, signaux et outils d'analyse
2. **Modulations linéaires** — `mod-ana` : modulations d'amplitude
3. **Modulations angulaires** — `mod-ana` : modulations de fréquence et de phase
4. **Introduction aux modulations numériques** — `mod-num` : ASK, FSK, PSK, représentation IQ, critères de performance

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

**29 octobre 2026** : plan validé et appliqué (4 chapitres, statut `valide`) ; slugs : `01-introduction-signaux-outils`, `02-modulations-lineaires`, `03-modulations-angulaires`, `04-modulations-numeriques`. Le support « Student » est complet (aucun trou). Rapports : `analyses/0N-*.md`.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/earf1/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/Modulations Analogiques/TD/TD1 - Principe des Modulations.pdf` | `corriges/2023-td01-principe-modulations.pdf` |
| `S7/S7/Modulations Analogiques/TD/TD2 - Modulateurs.pdf` | `corriges/2023-td02-modulateurs.pdf` |
| `S7/S7/Modulations Analogiques/TD/TD 3 - Démodulateurs.pdf` | `corriges/2023-td03-demodulateurs.pdf` |
| `S7/S7/Modulations Analogiques/Cours/Modulations Analogiques.pdf` | `notes/2023-notes-modulations-analogiques.pdf` |
| `S7/S7/Modulations Analogiques/Cours/Introduction aux Modulations Numériques.pdf` | `notes/2023-notes-modulations-numeriques.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EARF1 Modulations Analogiques & Numériques pour les communications/1_Cours_Mod_Analog_Student.pdf` | `support/cours-01-modulations-analogiques.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EARF1 Modulations Analogiques & Numériques pour les communications/2_Cours_Mod_Num_Student.pdf` | `support/cours-02-modulations-numeriques.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EARF1 Modulations Analogiques & Numériques pour les communications/TD1_gnuradio_Modulations.docx` | `td/td01-gnuradio-modulations.docx` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EARF1 Modulations Analogiques & Numériques pour les communications/TD1_gnuradio_Modulations.pdf` | `td/td01-gnuradio-modulations.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EARF1 Modulations Analogiques & Numériques pour les communications/TD2_Modulateurs.pdf` | `td/td02-modulateurs.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EARF1 Modulations Analogiques & Numériques pour les communications/TD3_Démodulateurs.pdf` | `td/td03-demodulateurs.pdf` |
