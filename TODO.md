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
