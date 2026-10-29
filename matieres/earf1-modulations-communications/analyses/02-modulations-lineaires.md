# EARF1 ch. 2 — Modulations linéaires : rapport d'analyse

> 29 octobre 2026. Document de travail. Étapes 2 à 7 dans la même session ; blocs *À vérifier* tranchés par Claude sur délégation d'Armand.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `mod-ana` | `sources/earf1/support/cours-01-modulations-analogiques.pdf` | officielle | p. 19-32 |
| `td1` | `sources/earf1/td/td01-gnuradio-modulations.pdf` | officielle | p. 2-4 (partie I) |
| `td3` | `sources/earf1/td/td03-demodulateurs.pdf` | officielle | p. 1-2 (exercice 1) |
| `notes-2023-ana` | `sources/earf1/notes/2023-notes-modulations-analogiques.pdf` | externe | p. 3-4 |
| `corrige-2023-td01` | `sources/earf1/corriges/2023-td01-principe-modulations.pdf` | externe | p. 1-2 |
| `corrige-2023-td03` | `sources/earf1/corriges/2023-td03-demodulateurs.pdf` | externe | p. 1-2 |

## 2. Contenu repris

Support p. 20 (principe AM, trois types), p. 21-25 (AMDBSP : principe, sinusoïdal et quelconque, modulation, démodulation cohérente, problème du déphasage), p. 26-29 (AMDBAP : principe, taux $k$, allures pour $k < 1$, $= 1$, $> 1$, $k = (S_\mathrm{max} - S_\mathrm{min})/(S_\mathrm{max} + S_\mathrm{min})$, spectre, génération, démodulation), p. 30-31 (BLU : principe, filtrage, variante à $\Delta f$), p. 32 (11 questions, en exercice). Le dessin humoristique de la p. 24 (tour Eiffel, plage) est résumé par la phrase « la porteuse de réception n'est pas en phase ».

TD : TD 1 partie I (AM, GNU Radio) ; TD 3 exercice 1 (détecteur d'enveloppe, application OOK). Corrigé 2023 du TD 1 (ancienne version, énoncé absent) : exercices 1 et 2, repris comme « exemples d'application » avec les seules données lisibles.

## 3. Blocs *À vérifier* (tous tranchés)

| id | Question | Décision |
|---|---|---|
| `av-condition-surmodulation` | notes 2023 : $|k| < 1$ ; support : $k = 1$ encore exploitable | $k \leq 1$ (support), marge $k < 1$ en pratique |
| `av-bornes-spectre-dbap` | p. 28 : les deux bornes notées $f_p + B_m$ | $f_p - B_m$ et $f_p + B_m$ |
| `av-niveau-05-td3` | TD 3 fig. 2 : rôle du niveau 0,5 V | seuil de décision (comme le corrigé 2023) |

## 4. Corrections de forme

- p. 25 : « AMDPSP » (étiquette du schéma) → AMDBSP ; p. 31 : « rejection » → « réjection ».
- p. 29 : $A[1 + k\,m(t)]$ avec $m$ normalisé, alors que p. 26 écrit $A + m(t)$ : expliqué en *Complément* (pas une erreur).
- TD 3 : « signa d'entrée » → « signal d'entrée ».

## 5. Choix par défaut

- Figures recalculées (matplotlib) : AMDBSP temporel (F3), AMDBAP pour trois $k$ (F4), spectres des trois AM pour un modulant quelconque (F5) ; simulation du détecteur d'enveloppe sur le signal OOK du TD 3 (F6, *Complément*, $R_1C_1 = 0{,}3\ \mu$s).
- Section « Puissance et rendement » en *Complément* (rendement $k^2/(2 + k^2)$, formule du TD 1) : le support ne la donne pas, mais le TD la demande.
- Questions de la p. 32 : réponses des notes 2023 (*Notes externes*), complétées (*Complément*) pour les questions 1 et 8.
- TD 1 partie I : solution rédigée par Claude (*Complément*) ; colonne « simulation » non remplie (machine).
- TD 3 exercice 1 : rangé dans ce chapitre (le détecteur d'enveloppe démodule l'AM) ; l'application OOK y est traitée aussi, avec un lien depuis le chapitre 4.
- Le taux de modulation noté $m$ par le TD 1 est noté $k$ dans le cours (table des notations).

## 6. Sources externes : erreurs non reprises

- [corrige-2023-td01, p. 2] : « $f_p - f_m = 100{,}1$ kHz » (pour $f_p + f_m$) : signalé en *Complément*.
- [corrige-2023-td01, p. 1] : le spectre dessiné porte « 100 » pour la porteuse et le calcul divise par 50 : cohérent ($kA/2$), repris avec l'explication.

## 7. Vérification (étape 6)

- Toutes les diapositives p. 19-32 reprises.
- Recalculs : produit $\cos^2$, déphasage $\cos\varphi$, $S_\mathrm{max}/S_\mathrm{min}$, trois raies de l'AMDBAP, démodulation AMDBAP, puissance et rendement (33,3 % et 11,1 %), dBV ($-3{,}0$ et $-9{,}0$), exemples 2023 ($600{,}0$ kHz, 6892 V², 137,8 W, $1/19 = 5{,}3\ \%$), condition sur $R_1C_1$ ($\tau < T_b/\ln 2$).
- Rendu Quarto sans avertissement ; formules compilées (MathJax 3.2.2).

## 8. Validation (étape 7)

Validé le 29 octobre 2026 sur délégation d'Armand ; statut `valide`.
