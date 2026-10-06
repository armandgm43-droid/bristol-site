# Bristol — Contexte du projet

> **Document de référence principal du projet.**
> À lire en premier au début de chaque nouvelle conversation, avec `conventions.md` et `ETAT_PROJET.md`.
>
> Phrase de démarrage type :
> « Lis `CONTEXTE_PROJET.md`, `conventions.md` et `ETAT_PROJET.md`, puis reprends le projet à partir de son état actuel. »
>
> Dernière mise à jour : 6 octobre 2026.

---

## Sommaire

0. [Comment utiliser ce document](#0-comment-utiliser-ce-document)
1. [Présentation générale](#1-présentation-générale)
2. [Philosophie du projet](#2-philosophie-du-projet)
3. [Contexte utilisateur](#3-contexte-utilisateur)
4. [Architecture générale du site](#4-architecture-générale-du-site)
5. [Technologie](#5-technologie)
6. [Traitement des cours](#6-traitement-des-cours)
7. [Distinction des sources : les quatre catégories](#7-distinction-des-sources--les-quatre-catégories)
8. [Notes manuscrites](#8-notes-manuscrites)
9. [Figures et schémas](#9-figures-et-schémas)
10. [Flashcards](#10-flashcards)
11. [Workflow d'un chapitre](#11-workflow-dun-chapitre)
12. [Organisation du travail avec Claude](#12-organisation-du-travail-avec-claude)
13. [Fichiers de mémoire du projet](#13-fichiers-de-mémoire-du-projet)
14. [Gestion des conversations](#14-gestion-des-conversations)
15. [Git](#15-git)
16. [Gestion des erreurs et vérification](#16-gestion-des-erreurs-et-vérification)
17. [Statut des chapitres](#17-statut-des-chapitres)
18. [Première matière : TS227](#18-première-matière--ts227)
19. [Règles non négociables](#19-règles-non-négociables)
20. [L'existant : l'application Bristol actuelle](#20-lexistant--lapplication-bristol-actuelle)
21. [Journal des décisions](#21-journal-des-décisions)
22. [Questions ouvertes](#22-questions-ouvertes)
23. [État actuel](#état-actuel)

---

## 0. Comment utiliser ce document

Ce fichier est la **mémoire persistante** du projet. Il décrit le *pourquoi*, le *quoi* et le *comment*, ainsi que les décisions prises. Il doit permettre à une nouvelle conversation de reprendre le projet **sans relire les anciennes conversations**.

Répartition des rôles entre les fichiers de mémoire :

| Fichier | Contenu | Fréquence de mise à jour |
|---|---|---|
| `CONTEXTE_PROJET.md` | Vision, principes, décisions structurantes, méthode | Rare : quand une décision de fond change |
| `conventions.md` | Règles détaillées de rédaction, de mise en forme, de nommage | Quand une convention est ajoutée ou précisée |
| `architecture.md` | Détails techniques : configuration Quarto, scripts, build, hébergement | Quand la technique évolue |
| `ETAT_PROJET.md` | Où en est le projet : fait, en cours, à faire, problèmes connus | À la fin de chaque session de travail |
| `TODO.md` | Liste des tâches concrètes | En continu |

**En cas de contradiction** entre ce document et une conversation, le document fait foi, sauf si Armand indique explicitement qu'une décision a changé. Dans ce cas, mettre à jour ce document (et le [journal des décisions](#21-journal-des-décisions)).

**Pour Claude :** quand une information nécessaire n'est dans aucun des fichiers fournis, la demander à Armand plutôt que de la supposer.

---

## 1. Présentation générale

**Bristol** est un projet personnel d'Armand : une **base de connaissances complète pour ses études d'ingénieur**, utilisable pendant plusieurs années.

Le nom vient des fiches bristol, les fiches cartonnées utilisées pour réviser. Il désigne à l'origine l'application de flashcards du projet (voir [section 20](#20-lexistant--lapplication-bristol-actuelle)) et, désormais, l'ensemble du site.

### Ce que Bristol doit centraliser, à terme

| Ressource | Description | Priorité |
|---|---|---|
| **Cours** | Cours reconstruits à partir des supports officiels et des notes personnelles | **Phase 1** |
| **Flashcards** | Cartes de révision à répétition espacée, générées à partir des cours validés | **Phase 1** |
| TD | Énoncés de travaux dirigés | Phase 2 |
| TP | Énoncés et comptes rendus de travaux pratiques | Phase 2 |
| Annales | Sujets d'examens des années précédentes | Phase 2 |
| Corrigés | Corrections des TD, TP et annales | Phase 2 |
| Autres | Fiches de synthèse, formulaires, ressources externes… | Plus tard |

### Ce que Bristol n'est pas

- Ce n'est **pas un simple dossier de notes** ou un dépôt de PDF.
- Ce n'est **pas un résumé** des supports des enseignants.
- Ce n'est **pas un projet lié à une seule matière** : tout doit être pensé pour des dizaines de matières et plusieurs centaines de chapitres.

### Le problème que Bristol résout

Dans beaucoup de cours, l'enseignant suit un diaporama mais ajoute au tableau des démonstrations, des calculs, des schémas et des remarques qui ne figurent pas dans les slides. Le savoir est donc éclaté entre plusieurs sources incomplètes : slides, polycopié, notes manuscrites, photos du tableau. Les TD utilisent parfois d'autres notations que le cours, certains exercices n'ont pas de corrigé, et les supports contiennent des coquilles.

Bristol reconstruit, pour chaque chapitre, **le cours tel qu'il devrait idéalement exister dans un document unique**, en gardant la trace de l'origine de chaque information, et le relie à des flashcards et (plus tard) aux TD, TP et annales.

---

## 2. Philosophie du projet

Six principes guident toutes les décisions. En cas de doute, revenir à eux.

### 2.1 Exactitude

- Ne **jamais inventer** une information absente des sources.
- Une information ambiguë, illisible ou incertaine est **signalée**, jamais devinée.
- Une erreur dans un cours de révision est pire qu'un manque : elle sera apprise.

### 2.2 Fidélité aux sources

- Les supports officiels et les notes personnelles sont **deux sources distinctes**, conservées comme telles.
- Le but n'est pas de remplacer les supports par une synthèse approximative, mais de **reconstruire un cours plus complet en combinant les sources**.
- Le sens d'une information n'est jamais modifié pour la rendre plus élégante.

### 2.3 Compréhension

- Le résultat doit permettre à **quelqu'un qui n'a pas assisté au cours de comprendre réellement le chapitre** en ne lisant que la version Bristol.
- On peut réorganiser, expliciter, relier les notions entre elles, à condition de respecter les principes d'exactitude et de traçabilité.

### 2.4 Traçabilité

On doit toujours pouvoir savoir, pour chaque élément du cours :

- ce qui vient du **support officiel** ;
- ce qui vient des **notes d'Armand** (tableau, oral) ;
- ce qui a été **reconstruit** (figure redessinée, démonstration complétée) ;
- ce qui a été **ajouté comme complément** par Claude ;
- ce qui reste **incertain**.

C'est le rôle des [quatre catégories](#7-distinction-des-sources--les-quatre-catégories) et des métadonnées de sources de chaque chapitre.

### 2.5 Maintenabilité

- Chaque décision doit fonctionner à l'échelle de **plusieurs années, 20 matières et plusieurs centaines de chapitres**.
- Éviter les solutions rapides qui deviennent ingérables : fichiers géants, liens codés en dur, renommages, conventions implicites.
- Préférer des formats texte simples, versionnés avec Git, et des outils standards.

### 2.6 Réutilisabilité

- Les conventions mises en place pour une matière s'appliquent à **toutes** les autres.
- Tout ce qui est spécifique à une matière (notations, organisation particulière) est documenté dans la page de cette matière, pas dans les conventions générales.

---

## 3. Contexte utilisateur

Seules les informations utiles au projet figurent ici.

- **Armand**, étudiant ingénieur à l'**ENSEIRB-MATMECA (Bordeaux INP)**, filière **Électronique**.
- Année 2026-2027 : 4e année d'études supérieures (équivalent M1), après deux ans de classe préparatoire.
- Domaines d'intérêt : électronique, systèmes embarqués, systèmes électroniques, traitement du signal, communications numériques, informatique.
- Niveau attendu des contenus : école d'ingénieurs. Les rappels de base (probabilités, transformée de Fourier, convolution…) sont utiles quand le cours les fait, mais il ne faut pas vulgariser à l'excès.
- Langue du projet : **français**, avec les termes techniques anglais usuels quand le cours les emploie.
- Bristol accompagne l'**ensemble des études d'ingénieur** d'Armand : il ne doit pas être conçu autour d'une seule matière.

---

## 4. Architecture générale du site

### 4.1 Structure logique

```text
Bristol
└── Matière (ex. TS227 — Introduction aux communications numériques)
    ├── Fiche matière : enseignant(s), année, plan, table des notations
    ├── Cours
    │   ├── Chapitre 1
    │   ├── Chapitre 2
    │   └── ...
    ├── TD          (phase 2)
    ├── TP          (phase 2)
    ├── Annales     (phase 2)
    ├── Corrigés    (phase 2)
    └── Flashcards
```

Les ressources sont reliées entre elles :

- chaque chapitre affiche ses flashcards et, plus tard, les TD, TP et annales qui le concernent ;
- chaque TD, TP ou annale déclare dans ses métadonnées les chapitres qu'il couvre ; les liens sont générés automatiquement, pas écrits à la main ;
- chaque flashcard renvoie au passage exact du cours dont elle est issue.

### 4.2 Organisation des fichiers (envisagée)

```text
bristol/
├── _quarto.yml               # configuration du site : navigation, thème, options
├── CONTEXTE_PROJET.md        # ce document
├── conventions.md            # règles de rédaction et de mise en forme
├── architecture.md           # détails techniques
├── ETAT_PROJET.md            # état d'avancement
├── TODO.md                   # tâches
├── _macros.qmd               # macros LaTeX communes à tout le site
├── index.qmd                 # page d'accueil
│
├── assets/                   # styles (blocs des quatre catégories), images communes
│
├── matieres/
│   └── ts227-communications-numeriques/
│       ├── index.qmd         # fiche matière + table des notations
│       ├── cours/
│       │   ├── 01-introduction.qmd
│       │   ├── 02-....qmd
│       │   └── ...
│       ├── figures/          # sources (.py, .tex) et rendus (.svg)
│       ├── flashcards/       # un fichier par chapitre
│       ├── td/
│       ├── tp/
│       ├── annales/
│       └── corriges/
│
├── revision/                 # application Bristol (flashcards)
│
└── scripts/                  # conversion des flashcards, vérifications automatiques
```

Les **sources brutes** (PDF des enseignants, scans des notes) ne doivent pas être publiées. Elles restent hors du site publié, et idéalement hors de tout dépôt public (voir [section 5.4](#54-hébergement-et-droits)).

### 4.3 Règles de nommage

- Dossier de matière : `<code>-<intitule-en-minuscules-sans-accents>`, par exemple `ts227-communications-numeriques`. S'il n'y a pas de code officiel, utiliser un code court explicite.
- Fichier de chapitre : `NN-slug.qmd`, numéro sur deux chiffres, par exemple `03-dsp-signaux-codes-en-ligne.qmd`.
- **Un fichier ou un identifiant publié n'est jamais renommé.** Si un renommage est indispensable, prévoir une redirection et le noter dans `ETAT_PROJET.md`.
- Le détail des règles de nommage (labels, figures, flashcards) est dans `conventions.md`.

Cette architecture **n'est pas définitive**. Si une meilleure organisation est décidée, mettre à jour ce document et le journal des décisions.

---

## 5. Technologie

### 5.1 Décision

**Quarto + Markdown, avec les mathématiques en syntaxe LaTeX**, pour générer un **site statique**.

Les cours sont écrits dans des fichiers `.qmd` (Markdown enrichi). Quarto les transforme en pages HTML, avec navigation, recherche intégrée et rendu des équations par MathJax.

### 5.2 Pourquoi Quarto

| Critère | Ce qu'apporte Quarto |
|---|---|
| Édition | Markdown, simple à écrire et à relire, diff Git lisibles |
| Mathématiques | Syntaxe LaTeX native, rendu MathJax de qualité, équations numérotées |
| Références croisées | `@eq-…`, `@fig-…`, `@sec-…`, `@def-…`, `@thm-…` avec liens automatiques |
| Structure d'un cours | Environnements définition, théorème, proposition, exemple, exercice, démonstration, remarque |
| Figures | Images, SVG, figures calculées en Python, TikZ via extension |
| Navigation | Barre latérale par matière, sommaire de page, liens entre chapitres |
| Recherche | Recherche plein texte intégrée, côté navigateur |
| PDF | Le même source peut produire un PDF de chapitre (via LaTeX) |
| Maintenance | Projet activement maintenu, formats texte, versionnable avec Git |
| Montée en charge | Rendu incrémental et gel des calculs (`freeze`) pour les gros sites |

### 5.3 Solutions écartées et raisons

| Solution | Raison de l'écart |
|---|---|
| LaTeX comme format source, converti en HTML | Excellente typographie en PDF, mais conversion web fragile, navigation et recherche à construire soi-même, édition plus lourde. Les maths en syntaxe LaTeX restent utilisées *dans* le Markdown. |
| MkDocs Material | Très bon pour la documentation, mais références croisées d'équations et de figures moins abouties, pas de figures calculées ni de PDF natifs. Solution de repli crédible. |
| Docusaurus, Astro | Très flexibles mais maintenance lourde (écosystème JavaScript), maths et références croisées par plugins. |
| Obsidian + Quartz | Excellents pour les liens entre notes, moins adaptés à une hiérarchie stricte Matière → Chapitre → Ressources. |

### 5.4 Hébergement et droits

- Le site pourra être hébergé sur **GitHub Pages** (l'application de flashcards l'est déjà) ou sur une autre solution.
- **Attention :** un site GitHub Pages est **public**, même si le dépôt est privé (sauf offre GitHub Enterprise).
- Le site contiendra des contenus dérivés des supports des enseignants (texte, figures). Cela pose une question de **droits** et, potentiellement, de règlement de l'école.
- **Décision : le site de cours ne doit pas être publié tant que la question des droits n'est pas clarifiée.**
- Options identifiées, non tranchées :
  1. demander l'accord des enseignants concernés ;
  2. héberger derrière une authentification (par exemple Cloudflare Pages + Cloudflare Access, qui propose une offre gratuite pour un petit nombre d'utilisateurs) ;
  3. utiliser le site uniquement en local (`quarto preview`) ;
  4. publier seulement les parties qui ne reprennent pas les supports.
- Dans tous les cas, les sources brutes (PDF, scans) ne sont jamais publiées.

### 5.5 Rendu mathématique

- Moteur : **MathJax 3** (par défaut dans Quarto, et déjà utilisé par l'application de flashcards). Une même syntaxe LaTeX fonctionne donc dans le cours et dans les cartes.
- Macros communes (`\Ts`, `\sinc`, `\E`…) : définies **une seule fois** dans `_macros.qmd` (inclus en haut de chaque page par `{{< include /_macros.qmd >}}`) et utilisées partout. Ne pas redéfinir localement une macro existante.

---

## 6. Traitement des cours

C'est le cœur du projet.

### 6.1 Sources possibles

Pour chaque matière, Armand peut fournir :

- **sources officielles** : PDF de l'enseignant, slides, polycopié, énoncés et corrigés officiels ;
- **sources personnelles** : notes manuscrites (scans ou photos), photos du tableau, notes tapées ;
- **autres documents** : documents de camarades, ressources externes (à identifier comme tels).

Chaque source est **inventoriée** dans les métadonnées du chapitre : nom du fichier, version ou date, pages utilisées, nature (officielle ou personnelle).

### 6.2 Objectif : fusionner, pas résumer

Le travail consiste à **fusionner intelligemment** les sources. Il ne faut **surtout pas** se contenter de résumer les slides.

Le cours final doit conserver :

- les définitions ;
- les propriétés, théorèmes et résultats ;
- les **démonstrations**, et en particulier celles faites au tableau ;
- les calculs ;
- les exemples, y compris les quiz du cours quand ils illustrent une notion ;
- les remarques importantes de l'enseignant ;
- les méthodes de résolution ;
- les schémas et figures utiles ;
- les formules **avec leurs conditions d'application** ;
- les mises en garde et erreurs fréquentes.

### 6.3 Ce qui est permis

- **Réorganiser** l'ordre des notions si cela rend le cours plus compréhensible (en restant proche du plan officiel pour garder les repères).
- **Expliciter** une étape de raisonnement implicite, en la marquant comme *Complément* si elle ne figure dans aucune source.
- **Supprimer les vraies redondances** : les slides répétées à l'identique, les pages de plan, les diapositives de quiz sans contenu (« Sortez vos téléphones »).
- **Harmoniser les notations** dans le cours, selon la table des notations de la matière, en signalant les correspondances avec les autres documents.

### 6.4 Ce qui est interdit

- Supprimer une information importante parce qu'elle n'apparaît que dans les notes.
- Fusionner deux affirmations contradictoires en une seule sans le signaler.
- Présenter une reconstruction comme si elle venait de l'enseignant.
- Corriger silencieusement une coquille.

### 6.5 Structure d'un chapitre

Structure indicative, à **adapter au contenu réel** (ne pas la forcer) :

1. Introduction et objectifs du chapitre ;
2. Définitions importantes ;
3. Concepts fondamentaux ;
4. Développements théoriques ;
5. Démonstrations ;
6. Exemples ;
7. Applications ;
8. Résultats et formules à retenir, avec leurs conditions d'application ;
9. Résumé de fin de chapitre.

Chaque chapitre commence par un **en-tête de métadonnées** (front matter YAML), dont le format exact est fixé dans `conventions.md`. Il contient au minimum : titre, matière, numéro de chapitre, enseignant(s), année universitaire, liste des sources utilisées, **statut**, date de dernière mise à jour.

### 6.6 Fiche matière

Chaque matière a une page `index.qmd` contenant :

- intitulé, code, enseignant(s), année, volume horaire si connu ;
- plan des chapitres avec leur statut ;
- **table des notations** de la matière, avec les correspondances entre documents (par exemple cours et TD) ;
- liste des sources disponibles ;
- remarques générales (erreurs connues des supports, particularités).

---

## 7. Distinction des sources : les quatre catégories

Cette distinction doit être **visible directement dans le cours final**, même dans un très gros document. Chaque catégorie combine **trois indices redondants** (couleur, filet, étiquette), pour rester lisible en noir et blanc et accessible à tous.

### 7.1 Support officiel

Contenu provenant directement du support de l'enseignant.

- **Rendu :** texte normal, sans marquage.
- C'est la catégorie par défaut.

### 7.2 Notes de cours

Contenu provenant des prises de notes d'Armand, du tableau ou d'explications orales.

- **Rendu :** bloc avec **filet vertical bleu** (bleu encre) à gauche, étiquette **`✎ Notes de cours`**, fond très légèrement teinté.
- Ce n'est **pas** un encadré secondaire : c'est du contenu de cours à part entière, souvent essentiel (démonstrations, calculs faits au tableau, remarques du professeur, méthodes, exemples supplémentaires, schémas).
- Un bloc de notes peut contenir des équations, des figures et des listes, comme le reste du cours.

### 7.3 Complément

Contenu ajouté ou reconstruit par Claude à partir d'informations suffisamment fiables (connaissances générales du domaine, étape de calcul évidente, figure reconstruite).

- **Rendu :** bloc avec **filet gris en pointillés**, étiquette **`+ Complément`**.
- Doit être clairement identifiable comme **n'étant pas issu des documents fournis**.
- Un complément ne doit jamais contredire une source sans passer par la catégorie *À vérifier*.

### 7.4 À vérifier

Utilisé lorsque :

- une note est illisible ;
- une formule est ambiguë ;
- une incohérence existe dans une source ;
- une information semble erronée (coquille du support, erreur de calcul) ;
- deux sources se contredisent.

- **Rendu :** bloc avec **filet orange**, étiquette **`? À vérifier`**.
- Contenu attendu : ce que dit la source (citée fidèlement, avec sa référence), le problème identifié, et si possible la **correction proposée**, présentée comme une proposition.
- Un bloc *À vérifier* est **levé** une fois la question tranchée par Armand : le contenu est alors réintégré dans la bonne catégorie, et la décision notée dans `ETAT_PROJET.md` si elle est importante.

### 7.5 Mise en œuvre

Dans les fichiers `.qmd`, les catégories s'écrivent avec des blocs (divs) et des segments (spans) Quarto. Noms de classes **figés** (voir `conventions.md`, section 5) :

```markdown
::: {.notes}
Démonstration faite au tableau : on part de l'autocorrélation moyennée…
:::

::: {.complement}
Étape non écrite au tableau : changement d'indice $k \to k - 1$.
:::

::: {.a-verifier}
Le support écrit $\mathcal{N}(a\mu + b,\ b^2\sigma^2)$ (p. 78).
La variance correcte semble être $a^2\sigma^2$.
:::

Dans une phrase : [remarque orale du professeur]{.notes}.
```

Règles d'usage :

- **Préférer les blocs** : une démonstration du tableau forme un bloc entier. Les segments en ligne sont réservés à quelques mots insérés dans une phrase du support.
- Le rendu PDF doit reproduire les mêmes repères (filet, étiquette).
- La convention est la **même pour toutes les matières**.

---

## 8. Notes manuscrites

### 8.1 Statut des notes

Les notes manuscrites sont une **source de premier rang**, au même titre que le support officiel. Elles peuvent contenir :

- des démonstrations et des calculs absents des slides ;
- des exemples et des méthodes ;
- des remarques et mises en garde de l'enseignant ;
- des schémas faits au tableau ;
- des corrections apportées au support pendant le cours ;
- des explications orales.

### 8.2 Règles de lecture

- **Ne pas deviner.** Un mot, un indice, un signe ou un exposant douteux va dans un bloc *À vérifier*, avec la page et l'emplacement dans les notes.
- Les erreurs de lecture les plus dangereuses portent sur les formules : indices, signes, exposants, facteurs 2, bornes d'intégrales. Les vérifier par cohérence (dimensions, cas particuliers, cohérence avec le support), et signaler tout doute.
- Une note qui **contredit** le support n'est ni ignorée ni appliquée silencieusement : elle va dans *À vérifier*, avec les deux versions.
- Le contenu sans intérêt pédagogique (gribouillages, remarques personnelles, commentaires sans rapport) n'est pas repris.

### 8.3 Qualité des sources fournies

Pour une lecture fiable : pages à plat, bien éclairées, une page par image, idéalement réunies dans un PDF par séance, dans l'ordre. Indiquer la date de la séance et le chapitre concerné.

---

## 9. Figures et schémas

### 9.1 Principe

Les figures sont conservées lorsqu'elles **apportent quelque chose à la compréhension**. On évite autant que possible d'utiliser directement des photos de notes manuscrites comme figures finales : elles sont peu lisibles et lourdes.

### 9.2 Par type de figure

| Type | Méthode privilégiée |
|---|---|
| **Courbes** (DSP, probabilités d'erreur, diagramme de l'œil, réponses fréquentielles…) | Recréées proprement, idéalement **générées en Python** (matplotlib) à partir des formules : exactes et modifiables |
| **Schémas électroniques** | **TikZ / circuitikz** compilés en SVG, ou autre solution vectorielle adaptée |
| **Schémas-blocs** (chaînes de transmission, architectures) | Reconstruits en vectoriel (TikZ ou SVG) |
| **Figures du professeur** | Conservées si nécessaires (extraction vectorielle si possible), en gardant à l'esprit la question des droits |
| **Figures issues des notes** | Reconstruites lorsque cela améliore nettement la lisibilité |

Les fichiers sources des figures (`.py`, `.tex`) sont versionnés dans `figures/`, avec leur rendu. Une figure doit pouvoir être régénérée.

### 9.3 Traçabilité des figures

La légende de chaque figure indique son origine :

- **Support** : « D'après le support, p. X. »
- **Notes** : « D'après les notes de cours (séance du JJ/MM, p. Y), redessinée. »
- **Reconstruite ou complétée** : les éléments ajoutés par rapport à la source sont tracés en **pointillés gris**, et la légende précise ce qui a été ajouté.

Le scan original reste consultable par Armand (archive locale non publiée), pour vérification.

---

## 10. Flashcards

### 10.1 Principe

Les flashcards sont générées **à partir du cours finalisé et validé**, jamais directement à partir des slides. Elles alimentent l'application de révision (voir [section 20](#20-lexistant--lapplication-bristol-actuelle)).

### 10.2 Ce qu'elles doivent couvrir

- définitions ;
- formules **et leurs conditions d'application** ;
- propriétés ;
- méthodes ;
- étapes de raisonnement et de démonstration ;
- pièges et erreurs fréquentes ;
- relations entre notions ;
- résultats importants ;
- mini-exercices d'application.

### 10.3 Qualité d'une carte

- **Une seule notion par carte.**
- La question oblige à **retrouver** la réponse, pas seulement à la reconnaître.
- Éviter les cartes qui demandent de réciter un paragraphe ou une longue liste : découper.
- Préférer « Quelle est l'expression de X, et dans quelles conditions peut-on l'utiliser ? » à « Donne la formule de X ».
- Pour une démonstration : des cartes sur les **étapes clés** (« Quel changement de variable permet de… ? »), pas sur la démonstration entière.
- Réponse courte et précise. Un lien vers le cours permet d'approfondir.
- Les pièges identifiés dans les blocs *À vérifier* tranchés donnent souvent de bonnes cartes.

### 10.4 Types de cartes

Chaque carte a un type parmi : `definition`, `formule`, `condition`, `propriete`, `methode`, `raisonnement`, `piege`, `relation`, `resultat`, `exercice`. La liste peut évoluer : la tenir à jour dans `conventions.md`.

### 10.5 Format

Les cartes sont écrites dans un fichier par chapitre, dans `matieres/<matiere>/flashcards/`, au format **YAML** (`flashcards/NN-slug.yml`, même nom que le chapitre ; format détaillé dans `conventions.md`, section 10). Un script de `scripts/` les convertit au format de l'application de révision.

La matière et le chapitre sont déclarés **une fois en tête de fichier**, avec la liste des identifiants retirés. Champs de chaque carte :

```text
id          identifiant persistant (jamais réutilisé, jamais modifié)
type        voir 10.4
question    recto
reponse     verso
ref         label du passage du cours (ex. eq-bennett) ; NN-slug.qmd#label pour un autre chapitre
source      facultatif : officiel, notes, complement
tags        facultatif
```

Exemple :

```yaml
matiere: ts227
chapitre: 3
cours: cours/03-dsp-signaux-codes-en-ligne.qmd
ids-retires: []
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
```

### 10.6 Identifiants

- Les identifiants sont **persistants** : ils servent à conserver la progression de révision quand une carte est modifiée.
- Une carte modifiée garde son identifiant. Une carte supprimée libère son identifiant, qui n'est **jamais réutilisé** (il est noté dans `ids-retires`).
- Format : `<matiere>-<slug>`, par exemple `ts227-bennett-conditions`. **Pas de numéro de chapitre** : comme les labels du cours, l'identifiant décrit la notion et est **unique dans toute la matière**. Une carte qui change de chapitre garde donc son identifiant.

---

## 11. Workflow d'un chapitre

```text
1. Réception des sources
        ↓
2. Analyse des sources
        ↓
3. Identification des différences
        ↓
4. Reconstruction du cours
        ↓
5. Intégration des figures
        ↓
6. Vérification
        ↓
7. Validation par Armand
        ↓
8. Génération des flashcards
        ↓
9. Intégration au site
```

### Détail des étapes

**1. Réception des sources.** Armand fournit le support officiel du chapitre et ses notes. Inventorier les fichiers (nom, version ou date, pages concernées).

**2. Analyse des sources.** Lire **toutes** les sources avant d'écrire quoi que ce soit. Produire un **rapport d'analyse** contenant :

- la correspondance entre les pages du support et les pages des notes ;
- ce qui ne figure **que** dans les notes (démonstrations, exemples, remarques) ;
- les informations redondantes ;
- les figures importantes, avec leur source ;
- les incohérences, contradictions et coquilles ;
- les passages illisibles ou ambigus ;
- les **questions à poser à Armand**.

**3. Identification des différences.** Armand répond aux questions du rapport. Les points restés ouverts seront traités en *À vérifier*.

**4. Reconstruction du cours.** Rédaction du fichier `.qmd` selon les sections 6 et 7.

**5. Intégration des figures.** Selon la section 9.

**6. Vérification.** Relecture systématique par Claude :

- toutes les informations du support et des notes sont présentes ;
- les formules sont cohérentes (dimensions, cas particuliers, notations de la matière) ;
- les quatre catégories sont correctement appliquées ;
- les références croisées fonctionnent ;
- la liste des blocs *À vérifier* restants est à jour.

**7. Validation par Armand.** Armand relit le chapitre, tranche les blocs *À vérifier* et valide. Cette relecture est aussi une étape d'apprentissage actif.

**8. Génération des flashcards.** À partir du chapitre **validé** uniquement.

**9. Intégration au site.** Ajout à la navigation, mise à jour de la fiche matière, conversion des flashcards, commit.

**Important : ne jamais générer les flashcards définitives avant que le cours soit validé.**

---

## 12. Organisation du travail avec Claude

### 12.1 Principe

Le projet ne doit **pas** dépendre d'une conversation gigantesque. **Une conversation = une tâche ou une étape limitée.**

Exemples de noms de conversations :

```text
Bristol — Architecture
Bristol — Prototype
Bristol — TS227 Chapitre 1 — Analyse
Bristol — TS227 Chapitre 1 — Rédaction
Bristol — TS227 Chapitre 1 — Vérification
Bristol — TS227 Chapitre 1 — Flashcards
```

### 12.2 Le dépôt est la source de vérité

- Les décisions importantes sont enregistrées **dans les fichiers du projet**, pas seulement dans les conversations.
- Claude **ne voit pas le dépôt** d'une conversation à l'autre : Armand fournit à chaque session les fichiers de contexte et les fichiers concernés par la tâche.
- Pour les tâches qui touchent beaucoup de fichiers (mise en place du site, scripts, réorganisation), **Claude Code**, qui travaille directement dans le dépôt, est plus adapté que le chat.

### 12.3 Début de session

1. Armand fournit `CONTEXTE_PROJET.md`, `conventions.md`, `ETAT_PROJET.md` et les fichiers utiles à la tâche.
2. Claude les lit, résume en quelques lignes l'état du projet et la tâche du jour, et signale toute incohérence entre les fichiers.
3. Le travail commence.

### 12.4 Fin de session

1. Lister les décisions prises pendant la session.
2. Mettre à jour `ETAT_PROJET.md` (et `TODO.md`, et si besoin `conventions.md` ou ce document).
3. Proposer un message de commit.
4. Indiquer la prochaine étape.

### 12.5 Ce que Claude doit faire spontanément

- Signaler les incertitudes plutôt que de les masquer.
- Poser une question quand une information manque, plutôt que de la supposer.
- Proposer la mise à jour des fichiers de mémoire quand une décision est prise.
- Respecter les conventions existantes, et proposer explicitement toute nouvelle convention avant de l'appliquer.

---

## 13. Fichiers de mémoire du projet

| Fichier | Rôle | Contenu minimal |
|---|---|---|
| `CONTEXTE_PROJET.md` | Vision globale et méthode | Ce document |
| `conventions.md` | Toutes les règles de rédaction et de mise en forme | Classes des quatre catégories, front matter des chapitres, nommage des fichiers, labels (`sec-`, `eq-`, `fig-`, `def-`, `thm-`…), légendes de figures, format et types de flashcards, règles d'écriture mathématique, macros |
| `architecture.md` | Architecture technique | Configuration Quarto, structure des dossiers, scripts, chaîne de génération des flashcards, build, hébergement, dépendances et versions |
| `ETAT_PROJET.md` | État actuel | Terminé, en cours, à faire, décisions récentes, problèmes connus, statut de chaque chapitre |
| `TODO.md` | Tâches | Tâches concrètes, classées par priorité |

Ces fichiers doivent être **maintenus à jour**. Un fichier de mémoire obsolète est dangereux : il faut le corriger dès qu'un écart est constaté.

---

## 14. Gestion des conversations

Lorsqu'une conversation devient trop longue (réponses plus lentes, risque de perte de contexte, ou changement de tâche) :

1. sauvegarder les décisions importantes dans les fichiers ;
2. mettre à jour `ETAT_PROJET.md` ;
3. commencer une nouvelle conversation ;
4. demander à Claude de lire les fichiers de contexte ;
5. continuer le travail.

**Ne jamais supposer qu'une décision importante restera accessible uniquement grâce à l'historique d'une conversation.**

---

## 15. Git

Le projet est versionné avec Git.

- Un commit = **une étape logique**, compréhensible seule.
- Messages au format *Conventional Commits* :

```text
feat: add TS227 chapter 1
feat: add handwritten notes integration
fix: correct Nyquist equation
feat: add TS227 chapter 1 flashcards
docs: update ETAT_PROJET after chapter 1 review
refactor: move shared macros to _macros.qmd
```

- Éviter les modifications massives impossibles à relire.
- Une étiquette (tag) par année universitaire permet de retrouver l'état des cours d'une année donnée.
- Les sources brutes (PDF, scans) ne sont pas versionnées dans un dépôt public.

---

## 16. Gestion des erreurs et vérification

Le système distingue toujours :

| Nature de l'information | Traitement |
|---|---|
| Information certaine issue du support | Texte normal |
| Information issue des notes | Bloc *Notes de cours* |
| Interprétation ou reconstruction | Bloc *Complément*, en le disant explicitement |
| Complément de connaissances générales | Bloc *Complément* |
| Information incertaine ou contradictoire | Bloc *À vérifier* |

Règles :

- Ne jamais présenter une reconstruction comme si elle provenait du professeur.
- Ne jamais inventer une démonstration manquante. Si une étape manque et peut être complétée de manière fiable, la compléter dans un bloc *Complément* ; sinon, signaler le manque.
- Ne jamais corriger silencieusement une coquille : bloc *À vérifier* avec la version de la source et la correction proposée.
- Vérifier les formules par cohérence : dimensions, cas particuliers (M = 2, f = 0…), symétries, cohérence avec les autres chapitres.

---

## 17. Statut des chapitres

Chaque chapitre a un statut, indiqué **dans son front matter** et récapitulé dans `ETAT_PROJET.md` et sur la fiche matière.

```text
BROUILLON            sources reçues, rien n'est encore rédigé
    ↓
ANALYSÉ              rapport d'analyse produit, questions posées
    ↓
RÉDIGÉ               cours reconstruit, figures intégrées
    ↓
VÉRIFIÉ              relecture et vérifications de Claude faites
    ↓
VALIDÉ               relu et validé par Armand
    ↓
FLASHCARDS GÉNÉRÉES  cartes produites à partir du cours validé
```

Un chapitre ne revient en arrière qu'explicitement (par exemple de VALIDÉ à RÉDIGÉ si de nouvelles notes arrivent), et ce retour est noté dans `ETAT_PROJET.md`.

**Mise à jour d'un chapitre validé** (nouvelles notes, correction) : modification ciblée, nouvelle vérification, nouvelle validation, puis mise à jour des flashcards concernées **en conservant leurs identifiants**.

---

## 18. Première matière : TS227

### 18.1 Rôle

**TS227 — Introduction aux communications numériques** est la matière qui sert à **tester tout le système**. Objectif : réussir parfaitement **un** chapitre de bout en bout avant de généraliser la méthode.

### 18.2 Sources déjà identifiées

| Source | Nature | Description |
|---|---|---|
| `poly_ts227.pdf` | Officielle | « Introduction aux communications numériques », Romain Tajan, slides au format poly, 180 pages (version du 9 octobre 2025) |
| `TD_TS_227.pdf` | Officielle | TD « Transmissions en bande de base », Guillaume Ferré et Romain Tajan, 2020/2021, 4 pages |
| `correction_TD_TS_227.pdf` | Officielle | Correction partielle du TD, 15 pages |
| Notes manuscrites | Personnelle | **Pas encore fournies** |

### 18.3 Plan du support officiel

1. Introduction (définitions, historique, modèle OSI, modèle de Shannon et Weaver) ;
2. Principes de communication en l'absence de bruit (chaîne de transmission, interférence entre symboles, critère de Nyquist, diagramme de l'œil) ;
3. DSP des signaux codés en ligne (rappels de probabilités, processus aléatoires, cyclostationnarité, formule de Bennett) ;
4. Transmission en présence de bruit (probabilités d'erreur, cas binaire et M-aire, récepteur optimal et filtre adapté, filtres demi-Nyquist, lien entre Pb et Eb/N0) ;
5. Transmission sur fréquence porteuse (enveloppe complexe, modulateur et démodulateur I/Q) ;
6. Modulation et démodulation numériques (ASK, PSK, APK/QAM, FSK, performances, efficacité spectrale) ;
7. Conclusion.

Le découpage en chapitres Bristol suivra a priori ce plan. À confirmer lors de l'analyse.

### 18.4 Points déjà connus (à traiter lors de la rédaction)

**Notations différentes entre le cours et le TD.** Décision : le cours Bristol suit les notations **du cours**, et la table des notations de la fiche matière donne les correspondances.

| Rôle | Cours (poly) | TD |
|---|---|---|
| Filtre de mise en forme | $h(t)$ | $g(t)$ |
| Filtre de réception | $h_a(t)$ | $g_a(t)$ |
| Filtre global | $g(t) = (h \star h_c \star h_a)(t)$ | $v(t)$ |

**Coquilles ou approximations repérées dans le poly** (à présenter en blocs *À vérifier*, sans correction silencieuse) :

- p. 78 : loi de $Y = aX + b$ donnée avec la variance $b^2\sigma^2$ ; la variance correcte est $a^2\sigma^2$ ;
- p. 78 : intervalles de confiance gaussiens donnés à 67 % (±σ) et 99 % (±3σ) ; valeurs usuelles ≈ 68 % et 99,7 % ;
- p. 130 : filtre adapté causal écrit $h_a(t) = h(t - T_h)$ ; il manque le retournement temporel, $h_a(t) = h^*(T_h - t)$, comme dans le TD ;
- p. 153 : la formule de $P_b$ de la M-PSK est en réalité une approximation de $P_s$, valable pour $M \geq 4$ ; pour la BPSK, $P_b = Q\left(\sqrt{2E_b/N_0}\right)$ ;
- p. 111 : la réponse marquée comme correcte au quiz sur la « pire » probabilité d'erreur binaire est à vérifier sur la diapositive ; la valeur attendue est 0,5.

**Dans la correction du TD :**

- le terme de phase de la TF de la porte est écrit $e^{+j\pi T_s f}$ ; cela dépend de la convention de signe de la TF (le poly utilise $e^{+j2\pi f t}$ à la p. 40, convention à clarifier) ;
- les questions 5 et 6 de l'exercice 1, la question 6 de l'exercice 2 (DSP de l'OOK), les questions 3 à 5 de l'exercice 3 et toute l'étude pratique **n'ont pas de corrigé**.
  - Des solutions ont été produites par Claude (paquet de flashcards provisoire).
  - Pour l'étude pratique, l'étiquetage de la 4-PAM n'est pas donné par l'énoncé : celui du cours a été supposé (00 → −3, 01 → −1, 11 → 1, 10 → 3).

### 18.5 Flashcards provisoires existantes

Un paquet de **129 cartes** (`ts227.json`, clés `ts-<section>-NN`) a été généré à partir du poly et du TD, **avant** la mise en place de la méthode Bristol. Il est **provisoire** : il sera remplacé par des cartes générées à partir des chapitres validés. Voir la question ouverte sur la conservation de la progression ([section 22](#22-questions-ouvertes)).

---

## 19. Règles non négociables

1. **Ne pas inventer.**
2. **Ne pas corriger silencieusement** une source.
3. **Ne pas supprimer** une information importante des notes.
4. **Ne pas générer les flashcards définitives** avant la validation du cours.
5. **Ne pas publier les supports** (ni les contenus qui en dérivent) sans avoir vérifié les droits.
6. **Ne pas dépendre d'une conversation unique** : tout ce qui compte est dans les fichiers.
7. **Conserver des identifiants stables** : fichiers, labels, flashcards.
8. **Privilégier la maintenabilité** à la rapidité.
9. **Signaler les incertitudes**, toujours.
10. **Rendre visible l'origine** de chaque contenu (quatre catégories).

---

## 20. L'existant : l'application Bristol actuelle

Avant le projet de site, Bristol existait déjà comme **application de flashcards**. Elle deviendra la section « Révisions » du site (`revision/`).

### 20.1 Description

- Un **fichier HTML unique** (`index.html`) : HTML, CSS et JavaScript dans le même fichier, sans étape de build.
- Algorithme de répétition espacée inspiré de **SM-2 / Anki** :
  - quatre réponses : Encore, Difficile, Bien, Facile ;
  - étapes d'apprentissage de 1 et 10 minutes, premier intervalle 1 jour (4 jours avec « Facile ») ;
  - facilité initiale 2,5 ;
  - la journée commence à 4 h ;
  - limite de nouvelles cartes par jour réglable par paquet (20 par défaut).
- Fonctions : paquets, ajout, modification et suppression de cartes, recherche, import et export texte (compatible Anki et Quizlet), annulation de la dernière réponse, raccourcis clavier.
- Rendu des cartes :
  - sous-ensemble de Markdown : `**gras**`, `*italique*`, code entre accents graves ;
  - LaTeX via **MathJax 3** (`$…$` et `$$…$$`) ;
  - le code est protégé : ni formule ni mise en forme n'y est interprétée.

### 20.2 Deux versions

| Version | Hébergement | Stockage de la progression | Arrivée des cartes |
|---|---|---|---|
| **GitHub** (version de référence d'Armand) | Dépôt GitHub d'Armand | Navigateur (`localStorage`), donc **propre à chaque appareil** | Fichiers `cartes/*.json` listés dans `cartes/index.json`, lus à chaque ouverture |
| claude.ai | Artifact publié : https://claude.ai/artifact/Kdg6LnEv1Ewz5HoU8ysotM | Compte Claude (base de données de l'artifact) | Dépôt direct par Claude dans une « boîte de réception » |

Décision : utiliser **une seule** des deux versions pour réviser, la version GitHub.

### 20.3 Format des paquets (`cartes/<paquet>.json`)

```json
{
  "deck": "Nom du paquet",
  "color": "#FFF0A6",
  "items": [
    { "key": "id-persistant", "chap": "Nom du chapitre", "front": "Recto", "back": "Verso" }
  ]
}
```

Comportement à chaque ouverture du site :

- une carte dont la `key` existe déjà est **mise à jour sans perdre sa progression** ;
- une carte nouvelle est ajoutée ;
- une carte venue de ce fichier et absente de la nouvelle version est **supprimée** (le fichier est considéré comme le contenu complet du paquet) ;
- les nouvelles cartes sont présentées dans l'ordre du fichier (utile pour espacer les cartes qui se répondent, comme les deux sens d'un mot de vocabulaire).

Contrainte de rédaction des cartes : en dehors du code et des formules, une ligne ne doit pas contenir un seul astérisque isolé (il serait pris pour de l'italique).

### 20.4 Paquets existants

Tous ont été générés **avant** la méthode Bristol. Ils sont à considérer comme **hérités**.

| Fichier | Paquet | Cartes | Préfixe des clés | Origine |
|---|---|---|---|---|
| `reseaux.json` | Réseaux et programmation réseau (RE223) | 225 | `res-` | Poly du cours + notes d'Armand |
| `anglais-ielts.json` | Anglais : vocabulaire IELTS | 107 | `ang-` | Fiches de vocabulaire d'Armand |
| `vhdl.json` | VHDL | 90 | `vhdl-` | Connaissances générales (pas de cours fourni) |
| `c-unix.json` | C et Unix | 108 | `cu-` | Connaissances générales (pas de cours fourni) |
| `latex.json` | LaTeX | 92 | `latex-` | Connaissances générales |
| `ts227.json` | Communications numériques (TS227) | 129 | `ts-` | Poly + TD + correction (provisoire, voir 18.5) |

### 20.5 Évolutions prévues de l'application

- générer les fichiers `cartes/*.json` à partir des flashcards du site (`matieres/*/flashcards/`) par un script ;
- lien « Voir dans le cours » sur chaque carte (champ `ref`) ;
- révision d'un seul chapitre, et mode « veille d'examen » ;
- à plus long terme : synchronisation de la progression entre appareils.

---

## 21. Journal des décisions

| Date | Décision | Raison |
|---|---|---|
| 2026-10 | Application de flashcards hébergée sur GitHub, cartes en fichiers JSON dans `cartes/` | Contrôle par Armand, pas de dépendance à un compte |
| 2026-10 | Mise à jour des cartes par identifiant persistant, sans perte de progression | Les cours évoluent avec les notes d'amphi |
| 2026-10-06 | Bristol devient un site centralisé des enseignements (cours, puis TD, TP, annales, corrigés, flashcards) | Centraliser une base de connaissances sur plusieurs années |
| 2026-10-06 | Phase 1 : cours et flashcards uniquement | Réussir la méthode avant d'élargir |
| 2026-10-06 | Technologie : Quarto + Markdown + maths LaTeX, site statique | Voir section 5 |
| 2026-10-06 | Quatre catégories visibles : support officiel, notes de cours, complément, à vérifier | Traçabilité |
| 2026-10-06 | Flashcards générées uniquement à partir des cours validés | Éviter d'apprendre des erreurs |
| 2026-10-06 | Pas de publication du site de cours avant clarification des droits | Supports des enseignants |
| 2026-10-06 | TS227 comme matière de test ; notations du cours retenues | Matière riche en maths, sources déjà disponibles |
| 2026-10-06 | Une conversation par étape, dépôt = source de vérité | Ne pas dépendre de l'historique des conversations |
| 2026-10-06 | Classes des quatre catégories figées : `.notes`, `.complement`, `.a-verifier` ; rendu HTML de `assets/bristol.scss` retenu ; rendu PDF à faire (question 3) | Classes déjà stylées dans le prototype |
| 2026-10-06 | Flashcards en YAML, un fichier par chapitre ; identifiants `<matiere>-<slug>`, uniques dans la matière, sans numéro de chapitre (question 4) | Un identifiant ne dépend pas de la position de la carte, comme les labels |
| 2026-10-06 | Macros communes dans `_macros.qmd` (et non `_macros.tex`) | Fichier inclus directement dans les pages Quarto |
| 2026-10-06 | Conventions détaillées figées dans `conventions.md` (front matter, statuts, labels, blocs *À vérifier* identifiés par `#av-slug`) | Voir `conventions.md`, section 12 |

---

## 22. Questions ouvertes

À trancher au fil du projet. Une fois tranchée, une question passe dans le [journal des décisions](#21-journal-des-décisions).

1. **Hébergement du site de cours** : public avec accord des enseignants, privé derrière une authentification, ou local uniquement ?
   *Règle provisoire : utilisation en local uniquement (`quarto preview`), rien n'est publié.*
2. **Dépôt** : un seul dépôt (site + application de révision), ou deux dépôts ? Les sources brutes restent dans tous les cas hors du dépôt public.
3. ~~**Classes des quatre catégories**~~ : *tranchée le 2026-10-06, voir le journal des décisions.*
4. ~~**Format des flashcards**~~ : *tranchée le 2026-10-06, voir le journal des décisions.*
5. **Paquet TS227 provisoire** : réutiliser les anciennes clés `ts-…` pour les cartes équivalentes, afin de conserver la progression, ou repartir de nouveaux identifiants ?
6. **Paquets hérités** (réseaux, anglais, VHDL, C et Unix, LaTeX) : les migrer vers le nouveau système, ou les conserver tels quels ?
   *Règle provisoire : conservés tels quels dans `revision/cartes/`, avec leurs clés actuelles ; leurs préfixes (`res-`, `ang-`, `vhdl-`, `cu-`, `latex-`, `ts-`) sont réservés.*
7. **Premier chapitre de test de TS227** : le chapitre 1 (introduction) est léger en contenu ; le chapitre 2 (critère de Nyquist) serait un test plus représentatif de la fusion slides et notes. À décider avec les notes disponibles.
8. **Synchronisation de la progression** entre appareils : nécessaire à terme, solution à choisir.

---

# État actuel

> Section à mettre à jour régulièrement. Le détail vit dans `ETAT_PROJET.md` ; cette section en donne la vue d'ensemble.

## Architecture
- [x] Vision et principes définis (ce document)
- [x] Technologie choisie : Quarto + Markdown + LaTeX
- [x] `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` créés
- [x] Prototype Quarto (squelette du site, page de démonstration `demo-conventions.qmd`)
- [x] Navigation (barre de navigation, barre latérale TS227, fiche matière)
- [x] Styles des blocs des quatre catégories en HTML
- [ ] Styles des blocs des quatre catégories en PDF
- [x] Macros LaTeX communes (`_macros.qmd`)
- [x] Format des flashcards et des identifiants
- [ ] Scripts : conversion des flashcards, vérifications automatiques
- [ ] Lien « Voir dans le cours » dans l'application de révision
- [ ] Dépôt Git initialisé
- [ ] Décision sur l'hébergement et les droits (provisoirement : local uniquement)

## TS227
- [x] Supports officiels reçus (poly, TD, correction partielle)
- [x] Fiche matière avec table des notations
- [ ] Supports copiés dans `sources/ts227/support/`
- [ ] Premier chapitre de test choisi (question ouverte 7)
- [ ] Notes manuscrites de ce chapitre reçues
- [ ] Chapitre de test analysé
- [ ] Chapitre de test rédigé
- [ ] Chapitre de test vérifié
- [ ] Chapitre de test validé
- [ ] Flashcards du chapitre de test

## Prochaines étapes
1. Initialiser le dépôt Git et copier les sources TS227 dans `sources/`.
2. Choisir le premier chapitre de test de TS227 (question ouverte 7), puis fournir le support et les notes correspondantes pour l'étape d'analyse.
3. Écrire les scripts de vérification et de conversion des flashcards avant la génération des premières cartes.
4. Trancher la question de l'hébergement et des droits avant toute publication.
