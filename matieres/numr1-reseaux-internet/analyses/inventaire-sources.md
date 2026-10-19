# NUMR1 — Inventaire des sources

> Mise en place de la matière, 19 octobre 2026 (archive `2A.zip`). Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/numr1/` (hors dépôt). Pages = pages du PDF.
> Identification faite sur les métadonnées, la première page et les sommaires des PDF ; les PDF manuscrits ont été lus sur des aperçus basse résolution. La lecture fine se fait à l'analyse de chaque chapitre.

## 1. Identification

| | |
|---|---|
| Code | NUMR1 (EEL7-NUMR1 ; ancien code : RE223) |
| UE | EEL7FE-UEB Électronique Numérique |
| Enseignants | Patrice Kadionik (cours TCP/IP, TP sockets) ; Olivier Villain (cours partie 2, TP) |
| Année | 2026-2027 (cours : partie 1 v2.3, partie 2 v2.5 ; TP sockets v6.7) |

## 2. Fichiers

### `support/` — support officiel

| Fichier | Pages | Taille |
|---|---|---|
| `support/tcpip-partie-1-ancienne-version.pdf` | 306 | 3,0 Mo |
| `support/tcpip-partie-1-v2-3.pdf` | 248 | 2,1 Mo |
| `support/tcpip-partie-2-v2-5.pdf` | 120 | 1,8 Mo |

### `tp/` — énoncés et fichiers de TP

| Fichier | Pages | Taille |
|---|---|---|
| `tp/presentation-tp-reseaux.pdf` | 8 | 0,1 Mo |
| `tp/tp-sockets-ancienne-version.pdf` | 8 | 0,2 Mo |
| `tp/tp-sockets-v6-7.pdf` | 18 | 0,6 Mo |
| `tp/fichiers/calc.html` |  | 2 ko |
| `tp/fichiers/cur` |  | 1 ko |
| `tp/fichiers/fichiers-projet-serveur-tcp.txt` |  | 1 ko |
| `tp/fichiers/snippet-client.txt` |  | 1 ko |
| `tp/fichiers/snippet-serveur.txt` |  | 1 ko |

### `notes/` — notes de cours

| Fichier | Pages | Taille |
|---|---|---|
| `notes/2023-notes-cours.pdf` | 2 | 3,6 Mo |

### `travaux/` — travaux personnels (non publiés)

| Fichier | Pages | Taille |
|---|---|---|
| `travaux/tp-sockets/monclient1.c` |  | 2 ko |
| `travaux/tp-sockets/monclient2.c` |  | 3 ko |
| `travaux/tp-sockets/monclient3.c` |  | 3 ko |
| `travaux/tp-sockets/monserveur1.c` |  | 2 ko |
| `travaux/tp-sockets/monserveur2.c` |  | 3 ko |
| `travaux/tp-sockets/monserveur3.c` |  | 4 ko |
| `travaux/tp-sockets/monserveur5.c` |  | 6 ko |
| `travaux/tp-sockets/monserveur6.c` |  | 8 ko |
| `travaux/tp-sockets/monserveur6_thread.c` |  | 8 ko |
| `travaux/tp-sockets/monserveur7.c` |  | 10 ko |
| `travaux/tp-sockets/myserverudp.c` |  | 2 ko |

## 3. Plan proposé

Plan à établir à l'analyse : les deux parties du cours (368 p. de diapositives) seront découpées d'après leurs sommaires.


## 4. Choix appliqués par défaut

- Nommage : minuscules sans accents, mots séparés par des tirets ; nom d'origine dans l'archive : § 6.
- Documents d'un ancien élève (dossier « S7 » de l'archive, promotion 2023, même auteur que `notes-2023` d'EANA3) : nature `externe`, préfixe `2023-` ; notes dans `notes/`, TD et comptes rendus de TP manuscrits dans `corriges/`.
- Versions antérieures d'un support officiel : gardées avec le suffixe `-ancienne-version`.
- Fichiers fournis pour les TP (code, projets logiciels, signaux) : `tp/fichiers/`, archives `.zip` conservées telles quelles.
- Travaux personnels d'Armand : `travaux/`, jamais publiés.

## 5. Questions

Aucune question bloquante à l'inventaire. Le plan proposé (§ 3) est à valider avant l'analyse du premier chapitre.

## 6. Correspondance des noms

Chemin dans `2A.zip` (sans le préfixe `2A/`) → chemin dans `sources/numr1/`.

| Nom d'origine | Fichier rangé |
|---|---|
| `S7/S7/Intro aux réseaux et à Internet/Cours prise de notes.pdf` | `notes/2023-notes-cours.pdf` |
| `S7/S7/Intro aux réseaux et à Internet/Cours partie 1.pdf` | `support/tcpip-partie-1-ancienne-version.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/tcpip_enseirb partie 1 v2.3.pdf` | `support/tcpip-partie-1-v2-3.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/tcpip_enseirb partie 2 v2.5.pdf` | `support/tcpip-partie-2-v2-5.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/calc.html` | `tp/fichiers/calc.html` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/cur` | `tp/fichiers/cur` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/Fichiers pour le projet serveur TCP.txt` | `tp/fichiers/fichiers-projet-serveur-tcp.txt` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/snippet client.txt` | `tp/fichiers/snippet-client.txt` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/snippet serveur.txt` | `tp/fichiers/snippet-serveur.txt` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/TP RESEAUX présentation.pdf` | `tp/presentation-tp-reseaux.pdf` |
| `S7/S7/Intro aux réseaux et à Internet/TP Programmation réseau.pdf` | `tp/tp-sockets-ancienne-version.pdf` |
| `EEL7FE-UEB Electronique Numérique/EEL7-NUMR1 Introduction aux réseaux et à Internet. Programmation réseau/tpsocket_enseirb v6.7.pdf` | `tp/tp-sockets-v6-7.pdf` |
| `Reseau/monclient1.c` | `travaux/tp-sockets/monclient1.c` |
| `Reseau/monclient2.c` | `travaux/tp-sockets/monclient2.c` |
| `Reseau/monclient3.c` | `travaux/tp-sockets/monclient3.c` |
| `Reseau/monserveur1.c` | `travaux/tp-sockets/monserveur1.c` |
| `Reseau/monserveur2.c` | `travaux/tp-sockets/monserveur2.c` |
| `Reseau/monserveur3.c` | `travaux/tp-sockets/monserveur3.c` |
| `Reseau/monserveur5.c` | `travaux/tp-sockets/monserveur5.c` |
| `Reseau/monserveur6.c` | `travaux/tp-sockets/monserveur6.c` |
| `Reseau/monserveur6_thread.c` | `travaux/tp-sockets/monserveur6_thread.c` |
| `Reseau/monserveur7.c` | `travaux/tp-sockets/monserveur7.c` |
| `Reseau/myserverudp.c` | `travaux/tp-sockets/myserverudp.c` |
