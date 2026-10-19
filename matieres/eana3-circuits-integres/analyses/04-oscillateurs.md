# EANA3 — Chapitre 4 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow, session « Bristol — Circuits intégrés — Chapitres 1 à 5 » (8 octobre 2026).
> Chapitre : *Oscillateurs*. Fichier : `cours/04-oscillateurs.qmd`. Statut : `redige`.
> Règle appliquée : `conventions.md` § 14.

---

## 0. Résumé

- Premier chapitre de la partie Deval (cours 3, 5, 7, 9). Le support ne donne que le plan et les énoncés : **tout le cours vient des notes externes de 2023** (`.notes-externes`), complétées par Claude (`.complement`).
- TD intégrés : TD 4 (résistance négative, deux corrigés externes concordants), TD 6 (oscillateur à AOP, sans corrigé), TD additionnel « oscillateur en anneau » (corrigé externe, deux erreurs), sujet 2021 « oscillateur à déphasage » du recueil TD 4-2026 (sans corrigé ; variante 2022 résumée).
- **4 blocs *À vérifier*** (section 7).
- **9 figures** : 5 circuitikz, 4 matplotlib.
- « Classes A, B et C » (cours 5) : **aucune source** ; section signalée vide.

---

## 1. Inventaire des sources

| id | Fichier (`sources/eana3/`) | Nature | Pages | Remarque |
|---|---|---|---|---|
| `support` | `support/support-cours-2025.pdf` | officielle | 2, 20-21, 24-28 | plan ; énoncés TD 4, TD 6, TD anneau (copies séparées identiques dans `td/`) |
| `td04-2026` | `td/td04-2026-recueil-sujets-deval.pdf` | officielle | 1-4 | sujets EA210 « oscillateur à déphasage » (22/11/2021, 08/04/2022) |
| `notes-2023-c03-05` | `notes/2023-cours-03-05-deval.pdf` | externe | 1-6 | sinusoïdaux, Colpitts, résistance négative, déphasage |
| `notes-2023-c07` | `notes/2023-cours-07-deval.pdf` | externe | 1-3 | astables, anneaux |
| `notes-2023-c09` | `notes/2023-cours-09-deval.pdf` | externe | 1-4 | Leeson, Hajimiri |
| `corr-2023-td04` | `corriges/2023-td04-oscillateur-resistance-negative.pdf` | externe | 1-3 | TD 4 |
| `corr-2025-td04` | `corriges/2025-td04-oscillateur-resistance-negative.pdf` | externe | 1-5 | TD 4 (plus complet, repris en priorité) |
| `corr-2023-td05-anneau` | `corriges/2023-td05-oscillateur-anneau.pdf` | externe | 1-3 | TD anneau, parties I et II |

Non utilisés : `tableau-2020-*` (partie Rivet) ; recueil TD 4-2026 p. 5-10 (chapitres 5 et 3).

---

## 2. Plan du support pour le chapitre 4

| Point du plan [support, p. 2] | Séance | Sources |
|---|---|---|
| Oscillateurs sinusoïdaux : Barkhausen, Colpitts, Hartley | cours 3 | notes c03-05 p. 1-5 |
| Résistance négative ; classes A, B et C | cours 5 | notes c03-05 p. 5-6 ; TD 4 ; TD 6 ; **classes : aucune** |
| Non sinusoïdaux : astables, anneaux | cours 7 | notes c07 ; TD anneau |
| Bruit de phase : Leeson, Hajimiri | cours 9 | notes c09 |

L'oscillateur à déphasage apparaît dans les notes (c03-05 p. 6, sans calcul) et dans les sujets de 2021-2022.

---

## 3-5. Correspondances, contenu propre aux notes, redondances

- Les deux corrigés du TD 4 donnent les mêmes résultats ; celui de 2025 garde $1/r_{ds}$ avant simplification (repris), celui de 2023 ajoute l'explication de la question 2 (reprise).
- La fréquence de l'anneau est écrite par les notes ($1/(6\Delta t)$, puis $1/(N\Delta t)$) et par le corrigé du TD ($1/(2Mt_p)$) : le corrigé tranche (bloc `av-frequence-anneau`).
- Contenu propre aux notes : Colpitts détaillé, capacité variable, multivibrateur à paire croisée, anneau différentiel, Leeson, Hajimiri.

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Boucle d'oscillateur | `04-boucle-barkhausen.tex` | `fig-boucle-barkhausen` | notes c03-05 p. 1 | circuitikz |
| Colpitts + Thévenin | `04-colpitts.tex` | `fig-colpitts` | notes c03-05 p. 3-4 | circuitikz |
| Astable | `04-astable.py` | `fig-astable` | notes c07 p. 1 | matplotlib |
| Anneau à 3 inverseurs | `04-anneau.py` | `fig-anneau` | notes c07 p. 2 ; corr anneau p. 1 | matplotlib |
| Leeson | `04-leeson.py` | `fig-leeson` | notes c09 p. 2 | matplotlib (courbe de Leeson calculée, coin $\omega_c$ ajouté en gris) |
| ISF | `04-isf.py` | `fig-isf` | notes c09 p. 3-4 | matplotlib (courbes calculées) |
| TD 4 | `04-resistance-negative.tex` | `fig-resistance-negative` | support p. 20 | circuitikz |
| TD 6 | `04-pont-reactif.tex` | `fig-pont-reactif` | support p. 24 | circuitikz |
| Déphasage 2021 | `04-dephasage.tex` | `fig-dephasage` | td04-2026 p. 1 | circuitikz |

Non redessinées (décrites) : réseau en π (notes c03-05 p. 2), paire croisée seule et schéma complet LC (p. 5-6), coupe du NMOS (p. 3), multivibrateur (c07 p. 2), anneau différentiel (c07 p. 3), spectre et phaseur (c09 p. 1), figures 2 du TD 4, figures 1-2 de la partie II du TD anneau, figures 2-3 et annexe du sujet 2021, sujet 2022.

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | Source | Résumé |
|---|---|---|
| `av-frequence-anneau` | notes c07 p. 2 | $F = 1/(N\Delta t)$ incompatible avec $T = 6\Delta t$ pour $N = 3$ ; proposé $F = 1/(2N\Delta t)$ (= corrigé du TD) |
| `av-phases-anneau-differentiel` | notes c07 p. 3 | 0°/90°/180°/270° étage par étage ; proposé : 45° par étage, quadrature entre étages 1 et 3 |
| `av-leeson-prefacteur` | notes c09 p. 1-2 | $FAkT/P_{sig}$ puis $FAkT/(2P_{sig})$, « $A$ » non défini ; forme de la littérature citée (Lee) |
| `av-anneau-dimensionnement` | corr anneau p. 3 | Q6 rapport inversé ($U_T\ln N/\Delta V = 0{,}11$, pas 9 ; valeurs donnant 5 mV) ; Q7 $N$ au lieu de $M$ ; proposé $W_1 = 3{,}3$ µm, autres 30 µm ; 1,22 et 1,47 GHz confirmés |

Vérifié (recalculé, sans bloc) : équation caractéristique du Colpitts (développement symbolique : identique aux notes) ; TD 4 (Q1-Q7) ; TD anneau Q1-Q5 et Q7 ; sujet 2021 ($\omega_0 = \sqrt6/(RC)$, $-1/29$) ; variante 2022 ($\omega_0 = 1/(\sqrt6 RC)$).

Traités sans bloc : notes c03-05 p. 4 « $C_1C_2'$ » pour $C_1'C_2'$ (corrigé, signalé en complément) ; convention de signe de Barkhausen (« inclu le soustracteur », expliqué en complément) ; corr-2023-td04 « O1, G2 » lu « D1, G2 » ; indices $r_{be1}$/$r_{be2}$ (sans effet) ; « Freq »/« Feq » ; $f_0/(2Q)$ vs $\omega_0/(2Q)$ (mentionné dans `av-leeson-prefacteur`).

---

## 8. Passages illisibles ou ambigus

| Où | Lecture | Traitement |
|---|---|---|
| notes c03-05 p. 5 | annotations « A » / « ∀ » | lues comme flèches montée/descente (« quand la grille monte, le drain descend ») |
| notes c03-05 p. 4 | parenthèse de $(1 + LC_{eq}p^2)$ | lecture confirmée par le calcul |
| notes c07 p. 2 | « 6 » ressemblant à « G » | $T = 6\Delta t$ (cohérent) |
| notes c07 p. 3 | « 90° » / « 50° » | dans `av-phases-anneau-differentiel` |
| notes c09 p. 1 | « Bruit d'amplitude » barré ou souligné | lu souligné (les deux bruits sont décrits) |
| notes c09 p. 3 | $h_\phi$ / $h_d$ | $h_\phi$ |
| corr-2025-td04 p. 5 | « $k_d$ » | écrit $k$ (convention du cours non connue) |
| corr anneau p. 2-3 | $L_0$/« $C_0$ », $L_i$/« $C_i$ » | $L$ (dimensions) |

---

## 9. Compléments ajoutés

| # | Complément | Justification |
|---|---|---|
| C1 | Lien avec la stabilité du chapitre 1 | contexte |
| C2 | Convention de signe et démarrage ($|A\beta| > 1$) | ambiguïté des notes |
| C3 | Vérification et lecture physique du Colpitts | calcul refait |
| C4 | Varicap, VCO | précision |
| C5 | Pourquoi « négative » ; lien avec Barkhausen | explication absente |
| C6 | Fonctionnement du multivibrateur | non décrit dans les notes |
| C7 | $\Delta t \approx C\Delta V/I$ ; anneau pair différentiel | lien avec le TD |
| C8 | Lecture de la courbe de Leeson | explication |
| C9 | Conséquences de l'ISF | explication |
| C10 | TD 4 : Q2 détaillée, Q6, double paire | question sans réponse dans le corrigé 2025 |
| C11 | TD 6 complet | sans corrigé |
| C12 | TD anneau : Q4 « remarquable », plage d'accord | sans réponse dans le corrigé |
| C13 | Sujet 2021 complet + variante 2022 | sans corrigé |

---

## 10. Exercices intégrés

| Énoncé | Où | Solutions |
|---|---|---|
| TD 4 « Oscillateur à résistance négative » | `exr-oscillateur-resistance-negative` | corrigés externes 2023 et 2025 ; complément |
| TD 6 « Oscillateur sinusoïdal à base d'AOP » | `exr-oscillateur-aop` | complément |
| TD additionnel « Oscillateur en anneau » (parties I et II) | `exr-oscillateur-anneau` | corrigé externe 2023 ; AV ; complément |
| Sujet 2021 « Oscillateur à déphasage » | `exr-oscillateur-dephasage` | complément (variante 2022 résumée) |

---

## 11. Plan retenu

1. Introduction (`sec-intro-oscillateurs`)
2. Oscillateurs sinusoïdaux : principe, Barkhausen, Colpitts/Hartley, Colpitts à source commune, capacité variable, résistance négative, classes A/B/C (vide), déphasage
3. Non sinusoïdaux : astables, anneaux
4. Bruit de phase : Leeson, Hajimiri
5. TD 4 ; TD 6 ; TD anneau ; sujet 2021
6. À retenir (`sec-retenir-oscillateurs`)

---

## 12. Choix appliqués par défaut

1. Cours entièrement en `.notes-externes` (aucune source officielle de cours) ; compléments séparés.
2. Énoncés : questions intégrales ; figures d'énoncé non redessinées décrites entre parenthèses.
3. Sujet 2021 traité en entier, variante 2022 résumée en complément (même méthode, mêmes résultats numériques).
4. Formule de l'anneau retenue dans le corps de l'AV : $F = 1/(2N\Delta t)$ (`eq-frequence-anneau` dans le bloc).
5. Formule de Leeson : forme des notes conservée, forme de la littérature citée dans l'AV.
6. Enseignant : Yann Deval (Nathalie Deltimple, auteur des énoncés TD 4 et anneau, non listée comme enseignante).

---

## 13. Corrections orthographiques sans bloc

| Source | Texte | Corrigé en |
|---|---|---|
| notes c03-05 p. 1 | « inclu le soustracteur » | « en incluant » |
| notes c09 p. 3 | « Impulse Sensitive Fonction » | « Impulse Sensitivity Function » |
| corr-2025-td04 p. 1 | « Résistence » | non cité |
| support p. 20 | « transistors à effet de champs » | « effet de champ » |
| support p. 21 | « d'oscillateur à résistance négative' » (apostrophe parasite) | guillemets |

---

## 14. Questions bloquantes pour Armand

1. **`av-frequence-anneau`** : $F = \frac{1}{2N\Delta t}$ ?
2. **`av-phases-anneau-differentiel`** : 45° par étage, quadrature entre étages non adjacents ?
3. **`av-leeson-prefacteur`** : quelle forme exacte l'enseignant donne-t-il ($FkT/(2P_{sig})$, $2FkT/P_{sig}$, rôle de « $A$ ») ?
4. **`av-anneau-dimensionnement`** : valider le dimensionnement corrigé ($W_1 = 3{,}3$ µm, autres 30 µm) et $f = 1/(2Mt_p)$.

Non bloquant : le cours de 2026-2027 sur les classes A, B et C ; un corrigé du TD 6 et du sujet 2021.

## 15. Validation et flashcards (étapes 6 à 8)

Décisions d'Armand du 14 octobre 2026 (« fais les démos » : décisions déléguées à Claude, sauf indication), appliquées le 18 octobre 2026 (le travail du 14 octobre n'avait pas été copié sur le PC). Vérification : références croisées, formules des cartes compilées avec MathJax 3.2.2 sans erreur. Chapitre validé, statut `flashcards`.

- `av-frequence-anneau`, `av-phases-anneau-differentiel`, `av-leeson-prefacteur`, `av-anneau-dimensionnement` : propositions retenues (`.tranche`).
- 38 cartes (`flashcards/04-oscillateurs.yml`).
