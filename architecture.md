# Bristol — Architecture technique

> Détails techniques du projet : configuration Quarto, structure des dossiers, application de révision, scripts, build, hébergement.
> Les choix de fond sont dans `CONTEXTE_PROJET.md` (section 5) ; les règles d'écriture dans `conventions.md`.
>
> Dernière mise à jour : 6 octobre 2026.

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
                    (à écrire)                     │
                                                   ▼
                                     revision/index.html (application)
```

---

## 2. Structure des dossiers (état réel au 6 octobre 2026)

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
│   └── bristol.scss          thème : polices, couleurs, styles des quatre catégories
├── matieres/
│   └── ts227-communications-numeriques/
│       ├── index.qmd         fiche matière
│       ├── cours/  figures/  flashcards/  td/  tp/  annales/  corriges/   (vides)
├── revision/
│   ├── index.html            application de flashcards (fichier unique)
│   └── cartes/
│       ├── index.json        liste des paquets à charger
│       └── *.json            paquets (6 paquets hérités)
├── scripts/                  (vide)
└── sources/                  sources brutes, ignorées par Git
    └── LISEZMOI.txt
```

Fichiers générés, jamais versionnés : `_site/`, `.quarto/`, `*_files/`, `*_cache/`.

---

## 3. Configuration Quarto (`_quarto.yml`)

| Réglage | Valeur | Rôle |
|---|---|---|
| `project.type` | `website` | site statique |
| `project.output-dir` | `_site` | dossier de sortie |
| `project.render` | `*.qmd`, `matieres/**/*.qmd` | seuls les `.qmd` deviennent des pages ; les `.md` restent des documents de travail |
| `project.resources` | `revision/**` | l'application de révision est copiée telle quelle |
| `lang` | `fr` | titres d'environnements et libellés en français |
| `website.search` | `true` | recherche plein texte côté navigateur |
| `website.navbar` | Matières, Révisions, Conventions | barre de navigation |
| `website.sidebar` | une barre par matière (`id: ts227`) | les chapitres y sont ajoutés à la main, dans l'ordre |
| `format.html.theme` | `cosmo` + `assets/bristol.scss` | thème |
| `format.html.html-math-method` | `mathjax` | rendu des maths (MathJax 3) |
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

## 4. Thème et styles (`assets/bristol.scss`)

- Polices : *Atkinson Hyperlegible* (texte) et *Literata* (titres), chargées depuis **Google Fonts** (connexion nécessaire ; sinon repli sur les polices système).
- Couleurs des catégories : bleu encre `#23489A` (notes), gris `#7E889B` (complément), orange `#C2610C` (à vérifier).
- Blocs `div.notes`, `div.complement`, `div.a-verifier` : filet à gauche + étiquette en `::before` + fond teinté. Segments `span.…` : couleur + symbole.
- Impression (`@media print`) : mêmes repères, sans fond.
- **Rendu PDF (LaTeX) : pas encore fait.** Il faudra un filtre Lua ou des environnements LaTeX (`tcolorbox`) qui reproduisent filet et étiquette.

---

## 5. Macros (`_macros.qmd`)

- Bloc `$$ \newcommand… $$` dans un div `.hidden`, inclus en haut de chaque page par `{{< include /_macros.qmd >}}`.
- Fonctionne pour le HTML (MathJax). Pour le PDF, il faudra aussi injecter les macros dans l'en-tête LaTeX (`include-in-header`).
- L'application de révision ne lit pas ce fichier : le script de conversion des flashcards devra soit développer les macros, soit les déclarer dans la configuration MathJax de l'application.

---

## 6. Application de révision (`revision/`)

- **Fichier unique** `index.html` (HTML + CSS + JS, ~86 ko), sans build.
- Maths : MathJax 3.2.2 (`tex-svg`) chargé depuis `cdn.jsdelivr.net`.
- Progression : `localStorage`, clé `bristol:v1` (format `{ v: 1, decks }`). Elle est **propre au navigateur et à l'adresse du site** : changer d'hébergement ou de domaine repart d'une progression vide, sauf export puis import.
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
| `ts227.json` | Communications numériques (TS227) | 129 | `ts-` |

---

## 7. Scripts (`scripts/`, à écrire)

Langage : **Python 3** avec **PyYAML** (seule dépendance prévue).

| Script | Rôle |
|---|---|
| `flashcards.py` | Convertit `matieres/*/flashcards/*.yml` en `revision/cartes/<matiere>.json` et met à jour `cartes/index.json` |
| `verifier.py` | Vérifications : front matter complet et statut valide ; labels uniques dans la matière ; `ref` des cartes qui pointent vers un label existant ; identifiants de cartes uniques dans la matière et absents de tous les `ids-retires` de la matière ; types de cartes valides ; astérisques isolés ; liste des blocs `#av-…` restants |

Le script de vérification sera lancé avant chaque commit (à la main, puis éventuellement en *pre-commit hook*).

---

## 8. Build et commandes

| Commande | Effet |
|---|---|
| `quarto preview` | aperçu local, rechargé à chaque modification |
| `quarto render` | génère le site complet dans `_site/` |
| `python scripts/flashcards.py` | (à venir) régénère les paquets de cartes |
| `python scripts/verifier.py` | (à venir) vérifications automatiques |

Pour un site de plusieurs centaines de pages : rendu d'un seul fichier (`quarto render chemin/fichier.qmd`) pendant la rédaction, et `freeze: auto` dès que des figures sont calculées en Python dans les pages.

---

## 9. Dépendances

| Outil | Version | Remarque |
|---|---|---|
| Quarto | **à préciser** | installé sur le PC d'Armand |
| Python | 3.x | figures et scripts |
| PyYAML | 6.x | scripts |
| matplotlib | à préciser | figures |
| LaTeX (TinyTeX ou TeX Live) | à préciser | PDF et TikZ, plus tard |
| Git | à préciser | dépôt pas encore initialisé |

---

## 10. Hébergement

**Non décidé** (question ouverte 1 de `CONTEXTE_PROJET.md`). En attendant : **utilisation locale uniquement** (`quarto preview`), conformément à la règle « pas de publication avant clarification des droits ».

L'application de révision est aujourd'hui hébergée sur GitHub Pages, depuis le dépôt GitHub d'Armand ; ce dossier-ci n'est pas encore un dépôt Git. L'organisation en un ou deux dépôts reste à trancher (question ouverte 2).
