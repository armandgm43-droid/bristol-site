# Bristol — Conventions

> Règles détaillées de rédaction, de mise en forme et de nommage.
> À lire avec `CONTEXTE_PROJET.md` (le *pourquoi*) et `ETAT_PROJET.md` (l'état du projet).
> Ces conventions s'appliquent à **toutes les matières**. Ce qui est propre à une matière (notations, convention de la TF…) va dans sa fiche matière, pas ici.
>
> Dernière mise à jour : 7 octobre 2026.

Toute nouvelle convention est **proposée explicitement** avant d'être appliquée, puis ajoutée ici et dans le [journal des conventions](#12-journal-des-conventions).

---

## 1. Langue et style

- Langue : **français**. Les termes techniques anglais usuels sont gardés quand le cours les emploie (*matched filter*, *eye diagram*…), en italique à leur première apparition.
- Ton neutre de manuel. Pas de « on va voir que… » en cascade, pas de familiarités.
- Typographie française : espace insécable avant `: ; ! ?` et dans « », virgule décimale dans le texte (« 0,5 »).
- Dans les formules, la virgule décimale s'écrit `0{,}5` (sinon LaTeX ajoute une espace).
- Unités : espace entre la valeur et l'unité (`10 kHz`, `$10\ \mathrm{kHz}$`).

---

## 2. Nommage des fichiers et dossiers

Règle générale : **minuscules, sans accents, mots séparés par des tirets**. Pas d'espace, pas de majuscule.

| Élément | Format | Exemple |
|---|---|---|
| Dossier de matière | `<code>-<intitule>` | `matieres/ts227-communications-numeriques/` |
| Code de matière (`<code>`) | code officiel en minuscules, ou code court explicite | `ts227` |
| Chapitre | `cours/NN-slug.qmd` | `cours/03-dsp-signaux-codes-en-ligne.qmd` |
| Flashcards d'un chapitre | `flashcards/NN-slug.yml` (même nom que le chapitre) | `flashcards/03-dsp-signaux-codes-en-ligne.yml` |
| Figure (source) | `figures/NN-slug-figure.py` ou `.tex` | `figures/03-dsp-nrz.py` |
| Figure (rendu) | même nom, `.svg` | `figures/03-dsp-nrz.svg` |
| TD, TP, annales (phase 2, provisoire) | `td/tdNN-slug.qmd`, `tp/tpNN-slug.qmd`, `annales/AAAA-session.qmd` | `td/td01-bande-de-base.qmd`, `annales/2025-janvier.qmd` |
| Sources brutes (hors dépôt) | `sources/<code>/support/…`, `sources/<code>/notes/AAAA-MM-JJ.pdf` | `sources/ts227/notes/2026-09-15.pdf` |
| Notes sans date de séance (hors dépôt) | `sources/<code>/notes/date-inconnue.pdf`, photos dans `sources/<code>/notes/date-inconnue/feuillet-N-recto.jpg` / `-verso.jpg` | `sources/ts227/notes/date-inconnue.pdf` |
| Rapport d'analyse d'un chapitre | `analyses/NN-slug.md` (même slug que le chapitre ; `.md`, donc non rendu par Quarto) | `matieres/ts227-communications-numeriques/analyses/02-communication-sans-bruit.md` |

- `NN` : numéro sur deux chiffres (`01`, `02`…).
- Le slug du chapitre décrit son contenu en 2 à 5 mots.
- **Un fichier publié n'est jamais renommé** (voir `CONTEXTE_PROJET.md`, section 4.3). Si c'est indispensable : redirection + note dans `ETAT_PROJET.md`.
- Les notes manuscrites sont nommées par **date de séance**, un PDF par séance. Si la date est inconnue : `date-inconnue.pdf`, pages dans l'ordre des feuillets (recto puis verso), les photos d'origine étant gardées dans `date-inconnue/`.

---

## 3. Front matter

### 3.1 Chapitre

Chaque chapitre commence par ce bloc YAML. Les champs marqués *obligatoire* doivent toujours être présents.

```yaml
---
title: "DSP des signaux codés en ligne"       # obligatoire
matiere: ts227                                # obligatoire : code de la matière
chapitre: 3                                   # obligatoire : numéro (entier)
enseignants: ["Romain Tajan"]                 # obligatoire
annee: "2026-2027"                            # obligatoire : année universitaire
statut: brouillon                             # obligatoire : voir section 4
date-modified: 2026-10-06                     # obligatoire : AAAA-MM-JJ
sources:                                      # obligatoire : au moins une source
  - id: poly                                  # identifiant court, utilisé pour citer
    fichier: poly_ts227.pdf
    nature: officielle                        # officielle | personnelle | externe
    version: "2025-10-09"
    pages: "60-95"
  - id: notes-2026-09-22
    fichier: notes/2026-09-22.pdf
    nature: personnelle
    seance: 2026-09-22
    pages: "1-6"
---

{{< include /_macros.qmd >}}
```

- `date-modified` est un champ standard de Quarto : il est affiché sur la page.
- L'`id` d'une source sert à la citer dans le texte : `[poly, p. 78]`, `[notes-2026-09-22, p. 3]`.
- **Numéros de page** : toujours ceux **du PDF** (1 à N), jamais les numéros imprimés sur les diapositives (« 36/161 »).
- Notes sans date : `seance: inconnue`, `id: notes` (ou `notes-…` s'il y en a plusieurs), et citation par feuillet : `[notes, f. 1 v°]`.
- La ligne `{{< include /_macros.qmd >}}` suit **toujours** le front matter.

### 3.2 Fiche matière (`index.qmd`)

```yaml
---
title: "TS227 — Introduction aux communications numériques"
subtitle: "Fiche matière"
matiere: ts227
enseignants: ["Romain Tajan"]
annee: "2026-2027"
number-sections: false
---
```

Contenu de la page : voir `CONTEXTE_PROJET.md`, section 6.6. La table des notations et les conventions propres à la matière (signe de la TF, étiquetage des constellations…) y sont obligatoires.

---

## 4. Statuts des chapitres

Le champ `statut` prend une valeur **en minuscules, sans accents**, pour pouvoir être lu par des scripts.

| Valeur du champ | Affichage | Signification |
|---|---|---|
| `brouillon` | BROUILLON | Sources reçues, rien n'est encore rédigé |
| `analyse` | ANALYSÉ | Rapport d'analyse produit, questions posées |
| `redige` | RÉDIGÉ | Cours reconstruit, figures intégrées |
| `verifie` | VÉRIFIÉ | Relecture et vérifications de Claude faites |
| `valide` | VALIDÉ | Relu et validé par Armand |
| `flashcards` | FLASHCARDS GÉNÉRÉES | Cartes produites à partir du cours validé |

Un retour en arrière est explicite et noté dans `ETAT_PROJET.md`.

---

## 5. Les quatre catégories

Classes **figées** (déjà stylées dans `assets/bristol.scss`, couleurs tirées des jetons `--cat-…` de `assets/bristol-tokens.css`, voir § 13) :

| Catégorie | Classe | Bloc | Segment dans une phrase |
|---|---|---|---|
| Support officiel | *(aucune)* | texte normal | texte normal |
| Notes de cours | `.notes` | `::: {.notes}` | `[texte]{.notes}` |
| Complément | `.complement` | `::: {.complement}` | `[texte]{.complement}` |
| À vérifier | `.a-verifier` | `::: {.a-verifier #av-slug}` ; tranché : `::: {.a-verifier .tranche #av-slug}` (§ 5.2) | `[texte]{.a-verifier}` |

### 5.1 Règles d'usage

- **Préférer les blocs.** Une démonstration faite au tableau forme un bloc entier. Les segments sont réservés à quelques mots insérés dans une phrase du support.
- Un bloc peut contenir des équations, des figures, des listes et des environnements (démonstration, exemple…).
- Pour imbriquer, l'enveloppe extérieure prend **plus de deux-points** que l'intérieure :

  ```markdown
  :::: {.notes}
  ::: {.proof}
  On part de l'autocorrélation moyennée…
  :::
  ::::
  ```

- Ne jamais imbriquer deux catégories (pas de `.complement` dans `.notes`) : fermer le premier bloc, ouvrir le second.

### 5.2 Bloc *À vérifier*

Chaque bloc *À vérifier* porte un **identifiant** `#av-<slug>`, unique dans la matière. Il permet de le citer dans `ETAT_PROJET.md` et de compter les blocs restants par script.

Contenu obligatoire, dans cet ordre :

```markdown
::: {.a-verifier #av-variance-affine}
**Source** [poly, p. 78] : « $Y \sim \mathcal{N}(a\mu + b,\ b^2\sigma^2)$ ».

**Problème** : la variance d'une transformation affine est $a^2\sigma^2$.

**Proposition** : $Y \sim \mathcal{N}(a\mu + b,\ a^2\sigma^2)$.
:::
```

- Citer la source **fidèlement**, sans la corriger.
- La *Proposition* est facultative si aucune correction fiable n'est possible.
- Une question tranchée par Armand se traite de deux façons :
  - **la source est corrigée** (coquille, erreur de formule, de réponse…) : le bloc **reste visible** et devient un bloc *tranché*, avec la classe `.tranche` et une quatrième partie **Décision**. Une correction de source n'est jamais silencieuse ;
  - **ce n'était pas une erreur** (lecture incertaine confirmée, condition simplement manquante…) : le bloc disparaît, son contenu est réintégré dans la bonne catégorie (texte normal, `.notes` ou `.complement`).
- Dans les deux cas, l'identifiant `av-…` n'est jamais réutilisé, et la décision est notée dans le rapport d'analyse du chapitre (et dans `ETAT_PROJET.md` si elle est importante).
- Un bloc **ouvert** est un bloc `.a-verifier` sans `.tranche` : c'est ce que comptent les scripts.

```markdown
::: {.a-verifier .tranche #av-centre-symetrie-nyquist}
**Source** [poly, p. 41] : « Le point $(\frac{1}{2T_s}, \frac{g_0}{2})$ est un centre de symétrie pour $G(f)$ ».

**Problème** : avec $\frac{1}{T_s}\sum_m G(f - m/T_s) = g_0$, l'ordonnée du centre est $g_0 T_s/2$.

**Proposition** : $(\frac{1}{2T_s}, \frac{g_0 T_s}{2})$.

**Décision** : correction retenue par Armand (2026-10-07).
:::
```

- Rendu d'un bloc tranché (`assets/bristol.scss`, jetons `--cat-verifier…`, clair et sombre) : étiquette **`✓ Corrigé`** au lieu de `? À vérifier`, filet de 2 px au lieu de 4 px, fond deux fois plus pâle, même famille de couleur. Exemple : `demo-conventions.qmd`.

### 5.3 Fautes d'orthographe des sources

- Une faute d'orthographe ou de typographie **sans effet sur le sens** (accord, accent, mot manquant évident dans un titre, nom propre mal orthographié dans les notes) est corrigée **sans bloc**.
- Chaque correction de ce type est **listée dans le rapport d'analyse** du chapitre (source, texte d'origine, texte corrigé).
- Tout ce qui touche au sens (formule, valeur, unité, réponse, définition) reste traité en *À vérifier*.

---

## 6. Environnements de cours

On utilise les environnements natifs de Quarto. Les titres s'affichent en français grâce à `lang: fr`.

| Contenu | Syntaxe | Numéroté |
|---|---|---|
| Définition | `::: {#def-slug}` | oui |
| Théorème | `::: {#thm-slug}` | oui |
| Propriété | `::: {#prp-slug}` | oui |
| Lemme | `::: {#lem-slug}` | oui |
| Corollaire | `::: {#cor-slug}` | oui |
| Exemple | `::: {#exm-slug}` | oui |
| Exercice | `::: {#exr-slug}` | oui |
| Démonstration | `::: {.proof}` | non |
| Remarque | `::: {.remark}` | non |
| Solution d'exercice | `::: {.solution}` | non |

- Le nom de l'environnement s'écrit en titre de niveau 2 à l'intérieur du bloc :

  ```markdown
  ::: {#def-cyclostationnaire}
  ## Processus cyclostationnaire

  Un processus est cyclostationnaire de période $\Ts$ si…
  :::
  ```

- Ne pas utiliser les *callouts* Quarto (`.callout-…`) pour le contenu de cours : leurs couleurs se confondraient avec les quatre catégories.
- Chaque chapitre se termine par une section `## À retenir` : liste des résultats et formules, **avec leurs conditions d'application**, et liens vers leur label.

---

## 7. Labels et références croisées

### 7.1 Format

`<préfixe>-<slug>`, en minuscules, sans accents, mots séparés par des tirets.

| Préfixe | Objet |
|---|---|
| `sec-` | section |
| `eq-` | équation |
| `fig-` | figure |
| `tbl-` | tableau |
| `def-`, `thm-`, `prp-`, `lem-`, `cor-`, `exm-`, `exr-` | environnements (section 6) |
| `av-` | bloc *À vérifier* (ancre simple, pas une référence Quarto) |

Exemples : `eq-bennett`, `fig-diagramme-oeil-nrz`, `def-filtre-adapte`, `sec-critere-nyquist`.

### 7.2 Règles

- Un label est **unique dans toute la matière** (pas seulement dans le chapitre), pour que les liens entre chapitres et les références des flashcards restent sans ambiguïté.
- Le slug décrit l'objet, **pas sa position** : pas de numéro de chapitre ni d'ordre (`eq-bennett`, pas `eq-3-12`).
- **Un label n'est jamais renommé** : les flashcards et les autres chapitres pointent dessus.
- Toute section de niveau 2 reçoit un label `{#sec-…}`. Les sections de niveau 3 en reçoivent un si on y renvoie.
- On ne labellise une équation que si elle est citée ailleurs, reprise dans « À retenir » ou visée par une flashcard.

### 7.3 Références

- Dans le même chapitre : `@eq-bennett`, `@def-filtre-adapte`, `@sec-critere-nyquist` (lien et numéro générés par Quarto).
- Vers un autre chapitre (Quarto ne résout pas `@` entre pages d'un site) : lien Markdown explicite, `[formule de Bennett](03-dsp-signaux-codes-en-ligne.qmd#eq-bennett)`.

---

## 8. Écriture mathématique

- En ligne : `$…$`. Centrée : `$$…$$`, suivie si besoin de son label : `$$ … $$ {#eq-slug}`.
- Macros communes : définies **uniquement** dans `_macros.qmd`, jamais redéfinies dans une page. Une nouvelle macro y est ajoutée et listée ci-dessous.

| Macro | Rendu | Usage |
|---|---|---|
| `\Ts` | $T_s$ | durée symbole |
| `\Tb` | $T_b$ | durée bit |
| `\E` | $\mathbb{E}$ | espérance |
| `\sinc` | $\operatorname{sinc}$ | sinus cardinal |
| `\TF` | $\operatorname{TF}$ | transformée de Fourier |

- Unité imaginaire : $j$. Différentielle : `\mathrm{d}t`. Indices textuels en romain : `E_\mathrm{b}` seulement si le support le fait ; sinon on suit le support (`E_b`).
- Convention de signe de la TF, définition de $\sinc$ (avec ou sans $\pi$) : **propres à chaque matière**, fixées dans la fiche matière.
- Toute formule importante est accompagnée de ses **conditions d'application** juste après (ou dans l'environnement qui la contient).

---

## 9. Figures

- Inclusion : `![Légende.](../figures/03-dsp-nrz.svg){#fig-dsp-nrz}`.
- Format publié : **SVG**. Les sources (`.py`, `.tex`) sont versionnées à côté du rendu ; une figure doit pouvoir être régénérée.
- Légende : une phrase de description, puis l'origine, selon `CONTEXTE_PROJET.md`, section 9.3 :
  - « D'après le support [poly, p. X]. »
  - « D'après les notes de cours [notes-AAAA-MM-JJ, p. Y], redessinée. »
  - « Reconstruite : … ajouté (en pointillés gris). »
- Éléments ajoutés par rapport à la source : **pointillés gris `#7E889B`** (la couleur de la catégorie *Complément* en mode clair, jeton `--cat-complement`). Les figures SVG gardent cette valeur fixe : elles ne changent pas avec le mode sombre, où elles sont posées sur un fond blanc (jeton `--figure-bg`, § 13).
- Courbes Python : matplotlib, police sans empattement, texte en français, axes titrés avec unités, export `svg`.

---

## 10. Flashcards

### 10.1 Fichier

Un fichier YAML par chapitre : `flashcards/NN-slug.yml`, même nom que le chapitre.

```yaml
matiere: ts227
chapitre: 3
cours: cours/03-dsp-signaux-codes-en-ligne.qmd
ids-retires: []          # identifiants supprimés : ne jamais les réutiliser
cartes:
  - id: ts227-bennett-conditions
    type: formule
    question: |
      Expression de la formule de Bennett, et hypothèses nécessaires ?
    reponse: |
      $$\Gamma_{s_l}(f) = \frac{|H(f)|^2}{\Ts} \sum_m R_A[m]\, e^{-j2\pi f m \Ts}$$
      Symboles formant un processus stationnaire à temps discret, mis en forme
      par un filtre linéaire invariant $h(t)$, au rythme $1/\Ts$.
    ref: eq-bennett
    source: officiel     # facultatif : officiel | notes | complement
    tags: [dsp]          # facultatif
```

| Champ | Obligatoire | Contenu |
|---|---|---|
| `id` | oui | identifiant persistant (10.3) |
| `type` | oui | voir 10.2 |
| `question` | oui | recto |
| `reponse` | oui | verso |
| `ref` | oui | label du passage du cours dans le chapitre du fichier (`eq-…`, `def-…`, `sec-…`). Vers un autre chapitre : `NN-slug.qmd#label` |
| `source` | non | catégorie d'origine du contenu |
| `tags` | non | mots-clés libres |

La matière et le chapitre sont déclarés **une fois en tête de fichier** et valent pour toutes les cartes.

### 10.2 Types

`definition`, `formule`, `condition`, `propriete`, `methode`, `raisonnement`, `piege`, `relation`, `resultat`, `exercice`.

### 10.3 Identifiants

- Format : `<matiere>-<slug>`, par exemple `ts227-bennett-conditions`.
- **Pas de numéro de chapitre** : comme les labels, l'identifiant décrit la notion visée (slug de 2 à 5 mots), pas sa position.
- Un identifiant est **unique dans toute la matière**, tous chapitres confondus.
- Une carte **modifiée garde son identifiant**. Une carte supprimée voit son identifiant ajouté à `ids-retires` du fichier où elle se trouvait ; il n'est **jamais réutilisé**, dans aucun chapitre de la matière.
- Une carte qui change de chapitre passe dans le fichier du nouveau chapitre et garde son identifiant (sans l'ajouter à `ids-retires`).
- Les préfixes des paquets hérités (`ts-`, `res-`, `ang-`, `vhdl-`, `cu-`, `latex-`) sont réservés à ces paquets.

### 10.4 Rédaction

- Une seule notion par carte ; la question oblige à **retrouver** la réponse.
- Réponse courte ; le lien vers le cours sert à approfondir.
- Mise en forme autorisée (celle de l'application de révision) : `**gras**`, `*italique*`, `` `code` ``, `$…$`, `$$…$$`.
- En dehors du code et des formules, **jamais d'astérisque isolé** sur une ligne (il serait pris pour de l'italique).
- En YAML, écrire `question` et `reponse` en bloc `|` : les antislashs du LaTeX n'ont alors pas à être doublés.
- Les macros de `_macros.qmd` (`\Ts`, `\Tb`, `\TF`…) s'écrivent dans les cartes **comme dans le cours** : l'application de révision ne les connaît pas, mais `scripts/flashcards.py` les développe à la conversion.
- Une formule en ligne `$…$` tient sur **une seule ligne** (l'application ne reconnaît pas une formule en ligne coupée) ; le script le contrôle.
- Sauts de ligne, comme en Markdown : les lignes d'un même paragraphe sont jointes par le script. Une nouvelle ligne commence devant une ligne `- …` (liste) et autour d'un bloc `$$…$$` ; une ligne vide sépare deux paragraphes.
- Typographie du cours : espace insécable avant `: ; ! ?`.

### 10.5 Conversion vers l'application

`python scripts/flashcards.py` produit un paquet par matière, `revision/cartes/<matiere>.json`, au format de l'application : `key` ← `id`, `chap` ← « Ch. NN — titre » (titre du front matter du chapitre), `front` ← `question`, `back` ← `reponse`, `deck` ← titre de la fiche matière. Les cartes sont écrites dans l'ordre des chapitres, puis dans l'ordre des fichiers. Le fichier de la matière est ajouté à `revision/cartes/index.json` s'il n'y figure pas.

Le script **n'écrit rien** au moindre problème : champ obligatoire manquant ou inconnu, identifiant non conforme, en double ou présent dans un `ids-retires` de la matière, préfixe hérité, type ou source inconnus, `ref` introuvable dans le chapitre visé, astérisque isolé, formule en ligne coupée. `--verifier` fait les contrôles sans écrire. Détails : `architecture.md` § 7.

Le paquet généré est le **contenu complet** de la matière : ne jamais le modifier à la main (la modification serait écrasée au lancement suivant).

---

## 11. Git

- Messages au format *Conventional Commits*, en anglais : `feat:`, `fix:`, `docs:`, `refactor:`, `chore:`.
- Portée facultative entre parenthèses : `feat(ts227): add chapter 2`.
- Un commit = une étape logique. Les sources brutes ne sont jamais commitées (`sources/` est dans `.gitignore`).

---

## 12. Journal des conventions

| Date | Convention | Remarque |
|---|---|---|
| 2026-10-06 | Classes `.notes`, `.complement`, `.a-verifier` figées | Celles proposées dans le contexte, déjà stylées |
| 2026-10-06 | Identifiant `#av-slug` obligatoire sur les blocs *À vérifier* | Nouveau : suivi et comptage |
| 2026-10-06 | Front matter des chapitres (section 3) avec `id` par source | Nouveau : `id` pour citer les sources |
| 2026-10-06 | Statuts en minuscules sans accents | Lisibles par script |
| 2026-10-06 | Labels uniques dans la matière, sans numéro | |
| 2026-10-06 | Flashcards en YAML, un fichier par chapitre, matière et chapitre en tête de fichier, `ids-retires` | Proposition du contexte, précisée |
| 2026-10-06 | Identifiants de cartes `<matiere>-<slug>`, uniques dans la matière, sans numéro de chapitre | Modifie la proposition du contexte (`<matiere>-c<NN>-<slug>`) |
| 2026-10-06 | Macros dans `_macros.qmd` (et non `_macros.tex`) | Fichier existant |
| 2026-10-06 | Pas de callouts Quarto pour le contenu ; section « À retenir » en fin de chapitre | |
| 2026-10-07 | Pages citées : numérotation du PDF | Rapport d'analyse TS227 ch. 2, Q8 |
| 2026-10-07 | Notes sans date : `date-inconnue.pdf`, `seance: inconnue`, citation par feuillet | Rapport ch. 2, décision 13.1 |
| 2026-10-07 | Rapports d'analyse dans `matieres/<matiere>/analyses/NN-slug.md` | Rapport ch. 2, Q14 |
| 2026-10-07 | Blocs *À vérifier* tranchés : classe `.tranche` + **Décision**, toujours visibles quand la source est corrigée | Modifie la règle « un bloc levé disparaît » ; rendu `✓ Corrigé` à styler |
| 2026-10-07 | Fautes d'orthographe sans effet sur le sens corrigées sans bloc, listées dans le rapport d'analyse | Nouveau (§ 5.3) |
| 2026-10-07 | Direction artistique unique « fiche bristol » pour le site et l'application ; jetons dans `assets/bristol-tokens.css` ; mode sombre | Nouveau (§ 13) |
| 2026-10-07 | Choix par défaut appliqués par Claude (forme, figures, rédaction) et listés dans le rapport ; questions à Armand réservées aux points bloquants | Nouveau (§ 14), décision d'Armand après la vérification du ch. 2 de TS227 |
| 2026-10-07 | Flashcards : macros écrites comme dans le cours (développées par le script), formules en ligne sur une ligne, sauts de ligne façon Markdown ; conversion par `scripts/flashcards.py` | Précise § 10.4 et § 10.5 (remplace « écrire la forme développée ») |
| 2026-10-07 | Paquet TS227 provisoire (préfixe `ts-`) abandonné ; le préfixe reste réservé | Question ouverte 5 |

---

## 13. Direction artistique

Une seule direction artistique pour le site Quarto et l'application de révision : **une fiche bristol posée sur un bureau**. Elle vient de l'application ; le site l'a reprise le 7 octobre 2026.

### 13.1 Source unique : les jetons

- Toutes les couleurs, polices, tailles de texte et espacements partagés sont définis **une seule fois**, sous forme de variables CSS (« jetons »), dans `assets/bristol-tokens.css`.
- `assets/bristol.scss` (thème Quarto) et `revision/index.html` (application) n'écrivent **aucune couleur en dur** : ils utilisent `var(--…)`.
- Changer une couleur = modifier le jeton, à un seul endroit. Ajouter un jeton = l'ajouter dans ce fichier, avec un commentaire, puis le signaler ici.
- Exception assumée : les figures SVG (§ 9) gardent leurs couleurs fixes ; en mode sombre, elles sont affichées sur un fond blanc avec une marge (`--figure-bg`, `--figure-pad`), comme une fiche posée sur la feuille.

### 13.2 Métaphore et surfaces

| Surface | Jetons | Où | Mode clair | Mode sombre |
|---|---|---|---|---|
| **Bureau** | `--desk`, `--desk-ink`, `--desk-muted`, `--desk-pen`, `--desk-line` | fond de page, barre de navigation, barres latérales, sommaire | gris-bleu `#E2E7ED` | bleu nuit `#1B2231` |
| **Feuille** | `--paper`, `--ink`, `--ink-soft`, `--ink-faint`, `--pen`, `--field…` | contenu d'une page du site, liste des paquets, dialogues | blanc | feuille sombre `#232B3B` |
| **Fiche** | `--card-ink…`, `--card-rule-blue`, teinte du paquet | cartes de révision | papier clair | **reste en papier clair** |

Repères graphiques, communs au site et à l'application :

- **ligne rouge** (`--rule-red`, épaisseur `--rule-red-width`) : sous le titre d'une page ou d'une feuille, sous le mot « Bristol » et sous le lien actif de la barre de navigation ;
- **lignes bleues** (`--rule-blue`) : sous les titres de section, entre les lignes d'un tableau ou d'une liste, comme les lignes d'une fiche ;
- **bleu encre** (`--pen`) : liens et actions.

### 13.3 Typographie et espacements

| Rôle | Jeton | Valeur |
|---|---|---|
| Titres, noms de paquets, texte des cartes | `--serif` | *Literata* |
| Texte courant, interface | `--sans` | *Atkinson Hyperlegible* |
| Code | `--mono` | police à chasse fixe du système |
| Taille de référence (1 rem) | `--font-size-root` | 16 px, identique site et application |
| Texte des pages de cours | `--font-size-reading` | 1,0625 rem (17 px) |
| Liens de la barre de navigation | `--font-size-nav` | 0,95 rem |
| Espacements | `--space-1` à `--space-7` | 0,25 / 0,5 / 0,75 / 1 / 1,5 / 2 / 3 rem |
| Rayons | `--radius-paper`, `--radius-control` | 4 px (feuilles, fiches), 6 px (boutons, champs) |
| Barre de navigation | `--nav-height` | 3,5 rem |

Les polices sont chargées depuis Google Fonts par `assets/bristol-tokens.css` (une seule déclaration pour les deux).

### 13.4 Les quatre catégories

Formes, étiquettes et symboles **inchangés** (§ 5) : filet plein bleu `✎ Notes de cours`, filet gris pointillé `+ Complément`, filet orange `? À vérifier`.

| Catégorie | Jetons | Mode clair | Mode sombre |
|---|---|---|---|
| Notes de cours | `--cat-notes`, `--cat-notes-bg` | `#23489A` (inchangé) | `#A9BFF2` |
| Complément | `--cat-complement`, `--cat-complement-ink`, `--cat-complement-bg` | `#7E889B` / `#5A6478` (inchangés) | `#8792A6` / `#B4BDCC` |
| À vérifier | `--cat-verifier`, `--cat-verifier-bg` | `#C2610C` (inchangé) | `#F0A15C` |

En mode sombre, chaque catégorie garde sa **famille de couleur** (bleu, gris, orange), éclaircie pour rester lisible sur la feuille sombre. Les trois indices redondants (filet, étiquette, fond) sont conservés dans les deux modes.

### 13.5 Mode sombre

- Par défaut, le site et l'application suivent la préférence du système.
- Le bouton clair/sombre de la barre de navigation enregistre un choix explicite dans `localStorage`, clé `quarto-color-scheme` (`alternate` = sombre, `default` = clair) : **le même choix vaut pour le site et pour l'application**.
- Les formules (MathJax) prennent la couleur du texte : elles restent lisibles dans les deux modes.

### 13.6 Barre de navigation commune

- Même dessin sur le site et dans l'application : « Bristol » souligné de rouge (lien vers l'accueil), puis Matières, Révisions, Conventions, et à droite le bouton clair/sombre. L'application y ajoute son indicateur d'enregistrement ; le site, la recherche.
- Les liens de l'application sont écrits dans `revision/index.html` : toute modification de `website.navbar` dans `_quarto.yml` doit y être reportée (voir `architecture.md`, § 6).

---

## 14. Questions à Armand et choix par défaut

Règle fixée par Armand le 7 octobre 2026, valable pour tous les chapitres suivants.

### 14.1 Choix appliqués sans question

Pour les **choix de forme, de figures et de rédaction**, Claude applique lui-même sa réponse par défaut, sans attendre de validation. Exemples :

- plan du chapitre, ordre des notions, découpage en sections ;
- catégorie d'un passage quand elle découle des règles (§ 5 et `CONTEXTE_PROJET.md` § 7) ;
- compléments d'explication (bloc *Complément*) : étape de calcul, hypothèse implicite, nom usuel d'une notion ;
- présentation des quiz en exercices, fautes d'orthographe sans effet sur le sens (§ 5.3) ;
- figures : outil, forme choisie pour une illustration, paramètres d'une simulation, normalisation des axes, fusion ou omission d'une figure redondante.

Chaque choix est **listé dans le rapport d'analyse du chapitre** (section « Choix appliqués par défaut »), avec sa justification, pour qu'Armand puisse le revoir à la validation. Un choix qui concerne une figure est aussi signalé dans sa légende (§ 9).

### 14.2 Questions bloquantes

Claude ne pose à Armand que les questions **bloquantes** :

- **lecture douteuse des notes** : mot, indice, signe, exposant ou schéma illisible ou ambigu ;
- **contradiction entre sources** (support, notes, TD…) ;
- **erreur qui touche au sens** : formule, valeur, unité, réponse de quiz, définition.

Ces points passent toujours par un bloc *À vérifier* tant qu'ils ne sont pas tranchés (§ 5.2). Les règles de fond ne changent pas : ne rien inventer, ne rien corriger silencieusement (`CONTEXTE_PROJET.md` § 19). Une information manquante qui ne relève d'aucun de ces trois cas est signalée dans le cours (bloc *Notes de cours* ou *Complément* selon le cas) et dans le rapport, sans question.

