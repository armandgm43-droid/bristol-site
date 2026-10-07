# Bristol — État du projet

> Où en est le projet. Mis à jour **à la fin de chaque session de travail**.
> Vision et méthode : `CONTEXTE_PROJET.md`. Règles : `conventions.md`. Technique : `architecture.md`. Tâches : `TODO.md`.
>
> Dernière mise à jour : 7 octobre 2026.

---

## 1. En bref

Le prototype est validé. Le premier chapitre de test est le **chapitre 2 de TS227** (*Principes de communication en l'absence de bruit*). Son **rapport d'analyse** est fait et **toutes ses questions sont tranchées** (étape 3, section 13 du rapport `matieres/ts227-communications-numeriques/analyses/02-communication-sans-bruit.md`). Le chapitre est **rédigé** (texte et figures, étapes 4 et 5) : statut `redige`. Vérification faite (étape 6, rapport section 13.10), points V1 à V6 tranchés et appliqués : le chapitre est **validé** par Armand (statut `valide`, rapport section 13.11). **Flashcards générées** (étape 8, 61 cartes, rapport section 13.12) : statut `flashcards`. Le premier chapitre est donc fait de bout en bout.

**Chapitre 3 de TS227** (*DSP des signaux codés en ligne*) : analyse, rédaction et figures (étapes 2 à 5), exercices du TD intégrés ; vérifié (étape 6, rapport § 17), **validé** par Armand, `av-dsp-porte-notes` tranché d'après la correction du TD ; **flashcards générées** (étape 8, 56 cartes, rapport § 18) : statut `flashcards`. 0 bloc ouvert, 5 tranchés, 4 levés.

Révision : en local avec `quarto preview` (port fixe 4848, `http://localhost:4848/revision/`). Le paquet TS227 provisoire (clés `ts-…`) est abandonné (question 5) ; `revision/cartes/ts227.json` est généré par `scripts/flashcards.py`. L'ancien site de cartes (dépôt `bristol`) est **figé**.

Décision du 7 octobre 2026 : le site sera **publié à la fin pour les étudiants de la promo**, derrière un accès réservé et avec l'accord des enseignants (`CONTEXTE_PROJET.md` § 5.4).

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
- [x] TS227 chapitre 2 vérifié puis validé (7 octobre 2026, rapport sections 13.10 et 13.11).
- [x] Direction artistique unique site + application (« fiche bristol »), jetons dans `assets/bristol-tokens.css`, mode sombre, barre de navigation commune (7 octobre 2026). Voir `conventions.md` § 13 et `architecture.md` § 4.
- [x] Flashcards du chapitre 2 de TS227 : `flashcards/02-communication-sans-bruit.yml`, 61 cartes ; V5 trié (2 labels retirés) ; statut `flashcards` (7 octobre 2026).
- [x] `scripts/flashcards.py` : conversion YAML → `revision/cartes/<matiere>.json`, contrôles, macros développées ; lancé : `ts227.json` régénéré (61 cartes `ts227-…`, les 129 cartes `ts-…` disparaissent).
- [x] Port de `quarto preview` fixé à 4848 dans `_quarto.yml` (progression de révision conservée) ; noté dans `architecture.md` § 6 et § 8.
- [x] Correction de `architecture.md` (§ 6) et de ce fichier : l'export actuel de l'application exporte les **cartes**, pas la progression ; renvoi vers la tâche « export/import de la progression » de `TODO.md` (7 octobre 2026). `README.md` ne contenait pas ce conseil.
- [x] TS227 chapitre 3 : rapport d'analyse, `cours/03-dsp-signaux-codes-en-ligne.qmd` (TD ex. 2 et ex. 5 q. 10-11 intégrés), 5 figures `figures/03-*.py` + SVG ; ajouté à `_quarto.yml` et à la fiche matière (convention $\sinc$, notations de l'autocorrélation) (7 octobre 2026).
- [x] TS227 chapitre 3 vérifié (rapport § 17 : exhaustivité support/notes/TD, 569 formules, références ; 6 corrections de forme), validé, `av-dsp-porte-notes` tranché (7 octobre 2026).
- [x] Flashcards du chapitre 3 de TS227 : `flashcards/03-dsp-signaux-codes-en-ligne.yml`, 56 cartes ; `scripts/flashcards.py` lancé : `ts227.json` = 117 cartes (61 + 56) ; statut `flashcards` (7 octobre 2026).

## 3. En cours

- Chapitre 3 de TS227 terminé (flashcards générées). À faire par Armand : contrôler le rendu du chapitre et des 56 cartes avec `quarto preview`.
- Chapitre 2 de TS227 terminé (flashcards générées). À faire par Armand : contrôler le rendu des cartes dans l'application (`quarto preview`) et signaler les cartes à reprendre.

## 4. À faire

Voir `TODO.md`.

---

## 5. Statut des chapitres

### TS227 — Introduction aux communications numériques

| N° | Chapitre (plan du poly) | Fichier | Statut | Blocs *À vérifier* ouverts |
|---|---|---|---|---|
| 1 | Introduction | — | brouillon | — |
| 2 | Principes de communication en l'absence de bruit | `cours/02-communication-sans-bruit.qmd` | **flashcards** (61 cartes) | 0 ouvert + 4 tranchés (`av-signe-tf-nyquist`, `av-centre-symetrie-nyquist`, `av-quiz-debit-porte`, `av-echelles-figure-cosinus-sureleve`) |
| 3 | DSP des signaux codés en ligne | `cours/03-dsp-signaux-codes-en-ligne.qmd` | **flashcards** (56 cartes) | 0 ouvert + 5 tranchés (`av-variance-affine`, `av-esperance-exercice-bpsk`, `av-moment-ordre-2-notes`, `av-dsp-porte-notes`, `av-phase-tf-porte-td`) |
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
| 2026-10-07 | Correction : l'export de l'application ne contient que les cartes ; transfert de progression impossible tant que la tâche « export/import de la progression » n'est pas faite | `architecture.md` § 6 ; § 7 ci-dessous ; `TODO.md` |
| 2026-10-07 | TS227 ch. 3 validé ; `av-dsp-porte-notes` tranché : résultats de la correction du TD ($\sigma_a^2\Ts\sinc^2(f\Ts)$, sommet $\sigma_a^2\Ts$) ; 56 flashcards | rapport ch. 3, § 18 |
| 2026-10-07 | TS227 : $\sinc(x) = \sin(\pi x)/(\pi x)$ ; convention d'autocorrélation du poly ($t - \tau$, $n - m$) retenue partout, y compris pour le TD | fiche matière ; rapport ch. 3, § 16 |
| 2026-10-07 | TS227 ch. 3 : variance affine $a^2\sigma^2$ (poly p. 78 corrigé) ; 67 %/99 % gardés comme arrondis ; $N_0B$ des notes = aire de la bande positive | rapport ch. 3, § 16 |
| 2026-10-07 | Question 5 tranchée : paquet TS227 provisoire (`ts-…`) abandonné, nouvelles clés `ts227-<slug>` ; `ts227.json` généré par script | `CONTEXTE_PROJET.md` § 18.5, § 22, journal |
| 2026-10-07 | Ancien site de cartes (dépôt `bristol`) figé ; révision en local, `quarto preview` sur le port fixe 4848 | `CONTEXTE_PROJET.md` § 20.2 ; `architecture.md` § 6, § 10 ; `_quarto.yml` |
| 2026-10-07 | Flashcards : macros écrites comme dans le cours (développées par le script), sauts de ligne façon Markdown | `conventions.md` § 10.4, § 10.5 |
| 2026-10-07 | TS227 ch. 2 : V5 trié, `eq-signal-yl` et `eq-efficacite-spectrale` retirés (non cités, visés par aucune carte) | rapport ch. 2, 13.12 |
| 2026-10-07 | Site publié à la fin pour les étudiants de la promo ; conditions : accès réservé (liste d'e-mails, ex. Cloudflare Access) et accord des enseignants ; en attendant, local uniquement | `CONTEXTE_PROJET.md` § 1, § 5.4, règle 19.5, journal |
| 2026-10-07 | Pages publiées : aucun contenu personnel ou sans rapport avec le cours | `CONTEXTE_PROJET.md` § 5.4, règle 19.5 |
| 2026-10-07 | Avant publication : page « À propos » (quatre catégories, origine des notes) et export/import de la progression | `CONTEXTE_PROJET.md` § 5.4 ; `TODO.md` |
| 2026-10-07 | Choix de forme, de figures et de rédaction appliqués par défaut par Claude et listés dans le rapport ; questions réservées aux points bloquants | `conventions.md` §14 |
| 2026-10-07 | TS227 ch. 2 validé (V1-V6 tranchés) | rapport ch. 2, 13.11 |
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
9. ~~Rendu des blocs tranchés~~ : stylé le 7 octobre 2026 dans `assets/bristol.scss` (jetons `--cat-verifier…`, clair et sombre), exemple dans `demo-conventions.qmd`. Rendu à contrôler avec `quarto preview`.
16. **Deux dépôts GitHub à ne pas confondre** : `armandgm43-droid/bristol-site` (privé) est le dépôt du projet ; `armandgm43-droid/bristol` est l'ancien site de cartes, toujours en ligne avec GitHub Pages mais **figé** depuis le 7 octobre 2026 (voir `architecture.md` § 10).
13. ~~**Application de révision liée au site**~~ : sans objet depuis que l'ancien site est figé (plus de copie isolée de `revision/`). Rappel : `revision/index.html` charge `../assets/bristol-tokens.css` ; à garder en tête si l'application est un jour copiée ailleurs.
17. **Progression de révision locale** : liée à `http://localhost:4848` et au navigateur. Changer de port, passer par `127.0.0.1` ou changer de navigateur repart de zéro. La progression de l'ancien site GitHub Pages ne se transfère pas non plus. **L'export actuel de l'application exporte les cartes, pas la progression** : aucun transfert n'est possible tant que la tâche « export/import de la progression » de `TODO.md`, section « Avant la publication » n'est pas faite (corrigé le 7 octobre 2026).
18. **Rendu des cartes non contrôlé dans le navigateur** : les 247 formules du paquet TS227 compilent sans erreur avec MathJax 3.2.2 (contrôle de Claude), mais l'affichage réel dans l'application reste à vérifier avec `quarto preview`.
14. **Liens de la barre de navigation écrits deux fois** : `website.navbar` de `_quarto.yml` et en-tête de `revision/index.html`, à garder alignés.
15. **MathJax** : le site (Quarto 1.10) charge MathJax 4, l'application MathJax 3.2.2 ; même syntaxe LaTeX courante. `CONTEXTE_PROJET.md` § 5.5 et § 20.1 mis à jour le 7 octobre 2026. Une formule qui s'affiche différemment dans les deux reste possible : à signaler si elle apparaît.
10. ~~Dossier vide `sources/ts227/notes/a-dater/`~~ : supprimé par Armand.
11. **Énoncé et correction du TD de versions différentes** : numéros de questions à préciser en phase 2.
8. **Notes non datées** : dates inconnues, définitivement ; convention `date-inconnue.pdf` adoptée.
3. ~~Version de Quarto inconnue~~ : 1.10.19, notée dans `architecture.md` § 9.
4. **Rendu PDF des quatre catégories** non implémenté.
5. **Progression des révisions liée à l'adresse du site** (`localStorage`) : déplacer l'application vers un autre hébergement fera repartir de zéro (l'export actuel ne contient que les cartes, pas la progression). À prendre en compte avant de choisir l'hébergement. **Export et import de la progression à faire avant la publication** (décision du 7 octobre 2026, `TODO.md`).
6. **Polices et MathJax chargés depuis Internet** (Google Fonts, jsDelivr) : sans connexion, polices de repli et pas de formules dans l'application de révision.
7. ~~**Paquet `ts227.json` hérité**~~ : réglé (question 5) ; le fichier est désormais généré par `scripts/flashcards.py`, les cartes `ts-…` disparaissent à la prochaine ouverture de l'application.

---

## 8. Questions ouvertes (suivi de `CONTEXTE_PROJET.md`, section 22)

| N° | Question | État |
|---|---|---|
| 1 | Hébergement du site de cours | Ouverte, **orientée** (2026-10-07) : publication pour la promo, accès réservé par liste d'e-mails (ex. Cloudflare Access) + accord des enseignants. En attendant : local uniquement |
| 2 | Un ou deux dépôts | Ouverte |
| 3 | Classes et rendu des quatre catégories | **Tranchée** : classes figées, rendu HTML actuel ; PDF à faire |
| 4 | Format des flashcards et des identifiants | **Tranchée** : YAML, `<matiere>-<slug>` |
| 5 | Reprise des clés `ts-…` du paquet provisoire | **Tranchée** : paquet abandonné, nouvelles clés `ts227-<slug>` |
| 6 | Migration des paquets hérités | Ouverte. Règle provisoire : conservés tels quels |
| 7 | Premier chapitre de test de TS227 | **Tranchée** : chapitre 2 |
| 8 | Synchronisation de la progression entre appareils | Ouverte |
| 9 | Découpage des chapitres 3 et 4 de TS227 (ordre du cours ≠ ordre du poly) | **Tranchée** : ordre du poly |
| 10 | Numérotation des pages citées : PDF ou diapositive | **Tranchée** : pages du PDF |
| 11 | Emplacement des rapports d'analyse | **Tranchée** : `matieres/<matiere>/analyses/NN-slug.md` |
| 12 | Fautes d'orthographe des sources corrigées sans bloc *À vérifier* | **Tranchée** : oui, listées dans le rapport |
| 13 | Signalement d'erreurs et propositions de notes par les camarades | Ouverte (plus tard) |

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
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Vérification | Style des blocs tranchés (`✓ Corrigé`, jetons, clair et sombre) + exemple dans `demo-conventions.qmd` ; `CONTEXTE_PROJET.md` § 5.5 (MathJax 4 / 3.2.2) ; dépôts GitHub notés dans `architecture.md` § 10 ; vérification complète du chapitre 2 (rapport, section 13.10) : 6 points à trancher (V1 : facteur de retombée estimé ≈ 0,35 et non 0,2) |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Vérification (suite) | V1-V6 tranchés et appliqués (β ≈ 0,35, F10 et F11 régénérées ; F12 refaite en spectre rectangulaire ; bloc AV8 levé ; Ш en notes) ; chapitre **validé** ; nouvelle règle `conventions.md` § 14 (choix par défaut, questions bloquantes seulement) |
| 2026-10-07 | Bristol — Publication pour la promo | Décision : site publié pour la promo (accès réservé + accord des enseignants) ; `CONTEXTE_PROJET.md` (§ 1, § 5.4, règle 19.5, journal, questions 1 et 13, « État actuel »), `ETAT_PROJET.md` et `TODO.md` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 2 — Flashcards | Question 5 tranchée ; 61 cartes (`flashcards/02-communication-sans-bruit.yml`) ; V5 trié ; `scripts/flashcards.py` écrit et lancé (`ts227.json` régénéré) ; port de `quarto preview` fixé à 4848 ; ancien site figé ; statut `flashcards` ; `CONTEXTE_PROJET.md`, `conventions.md`, `architecture.md`, `ETAT_PROJET.md`, `TODO.md`, rapport (13.12), fiche matière mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Rédaction | Conseil erroné d'export de la progression corrigé (`architecture.md`, `ETAT_PROJET.md`, `TODO.md`) ; chapitre 3 : analyse, rédaction, 5 figures, TD ex. 2 et ex. 5 q. 10-11 intégrés ; 8 blocs ouverts + 1 tranché ; statut `redige` ; rapport, fiche matière, `_quarto.yml` mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Rédaction (suite) | Réponses d'Armand aux 8 questions appliquées : 2 tranchés, 4 levés, 3 ouverts ; fiche matière, rapport (§ 16) mis à jour |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Rédaction (fin) | Blocs `av-esperance-exercice-bpsk` et `av-moment-ordre-2-notes` tranchés (choix laissé à Claude) ; reste 1 bloc ouvert |
| 2026-10-07 | Bristol — TS227 Chapitre 3 — Vérification et flashcards | Vérification (rapport § 17, 6 corrections de forme, aucune erreur de fond) ; `av-dsp-porte-notes` tranché (TD) ; chapitre validé ; 56 cartes (`flashcards/03-dsp-signaux-codes-en-ligne.yml`) ; `flashcards.py` lancé (117 cartes TS227) ; statut `flashcards` ; rapport (§ 17-18), fiche matière, `ETAT_PROJET.md`, `TODO.md`, `CONTEXTE_PROJET.md` mis à jour |
