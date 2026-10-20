# TSIG1 ch. 3 — TFD et interprétation fréquentielle des SLI : rapport d'analyse

> 20 octobre 2026. Document de travail.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `notes` | `sources/tsig1/notes/date-inconnue.pdf` | personnelle | f. 6 r° à f. 8 r° |
| `notes-2023-ch03` | `sources/tsig1/notes/2023-cours-ch03-caracterisation-frequentielle.pdf` | externe (promotion 2023) | p. 1-7 |
| `notes-2023-ch04` | `sources/tsig1/notes/2023-cours-ch04-implementation-filtres.pdf` | externe (promotion 2023) | p. 1 |
| `notes-2023-ch05` | `sources/tsig1/notes/2023-cours-ch05-sli-representation-phase.pdf` | externe (promotion 2023) | p. 3 |
| `fiche-rappels` | `sources/tsig1/notes/externe-fiche-rappels-traitement-signal.pdf` | externe (fiche de synthèse d'un tiers) | p. 3 |
| `illustrations` | `sources/tsig1/support/illustrations-berthoumieu.pdf` (version « TS201 ») | officielle | p. 3-4 |
| `td` | `sources/tsig1/td/recueil-td-2023.pdf` (version « 2023 (v2) ») | officielle | p. 5-6 |
| `corrige-2023-td01` | `sources/tsig1/corriges/2023-td01-systeme-discret-representation-frequence.pdf` | externe (corrigé manuscrit, 2023) | p. 9-12 |

Le f. 6 v° a été photographié trois fois (deux doublons rangés dans `date-inconnue/doublons/`).

## 2. Contenu repris

TFSD ; construction de la TFD (support fini, fenêtre d'observation, exemple du cosinus fenêtré, échantillonnage de l'axe des fréquences, $\Delta f = f_e/M$) ; « TFD ≠ TFSD » ; exemple Matlab ; réponse en fréquence $Y = HX$ avec démonstration ; module et phase ; théorème du retard ; exemple RIF $x[n] - 0{,}5x[n-1]$ par deux méthodes ; remarque sur les fenêtres (rectangulaire, Blackman) ; exemple de la moyenne ; fréquence normalisée ; $H = e^{-j\pi f}\cos\pi f$, passe-bas non idéal, phase linéaire.

## 3. Blocs *À vérifier*

| id | Question |
|---|---|
| `av-tfd-ecriture-exponentielle` | $j$ manquant dans $\exp(-2\pi f n T_e)$ ; signe peu lisible dans la ligne « Attention » |
| `av-matlab-linspace` | `linspace(1/(2Te), 1/(2Te), M)` : borne $-1/(2T_e)$, $M = 512$ ? |
| `av-blackman-lobes-secondaires` | mot partiellement lisible (« prise en compte des lobes secondaires ») |
| `av-exemple-moyenne-ecriture` | $X(f)$ pour $H(f)$, signe « − » recopié, $X(f)$ manquant devant l'exponentielle |
| `av-phase-moyenne-signe` | phase tracée croissante ; calcul : $-\pi f$, décroissante |
| `av-phase-lineaire-retard-groupe` | « phase linéaire → pas de retard de groupe » contredit le f. 12 r° (retard constant, ici $T_e/2$) |
| `av-fenetre-hanning-hamming` | support officiel : fenêtre « Hanning » $0{,}54 + 0{,}46\cos(\cdot)$ : c'est la fenêtre de Hamming ? |
| `av-td-retard-quatre-ecriture` | corrigé TD 1 : « $X(f) = X(f)(1 - e^{-j8\pi f})$ » : lire $Y(f)$ ? |
| `av-td-quadrature-minimum` | corrigé TD 1 : croquis de $\lvert H_A(f)\rvert$ non nul en $f = 0$, alors que $H_A(0) = 0$ |

## 4. Corrections de forme

- f. 7 r° : « $|H(f)|$ : ~~phase~~ module du filtre » : correction déjà faite dans les notes.
- Notation $[\![0, M-1]\!]$ pour les intervalles d'entiers (notes : $[0, M-1]$).

## 5. Choix par défaut

- Compléments : périodicité de la TFSD, expression $W(f) = \tau\sinc(f\tau)$, résolution et fuite spectrale, passage $f n T_e = kn/M$, *zero padding*, FFT, lecture chiffrée de l'exemple Matlab et axe exact des fréquences, module de l'exemple RIF (passe-haut peu sélectif), changement d'indice de la démonstration.
- Figures : cosinus fenêtré ($f_0 = 10$ Hz, $\tau = 0{,}4$ s, valeurs choisies pour la lisibilité), TFD calculée avec les paramètres de l'exemple Matlab (axe exact), module et phase de la moyenne avec gabarit idéal ajouté en pointillés gris (coupure 0,25 arbitraire, figure indicative).

## 6. Sources externes

Intégrées le 20 octobre 2026 à partir de `externes-ch1-3.md`, `externes-ch4-5.md` (avis sur les AV) et `td-exercices.md`.

**Notes 2023 et fiche de rappels** (7 blocs *Notes externes* dans le cours, 2 nouvelles sous-sections) :

- [notes-2023-ch03, p. 1-2] : la TFD comme algorithme (vecteurs de $N$ et $M$ points, deux étapes) ; `sec-tfsd`.
- [notes-2023-ch03, p. 1-2] : fenêtre d'apodisation ; `sec-fenetre-observation`.
- [notes-2023-ch03, p. 3] : *zero padding*, $M \geq N$ (+ *Complément*) ; `sec-echantillonnage-frequentiel`.
- [notes-2023-ch03, p. 4] [fiche-rappels, p. 3] : action fréquentielle, gabarits idéaux PB/PH ; `sec-reponse-frequence`.
- [notes-2023-ch03, p. 4-5] [fiche-rappels, p. 3] : fréquence réduite, écriture « classique » ; `sec-frequence-normalisee`.
- [notes-2023-ch03, p. 5] : nouvelle sous-section `sec-stabilite-reponse-frequence` (`eq-borne-module-stabilite`, + *Complément* : réciproque fausse).
- [notes-2023-ch03, p. 5-6] : nouvelle sous-section `sec-reponse-sinusoide` (`eq-reponse-sinusoide`, + *Complément* : $h$ réelle).
- Deux puces ajoutées à « À retenir ». Pages 6-7 (deux sinusoïdes, retard de groupe) : relèvent du ch. 5, déjà couvertes. Page 8 : résumé, doublon.

**Support d'illustrations (officiel)** [illustrations, p. 3-4] : tableau des fenêtres de pondération (Bartlett, Hann, « Hanning », Blackman), spectre pondéré, diapositive Matlab `wvtool`, exemple des trois sinusoïdes (rectangulaire / Blackman), en texte normal dans `sec-calcul-h-f`, + *Complément* de lecture et nouvel AV `av-fenetre-hanning-hamming`.

**AV existants** (tous restent ouverts) : ligne **Autres sources** ajoutée à `av-tfd-ecriture-exponentielle` (confirmé par les notes 2023 et la fiche), `av-blackman-lobes-secondaires` (sens confirmé par le support officiel, mot toujours illisible), `av-phase-moyenne-signe` (appui indirect, [notes-2023-ch04, p. 1]), `av-phase-lineaire-retard-groupe` (« phase linéaire équivalent à un retard de groupe constant » [notes-2023-ch05, p. 3], fiche p. 3). Rien de nouveau pour `av-matlab-linspace` et `av-exemple-moyenne-ecriture`.

**Exercices du TD** (`sec-exercices-td-ch03`) :

- `exr-td-rif-retard-quatre` (TD 1, II-1, question 2 a-d), + AV `av-td-retard-quatre-ecriture` ;
- `exr-td-filtres-quadrature` (TD 1, II-2), + AV `av-td-quadrature-minimum`.

**Erreurs des sources externes non reprises** :

- [fiche-rappels, p. 3] : propriété du retard « $x((n-k)T_e) \to X(f)\exp(-j2\pi kT_e)$ » ($f$ manquant) ; notre @eq-retard-tfsd est juste.
- [notes-2023-ch03, p. 8] : « $y(n) = \sum_{n=-\infty}^{+\infty} h(k)x(n-k)$ » (indice de sommation $n$).
- [notes-2023-ch03, p. 6] : retard de chaque composante écrit sans le $2\pi$ au dénominateur ; passage non cité (notre ch. 5 a la forme juste), slug réservé `av-retard-composante-2pi` non utilisé.

**Passages illisibles ou douteux** :

- [notes-2023-ch03, p. 5] : indice de la borne « $|H(f)| \leq M_? < \infty$ » illisible ; écrit $M_h$ (borne de la condition de stabilité).
- [notes-2023-ch03, p. 5] : la source mélange $f_n$ et $f_r$ pour la fréquence réduite ; $f_n$ gardé dans le cours, $f_r$ cité.
- [illustrations, p. 4] : graduations des tracés `wvtool` illisibles, couleurs des trois fenêtres non légendées ; les deux spectres de l'exemple ne sont pas légendés (attribution rectangulaire / Blackman d'après l'ordre de la liste, signalée en *Complément*).

## 7. Vérification (étape 6, 20 octobre 2026)

- (a) 50 blocs de formules ; 2 exercices recalculés ($x[n] - x[n-4]$, filtres en quadrature) ; valeurs de l'exemple Matlab ; tableau des fenêtres comparé au PDF.
- (b) Fenêtres : « définies pour $-M \leq n \leq M$ » retiré du texte officiel (absent du support) et passé en *Complément* ; $\tau_g$ → $\tau$ dans `av-phase-lineaire-retard-groupe` ; ligne vide de « À retenir » supprimée.
- (c) `av-matlab-linspace` complété : la photo a(10) porte « `x = cos(2*pi*n*Te)` » sans `f0`, corrigé jusque-là sans signalement dans le code du cours.
- (d) Signe de l'exponentielle de la ligne « Attention » toujours ambigu (AV existant). AV ouverts : 9.

Détail : `verification.md`.
