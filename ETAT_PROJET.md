# Bristol — État du projet

> Où en est le projet. Mis à jour **à la fin de chaque session de travail**.
> Vision et méthode : `CONTEXTE_PROJET.md`. Règles : `conventions.md`. Technique : `architecture.md`. Tâches : `TODO.md`.
>
> Dernière mise à jour : 6 octobre 2026.

---

## 1. En bref

La méthode est définie et les fichiers de mémoire existent. Le squelette du site Quarto est en place, avec la fiche matière TS227 et une page de démonstration des quatre catégories. **Aucun chapitre n'est encore rédigé** : la prochaine étape est de choisir le premier chapitre de test de TS227 et de fournir ses sources (support et notes).

---

## 2. Fait

- [x] `CONTEXTE_PROJET.md` : vision, principes, méthode.
- [x] `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` créés (6 octobre 2026).
- [x] Squelette Quarto : `_quarto.yml`, `index.qmd`, `README.md`, `.gitignore`.
- [x] Thème `assets/bristol.scss` avec les styles HTML des quatre catégories.
- [x] Macros communes dans `_macros.qmd`.
- [x] Page `demo-conventions.qmd` (rendu des quatre catégories, références croisées).
- [x] Fiche matière TS227 : enseignants, plan, table des notations cours/TD.
- [x] Arborescence de la matière TS227 (dossiers vides).
- [x] Application de révision copiée dans `revision/`, avec les 6 paquets hérités.

## 3. En cours

- Rien.

## 4. À faire

Voir `TODO.md`.

---

## 5. Statut des chapitres

### TS227 — Introduction aux communications numériques

| N° | Chapitre (plan du poly) | Fichier | Statut | Blocs *À vérifier* ouverts |
|---|---|---|---|---|
| 1 | Introduction | — | brouillon | — |
| 2 | Principes de communication en l'absence de bruit | — | brouillon | — |
| 3 | DSP des signaux codés en ligne | — | brouillon | — |
| 4 | Transmission en présence de bruit | — | brouillon | — |
| 5 | Transmission sur fréquence porteuse | — | brouillon | — |
| 6 | Modulation et démodulation numériques | — | brouillon | — |

Remarque : « brouillon » signifie ici « sources officielles reçues, rien de rédigé ». Les notes manuscrites ne sont pas encore fournies. Le découpage en chapitres reste à confirmer lors de la première analyse.

### Sources disponibles

| Source | Nature | Dans `sources/` ? |
|---|---|---|
| `poly_ts227.pdf` (9 oct. 2025, 180 p.) | officielle | **non** |
| `TD_TS_227.pdf` (2020/2021, 4 p.) | officielle | **non** |
| `correction_TD_TS_227.pdf` (15 p.) | officielle | **non** |
| Notes manuscrites | personnelle | **non fournies** |

---

## 6. Décisions récentes

| Date | Décision | Où |
|---|---|---|
| 2026-10-06 | Classes des catégories figées : `.notes`, `.complement`, `.a-verifier` | `conventions.md` §5 (question ouverte 3) |
| 2026-10-06 | Rendu HTML des catégories validé tel qu'il est dans `bristol.scss` ; rendu PDF reporté | `architecture.md` §4 (question ouverte 3) |
| 2026-10-06 | Flashcards en YAML, un fichier par chapitre ; identifiants `<matiere>-<slug>`, uniques dans la matière, sans numéro de chapitre | `conventions.md` §10 (question ouverte 4) |
| 2026-10-06 | Blocs *À vérifier* identifiés par `#av-slug` | `conventions.md` §5.2 |
| 2026-10-06 | Statuts en minuscules sans accents dans le front matter | `conventions.md` §4 |
| 2026-10-06 | Labels uniques dans la matière, sans numéro | `conventions.md` §7 |
| 2026-10-06 | Macros dans `_macros.qmd` (le contexte disait `_macros.tex`) | `conventions.md` §8 |
| 2026-10-06 | Règle provisoire : site utilisé en local uniquement tant que l'hébergement n'est pas décidé | `architecture.md` §10 (question ouverte 1) |
| 2026-10-06 | Règle provisoire : paquets hérités conservés tels quels, préfixes réservés | `conventions.md` §10.3 (question ouverte 6) |
| 2026-10-06 | `prp-title: "Propriété"` ajouté dans `_quarto.yml` | `_quarto.yml` |

Toutes ces décisions ont été **validées par Armand** le 6 octobre 2026 et reportées dans le journal des décisions de `CONTEXTE_PROJET.md`.

---

## 7. Problèmes connus et incohérences

1. **Le dossier n'est pas un dépôt Git** : rien n'est encore versionné.
2. **Les sources TS227 ne sont pas dans `sources/`** : à y copier (`sources/ts227/support/`).
3. **Version de Quarto inconnue** : à noter dans `architecture.md`.
4. **Rendu PDF des quatre catégories** non implémenté.
5. **Progression des révisions liée à l'adresse du site** (`localStorage`) : déplacer l'application vers un autre hébergement fera repartir de zéro, sauf export puis import. À prendre en compte avant de choisir l'hébergement.
6. **Polices et MathJax chargés depuis Internet** (Google Fonts, jsDelivr) : sans connexion, polices de repli et pas de formules dans l'application de révision.
7. **Paquet `ts227.json` hérité** : le futur paquet généré pour TS227 portera a priori le même nom de fichier ; à régler avec la question ouverte 5.

---

## 8. Questions ouvertes (suivi de `CONTEXTE_PROJET.md`, section 22)

| N° | Question | État |
|---|---|---|
| 1 | Hébergement du site de cours | Ouverte. Règle provisoire : local uniquement |
| 2 | Un ou deux dépôts | Ouverte |
| 3 | Classes et rendu des quatre catégories | **Tranchée** : classes figées, rendu HTML actuel ; PDF à faire |
| 4 | Format des flashcards et des identifiants | **Tranchée** : YAML, `<matiere>-<slug>` |
| 5 | Reprise des clés `ts-…` du paquet provisoire | Ouverte |
| 6 | Migration des paquets hérités | Ouverte. Règle provisoire : conservés tels quels |
| 7 | Premier chapitre de test de TS227 | Ouverte |
| 8 | Synchronisation de la progression entre appareils | Ouverte |

---

## 9. Journal des sessions

| Date | Session | Résultat |
|---|---|---|
| 2026-10-06 | Sessions précédentes | `CONTEXTE_PROJET.md` rédigé ; squelette Quarto créé |
| 2026-10-06 | Bristol — Fichiers de mémoire | `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` créés ; choix validés (identifiants de cartes sans numéro de chapitre) ; `CONTEXTE_PROJET.md` et `_quarto.yml` mis à jour ; fichiers de mémoire copiés dans le projet claude.ai |
