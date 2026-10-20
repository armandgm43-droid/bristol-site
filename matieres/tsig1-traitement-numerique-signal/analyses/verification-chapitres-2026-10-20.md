# TSIG1 — Vérification (étape 6), chapitres 1 à 5

Date : 20 octobre 2026. Vérification faite par Claude sur les qmd de `cours/`, en contrôlant les photos des notes d'Armand, les pages PNG des notes et corrigés 2023, le recueil de TD (PDF) et le support d'illustrations (PDF).

## Bilan général

- **Exactitude** : toutes les formules centrées relues (≈ 290 blocs `$$`), 16 exercices de TD et tous les blocs *Complément* chiffrés recalculés (numpy, scipy, sympy) : **aucune erreur mathématique** dans le texte de Claude.
- **Blocs *À vérifier*** : 30 blocs relus contre leur source (photo ou page). **Toutes les citations sont fidèles, tous les problèmes sont réels, toutes les propositions sont justes.** Aucun AV n'accuse à tort une source correcte : aucun n'est supprimé. 3 AV sont complétés (deux contenus de source corrigés sans signalement, voir ch. 3 et ch. 5), 1 AV reformulé (notation).
- **Catégories** : 4 passages de Claude placés dans des blocs `.notes` (ajouts absents des notes) déplacés en *Complément* ; 1 passage du texte officiel (précision absente du support) déplacé en *Complément*.
- **Forme** : labels uniques dans la matière (aucun doublon), tous les liens entre chapitres pointent sur un label existant, blocs `:::` équilibrés (`check_divs.py` : OK ×5), rendu Quarto sans avertissement ni erreur, aucune référence `?@` non résolue, **1 801 formules compilées par MathJax 3.2.2 sans erreur**.
- **Cohérence entre chapitres** : $x[n] = x(nT_e)$, $T_e$, $f_e = 1/T_e$, TF en $e^{-j2\pi ft}$, $\sinc(x) = \sin(\pi x)/(\pi x)$, fréquence normalisée $f_n = f/f_e \in [-\frac12, \frac12]$ ($f_r$ cité pour 2023), $\omega = 2\pi f$ normalisée : cohérents. Retard de groupe : $\tau$ dans la définition (ch. 5), $r_H$ dans les calculs repris des notes (signalé en *Complément*) ; le ch. 3 utilisait $\tau_g$, aligné sur $\tau$.
- **À retenir** : chaque résultat listé existe dans le chapitre, avec ses conditions.

Compte des AV ouverts : ch. 1 : 1 ; ch. 2 : 4 ; ch. 3 : 9 ; ch. 4 : 11 ; ch. 5 : 5 ; **total 30** (inchangé).

---

## Chapitre 1 — Échantillonnage et signal discret

**(a) Points vérifiés.** 38 blocs de formules : peigne de Dirac et sa série de Fourier ($c_k = 1/T_e$), TF du peigne, périodisation $\frac{1}{T_e}\sum_k X_a(f - kf_e)$, gain $T_e$ du filtre de reconstruction, calcul complet de $h_\mathrm{rec}(t) = T_e \sin(\pi f_e t)/(\pi t) = \sinc(f_e t)$, formule d'interpolation, débit $96\,000 \times 16 = 1{,}536$ Mbit/s, condition $f_{\max} \leq f_e - f_{\max}$. AV `av-indices-entiers-naturels` contrôlé sur la photo a (« $n \in \mathbb{N}$ » bien écrit, à côté de $x[-1]$) et sur [notes-2023-ch01, p. 1] (même écriture). Échantillonnage des notes externes : p. 1 (paramètres $T_e$, $B$ « support binaire », remarque sur le choix de $T_e$), p. 5 (identification $C = T_e$, BF/HF), p. 7 (cas $T_e = T_0/2$, « $x(\ ) = 0$ », vecteur) : conformes.

**(b) Corrections.** Aucune.

**(c) AV.** Aucun modifié ni supprimé.

**(d) Restant douteux.** Rien de nouveau.

---

## Chapitre 2 — Systèmes discrets et convolution

**(a) Points vérifiés.** 36 blocs de formules ; démonstrations (convolution, condition nécessaire et suffisante de stabilité avec l'entrée $h^*[-n]/|h[-n]|$, causalité). 4 exercices recalculés : convolution graphique ($y = 1, 4, 8, 8, 3, -2, -1$ pour $n = -1 \dots 5$, valeurs de $h$ et $x$ relues sur le graphe [td, p. 3]) ; deux portes (trapèze $7, 14, 21, 28, 28, 21, 14, 7$ pour $n = 4 \dots 11$) ; cascade d'exponentielles ($\alpha = 2$, $\beta = -1$, égalité des deux méthodes vérifiée sur 10 termes) ; propriétés du RIF. Exemple 2D des illustrations : $38$ confirmé sans retournement du masque (avec retournement : 31), donc le *Complément* « corrélation » est juste. AV vérifiés sur la photo a(6) (« $y(n) = 0{,}5x[n] - 0{,}2y[n]$ », indice illisible de « $0{,}25x[\,?\,]$ » confirmé en zoom), a(8) (ligne rouge pâle sur la latence) et [notes-2023-ch02, p. 1 et 3] (citations exactes, dont « $k = 0$ (causalité) » sous $\sum x(k)h(n-k)$). Corrigé TD1 p. 5 (méthode 1, $\alpha$, $\beta$) : conforme.

**(b) Corrections.** Aucune.

**(c) AV.** Aucun modifié ni supprimé.

**(d) Restant douteux.** Rien de nouveau.

---

## Chapitre 3 — TFD et interprétation fréquentielle des SLI

**(a) Points vérifiés.** 50 blocs de formules ; démonstrations de $Y = HX$ et du théorème du retard ; $|1 - 0{,}5e^{-j\theta}|^2 = 1{,}25 - \cos\theta$ ; $H = e^{-j\pi f}\cos(\pi f)$ ; valeurs de l'exemple Matlab ($\tau = 2{,}56$ s, $\Delta f \approx 0{,}195$ Hz, premier zéro à $\pm 0{,}39$ Hz, axe exact après `fftshift`). 2 exercices recalculés : $y[n] = x[n] - x[n-4]$ ($H = 2j e^{-j4\pi f}\sin 4\pi f$, $H(\frac14) = 0$, $H(\frac18) = 2$, phase par morceaux $\pm\frac{\pi}{2} - 4\pi f$, $y = 2\cos(\pi n/4)$) ; filtres en quadrature ($|H_A| = 2\sin^2\pi f$, $|H_C| = 2\cos^2 \pi f$, $H_C(f) = H_A(f - \frac12)$, somme égale à 2). Tableau des fenêtres comparé à [illustrations, p. 3] (formules exactes, « Hanning » bien écrit avec 0.54/0.46). AV vérifiés sur les photos a(10), a(11), a(12), a(14), a(15), [notes-2023-ch04, p. 1], [corrige-2023-td01, p. 9 et 12] : tous fidèles.

**(b) Corrections.**

- Fenêtres : « définies pour $-M \leq n \leq M$ (longueur $2M + 1$) [illustrations, p. 3] » dans le texte officiel → retiré ; le support ne donne pas l'intervalle. L'interprétation est passée dans le *Complément* qui suit (« le support ne précise pas l'intervalle de $n$ ; les expressions sont celles de fenêtres centrées… »).
- AV `av-phase-lineaire-retard-groupe` : notation $\tau_g$ → $\tau$, avec lien vers la définition du ch. 5 (cohérence de notation).
- À retenir : ligne vide parasite dans la liste supprimée.

**(c) AV.**

- `av-matlab-linspace` **complété** : la photo a(10) (et ses doublons a(11), a(12)) porte « `x = cos(2*pi*n*Te);` », **sans `f0`**, alors que le code du cours écrit `cos(2*pi*f0*n*Te)` (correction silencieuse, la transcription avait lu `f0`). Ajout du point dans **Source**, **Problème** et **Proposition** (`x = cos(2*pi*f0*n*Te)`, forme retenue dans le code et dans @fig-tfd-cosinus).
- `av-phase-lineaire-retard-groupe` : notation seulement (voir b).

**(d) Restant douteux.** Signe de l'exponentielle dans la ligne « Attention TFD ≠ TFSD » de la photo a(10) : toujours ambigu (couvert par `av-tfd-ecriture-exponentielle`). Dans [corrige-2023-td01, p. 9], la dernière ligne encadrée « $|H(f)| = 2j e^{-j4\pi f}\sin(4\pi f)$ » : les barres peuvent être le bord du cadre ; non signalé (la solution du cours écrit $H(f) = \dots$ et $|H(f)| = 2|\sin 4\pi f|$).

---

## Chapitre 4 — Implémentation des SLI et équations aux différences

**(a) Points vérifiés.** 103 blocs de formules ; factorisation pôles-zéros, module et phase d'un facteur élémentaire ; exemple complet (pôles $-\frac34$, $\frac12$, $A = \frac35$, $B = \frac25$, $h[n]$ comparée à la récurrence sur 5 termes) ; variante 2023 (pôles $\frac34$, $-\frac12$, $A = \frac25$, $B = \frac35$, lien $z \to -z$) ; zéro $0{,}9625$. 7 exercices recalculés : porte (TF en $\sin(\pi N f)/\sin(\pi f)$, TFD sur $N$ points $= N\delta[k]$) ; trapèze $an + b$ (formule de $X(z)$ vérifiée par sympy pour $N = 3, 4, 5, 7$) ; équation d'ordre 2 (zéros $0{,}25 \pm 0{,}25j$, $|H|$ croissant de $0{,}625$ à $1{,}625$ ; pôles $0{,}47 \pm 0{,}528j$, $\Delta = -1{,}1164$, arguments $\pm 0{,}2686\pi$, $|H(0)| = 1{,}786$, max $2{,}677$ ($8{,}55$ dB) en $f = 0{,}1255$, $|H(\frac12)| = 0{,}410$) ; $1 + z^{-1}$ ; $(1 + z^{-1})^2$ ; $(1 - z^{-1})^3$ ($8|\sin\pi f|^3$, phase $-3\pi f - \frac{\pi}{2}$) ; RII $0{,}8e^{\pm j2\pi/3}$ ($h[n]$ par la formule = récurrence sur 10 termes, maximum $3{,}21$ en $f = 0{,}336$) ; $G(z) = H(-z^2)$ ($h[k] = (\frac14)^{\lfloor k/2 \rfloor}$, $g = 1, 0, -1, 0, \frac14, 0, -\frac14, 0, \frac{1}{16}$, pôles de module $1/\sqrt2$). Annexe du recueil relue dans le PDF (« $d^l x(t)/dt^p$ », « $(K > L)$ Système causal » : conformes). AV vérifiés sur la photo b(2), [notes-2023-ch04, p. 4-5], [corrige-2023-td02, p. 2-4], [corrige-2023-td03, p. 2] : tous fidèles.

**(b) Corrections.**

- Bloc `.notes` du contexte RIF : « (forme en cosinus, comme la moyenne de deux échantillons du chapitre 3) » → « (forme en cosinus) » ; le renvoi au ch. 3, absent des notes, passe dans le *Complément* suivant.
- Bloc `.notes` de la transformée en $z$ : « Afin d'étudier l'existence de $|H(f)|$ » → « Afin de montrer l'existence » (mot des notes, f. 10 r°).
- Bloc `.notes` du type de zone de convergence : « la majoration décroît quand $r$ augmente, et la zone… » → « la zone… » ; l'explication, absente des notes, passe dans le *Complément* suivant.
- Solution 2023 de $y = x[n] + 2x[n-1] + x[n-2]$, question 6 : « zéro (double) » → « zéro » (le corrigé n'écrit pas « double ») ; la multiplicité est ajoutée au *Complément* suivant.

**(c) AV.** Aucun modifié ni supprimé.

**(d) Restant douteux.** Photo b(2) : dans la formule du module, le signe de l'exposant de « $z_l e^{\,?j2\pi f}$ » est peu lisible (le moins est net dans la ligne de la phase) ; la transcription et le cours écrivent $e^{-j2\pi f}$, ce qui est juste. Corrigé TD2 p. 3, Q6 de $1 + z^{-1}$ : « Pas de pôles ($z = e^{j\pi}$ » ; le cours lit « zéro en $z = -1 = e^{j\pi}$ », interprétation sûre mais non écrite mot pour mot.

---

## Chapitre 5 — SLI et représentation en phase

**(a) Points vérifiés.** 64 blocs de formules ; les deux dérivées d'arctangente et $r_A = (1 - b^2)/(1 - 2b\cos\omega + b^2)$ refaits à la main et comparés à `scipy.signal.group_delay` ($a = 0{,}5$, $b = 0{,}6$) ; $H(z) = z^{-M}H(z^{-1})$. 3 exercices recalculés : filtre à phase nulle ($H_1 = |H|^2$, $H_2 = 2|H|\cos\operatorname{Arg}H$, $\sqrt2$ en $\frac{\pi}{4}$) ; gabarit RIF symétrique (solution unique $(\frac14, 0, -\frac12, 0, \frac14)$, $|H| = \sin^2\omega$) ; TD3 ($h_1 = 3{,}306 ; 3{,}636 ; 3 ; 1{,}1 ; 0{,}3025$, $h_2 = 1 ; 2{,}368 ; 4{,}608 ; 2{,}368 ; 1$, $|H_1| = |H_2|$, $21{,}1$ / $1{,}63$ dB en $f = 0{,}351$ / $1{,}87$ dB en $\frac13$ / $5{,}45$ dB, crochet minimum $1{,}206$, retard de groupe de $H_3$ positif partout). AV vérifiés sur la photo b(6), [notes-2023-ch05, p. 3-4], [corrige-2023-td01, p. 13], [corrige-2023-td03, p. 2] : tous fidèles.

**(b) Corrections.**

- Bloc `.notes` : « le retard de groupe est constant (égal à $D$) » → « …constant » ; la valeur $D$ (calcul de Claude, juste) passe dans le *Complément* suivant (« avec $\omega = 2\pi f$, $-D\omega + \beta$ donne $\tau = D$ »).

**(c) AV.**

- `av-td-gabarit-signes` **complété** : [corrige-2023-td01, p. 13] écrit « $h(1)[-e^{-j\omega} + e^{-j3\omega}]$ » (signe moins, lecture probable), alors que la solution du cours écrit $h[1][e^{-j\omega} + e^{-j3\omega}]$ sans le signaler. Le point est ajouté (**Source**, **Problème** (a), **Proposition**) ; la ligne suivante du corrigé est juste.

**(d) Restant douteux.** Le signe moins de « $[-e^{-j\omega}$ » du corrigé p. 13 est très probable mais peut être un trait parasite (à confirmer par Armand lors de la levée de l'AV). Définition du retard de groupe : « $\omega = 2\pi f$ » est une précision de Claude dans le bloc `.notes` (laissée, cohérente avec le ch. 3).
