# Bristol — TODO

> Tâches concrètes, classées par priorité. Cocher puis reporter dans `ETAT_PROJET.md` en fin de session.
>
> Dernière mise à jour : 19 octobre 2026 (archive 2A redistribuée, 14 matières du S7 mises en place).

## Priorité 1 — Avant le premier chapitre

- [x] Relire `conventions.md`, `architecture.md` et `ETAT_PROJET.md`, et confirmer les choix faits à la place des questions ouvertes 3 et 4.
- [x] Mettre à jour `CONTEXTE_PROJET.md` : section « État actuel », `_macros.tex` → `_macros.qmd`, questions 3 et 4 dans le journal des décisions.
- [x] Initialiser le dépôt Git et faire un premier commit.
- [x] Copier le poly TS227 dans `sources/ts227/support/`.
- [x] Copier `TD_TS_227.pdf` et `correction_TD_TS_227.pdf` dans `sources/ts227/support/` (inventoriés).
- [x] Noter la version de Quarto dans `architecture.md` (1.10.19, § 9).
- [x] Ajouter `prp-title: "Propriété"` dans la section `crossref` de `_quarto.yml`.
- [ ] Vérifier le rendu de `demo-conventions.qmd` avec `quarto preview`.
- [x] Choisir le premier chapitre de test de TS227 (question ouverte 7) : chapitre 2.
- [x] Fournir les notes manuscrites de ce chapitre.
- [x] Ranger les notes : dates inconnues → `sources/ts227/notes/date-inconnue.pdf` + photos dans `date-inconnue/`.
- [x] Supprimer le dossier vide `sources/ts227/notes/a-dater/` (fait par Armand).

## Priorité 2 — Premier chapitre de bout en bout

- [x] Analyse du chapitre de test : rapport d'analyse et questions.
- [x] Répondre aux 16 questions du rapport — étape 3 (décisions : section 13 du rapport).
- [x] Rédaction du chapitre `cours/02-communication-sans-bruit.qmd` selon la section 13 du rapport, ajout dans `_quarto.yml` et dans la fiche matière (texte ; 7 octobre 2026).
- [x] Trancher le nouveau bloc `av-echelles-figure-cosinus-sureleve` et valider les choix de rédaction (7 octobre 2026 : axes normalisés ; choix validés).
- [x] Styler les blocs tranchés `.a-verifier.tranche` (étiquette `✓ Corrigé`) dans `assets/bristol.scss`, et les ajouter à `demo-conventions.qmd` (7 octobre 2026).
- [ ] Contrôler avec `quarto preview` le rendu des blocs tranchés (clair et sombre) et du chapitre 2.
- [x] Figures du chapitre (12 SVG : 11 matplotlib + 1 TikZ ; F4 omise, F8 fusionnée avec F11) ; statut `redige` (7 octobre 2026).
- [x] Valider les choix des figures listés en section 13.9 du rapport (validés ; F12 refaite en spectre rectangulaire).
- [x] Vérification par Claude (7 octobre 2026, rapport section 13.10).
- [x] Trancher et appliquer les points V1 à V6 du rapport (section 13.11).
- [x] Validation par Armand (7 octobre 2026).
- [x] Trancher la question ouverte 5 (clés `ts-…`) : paquet provisoire abandonné, nouvelles clés (7 octobre 2026).
- [x] Flashcards du chapitre validé (`flashcards/02-communication-sans-bruit.yml`, 61 cartes) ; V5 trié (7 octobre 2026).
- [ ] Contrôler les cartes dans l'application avec `quarto preview` (http://localhost:4848/revision/) : rendu des formules, cartes à reprendre.

## Priorité 2 bis — TS227 chapitre 3

- [x] Analyse, rédaction et figures (étapes 2 à 5) ; TD ex. 2 et ex. 5 q. 10-11 intégrés (7 octobre 2026).
- [x] Répondre aux 8 questions bloquantes (7 octobre 2026, rapport section 16).
- [x] Blocs `av-esperance-exercice-bpsk` et `av-moment-ordre-2-notes` tranchés (7 octobre 2026).
- [x] Trancher `av-dsp-porte-notes` (résultats du TD, sommet $\sigma_a^2 T_s$) et revoir les choix par défaut (7 octobre 2026).
- [ ] Contrôler le rendu avec `quarto preview` (segments `[$…$]{.a-verifier}`, premier environnement `cor-` du site).
- [x] Vérification par Claude (étape 6, rapport § 17), validation (étape 7) et flashcards (étape 8, 56 cartes) (7 octobre 2026).
- [ ] Contrôler les 56 cartes du chapitre 3 dans l'application (`quarto preview`, http://localhost:4848/revision/).

## Priorité 2 ter — TS227 chapitres 1 et 4

- [x] Analyse, rédaction et figures (étapes 2 à 5) des chapitres 4 et 1 ; TD ex. 3, ex. 4 et ex. 5 q. 12-13 intégrés au ch. 4 (7 octobre 2026).
- [x] Questions bloquantes tranchées (choix laissé à Claude, 13 blocs tranchés, rapports § 16) (7 octobre 2026).
- [x] Revoir les choix par défaut (§ 12 des deux rapports) à la validation (validés avec les chapitres, 7 octobre 2026).
- [ ] Contrôler le rendu avec `quarto preview` (ch. 4 : définition `def-fonction-q` et tableau dans un bloc `.notes`, segment orange p. 130 ; ch. 1 : exposants et segments dans les tableaux).
- [x] Vérification (étape 6, rapports § 17), validation (étape 7) et flashcards (étape 8 : 12 + 57 cartes) des chapitres 1 et 4 (7 octobre 2026).
- [ ] Contrôler les 69 cartes des chapitres 1 et 4 dans l'application (`quarto preview`, http://localhost:4848/revision/).
- [ ] Facultatif : noter $r_n$ (au lieu de $r_l[n]$) l'abscisse de `figures/04-constellation-bruitee.py`, pour l'accorder à la légende.

## Priorité 2 quater — EANA3 Circuits intégrés

- [x] Mise en place : sources triées (`sources/eana3/`), arborescence, fiche matière, `_quarto.yml`, accueil, paquet vide, inventaire et plan (7 octobre 2026).
- [x] Q1 de l'inventaire : notes `notes-2023` et `tableau-2020` = sources externes, pas celles d'Armand (7 octobre 2026).
- [ ] **Armand** : confirmer la présentation des notes externes (blocs `.notes` avec citation de la source, ou étiquette distincte « Notes externes ») et, si tu le sais, l'auteur de `tableau-2020` (tableau de F. Rivet ?).
- [ ] **Armand** : fournir tes notes de 2026-2027 dès que tu les as (une par séance, `notes/AAAA-MM-JJ.pdf`).
- [ ] **Armand** : revoir le plan en 5 chapitres et les choix par défaut (inventaire § 4 et § 7), dont le nommage des jeux de notes non datés (à inscrire ensuite dans `conventions.md` § 2).
- [ ] Fournir si possible : tes notes de 2026-2027, une version 2026 du support, les énoncés manquants (TD « amplificateur à contre-réaction », TD « mode commun », annale 2017-2018).
- [ ] Contrôler avec `quarto preview` la barre latérale EANA3, la fiche matière et le paquet vide dans l'application.
- [x] Chapitre 1 : analyse, rédaction, figures (8 octobre 2026) ; statut `redige`.
- [ ] **Armand** : répondre aux 7 questions du rapport du chapitre 1 (§ 14), puis vérification (étape 6) et validation.
- [x] Chapitre 2 : analyse, rédaction, figures, TD 1 (8 octobre 2026) ; statut `redige` ; aucune question bloquante (2 demandes non bloquantes, rapport § 14).
- [x] Chapitre 3 : analyse, rédaction, figures, exercices guidés et 4 TD (8 octobre 2026) ; statut `redige` ; 2 questions (rapport § 14).
- [ ] **Armand** : relire en priorité les solutions proposées des TD du chapitre 3 (aucun corrigé dans les sources) ; fournir les corrigés officiels s'ils existent.
- [x] Chapitre 4 : analyse, rédaction, 9 figures, TD 4, TD 6, TD anneau, sujet 2021 (8 octobre 2026) ; statut `redige` ; 4 questions (rapport § 14).
- [ ] **Armand** : relire les solutions proposées du TD 6 et du sujet 2021 (chapitre 4, sans corrigé) ; signaler si le cours 2026-2027 traite les classes A, B et C.
- [x] Chapitre 5 : analyse, rédaction, 9 figures, TD 5, sujet Brokaw 2025 (partie Deval), sujet 2026 (8 octobre 2026) ; statut `redige` ; 3 questions (rapport § 14).
- [ ] **Armand** : relire les solutions proposées du chapitre 5 (TD 5 version SOI, Brokaw, générateur de courant : aucun corrigé) ; confirmer ce que l'enseignant appelle « bandgap fractionnaire ».
- [ ] Après les réponses d'Armand : vérification (étape 6) et flashcards des chapitres 1 à 5 ; contrôle `quarto preview` des 5 chapitres (clair et sombre).
- [ ] Contrôler avec `quarto preview` le rendu du chapitre 1 et des blocs `✎ Notes externes` (clair et sombre).

## Priorité 2 quinquies — Matières du S7 (archive 2A, 19 octobre 2026)

- [x] Redistribuer `sources/2A.zip` : 413 fichiers rangés dans `sources/<code>/`, copies vérifiées (MD5) ; fiches matières, inventaires et plans proposés des 14 nouvelles matières ; barres latérales, accueil, paquets vides (19 octobre 2026).
- [x] Contrôler le rendu de l'accueil, des 14 barres latérales et des fiches matières (Claude, Quarto 1.10.19, 19 octobre 2026) ; reste à voir chez Armand : polices et formules.
- [ ] **Armand** : valider ou corriger les plans proposés (AUTO1 6 ch., AUTO3 4, EAEP1 7, EANA2 5, EARF1 4, NUMC1 6 ; TSIG1 : fait, plan des notes d'Armand) avant l'analyse des premiers chapitres.
- [ ] **Armand** : confirmer deux rattachements par défaut : annales « Initiation aux bruits » (EA222) → EANA2 ; TD VHDL rangés dans NUMC1 (et non NUME3).
- [ ] **Armand** : fournir le support d'EANA1 (aucun support officiel dans l'archive) et, pour TSIG1, le support de cours s'il existe (seules 6 p. d'illustrations reçues).
- [ ] **Armand** : compléter les enseignants manquants (EANA1, NUME3, PROJ1).
- [ ] NUMR1 : établir le plan à partir des deux parties du cours (368 p.) ; décider du sort du paquet hérité `reseaux.json` (question ouverte 6).
- [ ] TS227 : exploiter les notes externes `notes-2023` (16 p.) dans les chapitres 1 à 4, et les TP 1 à 3 (phase 2).
- [ ] **Armand** : supprimer `sources/2A.zip` (contenu redistribué).
- [ ] Choisir l'ordre des matières à traiter ensuite (suggestion : celles dont l'examen arrive en premier).

## Priorité 2 sexies — TSIG1 (partiel le 22 octobre 2026)

- [x] Notes d'Armand rangées et transcrites ; 5 chapitres rédigés et vérifiés (statut `verifie`), TD 1 à 3 intégrés (20 octobre 2026).
- [ ] **Armand** : relire les 5 chapitres et trancher les 30 blocs *À vérifier* (1/4/9/11/5), en priorité `av-phase-moyenne-signe`, `av-phase-lineaire-retard-groupe`, `av-module-passe-tout` et les `av-td-…` (erreurs des corrigés 2023).
- [ ] Après la relecture : statut `valide`, flashcards définitives (`flashcards/0N-*.yml`, identifiants `tsig1-…`), `scripts/flashcards.py`, retrait du paquet provisoire `tsig1-partiel.json` (préfixe `tsig1p-` réservé).
- [ ] Contrôler le rendu des 5 chapitres avec `quarto preview` (formules, clair et sombre).
- [x] Annales : 9 sujets corrigés en images découpées par question (20 octobre 2026), dont le corrigé 2022-2023.
- [ ] **Armand** : relire les corrigés des annales et trancher les 11 blocs `av-ann…` (notamment `av-ann13-pulsation-3pi4`, `av-ann22-gain-conception`).
- [ ] Mettre à jour `analyses/annales-partiel.md` avec les trois sujets du recueil (mars 2014, mars 2018, décembre 2019).

## Priorité 3 — Outillage

- [x] `scripts/flashcards.py` : conversion YAML → `revision/cartes/*.json`, avec traitement des macros et contrôles (7 octobre 2026).
- [x] Fixer le port de `quarto preview` (4848) pour conserver la progression de révision (7 octobre 2026).
- [ ] Si besoin : transférer la progression des paquets hérités de l'ancien site (figé) vers l'application locale. **Impossible avec l'export actuel** (cartes seulement) : dépend de la tâche « export/import de la progression » (section « Avant la publication »).
- [ ] `scripts/verifier.py` : vérifications listées dans `architecture.md` §7.
- [ ] Rendu PDF des quatre catégories (filtre Lua ou `tcolorbox`), et macros dans l'en-tête LaTeX.
- [ ] Application de révision : lien « Voir dans le cours » (champ `ref`).

## Avant la publication (pour la promo)

- [ ] Mettre en place l'accès réservé par liste d'e-mails (question 1 ; solution privilégiée : Cloudflare Pages + Cloudflare Access).
- [ ] Demander l'accord des enseignants concernés.
- [ ] Rédiger la page « À propos » : quatre catégories, origine des notes.
- [ ] Application de révision : export et import de la **progression** (pas seulement des cartes).
- [ ] Relire les pages à publier : aucun contenu personnel ou sans rapport avec le cours.

## Plus tard

- [ ] Trancher l'organisation des dépôts (question 2).
- [ ] Prévoir un moyen pour les camarades de signaler une erreur ou de proposer des notes (question 13).
- [ ] TS227 chapitre 6 : renvoyer vers l'efficacité spectrale du chapitre 2 (`02-communication-sans-bruit.qmd`).
- [ ] Vérifier si rtajan.github.io contient une version plus récente du poly ou d'autres ressources.
- [ ] Phase 2 : préciser la correspondance des numéros de questions entre l'énoncé et la correction du TD (versions différentes).
- [ ] Décider du sort des paquets hérités (question 6).
- [ ] Révision par chapitre et mode « veille d'examen » dans l'application.
- [ ] Synchronisation de la progression entre appareils (question 8).
- [ ] Phase 2 : TD, TP, annales, corrigés.
