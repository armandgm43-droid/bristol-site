# PROJ1 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/proj1/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | PROJ1 (EEL7-PROJ1 ; ancien code : PR206) |
| UE | EEL7FE-UEA Circuits et Systèmes Analogiques |
| Encadrants | deux enseignants par séance, non nommés dans les informations générales |
| Année | 2026-2027 (informations générales du 25 août 2026) |
| Nature | projet en binôme : conception d'un système analogique à partir d'un sujet, rapport d'une vingtaine de pages |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/consignes-rapport-moodle.txt` |  | 1 ko |
| `support/grille-evaluation-2026-2027.pdf` | 1 | 57 ko |
| `support/informations-generales-2026.pdf` | 12 | 0,3 Mo |
| `support/tutoriel-draw-io.pdf` | 3 | 0,3 Mo |
| `support/ressources-groupe-d/0-ressources_generales/…` | 90 fichiers | 233,2 Mo |
| `support/ressources-groupe-d/A-cardiofrequencemetre_optique/…` | 7 fichiers | 10,4 Mo |
| `support/ressources-groupe-d/B-cardiofrequencemetre_electrique/…` | 12 fichiers | 9,5 Mo |
| `support/ressources-groupe-d/C-capteur_mouvement_pyroelectrique/…` | 19 fichiers | 22,0 Mo |
| `support/ressources-groupe-d/D-sonde_de_temperature_rtd/…` | 12 fichiers | 9,3 Mo |
| `support/ressources-groupe-d/E-excitation_ventilateur_mli/…` | 7 fichiers | 2,5 Mo |
| `support/ressources-groupe-d/F-magnetometre_portatif/…` | 16 fichiers | 22,0 Mo |
| `support/ressources-groupe-d/G-interface_boucle_4-20mA/…` | 7 fichiers | 4,1 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-Amplficateur_gain_controle/…` | 1 fichier | 0,2 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-Amplificateur_logarithmique/…` | 1 fichier | 0,2 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-Capteur_piezoelectrique/…` | 10 fichiers | 14,2 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-Egaliseur_audio/…` | 1 fichier | 0,1 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-GBF/…` | 1 fichier | 0,2 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-Octaveur/…` | 1 fichier | 0,2 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-Thérémine/…` | 1 fichier | 0,1 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-detecteur_de_claquement/…` | 4 fichiers | 2,4 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-detecteur_objet_colore/…` | 4 fichiers | 0,7 Mo |
| `support/ressources-groupe-d/Z-NON_PROPOSE-transmission_optoelectronique/…` | 13 fichiers | 6,0 Mo |
| `support/sujets-2026-2027/eel7-proj1-sujet_cardiofrequencemetre_electrique_v3.pdf` | 1 | 0,1 Mo |
| `support/sujets-2026-2027/eel7-proj1-sujet_cardiofrequencemetre_optique_v3.pdf` | 1 | 0,1 Mo |
| `support/sujets-2026-2027/eel7-proj1-sujet_detecteur_pyroelectrique_v3.pdf` | 1 | 0,1 Mo |
| `support/sujets-2026-2027/eel7-proj1-sujet_interface_boucle_4-20_mA_v2.pdf` | 1 | 29 ko |
| `support/sujets-2026-2027/eel7-proj1-sujet_magnetometre_portatif_v3.pdf` | 1 | 0,1 Mo |
| `support/sujets-2026-2027/eel7-proj1-sujet_mli_ventilateur_v3.pdf` | 1 | 0,1 Mo |
| `support/sujets-2026-2027/eel7-proj1-sujet_sonde_rtd_v4.pdf` | 1 | 0,1 Mo |

### `travaux/` — travaux personnels (non publiés)

| Fichier | Pages | Taille |
|---|---|---|
| `travaux/cardiofrequencemetre/cardiofrequencemetre.pdf` | 6 | 0,4 Mo |
| `travaux/cardiofrequencemetre/cardiofrequencemetre.tex` |  | 25 ko |
| `travaux/cardiofrequencemetre/figures/…` | 2 fichiers | 39 ko |
| `travaux/mesures/ap-derivateur-armand.png` |  | 24 ko |
| `travaux/mesures/ap-derivateur-lucas.png` |  | 25 ko |
| `travaux/mesures/sortie-comparateur.png` |  | 29 ko |
| `travaux/mesures/tek00000-aamir.png` |  | 22 ko |
| `travaux/mesures/tek00003.png` |  | 24 ko |

## 3. Plan proposé

Matière de projet : pas de chapitre de cours. Bristol pourra en tirer des fiches de méthode (phase 2). Sujets 2026-2027 :


- **A** : cardiofréquencemètre optique
- **B** : cardiofréquencemètre électrique
- **C** : détecteur de mouvement pyroélectrique
- **D** : sonde de température RTD
- **E** : excitation d'un ventilateur par MLI
- **F** : magnétomètre portatif
- **G** : interface de boucle 4-20 mA

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/proj1/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-PROJ1 Projet analogique/Deadline.txt` | `support/consignes-rapport-moodle.txt` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-PROJ1 Projet analogique/eel7-proj1-grille_evaluation_v0-2026-2027.pdf` | `support/grille-evaluation-2026-2027.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-PROJ1 Projet analogique/eel7-proj1_ex-pr206-informations_generales-2026-08-25_b-version_eleves.pdf` | `support/informations-generales-2026.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-PROJ1 Projet analogique/tutoriel_saisie_schema-draw_io-slagoug_2024.pdf` | `support/tutoriel-draw-io.pdf` |
| `Analogique/cardiofrequencemetre_latex/cardiofrequencemetre.pdf` | `travaux/cardiofrequencemetre/cardiofrequencemetre.pdf` |
| `Analogique/cardiofrequencemetre_latex/cardiofrequencemetre.tex` | `travaux/cardiofrequencemetre/cardiofrequencemetre.tex` |
| `Analogique/cardiofrequencemetre_latex/figures/avant_derivateur.png` | `travaux/cardiofrequencemetre/figures/avant_derivateur.png` |
| `Analogique/cardiofrequencemetre_latex/figures/sortie_derivateur.png` | `travaux/cardiofrequencemetre/figures/sortie_derivateur.png` |
| `Analogique/ap dérivateur armand.PNG` | `travaux/mesures/ap-derivateur-armand.png` |
| `Analogique/ap dérivateur lucas.PNG` | `travaux/mesures/ap-derivateur-lucas.png` |
| `Analogique/sortie comparateur.PNG` | `travaux/mesures/sortie-comparateur.png` |
| `Analogique/TEK00000 aamir.PNG` | `travaux/mesures/tek00000-aamir.png` |
| `Analogique/TEK00003.PNG` | `travaux/mesures/tek00003.png` |
| `…/ressources_EEL7-PROJ1_groupe_D-20261019.zip`, `…/Sujets 2026-2027-20261019.zip` | extraits tels quels dans `support/ressources-groupe-d/` et `support/sujets-2026-2027/` |
