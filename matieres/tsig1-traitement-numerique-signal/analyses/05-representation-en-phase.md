# TSIG1 ch. 5 — SLI et représentation en phase : rapport d'analyse

> 20 octobre 2026. Document de travail.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `notes` | `sources/tsig1/notes/date-inconnue.pdf` | personnelle | f. 12 r° à f. 13 r° |
| `notes-2023-ch05` | `sources/tsig1/notes/2023-cours-ch05-sli-representation-phase.pdf` | externe (promotion 2023) | p. 1-4 |
| `notes-2023-ch04` | `sources/tsig1/notes/2023-cours-ch04-implementation-filtres.pdf` | externe (promotion 2023) | p. 5, 7 |
| `td` | `sources/tsig1/td/recueil-td-2023.pdf` (version « 2023 (v2) ») | officielle | p. 4-6, 9 |
| `corrige-2023-td01` | `sources/tsig1/corriges/2023-td01-systeme-discret-representation-frequence.pdf` | externe (corrigé manuscrit, 2023) | p. 6-8, 13 |
| `corrige-2023-td03` | `sources/tsig1/corriges/2023-td03-placement-poles-zeros-rii.pdf` | externe (corrigé manuscrit, 2023) | p. 1-2, 4 |

Le chapitre n'a pas de titre dans les notes (le f. 12 r° commence par « I Contexte ») : titre repris des notes 2023 (ch. 5).

## 2. Contenu repris

Contexte (deux sinusoïdes, retards différents) ; retard de groupe ; phase linéaire → retard constant ; filtre à phase linéaire, phase nulle non causale, RIF décalé ; zéros par paires $\{z_i, z_i^{-1}\}$, $h(n) = \pm h(M - n)$ ; minimum de phase : cas étudié $H_1 = (z-b)/(z+a)$, $H_2 = (bz-1)/(z+a)$, égalité des modules, passe-tout $A$, $r_{H_2} = r_{H_1} + r_A$, calcul de $r_A = (1-b^2)/(1 - 2b\cos\omega + b^2)$ ; définition du minimum de phase ; $H = H_\mathrm{min} A$.

## 3. Blocs *À vérifier*

| id | Question |
|---|---|
| `av-module-passe-tout` | carré du sinus et terme $b^2\sin^2\omega$ manquants : la démonstration ne conclut pas telle qu'écrite |
| `av-phase-nulle-symetrie-tf` | notes 2023 : $j$ manquant dans $e^{-j\beta\omega + \alpha}$, exposant du terme $\tilde h[-2]$, cas antisymétrique non signalé |
| `av-rif-phase-lineaire-exposant` | notes 2023 : « $z^{-M}\sum h(n)\,z$ » : exposant de $z$ manquant ($z^{n}$) |
| `av-td-gabarit-signes` | corrigé TD 1 : $h[2] = \pm\frac12$, $h[0] = \pm\frac14$ : signes liés (opposés) et fixés par $H(e^{j0{,}5\pi}) = 1$ |
| `av-td-minimum-phase-decomposition` | corrigé TD 3 : $H_1 = H_2 H_3$ avec $H_2$ « minimum de phase » : rôles de $H_1$ et $H_2$ intervertis |

## 4. Corrections de forme

- f. 13 r° : « $H_\mathrm{min}(A)$ » pour $H_\mathrm{min}(z)$.
- f. 12 v° : deux lignes raturées ($\sqrt{1+b^2}$) non reprises.
- Harmonisation de notre propre texte (pas d'une source) : la phase linéaire s'écrit $-2\pi D f + \beta$ dans `sec-retard-groupe` ; @eq-phase-lineaire et la puce correspondante de « À retenir » écrivaient $e^{-j(2\pi D f + \beta)}$ (soit $-2\pi Df - \beta$) : remplacé par $e^{j(-2\pi D f + \beta)}$ (20 octobre 2026).

## 5. Choix par défaut

- Compléments : signe du retard de phase et distorsion de phase ; exemple chiffré ($\frac12$ échantillon) ; zéros conjugués pour des coefficients réels, $D = M/2$ ; détail de la différence des dérivées ; méthode de construction de $H_\mathrm{min}$ (inverses conjugués).
- Figures : RIF symétrique de longueur 9 (sinus cardinal tronqué) avant et après décalage ; pôles-zéros de $H_1$, $H_2$ et retards de groupe calculés ($a = 0{,}5$, $b = 0{,}6$) ; le script vérifie $|H_1| = |H_2|$, $|A| = 1$, la formule de $r_A$ et $r_{H_2} \geq r_{H_1}$.

## 6. Sources externes

Intégrées le 20 octobre 2026 à partir de `externes-ch4-5.md` et `td-exercices.md`.

**Notes 2023** (4 blocs *Notes externes* dans le cours) :

- [notes-2023-ch05, p. 1, 3] [notes-2023-ch04, p. 7] : $\omega$ normalisée, phase linéaire $\Leftrightarrow$ retard de groupe constant ($-\beta\omega + \alpha$) ; `sec-retard-groupe` (+ *Complément*).
- [notes-2023-ch05, p. 3] : passage du filtre à phase nulle au RIF causal, justification par la symétrie $\tilde h[2] = \tilde h[-2]$ ; `sec-phase-lineaire` (+ AV `av-phase-nulle-symetrie-tf`).
- [notes-2023-ch05, p. 4] : `prp-rif-phase-lineaire-zeros` ($H(z) = z^{-M} H(z^{-1})$, couples de zéros) avec démonstration ; `sec-phase-lineaire` (+ AV `av-rif-phase-lineaire-exposant`, + *Complément*).
- [notes-2023-ch05, p. 2-3] : $H_2 = A\,H_\mathrm{min}$, zéros **et pôles** de $H_\mathrm{min}$ dans $\mathcal{C}_1$ ; `sec-definition-minimum-phase` (+ *Complément*).
- Non intégré (déjà couvert) : cas $H_1$, $H_2$ et égalité des modules (p. 1), décomposition $H_2 = A H_1$ et arctangentes (p. 1-2).

**AV existant** : `av-module-passe-tout` reste ouvert ; ligne **Autres sources** ajoutée (calcul complet et juste dans [notes-2023-ch05, p. 1] et, en général, [notes-2023-ch04, p. 5]).

**Exercices du TD** (`sec-exercices-td-ch05`) :

- `exr-td-filtre-phase-nulle` (TD 1, II, causalité et filtre à phase nulle) ;
- `exr-td-gabarit-rif-symetrique` (TD 1, II-3), + AV `av-td-gabarit-signes` ;
- `exr-td-poles-zeros-phase-lineaire` (TD 3, I), + AV `av-td-minimum-phase-decomposition`.

Corrigés incomplets (solutions données en *Complément*) : TD 1 § II-3 (module non tracé), TD 3 § I q. 1 ($h_1[n]$) et q. 2-c. Coquille du recueil reprise sans bloc : TD 3 § I, troisième sous-question numérotée « -a » (signalée dans l'énoncé) ; « réponse fréquentielles ».

**Erreurs des sources externes non reprises** :

- [notes-2023-ch05, p. 1] : « $0 < a, b \leq 1$ » au lieu de $0 < a, b < 1$ (avec $a = 1$, pôle sur le cercle ; avec $b = 1$, $H_1 = H_2$) ; nos notes sont correctes.
- [notes-2023-ch05, p. 2] : signes faux dans la dérivée de l'arctangente et dans $r_A$ ; résultat final cohérent avec @eq-retard-groupe-passe-tout.
- [td, p. 4-5] (TD 1 § II, q. 3) : phase donnée $\operatorname{Arg}(H(\omega)) = \omega$ croissante (avance) ; sans effet sur les amplitudes demandées, non signalée en bloc.

**Passages illisibles ou douteux** :

- [notes-2023-ch05, p. 2] : dénominateur « $1 - - 1$ » de $r_A$ : griffonné, non repris.
- [notes-2023-ch05, p. 1] : annotation « ⚠ $\omega$ » : seul le symbole est lisible (interprétée comme une mise en garde sur la normalisation).
- [notes-2023-ch05, p. 3] : tracés schématiques sans valeurs, non redessinés (@fig-phase-lineaire-rif existe déjà).

## 7. Vérification (étape 6, 20 octobre 2026)

- (a) 64 blocs de formules ; $r_A$ refait et comparé à `scipy.signal.group_delay` ; 3 exercices recalculés (phase nulle, gabarit symétrique, TD3 $H_1$/$H_2$/$H_3$ et valeurs en dB).
- (b) « (égal à $D$) » retiré du bloc `.notes` (absent des notes) et passé en *Complément*.
- (c) `av-td-gabarit-signes` complété : le corrigé p. 13 écrit « $h(1)[-e^{-j\omega} + e^{-j3\omega}]$ », corrigé jusque-là sans signalement dans la solution.
- (d) Ce signe moins est une lecture probable (trait parasite possible) ; « $\omega = 2\pi f$ » de la définition reste une précision de Claude dans `.notes`. AV ouverts : 5.

Détail : `verification.md`.
