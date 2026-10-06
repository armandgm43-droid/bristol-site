# Bristol — TODO

> Tâches concrètes, classées par priorité. Cocher puis reporter dans `ETAT_PROJET.md` en fin de session.
>
> Dernière mise à jour : 6 octobre 2026.

## Priorité 1 — Avant le premier chapitre

- [x] Relire `conventions.md`, `architecture.md` et `ETAT_PROJET.md`, et confirmer les choix faits à la place des questions ouvertes 3 et 4.
- [x] Mettre à jour `CONTEXTE_PROJET.md` : section « État actuel », `_macros.tex` → `_macros.qmd`, questions 3 et 4 dans le journal des décisions.
- [ ] Initialiser le dépôt Git (`git init`) et faire un premier commit (`chore: initial project skeleton`).
- [ ] Copier les sources TS227 dans `sources/ts227/support/`.
- [ ] Noter la version de Quarto dans `architecture.md` (`quarto --version`).
- [x] Ajouter `prp-title: "Propriété"` dans la section `crossref` de `_quarto.yml`.
- [ ] Vérifier le rendu de `demo-conventions.qmd` avec `quarto preview`.
- [ ] Choisir le premier chapitre de test de TS227 (question ouverte 7).
- [ ] Fournir les notes manuscrites de ce chapitre (un PDF par séance, nommé par date).

## Priorité 2 — Premier chapitre de bout en bout

- [ ] Analyse du chapitre de test : rapport d'analyse et questions.
- [ ] Rédaction du chapitre (`cours/NN-slug.qmd`), ajout dans `_quarto.yml` et dans la fiche matière.
- [ ] Figures du chapitre (Python ou TikZ, en SVG).
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
- [ ] Décider du sort des paquets hérités (question 6).
- [ ] Révision par chapitre et mode « veille d'examen » dans l'application.
- [ ] Synchronisation de la progression entre appareils (question 8).
- [ ] Phase 2 : TD, TP, annales, corrigés.
