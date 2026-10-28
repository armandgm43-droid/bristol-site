# Bristol — Architecture technique

> Détails techniques du projet : configuration Quarto, structure des dossiers, application de révision, scripts, build, hébergement.
> Les choix de fond sont dans `CONTEXTE_PROJET.md` (section 5) ; les règles d'écriture dans `conventions.md`.
>
> Dernière mise à jour : 25 octobre 2026 (§ 10 : publication sur GitHub Pages).

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
│       └── *.json            paquets : 5 hérités + ts227.json, eana3.json (générés par scripts/flashcards.py)
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
| `format.html.theme` | clair : `default` + `assets/bristol.scss` ; sombre : idem + `assets/bristol-sombre.scss` (cosmo abandonné le 28 octobre 2026 : il importait une police Google) | thème (§ 4) |
| `project.pre-render` | `scripts/catalogue.ts` : catalogue des matières (§ 4.4) | accueil, annales, en-têtes |
| `format.html.filters`, `template-partials`, `grid` | `assets/bristol.lua`, `assets/partials/title-block.html`, largeurs des colonnes | § 4.1 |
| `website.navbar`, `page-footer` | Matières, Annales, Révisions ; « Conventions de lecture » dans le pied de page | navigation |
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

Règles de la DA (palette, typographie, composants, catégories, mode sombre) : `conventions.md`, § 13. Ici, la mise en œuvre. **Refonte complète le 28 octobre 2026** (design system « Bristol 2026 »).

### 4.1 Fichiers dans `assets/`

| Fichier | Contenu | Lu par |
|---|---|---|
| `bristol-tokens.css` | **Source unique** : `@font-face` des polices Geist (auto-hébergées), variables CSS (couleurs, échelle typographique, espacements, rayons, ombres, durées) en clair et en sombre, icônes Lucide en masques CSS (`--icon-…`, classe `.i .i-…`), style `kbd`, `prefers-reduced-motion` | le site (`format.html.css`) et l'application (`<link href="../assets/bristol-tokens.css">`) |
| `fonts/` | `Geist-Variable.woff2`, `Geist-Italic-Variable.woff2`, `GeistMono-Variable.woff2` + `LICENSE-Geist.txt` (SIL OFL) ; copiés dans le site par `project.resources` | `bristol-tokens.css` |
| `bristol.scss` | Thème Quarto (base `default`, plus `cosmo`) : règles seulement, en 10 parties (base, navigation, barres latérales, en-tête, lecture, quatre catégories, environnements de cours, « Pour continuer », accueil/annales/fiches, recherche/pied de page/impression). Aucune couleur en dur, sauf `$primary` passé à Bootstrap pour ses calculs internes | Quarto (thème clair et sombre) |
| `bristol-sombre.scss` | Commentaire sentinelle `/*! dark */` (inchangé) | Quarto (thème sombre) |
| `bristol.lua` | Filtre Quarto (`format.html.filters`) : lit `catalogue.json` ; en-tête de contexte des chapitres (matière, « Chapitre N sur M », état du contenu), des fiches matières (domaine) et des autres pages d'une matière ; section « Pour continuer » en fin de chapitre (flashcards, annales, retour à la matière) ; accès rapides en tête des fiches matières ; déclare `bristol.js` comme dépendance HTML (copié dans `site_libs/`) | Quarto |
| `partials/title-block.html` | Copie du partial `title-block.html` de Quarto 1.10, avec la variable `bristol-context` au-dessus du titre (`format.html.template-partials`). À comparer au partial d'origine en cas de mise à jour de Quarto | Quarto |
| `bristol.js` | JavaScript léger, sans dépendance : Ctrl/⌘ K (recherche), barre de progression de lecture et mémorisation du dernier chapitre ouvert (`localStorage` « `bristol:lecture` »), filtres de la bibliothèque, tuiles « Reprendre » et « Flashcards » de l'accueil (cartes dues lues dans « `bristol:v1` », le stockage de l'application, sans rien inventer), lien « Toutes les matières » dans la barre latérale. Sans JavaScript, toutes les pages restent complètes | toutes les pages |
| `catalogue.json` | **Généré** par `scripts/catalogue.ts` (voir § 4.4) | `bristol.lua`, `bristol.js` |

### 4.2 Sélection du jeu de jetons

Inchangé : dans `bristol-tokens.css`, (1) `:root` clair, (2) `@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) }`, (3) `:root[data-theme="dark"]` (application) et `:root:has(> body.quarto-dark)` (site), (4) `:root:has(> body.quarto-light)`. Choix mémorisé dans `localStorage`, clé **`quarto-color-scheme`**, commun au site et à l'application (vérifié le 28 octobre 2026 dans les deux sens). **Les trois copies du jeu sombre et les deux du jeu clair doivent rester identiques.** Remarque : en `file://`, Quarto ne mémorise pas le choix (comportement normal).

### 4.3 Catégories, environnements, impression, PDF

- Quatre catégories : formes, étiquettes et classes inchangées (filet à gauche + étiquette + fond) ; couleurs des jetons `--cat-…` reprises dans la nouvelle palette (mêmes familles).
- Environnements de cours (`.theorem.definition`, `.proposition`, `.example`, `.exercise`, `.proof`, `.proof.solution`, `.proof.remark`) : encadré complet à bordure fine avec icône Lucide et teinte très légère par type (jetons `--env-…`) — forme distincte des catégories, même imbriqués. Démonstrations : filet fin et `∎` final.
- « À retenir » : les sections `#sec-retenir-…` sont stylées en panneau de synthèse (icône signet). Aucune modification des `.qmd`.
- Classe `.attention` stylée (proposition, voir `conventions.md` § 6), non utilisée dans les cours.
- Impression (`@media print`) : navigation masquée, fonds retirés, repères conservés. **Rendu PDF (LaTeX) : toujours à faire.**
- Figures : fond `--figure-bg` et marge `--figure-pad` en sombre (inchangé).
- Mobile : `main.content { overflow-x: clip }` sous 768 px (les numéros d'équation de MathJax, positionnés en absolu, faisaient déborder la page) ; formules en ligne trop longues défilables.
- Polices : auto-hébergées (plus de Google Fonts). MathJax reste chargé depuis jsDelivr (site : MathJax 4 ; application : 3.2.2).

### 4.4 Catalogue généré (`scripts/catalogue.ts`)

- Script **Deno** lancé par Quarto avant chaque rendu complet (`project.pre-render` dans `_quarto.yml`) : rien à installer, ni sous Windows ni sur GitHub Actions. Lancement manuel : `quarto run scripts/catalogue.ts`.
- Lit `matieres/*/index.qmd`, `cours/*.qmd` (titre, `chapitre`, `statut`), `annales/`, `fiches/`, `td/`, `tp/`, le nombre de cartes de `flashcards/NN-slug.yml`, et `revision/cartes/*.json` (paquets de la matière : `<code>.json` et `<code>-*.json`). Classement par domaine et nature (cours, TP, projet) : **`matieres/domaines.json`** (à compléter pour une nouvelle matière).
- Écrit `assets/catalogue.json`, `_generes/accueil-acces.md` (tuiles de l'accueil), `_generes/accueil-matieres.md` (bibliothèque) et `_generes/annales.md` (page `annales.qmd`), seulement si leur contenu change. **Ces fichiers sont versionnés** : un rendu d'une seule page (`quarto render index.qmd`) ne lance pas le script et doit trouver les fichiers inclus. Ne pas les modifier à la main.
- Conséquence : **plus aucun compteur à tenir à jour à la main sur l'accueil** (ancien § 13.7 de `conventions.md`).

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
  - Une matière dont le dossier `flashcards/` ne contient aucun fichier YAML produit un **paquet vide** (`items: []`), pour qu'elle apparaisse dans l'application (ajouté le 7 octobre 2026 pour EANA3).
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
| `flashcards.py` | **Écrit (7 octobre 2026).** Convertit `matieres/*/flashcards/*.yml` en `revision/cartes/<matiere>.json` et ajoute le paquet à `cartes/index.json` s'il manque. Contrôles avant écriture (rien n'est écrit au moindre problème) : champs obligatoires et inconnus ; `matiere` cohérent avec le dossier ; nom du fichier = nom du chapitre ; identifiants `<matiere>-<slug>` uniques dans la matière, absents des `ids-retires`, sans préfixe hérité ; types et sources valides ; `ref` présent dans le chapitre (ou `NN-slug.qmd#label`) ; astérisque isolé ; formule en ligne coupée. Transformations : macros développées, lignes jointes façon Markdown (`conventions.md` § 10.4). Couleur du paquet : celle du fichier existant, sinon `#FFF0A6`. Option `--verifier` : contrôles seuls. Depuis le 18 octobre 2026, une matière sans fiche `index.qmd` (dossier créé d'avance) est ignorée |
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
| Quarto (contrôle par Claude) | 1.10.19, archive Linux de GitHub (`quarto-1.10.19-linux-amd64.tar.gz`) | installé par Claude dans sa machine de travail (hors du projet) pour rendre une copie du site sans `sources/` ; rien n'est écrit dans `_site/` ni `.quarto/` du projet |
| Python | 3.x | figures et scripts |
| PyYAML | 6.x | scripts |
| matplotlib | 3.10 (rendu des figures du ch. 2 de TS227) | figures : `python3 figures/NN-slug.py` écrit le `.svg` voisin |
| LaTeX (TinyTeX ou TeX Live) + dvisvgm | TeX Live 2022, dvisvgm 2.13 (rendu des figures du ch. 2) | schémas TikZ : `latex` dans un dossier temporaire, puis `dvisvgm --no-fonts --exact-bbox` (commande en tête de chaque `.tex`) ; PDF plus tard |
| Git | à préciser | dépôt initialisé (commit `501e006`) ; dépôt GitHub : voir § 10 |

---

## 10. Hébergement

**GitHub Pages, accès public** (décision d'Armand du 25 octobre 2026, `CONTEXTE_PROJET.md` § 5.4). Adresse : https://armandgm43-droid.github.io/bristol-site/ (révisions : `https://armandgm43-droid.github.io/bristol-site/revision/`).

- Construction : `.github/workflows/publier-site.yml`. À chaque push sur `main` (ou bouton « Run workflow » de l'onglet *Actions*), GitHub installe Quarto 1.10.19, lance `quarto render` et publie `_site/`. Aucune cellule de code n'est exécutée : les figures sont versionnées en SVG, Python n'est pas nécessaire.
- Réglage unique sur GitHub : *Settings → Pages → Build and deployment → Source : GitHub Actions*.
- Dépôt **rendu public** par Armand le 27 octobre 2026 (GitHub Pages n'est gratuit que sur un dépôt public). Tout ce qui est versionné est donc lisible, historique compris : ne jamais commiter de contenu personnel ni de source brute (`sources/` reste ignoré par Git). Alternative si le dépôt doit redevenir privé : GitHub Pro (Student Developer Pack) ou Cloudflare Pages.
- Mis en ligne et contrôlé le 27 octobre 2026 (accueil et `revision/cartes/index.json` accessibles).
- Ce qui est publié : uniquement le contenu de `_site/` (pages `.qmd`, `revision/`, `assets/bristol-tokens.css`). Les `.md` de travail et `sources/` (ignoré par Git) ne le sont pas.
- **Progression de révision** : liée à l'adresse (`localStorage`). Celle de `localhost:4848` ne se transfère pas vers le site publié (voir `ETAT_PROJET.md`, problème 17).
- `quarto preview` (port 4848) reste utilisable en local.

### Dépôts GitHub

| Dépôt | Visibilité | Contenu | Remarque |
|---|---|---|---|
| `armandgm43-droid/bristol-site` | **public** depuis le 27 octobre 2026 (GitHub Pages) | **dépôt du projet** : ce dossier (site Quarto, application dans `revision/`, fichiers de mémoire) | dépôt de référence |
| `armandgm43-droid/bristol` | public (GitHub Pages) | **ancien site de cartes** (application de révision seule) | **figé** depuis le 7 octobre 2026 : plus aucune modification ; **ne pas confondre** avec le dépôt du projet |

La révision se fait désormais en local (§ 6). L'ancien dépôt `bristol` n'est plus mis à jour ; son sort (archiver, supprimer) pourra être décidé avec la question ouverte 2.
