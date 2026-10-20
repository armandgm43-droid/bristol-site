# TSIG1 ch. 4 — Implémentation des SLI et équations aux différences : rapport d'analyse

> 20 octobre 2026. Document de travail.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `notes` | `sources/tsig1/notes/date-inconnue.pdf` | personnelle | f. 9 r° à f. 11 r° |
| `notes-2023-ch04` | `sources/tsig1/notes/2023-cours-ch04-implementation-filtres.pdf` | externe (promotion 2023) | p. 1-7 |
| `notes-2023-ch05` | `sources/tsig1/notes/2023-cours-ch05-sli-representation-phase.pdf` | externe (promotion 2023) | p. 2 |
| `td` | `sources/tsig1/td/recueil-td-2023.pdf` (version « 2023 (v2) ») | officielle | p. 7-11 |
| `corrige-2023-td02` | `sources/tsig1/corriges/2023-td02-transformee-z-equation-differences.pdf` | externe (corrigé manuscrit, 2023) | p. 1-5 |
| `corrige-2023-td03` | `sources/tsig1/corriges/2023-td03-placement-poles-zeros-rii.pdf` | externe (corrigé manuscrit, 2023) | p. 2-3 |

Le titre du f. 9 r° porte « Ch 2 » (lecture probable, encre rouge) alors que la page suit le chapitre 3 : le numéro 4 est retenu (choix par défaut, ordre des notes).

## 2. Contenu repris

RIF (toujours stables, faiblement réjecteurs) et RII ; analogie RC ; forme générale des équations différentielles ; approximation de la dérivée ; équation aux différences et exemples RIF/RII ; $H(f)$ puis $H(z) = N/D$ ; transformée en $z$, cercle unité ; stabilité par la zone de convergence ; zone de convergence d'un système causal ; factorisation pôles-zéros, module et phase ; cellule d'ordre 1 ; décomposition en éléments simples et condition $|p_k| < 1$ ; exemple complet ($p = \frac12, -\frac34$ ; $A = \frac35$, $B = \frac25$).

## 3. Blocs *À vérifier*

| id | Question |
|---|---|
| `av-bornes-factorisation` | produits de $l = 0$ à $L-1$ : $L$ facteurs pour un polynôme de degré $L-1$ |
| `av-rif-somme-cosinus-exposant` | notes 2023 : $H(f) = e^{-j2\pi f}\,2\cos(\pi f)$ pour $1 + e^{-j2\pi f}$ : exposant $-j\pi f$ ? |
| `av-phase-facteur-elementaire-signe` | notes 2023 : signe moins dans l'arctangente de $\operatorname{Arg}(1 - \alpha e^{-j\omega})$, contraire à la partie imaginaire $+b\sin(\omega - \theta)$ |
| `av-roc-inclusion-disque` | notes 2023 : « $\mathrm{ROC}(H(z)) \subset \mathcal{C}_1$ » : inclusion inversée ($\mathcal{C}_1 \subset \mathrm{ROC}$) ? |
| `av-td-annexe-derivee` | recueil de TD (annexe) : $\mathrm{d}^l x/\mathrm{d}t^p$ au lieu de $\mathrm{d}t^l$ |
| `av-td-tfd-porte` | corrigé TD 2 : $M$ et $N$ intervertis ; échantillons de la TFD de la porte placés hors des zéros |
| `av-td-trapeze-interpretation` | corrigé TD 2 : « trapèze » traité comme convolution de deux portes au lieu de $an + b$ |
| `av-td-discriminant-stabilite` | corrigé TD 2 : « $\Delta < 0$ donc instable » puis « stable » |
| `av-td-rif-poles-origine` | corrigé TD 2 : « pas de pôles » pour $1 + z^{-1}$ et $(1 + z^{-1})^2$ (pôles en $z = 0$) |
| `av-td-phase-binomial-signe` | corrigé TD 2 : $e^{+j2\pi f/f_e}$ au lieu de $e^{-j2\pi f/f_e}$ ; argument du cosinus de la légende |
| `av-td-rii-ou-rif` | corrigé TD 3 : filtre récursif déclaré « RIF » |

## 4. Corrections de forme

- f. 9 v° : deuxième « II » de la page (numérotation des sections) : sections renumérotées.
- f. 10 v° : « $H(t)$ » pour $H(z)$ dans la remarque sur $\alpha^n u[n]$.
- f. 10 v° : les racines du dénominateur sont notées $z_1$, $z_2$ : notées $p_1$, $p_2$ (pôles), signalé en *Complément*.
- f. 10 r° : indices raturés dans la première écriture de $H(z)$.

## 5. Choix par défaut

- Compléments : stabilité des RIF, différence arrière causale, forme récursive de l'algorithme, zone de convergence $|z| > \max|p_k|$, lecture géométrique du module, $A z/(z-p) \leftrightarrow A p^n u[n]$, valeurs $A_0 = \frac25$, $A_1 = \frac35$ (non reportées dans les notes) et contrôle par récurrence ($h[0] = 1$, $h[1] = -\frac14$).
- Figures : cellule d'ordre 1 ($\alpha = \pm 0{,}8$, réponses impulsionnelles ajoutées) ; diagramme pôles-zéros et $h[n]$ de l'exemple (h[n] vérifiée par récurrence dans le script).

## 6. Sources externes

Intégrées le 20 octobre 2026 à partir de `externes-ch4-5.md` et `td-exercices.md`.

**Notes 2023** (8 blocs *Notes externes* dans le cours) :

- [notes-2023-ch04, p. 1] : RIF non causal `eq-rif-non-causal`, exemple $x[n] + x[n-1]$, RII non implémentable par convolution ; `sec-contexte-rif-rii` (+ AV `av-rif-somme-cosinus-exposant`, + *Complément*).
- [notes-2023-ch04, p. 2] : masques de dérivation d'ordres 1 et 2 ; `sec-analogie-continu`.
- [notes-2023-ch04, p. 2 et 7] : deux filtres récursifs, usage RIF/RII ; `sec-forme-generale-equation-differences`.
- [notes-2023-ch04, p. 3 et 7] : $\omega$ et $f$ normalisées, généralisation de la TF ; `sec-interpretation-frequentielle-equations`.
- [notes-2023-ch04, p. 4] : théorème du retard pour la TZ, `prp-retard-transformee-z` avec démonstration ; `sec-cellule-ordre-1` (+ AV `av-roc-inclusion-disque`).
- [notes-2023-ch04, p. 5] : module et phase d'un facteur $(1 - \alpha z^{-1})$, `eq-module-facteur-elementaire`, `eq-phase-facteur-elementaire` ; `sec-poles-zeros` (+ AV `av-phase-facteur-elementaire-signe`).
- [notes-2023-ch04, p. 5] : éléments simples en $z^{-1}$ ; `sec-generalisation-elements-simples`.
- [notes-2023-ch04, p. 5-6] : variante de l'exemple complet, `exm-rii-ordre-2-variante` ; `sec-exemple-complet-rii`.
- Non intégré (déjà couvert) : généralisation de la TF en TZ et ROC (p. 3), théorème du retard de la TFSD (p. 2), cellule d'ordre 1 (p. 4), « cas de la phase » (p. 7, relève du ch. 5).

**AV existant** : `av-bornes-factorisation` reste ouvert ; ligne **Autres sources** ajoutée (produits sans bornes dans [notes-2023-ch04, p. 5] et [notes-2023-ch05, p. 2]).

**Exercices du TD** (`sec-exercices-td-ch04`, précédés d'une remarque reprenant l'annexe du recueil [td, p. 11], + AV `av-td-annexe-derivee`) :

- `exr-td-porte-trapeze` (TD 2, I), + AV `av-td-tfd-porte`, `av-td-trapeze-interpretation` ;
- `exr-td-equation-differences-ordre-2` (TD 2, II), + AV `av-td-discriminant-stabilite` ;
- `exr-td-rif-somme-deux` (TD 2, III, q. 1-7), + AV `av-td-rif-poles-origine` ;
- `exr-td-rif-binomial-ordre-2` (TD 2, III, q. 8), + AV `av-td-phase-binomial-signe` ;
- `exr-td-rif-difference-ordre-3` (TD 2, III, q. 9 ; pas de corrigé : solution en *Complément*) ;
- `exr-td-rii-poles-complexes` (TD 2, III, q. 10) ;
- `exr-td-filtre-transforme-moins-z2` (TD 3, II), + AV `av-td-rii-ou-rif`.

Corrigés incomplets (solutions données en *Complément*) : TD 2 § II (premier cas), § III q. 9 et q. 10 ($h[n]$ arrêté à $h[1]$), TD 3 § II q. 4. Coquilles du recueil sans effet sur le sens (« défini » pour « définie », TD 2) reprises sans bloc.

**Erreurs des sources externes non reprises** : aucune hors des AV ci-dessus.

**Passages illisibles ou douteux** :

- [notes-2023-ch04, p. 1] : exposant de l'exponentielle encadrée lu « $-j2\pi f$ » avec une bonne certitude (d'où l'AV).
- [notes-2023-ch04, p. 7] : coefficient « $0{,}77$ » de $x[n-1]$ : lecture nette, valeur inhabituelle.
- [corrige-2023-td02, p. 4] : exposant 2 de la légende « $4\cos\,2\pi f/f_\mathrm{ech}$ » peu lisible (dans `av-td-phase-binomial-signe`).

## 7. Vérification (étape 6, 20 octobre 2026)

- (a) 103 blocs de formules ; exemple complet et variante 2023 recalculés (comparés à la récurrence) ; 7 exercices recalculés (porte, trapèze par sympy, ordre 2, trois RIF, RII à pôles complexes, $G(z) = H(-z^2)$) ; annexe du recueil relue.
- (b) Quatre ajouts de Claude retirés des blocs `.notes` / `.notes-externes` et placés en *Complément* : renvoi « comme la moyenne… du ch. 3 », « la majoration décroît quand $r$ augmente », « zéro (double) » ; « Afin d'étudier » → « Afin de montrer » (mot des notes).
- (c) 11 AV contrôlés (photo b(2), notes 2023 p. 4-5, corrigés TD2 et TD3) : tous fidèles et justifiés, gardés tels quels.
- (d) Signe de l'exposant dans la formule du module (photo b(2)) peu lisible, version juste retenue. AV ouverts : 11.

Détail : `verification.md`.
