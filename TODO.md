# Bristol — TODO

> Tâches concrètes, classées par priorité. Cocher puis reporter dans `ETAT_PROJET.md` en fin de session.
>
> Dernière mise à jour : 7 octobre 2026.

## Priorité 1 — Avant le premier chapitre

- [x] Relire `conventions.md`, `architecture.md` et `ETAT_PROJET.md`, et confirmer les choix faits à la place des questions ouvertes 3 et 4.
- [x] Mettre à jour `CONTEXTE_PROJET.md` : section « État actuel », `_macros.tex` → `_macros.qmd`, questions 3 et 4 dans le journal des décisions.
- [x] Initialiser le dépôt Git et faire un premier commit.
- [x] Copier le poly TS227 dans `sources/ts227/support/`.
- [x] Copier `TD_TS_227.pdf` et `correction_TD_TS_227.pdf` dans `sources/ts227/support/` (inventoriés).
- [ ] Noter la version de Quarto dans `architecture.md` (`quarto --version`).
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
- [ ] Trancher le nouveau bloc `av-echelles-figure-cosinus-sureleve` (rapport ch. 2, section 13.8) et valider les choix de rédaction listés en 13.8.
- [ ] Styler les blocs tranchés `.a-verifier.tranche` (étiquette `✓ Corrigé`) dans `assets/bristol.scss`, et les ajouter à `demo-conventions.qmd`.
- [ ] Figures du chapitre (Python ou TikZ, en SVG) : F1 à F14, emplacements marqués `<!-- FIGURE Fn -->` dans le `.qmd` ; puis statut `redige`.
- [ ] Vérification par Claude, puis validation par Armand.
- [ ] Trancher la question ouverte 5 (clés `ts-…`) avant de générer les flashcards.
- [ ] Flashcards du chapitre validé (`flashcards/NN-slug.yml`).

## Priorité 3 — Outillage

- [ ] `scripts/flashcards.py` : conversion YAML → `revision/cartes/*.json`, avec traitement des macros.
- [ ] `scripts/verifier.py` : vérifications listées dans `architecture.md` §7.
- [ ] Rendu PDF des quatre catégories (filtre Lua ou `tcolorbox`), et macros dans l'en-tête LaTeX.
- [ ] Application de révision : lien « Voir dans le cours » (champ `ref`).

## Plus tard

- [ ] Trancher l'hébergement et les droits (question 1), et l'organisation des dépôts (question 2).
- [ ] TS227 chapitre 6 : renvoyer vers l'efficacité spectrale du chapitre 2 (`02-communication-sans-bruit.qmd`).
- [ ] Vérifier si rtajan.github.io contient une version plus récente du poly ou d'autres ressources.
- [ ] Phase 2 : préciser la correspondance des numéros de questions entre l'énoncé et la correction du TD (versions différentes).
- [ ] Décider du sort des paquets hérités (question 6).
- [ ] Révision par chapitre et mode « veille d'examen » dans l'application.
- [ ] Synchronisation de la progression entre appareils (question 8).
- [ ] Phase 2 : TD, TP, annales, corrigés.
