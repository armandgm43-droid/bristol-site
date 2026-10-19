# AUTO2 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/auto2/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | AUTO2 (EEL7-AUTO2) |
| UE | EEL7FE-UEC Automatique et Signal |
| Enseignants | Pierre Melchior, Patrick Lanusse, Ghazi Bel Haj Frej, Mathieu Chevrié (page de titre des polys) |
| Année | 2026-2027 |
| Nature | matière de travaux pratiques (pas de cours magistral) |

## 2. Fichiers

### `tp/` — énoncés et fichiers de TP

| Fichier | Pages | Taille |
|---|---|---|
| `tp/annexes-grafcet-ladder.pdf` | 6 | 0,3 Mo |
| `tp/annexes-logiciel-automgen.pdf` | 4 | 0,1 Mo |
| `tp/annexes-logiciel-fst.pdf` | 3 | 0,2 Mo |
| `tp/tp-automatique-1.pdf` | 19 | 0,6 Mo |
| `tp/tp-automatique-2.pdf` | 25 | 0,8 Mo |
| `tp/fichiers/config-ascenseur.agn` |  | 8 ko |
| `tp/fichiers/fichiers-fst-festo.zip` |  | 18 ko |
| `tp/fichiers/tp-labview-moteur-ls.zip` |  | 12,3 Mo |
| `tp/fichiers/tp-labview-moteur-parvex.zip` |  | 12,3 Mo |
| `tp/fichiers/tp-labview-thermique-retard.zip` |  | 6,2 Mo |

### `corriges/` — corrigés et comptes rendus

| Fichier | Pages | Taille |
|---|---|---|
| `corriges/2023-tp01-ascenseur-grafcet-cr.pdf` | 8 | 2,6 Mo |
| `corriges/2023-tp02-commande-pid-boucle-fermee-cr.pdf` | 7 | 2,1 Mo |
| `corriges/2023-tp04-pid-systeme-retard-cr.pdf` | 5 | 0,8 Mo |

### `travaux/` — travaux personnels (non publiés)

| Fichier | Pages | Taille |
|---|---|---|
| `travaux/cr-tp1-ascenseur-grafcet/CR_TP1_Ascenseur_Grafcet.pdf` | 17 | 0,6 Mo |
| `travaux/cr-tp1-ascenseur-grafcet/CR_TP1_Ascenseur_Grafcet.tex` |  | 51 ko |
| `travaux/cr-tp1-ascenseur-grafcet/inp.png` |  | 78 ko |

## 3. Plan proposé

Matière de TP : pas de chapitre de cours. Le contenu théorique est celui d'AUTO1 ; les TP seront traités en phase 2 (dossier `tp/`). Séances relevées dans les polys :


- **Poly « Travaux pratiques d'automatique 1 »** : ascenseur commandé par automate programmable (Grafcet, Ladder, Automgen) ; commande PID en boucle fermée d'un moteur (LabVIEW)
- **Poly « Travaux pratiques d'automatique 2 »** : chaîne d'assemblage FESTO (FST) ; commande PIDF d'une enceinte thermique à retard ; synthèse d'un régulateur discret par la transformation en W

## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/auto2/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/Automatique/TP Autom/TP1 Ascenseur Grafcet.pdf` | `corriges/2023-tp01-ascenseur-grafcet-cr.pdf` |
| `S7/S7/Automatique/TP Autom/TP2 Commande PID en Boucle fermée.pdf` | `corriges/2023-tp02-commande-pid-boucle-fermee-cr.pdf` |
| `S7/S7/Automatique/TP Autom/TP4 Commande PID d’un système à retard.pdf` | `corriges/2023-tp04-pid-systeme-retard-cr.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/Annexes Grafcet, Ladder et Automgen-20261019.zip :: Annexes_GRAFCET_Ladder.pdf` | `tp/annexes-grafcet-ladder.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/Annexes Grafcet, Ladder et Automgen-20261019.zip :: Annexes_logiciel_AUTOMGEN.pdf` | `tp/annexes-logiciel-automgen.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/Annexes Grafcet, Ladder et FST-20261019.zip :: Annexes_logiciel_FST.pdf` | `tp/annexes-logiciel-fst.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/ConfigAscenseur.agn` | `tp/fichiers/config-ascenseur.agn` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/Fichiers FST manipulation FESTO (mise en oeuvre dune chaîne dassemblage)-20261019.zip` | `tp/fichiers/fichiers-fst-festo.zip` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/tp-labview-moteur-LS.zip` | `tp/fichiers/tp-labview-moteur-ls.zip` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/tp-labview-moteur-Parvex.zip` | `tp/fichiers/tp-labview-moteur-parvex.zip` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/tp-labview-thermique-retard.zip` | `tp/fichiers/tp-labview-thermique-retard.zip` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/TP_Travaux_Pratiques_Automatique_1.pdf` | `tp/tp-automatique-1.pdf` |
| `EEL7FE-UEC Automatique et Signal/EEL7-AUTO2 Travaux Pratiques Automatique 1 et 2/TP_Travaux_Pratiques_Automatique_2.pdf` | `tp/tp-automatique-2.pdf` |
| `Automatique et signal/CR_TP1_Ascenseur_Grafcet.pdf` | `travaux/cr-tp1-ascenseur-grafcet/CR_TP1_Ascenseur_Grafcet.pdf` |
| `Automatique et signal/CR_TP1_Ascenseur_Grafcet.tex` | `travaux/cr-tp1-ascenseur-grafcet/CR_TP1_Ascenseur_Grafcet.tex` |
| `Automatique et signal/inp.png` | `travaux/cr-tp1-ascenseur-grafcet/inp.png` |
