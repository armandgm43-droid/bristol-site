# NUME3 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/nume3/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | NUME3 (EEL7-NUME3 ; ancien code : EN202) |
| UE | EEL7FE-UEB Électronique Numérique |
| Enseignants | à compléter (énoncés : C. Jégo ; planning du TP 1 : « Valéry », nom complet à confirmer) |
| Année | 2026-2027 |
| Nature | projet : lecteur MP3 sur carte FPGA (Nexys A7 / Nexys 4 DDR) |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/enonce-projet-en202.pdf` | 7 | 0,2 Mo |

### `tp/` — énoncés et fichiers de TP

| Fichier | Pages | Taille |
|---|---|---|
| `tp/tp01-interface-lecteur-mp3-ancienne-version.pdf` | 7 | 0,8 Mo |
| `tp/tp01-interface-lecteur-mp3.pdf` | 7 | 0,6 Mo |
| `tp/tp02-vhdl.pdf` | 10 | 0,2 Mo |
| `tp/fichiers/fichiers-xdc.zip` |  | 6 ko |
| `tp/fichiers/music.zip` |  | 1,1 Mo |
| `tp/fichiers/rom-sinus.txt` |  | 1,0 Mo |
| `tp/fichiers/uart-mp3.zip` |  | 4 ko |

### `notes/` — notes de cours

| Fichier | Pages | Taille |
|---|---|---|
| `notes/2023-notes-definition-projet.pdf` | 5 | 0,8 Mo |

### `corriges/` — corrigés et comptes rendus

| Fichier | Pages | Taille |
|---|---|---|
| `corriges/2023-projet-jack-brouillon-cr.pdf` | 2 | 0,2 Mo |
| `corriges/2023-projet-mp3-notes.pdf` | 2 | 1,7 Mo |
| `corriges/externe-projet-matthieu/tb/…` | 3 fichiers | 6 ko |
| `corriges/externe-projet-matthieu/vhdl/…` | 3 fichiers | 5 ko |

### `annales/` — sujets d'examen

| Fichier | Pages | Taille |
|---|---|---|
| `annales/2013-2014-partiel-synthese-vhdl.pdf` | 2 | 1,6 Mo |

### `travaux/` — travaux personnels (non publiés)

| Fichier | Pages | Taille |
|---|---|---|
| `travaux/lecteur-mp3/lecteur_MP3.xpr` |  | 14 ko |
| `travaux/lecteur-mp3/sim/…` | 8 fichiers | 18 ko |
| `travaux/lecteur-mp3/sources/…` | 8 fichiers | 67 ko |

## 3. Plan proposé

Matière de projet : pas de chapitre de cours. Les rappels de VHDL sont dans NUMC1 ; les TP et le projet seront traités en phase 2 (dossier `tp/`). Séances relevées :


- **TP 1** : interface du lecteur MP3 (machine à états, compteurs)
- **TP 2** : TP VHDL (version 2016-2017)
- **Projet** : lecteur MP3 : énoncé du projet EN202 ; fichiers fournis (contraintes XDC, réception UART, ROM sinus, musiques)

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/nume3/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/VHDL/TP/Projet Jack/Brouillon CR.pdf` | `corriges/2023-projet-jack-brouillon-cr.pdf` |
| `S7/S7/VHDL/TP/Projet MP3/Projet MP3 VHDL.pdf` | `corriges/2023-projet-mp3-notes.pdf` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/TB/cpt_1_599_tb.vhd` | `corriges/externe-projet-matthieu/tb/cpt_1_599_tb.vhd` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/TB/cpt_1_9_tb.vhd` | `corriges/externe-projet-matthieu/tb/cpt_1_9_tb.vhd` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/TB/fsm_MP3_tb.vhd` | `corriges/externe-projet-matthieu/tb/fsm_MP3_tb.vhd` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/VHDL/cpt_1_599.vhd` | `corriges/externe-projet-matthieu/vhdl/cpt_1_599.vhd` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/VHDL/cpt_1_9.vhd` | `corriges/externe-projet-matthieu/vhdl/cpt_1_9.vhd` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/VHDL/fsm_MP3.vhd` | `corriges/externe-projet-matthieu/vhdl/fsm_MP3.vhd` |
| `S7/S7/VHDL/Projet/1 - définition du projet.pdf` | `notes/2023-notes-definition-projet.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/Enonce_EN202.pdf` | `support/enonce-projet-en202.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/fichiers_XDC-20261019.zip` | `tp/fichiers/fichiers-xdc.zip` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/Music.zip` | `tp/fichiers/music.zip` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/ROM Sinus.txt` | `tp/fichiers/rom-sinus.txt` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/UART_MP3.zip` | `tp/fichiers/uart-mp3.zip` |
| `VHDL/EE7EN202_projet_vhdl_Matthieudocs/Enonces/EN208_TP1_VHDL.pdf` | `tp/tp01-interface-lecteur-mp3-ancienne-version.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/TP1_Interface_Lecteur.pdf` | `tp/tp01-interface-lecteur-mp3.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUME3 Conception VHDLFPGA/EN208_TP2_VHDL.pdf` | `tp/tp02-vhdl.pdf` |
| `VHDL/lecteur_MP3/lecteur_MP3.xpr` | `travaux/lecteur-mp3/lecteur_MP3.xpr` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/cpt_1_599_tb.vhd` | `travaux/lecteur-mp3/sim/cpt_1_599_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/cpt_1_9_tb.vhd` | `travaux/lecteur-mp3/sim/cpt_1_9_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/detec_impulsion_tb.vhd` | `travaux/lecteur-mp3/sim/detec_impulsion_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/fsm_MP3_tb.vhd` | `travaux/lecteur-mp3/sim/fsm_MP3_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/gestion_freq_tb.vhd` | `travaux/lecteur-mp3/sim/gestion_freq_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/mod8_tb.vhd` | `travaux/lecteur-mp3/sim/mod8_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/mux8_tb.vhd` | `travaux/lecteur-mp3/sim/mux8_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sim_1/new/trans_tb.vhd` | `travaux/lecteur-mp3/sim/trans_tb.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/cpt_1_599.vhd` | `travaux/lecteur-mp3/sources/cpt_1_599.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/cpt_1_9.vhd` | `travaux/lecteur-mp3/sources/cpt_1_9.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/detec_impulsion.vhd` | `travaux/lecteur-mp3/sources/detec_impulsion.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/fsm_MP3.vhd` | `travaux/lecteur-mp3/sources/fsm_MP3.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/gestion_freq.vhd` | `travaux/lecteur-mp3/sources/gestion_freq.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/mod8.vhd` | `travaux/lecteur-mp3/sources/mod8.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/mux8.vhd` | `travaux/lecteur-mp3/sources/mux8.vhd` |
| `VHDL/lecteur_MP3/lecteur_MP3.srcs/sources_1/new/trans.vhd` | `travaux/lecteur-mp3/sources/trans.vhd` |
