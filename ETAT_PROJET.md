# Bristol — État du projet

> Où en est le projet. Mis à jour **à la fin de chaque session de travail**.
> Vision et méthode : `CONTEXTE_PROJET.md`. Règles : `conventions.md`. Technique : `architecture.md`. Tâches : `TODO.md`.
>
> Dernière mise à jour : 29 octobre 2026 (EARF1 : 4 chapitres validés, 74 flashcards).

---

## 1. En bref

Le prototype est validé. Le premier chapitre de test est le **chapitre 2 de TS227** (*Principes de communication en l'absence de bruit*). Son **rapport d'analyse** est fait et **toutes ses questions sont tranchées** (étape 3, section 13 du rapport `matieres/ts227-communications-numeriques/analyses/02-communication-sans-bruit.md`). Le chapitre est **rédigé** (texte et figures, étapes 4 et 5) : statut `redige`. Vérification faite (étape 6, rapport section 13.10), points V1 à V6 tranchés et appliqués : le chapitre est **validé** par Armand (statut `valide`, rapport section 13.11). **Flashcards générées** (étape 8, 61 cartes, rapport section 13.12) : statut `flashcards`. Le premier chapitre est donc fait de bout en bout.

**Chapitre 3 de TS227** (*DSP des signaux codés en ligne*) : analyse, rédaction et figures (étapes 2 à 5), exercices du TD intégrés ; vérifié (étape 6, rapport § 17), **validé** par Armand, `av-dsp-porte-notes` tranché d'après la correction du TD ; **flashcards générées** (étape 8, 56 cartes, rapport § 18) : statut `flashcards`. 0 bloc ouvert, 5 tranchés, 4 levés.

**Chapitres 1 et 4 de TS227** (*Introduction* ; *Transmission en présence de bruit*) : analyse, rédaction et figures (étapes 2 à 5) dans la même session ; TD ex. 3, ex. 4 et ex. 5 q. 12-13 intégrés au chapitre 4 ; chapitre 1 rédigé à partir du **poly seul** (aucune note). Questions bloquantes tranchées (Armand a laissé le choix à Claude) : 0 bloc ouvert, 2 tranchés (ch. 1) et 11 tranchés (ch. 4) ; rapports, § 16. Vérifiés (étape 6, rapports § 17 : aucun point bloquant, 7 corrections de forme), **validés** par Armand, **flashcards générées** (étape 8 : 12 cartes ch. 1, 57 cartes ch. 4 ; rapports § 18) : statut `flashcards`. `ts227.json` = 186 cartes.

Révision : en local avec `quarto preview` (port fixe 4848, `http://localhost:4848/revision/`). Le paquet TS227 provisoire (clés `ts-…`) est abandonné (question 5) ; `revision/cartes/ts227.json` est généré par `scripts/flashcards.py`. L'ancien site de cartes (dépôt `bristol`) est **figé**.

**Nouvelle matière EANA3 — Circuits intégrés** (F. Rivet, Y. Deval) : mise en place faite (sources triées dans `sources/eana3/`, arborescence `matieres/eana3-circuits-integres/`, fiche matière, entrées dans `_quarto.yml` et sur l'accueil, paquet de cartes vide). Inventaire et plan proposé en 5 chapitres : `matieres/eana3-circuits-integres/analyses/inventaire-sources.md`. Q1 tranchée : les notes disponibles (`notes-2023`, `tableau-2020`) **ne sont pas celles d'Armand** (nature `externe`) ; Armand n'a pas encore les siennes. Plus de question bloquante avant l'analyse du chapitre 1.

**EANA3, rédaction des chapitres (8 octobre 2026)** : plan en 5 chapitres validé ; catégorie *Notes externes* (`.notes-externes`, `✎ Notes externes`) créée pour les notes qui ne sont pas celles d'Armand. Sources manuscrites transcrites intégralement (`sources/eana3/transcriptions/`, non publiées). **Chapitre 1** (*Rappels et généralités sur la contre-réaction*) : analyse, rédaction, 7 figures, exercice guidé « Séparation des pôles » intégré ; statut `redige` ; 7 blocs *À vérifier* ouverts (questions : rapport § 14). **Chapitre 2** (*Amplificateurs en contre-réaction*) : analyse, rédaction, 6 figures, TD 1 intégré ; statut `redige` ; aucun bloc *À vérifier* ; TD 2, TD 3 et « VDD is not your BFF » reportés au chapitre 3. **Chapitre 3** (*Applications de la théorie de la contre-réaction*) : chapitre d'exercices (dégénérescence inductive, Widlar, TD 2, TD 3, TD additionnel, partie Rivet du sujet 2025 sur le bandgap de Brokaw) ; 6 figures ; statut `redige` ; 2 blocs *À vérifier* ; les 4 TD n'ont pas de corrigé : solutions proposées en *Complément*, à relire en priorité. **Chapitre 4** (*Oscillateurs*) : cours entièrement tiré des notes externes de 2023 (Barkhausen, Colpitts, résistance négative, astables, anneaux, Leeson, Hajimiri) ; TD 4 (deux corrigés externes), TD 6, TD anneau, sujet 2021 sur l'oscillateur à déphasage ; 9 figures ; statut `redige` ; 4 blocs *À vérifier* ; classes A, B et C sans aucune source. **Chapitre 5** (*Références de tension*) : cours tiré des notes externes de 2023 (cours 10 : $V_{BE}(T)$, PTAT, bandgaps de Widlar, à miroir PNP et CMOS, référence dual-$V_{th}$ avec le corrigé d'une autre version du TD 5) ; TD 5 (version SOI), partie Deval du sujet Brokaw 2025, sujet 2026 « générateur de courant suppresseur de variations » ; 9 figures ; statut `redige` ; 2 blocs *À vérifier* ; bandgap fractionnaire (cours 13) sans notes. **Les 5 chapitres EANA3 sont rédigés** ; prochaine étape : réponses d'Armand aux questions des rapports (§ 14), puis vérification (étape 6) et flashcards.

**Matières du S7 (19 octobre 2026)** : l'archive `sources/2A.zip` (cours de l'année) est redistribuée dans `sources/<code>/` (413 fichiers, copies contrôlées par MD5). Les 14 matières sans fiche (AUTO1, AUTO2, AUTO3, EAEP1, EANA1, EANA2, EANA4, EARF1, NUMC1, NUME3, NUMR1, PROJ1, TSIG1, TSIG2) ont maintenant une fiche matière, un inventaire des sources (`analyses/inventaire-sources.md`, avec la correspondance des noms d'origine), une barre latérale et un paquet de cartes vide. Plans proposés, **à valider** : AUTO1 (6 chapitres), AUTO3 (4), EAEP1 (7), EANA2 (5), EARF1 (4), NUMC1 (6), TSIG1 (5, d'après des notes externes) ; EANA1 sans support officiel, NUMR1 à découper ; AUTO2, EANA4, NUME3, PROJ1, TSIG2 sont des matières de TP ou de projet (pas de chapitre de cours, phase 2). Documents d'un ancien élève (dossier « S7 », promotion 2023, même auteur que `notes-2023` d'EANA3) rangés en nature `externe`.

**TSIG1 — Traitement numérique du signal (20 octobre 2026)** : notes d'Armand reçues (24 photos : 13 feuillets, 22 pages + 2 doublons), rangées dans `sources/tsig1/notes/date-inconnue/` + `date-inconnue.pdf`, transcrites (`sources/tsig1/transcriptions/notes-2026.md`). **Plan des notes d'Armand retenu** (choix d'Armand, à la place du plan des notes 2023) : 1. Échantillonnage et signal discret, 2. Systèmes discrets et convolution, 3. TFD et interprétation fréquentielle des SLI, 4. Implémentation des SLI et équations aux différences, 5. SLI et représentation en phase. Les **5 chapitres sont rédigés et vérifiés** (statut `verifie`) : notes d'Armand en `.notes`, notes 2023 et corrigés de TD 2023 en `.notes-externes`, 16 exercices des TD 1 à 3 intégrés (sections « Exercices du TD »), 11 figures ; vérification : ~290 blocs de formules et 16 exercices recalculés, 1 801 formules compilées (MathJax 3.2.2), rendu Quarto sans avertissement. **30 blocs *À vérifier* ouverts** (1/4/9/11/5), dont 11 erreurs des corrigés 2023. Méthode « deux temps » choisie par Armand : il relit et tranche, puis Claude génère les cartes définitives et retire le paquet provisoire `tsig1p-`. Partiel le jeudi 22 octobre.

**TSIG1 — Annales (20 octobre 2026)** : 9 sujets corrigés, affichés **en images découpées question par question** avec la solution sous chaque question (demande d'Armand) : partiels 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2019-2020, 2022-2023, 2025-2026, examens de mars 2014 et mars 2018 (les trois derniers sujets du recueil de TD ; 2014-2015 et 2016-2017 y figurent aussi, identiques aux scans). 138 images (≈ 2 Mo) dans `annales/sujets/`, régénérables (`<annale>-decoupe.py`, `normaliser-largeur.py`) ; 9 figures calculées ; 11 blocs *À vérifier* `av-ann…` (énoncés ambigus ou incomplets) ; chaque solution vérifiée par le calcul ; rendu Quarto du site complet sans avertissement.

**EARF1 — Modulations analogiques et numériques (29 octobre 2026)** : à la demande d'Armand (« fais toutes les étapes jusqu'à ce que ce cours soit considéré comme validé »), les **4 chapitres** sont analysés, rédigés, vérifiés et **validés** (statut `valide`, validation déléguée par Armand) : 1. Introduction : signaux et outils d'analyse ; 2. Modulations linéaires ; 3. Modulations angulaires ; 4. Introduction aux modulations numériques. Le support « Student » est complet (aucun trou). Sources : supports de T. Taris, TD 1 (GNU Radio, sans corrigé), TD 2 et 3, notes et corrigés de 2023 (ancien élève, `.notes-externes`). 16 figures régénérables ; 11 blocs *À vérifier*, **tous tranchés** par Claude sur délégation (coquilles du support : signe de la série de Bessel, facteur $2\pi$ du discriminateur, $\pi/8 \neq 45°$ en 16QAM, unité du *symbol rate*…) ; solutions des TD sans corrigé en *Complément*. Rapports : `matieres/earf1-modulations-communications/analyses/0N-*.md`. **Flashcards générées** (étape 8, à la demande d'Armand) : 74 cartes (17/18/21/18), `revision/cartes/earf1.json` ; statut `flashcards`.

Décision du 7 octobre 2026 : le site sera **publié à la fin pour les étudiants de la promo**, derrière un accès réservé et avec l'accord des enseignants (`CONTEXTE_PROJET.md` § 5.4).

---

## 2. Fait

- [x] `CONTEXTE_PROJET.md` : vision, principes, méthode.
- [x] `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` créés (6 octobre 2026).
- [x] Squelette Quarto : `_quarto.yml`, `index.qmd`, `README.md`, `.gitignore`.
- [x] Thème `assets/bristol.scss` avec les styles HTML des quatre catégories.
- [x] Macros communes dans `_macros.qmd`.
- [x] Page `demo-conventions.qmd` (rendu des quatre catégories, références croisées).
- [x] Fiche matière TS227 : enseignants, plan, table des notations cours/TD.
- [x] Arborescence de la matière TS227 (dossiers vides).
- [x] Application de révision copiée dans `revision/`, avec les 6 paquets hérités.
- [x] Dépôt Git initialisé (commit `501e006`, « Initialisation du projet Bristol »).
- [x] Poly TS227 copié dans `sources/ts227/support/`.
- [x] Prototype validé par Armand ; chapitre 2 choisi comme chapitre de test (7 octobre 2026).
- [x] Notes manuscrites TS227 reçues (5 feuillets recto-verso, date inconnue) : `sources/ts227/notes/date-inconnue.pdf` et photos dans `date-inconnue/`.
- [x] TD et correction TS227 copiés dans `sources/ts227/support/` et inventoriés.
- [x] Rapport d'analyse du chapitre 2 (7 octobre 2026).
- [x] Étape 3 du chapitre 2 : 16 questions tranchées, 8 points *À vérifier* traités (7 octobre 2026).
- [x] `conventions.md` : 5 conventions ajoutées (voir section 6).
- [x] Rédaction du texte du chapitre 2 de TS227, ajouté à la barre latérale et à la fiche matière (7 octobre 2026).
- [x] Figures du chapitre 2 de TS227 : 12 SVG régénérables dans `figures/` (7 octobre 2026).
- [x] Fiche matière TS227 : table des notations étendue (poly, TD, notes), conventions de la matière (TF, $\Pi_T$), sources, ordre du cours.
- [x] TS227 chapitre 2 vérifié puis validé (7 octobre 2026, rapport sections 13.10 et 13.11).
- [x] Direction artistique unique site + application (« fiche bristol »), jetons dans `assets/bristol-tokens.css`, mode sombre, barre de navigation commune (7 octobre 2026). Voir `conventions.md` § 13 et `architecture.md` § 4.
- [x] Flashcards du chapitre 2 de TS227 : `flashcards/02-communication-sans-bruit.yml`, 61 cartes ; V5 trié (2 labels retirés) ; statut `flashcards` (7 octobre 2026).
- [x] `scripts/flashcards.py` : conversion YAML → `revision/cartes/<matiere>.json`, contrôles, macros développées ; lancé : `ts227.json` régénéré (61 cartes `ts227-…`, les 129 cartes `ts-…` disparaissent).
- [x] Port de `quarto preview` fixé à 4848 dans `_quarto.yml` (progression de révision conservée) ; noté dans `architecture.md` § 6 et § 8.
- [x] Correction de `architecture.md` (§ 6) et de ce fichier : l'export actuel de l'application exporte les **cartes**, pas la progression ; renvoi vers la tâche « export/import de la progression » de `TODO.md` (7 octobre 2026). `README.md` ne contenait pas ce conseil.
- [x] TS227 chapitre 3 : rapport d'analyse, `cours/03-dsp-signaux-codes-en-ligne.qmd` (TD ex. 2 et ex. 5 q. 10-11 intégrés), 5 figures `figures/03-*.py` + SVG ; ajouté à `_quarto.yml` et à la fiche matière (convention $\sinc$, notations de l'autocorrélation) (7 octobre 2026).
- [x] TS227 chapitre 3 vérifié (rapport § 17 : exhaustivité support/notes/TD, 569 formules, références ; 6 corrections de forme), validé, `av-dsp-porte-notes` tranché (7 octobre 2026).
- [x] TS227 chapitres 1 et 4 : rapports d'analyse, `cours/01-introduction.qmd` et `cours/04-transmission-presence-bruit.qmd`, figures `figures/01-shannon-weaver.tex` (TikZ) et `figures/04-*.py` (7 matplotlib) + SVG ; TD ex. 3, 4 et ex. 5 q. 12-13 intégrés ; `_quarto.yml` et fiche matière (statuts, notations du ch. 4) mis à jour (7 octobre 2026).
- [x] Flashcards du chapitre 3 de TS227 : `flashcards/03-dsp-signaux-codes-en-ligne.yml`, 56 cartes ; `scripts/flashcards.py` lancé : `ts227.json` = 117 cartes (61 + 56) ; statut `flashcards` (7 octobre 2026).
- [x] TS227 chapitres 1 et 4 vérifiés (rapports § 17 : exhaustivité poly/notes/TD, 803 formules, références, figures ; 7 corrections de forme, dont la ligne **Décision** des 13 blocs tranchés), validés, flashcards (`flashcards/01-introduction.yml`, 12 cartes ; `flashcards/04-transmission-presence-bruit.yml`, 57 cartes) ; `flashcards.py` lancé : `ts227.json` = 186 cartes ; statut `flashcards` (7 octobre 2026).

- [x] EANA3 — mise en place (7 octobre 2026) : 37 PDF triés et renommés dans `sources/eana3/{support,td,notes,corriges,annales}/` (dossier `sources/Circuits integres/` renommé) ; `matieres/eana3-circuits-integres/` (arborescence, `index.qmd`, `analyses/inventaire-sources.md`) ; `_quarto.yml` (barre latérale `eana3`) ; `index.qmd` (accueil) ; `scripts/flashcards.py` produit un paquet vide pour une matière sans carte → `revision/cartes/eana3.json` (0 carte) ajouté à `index.json` ; `architecture.md` § 6.

- [x] Archive 2A (19 octobre 2026) : 413 fichiers de `sources/2A.zip` rangés dans `sources/<code>/{support,td,tp,tp/fichiers,notes,corriges,annales,travaux}` et contrôlés ; fiches matières et inventaires des 14 matières du S7 ; `_quarto.yml` (14 barres latérales) ; accueil réorganisé par UE ; 14 paquets vides (`scripts/flashcards.py`) ; compléments des fiches TS227 (TP, TS205, notes 2023) et EANA3 (TP oscillateur LC) ; `conventions.md` § 2 (dossiers `tp/`, `travaux/`, documents d'un tiers, versions antérieures).

- [x] Refonte allégée de la DA (19 octobre 2026) : jetons (`assets/bristol-tokens.css`), thème (`assets/bristol.scss`), CSS de l'application (`revision/index.html`, JavaScript inchangé), accueil en cartes par UE (`index.qmd`), statuts en pastilles dans 9 fiches matières ; police *Source Sans 3* ; `conventions.md` § 4 et § 13, `architecture.md` § 4.

- [x] **Refonte complète de l'interface (28 octobre 2026)** : design system « Bristol 2026 » (`assets/bristol-tokens.css`, `assets/bristol.scss` réécrits ; polices Geist auto-hébergées dans `assets/fonts/`) ; accueil en tableau de bord généré par `scripts/catalogue.ts` (pre-render Deno) avec `matieres/domaines.json` ; page `annales.qmd` ; filtre `assets/bristol.lua` + partial `assets/partials/title-block.html` (contexte des chapitres, « Pour continuer », accès rapides des fiches matières) ; `assets/bristol.js` (Ctrl K, reprise de lecture, cartes dues, filtres) ; application de révision : CSS et gabarits refaits, mode concentration, progression de séance, liens profonds `#reviser=` / `#paquet=` (planification, stockage, fusion inchangés) ; `_quarto.yml` (pre-render, navigation, pied de page, filtre, grille, thème `default`). Contrôles : rendu Quarto 1.10.19 complet sans avertissement (65 pages), aucune erreur JavaScript en clair et en sombre, aucun débordement horizontal sur mobile (375 px), captures (accueil, fiche, chapitres, annales, révisions, séance ; clair, sombre, mobile), synchronisation clair/sombre site ↔ application. Copies des fichiers d'avant la refonte : `_apercu_tmp/avant-refonte/`. `conventions.md` § 6 et § 13, `architecture.md` § 3 et § 4.

- [x] EARF1 (29 octobre 2026) : 4 chapitres `cours/01` à `04` (statut `valide`), 16 figures (`figures/0N-*.py` + SVG), 4 rapports d'analyse, fiche matière (plan, table des notations, conventions, sources), barre latérale `_quarto.yml`, inventaire mis à jour. Contrôles : rendu Quarto 1.10.19 sans avertissement (projet minimal), 1094 formules compilées avec MathJax 3.2.2 sans erreur, références croisées résolues.

## 3. En cours

- EANA3 : plan proposé (5 chapitres) et choix par défaut à revoir par Armand (inventaire § 4, § 7, § 8). Analyse du chapitre 1 possible ; notes d'Armand attendues.
- Chapitres 1 et 4 de TS227 terminés (flashcards générées). À faire par Armand : contrôler le rendu des chapitres et des 69 cartes avec `quarto preview`.
- Chapitre 3 de TS227 terminé (flashcards générées). À faire par Armand : contrôler le rendu du chapitre et des 56 cartes avec `quarto preview`.
- Chapitre 2 de TS227 terminé (flashcards générées). À faire par Armand : contrôler le rendu des cartes dans l'application (`quarto preview`) et signaler les cartes à reprendre.

## 4. À faire

Voir `TODO.md`.

---

## 5. Statut des chapitres

### TS227 — Introduction aux communications numériques

| N° | Chapitre (plan du poly) | Fichier | Statut | Blocs *À vérifier* ouverts |
|---|---|---|---|---|
| 1 | Introduction | `cours/01-introduction.qmd` | **flashcards** (12 cartes ; poly seul) | 0 ouvert + 2 tranchés (`av-osi-couches-identiques`, `av-recepteur-destination`) |
| 2 | Principes de communication en l'absence de bruit | `cours/02-communication-sans-bruit.qmd` | **flashcards** (61 cartes) | 0 ouvert + 4 tranchés (`av-signe-tf-nyquist`, `av-centre-symetrie-nyquist`, `av-quiz-debit-porte`, `av-echelles-figure-cosinus-sureleve`) |
| 3 | DSP des signaux codés en ligne | `cours/03-dsp-signaux-codes-en-ligne.qmd` | **flashcards** (56 cartes) | 0 ouvert + 5 tranchés (`av-variance-affine`, `av-esperance-exercice-bpsk`, `av-moment-ordre-2-notes`, `av-dsp-porte-notes`, `av-phase-tf-porte-td`) |
| 4 | Transmission en présence de bruit | `cours/04-transmission-presence-bruit.qmd` | **flashcards** (57 cartes) | 0 ouvert + 11 tranchés (`av-pb-notes-probabilites-a-priori`, `av-variables-muettes`, `av-quiz-seuil-ook`, `av-quiz-pire-probabilite`, `av-facteur-calcul-pb`, `av-definition-q-notes`, `av-variance-bruit-filtre`, `av-filtre-adapte-causal`, `av-densite-conditionnelle-td`, `av-dsp-bruit-filtre-td`, `av-variance-bruit-discret-td`) |
| 5 | Transmission sur fréquence porteuse | — | brouillon | — |
| 6 | Modulation et démodulation numériques | — | brouillon | — (à la rédaction : renvoi vers l'efficacité spectrale du chapitre 2) |

Remarque : « brouillon » signifie ici « sources officielles reçues, rien de rédigé ». Les notes reçues couvrent aussi une partie des chapitres 3 et 4 (voir section 10 du rapport du chapitre 2). L'enseignant n'a pas suivi l'ordre du poly (bruit avant DSP) ; **décision du 7 octobre 2026 : on garde l'ordre du poly**, et la fiche matière le signale.

### EANA3 — Circuits intégrés

| N° | Chapitre (plan du support 2025) | Fichier prévu | Statut | Notes rattachées |
|---|---|---|---|---|
| 1 | Rappels et généralités sur la contre-réaction | `cours/01-generalites-contre-reaction.qmd` | **flashcards** (32 cartes ; 5 AV tranchés, 2 retirés en complément) | `notes-2023` c. 01-02 ; `tableau-2020` c. 01, 02, 03 p. 1-3 |
| 2 | Amplificateurs en contre-réaction | `cours/02-amplificateurs-contre-reaction.qmd` | **flashcards** (23 cartes ; 0 AV) | `notes-2023` c. 04-06 ; `tableau-2020` c. 03 p. 4-6, 04 |
| 3 | Applications de la théorie de la contre-réaction | `cours/03-applications-contre-reaction.qmd` | **flashcards** (25 cartes ; 2 AV tranchés) | `notes-2023` c. 08, 11 (dégénérescence inductive : aucune note) |
| 4 | Oscillateurs | `cours/04-oscillateurs.qmd` | **flashcards** (38 cartes ; 4 AV tranchés) | `notes-2023` c. 03-05, 07, 09 (classes A/B/C : aucune note) |
| 5 | Références de tension | `cours/05-references-de-tension.qmd` | **flashcards** (32 cartes ; 2 AV tranchés) | `notes-2023` c. 10 (bandgap fractionnaire : aucune note) |

« brouillon » : sources reçues, rien de rédigé. Le support 2025 ne contient pas de cours rédigé (plan + exercices + TD). Détail : `matieres/eana3-circuits-integres/analyses/inventaire-sources.md`.

### EARF1 — Modulations analogiques et numériques

| N° | Chapitre | Fichier | Statut | Blocs *À vérifier* |
|---|---|---|---|---|
| 1 | Introduction : signaux et outils d'analyse | `cours/01-introduction-signaux-outils.qmd` | **flashcards** (17 cartes) | 0 ouvert + 2 tranchés (`av-tf-pulsation-frequence`, `av-indices-fourier`) |
| 2 | Modulations linéaires | `cours/02-modulations-lineaires.qmd` | **flashcards** (18 cartes) | 0 ouvert + 3 tranchés (`av-condition-surmodulation`, `av-bornes-spectre-dbap`, `av-niveau-05-td3`) |
| 3 | Modulations angulaires | `cours/03-modulations-angulaires.qmd` | **flashcards** (21 cartes) | 0 ouvert + 3 tranchés (`av-signe-serie-bessel`, `av-symetrie-bessel`, `av-derivee-fm-facteur-2pi`) |
| 4 | Introduction aux modulations numériques | `cours/04-modulations-numeriques.qmd` | **flashcards** (18 cartes) | 0 ouvert + 3 tranchés (`av-unite-symbol-rate`, `av-dphi-16qam`, `av-lobe-msk`) |

Validation déléguée par Armand le 29 octobre 2026 : à relire quand il le souhaite (les blocs tranchés et les *Compléments* sont les passages à regarder en priorité).

### Matières du S7 mises en place le 19 octobre 2026

Aucun chapitre rédigé : statut `brouillon` pour tous les chapitres proposés. Détail dans chaque fiche matière et dans `analyses/inventaire-sources.md`.

| Matière | Plan | Remarque |
|---|---|---|
| AUTO1 — Commande des systèmes linéaires | 6 chapitres proposés | note de cours Melchior (v03 de référence) |
| AUTO2 — TP d'automatique | TP | 2 polys de TP |
| AUTO3 — Optimisation | 4 chapitres proposés | support en anglais (R. Malti) |
| EAEP1 — Conversion d'énergie 1 | 7 chapitres proposés | support 2026 (J.-M. Vinassa) |
| EANA1 — Composants et circuits de commutation | à établir | **aucun support officiel** |
| EANA2 — Chaîne d'acquisition | 5 chapitres proposés | CAN (F. Rivet) + bruit (T. Taris) |
| EANA4 — TP d'électronique | TP | poly 2026, TP 1 à 5 |
| EARF1 — Modulations | **4 chapitres, 74 flashcards** (29 octobre 2026) | T. Taris ; voir le tableau ci-dessus |
| NUMC1 — Technologie des circuits numériques | 6 chapitres proposés | S. Renaud, B. Le Gal ; TD VHDL |
| NUME3 — Conception VHDL/FPGA | projet | lecteur MP3 |
| NUMR1 — Réseaux et Internet | à établir | 368 p. de diapositives ; paquet hérité `reseaux.json` |
| PROJ1 — Projet analogique | projet | 7 sujets, ressources du groupe D |
| TSIG1 — Traitement numérique du signal | **5 chapitres `verifie`** (20 octobre 2026) | plan des notes d'Armand ; 30 AV ouverts (1/4/9/11/5) ; détail dans la fiche matière |
| TSIG2 — TP signal | TP | poly 2026-2027 |

### Sources disponibles (TS227)

| Source | Nature | Dans `sources/` ? |
|---|---|---|
| `poly_ts227.pdf` (9 oct. 2025, 180 p.) | officielle | oui, `support/` |
| `TD_TS_227.pdf` (2020/2021, 4 p.) | officielle | oui, `support/` |
| `correction_TD_TS_227.pdf` (15 p.) | officielle | oui, `support/` — suit une **autre version de l'énoncé** (numérotation des questions différente, ex. 2 à 5) |
| Notes manuscrites (5 feuillets recto-verso, 10 photos) | personnelle | oui, `notes/date-inconnue.pdf` + `notes/date-inconnue/` (dates inconnues, définitivement) |

---

## 6. Décisions récentes

| Date | Décision | Où |
|---|---|---|
| 2026-10-29 | EARF1 : plan en 4 chapitres validé ; Armand **délègue la validation** (« toutes les étapes jusqu'à valide ») : 11 blocs *À vérifier* tranchés par Claude (propositions retenues, ligne **Décision** « déléguée par Armand ») ; flashcards non demandées | rapports EARF1 ; fiche matière |
| 2026-10-28 | Refonte complète de l'interface (brief d'Armand) : DA « Bristol 2026 » à la place de « fiche bristol » ; accueil, page Annales et en-têtes générés depuis les fichiers (`scripts/catalogue.ts`) ; navigation Matières / Annales / Révisions ; fichiers générés `_generes/` et `assets/catalogue.json` versionnés — **choix par défaut, à valider** ; classe `.attention` proposée, non utilisée | `conventions.md` § 6, § 13 ; `architecture.md` § 4 |
| 2026-10-25 | Site publié sur GitHub Pages en **accès public** (https://armandgm43-droid.github.io/bristol-site/), construit par GitHub Actions — **choix d'Armand**, remplace provisoirement « accès réservé + accord des enseignants » | `CONTEXTE_PROJET.md` § 5.4, règle 19.5, journal ; `architecture.md` § 10 |
| 2026-10-20 | Annales : énoncé en images découpées par question, solution dessous ; sujets du recueil de TD traités comme annales — **choix d'Armand** ; doublons scan/recueil : images tirées du recueil (plus net), deux sources citées — choix par défaut | `conventions.md` § 2 ; fiche TSIG1 |
| 2026-10-20 | TSIG1 : plan des notes d'Armand (5 chapitres) à la place du plan des notes 2023 ; méthode « deux temps » (rédaction + vérification le 20 oct., cartes définitives après la relecture d'Armand) — **choix d'Armand** ; notes d'Armand non datées rangées en `date-inconnue/feuillet-NN-recto|verso.jpg`, citées par feuillet — choix par défaut | fiche TSIG1 ; rapports `analyses/0N-*.md` |
| 2026-10-19 | Refonte de la DA : esprit fiche gardé mais allégé, application incluse, *Source Sans 3* à la place d'*Atkinson Hyperlegible* — **choix d'Armand** ; détail de la mise en page (accueil en cartes, trait rouge court, statuts en pastilles, libellés « À venir ») — choix par défaut | `conventions.md` § 4, § 13 |
| 2026-10-19 | Archive 2A : périmètre « ranger + fiches + plans » ; dossier « S7 » d'un ancien élève intégré en `externe` (préfixe `2023-`) ; travaux personnels dans `sources/<code>/travaux/` (jamais publiés) ; TS205 (OFDM) rattaché à TS227 — **choix d'Armand** | inventaires des matières ; `conventions.md` § 2 |
| 2026-10-19 | Annales « Initiation aux bruits » (EA222) rattachées à EANA2 ; TD VHDL rangés une fois, dans NUMC1 ; versions antérieures des supports gardées avec le suffixe `-ancienne-version` — **choix par défaut, à confirmer** | inventaires EANA2, NUMC1 |
| 2026-10-07 | EANA3 : code `eana3` (ancien EA234), enseignants F. Rivet et Y. Deval ; plan en 5 chapitres (un par chapitre du support, numérotés à la suite) ; nommage des sources et jeux de notes non datés (`<année>-cours-NN-…`) ; sujets distribués comme TD rangés dans `td/` — **choix par défaut, à revoir par Armand** | inventaire EANA3, § 4 et § 7 |
| 2026-10-07 | EANA3, Q1 : notes `notes-2023` et `tableau-2020` = sources `externe` (pas les notes d'Armand) ; blocs `.notes` avec citation de la source, sans nouvelle classe (choix par défaut, à confirmer) | inventaire EANA3, § 8 ; fiche matière |
| 2026-10-07 | `scripts/flashcards.py` : paquet vide pour une matière sans carte | `architecture.md` § 6 |
| 2026-10-07 | TS227 ch. 1 et 4 vérifiés (aucun point bloquant) et validés ; 12 + 57 flashcards | rapports ch. 1 et ch. 4, § 17-18 |
| 2026-10-07 | TS227 ch. 1 et 4 : 13 propositions des rapports retenues (choix laissé à Claude), blocs tranchés ; notamment filtre adapté causal $h^*(T_h - t)$ (p. 130) et « pire » $P_b$ = 0,5 (p. 111) | rapports ch. 1 et ch. 4, § 16 |
| 2026-10-07 | Correction : l'export de l'application ne contient que les cartes ; transfert de progression impossible tant que la tâche « export/import de la progression » n'est pas faite | `architecture.md` § 6 ; § 7 ci-dessous ; `TODO.md` |
| 2026-10-07 | TS227 ch. 3 validé ; `av-dsp-porte-notes` tranché : résultats de la correction du TD ($\sigma_a^2\Ts\sinc^2(f\Ts)$, sommet $\sigma_a^2\Ts$) ; 56 flashcards | rapport ch. 3, § 18 |
| 2026-10-07 | TS227 : $\sinc(x) = \sin(\pi x)/(\pi x)$ ; convention d'autocorrélation du poly ($t - \tau$, $n - m$) retenue partout, y compris pour le TD | fiche matière ; rapport ch. 3, § 16 |
| 2026-10-07 | TS227 ch. 3 : variance affine $a^2\sigma^2$ (poly p. 78 corrigé) ; 67 %/99 % gardés comme arrondis ; $N_0B$ des notes = aire de la bande positive | rapport ch. 3, § 16 |
| 2026-10-07 | Question 5 tranchée : paquet TS227 provisoire (`ts-…`) abandonné, nouvelles clés `ts227-<slug>` ; `ts227.json` généré par script | `CONTEXTE_PROJET.md` § 18.5, § 22, journal |
| 2026-10-07 | Ancien site de cartes (dépôt `bristol`) figé ; révision en local, `quarto preview` sur le port fixe 4848 | `CONTEXTE_PROJET.md` § 20.2 ; `architecture.md` § 6, § 10 ; `_quarto.yml` |
| 2026-10-07 | Flashcards : macros écrites comme dans le cours (développées par le script), sauts de ligne façon Markdown | `conventions.md` § 10.4, § 10.5 |
| 2026-10-07 | TS227 ch. 2 : V5 trié, `eq-signal-yl` et `eq-efficacite-spectrale` retirés (non cités, visés par aucune carte) | rapport ch. 2, 13.12 |
| 2026-10-07 | Site publié à la fin pour les étudiants de la promo ; conditions : accès réservé (liste d'e-mails, ex. Cloudflare Access) et accord des enseignants ; en attendant, local uniquement | `CONTEXTE_PROJET.md` § 1, § 5.4, règle 19.5, journal |
| 2026-10-07 | Pages publiées : aucun contenu personnel ou sans rapport avec le cours | `CONTEXTE_PROJET.md` § 5.4, règle 19.5 |
| 2026-10-07 | Avant publication : page « À propos » (quatre catégories, origine des notes) et export/import de la progression | `CONTEXTE_PROJET.md` § 5.4 ; `TODO.md` |
| 2026-10-07 | Choix de forme, de figures et de rédaction appliqués par défaut par Claude et listés dans le rapport ; questions réservées aux points bloquants | `conventions.md` §14 |
| 2026-10-07 | TS227 ch. 2 validé (V1-V6 tranchés) | rapport ch. 2, 13.11 |
| 2026-10-07 | Une seule DA (« fiche bristol ») pour le site et l'application ; jetons dans `assets/bristol-tokens.css` ; mode sombre : feuilles sombres, fiches de révision et figures sur papier clair ; préférence clair/sombre partagée | `conventions.md` §13, `architecture.md` §4 |
| 2026-10-07 | TS227 : ordre des chapitres du poly conservé (3 = DSP, 4 = bruit), ordre réel du cours signalé dans la fiche matière | fiche matière |
| 2026-10-07 | TS227 : convention de la TF $e^{-j2\pi ft}$ ; p. 40 du poly = coquille (bloc tranché) | fiche matière ; rapport ch. 2, 13.3 |
| 2026-10-07 | TS227 ch. 2 : centre de symétrie $(1/(2\Ts), g_0\Ts/2)$, correction du poly p. 41 (bloc tranché) | rapport ch. 2, 13.3 |
| 2026-10-07 | TS227 ch. 2 : efficacité spectrale dans le chapitre 2, renvoi depuis le chapitre 6 | rapport ch. 2, 13.2 |
| 2026-10-07 | Blocs *À vérifier* tranchés visibles (`.tranche` + **Décision**) quand la source est corrigée | `conventions.md` §5.2 |
| 2026-10-07 | Fautes d'orthographe sans effet sur le sens corrigées sans bloc, listées dans le rapport | `conventions.md` §5.3 |
| 2026-10-07 | TS227 ch. 2 : `av-echelles-figure-cosinus-sureleve` tranché (axes normalisés dans F11) ; choix de rédaction de l'étape 4 validés | rapport ch. 2, 13.9 |
| 2026-10-07 | Pages citées = pages du PDF ; notes sans date = `date-inconnue.pdf` ; rapports dans `analyses/` | `conventions.md` §2, §3.1 |
| 2026-10-06 | Classes des catégories figées : `.notes`, `.complement`, `.a-verifier` | `conventions.md` §5 (question ouverte 3) |
| 2026-10-06 | Rendu HTML des catégories validé tel qu'il est dans `bristol.scss` ; rendu PDF reporté | `architecture.md` §4 (question ouverte 3) |
| 2026-10-06 | Flashcards en YAML, un fichier par chapitre ; identifiants `<matiere>-<slug>`, uniques dans la matière, sans numéro de chapitre | `conventions.md` §10 (question ouverte 4) |
| 2026-10-06 | Blocs *À vérifier* identifiés par `#av-slug` | `conventions.md` §5.2 |
| 2026-10-06 | Statuts en minuscules sans accents dans le front matter | `conventions.md` §4 |
| 2026-10-06 | Labels uniques dans la matière, sans numéro | `conventions.md` §7 |
| 2026-10-06 | Macros dans `_macros.qmd` (le contexte disait `_macros.tex`) | `conventions.md` §8 |
| 2026-10-06 | Règle provisoire : site utilisé en local uniquement tant que l'hébergement n'est pas décidé | `architecture.md` §10 (question ouverte 1) |
| 2026-10-06 | Règle provisoire : paquets hérités conservés tels quels, préfixes réservés | `conventions.md` §10.3 (question ouverte 6) |
| 2026-10-06 | `prp-title: "Propriété"` ajouté dans `_quarto.yml` | `_quarto.yml` |

Toutes ces décisions ont été **validées par Armand** le 6 octobre 2026 et reportées dans le journal des décisions de `CONTEXTE_PROJET.md`.

---

## 7. Problèmes connus et incohérences

1. ~~Le dossier n'est pas un dépôt Git~~ : réglé (commit `501e006`).
2. ~~TD et correction absents de `sources/`~~ : réglé.
12. ~~Nouveau point *À vérifier* au chapitre 2 (`av-echelles-figure-cosinus-sureleve`)~~ : tranché le 7 octobre 2026 (axes normalisés).
9. ~~Rendu des blocs tranchés~~ : stylé le 7 octobre 2026 dans `assets/bristol.scss` (jetons `--cat-verifier…`, clair et sombre), exemple dans `demo-conventions.qmd`. Rendu à contrôler avec `quarto preview`.
16. **Deux dépôts GitHub à ne pas confondre** : `armandgm43-droid/bristol-site` (**public** depuis le 27 octobre 2026, site publié sur https://armandgm43-droid.github.io/bristol-site/) est le dépôt du projet ; `armandgm43-droid/bristol` est l'ancien site de cartes, toujours en ligne avec GitHub Pages mais **figé** depuis le 7 octobre 2026 (voir `architecture.md` § 10).
13. ~~**Application de révision liée au site**~~ : sans objet depuis que l'ancien site est figé (plus de copie isolée de `revision/`). Rappel : `revision/index.html` charge `../assets/bristol-tokens.css` ; à garder en tête si l'application est un jour copiée ailleurs.
17. **Progression de révision locale** : liée à `http://localhost:4848` et au navigateur. Changer de port, passer par `127.0.0.1` ou changer de navigateur repart de zéro. La progression de l'ancien site GitHub Pages ne se transfère pas non plus. **L'export actuel de l'application exporte les cartes, pas la progression** : aucun transfert n'est possible tant que la tâche « export/import de la progression » de `TODO.md`, section « Avant la publication » n'est pas faite (corrigé le 7 octobre 2026).
18. **Rendu des cartes non contrôlé dans le navigateur** : les formules du paquet TS227 (186 cartes ; 313 pour les ch. 1 et 4) compilent sans erreur avec MathJax 3.2.2 (contrôle de Claude), mais l'affichage réel dans l'application reste à vérifier avec `quarto preview`.
14. **Liens de la barre de navigation écrits deux fois** : `website.navbar` de `_quarto.yml` et en-tête de `revision/index.html`, à garder alignés.
15. **MathJax** : le site (Quarto 1.10) charge MathJax 4, l'application MathJax 3.2.2 ; même syntaxe LaTeX courante. `CONTEXTE_PROJET.md` § 5.5 et § 20.1 mis à jour le 7 octobre 2026. Une formule qui s'affiche différemment dans les deux reste possible : à signaler si elle apparaît.
10. ~~Dossier vide `sources/ts227/notes/a-dater/`~~ : supprimé par Armand.
11. **Énoncé et correction du TD de versions différentes** : numéros de questions à préciser en phase 2.
8. **Notes non datées** : dates inconnues, définitivement ; convention `date-inconnue.pdf` adoptée.
3. ~~Version de Quarto inconnue~~ : 1.10.19, notée dans `architecture.md` § 9.
4. **Rendu PDF des quatre catégories** non implémenté.
5. **Progression des révisions liée à l'adresse du site** (`localStorage`) : déplacer l'application vers un autre hébergement fera repartir de zéro (l'export actuel ne contient que les cartes, pas la progression). À prendre en compte avant de choisir l'hébergement. **Export et import de la progression à faire avant la publication** (décision du 7 octobre 2026, `TODO.md`).
6. **MathJax chargé depuis Internet** (jsDelivr) : sans connexion, pas de formules. Les polices sont auto-hébergées depuis le 28 octobre 2026.
7. ~~**Paquet `ts227.json` hérité**~~ : réglé (question 5) ; le fichier est désormais généré par `scripts/flashcards.py`, les cartes `ts-…` disparaissent à la prochaine ouverture de l'application.

---

19. **EANA3 : notes externes uniquement** (`notes-2023`, `tableau-2020`, auteurs inconnus, cours de 2020 et 2023) : nature `externe` (Q1 tranchée le 7 octobre 2026). Le cours a pu changer depuis : écarts en *À vérifier*. Les chapitres rédigés avant l'arrivée des notes d'Armand devront être repris (§ 17 du contexte).
20. **EANA3 : énoncés absents** pour trois corrigés manuscrits (TD1 « amplificateur à contre-réaction » et TD2 « mode commun » de 2023, annale 2017-2018) ; **sections sans notes** : dégénérescence inductive, classes A/B/C, bandgap fractionnaire.
21. **Rendu Quarto non contrôlé** après l'ajout d'EANA3 (Quarto absent de l'environnement de Claude) : vérifier la barre latérale et la fiche matière avec `quarto preview`.

22. **Archive 2A** : `sources/2A.zip` (870 Mo) est encore présent ; son contenu utile est redistribué, Armand peut le supprimer. Non repris : doublons, fichiers personnels (Eirspace, inscription, stages, Ingénib, anglais), fichiers de compilation et exécutables, module « Intégrer l'entreprise ».
23. ~~Rendu Quarto non contrôlé après l'ajout des 14 matières~~ : contrôlé le 19 octobre 2026 (Quarto 1.10.19 installé par Claude dans sa machine de travail, copie du projet sans `sources/`) : 27 pages, aucun avertissement ; captures de l'accueil et des fiches en clair, en sombre et sur mobile. Corrigé au passage : le code en ligne (`td code`, `li code`, `p code`) restait sur fond gris clair en mode sombre (règle de Bootstrap plus spécifique), `assets/bristol.scss` ; codes des matières insécables dans l'accueil. Non vérifiables dans cet environnement : polices et formules (Google Fonts et MathJax bloqués par le réseau de Claude).
24. **Sources manquantes** : EANA1 (aucun support officiel), TSIG1 (pas de support de cours rédigé ; cours reconstruit à partir des notes d'Armand), conditionnement analogique en EANA2 (objectif annoncé, aucun support).

25. **Annales sans entrée de barre latérale** (constaté le 28 octobre 2026) : `matieres/auto1-…/annales/` (7 pages) et `matieres/ts227-…/annales/` (5 pages) existent et sont publiées, mais ne figurent pas dans les barres latérales de `_quarto.yml`. L'accueil et la page Annales les listent déjà (catalogue généré).
26. **Rendu sur le PC non contrôlé après la refonte** : à faire par Armand avec `quarto preview` (le catalogue est régénéré au lancement) ; si Quarto signale une erreur sur `scripts/catalogue.ts`, me la transmettre.

## 8. Questions ouvertes (suivi de `CONTEXTE_PROJET.md`, section 22)

| N° | Question | État |
|---|---|---|
| 1 | Hébergement du site de cours | Ouverte, **orientée** (2026-10-07) : publication pour la promo, accès réservé par liste d'e-mails (ex. Cloudflare Access) + accord des enseignants. En attendant : local uniquement |
| 2 | Un ou deux dépôts | Ouverte |
| 3 | Classes et rendu des quatre catégories | **Tranchée** : classes figées, rendu HTML actuel ; PDF à faire |
| 4 | Format des flashcards et des identifiants | **Tranchée** : YAML, `<matiere>-<slug>` |
| 5 | Reprise des clés `ts-…` du paquet provisoire | **Tranchée** : paquet abandonné, nouvelles clés `ts227-<slug>` |
| 6 | Migration des paquets hérités | Ouverte. Règle provisoire : conservés tels quels |
| 7 | Premier chapitre de test de TS227 | **Tranchée** : chapitre 2 |
| 8 | Synchronisation de la progression entre appareils | Ouverte |
| 9 | Découpage des chapitres 3 et 4 de TS227 (ordre du cours ≠ ordre du poly) | **Tranchée** : ordre du poly |
| 10 | Numérotation des pages citées : PDF ou diapositive | **Tranchée** : pages du PDF |
| 11 | Emplacement des rapports d'analyse | **Tranchée** : `matieres/<matiere>/analyses/NN-slug.md` |
| 12 | Fautes d'orthographe des sources corrigées sans bloc *À vérifier* | **Tranchée** : oui, listées dans le rapport |
| 13 | Signalement d'erreurs et propositions de notes par les camarades | Ouverte (plus tard) |

---

## 9. Journal des sessions

| Date | Session | Résultat |
|---|---|---|
| 2026-10-06 | Sessions précédentes | `CONTEXTE_PROJET.md` rédigé ; squelette Quarto créé |
| 2026-10-06 | Bristol — Fichiers de mémoire | `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` créés ; choix validés (identifiants de cartes sans numéro de chapitre) ; `CONTEXTE_PROJET.md` et `_quarto.yml` mis à jour ; fichiers de mémoire copiés dans le projet claude.ai |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Analyse | Chapitre 2 choisi ; notes rangées dans `sources/ts227/notes/a-dater/` ; rapport d'analyse produit (7 points *À vérifier*, 16 questions) ; statut du chapitre 2 : `analyse` |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Différences | 16 questions tranchées ; notes rangées (`date-inconnue`) ; TD et correction inventoriés ; rapport (section 13), `conventions.md`, fiche matière, `ETAT_PROJET.md`, `TODO.md` et `CONTEXTE_PROJET.md` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Rédaction | `cours/02-communication-sans-bruit.qmd` rédigé (texte, sans figures) ; ajouté à `_quarto.yml` et à la fiche matière ; nouveau bloc ouvert `av-echelles-figure-cosinus-sureleve` ; 3 corrections orthographiques ajoutées au rapport (13.5) ; rapport complété (13.8) |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Figures | AV9 tranché ; 12 figures (11 matplotlib, 1 TikZ) dans `figures/`, intégrées au chapitre ; statut `redige` ; rapport (13.9), fiche matière, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` mis à jour |
| 2026-10-07 | Bristol — Interface | DA unifiée site + application validée sur captures ; `assets/bristol-tokens.css` et `assets/bristol-sombre.scss` créés ; `bristol.scss`, `_quarto.yml`, `revision/index.html` (CSS et barre de navigation, JavaScript de l'application inchangé) modifiés ; `conventions.md` §13 et `architecture.md` §4 rédigés |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Vérification | Style des blocs tranchés (`✓ Corrigé`, jetons, clair et sombre) + exemple dans `demo-conventions.qmd` ; `CONTEXTE_PROJET.md` § 5.5 (MathJax 4 / 3.2.2) ; dépôts GitHub notés dans `architecture.md` § 10 ; vérification complète du chapitre 2 (rapport, section 13.10) : 6 points à trancher (V1 : facteur de retombée estimé ≈ 0,35 et non 0,2) |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Vérification (suite) | V1-V6 tranchés et appliqués (β ≈ 0,35, F10 et F11 régénérées ; F12 refaite en spectre rectangulaire ; bloc AV8 levé ; Ш en notes) ; chapitre **validé** ; nouvelle règle `conventions.md` § 14 (choix par défaut, questions bloquantes seulement) |
| 2026-10-07 | Bristol — Publication pour la promo | Décision : site publié pour la promo (accès réservé + accord des enseignants) ; `CONTEXTE_PROJET.md` (§ 1, § 5.4, règle 19.5, journal, questions 1 et 13, « État actuel »), `ETAT_PROJET.md` et `TODO.md` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Flashcards | Question 5 tranchée ; 61 cartes (`flashcards/02-communication-sans-bruit.yml`) ; V5 trié ; `scripts/flashcards.py` écrit et lancé (`ts227.json` régénéré) ; port de `quarto preview` fixé à 4848 ; ancien site figé ; statut `flashcards` ; `CONTEXTE_PROJET.md`, `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md`, rapport (13.12), fiche matière mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Rédaction | Conseil erroné d'export de la progression corrigé (`architecture.md`, `ETAT_PROJET.md`, `TODO.md`) ; chapitre 3 : analyse, rédaction, 5 figures, TD ex. 2 et ex. 5 q. 10-11 intégrés ; 8 blocs ouverts + 1 tranché ; statut `redige` ; rapport, fiche matière, `_quarto.yml` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Rédaction (suite) | Réponses d'Armand aux 8 questions appliquées : 2 tranchés, 4 levés, 3 ouverts ; fiche matière, rapport (§ 16) mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Rédaction (fin) | Blocs `av-esperance-exercice-bpsk` et `av-moment-ordre-2-notes` tranchés (choix laissé à Claude) ; reste 1 bloc ouvert |
| 2026-10-07 | Bristol — TS227 Chapitres 1 et 4 — Rédaction | Étapes 2 à 5 des chapitres 4 puis 1 : rapports d'analyse, 2 chapitres (statut `redige`), 8 figures, TD ex. 3, 4, 5 q. 12-13 intégrés ; 13 questions bloquantes, tranchées (choix laissé à Claude) : 13 blocs tranchés ; `_quarto.yml`, fiche matière, `ETAT_PROJET.md`, `TODO.md` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Vérification et flashcards | Vérification (rapport § 17, 6 corrections de forme, aucune erreur de fond) ; `av-dsp-porte-notes` tranché (TD) ; chapitre validé ; 56 cartes (`flashcards/03-dsp-signaux-codes-en-ligne.yml`) ; `flashcards.py` lancé (117 cartes TS227) ; statut `flashcards` ; rapport (§ 17-18), fiche matière, `ETAT_PROJET.md`, `TODO.md`, `CONTEXTE_PROJET.md` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitres 1 et 4 — Vérification et flashcards | Vérification (rapports § 17 : poly, notes relues sur photos, TD et correction, 803 formules, figures ; 7 corrections de forme, aucun point bloquant) ; chapitres validés ; 12 + 57 cartes ; `flashcards.py` lancé (186 cartes TS227) ; statut `flashcards` ; rapports (§ 17-18), fiche matière, `ETAT_PROJET.md`, `TODO.md`, `CONTEXTE_PROJET.md` mis à jour |
| 2026-10-07 | Bristol — Circuits intégrés — Mise en place | Matière EANA3 : code et enseignants trouvés dans le support ; 37 PDF triés et renommés (`sources/eana3/`) ; arborescence, fiche matière, `_quarto.yml`, accueil, paquet vide ; inventaire et plan en 5 chapitres (`analyses/inventaire-sources.md`) ; 1 question bloquante (origine des notes) |
| 2026-10-08 | Bristol — Circuits intégrés — Chapitres 1 à 5 | Catégorie `.notes-externes` (conventions § 5, `bristol.scss`, jetons clair/sombre, démo) ; nommage des jeux de notes non datés (conventions § 2) ; 72 pages manuscrites transcrites ; **ch. 1 rédigé** (rapport, qmd, 7 figures, exercice guidé) ; **ch. 2 rédigé** (rapport, qmd, 6 figures, TD 1) ; **ch. 3 rédigé** (exercices guidés, 4 TD, 6 figures) ; **ch. 4 rédigé** (cours d'après notes externes, 4 TD, 9 figures, 4 AV) ; **ch. 5 rédigé** (3 exercices, 9 figures, 2 AV) |
| 2026-10-18 | Bristol — Arborescence du S7 | 14 matières du S7 ajoutées (codes officiels sans le préfixe EEL7) : `matieres/<code>-<intitule>/` (analyses, annales, corriges, cours, figures, flashcards, td, tp, avec `.gitkeep`) et `sources/<code>/` (support, notes, td, annales, corriges) pour eana1, eaep1, eana4, earf1, eana2, proj1, nume3, numc1, numr1, auto1, auto2, auto3, tsig1, tsig2. TS227 reste distinct d'EARF1 (confirmé par Armand). Pas encore de fiche matière, d'entrée `_quarto.yml` ni de paquet de cartes pour ces matières |
| 2026-10-18 | Bristol — Annales 2A élec | 60 fichiers de l'archive « Annales 2A élec » rangés et renommés (`AAAA-AAAA-partiel[-precision][-pN].ext`) dans `sources/<code>/annales/` : tsig1 (8 + fiche de rappels externe dans `notes/`), eana3 (12 : sujet 2025-2026, anciens partiels EA211 Contre-réaction dont corrigé 2015-2016, EA210 Circuits HF et oscillateurs), eana1 (6), eaep1 (4, dossier « Gestion de l'énergie 2 » = EA207), auto1 (7 : AU201 commande linéaire, AU205 temps discret), auto3 (5), numc1 (6 : EN208 TCIN, examen CI/VHDL 2025-2026), nume3 (1), tsig2 (3, TS202), ts227 (7). Non repris : modules de S8 ou hors filière (CEM, comm. num. avancées, filtrage et estimation, microprocesseurs, PLL, espace d'état, systèmes non linéaires, traitement d'image, C++, droit du travail, gestion financière), initiation aux bruits (EA222, rattachement inconnu), doublons et fichiers Zone.Identifier |
| 2026-10-18 | Bristol — Circuits intégrés — Validation et flashcards (reprise) | Le travail du 14 octobre n'avait pas atteint le PC : refait. 15 blocs AV traités selon les décisions du 14 octobre (`av-sensibilite-beta-signe` en valeur absolue, tranché par Armand ; 12 autres tranchés, propositions retenues ; `av-marge-phase-70` et `av-enonce-separation-poles` retirés et réintégrés en complément) ; 0 bloc ouvert ; 5 chapitres au statut `flashcards` ; **150 cartes** (32 + 23 + 25 + 38 + 32 ; ch. 2 centré sur les impédances par type de contre-réaction) ; 778 formules compilées sans erreur (MathJax 3.2.2) ; `scripts/flashcards.py` ignore désormais les matières sans `index.qmd` ; `eana3.json` écrit ; fiche matière mise à jour. À faire par Armand : contrôle avec `quarto preview` |
| 2026-10-19 | Bristol — Archive 2A | `sources/2A.zip` redistribué : 413 fichiers rangés et renommés dans `sources/<code>/` (dont `tp/`, `tp/fichiers/`, `travaux/`), copies vérifiées par MD5, doublons et fichiers personnels écartés ; 14 fiches matières et inventaires (avec plans proposés et correspondance des noms d'origine) ; `_quarto.yml`, accueil par UE, 14 paquets vides ; fiches TS227 et EANA3 complétées ; `conventions.md` § 2 ; `TODO.md`. Session interrompue par une coupure de connexion avec le PC, reprise ensuite |
| 2026-10-19 | Bristol — Contrôle du rendu | Quarto 1.10.19 installé par Claude (hors du dossier du projet) ; rendu complet du site sans avertissement ; correction du code en ligne en mode sombre (`assets/bristol.scss`) ; codes insécables dans l'accueil |
| 2026-10-19 | Bristol — Refonte du site | Diagnostic sur captures (« en travaux » : statuts internes sur l'accueil, filets partout, majuscules, gras, feuille ombrée) ; 3 choix d'Armand ; jetons et thème refaits, accueil en cartes, CSS de l'application allégé, statuts en pastilles ; rendu contrôlé (Quarto 1.10.19, polices et MathJax servis localement pour les captures) ; `conventions.md` § 4, § 13, `architecture.md` § 4. |
| 2026-10-19 | Bristol — TSIG1 — Préparation du partiel | Partiel le **jeudi 22 octobre 2026** (Armand). 6 annales lues : `analyses/annales-partiel.md` (thèmes et fréquences) ; `notes-2023` ch. 1 à 5 lues ; annales 2025-2026 et 2017-2018 corrigées (`annales/*.qmd`, solutions en *Complément*, 1 figure) ; **paquet provisoire** `revision/cartes/tsig1-partiel.json` (52 cartes, préfixe `tsig1p-`, accord d'Armand pour déroger à la règle « cartes après validation » à cause du partiel) ; fiche matière, barre latérale, accueil mis à jour. À faire : corrigé 2022-2023, chapitres (en attente des notes d'Armand), retrait du paquet provisoire après les cartes définitives |
| 2026-10-20 | Bristol — TSIG1 — Chapitres 1 à 5 | Photos des notes d'Armand rangées (`date-inconnue/`, PDF) et transcrites ; plan des notes retenu ; 5 chapitres rédigés (`cours/01` à `05`), 11 figures, 5 rapports d'analyse ; notes 2023, illustrations, recueil de TD et corrigés 2023 intégrés (16 exercices) ; vérification (étape 6, `analyses/verification-chapitres-2026-10-20.md`) ; statut `verifie` ; 30 AV ouverts ; fiche matière (plan, notations, conventions, sources), barre latérale, accueil. Session coupée ~3 h par une perte de connexion avec le PC |
| 2026-10-20 | Bristol — TSIG1 — Annales en images | 9 annales (dont 3 sujets du recueil de TD : mars 2014, mars 2018, décembre 2019) ; sujets découpés en images par question, solution sous chaque question ; pages 2017-2018 et 2025-2026 converties (labels conservés) ; 7 pages nouvelles ; `_quarto.yml`, fiche matière, accueil ; `conventions.md` § 2 (format des annales) |
| 2026-10-21 | Bristol — TSIG1 — Fiche de révision | `matieres/tsig1-traitement-numerique-signal/fiches/fiche-tf-tz-echantillonnage.qmd` (demande d'Armand, veille du partiel) : trois représentations et passages, échantillonnage et repliement, paires et propriétés TF/TZ, méthode $H(z) \to h[n]$, TFD, retards et phase ; texte non marqué = résumé du cours avec lien vers le passage d'origine, hors-cours en *Complément* ; paires et propriétés vérifiées numériquement, 250 formules compilées (MathJax 3.2.2) ; ajoutée à `_quarto.yml` (section « Fiches de révision ») et à la fiche matière. **Choix par défaut à valider** : dossier `fiches/` et convention « résumé du cours non marqué + lien » pour les fiches de synthèse (à reporter dans `conventions.md` si validé). Rendu Quarto non contrôlé (Quarto absent) |
| 2026-10-22 | Bristol — EANA3 — Annale résistance négative | Partiel EA210 « Circuits HF et oscillateurs » 2016-2017, **exercice II** (charge active à paire croisée PMOS, $Z = 2/(g_{m3}-g_{m2})$, $A_v = -g_{m1}/(g_{m3}-g_{m2})$) corrigé : `annales/2016-2017-partiel-circuits-hf.qmd` (solutions en *Complément*, énoncé en images par question, script `sujets/2016-2017-partiel-circuits-hf-decoupe.py`) ; correspondance avec la Partie I du partiel 2013-2014 (même exercice) ; `_quarto.yml` (section « Annales corrigées » d'EANA3), fiche matière. Exercice I non corrigé. Rendu Quarto non contrôlé |
| 2026-10-19 | Bristol — Paquets de langues | Deux paquets hors méthode des cours (comme les paquets hérités) : `revision/cartes/italien.json` (432 cartes, niveau B1 : conjugaison de tous les temps, subjonctif, impératif, vocabulaire dans les deux sens, faux amis) et `russe.json` (229 cartes, débutant : alphabet, prononciation, bases, vocabulaire dans les deux sens, accent tonique marqué) ; préfixes `it-` et `ru-` réservés ; ajoutés à `index.json` |
| 2026-10-25 | Bristol — Publication GitHub Pages | Workflow `.github/workflows/publier-site.yml` (Quarto 1.10.19, `quarto render`, déploiement Pages) ; décision « accès public » reportée dans `CONTEXTE_PROJET.md` (§ 5.4, règle 19.5, journal, question 1), `architecture.md` § 10 et ce fichier. À faire par Armand : activer Pages (source « GitHub Actions »), commit et push |
| 2026-10-27 | Bristol — Publication GitHub Pages (suite) | Dépôt `bristol-site` rendu **public** par Armand (Student Pack non nécessaire), Pages activé, workflow lancé : site en ligne, accueil et paquets de cartes accessibles ; `architecture.md` § 10 et problème 16 mis à jour |
| 2026-10-28 | Bristol — Refonte de l'interface | Audit (captures), architecture UX, design system, implémentation (jetons, thème, accueil, annales, chapitres, fiches matières, application de révision), vérification (rendu complet, captures clair/sombre/mobile, recherche, équations, JavaScript) ; fichiers de mémoire mis à jour. Incident : une commande `git status` a été lancée par erreur par Claude (lecture seule, rien modifié) |
| 2026-10-29 | Bristol — EARF1 — Chapitres 1 à 4 | Lecture complète des sources (supports, 3 TD, notes et corrigés 2023) ; 4 chapitres rédigés avec 16 figures, TD intégrés (TD 1 parties I à IV, TD 2, TD 3), corrigés 2023 en *Notes externes* ; 11 AV tranchés sur délégation ; vérification (rendu Quarto, MathJax, recalculs numériques) ; statut `valide` ; fiche matière, `_quarto.yml`, inventaire, `ETAT_PROJET.md` mis à jour |
| 2026-10-29 | Bristol — EARF1 — Flashcards | 74 cartes (`flashcards/01` à `04`, identifiants `earf1-…`), 246 formules compilées (MathJax 3.2.2), `scripts/flashcards.py --verifier` sans erreur puis lancé : `revision/cartes/earf1.json` (74 cartes) ; statut `flashcards` ; fiche matière mise à jour. À faire par Armand : push, contrôle du rendu en ligne |
