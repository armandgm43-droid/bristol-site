# Bristol — Architecture technique

> Détails techniques du projet : configuration Quarto, structure des dossiers, application de révision, scripts, build, hébergement.
> Les choix de fond sont dans `CONTEXTE_PROJET.md` (section 5) ; les règles d'écriture dans `conventions.md`.
>
> Dernière mise à jour : 7 octobre 2026.

---

## 1. Vue d'ensemble

```text
Sources brutes (sources/, hors dépôt)
        │  analyse et rédaction (Claude + Armand)
        ▼
Chapitres .qmd ──────────────► quarto render ──► _site/ (HTML statique)
        │                                          ▲
        ▼                                          │ copié tel quel
Flashcards .yml ──► script de conversion ──► revision/cartes/*.json
                    scripts/flashcards.py          │
                                                   ▼
                                     revision/index.html (application)
```

---

## 2. Structure des dossiers (état réel au 7 octobre 2026)

```text
Bristol/
├── _quarto.yml               configuration du site
├── _macros.qmd               macros LaTeX communes (inclus en haut de chaque page)
├── index.qmd                 page d'accueil : liste des matières
├── demo-conventions.qmd      page de démonstration des quatre catégories
├── CONTEXTE_PROJET.md        vision et méthode
├── conventions.md            règles de rédaction
├── architecture.md           ce document
├── ETAT_PROJET.md            état d'avancement
├── TODO.md                   tâches
├── README.md                 présentation et commandes
├── .gitignore
├── assets/
│   ├── bristol-tokens.css    jetons de DA (couleurs, polices, espacements, clair et sombre) : source unique site + application
│   ├── bristol.scss          thème Quarto : règles seulement, couleurs via var(--…)
│   └── bristol-sombre.scss   marqueur du thème sombre pour Quarto (aucune couleur)
├── matieres/
│   └── ts227-communications-numeriques/
│       ├── index.qmd         fiche matière
│       ├── analyses/         rapports d'analyse des chapitres (.md, non rendus)
│       ├── cours/        chapitres .qmd (02-communication-sans-bruit.qmd)
│       ├── figures/      sources .py/.tex et rendus .svg (12 figures du ch. 2)
│       ├── flashcards/   cartes YAML (02-communication-sans-bruit.yml : 61 cartes)
│       ├── td/  tp/  annales/  corriges/   (vides)
├── revision/
│   ├── index.html            application de flashcards (fichier unique)
│   └── cartes/
│       ├── index.json        liste des paquets à charger
│       └── *.json            paquets : 5 hérités + ts227.json (généré par scripts/flashcards.py)
├── scripts/
│   └── flashcards.py         conversion YAML → revision/cartes/<matiere>.json
└── sources/                  sources brutes, ignorées par Git
    ├── LISEZMOI.txt
    └── ts227/
        ├── support/          poly, TD, correction du TD
        └── notes/            date-inconnue.pdf + date-inconnue/ (photos des feuillets)
```

Fichiers générés, jamais versionnés : `_site/`, `.quarto/`, `*_files/`, `*_cache/`.

---

## 3. Configuration Quarto (`_quarto.yml`)

| Réglage | Valeur | Rôle |
|---|---|---|
| `project.type` | `website` | site statique |
| `project.output-dir` | `_site` | dossier de sortie |
| `project.render` | `*.qmd`, `matieres/**/*.qmd` | seuls les `.qmd` deviennent des pages ; les `.md` restent des documents de travail |
| `project.resources` | `revision/**`, `assets/bristol-tokens.css` | l'application de révision est copiée telle quelle, avec les jetons qu'elle charge |
| `lang` | `fr` | titres d'environnements et libellés en français |
| `website.search` | `true` | recherche plein texte côté navigateur |
| `website.navbar` | Matières, Révisions, Conventions | barre de navigation |
| `website.sidebar` | une barre par matière (`id: ts227`) | les chapitres y sont ajoutés à la main, dans l'ordre |
| `format.html.theme` | clair : `cosmo` + `assets/bristol.scss` ; sombre : idem + `assets/bristol-sombre.scss` | thème (§ 4) |
| `format.html.css` | `assets/bristol-tokens.css` | jetons de DA, inclus dans chaque page |
| `format.html.respect-user-color-scheme` | `true` | mode sombre selon le système, sauf choix explicite (bouton) |
| `format.html.html-math-method` | `mathjax` | rendu des maths (Quarto 1.10 charge MathJax 4 ; l'application, MathJax 3.2.2) |
| `format.html.number-sections` | `true` | sections numérotées (désactivé sur les pages d'index) |
| `crossref.*-prefix` | libellés français | `@eq-…` → « équation 3 », etc. |

### Ajout d'un chapitre

1. Créer `matieres/<matiere>/cours/NN-slug.qmd` avec le front matter de `conventions.md`.
2. L'ajouter dans la barre latérale de la matière, dans `_quarto.yml`, section « Cours ».
3. Mettre à jour le tableau des chapitres de la fiche matière.

### Ajout d'une matière

1. Créer `matieres/<code>-<intitule>/` avec `index.qmd` et les sous-dossiers.
2. Ajouter une barre latérale `id: <code>` dans `_quarto.yml`.
3. Ajouter la matière au tableau de `index.qmd`.

---

## 4. Direction artistique et thème

Règles de la DA (métaphore, surfaces, typographie, catégories, mode sombre) : `conventions.md`, § 13. Ici, la mise en œuvre.

### 4.1 Trois fichiers dans `assets/`

| Fichier | Contenu | Lu par |
|---|---|---|
| `bristol-tokens.css` | **Source unique** : variables CSS (couleurs, polices, tailles, espacements), en clair et en sombre ; import des polices Google Fonts | le site (`format.html.css`) et l'application (`<link href="../assets/bristol-tokens.css">`) |
| `bristol.scss` | Thème Quarto : règles seulement (barre de navigation, feuille de lecture, barres latérales, recherche, quatre catégories, impression). Aucune couleur en dur : tout passe par `var(--…)`. Côté Sass, seules les polices sont passées à Bootstrap | Quarto (thème clair et sombre) |
| `bristol-sombre.scss` | Commentaire sentinelle `/*! dark */`, sans aucune couleur : il indique à Quarto que la feuille compilée est le thème sombre (sinon Quarto la traite comme claire, la classe `body.quarto-dark` n'est jamais posée et le bouton ne fait rien) | Quarto (thème sombre uniquement) |

Les deux feuilles Bootstrap compilées (claire et sombre) sont donc presque identiques : c'est le **jeu de jetons actif** qui change les couleurs.

### 4.2 Sélection du jeu de jetons

Dans `bristol-tokens.css`, dans cet ordre :

1. `:root` : valeurs claires (défaut) ;
2. `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) }` : sombre si le système l'est ;
3. `:root[data-theme="dark"]` (application) et `:root:has(> body.quarto-dark)` (site) : sombre choisi explicitement ;
4. `:root:has(> body.quarto-light)` : clair choisi explicitement sur le site alors que le système est sombre.

Choix explicite mémorisé dans `localStorage`, clé **`quarto-color-scheme`** (`alternate` = sombre, `default` = clair), écrite par le bouton de Quarto et par celui de l'application (même origine, donc même préférence). L'application lit cette clé dans un petit script en tête de page et la suit aussi entre onglets (événement `storage`).

Les valeurs claires et sombres sont écrites deux fois dans ce même fichier (bloc `@media` et bloc explicite) : c'est imposé par CSS, sans préprocesseur. **Les deux copies doivent rester identiques.**

### 4.3 Catégories, impression, PDF

- Blocs `div.notes`, `div.complement`, `div.a-verifier` : filet à gauche + étiquette en `::before` + fond teinté, couleurs `--cat-…`. Segments `span.…` : couleur + symbole.
- Impression (`@media print`) : feuille blanche, mêmes repères, sans fond.
- Figures (`main.content figure img`) : fond `--figure-bg` et marge `--figure-pad`, nulle en clair ; en sombre, les SVG à couleurs fixes restent lisibles sur un fond blanc.
- Blocs tranchés (`.a-verifier.tranche`) : étiquette `✓ Corrigé`, filet de 2 px au lieu de 4 px, fond `--cat-verifier-bg` mélangé à 50 % de transparent (`color-mix`) ; mêmes jetons `--cat-verifier…`, donc clair et sombre sans couleur en dur. Exemple dans `demo-conventions.qmd`.
- **Rendu PDF (LaTeX) : pas encore fait.** Il faudra un filtre Lua ou des environnements LaTeX (`tcolorbox`) qui reproduisent filet et étiquette ; reprendre alors les couleurs claires de `bristol-tokens.css`.
- Polices et MathJax viennent d'Internet (Google Fonts, jsDelivr) : sans connexion, polices de repli et formules non rendues.

---

## 5. Macros (`_macros.qmd`)

- Bloc `$$ \newcommand… $$` dans un div `.hidden`, inclus en haut de chaque page par `{{< include /_macros.qmd >}}`.
- Fonctionne pour le HTML (MathJax). Pour le PDF, il faudra aussi injecter les macros dans l'en-tête LaTeX (`include-in-header`).
- L'application de révision ne lit pas ce fichier : `scripts/flashcards.py` **développe les macros** dans le texte des cartes (lecture des `\newcommand` de `_macros.qmd`, entre accolades si le corps contient `_` ou `^` : `x_\Ts` → `x_{T_s}`). Une nouvelle macro est donc prise en compte sans modifier le script.

---

## 6. Application de révision (`revision/`)

- **Fichier unique** `index.html` (HTML + CSS + JS, ~88 ko), sans build. **Dépend de `../assets/bristol-tokens.css`** (couleurs, polices, espacements) : une copie isolée du dossier `revision/` (dépôt GitHub Pages) doit emporter ce fichier au même chemin relatif.
- Barre de navigation : même dessin que celle du site (`conventions.md` § 13.6). Liens écrits en dur dans le `<header class="site-head">` : à tenir alignés sur `website.navbar` de `_quarto.yml`. « Révisions » ramène à la liste des paquets sans recharger la page ; « Bristol » et les autres liens mènent aux pages du site. Script de navigation séparé du script de l'application (il ne touche ni aux paquets ni à la progression).
- Mode sombre : les feuilles (liste, dialogues) deviennent sombres ; les fiches de révision restent en papier clair (jetons `--card-…`, redéfinis sur `.study`).
- Maths : MathJax 3.2.2 (`tex-svg`) chargé depuis `cdn.jsdelivr.net`.
- Progression : `localStorage`, clé `bristol:v1` (format `{ v: 1, decks }`). Elle est **propre au navigateur et à l'adresse du site** (protocole + nom d'hôte + port) : changer d'hébergement, de domaine ou de port repart d'une progression vide. **L'export actuel de l'application exporte les cartes (texte recto/verso), pas la progression** : il ne permet pas de la transférer. Transfert de la progression : tâche « export/import de la progression » de `TODO.md`, section « Avant la publication » (pas encore fait).
- **Révision en local (depuis le 7 octobre 2026)** : `quarto preview` sert le site sur un **port fixe, 4848** (`project.preview.port` dans `_quarto.yml`, avec `browser: true`). L'application est donc toujours à l'adresse `http://localhost:4848/revision/` et la progression est retrouvée d'un lancement à l'autre.
  - Ne pas changer ce port, ni lancer `quarto preview --port …` : autre adresse, progression vide.
  - Toujours passer par `localhost`, pas par `127.0.0.1` (autre adresse pour le navigateur).
  - Si le port 4848 est déjà pris (un autre `quarto preview` ouvert), fermer l'autre aperçu plutôt que de changer de port.
  - Après `python scripts/flashcards.py`, relancer `quarto preview` (ou recharger la page si l'aperçu a recopié `revision/`) : les paquets sont relus à l'ouverture de l'application.
  - La progression reste propre au navigateur et à l'ordinateur : pas de synchronisation (question ouverte 8). L'export actuel de l'application ne sauvegarde que les cartes, **pas la progression** : voir la tâche « export/import de la progression » de `TODO.md`, section « Avant la publication ».
- Chargement des paquets : à l'ouverture, lecture de `cartes/index.json` puis de chaque fichier listé (`fetch`, sans cache). Ne fonctionne pas en `file://` : passer par `quarto preview` ou un serveur local.
- Format d'un paquet :

  ```json
  { "deck": "Nom", "color": "#FFF0A6",
    "items": [ { "key": "id", "chap": "Chapitre", "front": "Recto", "back": "Verso" } ] }
  ```

- Fusion à l'ouverture : une `key` existante est mise à jour **sans perte de progression** ; une nouvelle est ajoutée ; une carte absente du fichier est supprimée.

### Paquets présents

| Fichier | Paquet | Cartes | Préfixe |
|---|---|---|---|
| `reseaux.json` | Réseaux et programmation réseau | 225 | `res-` |
| `anglais-ielts.json` | Anglais : vocabulaire IELTS | 107 | `ang-` |
| `vhdl.json` | VHDL | 90 | `vhdl-` |
| `c-unix.json` | C et Unix | 108 | `cu-` |
| `latex.json` | LaTeX | 92 | `latex-` |
| `ts227.json` | TS227 — Introduction aux communications numériques | 61 (ch. 2) | `ts227-` — **généré** par `scripts/flashcards.py` ; remplace le paquet provisoire (129 cartes `ts-`, abandonné le 7 octobre 2026) |

---

## 7. Scripts (`scripts/`)

Langage : **Python 3** avec **PyYAML** (seule dépendance prévue).

| Script | Rôle |
|---|---|
| `flashcards.py` | **Écrit (7 octobre 2026).** Convertit `matieres/*/flashcards/*.yml` en `revision/cartes/<matiere>.json` et ajoute le paquet à `cartes/index.json` s'il manque. Contrôles avant écriture (rien n'est écrit au moindre problème) : champs obligatoires et inconnus ; `matiere` cohérent avec le dossier ; nom du fichier = nom du chapitre ; identifiants `<matiere>-<slug>` uniques dans la matière, absents des `ids-retires`, sans préfixe hérité ; types et sources valides ; `ref` présent dans le chapitre (ou `NN-slug.qmd#label`) ; astérisque isolé ; formule en ligne coupée. Transformations : macros développées, lignes jointes façon Markdown (`conventions.md` § 10.4). Couleur du paquet : celle du fichier existant, sinon `#FFF0A6`. Option `--verifier` : contrôles seuls |
| `verifier.py` | Vérifications : front matter complet et statut valide ; labels uniques dans la matière ; `ref` des cartes qui pointent vers un label existant ; identifiants de cartes uniques dans la matière et absents de tous les `ids-retires` de la matière ; types de cartes valides ; astérisques isolés ; liste des blocs `#av-…` restants |

Le script de vérification sera lancé avant chaque commit (à la main, puis éventuellement en *pre-commit hook*).

---

## 8. Build et commandes

| Commande | Effet |
|---|---|
| `quarto preview` | aperçu local, rechargé à chaque modification, toujours sur `http://localhost:4848` (port fixe, voir § 6) |
| `quarto render` | génère le site complet dans `_site/` |
| `python scripts/flashcards.py` | régénère les paquets de cartes (`--verifier` : contrôles seuls) |
| `python scripts/verifier.py` | (à venir) vérifications automatiques |

Pour un site de plusieurs centaines de pages : rendu d'un seul fichier (`quarto render chemin/fichier.qmd`) pendant la rédaction, et `freeze: auto` dès que des figures sont calculées en Python dans les pages.

---

## 9. Dépendances

| Outil | Version | Remarque |
|---|---|---|
| Quarto | 1.10.19 (d'après le `_site/` généré le 6 octobre 2026) | installé sur le PC d'Armand ; ≥ 1.7 requis pour `respect-user-color-scheme` |
| Python | 3.x | figures et scripts |
| PyYAML | 6.x | scripts |
| matplotlib | 3.10 (rendu des figures du ch. 2 de TS227) | figures : `python3 figures/NN-slug.py` écrit le `.svg` voisin |
| LaTeX (TinyTeX ou TeX Live) + dvisvgm | TeX Live 2022, dvisvgm 2.13 (rendu des figures du ch. 2) | schémas TikZ : `latex` dans un dossier temporaire, puis `dvisvgm --no-fonts --exact-bbox` (commande en tête de chaque `.tex`) ; PDF plus tard |
| Git | à préciser | dépôt initialisé (commit `501e006`) ; dépôt GitHub : voir § 10 |

---

## 10. Hébergement

**Non décidé** (question ouverte 1 de `CONTEXTE_PROJET.md`). En attendant : **utilisation locale uniquement** (`quarto preview`), conformément à la règle « pas de publication avant clarification des droits ».

### Dépôts GitHub

| Dépôt | Visibilité | Contenu | Remarque |
|---|---|---|---|
| `armandgm43-droid/bristol-site` | **privé** | **dépôt du projet** : ce dossier (site Quarto, application dans `revision/`, fichiers de mémoire) | dépôt de référence |
| `armandgm43-droid/bristol` | public (GitHub Pages) | **ancien site de cartes** (application de révision seule) | **figé** depuis le 7 octobre 2026 : plus aucune modification ; **ne pas confondre** avec le dépôt du projet |

La révision se fait désormais en local (§ 6). L'ancien dépôt `bristol` n'est plus mis à jour ; son sort (archiver, supprimer) pourra être décidé avec la question ouverte 2.
