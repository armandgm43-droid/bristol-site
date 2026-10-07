# Bristol

Base de connaissances personnelle pour mes études d'ingénieur : cours, flashcards, puis TD, TP, annales et corrigés.

Avant toute chose, lire `CONTEXTE_PROJET.md`.

## Commandes

- `quarto preview` : aperçu du site en local, rechargé à chaque modification, toujours sur http://localhost:4848 (port fixe : la progression de révision en dépend).
  La progression ne peut pas encore être transférée d'une adresse ou d'un navigateur à l'autre : l'export actuel de l'application exporte les cartes, pas la progression (voir la tâche « export/import de la progression » de `TODO.md`).
- `python scripts/flashcards.py` : convertit les flashcards YAML en paquets de l'application (`revision/cartes/`).
- `quarto render` : génère le site complet dans `_site/`.
