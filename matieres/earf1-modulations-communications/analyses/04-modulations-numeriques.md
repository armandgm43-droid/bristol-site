# EARF1 ch. 4 — Introduction aux modulations numériques : rapport d'analyse

> 29 octobre 2026. Document de travail. Étapes 2 à 7 dans la même session ; blocs *À vérifier* tranchés par Claude sur délégation d'Armand.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `mod-num` | `sources/earf1/support/cours-02-modulations-numeriques.pdf` (30 p.) | officielle | p. 1-30 |
| `mod-ana` | `sources/earf1/support/cours-01-modulations-analogiques.pdf` | officielle | p. 54 |
| `td1` | `sources/earf1/td/td01-gnuradio-modulations.pdf` | officielle | p. 6, 10 (parties II et IV) |
| `td2` | `sources/earf1/td/td02-modulateurs.pdf` | officielle | p. 2-3 (exercices 2 et 3) |
| `notes-2023-num` | `sources/earf1/notes/2023-notes-modulations-numeriques.pdf` | externe | p. 1 |
| `corrige-2023-td01` | `sources/earf1/corriges/2023-td01-principe-modulations.pdf` | externe | p. 3-4 |
| `corrige-2023-td02` | `sources/earf1/corriges/2023-td02-modulateurs.pdf` | externe | p. 2-4 |

## 2. Contenu repris

mod-ana p. 54 (de l'analogique vers le numérique) ; mod-num p. 4-5 (principe, critères, compromis), p. 7-10 (allures, constellation IQ, modulateur IQ), p. 12-14 (OOK), p. 15-17 (BPSK), p. 18-20 (QPSK), p. 21 (MPSK), p. 22 (QAM), p. 23-27 (FSK, CPFSK, MSK, GMSK), p. 29-30 (bilan, métrique). Sommaires p. 2-3, 6, 11, 28 non repris.

TD : TD 1 parties II (ASK numérique) et IV (FSK) ; TD 2 exercices 2 (FSK par la varicap) et 3 (OOK par l'alimentation). Corrigé 2023 du TD 1 : exercices 3 (OOK) et 7 (8PSK).

## 3. Blocs *À vérifier* (tous tranchés)

| id | Question | Décision |
|---|---|---|
| `av-unite-symbol-rate` | p. 12, 15, 18, 30 : vitesse de transmission en « Bits/s » | en bauds |
| `av-dphi-16qam` | p. 22 : « $\Delta\varphi = \pi/8 = 45°$ » | $\pi/4 = 45°$ entre les coins ; valeur $\pi/8$ écartée |
| `av-lobe-msk` | p. 26-27 : lobe MSK « $1{,}75 \times D$ » | théorie $1{,}5D$ ; $1{,}75D$ = lecture de la mesure |

## 4. Corrections de forme

- p. 18 : « Quadratic Phase Shift Keying » → *Quadrature* Phase Shift Keying (nom usuel de la QPSK) ; « états ou Symbols » → symboles.
- p. 7 : porteuse notée $f_0$ (PSK) et $f_c$ ailleurs : signalé en *Complément*.
- p. 16, 19-20, 26-27 : bandes « $[-D, +D]$ » des spectres mesurés (tracés autour de 0) : expliqué en *Complément* (spectres centrés sur la porteuse).
- p. 21 : « $\Delta\varphi_{MPSK} \approx 2\pi/2^{N_{sym}}$ » : égalité exacte signalée en *Complément*.
- TD 2 : « Ou $C_0$… » → « Où » ; « excercice » → « exercice ».

## 5. Choix par défaut

- Figures : allures ASK/FSK/PSK (F13, recalculées), constellations OOK, BPSK, QPSK, 8PSK, 16QAM (F14 ; pas d'étiquettes binaires pour 8PSK et 16PSK, peu lisibles sur le support), modulateur IQ (F15), densités spectrales théoriques BPSK/QPSK/MSK (F16, *Complément*).
- Tableau récapitulatif (lignes 8PSK et 16QAM en *Complément*) ; tableau MQAM.
- TD 1 parties II et IV : fichiers de simulation absents ; méthode et réponses générales en *Complément* ; hypothèse explicite pour les noms des modulations « 1 » et « 2 » (OOK et ASK antipodale), à confirmer en séance.
- Bande FSK : $2(\Delta f + D)$ (forme de Carson du corrigé 2023), le support n'en donnant pas.
- Lien vers TS227 (cours de G. Ferré cité p. 30 du support).

## 6. Sources externes : remarques

- [corrige-2023-td02, p. 3] : la question GMSK (exercice 3, q. 5 de l'énoncé 2026) est traitée en « 4) » de l'exercice 2 : version différente de l'énoncé ; reprise à sa place.
- [corrige-2023-td02, p. 2] : $f_1 = 101$ MHz calculé exactement (pas d'approximation petit signal) ; repris avec un *Complément* sur la validité.

## 7. Vérification (étape 6)

- Toutes les diapositives de contenu reprises.
- Recalculs : relation IQ ($\cos(x + \pi/2) = -\sin x$), $\eta$ de chaque modulation, $\Delta\varphi$ 8PSK/16PSK, $\log_2 M$ des MQAM, MSK ($2\pi\Delta f T_r = \pi/2$), TD 2 ($C_{Dv}(0{,}7) = 0{,}6156\,C_0$, $f_1 = 100{,}96$ MHz, $f_0 = 97{,}96$ MHz, $\Delta f = 1{,}5$ MHz, $BW = 11$ MHz, $\eta = 0{,}36$ ; OOK 8 MHz), exemples 2023 (10 kbit/s, 20 kHz ; 8PSK $\eta = 1{,}5$).
- Spectre MSK théorique : premier zéro à $0{,}75D$ (figure F16).
- Rendu Quarto sans avertissement ; formules compilées (MathJax 3.2.2).

## 8. Validation (étape 7)

Validé le 29 octobre 2026 sur délégation d'Armand ; statut `valide`.
