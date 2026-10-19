# EAEP1 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/eaep1/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | EAEP1 (EEL7-EAEP1 ; ancien code : EA207) |
| UE | EEL7FE-UEA Circuits et Systèmes Analogiques |
| Enseignant | Jean-Michel Vinassa |
| Année | 2026-2027 (support de cours 2026, 142 p.) |
| Organisation (support, p. 2) | cours en amphi ; 5 TD / enseignements intégrés ; bureau d'études sur PSIM (2 parties) |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/aide-decomposition-serie-fourier.pdf` | 2 | 0,4 Mo |
| `support/cours-2026-vinassa.pdf` | 142 | 16,9 Mo |
| `support/lire-datasheet-transistor-puissance.pdf` | 19 | 0,6 Mo |
| `support/datasheets/byv29-philips.pdf` | 5 | 39 ko |
| `support/datasheets/irfz34n-infineon.pdf` | 10 | 0,2 Mo |

### `td/` — énoncés de TD

| Fichier | Pages | Taille |
|---|---|---|
| `td/be-2024-vinassa.pdf` | 6 | 0,4 Mo |
| `td/poly-td-2022-2023-vinassa.pdf` | 34 | 5,3 Mo |

### `notes/` — notes de cours

| Fichier | Pages | Taille |
|---|---|---|
| `notes/2023-notes-cours.pdf` | 2 | 0,3 Mo |

### `corriges/` — corrigés et comptes rendus

| Fichier | Pages | Taille |
|---|---|---|
| `corriges/2023-td-exercice-03-commande-transistor-puissance.pdf` | 3 | 0,8 Mo |

### `annales/` — sujets d'examen

| Fichier | Pages | Taille |
|---|---|---|
| `annales/2016-2017-partiel.pdf` | 2 | 0,7 Mo |
| `annales/2017-2018-partiel.pdf` | 2 | 0,7 Mo |
| `annales/2022-2023-partiel-p1.jpg` |  | 2,3 Mo |
| `annales/2022-2023-partiel-p2.jpg` |  | 1,8 Mo |

## 3. Plan proposé

Plan tiré de l'organisation du cours (`cours`, p. 2) : un chapitre Bristol par chapitre du support (la partie 08 est une bibliographie). Le rattachement des TD est proposé d'après leurs titres.

1. **Enjeux de l'électronique de puissance** — support, partie 01
2. **Convertisseurs DC/DC non isolés** — partie 02 ; TD 1
3. **Composants à semiconducteur de puissance** — partie 03 ; TD 2 et TD 3
4. **Commande des convertisseurs DC/DC** — partie 04
5. **Packaging et thermique** — partie 05 ; TD 4
6. **Composants de puissance passifs** — partie 06
7. **Conversion DC/AC : onduleurs** — partie 07 ; TD 5

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/eaep1/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/Électronique pour la Conversion d’Energie/TD/Exercice 3 - Circuit de commande du transistor de puissance.pdf` | `corriges/2023-td-exercice-03-commande-transistor-puissance.pdf` |
| `S7/S7/Électronique pour la Conversion d’Energie/Cours/Cours.pdf` | `notes/2023-notes-cours.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EAEP1 Électronique pour la Conversion d'Energie 1/Aide  Decomposition en serie de Fourier.pdf` | `support/aide-decomposition-serie-fourier.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EAEP1 Électronique pour la Conversion d'Energie 1/P_26_EEL7-EAEP1_exEA207_Cours_JMV.pdf` | `support/cours-2026-vinassa.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EAEP1 Électronique pour la Conversion d'Energie 1/BYV29_Philips.pdf` | `support/datasheets/byv29-philips.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EAEP1 Électronique pour la Conversion d'Energie 1/IRFZ34N_Infineon.pdf` | `support/datasheets/irfz34n-infineon.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EAEP1 Électronique pour la Conversion d'Energie 1/comment lire la data sheet dun transistor de puissance 2.pdf` | `support/lire-datasheet-transistor-puissance.pdf` |
| `EEL7FE-UEA Circuits et Systèmes Analogiques/EEL7-EAEP1 Électronique pour la Conversion d'Energie 1/S_24_EA207_BE_JMV.pdf` | `td/be-2024-vinassa.pdf` |
| `S7/S7/Électronique pour la Conversion d’Energie/TD/EA207_EI-TD_poly_2022-2023_JMV.pdf` | `td/poly-td-2022-2023-vinassa.pdf` |
