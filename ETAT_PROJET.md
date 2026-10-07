# Bristol — État du projet

> Où en est le projet. Mis à jour **à la fin de chaque session de travail**.
> Vision et méthode : `CONTEXTE_PROJET.md`. Règles : `conventions.md`. Technique : `architecture.md`. Tâches : `TODO.md`.
>
> Dernière mise à jour : 7 octobre 2026.

---

## 1. En bref

Le prototype est validé. Le premier chapitre de test est le **chapitre 2 de TS227** (*Principes de communication en l'absence de bruit*). Son **rapport d'analyse** est fait et **toutes ses questions sont tranchées** (étape 3, section 13 du rapport `matieres/ts227-communications-numeriques/analyses/02-communication-sans-bruit.md`). Le chapitre est **rédigé** (texte et figures, étapes 4 et 5) : statut `redige`. Prochaine étape : la **vérification** par Claude (étape 6), après validation par Armand des choix des figures (rapport, section 13.9).

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
- [x] Dépôt Git initialisé (commit `501e006`, « Initialisation du projet Bristol »).
- [x] Poly TS227 copié dans `sources/ts227/support/`.
- [x] Prototype validé par Armand ; chapitre 2 choisi comme chapitre de test (7 octobre 2026).
- [x] Notes manuscrites TS227 reçues (5 feuillets recto-verso, date inconnue) : `sources/ts227/notes/date-inconnue.pdf` et photos dans `date-inconnue/`.
- [x] TD et correction TS227 copiés dans `sources/ts227/support/` et inventoriés.
- [x] Rapport d'analyse du chapitre 2 (7 octobre 2026).
- [x] Étape 3 du chapitre 2 : 16 questions tranchées, 8 points *À vérifier* traités (7 octobre 2026).
- [x] `conventions.md` : 5 conventions ajoutées (voir section 6).
- [x] Rédaction du texte du chapitre 2 de TS227, ajouté à la barre latérale et à la fiche matière (7 octobre 2026).
- [x] Figures du chapitre 2 de TS227 : 12 SVG régénérables dans `figures/` (7 octobre 2026).
- [x] Fiche matière TS227 : table des notations étendue (poly, TD, notes), conventions de la matière (TF, $\Pi_T$), sources, ordre du cours.
- [x] Direction artistique unique site + application (« fiche bristol »), jetons dans `assets/bristol-tokens.css`, mode sombre, barre de navigation commune (7 octobre 2026). Voir `conventions.md` § 13 et `architecture.md` § 4.

## 3. En cours

- Rien. Le chapitre 2 est prêt pour la vérification (étape 6).

## 4. À faire

Voir `TODO.md`.

---

## 5. Statut des chapitres

### TS227 — Introduction aux communications numériques

| N° | Chapitre (plan du poly) | Fichier | Statut | Blocs *À vérifier* ouverts |
|---|---|---|---|---|
| 1 | Introduction | — | brouillon | — |
| 2 | Principes de communication en l'absence de bruit | `cours/02-communication-sans-bruit.qmd` | **redige** | 1 ouvert (`av-exemples-mise-en-forme-manquants`) + 4 tranchés (`av-signe-tf-nyquist`, `av-centre-symetrie-nyquist`, `av-quiz-debit-porte`, `av-echelles-figure-cosinus-sureleve`) |
| 3 | DSP des signaux codés en ligne | — | brouillon | — |
| 4 | Transmission en présence de bruit | — | brouillon | — |
| 5 | Transmission sur fréquence porteuse | — | brouillon | — |
| 6 | Modulation et démodulation numériques | — | brouillon | — (à la rédaction : renvoi vers l'efficacité spectrale du chapitre 2) |

Remarque : « brouillon » signifie ici « sources officielles reçues, rien de rédigé ». Les notes reçues couvrent aussi une partie des chapitres 3 et 4 (voir section 10 du rapport du chapitre 2). L'enseignant n'a pas suivi l'ordre du poly (bruit avant DSP) ; **décision du 7 octobre 2026 : on garde l'ordre du poly**, et la fiche matière le signale.

### Sources disponibles

| Source | Nature | Dans `sources/` ? |
|---|---|---|
| `poly_ts227.pdf` (9 oct. 2025, 180 p.) | officielle | oui, `support/` |
| `TD_TS_227.pdf` (2020/2021, 4 p.) | officielle | oui, `support/` |
| `correction_TD_TS_227.pdf` (15 p.) | officielle | oui, `support/` — suit une **autre version de l'énoncé** (numérotation des questions différente, ex. 2 à 5) |
| Notes manuscrites (5 feuillets recto-verso, 10 photos) | personnelle | oui, `notes/date-inconnue.pdf` + `notes/date-inconnue/` (dates inconnues, définitivement) |

---

## 6. Décisions récentes

| Date | Décision | Où |
|---|---|---|
| 2026-10-07 | Une seule DA (« fiche bristol ») pour le site et l'application ; jetons dans `assets/bristol-tokens.css` ; mode sombre : feuilles sombres, fiches de révision et figures sur papier clair ; préférence clair/sombre partagée | `conventions.md` §13, `architecture.md` §4 |
| 2026-10-07 | TS227 : ordre des chapitres du poly conservé (3 = DSP, 4 = bruit), ordre réel du cours signalé dans la fiche matière | fiche matière |
| 2026-10-07 | TS227 : convention de la TF $e^{-j2\pi ft}$ ; p. 40 du poly = coquille (bloc tranché) | fiche matière ; rapport ch. 2, 13.3 |
| 2026-10-07 | TS227 ch. 2 : centre de symétrie $(1/(2\Ts), g_0\Ts/2)$, correction du poly p. 41 (bloc tranché) | rapport ch. 2, 13.3 |
| 2026-10-07 | TS227 ch. 2 : efficacité spectrale dans le chapitre 2, renvoi depuis le chapitre 6 | rapport ch. 2, 13.2 |
| 2026-10-07 | Blocs *À vérifier* tranchés visibles (`.tranche` + **Décision**) quand la source est corrigée | `conventions.md` §5.2 |
| 2026-10-07 | Fautes d'orthographe sans effet sur le sens corrigées sans bloc, listées dans le rapport | `conventions.md` §5.3 |
| 2026-10-07 | TS227 ch. 2 : `av-echelles-figure-cosinus-sureleve` tranché (axes normalisés dans F11) ; choix de rédaction de l'étape 4 validés | rapport ch. 2, 13.9 |
| 2026-10-07 | Pages citées = pages du PDF ; notes sans date = `date-inconnue.pdf` ; rapports dans `analyses/` | `conventions.md` §2, §3.1 |
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

1. ~~Le dossier n'est pas un dépôt Git~~ : réglé (commit `501e006`).
2. ~~TD et correction absents de `sources/`~~ : réglé.
12. ~~Nouveau point *À vérifier* au chapitre 2 (`av-echelles-figure-cosinus-sureleve`)~~ : tranché le 7 octobre 2026 (axes normalisés).
9. **Rendu des blocs tranchés** (`.a-verifier.tranche`, étiquette `✓ Corrigé`) pas encore stylé dans `assets/bristol.scss` (à faire avec les jetons `--cat-verifier…`).
13. **Application de révision liée au site** : `revision/index.html` charge `../assets/bristol-tokens.css`. Une copie isolée de `revision/` (dépôt GitHub Pages actuel) doit emporter ce fichier, sinon l'application perd couleurs et polices. À régler avec la question ouverte 2.
14. **Liens de la barre de navigation écrits deux fois** : `website.navbar` de `_quarto.yml` et en-tête de `revision/index.html`, à garder alignés.
15. **MathJax** : le site (Quarto 1.10) charge MathJax 4, l'application MathJax 3.2.2. `CONTEXTE_PROJET.md` § 5.5 dit « MathJax 3 » pour les deux ; même syntaxe LaTeX, mais versions différentes.
10. ~~Dossier vide `sources/ts227/notes/a-dater/`~~ : supprimé par Armand.
11. **Énoncé et correction du TD de versions différentes** : numéros de questions à préciser en phase 2.
8. **Notes non datées** : dates inconnues, définitivement ; convention `date-inconnue.pdf` adoptée.
3. ~~Version de Quarto inconnue~~ : 1.10.19, notée dans `architecture.md` § 9.
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
| 7 | Premier chapitre de test de TS227 | **Tranchée** : chapitre 2 |
| 8 | Synchronisation de la progression entre appareils | Ouverte |
| 9 | Découpage des chapitres 3 et 4 de TS227 (ordre du cours ≠ ordre du poly) | **Tranchée** : ordre du poly |
| 10 | Numérotation des pages citées : PDF ou diapositive | **Tranchée** : pages du PDF |
| 11 | Emplacement des rapports d'analyse | **Tranchée** : `matieres/<matiere>/analyses/NN-slug.md` |
| 12 | Fautes d'orthographe des sources corrigées sans bloc *À vérifier* | **Tranchée** : oui, listées dans le rapport |

---

## 9. Journal des sessions

| Date | Session | Résultat |
|---|---|---|
| 2026-10-06 | Sessions précédentes | `CONTEXTE_PROJET.md` rédigé ; squelette Quarto créé |
| 2026-10-06 | Bristol — Fichiers de mémoire | `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` créés ; choix validés (identifiants de cartes sans numéro de chapitre) ; `CONTEXTE_PROJET.md` et `_quarto.yml` mis à jour ; fichiers de mémoire copiés dans le projet claude.ai |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Analyse | Chapitre 2 choisi ; notes rangées dans `sources/ts227/notes/a-dater/` ; rapport d'analyse produit (7 points *À vérifier*, 16 questions) ; statut du chapitre 2 : `analyse` |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Différences | 16 questions tranchées ; notes rangées (`date-inconnue`) ; TD et correction inventoriés ; rapport (section 13), `conventions.md`, fiche matière, `ETAT_PROJET.md`, `TODO.md` et `CONTEXTE_PROJET.md` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Rédaction | `cours/02-communication-sans-bruit.qmd` rédigé (texte, sans figures) ; ajouté à `_quarto.yml` et à la fiche matière ; nouveau bloc ouvert `av-echelles-figure-cosinus-sureleve` ; 3 corrections orthographiques ajoutées au rapport (13.5) ; rapport complété (13.8) |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Figures | AV9 tranché ; 12 figures (11 matplotlib, 1 TikZ) dans `figures/`, intégrées au chapitre ; statut `redige` ; rapport (13.9), fiche matière, `architecture.md`, `ETAT_PROJET.md`, `TODO.md` mis à jour |
| 2026-10-07 | Bristol — Interface | DA unifiée site + application validée sur captures ; `assets/bristol-tokens.css` et `assets/bristol-sombre.scss` créés ; `bristol.scss`, `_quarto.yml`, `revision/index.html` (CSS et barre de navigation, JavaScript de l'application inchangé) modifiés ; `conventions.md` §13 et `architecture.md` §4 rédigés |
