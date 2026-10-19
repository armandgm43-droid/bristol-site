# EANA3 — Inventaire des sources

> Mise en place de la matière, 7 octobre 2026. Document de travail (`.md`, non rendu par Quarto).
> Sources rangées dans `sources/eana3/` (hors dépôt). Pages = pages du PDF.
> Le texte des PDF manuscrits a été lu sur des aperçus basse résolution : le rattachement aux chapitres est fiable, la lecture fine des notes reste à faire à l'analyse de chaque chapitre.

## 1. Identification de la matière

| | Valeur | Où |
|---|---|---|
| Code | **EANA3** (code utilisé dans `sources/`, le dossier de la matière et les identifiants) | titre du support 2025 (p. 1) ; en-tête de l'examen du 24/10/2025 ; préfixes `E2-EANA3_`, `S7-EANA3_` des fichiers reçus |
| Ancien code | EA234 (énoncés 2023-2025) ; EA210 « Circuits HF & Oscillateurs » (sujets Deval 2021-2022) | en-têtes des énoncés |
| Intitulé | Circuits intégrés | support, p. 1 |
| Enseignants | **François Rivet** (partie « Systèmes contre-réactionnés ») ; **Yann Deval** (partie « Oscillateurs et références de tension ») | support, p. 1 |
| Autre auteur | Nathalie Deltimple (énoncés : oscillateur à résistance négative, oscillateur en anneau) | support, p. 20 et 26 |
| Version du support | 2025 (examen annoncé le 24 octobre 2025) ; aucune version 2026 reçue | support, p. 3 |

## 2. Plan officiel (support, p. 1-2)

**Partie Rivet — Systèmes contre-réactionnés**

- Cours 1 — Ch. 1 Rappels et généralités sur la contre-réaction : 1. systèmes asservis en réaction négative ; 2. robustesse ; 3. linéarisation ; 4. compromis gain-bande passante.
- Cours 2 — 5. Stabilité ; séparation des pôles (exercice guidé).
- Cours 4 — Ch. 2 Amplificateurs en contre-réaction : 0. topologies des quadripôles ; 1. tension-parallèle ; 2. courant-parallèle.
- Cours 6 — 3. tension-série ; 4. courant-série ; 5. synthèse.
- Cours 8 — Ch. 3 Application de la théorie de la contre-réaction : 1. adaptation d'impédance par dégénérescence inductive (exercice guidé).
- Cours 11 — 2. Bandgap de Widlar (exercice guidé) ; stabilité et compensation.

**Partie Deval — Oscillateurs et références de tension**

- Cours 3 — Ch. 1 Oscillateurs : 1. sinusoïdaux (Barkhausen, Colpitts, Hartley).
- Cours 5 — résistance négative ; classes A, B et C.
- Cours 7 — 2. non sinusoïdaux (astables, en anneau).
- Cours 9 — 3. bruit de phase (Leeson, Hajimiri).
- Cours 10 — Ch. 2 Références de tension : 1. bipolaire stable en température.
- Cours 12 — 2. MOS stable en température.
- Cours 13 — 3. bandgap fractionnaire.

TD du support : TD1 Où est la contre-réaction ? ; TD2 Un circuit pour l'espace ; TD3 Modulation d'amplitude ; TD4 Oscillateur à résistance négative ; TD5 Référence de tension stable en température ; TD6 Oscillateur sinusoïdal à AOP ; TD additionnels : oscillateur en anneau, « VDD is not your BFF ».

## 3. Inventaire

### 3.1 `support/` (officiel)

| Fichier (nom reçu) | Pages | Contenu |
|---|---|---|
| `support-cours-2025.pdf` (`E2-EANA3_support_cours_2025.pdf`) | 30 | p. 1-2 plan ; p. 3 H. S. Black ; p. 4-5 exercice guidé « Séparation des pôles » (cours 2) ; p. 6-7 « Adaptation d'impédance par dégénérescence inductive » (cours 8) ; p. 8-10 « Widlar, toute une histoire » (cours 11) ; p. 11-30 énoncés des TD (voir 3.2) |
| `cours02-separation-des-poles.pdf` (`EA234_cours2.pdf`) | 2 | identique au support p. 4-5 |
| `cours08-degenerescence-inductive.pdf` (`EA234_TD5.pdf`) | 2 | identique au support p. 6-7 |
| `cours11-bandgap-widlar.pdf` (`EA234_cours11.pdf`) | 3 | identique au support p. 8-10 (texte à 99,7 %) |

Le support 2025 ne contient **aucun cours rédigé** (ni slides ni poly) : seulement le plan, les exercices guidés et les TD.

### 3.2 `td/` (énoncés officiels)

Numérotation du support 2025. Les fichiers séparés ont le même texte que les pages correspondantes du support (contrôle automatique).

| Fichier (nom reçu) | Pages | Énoncé | = support | Chapitre(s) |
|---|---|---|---|---|
| `td01-ou-est-la-contre-reaction.pdf` (`EA234_TD2.pdf`) | 2 | Où est la contre-réaction ? (Rivet) | p. 11-12 | 2 |
| `td02-circuit-pour-l-espace.pdf` (`EA234_TD10.pdf`) | 4 | Un circuit pour l'espace (Rivet) | p. 13-16 | 2 |
| `td03-modulation-amplitude.pdf` (`E2-EANA3_TD3.pdf`) | 3 | Modulation d'amplitude (Rivet, examen du 25/10/2024) | p. 17-19 | 1, 2 |
| `td03-2026-bandgap-brokaw.pdf` (`E2-EANA3_TD3 (1).pdf`) | 2 | « Une référence des circuits intégrés » : bandgap de Brokaw (Rivet, **examen EANA3 du 24/10/2025**) ; reçu en 2026 sous le nom TD3 | — | 3, 5 |
| `td04-oscillateur-resistance-negative.pdf` (`EA234_TD4.pdf`) | 2 | Oscillateur à résistance négative (Deltimple) | p. 20-21 | 4 |
| `td04-2026-recueil-sujets-deval.pdf` (`E2-EANA3_TD4.pdf`) | 10 | Recueil reçu en 2026 sous le nom TD4 : oscillateur à déphasage (EA210, 22/11/2021 et 08/04/2022), référence de tension bipolaire de Brokaw (EANA3-EA234, **24/10/2025**), générateur de courant suppresseur de variations (EANA3-EA234, 02/04/2026, Deval et Rivet) | — | 4, 5, 3 |
| `td05-reference-tension-cmos.pdf` (`EA234_TD5 (1).pdf`) | 2 | Référence de tension CMOS stable en température (Deval, 06/11/2023) | p. 22-23 | 5 |
| `td06-oscillateur-aop.pdf` (`EA234_TD7.pdf`) | 2 | Oscillateur sinusoïdal à AOP (Deval, 07/03/2024) | p. 24-25 | 4 |
| `td-add-oscillateur-anneau.pdf` (`EA234_TD5 (2).pdf`) | 3 | Oscillateur en anneau (Deltimple) | p. 26-28 | 4 |
| `td-add-vdd-is-not-your-bff.pdf` (`EA234_TD11.pdf`) | 2 | VDD is not your BFF : régulateur LDO (Rivet, 06/11/2023) | p. 29-30 | 2, 3 |

### 3.3 `notes/` (notes de cours manuscrites)

Deux jeux, **aucun daté par séance** (dates de numérisation seulement). **Ce ne sont pas les notes d'Armand** (Q1, tranchée le 7 octobre 2026) : nature `externe`. Armand n'a pas encore ses propres notes de 2026-2027.

**Jeu `notes-2023` : notes manuscrites sur papier quadrillé, numérisées le 13/11/2023, nommées par l'enseignant.**

| Fichier (nom reçu) | Pages | Contenu | Chapitre |
|---|---|---|---|
| `2023-cours-01-rivet.pdf` (`Cours 1 (Rivet).pdf`) | 5 | p. 1-3 : systèmes asservis, robustesse, linéarisation, compromis gain-bande ; p. 3-5 : stabilité, marges de gain et de phase | 1 |
| `2023-cours-02-rivet.pdf` (`Cours 2 (Rivet).pdf`) | 6 | stabiliser un système instable (solution brutale, séparation des pôles) ; exercice guidé « Séparation des pôles » (parties 1 et 2) | 1 |
| `2023-cours-04-06-rivet.pdf` (`Cours 4 et 6 (Rivet).pdf`) | 8 | topologies des quadripôles ; les quatre contre-réactions (transfert, Zi, Zo) ; p. 8 : tableau de synthèse | 2 |
| `2023-cours-08-rivet.pdf` (`Cours 8 - Ou est la contre-réaction (Rivet).pdf`) | 4 | exercice « Où est la contre-réaction ? » (= TD1 du support 2025), fait en cours 8 en 2023 | 3 (et TD1) |
| `2023-cours-11-rivet.pdf` (`Cours 11 (Rivet).pdf`) | 2 | « Widlar, toute une histoire » (exercice guidé) | 3 |
| `2023-cours-03-05-deval.pdf` (`Cours 3 et 5 (Deval).pdf`) | 6 | oscillateurs sinusoïdaux : principe, Barkhausen, topologies, Colpitts (calcul), Hartley ; autres topologies : résistance négative (paire croisée), oscillateur à déphasage | 4 |
| `2023-cours-07-deval.pdf` (`Cours 7 ( Deval).pdf`) | 3 | oscillateurs non sinusoïdaux : astable à comparateur, oscillateur en anneau | 4 |
| `2023-cours-09-deval.pdf` (`Cours 9 (Deval).pdf`) | 4 | bruit de phase : théorie de Leeson, théorie de Hajimiri (fonction de sensibilité impulsionnelle) | 4 |
| `2023-cours-10-deval.pdf` (`Cours 10 (Deval).pdf`) | 6 | p. 1-3 : dépendance thermique de $V_{BE}$, référence bandgap bipolaire ; p. 4-6 : référence MOS stable en température (p. 4 : photo du tableau) | 5 |

**Jeu `tableau-2020` : tableau numérique de l'enseignant (support annoté au stylet), exporté en septembre 2020.** L'écriture et le contenu (plan du support annoté, exercice guidé annoté) laissent penser qu'il s'agit du tableau de F. Rivet ; à confirmer (Q1).

| Fichier (nom reçu) | Pages | Contenu | Chapitre |
|---|---|---|---|
| `2020-tableau-cours-01.pdf` (`Cours 1 - Notes.pdf`) | 7 | plan du chapitre 1 ; fonction de transfert, robustesse, linéarisation, compromis gain-bande passante | 1 |
| `2020-tableau-cours-02.pdf` (`Cours 2 - Tableau.pdf`) | 6 | p. 1-4 : stabilité, marges, diagramme de Bode, solutions pour stabiliser ; p. 5-6 : énoncé « Séparation des pôles » annoté | 1 |
| `2020-tableau-cours-03.pdf` (`Cours 3 - Tableau.pdf`) | 6 | p. 1-3 : séparation des pôles (calcul), capacité de compensation ; p. 4-6 : début du chapitre 2 (topologies, contre-réaction courant-série) | 1 (p. 1-3), 2 (p. 4-6) |
| `2020-tableau-cours-04.pdf` (`Cours 4 - Tableau.pdf`) | 9 | contre-réactions courant-série, tension-série, courant-parallèle (transfert, Zi, Zo) | 2 |

### 3.4 `corriges/` (corrigés manuscrits, phase 2)

| Fichier (nom reçu) | Pages | Corrigé de | Remarque |
|---|---|---|---|
| `2023-recueil-corriges-td.pdf` (`Untitled.pdf`) | 11 | séparation des pôles, Où est la contre-réaction ?, « TD1 amplificateur à contre-réaction », mode commun, circuit immunisé, oscillateur en anneau, référence CMOS, Widlar | même écriture que `notes-2023` ; recoupe les fichiers ci-dessous |
| `2023-td01-amplificateur-contre-reaction.pdf` | 2 | « TD1 Amplificateur à contre-réaction » | **énoncé non identifié** parmi les énoncés reçus |
| `2023-td02-contre-reaction-mode-commun.pdf` | 2 | « TD2 Contre-réaction de mode commun » | **énoncé absent** |
| `2023-td03-circuit-immunise.pdf` | 2 | TD2 du support (Un circuit pour l'espace) | |
| `2023-td04-oscillateur-resistance-negative.pdf` | 3 | TD4 | |
| `2023-td05-oscillateur-anneau.pdf` | 3 | TD additionnel (anneau) | |
| `2023-reference-tension-cmos-dual-vth.pdf` | 2 | TD5 | |
| `2025-td04-oscillateur-resistance-negative.pdf` (`S7-EANA3_corrige_…`) | 5 | TD4 | autre écriture, numérisé en 09/2025 |

### 3.5 `annales/`

| Fichier (nom reçu) | Pages | Contenu |
|---|---|---|
| `2016-2017-corrige-manuscrit.pdf` (`Sujet 2016-2017.pdf`) | 2 | corrigé manuscrit de l'« Adaptation d'impédance par dégénérescence inductive » (énoncé = support p. 6-7) — utile au chapitre 3 |
| `2017-2018-corrige-manuscrit.pdf` (`Sujet 2017-2018.pdf`) | 3 | corrigé manuscrit d'un sujet « Amplificateur large bande » (deux MOS) ; **énoncé absent** |

Les sujets d'examen datés (2023 à 2026) sont dans `td/`, où l'enseignant les a distribués comme TD.

## 4. Plan des chapitres proposé

Choix par défaut (conventions § 14) : **un chapitre Bristol par chapitre du support**, numérotés à la suite (partie Rivet, puis partie Deval, dans l'ordre du support p. 1), même si les séances alternent les deux enseignants.

| N° | Fichier prévu | Contenu (support) | Notes rattachées |
|---|---|---|---|
| 1 | `01-generalites-contre-reaction.qmd` | cours 1-2 : réaction négative, robustesse, linéarisation, gain-bande, stabilité, séparation des pôles | `notes-2023` c. 01, 02 ; `tableau-2020` c. 01, 02, 03 (p. 1-3) |
| 2 | `02-amplificateurs-contre-reaction.qmd` | cours 4-6 : topologies, quatre contre-réactions, synthèse | `notes-2023` c. 04-06 ; `tableau-2020` c. 03 (p. 4-6), 04 |
| 3 | `03-applications-contre-reaction.qmd` | cours 8, 11 : dégénérescence inductive, bandgap de Widlar, stabilité et compensation | `notes-2023` c. 08 (« Où est la CR ? »), 11 ; annale 2016-2017 (corrigé) |
| 4 | `04-oscillateurs.qmd` | cours 3, 5, 7, 9 : sinusoïdaux, résistance négative, classes A/B/C, non sinusoïdaux, bruit de phase | `notes-2023` c. 03-05, 07, 09 |
| 5 | `05-references-de-tension.qmd` | cours 10, 12, 13 : bipolaire, MOS, bandgap fractionnaire | `notes-2023` c. 10 |

Le chapitre 4 est long (quatre séances) : il pourra être découpé à l'analyse si besoin (les labels, sans numéro, le permettent avant toute publication).

## 5. Manques et points à signaler

**Chapitres ou sections sans notes**

- Ch. 3 : « Adaptation d'impédance par dégénérescence inductive » (cours 8 du plan 2025) : pas de notes de cours ; seul le corrigé manuscrit de l'annale 2016-2017 la traite. « Stabilité et compensation » (cours 11) : non repérée dans `notes-2023` c. 11 (Widlar) ; la capacité de compensation apparaît au chapitre 1 (`tableau-2020` c. 03).
- Ch. 4 : **classes A, B et C** (cours 5) : absentes des notes.
- Ch. 5 : **bandgap fractionnaire** (cours 13) : aucune note. La référence MOS (cours 12) n'est couverte que par `notes-2023` c. 10, p. 4-6.
- Aucun cours rédigé par les enseignants : le cours Bristol reposera presque entièrement sur les notes, ce qui rend la question Q1 importante.

**Notes sans chapitre** : aucune. `notes-2023` c. 08 est un exercice (TD1 du support 2025) fait en cours en 2023 : rattaché au chapitre 3 (application de la contre-réaction), à défaut de chapitre « exercices ».

**Lisibilité** (à confirmer à l'analyse, sur les images en pleine résolution)

- Les deux jeux sont globalement lisibles (écriture régulière, schémas nets).
- `notes-2023` c. 10, p. 4 : photo d'un tableau noir, peu lisible.
- `tableau-2020` c. 02, p. 6 et c. 03 : passages barrés ou surchargés de couleurs ; à lire avec soin.
- La reconnaissance automatique du texte (OCR des PDF) est inutilisable : la lecture se fera sur les images.

**Énoncés manquants** : corrigés « TD1 Amplificateur à contre-réaction », « TD2 Contre-réaction de mode commun » (2023) et annale 2017-2018.

**Doublons** : les 11 énoncés séparés de `support/` et `td/` sont identiques aux pages du support 2025 ; conservés (rien n'est supprimé). Le recueil `2023-recueil-corriges-td.pdf` recoupe les corrigés 2023 séparés.

## 6. Questions bloquantes

- ~~**Q1 — Origine des notes.**~~ *Tranchée le 7 octobre 2026 : ce ne sont pas les notes d'Armand, qui n'a pas encore les siennes. Les deux jeux sont des sources `externe` (voir § 8).* Question d'origine : Qui a écrit `notes-2023` (papier quadrillé, numérisé en novembre 2023) et `tableau-2020` (tableau numérique, septembre 2020) ? Ce sont des années où tu n'étais pas à l'ENSEIRB. La réponse fixe le champ `nature` des sources (`personnelle` ou `externe`) et la façon de les présenter : `CONTEXTE_PROJET.md` § 7.2 définit les blocs *Notes de cours* comme tes notes, et § 6.1 demande d'identifier comme tels les documents de camarades. Non bloquant pour l'inventaire, **bloquant pour l'analyse du chapitre 1**.

## 7. Choix appliqués par défaut

1. **Code** `eana3` (support et examen 2025) ; ancien code EA234 noté dans la fiche matière.
2. **Dossier** `sources/Circuits integres/` renommé `sources/eana3/` (comme `sources/ts227/`), sous-dossiers `support/`, `notes/`, `td/`, `corriges/`, `annales/`.
3. **Nommage des notes** (nouveau, conventions § 2 ne prévoit qu'un jeu daté par séance) : `notes/<année>-cours-NN-<enseignant>.pdf` et `notes/<année>-tableau-cours-NN.pdf`, l'année étant celle du jeu ; ids proposés pour le front matter : `notes-2023-c01`, `tableau-2020-c01`… Citation par page du PDF. Convention à confirmer avant de l'inscrire dans `conventions.md`.
4. **Nommage des TD** : numéros du support 2025 ; les versions distribuées en 2026 portent `-2026`.
5. **Sujets d'examen distribués comme TD** rangés dans `td/` ; `annales/` reçoit les corrigés de sujets non distribués.
6. **Plan** : cinq chapitres, un par chapitre du support (§ 4).
7. **Paquet de cartes** : `revision/cartes/eana3.json` généré vide par `scripts/flashcards.py`, modifié pour produire un paquet vide quand une matière n'a pas encore de carte (`architecture.md` § 6).
8. **Fiche matière** : notations relevées à l'inventaire, à confirmer chapitre par chapitre.

## 8. Décision sur Q1 et conséquences (7 octobre 2026)

- `notes-2023` et `tableau-2020` : **nature `externe`** dans le front matter des chapitres (`CONTEXTE_PROJET.md` § 6.1 : documents de camarades et ressources externes, à identifier comme tels).
- Auteurs inconnus. `tableau-2020` ressemble au tableau numérique de F. Rivet (support annoté) : s'il s'agit bien du tableau de l'enseignant, il pourra être requalifié.
- **Présentation dans le cours (choix par défaut, convention à confirmer)** : le contenu tiré de ces notes va dans des blocs `.notes` (contenu du tableau et de l'oral, § 7.2), mais chaque bloc **cite sa source** (`[notes-2023-c01, p. 2]`), et la fiche matière et la future page « À propos » précisent que ces notes ne sont pas celles d'Armand. Pas de nouvelle classe CSS. Alternative si Armand préfère une distinction visible : une étiquette propre (ex. `✎ Notes externes`), à ajouter dans `assets/bristol.scss` et `conventions.md` § 5.
- **Vigilance accrue** : notes d'années antérieures (2020, 2023), donc d'un cours qui a pu changer (ordre des séances déjà différent). Tout écart avec le plan ou les énoncés 2025-2026 passe en *À vérifier*.
- **Notes d'Armand à venir** : nommées selon la convention habituelle (`notes/AAAA-MM-JJ.pdf`, nature `personnelle`). Un chapitre rédigé avant leur arrivée sera mis à jour ensuite (`CONTEXTE_PROJET.md` § 17 : retour explicite, modification ciblée, nouvelle validation).

## 9. Ajouts du 19 octobre 2026 (archive `2A.zip`)

Les fichiers EANA3 de l'archive étaient presque tous déjà rangés (contrôle par empreinte MD5). Nouveaux fichiers :

| Fichier (nom reçu) | Pages | Contenu | Nature |
|---|---|---|---|
| `tp/tp-oscillateur-lc-350nm.pdf` (`LC Oscillator LAB 350nm.pdf`) | 11 | énoncé du TP (TDM) : conception d'un oscillateur LC en technologie CMOS 350 nm (Cadence) | officielle |
| `corriges/2023-tp-cadence-lab-cr.pdf` (`S7/…/TDM/CR Cadence Lab.pdf`) | 6 | compte rendu manuscrit du TP | externe (même auteur que `notes-2023`) |
| `corriges/2023-tp-cadence-lab-notes.pdf` (`S7/…/TDM/Cadence Lab.pdf`) | 4 | notes manuscrites sur le TP | externe |

Le TP n'est pas encore rattaché aux chapitres (lien naturel : chapitre 4, oscillateurs).
