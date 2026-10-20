# TSIG1 ch. 2 — Systèmes discrets et convolution : rapport d'analyse

> 20 octobre 2026. Document de travail.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `notes` | `sources/tsig1/notes/date-inconnue.pdf` | personnelle | f. 4 r° à f. 5 r° |
| `notes-2023-ch02` | `sources/tsig1/notes/2023-cours-ch02-systemes-discrets-lineaires-invariants.pdf` | externe (promotion 2023) | p. 1, 3-6 |
| `illustrations` | `sources/tsig1/support/illustrations-berthoumieu.pdf` (version « TS201 ») | officielle | p. 5-6 |
| `td` | `sources/tsig1/td/recueil-td-2023.pdf` (version « 2023 (v2) ») | officielle | p. 3-5 |
| `corrige-2023-td01` | `sources/tsig1/corriges/2023-td01-systeme-discret-representation-frequence.pdf` | externe (corrigé manuscrit, 2023) | p. 1-6, 8-9 |

## 2. Contenu repris

Système discret, exemples (max, combinaison, récursif) ; linéarité et invariance, exemples et contre-exemples ; convolution discrète et démonstration ; stabilité (entrée bornée, sortie bornée), CNS $\sum|h| < \infty$ avec démonstration des deux sens ; causalité, exemples, $h[n] = 0$ pour $n < 0$ ; association série et parallèle.

## 3. Blocs *À vérifier*

| id | Question |
|---|---|
| `av-exemple-systeme-recursif` | $y = 0{,}5x[n] - 0{,}2y[n]$ : sans doute $y[n-1]$ ? |
| `av-exemple-lineaire-indice` | indice du second terme de l'exemple linéaire peu lisible ($x[n-1]$ ?) |
| `av-latence-temps-reel` | ligne rouge pâle : « latence $\tau_\mathrm{lat}$ ; temps réel : $\tau_\mathrm{lat} < T_e$ » ? |
| `av-convolution-causale-bornes` | notes 2023 : $\sum_{k=0}^{+\infty} x[k]\,h[n-k]$ pour un système causal : la borne $k = 0$ ne vaut que pour la forme $\sum h[k]\,x[n-k]$ ? |

## 4. Corrections de forme

- f. 4 r° : flèches de l'invariance notées « TF » au-dessus (lu ainsi) : il s'agit du passage par le système $T$ ; écrit $x[n] \to y[n]$.
- f. 4 r° : le titre « Propriété de stabilité des systèmes linéaires invariants » (mot « linéaires » ajouté au-dessus de la ligne) repris tel quel.

## 5. Choix par défaut

- Tableau des exemples de causalité ; compléments : contre-exemple de linéarité (entrée nulle), vérification de la non-invariance de $n\,x[n]$, commutativité de la convolution, condition $h[-n] \neq 0$ de l'entrée choisie dans la démonstration, longueur d'une cascade de RIF.
- Pas de figure (les schémas des notes sont des schémas-blocs simples, décrits dans le texte).

## 6. Sources externes

Intégrées le 20 octobre 2026 à partir de `externes-ch1-3.md` et `td-exercices.md`.

**Notes 2023** (5 blocs *Notes externes* dans le cours) :

- [notes-2023-ch02, p. 1] : autres exemples de transformations ($\max\{x[n], x[n+1]\}$, $x^2[n]$) ; `sec-systeme-discret`.
- [notes-2023-ch02, p. 1] : exemples linéaire / affine et démonstration de la non-linéarité de $a\,x[n] + b$ (+ *Complément*) ; `sec-linearite`.
- [notes-2023-ch02, p. 5] : masque de convolution qui « circule centré » ; `sec-convolution-discrete`.
- [notes-2023-ch02, p. 4 et 6] : RIF immédiatement stable, exemple $\delta[n+1] + \delta[n] + \delta[n-1]$ (+ *Complément* : non causal) ; `sec-stabilite-sli`.
- [notes-2023-ch02, p. 3] : tableau d'exemples de causalité, « système temps réel est causal : $\tau_\text{latence} < T_e$ » ; `sec-causalite`, suivi du nouvel AV `av-convolution-causale-bornes`.
- Pages 2 et 6 (reste) : doublons.

**Support d'illustrations (officiel)** [illustrations, p. 5-6] : convolution 1D par fenêtre glissante, convolution 2D, filtres de Gabor, CNN (texte normal + *Complément* : la « convolution » des CNN est une corrélation).

**AV existants** (tous restent ouverts, ligne **Autres sources** ajoutée) : `av-exemple-systeme-recursif` (appui indirect), `av-exemple-lineaire-indice` (même structure en 2023), `av-latence-temps-reel` (même ligne, lisible, dans les notes 2023 ; le livrable proposait de lever le bloc : décision laissée à Armand).

**Exercices du TD** (`sec-exercices-td-ch02`, énoncés [td], solutions [corrige-2023-td01] en *Notes externes*, contrôles en *Complément*) :

- `exr-td-convolution-graphique` (TD 1, I-1, application 1) ;
- `exr-td-convolution-portes` (TD 1, I-1, application 2) ;
- `exr-td-cascade-exponentielles` (TD 1, I-2) ;
- `exr-td-rif-proprietes` (TD 1, II-1, question 1).

**Erreurs des sources externes non reprises** :

- [notes-2023-ch02, p. 4] : entrée du contre-exemple de stabilité « $x(k) = \frac{h^*(-k)}{|h(k)|}$ » (indices mélangés) et « $y(0) = \frac{\sum h(k)h^*(-k)}{|h(k)|}$ » ; notre démonstration est juste.
- [corrige-2023-td01, p. 2] : « $y(n) = \sum_{n=-\infty}^{+\infty} h(n-k)\,x(k)$ » (indice de sommation $n$ au lieu de $k$) ; la solution écrit directement @eq-convolution-discrete.

**Passages illisibles ou douteux** :

- [notes-2023-ch02, p. 1] : invariance, « $x(n-k) \to y(n-3)$ » : dernier indice probablement $k$ mal formé ; non repris.
- [notes-2023-ch02, p. 5] : « masque qui circule centré » : « centré » lu avec une confiance moyenne.

## 7. Vérification (étape 6, 20 octobre 2026)

- (a) 36 blocs de formules ; 4 exercices recalculés (convolution graphique, deux portes, cascade d'exponentielles, RIF) ; exemple 2D des illustrations ($38$, sans retournement) confirmé.
- (b) Aucune correction.
- (c) 4 AV contrôlés sur les photos a(6), a(8) et [notes-2023-ch02, p. 1, 3] : citations fidèles, problèmes réels, gardés tels quels.
- (d) Rien de nouveau. AV ouverts : 4.

Détail : `verification.md`.
