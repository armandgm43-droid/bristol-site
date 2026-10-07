# TS227 — Chapitre 4 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow (`CONTEXTE_PROJET.md`, section 11), enchaînées dans la même session que le chapitre 1, à la demande d'Armand (conversation « Bristol — TS227 Chapitres 1 et 4 — Rédaction », 7 octobre 2026).
> Chapitre : *Transmission en présence de bruit*. Fichier : `cours/04-transmission-presence-bruit.qmd`. Statut : `flashcards` (étapes 6 à 8, sections 17-18).
> Règle appliquée : `conventions.md` § 14 (choix de forme, de figures et de rédaction appliqués par défaut, section 12 ; questions bloquantes en section 14).

---

## 0. Résumé

- Le support couvre le chapitre 4 aux **pages 89 à 138** du PDF (diapositives 79 à 119/161). Après suppression des pages de plan, des écrans « Sortez vos téléphones » et des animations (p. 90-93, 95-97, 101-106 et 135-136 se complètent ou se répètent), il reste environ **30 pages utiles**.
- Notes : **f. 3 r° (bas), f. 3 v°, f. 4 r°, f. 4 v° (haut)**. Elles apportent le calcul complet du seuil optimal, la démonstration de la généralisation à la M-PAM (« 2 points au bord, M − 2 points avec 2 voisins »), la **définition de la fonction Q** (absente du support), la **construction de Gray en miroir**, les choix de $\lambda$ du filtre adapté et le dessin du filtre adapté causal.
- TD intégré : **ex. 3** (filtre adapté, causalité), **ex. 4** (probabilité d'erreur, bruit filtré, $E_b/N_0$), **ex. 5, q. 12-13** (bruit et fiabilité). Les questions 1-2 et 4-5 de l'ex. 4 de la correction sont reprises ; ex. 3 q. 3-4, ex. 4 q. 3-4 et ex. 5 q. 12-13 n'ont pas de corrigé (solutions en *Complément*).
- Blocs *À vérifier* : 11 ouverts à l'analyse (section 7 : 6 sur le support, 2 sur les notes, 3 sur le TD), **tous tranchés** à l'étape 3 (section 16).
- 7 nouvelles figures matplotlib ; la chaîne de transmission réutilise la figure du chapitre 2.

Citations : `[poly, p. N]` = page du PDF ; `[notes, f. 3 v°]` ; `[td, p. N]` ; `[td-correction, p. N]`. Réponses des quiz : lues dans le code `#QDLE#…#` de chaque diapositive (l'astérisque suit la bonne réponse ; convention vérifiée sur les quiz p. 25, 34 et 51 déjà traités au chapitre 2).

---

## 1. Inventaire des sources

| id | Fichier | Nature | Pages utilisées | Remarque |
|---|---|---|---|---|
| `poly` | `sources/ts227/support/poly_ts227.pdf` | officielle | 89-138 | version du 9 octobre 2025 |
| `notes` | `sources/ts227/notes/date-inconnue.pdf` (+ photos) | personnelle | f. 3 r° (bas), f. 3 v°, f. 4 r°, f. 4 v° (haut) | date inconnue |
| `td` | `sources/ts227/support/TD_TS_227.pdf` | officielle | p. 3 (ex. 3, ex. 4), p. 4 (ex. 5, q. 12-13) | énoncé 2020/2021 |
| `td-correction` | `sources/ts227/support/correction_TD_TS_227.pdf` | officielle | p. 9-14 | autre version de l'énoncé |

---

## 2. Plan du support pour le chapitre 4

| Partie du poly | Pages PDF | Pages utiles | Pages écartées |
|---|---|---|---|
| Probabilités d'erreur | 89-93 | 93 (version complète de 90-92) | 89 (plan), 90-92 (animations) |
| Cas binaire | 94-113 | 97, 99, 100, 101-102, 103-107, 108, 110, 111, 112, 113 | 94 (plan), 95-96 (versions incomplètes de 97), 98 et 109 (« Sortez vos téléphones ») |
| Cas M-aire | 114-123 | 115, 116-120, 122, 123 | 114 (plan), 121 (« Sortez vos téléphones ») |
| Récepteur optimal | 124-130 | 125-130 | 124 (plan) |
| Partage du canal de Nyquist | 131-132 | 132 | 131 (plan) |
| Lien entre $P_b$ et $E_b/N_0$ | 133-138 | 134, 135, 137, 138 | 133 (plan), 136 (doublon de 135) |

---

## 3. Correspondance support ↔ notes

| Notes | Contenu | Support |
|---|---|---|
| f. 3 r°, milieu-bas | erreur symbole comme réunion d'évènements, $P_s = \sum_m P(\hat{A}_n \neq a_m \mid A_n = a_m) P(A_n = a_m)$ ; $P_b$ (sans les probabilités a priori : AV) ; $R_n = g_0 A_n + Z'_n$ ; association $0 \to -1$, $1 \to 1$ | p. 90-97 |
| f. 3 v° | $P(\hat{B}_n = 1 \mid B_n = 0) = \int_{\gamma + g_0}^{\infty} f_Z$ ; $P_b(\gamma)$ ; dérivée ; calcul complet de $\gamma^*$ (encadré) ; « a priori » ; médiatrice si $p_0 = p_1$ et bruit gaussien ; dB = 10 log₁₀ d'un rapport de puissance | p. 105-108, 113 |
| f. 4 r°, haut | définition de $Q$ (lecture douteuse : AV) ; $P_s$ équiprobable ; calcul 4-PAM | p. 112, 115-119 |
| f. 4 r°, milieu | démonstration de $P_s = 2\frac{M-1}{M}Q$ ; $P_b \geq P_s/\log_2 M$ (encadré) | p. 120, 123 |
| f. 4 r°, bas | construction miroir de Gray ($M = 2, 4, 8$) ; « $g_0$ et $\sigma$ dépendent du choix du filtre » | p. 123 (Gray nommé seulement) |
| f. 4 v°, haut | $g(t) = \int G e^{j2\pi ft}$ ; $h_a = \lambda h^*(-t)$ (encadré), « maximise $g_0/\sigma$ » ; dessin $h$, $h^*(-t)$, retard $D \geq \Ts$ ; triangle ; $g = \lambda R_h$, $G = \lambda\lvert H\rvert^2$ ; $\lambda = 1$ ou $1/R_h(0)$ | p. 125-130 |

---

## 4. Contenu présent uniquement dans les notes (blocs `.notes`)

1. Ordre du cours (chapitre 4 traité avant le chapitre 3).
2. Écriture de l'erreur symbole par réunion d'évènements disjoints.
3. Association $B_n \to A_n$ dessinée.
4. Calcul complet du seuil optimal (le support saute les étapes) et terme « a priori ».
5. « Médiatrice » et condition « bruit gaussien ».
6. dB = $10\log_{10}$ d'un rapport de puissance.
7. Définition de $Q$ (le support ne la donne pas).
8. Calcul de $P_s$ de la 4-PAM terme à terme ; démonstration de la généralisation.
9. Construction de Gray en miroir (tableau `tbl-gray-miroir`).
10. « $g_0$ et $\sigma$ dépendent du choix des filtres ».
11. $g = \lambda R_h$, $G = \lambda\lvert H\rvert^2$, choix de $\lambda$.
12. Dessin du filtre adapté causal (retard $D \geq \Ts$) → figure.

---

## 5. Informations redondantes

- Notes = support (support conservé, sans bloc) : $P_s$ équiprobable, $\gamma^*$, $P_s$ M-PAM, $P_b \geq P_s/\log_2 M$, $h_a = \lambda h^*(-t)$.
- Support : p. 90-92 et 95-96 (animations), p. 136 (doublon de 135).
- TD ex. 4 q. 7 et poly p. 137 ($M = 2$) donnent le même $Q(\sqrt{2E_b/N_0})$ : le cours renvoie de l'un à l'autre.

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Chaîne de transmission | `02-chaine-bande-de-base.svg` (réutilisée) | `fig-chaine-bruit` | poly p. 95 (= p. 19) | TikZ (ch. 2) |
| Densités conditionnelles, seuil | `04-densites-conditionnelles.py` | `fig-densites-conditionnelles` | poly p. 103-106 | matplotlib |
| Seuil optimal $\gamma^*(p_0)$ | `04-seuil-optimal.py` | `fig-seuil-optimal` | poly p. 108 | matplotlib |
| $P_b = Q(g_0/\sigma)$ | `04-pb-rsb.py` | `fig-pb-rsb` | poly p. 113 | matplotlib |
| 4-PAM, seuils | `04-seuils-4pam.py` | `fig-seuils-4pam` | poly p. 116-119 | matplotlib |
| Filtre adapté à une porte | `04-filtre-adapte-porte.py` | `fig-filtre-adapte-porte` | notes f. 4 v° ; td-correction p. 10-11 | matplotlib |
| $P_{b,\min}$ (Eb/N0), M = 2…16 | `04-pb-eb-n0.py` | `fig-pb-eb-n0` | poly p. 138 | matplotlib |
| Échantillons bruités 4-PAM | `04-constellation-bruitee.py` | `fig-constellation-bruitee` | TD ex. 5 q. 12 (reconstruite) | matplotlib |

Figures régénérées sur le PC d'Armand (matplotlib 3.10) et relues en image. Non reprises : schémas-blocs du récepteur (p. 126-130), redondants avec la chaîne.

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | État | Source | Résumé |
|---|---|---|---|
| `av-pb-notes-probabilites-a-priori` | ouvert | notes f. 3 r° | $P_b$ écrit sans $P(B_k = 0)$, $P(B_k = 1)$ ; marque « ^ » douteuse sur le $B_k$ conditionnant |
| `av-variables-muettes` | ouvert | poly p. 107, p. 128 | dérivée écrite avec $z$ au lieu de $\gamma$ ; intégrale en $u$ avec $\mathrm{d}t$ |
| `av-quiz-seuil-ook` | ouvert | poly p. 110 | réponse « 0,5 » ; juste $\gamma^* = g_0/2$, donc 0,5 seulement si $g_0 = 1$ |
| `av-quiz-pire-probabilite` | ouvert | poly p. 111 | réponse marquée « 0 » ; attendu 0,5 (déjà relevé, `CONTEXTE_PROJET.md` § 18.4) |
| `av-facteur-calcul-pb` | ouvert | poly p. 112 | facteur 0,5 manquant à la 2ᵉ ligne du calcul (résultat juste) |
| `av-definition-q-notes` | ouvert | notes f. 4 r° | numérateur de $Q$ lu « $x$ » (ou « 1 » mal formé) |
| `av-variance-bruit-filtre` | ouvert | poly p. 127 | $\E[\lvert Z_l(n\Ts)\rvert^2]$ au lieu de $Z'_l$ |
| `av-filtre-adapte-causal` | ouvert | poly p. 130 | $h_a(t) = h(t - T_h)$ sans retournement ; notes, TD et correction : retournement (déjà relevé, § 18.4) — **contradiction entre sources** |
| `av-densite-conditionnelle-td` | ouvert | td-correction p. 12 | densité sachant $A_n = 1$ écrite avec $(r + v(0))^2$ |
| `av-dsp-bruit-filtre-td` | ouvert | td-correction p. 13 | $\Gamma_{n'_l} = \lvert G_a\rvert^2 \Gamma_{n'_l}$ (entrée au lieu de sortie) |
| `av-variance-bruit-discret-td` | ouvert | td p. 3, ex. 4 q. 3 | « $\sigma_{n_l}^2 = N_0/2$ » : vrai seulement avec bande limitée et $T_e = 1$ |

Vérifié sans problème : seuil optimal p. 107 (recalculé, et identique aux notes) ; limites p. 108 ; $P_b = Q(g_0/\sigma)$ ; seuils et probabilités 4-PAM p. 117-119 ; $P_s = 2\frac{M-1}{M}Q$ et cas particuliers ; quiz p. 99 (A), p. 100 (C), p. 122 (D) ; $g_0$ p. 126 ; $\sigma^2$ p. 127 (hors coquille) ; Cauchy-Schwarz et maximum p. 128 ; $E_b$ et $P_{b,\min}$ p. 134-137 ($\sigma_a^2 = (M^2-1)/3$ recalculé) ; courbes p. 113 et 138 recalculées (ex. M = 16 à 15 dB : ≈ 2·10⁻², comme le support) ; correction du TD ex. 3 q. 1-2 et ex. 4 (hors coquilles).

Points d'imprécision traités **sans bloc** (pas d'erreur de sens, choix listés en section 12) :

- p. 101 : inégalités larges dans les deux branches de la décision → *Complément* (évènement de probabilité nulle) ;
- p. 107 : « log » = ln → *Complément* ;
- p. 119 : intertitre « À l'intérieur : » placé avant les probabilités des extrémités → intertitre non repris (choix 9) ;
- p. 123 (et p. 129, 134, 137) : $P_b$ écrit avec « = » alors que c'est l'approximation de Gray → *Complément* (condition manquante) ;
- p. 128 : $\lambda \in \mathbb{R}^+$ (support) / $\lambda \in \mathbb{C}^*$ (correction du TD), $h(-t)$ / $h^*(-t)$ → *Complément* conciliant ;
- p. 132 : canal noté $H_l(f)$ → *Complément* de notation ;
- p. 135 : $\Gamma_{s_l} = \sigma_a^2\lvert H\rvert^2/\Ts$ sans rappeler « symboles iid centrés » → *Complément* ;
- TD ex. 4 q. 2 : $\gamma$ désigne $g_0^2/\sigma^2$ → noté $\rho$ dans Bristol.

---

## 8. Passages illisibles ou ambigus dans les notes

| Où | Lecture | Traitement |
|---|---|---|
| f. 3 r°, réunion d'évènements | borne « $n - 1$ » ou « $M - 1$ » ($M$ écrit comme « Π ») | lu $M - 1$, cohérent avec la somme qui suit (pas de question) |
| f. 3 r°, $P_b$ | marque « ^ » sur le $B_k$ conditionnant ; lettre barrée devant le second terme | dans `av-pb-notes-probabilites-a-priori` |
| f. 4 r°, $Q(x)$ | numérateur « $x$ » ou « 1 » ; argument « $x$ » écrit comme un « $n$ » | `av-definition-q-notes` |
| f. 4 r°, $P_s$ 4-PAM | premier terme « $\mid A_n = 0$ » | lu $A_n = a_0$ (motif des termes suivants ; pas de question) |
| f. 4 r°, dernier terme | « 2Q » avec le 2 barré | lu $Q$, cohérent avec $\frac{3}{2}Q$ |
| f. 4 v°, triangle | deux droites qui se croisent en plus du triangle | seul le triangle est repris (figure du TD) |
| f. 3 v°, « A prio… » | mot coupé au bord de la photo | lu « a priori » |

---

## 9. Compléments ajoutés (catégorie *Complément*)

| # | Complément | Justification |
|---|---|---|
| C1 | Introduction (plan du chapitre) | aucune source ne le donne |
| C2 | Probabilités totales, notations majuscules | étape implicite |
| C3 | Lien de $R_n = g_0A_n + Z'_n$ avec le modèle discret du ch. 2 | relie deux chapitres |
| C4 | Justifications des quiz p. 99, 100, 122 | le support ne donne que la réponse |
| C5 | Notation $f_Z$ / $f_{Z'}$ ; égalité $R_n = \gamma$ | imprécision p. 101, 104-107 |
| C6 | log = ln ; vérification du minimum | précision |
| C7 | Interprétation du déplacement du seuil | |
| C8 | Étapes du changement de variable p. 112 | étape non écrite |
| C9 | $Q = 1 - \Phi$, propriétés, $Q(4)$ | lien avec le ch. 3 |
| C10 | Cohérence $20\log_{10}$ / $10\log_{10}$, valeurs lues | relie support et notes |
| C11 | Distance $g_0$ aux seuils (4-PAM) ; conditions de $P_s$ M-PAM | |
| C12 | Justification de $P_b \geq P_s/\log_2 M$, approximation de Gray | condition manquante p. 123 |
| C13 | Gray miroir = étiquetage de la correction du TD (ex. 1) et du ch. 2 | |
| C14 | Démonstration de $g_0$ (TF inverse) | |
| C15 | Étapes du calcul de $\sigma^2$ (filtrage, gaussianité) | renvois ch. 3 |
| C16 | Application de Cauchy-Schwarz ; $\lambda$ ; cas complexe | |
| C17 | $\lambda = 1/E_h$ donne $g_0 = 1$ | interprétation des notes |
| C18 | Origine de $P_{b,\min}(E_h)$ | |
| C19 | Cas complexe de $R_h$, instants d'échantillonnage | |
| C20 | Demi-Nyquist : lien avec $\lvert H\rvert^2$, racine de cosinus surélevé (non cité par le support) | |
| C21 | Conditions de $P = \sigma_a^2E_h/\Ts$ | |
| C22 | Étapes de $E_b$, $\sigma_a^2$, cas binaire, +3 dB, lecture de la figure | |
| C23 | Solutions TD ex. 3 q. 3-4, ex. 4 q. 3-4, ex. 5 q. 12-13 | sans corrigé |

---

## 10. TD intégré au chapitre

| TD (énoncé) | Contenu | Où | Corrigé |
|---|---|---|---|
| ex. 3, q. 1-2 | filtre adapté à la porte, version causale, $v(t)$ | `exr-td-filtre-adapte` | correction p. 9-10 |
| ex. 3, q. 3-4 | critère de Nyquist, causalité | idem | aucun → C23 |
| ex. 4, q. 1-2 | $r_n$, $P_b$ 2-PAM | `exr-td-probabilite-erreur` | correction p. 11-12 (AV densité) |
| ex. 4, q. 3-4 | variance et autocorrélation du bruit discret | idem | aucun → C23 + `av-variance-bruit-discret-td` |
| ex. 4, q. 5-6 | bruit filtré, densité | idem | correction q. 3-4, p. 12-13 (AV DSP) |
| ex. 4, q. 7 | $P_b(E_b/N_0)$ | idem | correction q. 5, p. 13-14 |
| ex. 5, q. 12-13 | bruit $\sigma^2 = 1/16$, fiabilité | `exr-td-constellation-bruitee` | aucun → C23 |
| correction ex. 3, q. 4 | tracé des signaux | **non intégré** (absent de l'énoncé, sans corrigé) | — |

---

## 11. Plan retenu

1. Introduction (`sec-intro-bruit`) — p. 95 ; notes (ordre du cours)
2. Probabilités d'erreur (`sec-probabilites-erreur`) — p. 90-93 ; notes f. 3 r°
3. Cas binaire (`sec-modulation-binaire`) : hypothèses, quiz, seuil optimal, $P_b$, $Q$, RSB — p. 95-113 ; notes f. 3 r°-f. 4 r°
4. Cas M-aire (`sec-modulation-m-aire`) : $P_s$, 4-PAM, M-PAM, quiz, $P_b$, Gray — p. 114-123 ; notes f. 4 r°
5. Récepteur optimal (`sec-recepteur-optimal`) — p. 124-130 ; notes f. 4 v°
6. Partage optimal du canal de Nyquist (`sec-demi-nyquist`) — p. 132
7. Lien entre $P_b$ et $E_b/N_0$ (`sec-pb-eb-n0`) — p. 133-138
8. Exercices du TD (`sec-exercices-td-bruit`)
9. À retenir (`sec-retenir-bruit`)

---

## 12. Choix appliqués par défaut (`conventions.md` § 14)

**Plan et rédaction**

1. Ordre du poly conservé ; ordre réel du cours signalé en bloc `.notes` dans l'introduction.
2. Variables aléatoires en majuscules ($A_n$, $B_n$, $R_n$, $Z'_n$), comme le support ; indices harmonisés en $n$ (le support mélange $\hat{B}_k$ et $\hat{B}_n$, p. 103-106 : correction sans bloc, section 13).
3. Densité du bruit notée $f_Z$ (support p. 107 et notes) ; $f_{Z'}$ conservé dans l'exemple 4-PAM, comme le support (p. 117-118), avec un complément de notation.
4. Quiz p. 99, 100, 110, 111, 122 en exercices `exr-` : réponse du support en `.solution`, justification en *Complément* ; pour p. 110 et 111, bloc *À vérifier* après la réponse du support.
5. Fonction $Q$ : définition des notes dans un environnement `def-` à l'intérieur d'un bloc `.notes`, coefficient laissé en blanc (« $[\cdot]$ ») tant que `av-definition-q-notes` est ouvert ; la forme usuelle est donnée en *Complément* et dans « À retenir » (marquée *à vérifier*).
6. Formules du support à coquille (p. 107, 112, 127, 128) : écrites corrigées dans le texte, la version du support étant citée dans le bloc *À vérifier* placé juste après (texte du bloc : « écrit ainsi dans ce chapitre »). Exception : p. 130, la formule du support reste affichée dans un segment orange `[…]{.a-verifier}` (comme au chapitre 3), parce que la suite du texte du support en dépend.
7. Coquilles de la correction du TD : solution écrite corrigée, avec renvoi au bloc.
8. Exercices du TD : numéros de l'**énoncé**, correspondance avec la correction indiquée ; notations du cours ($h$, $h_a$, $g$, $z_l$, $r_n$) sauf dans les blocs qui citent la correction ; filtre adapté causal de la correction noté $h_{a,c}$ (pour ne pas le confondre avec le canal $h_c$) ; $\gamma$ du TD (ex. 4 q. 2) noté $\rho$.
9. p. 119 : intertitre « À l'intérieur : » mal placé (devant les extrémités) non repris ; les deux cas sont écrits sans intertitre. *À revoir par Armand s'il préfère un bloc.*
10. p. 123, « quelque soit », « on peux » : corrigés (section 13) ; « = » de l'approximation de Gray conservé, précisé en *Complément* (même traitement que la condition manquante `av-symetrie-hypotheses` du chapitre 2).
11. Construction de Gray en miroir : tableau (`tbl-gray-miroir`) plutôt que figure.
12. Racine de cosinus surélevé citée en *Complément* (connaissance générale, signalée « non cité par le support »).
13. Section « À retenir » : mentions *(notes)*, *(TD)*, *(complément)*, *(à vérifier)*.
14. Équations labellisées : toutes citées dans le chapitre ou dans « À retenir ».

**Figures**

15. Chaîne : figure du chapitre 2 réutilisée, nouveau label `fig-chaine-bruit`.
16. Densités conditionnelles : $g_0 = 2$, $\sigma = 1{,}3$, $\gamma = 0{,}5$ (lecture approximative de la p. 103).
17. Seuil optimal : axe vertical normalisé par $\sigma^2/(2g_0)$.
18. $P_b$ (RSB) et $P_{b,\min}$ ($E_b/N_0$) : courbes recalculées à partir des formules ; même plage et mêmes repères (10 dB, $10^{-2}$) que le support.
19. 4-PAM : $g_0 = 1$, $\sigma = 0{,}6$ ; zones d'erreur colorées pour $a_1$ seulement.
20. Filtre adapté : $D = \Ts$ (valeur de l'énoncé du TD) ; $h^*(-t)$ en orange tireté (et non en gris : il figure dans les notes).
21. Échantillons bruités (TD ex. 5 q. 12) : 400 tirages simulés (graine 4), ordonnée aléatoire sans signification ; seuils en pointillés gris (ajout).

---

## 13. Corrections orthographiques sans bloc (`conventions.md` § 5.3)

| Source | Texte de la source | Corrigé en |
|---|---|---|
| poly, en-têtes | « Principes de communication en l'absence bruit » (plan p. 89…) | « … en l'absence de bruit » (déjà au ch. 2) |
| poly, p. 97 | « indentiquement distribués » (deux fois) | « identiquement » |
| poly, p. 103-106 | $\hat{B}_k$, $B_k$ mêlés à $\hat{B}_n$, $B_n$ | indices harmonisés en $n$ |
| poly, p. 120, 123 | « quelque soit M » | « quel que soit $M$ » |
| poly, p. 123 | « on peux montrer » | « on peut montrer » |
| poly, p. 125 | « Ainsi, maximiser ⇒ minimiser $P_b$ » (objet manquant) | « maximiser $\frac{g_0}{\sigma}$ revient à minimiser $P_b$ » |
| poly, p. 127 | « Parceval » | « Parseval » |
| poly, p. 128 | « Cauchy-Schwartz » | « Cauchy-Schwarz » |
| poly, p. 129 | « $\int_{\mathbb{R}} \lvert h\rvert^2(t)\,\mathrm{d}t$ » | « $\int \lvert h(t)\rvert^2\,\mathrm{d}t$ » |
| poly, p. 132 | « ne pourra être mise en œuvre » | « mis en œuvre » |
| poly, p. 135 | « $\lvert H(f)\rvert.^2$ » ; « cyclo-stationnaire » ; « $nT_S$ » | « $\lvert H(f)\rvert^2$ » ; « cyclostationnaire » ; « $n\Ts$ » |
| td-correction, p. 10-13 | « impusionnelles », « adaptré », « su fait », « LEs hypothèses » | non repris tels quels (texte reformulé) |

---

## 14. Questions bloquantes pour Armand

> Une question par bloc ouvert ; la proposition est déjà écrite dans le bloc.

1. **`av-pb-notes-probabilites-a-priori` (notes f. 3 r°)** : le prof avait-il écrit les poids $P(B_k = 1)$, $P(B_k = 0)$ (ou $\frac12$) ? Que vaut la marque sur le $B_k$ de la condition ?
2. **`av-definition-q-notes` (notes f. 4 r°)** : numérateur de $Q(x)$ : « 1 » ou « $x$ » ? (proposition : 1.)
3. **`av-variables-muettes` (poly p. 107, 128)** : corrections $z \to \gamma$ et $\mathrm{d}t \to \mathrm{d}u$ retenues ?
4. **`av-facteur-calcul-pb` (poly p. 112)** : facteur 0,5 ajouté à la deuxième ligne ?
5. **`av-quiz-seuil-ook` (poly p. 110)** : réponse $g_0/2$ (0,5 seulement si $g_0 = 1$) ? Le prof avait-il pris $g_0 = 1$ ?
6. **`av-quiz-pire-probabilite` (poly p. 111)** : réponse 0,5 au lieu de 0 ? Qu'a dit le prof en cours ?
7. **`av-variance-bruit-filtre` (poly p. 127)** : $Z_l \to Z'_l$ retenu ?
8. **`av-filtre-adapte-causal` (poly p. 130)** : $h_a(t) = h^*(T_h - t)$ (notes, TD, correction) au lieu de $h(t - T_h)$ ?
9. **`av-densite-conditionnelle-td` (td-correction p. 12)** : signe $(r - v(0))^2$ retenu ?
10. **`av-dsp-bruit-filtre-td` (td-correction p. 13)** : $\Gamma_{n'_l} = \lvert G_a\rvert^2\Gamma_{n_l}$ retenu ?
11. **`av-variance-bruit-discret-td` (td, ex. 4 q. 3)** : interprétation « bruit limité à $[-f_e/2, f_e/2]$, $T_e = 1$ » retenue ? Le TD a-t-il été corrigé en séance ?

---

## 15. Vérifications faites (étape 6 non encore lancée)

- Formules des chapitres 1 et 4 compilées sans erreur par MathJax 3.2.2, avec les macros de `_macros.qmd` (776 formules extraites, macro inconnue comptée comme erreur).
- Labels uniques dans la matière (chapitres 1 à 4) ; toutes les références `@…` résolues dans le fichier ; liens vers les chapitres 2 et 3 résolus ; identifiants `av-…` cités existants ; aucun identifiant retiré réutilisé ; divs équilibrés (imbrications à quatre deux-points vérifiées).
- Recalculs : $\gamma^*$ ; $P_s$ 4-PAM et M-PAM ; $\sigma_a^2 = (M^2-1)/3$ ; $P_{b,\min}$ pour M = 2 à 16 (courbes du support) ; $Q(4) \approx 3{,}17\cdot10^{-5}$, $P_s = 4{,}75\cdot10^{-5}$ (TD ex. 5) ; $Q(1) \approx 0{,}159$, $Q(\sqrt{10}) \approx 7{,}8\cdot10^{-4}$, $Q(\sqrt{20}) \approx 3{,}9\cdot10^{-6}$ ; triangle $v(t)$ du TD.
- **Non vérifié** : rendu Quarto (Quarto n'est pas disponible dans l'environnement de Claude) → à contrôler avec `quarto preview`, en particulier la définition imbriquée dans un bloc `.notes` (`def-fonction-q`), le tableau `tbl-gray-miroir` dans un bloc `.notes` et le segment orange de la p. 130.

---

## 16. Décisions (étape 3, 7 octobre 2026)

Armand laisse le choix à Claude (« corrige avec ce que tu trouves le plus logique ») : les 11 propositions de la section 14 sont retenues. Toutes corrigent une source : les 11 blocs deviennent **tranchés** (`.tranche`, **Décision** « …, Armand a laissé le choix à Claude, 2026-10-07 »), conformément à `conventions.md` § 5.2.

| Q | Bloc | Décision | Application |
|---|---|---|---|
| 1 | `av-pb-notes-probabilites-a-priori` | poids a priori rétablis, marque sur $B_k$ parasite | bloc tranché |
| 2 | `av-definition-q-notes` | lecture « 1 » | coefficient $\frac{1}{\sqrt{2\pi}}$ écrit dans `def-fonction-q` ; « À retenir » mis à jour |
| 3 | `av-variables-muettes` | $z \to \gamma$, $\mathrm{d}t \to \mathrm{d}u$ | bloc tranché (texte déjà corrigé) |
| 4 | `av-facteur-calcul-pb` | facteur 0,5 rétabli | bloc tranché |
| 5 | `av-quiz-seuil-ook` | réponse $g_0/2$ (0,5 pour $g_0 = 1$) | « Réponse retenue » ajoutée à la solution |
| 6 | `av-quiz-pire-probabilite` | réponse 0,5 | « Réponse retenue » ajoutée à la solution |
| 7 | `av-variance-bruit-filtre` | $Z'_l$ | bloc tranché |
| 8 | `av-filtre-adapte-causal` | $h_a(t) = h^*(T_h - t)$ | segment orange remplacé par la formule corrigée, mention « formule corrigée » ; « À retenir » et fiche matière mis à jour |
| 9 | `av-densite-conditionnelle-td` | signe $(r - v(0))^2$ | bloc tranché |
| 10 | `av-dsp-bruit-filtre-td` | $\Gamma_{n'_l} = \lvert G_a\rvert^2\Gamma_{n_l}$ | bloc tranché |
| 11 | `av-variance-bruit-discret-td` | bande limitée, $\sigma^2 = N_0/(2T_e)$ | bloc tranché |

Bilan : **0 bloc ouvert, 11 tranchés**. Contrôles après modification : 801 formules (ch. 1 et 4) compilées sans erreur par MathJax 3.2.2 ; divs équilibrés. Les choix par défaut de la section 12 restent à revoir à la validation.

---

## 17. Vérification (étape 6, 7 octobre 2026)

Conversation « Bristol — TS227 Chapitres 1 et 4 — Vérification et flashcards ».

**Exhaustivité.**

- **Poly p. 89-138** relu page à page (texte extrait du PDF) : définitions de $P_s$ et $P_b$, hypothèses, 5 quiz, calcul du seuil optimal, cas particuliers, calcul de $P_b$, RSB, cas M-aire (4-PAM, généralisation, $P_b$/$P_s$, Gray), récepteur optimal (p. 125-130), demi-Nyquist (p. 132), $E_b/N_0$ (p. 134-138) : tout est repris. Seul manque relevé : l'égalité $P(\text{erreur} \mid A_n = a_i) = P(\hat{A}_n \neq A_n \mid A_n = a_i)$ des p. 117-118, ajoutée.
- **Notes f. 2 v° à f. 4 v°** relues sur les photos : tout le contenu du chapitre 4 est repris (14 blocs `.notes`). L'exercice du bas du f. 2 v° ($Z_n \sim \mathcal{N}(0, \sigma^2)$, $R_n = g_0 + Z_n$) est déjà au chapitre 3 (`exr-loi-gaussienne`) ; le haut du f. 3 r° (critère de Nyquist, efficacité spectrale) relève du chapitre 2 ; le bas du f. 4 v° ($s_l(t)$ aléatoire), du chapitre 3.
- **TD** (énoncé p. 3-4) et **correction** (p. 9-14) relus : ex. 3, ex. 4 et ex. 5 q. 12-13 complets ; correspondance des questions exacte ; $h_c = \delta$ vient de la correction (« $h_l(t) = \delta(t)$ »).

**Formules.** 803 formules (ch. 1 et 4) compilées sans erreur (MathJax 3.2.2, macros de `_macros.qmd`). Recalculés : $\gamma^*$ (support et notes), $P_s$ 4-PAM et M-PAM, $\sigma_a^2 = (M^2 - 1)/3$, $P_{b,\min}$ ; $Q(1) \approx 0{,}159$, $Q(\sqrt{10}) \approx 7{,}8 \cdot 10^{-4}$, $Q(\sqrt{20}) \approx 3{,}9 \cdot 10^{-6}$, $P_{b,\min}(M = 4, 10\ \mathrm{dB}) \approx 1{,}8 \cdot 10^{-3}$, $Q(4)$ ; triangle $v(t)$ ; solutions TD ex. 4 q. 2, 5-7. Aucune erreur.

**Catégories.** Texte du support sans marquage ; 14 blocs `.notes`, chacun cité par feuillet ; compléments C1-C23 ; 11 blocs tranchés complets (Source, Problème, Proposition, Décision). Une citation des notes ($g(t) = \int G(f) e^{j2\pi ft}\, \mathrm{d}f$, f. 4 v°) était dans un bloc *Complément* : déplacée dans un bloc `.notes`.

**Références.** Toutes les références `@…` résolues ; liens vers les chapitres 2 et 3 résolus ; identifiants `av-…` cités existants ; labels uniques ; divs équilibrés ; toutes les équations labellisées sont citées.

**Figures.** Les 7 SVG du chapitre (et la chaîne du ch. 2) relus en image : courbes conformes aux formules et au support (p. 103, 108, 113, 116-119, 138), légendes avec origine. Remarque sans correction : l'abscisse de `04-constellation-bruitee` est notée $r_l[n]$ (notation du TD), la légende dit $r_n$.

**Corrections de forme appliquées** (`conventions.md` § 14) :

1. 11 blocs tranchés : ligne **Décision** séparée de **Proposition** par une ligne vide.
2. Citation des notes sortie du complément de $g_0$ (nouveau bloc `.notes`).
3. TD ex. 3 q. 4 (complément) : « $g(-D) = 0$ » → « $A_0$ y contribue par $g(0) = 0$ » (c'est $g(0)$ qui intervient).
4. Égalité des p. 117-118 ajoutée (exemple 4-PAM).
5. Section 0 de ce rapport mise à jour.

**Points bloquants : aucun.** Statut : `verifie`.

---

## 18. Validation et flashcards (étapes 7 et 8, 7 octobre 2026)

- **Validation** : chapitre validé par Armand (« validé »), y compris les choix par défaut de la section 12. Statut `valide`.
- **Flashcards** : `flashcards/04-transmission-presence-bruit.yml`, **57 cartes**, générées à partir du cours validé (`conventions.md` § 10) ; `ids-retires: []`. Toutes les `ref` pointent vers un label du chapitre.
- Répartition (ch. 4) : 16 formules, 8 exercices, 6 définitions, 5 pièges, 5 propriétés, 5 raisonnements, 5 relations, 5 résultats, 1 condition, 1 méthode ; 9 cartes issues des notes.
- `python scripts/flashcards.py` lancé : `revision/cartes/ts227.json` = **186 cartes** (ch. 1 : 12, ch. 2 : 61, ch. 3 : 56, ch. 4 : 57), 69 nouvelles clés, 0 clé disparue. Formules des cartes des ch. 1 et 4 (313) compilées sans erreur avec MathJax 3.2.2, après développement des macros.
- Statut final : `flashcards`.
