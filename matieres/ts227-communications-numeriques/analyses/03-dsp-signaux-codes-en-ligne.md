# TS227 — Chapitre 3 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow (`CONTEXTE_PROJET.md`, section 11), enchaînées dans la même session à la demande d'Armand (conversation « Bristol — TS227 Chapitre 3 — Rédaction », 7 octobre 2026).
> Chapitre : *DSP des signaux codés en ligne*. Fichier : `cours/03-dsp-signaux-codes-en-ligne.qmd`. Statut : `redige`.
> **Mis à jour le 7 octobre 2026 avec les réponses d'Armand (étape 3)** : voir la section 16, qui fait foi en cas d'écart avec les sections 0 à 15.
> Règle appliquée : `conventions.md` § 14 (choix de forme, de figures et de rédaction appliqués par défaut et listés en section 12 ; questions bloquantes regroupées en section 14).

---

## 0. Résumé

- Le support couvre le chapitre 3 aux **pages 61 à 88** du PDF (diapositives 51 à 78/161). Après suppression des pages de plan et des sondages, il reste **19 pages utiles**. Le support ne contient **aucune démonstration** ni aucune solution d'exercice pour ce chapitre.
- Les notes du chapitre 3 sont celles inventoriées en section 10 du rapport du chapitre 2 : **f. 2 v° (bas)**, **f. 4 v° (bas)**, **f. 5 r°** et **f. 5 v°**. Elles apportent une démonstration (symétrie hermitienne), la remarque $R_X(0) = \int \Gamma_X$, le bruit blanc, un exercice absent du support (retard aléatoire d'un processus cyclostationnaire) et la **solution complète de l'exercice p. 88** (DSP avec une porte).
- Le TD apporte la **démonstration complète de la formule de Bennett** (correction, p. 4-7), son interprétation et la DSP de la 2-PAM. L'exercice 2 du TD et les questions 10-11 de l'exercice 5 sont intégrés au chapitre (demande d'Armand).
- Blocs *À vérifier* : **8 ouverts**, **1 tranché** (section 7). Deux reprennent des coquilles déjà repérées dans `CONTEXTE_PROJET.md` § 18.4 (p. 78).
- **8 questions bloquantes** pour Armand (section 14), une par bloc ouvert.
- 5 nouvelles figures matplotlib ; la chaîne de transmission réutilise la figure du chapitre 2.

Citations : `[poly, p. N]` = page du PDF ; `[notes, f. 5 r°]` ; `[td, p. N]` (énoncé) ; `[td-correction, p. N]`.

---

## 1. Inventaire des sources

| id | Fichier | Nature | Pages utilisées | Remarque |
|---|---|---|---|---|
| `poly` | `sources/ts227/support/poly_ts227.pdf` | officielle | 61-88 | version du 9 octobre 2025 |
| `notes` | `sources/ts227/notes/date-inconnue.pdf` (+ photos) | personnelle | f. 2 v° (bas), f. 4 v° (bas), f. 5 r°, f. 5 v° | date inconnue |
| `td` | `sources/ts227/support/TD_TS_227.pdf` | officielle | p. 2 (ex. 2), p. 4 (ex. 5, q. 10-12) | énoncé 2020/2021 |
| `td-correction` | `sources/ts227/support/correction_TD_TS_227.pdf` | officielle | p. 4-9 (ex. 2) | autre version de l'énoncé ; DSP de l'OOK sans corrigé |

---

## 2. Plan du support pour le chapitre 3

| Partie du poly | Pages PDF | Pages utiles | Pages écartées |
|---|---|---|---|
| Description | 61-68 | 63 | 61, 62 (plans), 64 (« Sortez vos téléphones »), 65-68 (sondages d'auto-évaluation « Je suis à l'aise avec… ») |
| Rappels sur les probabilités | 69-79 | 70-79 | 69 (plan) |
| De la VA au processus aléatoire | 80-88 | 81-88 | 80 (plan) |

Remarques : p. 63 et p. 88 reprennent le schéma de la chaîne de la p. 19 ; les exercices p. 75, 77, 79 et 88 n'ont pas de solution dans le support.

---

## 3. Correspondance support ↔ notes

| Notes | Contenu | Support |
|---|---|---|
| f. 2 v°, milieu | « III Transmission en présence de bruit », « Probas » : densité et propriétés, espérance (discrète et continue), variance, $\E[\lvert X\rvert^2]$ (lecture douteuse, AV `av-moment-ordre-2-notes`) | p. 72-73, 76 |
| f. 2 v°, bas | Loi gaussienne, croquis avec ±σ « 67 % » et ±3σ « 99 % » ; début de l'exercice $Z_n \sim \mathcal{N}(0, \sigma^2)$, $R_n = g_0 + Z_n$ | p. 78-79 |
| f. 4 v°, haut | filtre adapté, $R_h(t)$ « fonction d'autocorrélation déterministe de $h(t)$ » | chapitre 4 (p. 124-131) ; $R_h$ réutilisé ici |
| f. 4 v°, bas | « On s'intéresse désormais au signal $s_l(t)$ » : symboles envoyés, réponse impulsionnelle du filtre d'émission, « Signal aléatoire », deux réalisations $\omega_0$, $\omega_1$, « à temps continu, valeurs discrètes » | p. 81 (indirectement) |
| f. 5 r°, haut | moyenne, autocorrélation, SSL, démonstration $R_X(\tau) = R_X^*(-\tau)$, puissance $R_X(0)$, DSP, remarque TF inverse et $R_X(0) = \int \Gamma_X$ | p. 82-85 |
| f. 5 r°, milieu | bruit blanc gaussien, DSP $N_0/2$, bande $[f_p - B, f_p + B]$, « $N_0 B$ » | **aucune** |
| f. 5 r°, bas | exercice : $Y(t) = X(t - \theta)$, $\theta \sim \mathcal{U}_{[0,T[}$, « $Y$ stationnaire », calcul de $m_Y$ | **aucune** |
| f. 5 v° | exercice : DSP de $s_l(t)$ avec porte, symboles centrés indépendants : $m$, $R(t, \tau)$, périodicité, $\tilde{R} = \frac{\sigma_a^2}{\Ts} R_h$, $\Gamma = \frac{\sigma_a^2}{\Ts}\lvert H\rvert^2$, dessin, $B = 1/\Ts$ | p. 88 (énoncé seul) |

---

## 4. Contenu présent uniquement dans les notes (blocs `.notes`)

1. Ordre du cours : rappels de probabilités donnés au début de « III Transmission en présence de bruit » [f. 2 v°].
2. $s_l(t)$ comme signal aléatoire, réalisations $\omega_0$, $\omega_1$ [f. 4 v°] → figure.
3. Démonstration de la symétrie hermitienne de $R_X$ [f. 5 r°].
4. TF inverse et $R_X(0) = \int \Gamma_X(f)\,\mathrm{d}f$ [f. 5 r°].
5. Bruit blanc gaussien, $N_0/2$, « $N_0 B$ » [f. 5 r°] → figure, AV.
6. Exercice du retard aléatoire $\theta$ [f. 5 r°] (inachevé, complété en *Complément*).
7. Solution de l'exercice p. 88 [f. 5 v°], y compris la bande $B = 1/\Ts$.
8. Nom « autocorrélation déterministe » pour $R_h$ [f. 4 v°].
9. Énoncé de l'exercice p. 79 recopié au tableau [f. 2 v°].

---

## 5. Informations redondantes

- Notes = support (on garde le support, sans bloc) : densité et ses propriétés, $\E[h(X)]$, densité gaussienne, $R_X(t, \tau)$, SSL, $P_X = R_X(0)$, définition de la DSP.
- Notes moins précises que le support, non reprises : moyenne écrite $\bar{x}(t) = \int x f(x)\,\mathrm{d}t$ [f. 5 r°] (variable d'intégration $\mathrm{d}t$ pour $\mathrm{d}x$, densité sans indice $X(t)$) ; puissance $\E[X^2(t)]$ au lieu de $\E[\lvert X(t)\rvert^2]$ ; variance avec $\E[X]^2$ (signalée dans un bloc `.notes`, identique pour une VA réelle).
- Démonstration de Bennett : la correction du TD (cas général) et les notes (cas iid centré) se recouvrent ; la première est donnée après le théorème, la seconde dans l'exemple de la porte.
- Les lignes barrées de f. 5 v° (première tentative de calcul de $R_{s_l}$) ne sont pas reprises.

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Chaîne de transmission | `02-chaine-bande-de-base.svg` (réutilisée) | `fig-chaine-dsp` | poly p. 63 (= p. 19) | TikZ (ch. 2) |
| Loi gaussienne, ±σ, ±3σ | `03-loi-gaussienne.py` | `fig-loi-gaussienne` | poly p. 78 ; notes f. 2 v° | matplotlib |
| Réalisations de $s_l(t)$ | `03-realisations-signal-aleatoire.py` | `fig-realisations-signal-aleatoire` | notes f. 4 v° | matplotlib |
| DSP du bruit blanc | `03-bruit-blanc.py` | `fig-bruit-blanc` | notes f. 5 r° | matplotlib |
| DSP avec porte | `03-dsp-porte.py` | `fig-dsp-porte` | notes f. 5 v° ; td-correction p. 9 | matplotlib |
| DSP 2-PAM et 2-OOK | `03-dsp-2pam-ook.py` | `fig-dsp-2pam-ook` | td-correction p. 9 (2-PAM) ; OOK reconstruite | matplotlib |

Toutes les figures ont été régénérées sur le PC d'Armand (matplotlib 3.10) et relues en image.

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | État | Source | Résumé |
|---|---|---|---|
| `av-variance-affine` | **ouvert** | poly p. 78 | $Y = aX + b \sim \mathcal{N}(a\mu + b, b^2\sigma^2)$ ; proposition $a^2\sigma^2$ (déjà relevé dans `CONTEXTE_PROJET.md` § 18.4). Incohérent avec la propriété suivante du support |
| `av-intervalles-confiance-gaussiens` | **ouvert** | poly p. 78 ; notes f. 2 v° | 67 % et 99 % ; valeurs exactes 68,27 % et 99,73 % ; le TD (ex. 5, q. 12) écrit 99,7 % : **contradiction entre sources** |
| `av-esperance-exercice-bpsk` | **ouvert** | poly p. 77 | « que vaut $\E[X]$ ? » alors que la VA est $A_n$ |
| `av-moment-ordre-2-notes` | **ouvert** | notes f. 2 v° | lecture « $\sum_{n=0}^{N-1} h(x_0)^2 P(X = x_0)$ » : indices et $h(\cdot)^2$ douteux |
| `av-puissance-bruit-bande` | **ouvert** | notes f. 5 r° | « $N_0 B$ » = aire de la bande positive seule ; puissance d'un bruit réel dans la bande : $2N_0B$ |
| `av-moyenne-dephasage-aleatoire` | **ouvert** | notes f. 5 r° | « $m_Y(t)$ périodique » (ou $m_X$ ?) juste après « $Y$ stationnaire » |
| `av-dsp-porte-notes` | **ouvert** | notes f. 5 v° | $\lvert H\rvert^2$ noté « $\sinc(f\Ts)$ », sommet « $\sigma_a^2/\Ts$ » ; correct : $\Ts^2\sinc^2$, sommet $\sigma_a^2\Ts$ (confirmé par td-correction p. 8) : **contradiction notes / correction du TD** |
| `av-convention-autocorrelation-td` | **ouvert** | td p. 2 vs td-correction p. 5, 8, poly p. 83, notes | $R_A[k] = \E(A_n A^*_{n+k})$ et $\E(s_l(t)s_l^*(t+\tau))$ dans l'énoncé ; convention inverse ailleurs : **contradiction entre sources** |
| `av-phase-tf-porte-td` | **tranché** | td-correction p. 8 | $e^{+j\pi T_s f}$ ; décision déjà prise le 7 octobre 2026 (convention $e^{-j2\pi ft}$, `CONTEXTE_PROJET.md` § 18.4) |

Vérifié sans problème : formule de Bennett p. 87 (signe de l'exponentielle cohérent avec $R_A[m] = \E[A_n A^*_{n-m}]$, recalculé) ; définitions p. 82-86 ; TFD p. 85 ; démonstration de la correction p. 4-7 (refaite) ; DSP 2-PAM p. 8 ($\Ts\sinc^2$, puissance 1) ; calculs des notes f. 5 v° jusqu'à $\tilde{R} = \frac{\sigma_a^2}{\Ts}R_h$ ; démonstration de symétrie hermitienne f. 5 r°.

Points d'imprécision traités **sans bloc** (pas d'erreur de sens) :

- p. 85 : la DSP « caractérise la distribution de l'énergie en fréquence » ; c'est la puissance qui est répartie → *Complément* explicatif, texte du support conservé.
- p. 87 : $R_A[m]$ n'est pas défini → *Complément* (définition cohérente avec p. 83 et la correction du TD).
- p. 88 : amplitude de la porte et loi des symboles non précisées → *Complément*.

---

## 8. Passages illisibles ou ambigus dans les notes

| Où | Lecture | Traitement |
|---|---|---|
| f. 2 v°, milieu | $\E[\lvert X\rvert^2] = \sum_{n=0}^{N-1} h(x_0)^2 P(X = x_0)$ | bloc `av-moment-ordre-2-notes` (Q4) |
| f. 2 v°, croquis gaussien | sous la courbe, un label central peu lisible (« $\mu$ » ou « $2\sigma$ ») | non repris (sans conséquence) |
| f. 5 r°, milieu | « $m_Y(t)$ périodique avec : » (indice $Y$ ou $X$) | bloc `av-moyenne-dephasage-aleatoire` (Q6) |
| f. 5 r°, dessin du bruit blanc | label à gauche de l'axe (« $f$ » ou « $0$ ») | sans conséquence ; non repris |
| f. 5 v° | « $R_{s_l}(t - \Ts, \tau)$ » (signe peu lisible) | lu « $-$ », cohérent avec le membre de droite ; la périodicité ne dépend pas du sens (pas de question) |
| f. 5 v° | graduations du dessin de DSP ($-2/\Ts$, $-1/\Ts$, $1/\Ts$, $2/\Ts$, en partie raturées) | lobe principal $[-1/\Ts, 1/\Ts]$, cohérent avec « $B = 1/\Ts$ » |

---

## 9. Compléments ajoutés (catégorie *Complément*)

| # | Complément | Justification |
|---|---|---|
| C1 | Introduction : plan du chapitre | aucune source ne le donne |
| C2 | Solutions des exercices p. 75, 77, 79 | le support ne donne pas de réponses |
| C3 | Lien de l'exercice p. 79 avec `av-variance-affine` et avec la décision du chapitre 4 | relie deux points du support |
| C4 | Notation $A_m$ (majuscule) pour les symboles aléatoires | support p. 87 et notes ; lien avec $a_n$ du chapitre 2 |
| C5 | Fin de la démonstration hermitienne ; maximum en 0 par Cauchy-Schwarz | étape non écrite ; propriété non démontrée |
| C6 | « Énergie » → puissance (p. 85) ; puissance = aire sous la DSP | précision de vocabulaire |
| C7 | Bruit blanc : $R = \frac{N_0}{2}\delta$, puissance infinie, « gaussien » porte sur la loi | les notes ne donnent que le dessin |
| C8 | Fin de l'exercice du retard aléatoire : $m_Y$ constante, $R_Y = \tilde{R}_X$, justification de la définition p. 86 | exercice inachevé dans les notes |
| C9 | Définition et conditions de $R_A[m]$ dans Bennett | absentes p. 87 |
| C10 | Correspondance $v(\tau)$ (correction) / $R_h(\tau)$ (cours, notes) | conflit de notation avec $v(t)$ du TD |
| C11 | Puissance $P_{s_l} = \sigma_A^2 E_h / \Ts$ (TD ex. 2, q. 8, sans corrigé) | |
| C12 | Calcul complet de $H(f)$ pour la porte, zéros, lobe principal, lien avec la bande de Nyquist | |
| C13 | DSP de la 2-OOK (TD ex. 2, q. 11, sans corrigé) : $\frac{\Ts}{4}\sinc^2 + \frac14\delta$, interprétation | |
| C14 | TD ex. 5, q. 10-11 (sans corrigé) : DSP de $s_l[n]$, largeur du lobe principal 4 kHz ($B = 2$ kHz) | |

---

## 10. TD intégré au chapitre

| TD | Contenu | Où dans le chapitre | Corrigé |
|---|---|---|---|
| ex. 2, q. 1-9 | cyclostationnarité, $\bar{m}$, $\bar{R}$, puissance, Bennett | `exr-td-bennett` ; démonstration du `thm-bennett` | correction p. 4-7 (q. 8 sans corrigé → C11) |
| ex. 2, q. 10 | DSP 2-PAM | `exr-td-dsp-2pam` | correction p. 7-9 |
| ex. 2, q. 11 | DSP 2-OOK | `exr-td-dsp-ook` | aucun → C13 |
| ex. 5, q. 10-11 | DSP de $s_l[n]$, largeur de bande | `exr-td-largeur-bande` | aucun → C14 |
| ex. 4, q. 4-5 (énoncé) | autocorrélation du bruit échantillonné, « formule du filtrage des PA » | **non intégré** : relève du bruit (chapitre 4) | correction p. 13-14 |
| ex. 5, q. 12 | ±3σ « soit 99,7 % » | cité dans `av-intervalles-confiance-gaussiens` | — |

---

## 11. Plan retenu

1. Introduction (`sec-intro-dsp`) — p. 63
2. Rappels de probabilités (`sec-rappels-probabilites`) — p. 70-79 ; notes f. 2 v°
3. Processus aléatoires (`sec-processus-aleatoires`) : définition, moyenne et autocorrélation, SSL, DSP, bruit blanc, cyclostationnarité — p. 81-86 ; notes f. 4 v°, f. 5 r°
4. Filtrage et formule de Bennett (`sec-bennett`) — p. 87 ; td-correction p. 4-8 ; notes f. 4 v°
5. Exemple : mise en forme par une porte (`sec-dsp-porte`) — p. 88 ; notes f. 5 v° ; td-correction p. 8
6. Exercices du TD (`sec-exercices-td-dsp`)
7. À retenir (`sec-retenir-dsp`)

---

## 12. Choix appliqués par défaut (`conventions.md` § 14)

**Plan et rédaction**

1. Ordre du poly conservé ; les rappels de probabilités restent au chapitre 3 (décision Q7 du chapitre 2), l'ordre réel du cours est signalé en bloc `.notes` dans l'introduction.
2. Pages écartées : plans, « Sortez vos téléphones » et les 4 sondages d'auto-évaluation (p. 65-68), sans contenu.
3. Exercices du support (p. 75, 77, 79, 88) en environnements `exr-` ; solutions en *Complément* (le support n'en donne pas), sauf p. 88, résolu dans les notes.
4. Démonstration de Bennett tirée de la **correction du TD** (source officielle) : écrite en texte normal, citée, avec les notations du cours ($g \to h$, $s_s \to s_a$) ; la version des notes (cas iid centré) est donnée dans l'exemple de la porte.
5. Autocorrélation déterministe notée $R_h(\tau)$ (notes) plutôt que $v(\tau)$ (correction du TD), pour éviter la confusion avec le filtre global $v(t)$ du TD ; correspondance dans la fiche matière.
6. Symboles aléatoires notés $A_m$ (support p. 87, notes, TD).
7. Bloc *À vérifier* ouvert sur une formule du support : la formule du support reste affichée dans un segment orange `[…]{.a-verifier}`, la proposition est dans le bloc (pas de correction anticipée).
8. Exercices du TD réécrits avec les notations du cours ; les questions 1 à 9 de l'ex. 2 forment un seul exercice ; la solution renvoie à la démonstration du théorème.
9. TD ex. 4, q. 4-5 laissées au chapitre 4 ; ex. 5, q. 10-11 intégrées.
10. p. 73 « Pour une VA discrète $X$ continue » corrigé en « une VA $X$ continue » **sans bloc** : mot en trop évident, le titre de la diapositive (« Cas des variables aléatoires continues ») lève toute ambiguïté. *À revoir par Armand s'il préfère un bloc.*
11. p. 85 : « énergie » conservé, précision en *Complément* (pas de bloc : imprécision de vocabulaire, pas d'erreur de formule).
12. Ajout à la fiche matière : convention $\sinc(x) = \sin(\pi x)/(\pi x)$ (seule définition présente dans les sources : correction p. 8, notes f. 5 v°) ; lignes de notations du chapitre 3.
13. Section « À retenir » : mentions *(notes)*, *(TD)*, *(complément)*, et *(à vérifier)* pour les points qui dépendent d'un bloc ouvert ; pour ces points, la proposition est écrite et la valeur du support rappelée.
14. Équations labellisées : toutes citées dans le chapitre ou dans « À retenir ».

**Figures**

15. Chaîne de transmission : figure du chapitre 2 réutilisée (même schéma p. 63 et p. 19), nouveau label `fig-chaine-dsp`.
16. Loi gaussienne : axe gradué en $\mu \pm k\sigma$ ; pourcentages **calculés** (68,3 %, 99,7 %) en gris, la légende renvoie au bloc ouvert.
17. Réalisations de $s_l(t)$ : 2-PAM $\pm 1$, porte d'amplitude 1, suites tirées au hasard (graine 3), instant $t = 3{,}4\,\Ts$.
18. Bruit blanc : valeurs $f_p = 3$, $B = 1$ (unités arbitraires) ; bande des fréquences négatives ajoutée en pointillés gris.
19. DSP avec porte : axes normalisés, **échelle linéaire** (la figure de la correction semble en échelle logarithmique, non graduée) ; sommet $\sigma_A^2\Ts$ (proposition du bloc `av-dsp-porte-notes`).
20. DSP 2-PAM / 2-OOK : deux panneaux, même échelle ; raie $\frac14\delta(f)$ dessinée par une flèche hors échelle (signalé dans la légende).

---

## 13. Corrections orthographiques sans bloc (`conventions.md` § 5.3)

| Source | Texte de la source | Corrigé en |
|---|---|---|
| poly, p. 70 | « peuvent être continues ou discrète » | « discrètes » |
| poly, p. 71 | « deux ensembles disjoint » | « disjoints » |
| poly, p. 73 | « Pour une VA discrète X continue » | « Pour une VA $X$ continue » (voir choix 10) |
| poly, p. 74 | « deux VA indépendante » | « indépendantes » |
| poly, p. 81 | « les densité de probabilité » | « la densité de probabilité, la moyenne… » |
| poly, p. 85 | « théorème de Wiener Kintchine » | « Wiener-Khintchine » |
| poly, p. 86 | « si ces propriétés statistiques » | « ses » |
| poly, p. 86-87 | « cyclo-stationnaires » | « cyclostationnaires » (harmonisé) |
| poly, p. 77 | « Exercice - Loi uniforme discrète », « (ie P…) » | ponctuation harmonisée (« c'est-à-dire ») |
| td-correction, p. 7 | « formule de Bennettt » ; « la DSP de $P_{s_l}(t)$ » | « Bennett » ; « la DSP de $s_l(t)$ » |
| td-correction, p. 4 | « période » écrit « préiode » | non repris (titre de question reformulé) |

---

## 14. Questions bloquantes pour Armand

> Chaque question correspond à un bloc *À vérifier* ouvert ; ma proposition est déjà écrite dans le bloc.

1. **`av-variance-affine` (poly p. 78)** : correction $Y \sim \mathcal{N}(a\mu + b, a^2\sigma^2)$ retenue ? (erreur de formule.)
2. **`av-intervalles-confiance-gaussiens` (poly p. 78, notes, TD)** : remplacer 67 % / 99 % par ≈ 68 % / ≈ 99,7 % (valeurs exactes, et celle du TD) ? Le prof a-t-il dit autre chose en cours ?
3. **`av-esperance-exercice-bpsk` (poly p. 77)** : lire « $\E[A_n]$ » au lieu de « $\E[X]$ » ?
4. **`av-moment-ordre-2-notes` (notes f. 2 v°)** : que lis-tu dans la formule de $\E[\lvert X\rvert^2]$ (indices $x_0$ / $x_n$, $h(\cdot)^2$) ? Proposition : $\sum_n \lvert x_n\rvert^2 P(X = x_n)$.
5. **`av-puissance-bruit-bande` (notes f. 5 r°)** : « $N_0 B$ » était-il présenté comme la puissance du bruit dans la bande ? Proposition : $N_0B$ = aire des fréquences positives, puissance totale d'un bruit réel $2N_0B$.
6. **`av-moyenne-dephasage-aleatoire` (notes f. 5 r°)** : « $m_Y(t)$ périodique » ou « $m_X(t)$ périodique » ? Proposition : $m_X$.
7. **`av-dsp-porte-notes` (notes f. 5 v°)** : sommet de la DSP $\sigma_a^2/\Ts$ (notes) ou $\sigma_a^2\Ts$ (calcul, correction du TD) ? Le prof avait-il normalisé la porte (amplitude $1/\Ts$) ?
8. **`av-convention-autocorrelation-td` (énoncé du TD)** : suivre partout la convention du poly ($t - \tau$, $n - m$) et signaler celle de l'énoncé dans la fiche matière ?

---

## 15. Vérifications faites (étape 6 non encore lancée)

- 576 formules du chapitre compilées sans erreur par MathJax 3.2.2 (macros de `_macros.qmd`).
- Labels uniques dans la matière (chapitres 2 et 3) ; toutes les références `@…` du chapitre résolues dans le fichier ; tous les blocs cités par leur identifiant existent ; divs équilibrés.
- Recalculs : formule de Bennett (signe), DSP 2-PAM (puissance 1), DSP 2-OOK (puissance 1/2), $\Phi(-4) \approx 3{,}17 \cdot 10^{-5}$, $2\Phi(1) - 1 = 0{,}6827$, $2\Phi(3) - 1 = 0{,}9973$, $\int \sigma^2\Ts\sinc^2(f\Ts)\,\mathrm{d}f = \sigma^2$.
- Figures régénérées sur le PC d'Armand et relues.
- **Non vérifié** : rendu Quarto (Quarto n'est pas disponible dans l'environnement de Claude) → à contrôler avec `quarto preview`, en particulier les segments `[$…$]{.a-verifier}` contenant des formules et l'environnement `cor-` (premier corollaire du site).

---

## 16. Décisions d'Armand (étape 3, 7 octobre 2026)

| Q | Bloc | Réponse d'Armand | Application dans le cours |
|---|---|---|---|
| 1 | `av-variance-affine` | correction retenue | bloc **tranché** (`.tranche`, **Décision**) ; propriété écrite avec $a^2\sigma^2$, mention « variance corrigée » |
| 2 | `av-intervalles-confiance-gaussiens` | « ce sont des arrondis » : pas une erreur | bloc **levé** ; valeurs du support (67 %, 99 %) conservées comme arrondis ; valeurs exactes (68,27 %, 99,73 %) et usuelles (68 %, 99,7 %, TD) en *Complément* ; légende de la figure et « À retenir » mises à jour. Identifiant retiré |
| 3 | `av-esperance-exercice-bpsk` | Armand ne trouve pas l'exercice | bloc **ouvert**. Repère : page 77 **du PDF** = diapositive imprimée « 67 / 161 », titre « Exercice - Loi uniforme discrète » |
| 4 | `av-moment-ordre-2-notes` | lecture confirmée (indice $x_0$, terme $h(\cdot)^2$) | bloc **ouvert**, réécrit : la lecture n'est plus en doute ; reste l'indice $x_0$ dans une somme sur $n$ (proposition : $x_n$, avec $h(x) = x$) |
| 5 | `av-puissance-bruit-bande` | l'amplitude est $N_0/2$, donc l'aire vaut $N_0 B$ | bloc **levé** : les notes sont justes pour l'aire hachurée. *Complément* : la bande négative porte la même puissance, puissance totale d'un bruit réel dans la bande $2N_0B$. Identifiant retiré |
| 6 | `av-moyenne-dephasage-aleatoire` | lecture « $m_Y$ » confirmée | bloc **levé**, phrase réintégrée dans le bloc *Notes de cours* ; le *Complément* précise que $m_Y$ est constante (donc périodique). Identifiant retiré |
| 7 | `av-dsp-porte-notes` | Armand ne sait pas | bloc **ouvert** (mention ajoutée) ; la valeur $\sigma_a^2\Ts$ reste la proposition, appuyée par la correction du TD |
| 8 | `av-convention-autocorrelation-td` | convention du poly partout | bloc **levé** (différence de convention, pas une erreur), remplacé par un *Complément* en tête des exercices du TD ; fiche matière : « convention retenue ». Identifiant retiré |

Bilan : **3 blocs ouverts** (`av-esperance-exercice-bpsk`, `av-moment-ordre-2-notes`, `av-dsp-porte-notes`), **2 tranchés** (`av-variance-affine`, `av-phase-tf-porte-td`). Identifiants retirés, jamais réutilisés : `av-intervalles-confiance-gaussiens`, `av-puissance-bruit-bande`, `av-moyenne-dephasage-aleatoire`, `av-convention-autocorrelation-td`.

Contrôles après modification : 565 formules compilées sans erreur (MathJax 3.2.2) ; références et identifiants cités résolus ; divs équilibrés.

### 16.1 Blocs 3 et 4 (7 octobre 2026)

Armand laisse le choix à Claude pour `av-esperance-exercice-bpsk` et `av-moment-ordre-2-notes` : les deux propositions sont retenues, et les blocs deviennent **tranchés** (`.tranche`, **Décision** « proposition retenue, choix laissé à Claude ») pour que la correction reste visible :

- `av-esperance-exercice-bpsk` : énoncé de l'exercice p. 77 écrit avec $\E[A_n]$, mention « énoncé corrigé » à la place du segment orange ;
- `av-moment-ordre-2-notes` : $\E[|X|^2] = \sum_n h(x_n)^2 P(X = x_n)$ avec $h(x) = x$, soit $\sum_n |x_n|^2 P(X = x_n)$.

Bilan final : **1 bloc ouvert** (`av-dsp-porte-notes`), **4 tranchés** (`av-variance-affine`, `av-esperance-exercice-bpsk`, `av-moment-ordre-2-notes`, `av-phase-tf-porte-td`), 4 identifiants retirés.
