# EARF1 ch. 3 — Modulations angulaires : rapport d'analyse

> 29 octobre 2026. Document de travail. Étapes 2 à 7 dans la même session ; blocs *À vérifier* tranchés par Claude sur délégation d'Armand.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `mod-ana` | `sources/earf1/support/cours-01-modulations-analogiques.pdf` | officielle | p. 33-53 |
| `td1` | `sources/earf1/td/td01-gnuradio-modulations.pdf` | officielle | p. 7-10 (partie III) |
| `td2` | `sources/earf1/td/td02-modulateurs.pdf` | officielle | p. 1-2 (exercice 1) |
| `td3` | `sources/earf1/td/td03-demodulateurs.pdf` | officielle | p. 2-3 (exercice 2) |
| `notes-2023-ana` | `sources/earf1/notes/2023-notes-modulations-analogiques.pdf` | externe | p. 5-7 |
| `corrige-2023-td01` | `sources/earf1/corriges/2023-td01-principe-modulations.pdf` | externe | p. 3 |
| `corrige-2023-td02` | `sources/earf1/corriges/2023-td02-modulateurs.pdf` | externe | p. 1-2 |
| `corrige-2023-td03` | `sources/earf1/corriges/2023-td03-demodulateurs.pdf` | externe | p. 2-3 |

## 2. Contenu repris

Support p. 34 (principe, phase et fréquence instantanées, avantages), p. 35-37 (FM, $\Delta f$, $\beta$), p. 38-41 (Bessel, tableau, spectres $\beta = 0{,}2$ à 5, propriétés), p. 42-44 (bande pratique, puissance, Carson, modulant quelconque, exemple radio FM), p. 45-47 (génération, démodulation, Armstrong, discriminateur), p. 48-49 (PM), p. 50 (10 questions), p. 52-53 (conclusion, en « Bilan des modulations analogiques ») ; p. 54 placée en tête du chapitre 4.

TD : TD 1 partie III (FM, GNU Radio) ; TD 2 exercice 1 (modulateur à varicap) ; TD 3 exercice 2 (démodulateur à intégrateur). Corrigé 2023 du TD 1 : exercices 4 et 5 (seul l'exemple $\beta = 30$, aux données contrôlables, est repris).

## 3. Blocs *À vérifier* (tous tranchés)

| id | Question | Décision |
|---|---|---|
| `av-signe-serie-bessel` | p. 38 : $(-1)^n$ au lieu de $(-1)^m$ dans la série de $J_n$ | $(-1)^m$ |
| `av-symetrie-bessel` | p. 41 : « $A.J_n(\beta) = (-1)^n J_{-n}(\beta)$ » (facteur $A$ d'un seul côté) | $J_{-n} = (-1)^n J_n$ |
| `av-derivee-fm-facteur-2pi` | p. 47 : $2\pi f_p + k_f m(t)$, facteur $2\pi$ manquant | $2\pi(f_p + k_f m(t))$ |

## 4. Corrections de forme

- Notation : $f_0$ (p. 34-44) et $f_p$ (p. 45-49) harmonisées en $f_p$ (table des notations).
- p. 39 : le tableau complet (17 × 15 valeurs) est remplacé par un extrait arrondi et une figure des courbes ; colonne $\beta = 0{,}5$ ajoutée (calculée) pour le TD.
- TD 1 : deux questions numérotées « III.3 » ; renumérotées dans l'exercice.
- TD 3 fig. 4 : axe nommé « $V_{AM}(t)$ » pour le signal FM (non repris).

## 5. Choix par défaut

- Figures : signal FM et fréquence instantanée (F7), courbes de Bessel (F8, calculées), spectres FM recalculés avec la zone de Carson (F9), modulateur d'Armstrong (F10), discriminateur (F11), simulation du TD 3 exercice 2 (F12, fréquences 3 et 6 kHz choisies d'après l'allure de la figure).
- Compléments : FM à bande étroite, zéro de $J_0$, identité $\sum J_n^2 = 1$, vérification de Carson (0,999 et 0,998), multiplication de fréquence (Armstrong), limiteur, $k_p = 2\pi k_f$, comparaison FM/PM.
- TD 1 III.6 : « nombre d'harmoniques » interprété comme $2N + 1$ raies avec $N$ = partie entière de $\beta + 1$ (choix justifié : ce sont les raies dans la bande de Carson ; chaque cas contient au moins 98 % de la puissance).
- Solutions des TD sans corrigé (TD 1) rédigées par Claude en *Complément* ; corrigés 2023 en *Notes externes*, complétés et contrôlés.

## 6. Sources externes : erreurs non reprises

- [notes-2023-ana, p. 7] : question 1 « fréquence ou amplitude » (faux : fréquence ou phase) ; question 5 « symétriques autour de 0 » (de $f_p$) ; question 7 « $B_s = 2\beta_{FM}$ » (facteur $f_m$ manquant) : corrigés en *Complément*.
- [notes-2023-ana, p. 6] : « nombre de raies utiles : $2(\beta + 1)f_m$ » (confond nombre de raies et bande) : non repris.
- [corrige-2023-td01, p. 3] : exercice 6 (« 9 raies → $\beta_{FM} = 1{,}5$ ») incohérent avec Carson ($N = 4$ donnerait $\beta = 3$) et énoncé absent : non repris. Exercice 4 ($B = 24$ kHz) : données absentes, non repris.
- [corrige-2023-td03, p. 3] : suit une autre version de l'énoncé (ordre des fréquences inversé) : signalé.

## 7. Vérification (étape 6)

- Toutes les diapositives p. 33-53 reprises.
- Recalculs : $\theta_i$ par intégration, tableau de Bessel (scipy) et spectres de la p. 40 (toutes les valeurs affichées concordent), $\sum_{|n| \leq \beta + 1} J_n^2$, exemple radio FM (180 kHz), dérivée du signal FM, TD 1 ($P_C$ = 0,499 / 0,4996 / 0,492 V², $BW_C$ = 2,1 / 2,8 / 7,7 kHz), TD 2 ($\lambda = -1\ \mathrm{V^{-1}}$, $k_f = 7{,}5\ \mathrm{MHz/V}$, $C + C_0 = 196$ pF, $C = 166$ pF, $L = 13{,}5$ nH), exemple 2023 (155 kHz).
- Rendu Quarto sans avertissement ; formules compilées (MathJax 3.2.2).

## 8. Validation (étape 7)

Validé le 29 octobre 2026 sur délégation d'Armand ; statut `valide`.
