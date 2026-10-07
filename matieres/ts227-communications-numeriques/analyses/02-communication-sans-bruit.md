# TS227 — Chapitre 2 — Rapport d'analyse des sources

> Étape 2 du workflow (`CONTEXTE_PROJET.md`, section 11). **Aucun contenu de cours n'est rédigé ici.**
> Chapitre : *Principes de communication en l'absence de bruit*.
> Date : 7 octobre 2026. Statut du chapitre : `analyse`.
> **Mis à jour le 7 octobre 2026 après l'étape 3 (identification des différences)** : toutes les questions sont tranchées, voir la [section 13](#13-décisions-de-létape-3). En cas d'écart entre les sections 0 à 12 (rapport initial) et la section 13, la section 13 fait foi.

---

## 0. Résumé

- Le support couvre le chapitre 2 aux **pages 15 à 60** du PDF (diapositives 15 à 50/161). Après suppression des pages de plan, des diapositives dupliquées (animations) et des écrans « Sortez vos téléphones », il reste environ **25 pages utiles**.
- Les notes fournies forment **5 feuillets recto-verso (10 photos)**, non datés. Seule la **première moitié** concerne le chapitre 2 (f. 1 r° à f. 2 v° haut, puis f. 3 r° haut). Le reste relève des chapitres 3 et 4 du poly ; c'est inventorié en section 10 pour les analyses suivantes.
- Les notes apportent au chapitre 2 **trois démonstrations absentes du support** (critère de Nyquist temporel, passage à la version fréquentielle, bande minimale $B \ge 1/(2\Ts)$), **un exemple** (code Manchester), la notion d'**efficacité spectrale** et plusieurs remarques de l'enseignant.
- **7 points *À vérifier*** ont été repérés, dont 2 qui touchent des formules du cours (centre de symétrie du critère fréquentiel, signe de la TF) et 1 qui touche la réponse d'un quiz.
- **16 questions** pour Armand (section 12). Les plus bloquantes pour la rédaction : Q1 (dates des séances), Q2 (exemples 1 et 2 manquants), Q3 (schéma OOK), Q6 (périmètre du chapitre). **Toutes tranchées le 7 octobre 2026 (section 13)** ; un 8e point *À vérifier* (AV8, exemples 1 et 2 manquants) en est issu.

Conventions de citation dans ce rapport : `[poly, p. N]` = page **du PDF** (même numérotation que celle déjà utilisée dans `CONTEXTE_PROJET.md`, ex. « p. 78 »), suivie si utile du numéro de diapositive imprimé (« d. 36/161 »). `[f. 1 r°]` = feuillet 1 recto des notes. Voir Q8.

---

## 1. Inventaire des sources

| id proposé | Fichier | Nature | Pages utilisées | Remarque |
|---|---|---|---|---|
| `poly` | `sources/ts227/support/poly_ts227.pdf` | officielle | 15-60 | version du 9 octobre 2025, 180 p. (Beamer) |
| `notes` | `sources/ts227/notes/date-inconnue.pdf` (10 pages) et `sources/ts227/notes/date-inconnue/feuillet-N-recto.jpg`, `feuillet-N-verso.jpg` (N = 1 à 5) | personnelle | f. 1 r° → f. 3 r° (haut) | **date inconnue** (décision 13.1) ; page *k* du PDF = ordre f. 1 r°, f. 1 v°, f. 2 r°… |
| `td` | `sources/ts227/support/TD_TS_227.pdf` | officielle | ex. 1 ; ex. 3 ; ex. 5, q. 1-4 | ajouté à l'inventaire à l'étape 3 (section 13.6) ; phase 2, non intégré au cours |
| `td-correction` | `sources/ts227/support/correction_TD_TS_227.pdf` | officielle | p. 1-3 (ex. 1), p. 10-11 (ex. 3) | idem |

Ordre des feuillets reconstitué : numéro écrit en haut à gauche des rectos (1 à 5), et continuité du contenu recto → verso. Chaque recto commence par la mention marginale « Com numérique », ce qui suggère un début de séance (à confirmer, Q1).

Lien noté en marge de f. 1 r° : « rtajan.github.io » (site de l'enseignant, Q16).

---

## 2. Plan du support pour le chapitre 2

| Partie du poly | Pages PDF | Pages utiles | Pages écartées |
|---|---|---|---|
| Définitions (bande de base / transposée) | 16-17 | 17 | 16 (plan) |
| Principes en bande de base (schéma de la chaîne) | 18-19 | 19 | 18 (plan) |
| Définition mathématique des signaux | 20-34 | 21, 22, 23, 25 (quiz), 28, 29, 30, 31, 32, 34 (quiz) | 20 (plan), 24 et 33 (« Sortez vos téléphones »), 26 (sondage d'auto-évaluation), 27 (version incomplète de 28) |
| Interférence entre symboles, critère de Nyquist | 35-52 | 38, 39, 40, 41, 43, 45, 47-51 (quiz), 52 | 35 (plan), 36-37 (versions incomplètes de 38), 42 (doublon de 41), 44 (version incomplète de 45), 46 (« Sortez vos téléphones ») |
| Diagramme de l'œil | 53-60 | 56, 60 | 53 (plan), 54-55 (versions incomplètes de 56), 57-59 (versions incomplètes de 60) |

Remarques sur le support :

- p. 19 et p. 29-30 répètent le même schéma de chaîne ; seules les légendes ajoutées diffèrent (une figure suffit).
- p. 29 introduit déjà le bruit $z_l(t)$ (« processus aléatoire Gaussien blanc et réel »), puis p. 36 le supprime par hypothèse. Le modèle complet est donc posé dans ce chapitre, et utilisé au chapitre 4.
- Le support ne contient **aucune démonstration** dans ce chapitre : les deux versions du critère de Nyquist sont énoncées sans preuve (p. 39-40).

---

## 3. Correspondance support ↔ notes

| Notes | Contenu des notes | Support |
|---|---|---|
| f. 1 r°, haut | $s_b(t) = \sum_k b_k\,\delta(t - k\Tb)$, croquis du peigne, $D_b = 1/\Tb$ | p. 21 |
| f. 1 r°, milieu | Constellation 4 niveaux, étiquettes, « Mapping de Grey », « Voie en phase », « pulse amplitude modulation PAM » ; croquis de $s_a(t)$ avec $\Ts = 2\Tb$ | p. 22-23 |
| f. 1 r°, milieu | $M = 16 = 2^4$ ; $\Ts = n_b \Tb$ ; $D_s = 1/\Ts = D_b/n_b$ ; $D_b = \log_2 M \cdot D_s$, « $D_b$ vendu par le fournisseur », « $D_s$ ↔ bande passante » | p. 23 (formule seulement) |
| f. 1 r°, bas | « Après blocage du signal échantillonné » : $s_e(t) = \sum_m a_m h(t - m\Ts)$, développé | p. 27-28 ($s_l(t)$) |
| f. 1 r°, bas | Schéma : constellations $\{-\sqrt{1/2},\ \sqrt{1/2}\}$ et $\{0, 1\}$, « P = 0,5 W », « (OOK) On Off Keying » | **aucune** |
| f. 1 v°, haut | « Exemple 3 : Code Manchester », $\Pi_{\Ts/2}(t)$, $h(t)$ biphase, « signal à moyenne nulle et ne fait pas de séquence constante » | **aucune** |
| f. 1 v°, milieu | Filtre de réception, échantillonnage $t = n\Ts$, modèle $r_n = a_n g_0 + \sum_{m \ne n} a_m g_{n-m} + z'_n$, « symbole d'intérêt », « interférences entre symboles », « Détection : mise en place de seuil de décision » | p. 30, 31, 32, 38 |
| f. 1 v°, bas | Démonstration : $g_m = 0\ \forall m \in \mathbb{Z}^*$ ⇔ $g(t)\,Ш_{\Ts}(t) = g_0\,\delta(t)$ ; croquis de $g(t)$ s'annulant aux $m\Ts$ ; critère de Nyquist encadré | p. 39 (énoncé seul) |
| f. 2 r°, haut | « Rappel IES » ; démonstration de la version fréquentielle par TF ; dessin des répliques $G(f \pm 1/\Ts)$ ; règle du centre de symétrie $\left(\frac{1}{2\Ts}, \frac{g_0}{2}\right)$ | p. 40-41 (énoncés seuls) |
| f. 2 r°, milieu | « Exemple » : croquis d'un $g(t)$ oscillant ; « Critère temporel » | p. 43-45 (titre de sous-figure « Critère temporel ») |
| f. 2 r°, bas | $B \ge 1/\Ts - B$ ⇒ $B \ge 1/(2\Ts)$, avec dessin de spectres rectangulaires | **aucune** (le poly nomme seulement la fréquence de Nyquist $1/(2\Ts)$, p. 41) |
| f. 2 v°, haut | Diagramme de l'œil : croquis + 3 points | p. 56-60 |
| f. 3 r°, haut | Reprise : chevauchement des répliques nécessaire « pour avoir une constante », $1/\Ts - B \le B$ ⇒ $B \ge 1/(2\Ts)$ ; efficacité spectrale $\eta = D_b/B$ (bits·s⁻¹·Hz⁻¹), $D_b = n_b D_s$ ; « Critère de Nyquist (sans bruit) : si $h \star h_a$ vérifie le critère alors $r_n = g_0 a_n$ » | p. 52 (conclusion) ; $\eta$ seulement p. 177 et 179 (chapitre 6, conclusion) |

---

## 4. Contenu présent uniquement dans les notes

À reprendre en blocs `.notes`. Classé par importance pour le chapitre.

1. **Démonstration du critère de Nyquist temporel** [f. 1 v°] : $g(t)\,Ш_{\Ts}(t) = \sum_m g(m\Ts)\,\delta(t - m\Ts)$, donc l'absence d'IES ($g(m\Ts) = 0$ pour $m \ne 0$) équivaut à $g(t)\,Ш_{\Ts}(t) = g_0\,\delta(t)$.
2. **Démonstration de la version fréquentielle** [f. 2 r°] : TF des deux membres, $\TF[Ш_{\Ts}] = \frac{1}{\Ts} Ш_{1/\Ts}$, d'où $\frac{1}{\Ts}\sum_m G(f - m/\Ts) = g_0$. Avec le dessin des répliques qui se chevauchent.
3. **Bande minimale** [f. 2 r° et f. 3 r°] : les répliques doivent se chevaucher pour que leur somme soit constante, d'où $1/\Ts - B \le B$, soit $B \ge \frac{1}{2\Ts}$. Résultat encadré dans les notes. Absent du poly sous cette forme.
4. **Efficacité spectrale** $\eta = D_b/B$ en bits·s⁻¹·Hz⁻¹ [f. 3 r°]. Dans le poly, elle n'apparaît qu'au chapitre 6 (p. 177, 179). Voir Q6.
5. **Exemple 3 : code Manchester** [f. 1 v°] : $h(t)$ vaut une constante positive sur $[0, \Ts/2]$ et l'opposée sur $[\Ts/2, \Ts]$ ; propriétés : moyenne nulle, pas de longue séquence constante. Les exemples 1 et 2 **ne figurent pas** dans les photos (Q2).
6. **Bloqueur et signal $s_e(t)$** [f. 1 r°] : interprétation de la mise en forme comme un « blocage » (bloqueur) du signal échantillonné (Q4).
7. **Comparaison OOK / antipodal à puissance égale** [f. 1 r°] : interprétation à confirmer (Q3).
8. **Remarques de l'enseignant** [f. 1 r°] : $D_b$ est la grandeur « vendue par le fournisseur » ; $D_s$ est liée à la bande passante. Exemple $M = 16 = 2^4$.
9. **Vocabulaire** : « Mapping de Gray » pour l'étiquetage de la p. 22 (le poly ne nomme l'étiquetage de Gray qu'au chapitre 4, p. 123) ; « PAM » (*pulse amplitude modulation*) pour la constellation réelle à $M$ niveaux (le poly emploie « 4-PAM » à partir de la p. 116).
10. **Lecture du diagramme de l'œil** [f. 2 v°] : « les courbes se croisent en 2 points uniques ⇒ absence d'IES », plus précis que le poly (« Absence d'IES », p. 60).
11. **Récapitulatif** [f. 3 r°] : si $h \star h_a$ vérifie le critère, $r_n = g_0 a_n$ (sans bruit).

---

## 5. Informations redondantes

- Notes et support identiques (on garde le support, sans bloc `.notes`) : définitions de $s_b$, $D_b$, $s_a$, $D_s$, $D_b = n_b D_s$ ; modèle $r_n$ ; énoncés des deux critères ; les trois points du diagramme de l'œil ; définition de l'IES.
- Les notes écrivent l'IES sous la forme $\sum_{m \ne n} a_m g_{n-m}$, le poly sous la forme $\sum_{m \ne 0} a_{n-m} g_m$ : même somme après changement d'indice. On garde la forme du poly.
- $B \ge 1/(2\Ts)$ est démontré deux fois dans les notes (f. 2 r° et f. 3 r°) : une seule démonstration, avec la figure de f. 3 r° (plus claire : spectres qui se chevauchent).
- Support : voir les pages écartées en section 2.

---

## 6. Figures

| # | Figure | Source | Utilité | Méthode proposée |
|---|---|---|---|---|
| F1 | Chaîne de transmission en bande de base | poly p. 19 (= 29, 30) | essentielle | schéma-bloc reconstruit (TikZ → SVG) |
| F2 | Constellation 4-PAM avec étiquettes de Gray | poly p. 22 ; notes f. 1 r° | essentielle | reconstruite (TikZ ou matplotlib) |
| F3 | $s_a(t)$ et $s_l(t)$ (impulsions et porte) | poly p. 28 | utile | Python, à partir de la séquence lue sur la figure |
| F4 | Peigne $s_b(t)$ | notes f. 1 r° | faible (redondante avec F3) | à omettre ou fusionner avec F3 |
| F5 | Régions et seuils de décision | poly p. 32, 34 | essentielle (sert au quiz p. 34) | reconstruite |
| F6 | Constellations OOK et antipodale à même puissance | notes f. 1 r° | utile si Q3 confirmée | reconstruite |
| F7 | $h(t)$ du code Manchester | notes f. 1 v° | utile | Python |
| F8 | $g(t)$ s'annulant aux instants $m\Ts$ | notes f. 1 v° | utile (illustre le critère temporel) | Python, à fusionner avec F11 |
| F9 | Répliques $G(f - m/\Ts)$ qui se chevauchent | notes f. 2 r°, f. 3 r° | essentielle (démonstration) | Python |
| F10 | Symétrie de $G(f)$ autour de $(1/(2\Ts), \cdot)$ | poly p. 41 | essentielle | Python ; **légende de l'axe à corriger selon AV2** |
| F11 | Exemple de filtre de Nyquist, temps et fréquence, avec répliques | poly p. 43-45 ; notes f. 2 r° | essentielle | Python ; d'après la figure, cosinus surélevé de facteur de retombée ≈ 0,2 avec $\Ts = 1$ ms (lecture, voir C4) |
| F12 | Bande minimale (spectres rectangulaires) | notes f. 2 r° | utile | Python |
| F13 | Filtres des exercices (portes, triangles) | poly p. 47-51 | nécessaire aux exercices | Python |
| F14 | Construction et lecture du diagramme de l'œil | poly p. 56, 60 ; notes f. 2 v° | essentielle | Python (simulation) ; paramètres du poly inconnus (voir C6) |

---

## 7. Incohérences, contradictions et coquilles

> État après l'étape 3 : voir le tableau de la section 13.3 (décision pour chaque point).

Identifiants `av-…` proposés pour les blocs *À vérifier* de la rédaction.

**AV1 — Signe de la TF** (`av-signe-tf-nyquist`)
- Source [poly, p. 40] : « $G(f) = \int_{-\infty}^{+\infty} g(t)\,e^{j2\pi ft}\,\mathrm{d}t$ ».
- Problème : le poly utilise $e^{-j2\pi f\tau}$ pour les TF des p. 85, 86 et 87 ; les notes aussi ($\Gamma_x(f) = \int R_x(\tau)\,e^{-j2\pi f\tau}\,\mathrm{d}\tau$ et $R_x(\tau) = \int \Gamma_x(f)\,e^{+j2\pi f\tau}\,\mathrm{d}f$, f. 5 r°). La p. 40 est donc isolée.
- Proposition : convention $e^{-j2\pi ft}$ pour la TF directe, à fixer dans la fiche matière. Le résultat du critère n'en dépend pas. Ce point était listé comme « convention à clarifier » dans `CONTEXTE_PROJET.md` (18.4) : les autres pages permettent maintenant de trancher (Q9).

**AV2 — Ordonnée du centre de symétrie** (`av-centre-symetrie-nyquist`)
- Source [poly, p. 41-42] : « Le point $\left(\frac{1}{2\Ts}, \frac{g_0}{2}\right)$ est un centre de symétrie pour $G(f)$ ». Repris tel quel dans les notes [f. 2 r°]. Sur la figure, la graduation « $g(0)/2$ » est placée à la moitié de $G(0) = 10$.
- Problème : avec le critère $\frac{1}{\Ts}\sum_m G(f - m/\Ts) = g_0$ (p. 40), on obtient pour $f \in [0, 1/\Ts]$ : $G(f) + G(f - 1/\Ts) = g_0 \Ts$. L'ordonnée du centre est donc $\frac{g_0 \Ts}{2}$ (égale à $G(0)/2$), pas $\frac{g_0}{2}$. Contrôle par les dimensions ($G$ est en [g]·s, $g_0$ en [g]) et par l'exercice de la p. 49 : triangle de hauteur 10 sur $[-1000, 1000]$ Hz, $\Ts = 1$ ms, donc $g_0 = \int G = 10^4$ ; le centre de symétrie est en $(500\ \text{Hz}, 5) = (1/(2\Ts), g_0\Ts/2)$, alors que $g_0/2 = 5000$.
- Proposition : $\left(\frac{1}{2\Ts}, \frac{g_0 \Ts}{2}\right)$, ou de manière équivalente $\left(\frac{1}{2\Ts}, \frac{G(0)}{2}\right)$ quand $G(\pm 1/\Ts) = 0$. Sauf si l'enseignant a utilisé une autre normalisation en cours (Q10).

**AV3 — Hypothèses implicites de la règle de symétrie** (`av-symetrie-hypotheses`)
- Source [poly, p. 41] : seule hypothèse donnée, « $G(f)$ à support borné $[-1/\Ts, 1/\Ts]$ ».
- Problème : passer de $G(f) + G(f - 1/\Ts) = g_0\Ts$ à une symétrie centrale suppose $G$ **réelle et paire**, c'est-à-dire $g$ réel et pair. C'est le cas de tous les exemples du poly, mais ce n'est pas dit.
- Proposition : ajouter l'hypothèse en *Complément*. Ce n'est pas une erreur, seulement une condition manquante ; à classer en *Complément* plutôt qu'en *À vérifier* si Armand est d'accord (Q11).

**AV4 — Quiz p. 51 : unité du débit ou réponse** (`av-quiz-debit-porte`)
- Source [poly, p. 51] : $h(t)$ = porte de hauteur 10 sur $[0, 1[$ ms, $h_a(t) = h(t)$ ; « le débit maximal d'une communication sans IES est de $D_s = 1$ Msymboles/s ? » ; réponse marquée : A (Oui).
- Problème : $g = h \star h$ est un triangle de support $[0, 2]$ ms, de sommet en $t = 1$ ms. En échantillonnant au sommet, il s'annule à ±1 ms : le débit maximal est $1/\Ts = 1$ **k**symbole/s. Avec « Msymboles/s », la bonne réponse serait B. Le quiz voisin (p. 50, triangle identique) dit bien « 1 ksymboles/s ».
- Proposition : coquille d'unité (« ksymboles/s »), réponse A. À confirmer avec ce qui a été dit en cours (Q12).
- Remarque liée : $g(t)$ est ici centré en 1 ms et non en 0 ; il faut échantillonner aux instants $1\ \text{ms} + n\Ts$. Le modèle du poly ($g_0 = g(0)$, p. 31) ne prévoit pas ce retard (à expliquer en *Complément*, C3).

**AV5 — Quiz p. 34 : deux propositions identiques** (`av-quiz-seuils`)
- Source [poly, p. 34] : propositions A et C toutes deux « $\hat{a} = [1, -3, -1]$ » ; réponse marquée D, $[1, -3, 3]$.
- Problème : doublon dans les propositions. La réponse D est correcte (seuils $-2{,}5$, $0{,}5$, $1{,}5$ : $1{,}2 \to 1$, $-4 \to -3$, $2{,}1 \to 3$).
- Proposition : présenter l'exercice sans les propositions de QCM (énoncé, puis solution). Pas d'impact sur le cours.

**AV6 — Titre du chapitre** (`av-titre-chapitre`, ou correction typographique, Q13)
- Source [poly, p. 15 à 60, en-têtes] : « Principes de communication en l'absence bruit ».
- Proposition : « … en l'absence **de** bruit » (forme utilisée dans `CONTEXTE_PROJET.md`).

**AV7 — Fautes d'orthographe sans effet sur le sens** (Q13) : « variables aléatoires discrètes indépendante » (p. 21), « Symbole d'Intéret » (p. 37-39), « et ceux, même en l'absence » pour « et ce » (p. 52), « Mapping de Grey » pour Gray (notes, f. 1 r°).

Vérifications faites sans problème : réponses des quiz p. 25 (A, 0,5 Msymbole/s), p. 47 (A), p. 48 (B : $g(0{,}5\ \text{ms}) = 5 \ne 0$), p. 49 (A : les répliques du triangle somment à une constante), p. 50 (A) ; exemple de la p. 23 ; étiquetage de la p. 22 (étiquettes voisines différant d'un seul bit).

Aucune **contradiction de fond** entre notes et support pour ce chapitre : les notes complètent, elles ne contredisent pas (sauf qu'elles reprennent AV2 telle quelle).

---

## 8. Passages illisibles ou ambigus dans les notes

| Où | Ce qui est écrit (lecture) | Doute |
|---|---|---|
| f. 1 r°, milieu | croquis de $s_a(t)$ : impulsion d'amplitude 3, flèches hachurées, « $\Ts = 2\Tb$ » écrit en surcharge | dessin raturé ; sens probable : 4-PAM, $n_b = 2$, donc $\Ts = 2\Tb$ (Q5) |
| f. 1 r°, milieu | « $D_s = \frac{1}{\Ts} = $ [mot barré] $\frac{1}{n_b \Tb}$ » | le mot barré est illisible, sans conséquence |
| f. 1 r°, bas | schéma OOK : croix en $-1$ et $1$ (noir), $\pm\sqrt{1/2}$ et « $\sqrt{2}$ » (vert), « [0] », « [1] », « P = 0,5 W » | quelles constellations sont comparées, et pourquoi des croix en $\pm 1$ (Q3) |
| f. 1 r°, bas | « $s_e(t)$ » | indice « e » ou « l » ? même signal que $s_l(t)$ ? (Q4) |
| f. 1 v°, milieu | terme encerclé « $a_n g_0$ » | se lit aussi « $a_m a_0$ » ; la lecture $a_n g_0$ est la seule cohérente avec la suite |
| f. 1 v°, haut | « $\Pi_{\Ts/2}(t)$ » bornes $\pm\Ts/4$ ; amplitude de $h(t)$ non notée | notation $\Pi_T$ = porte de largeur $T$ centrée (cohérent avec f. 5 v°, $h(t) = \Pi_{\Ts}(t - \Ts/2)$) ; amplitude à fixer (±1 par défaut, en *Complément*) |
| f. 2 r°, schéma | « $G(1 + \frac{1}{\Ts})$ » | lire $G(f + \frac{1}{\Ts})$ |
| f. 2 r°, milieu | « Critère temporel » sous le croquis de l'exemple | correspond au titre de sous-figure du poly p. 43, pas à une nouvelle notion |

---

## 9. Compléments envisagés (catégorie *Complément*, à approuver)

| # | Complément | Justification |
|---|---|---|
| C1 | Expression de $h(t)$ du code Manchester avec des portes, et remarque sur les deux conventions de signe (IEEE 802.3 / G.E. Thomas) | les notes n'ont que le dessin |
| C2 | Hypothèse « $G$ réelle et paire » de la règle de symétrie (AV3) | condition manquante |
| C3 | Retard d'échantillonnage quand $g(t)$ n'est pas centré en 0 (quiz p. 51) | sinon l'exercice contredit le modèle $g_0 = g(0)$ |
| C4 | Nommer le filtre des p. 43-45 : cosinus surélevé ; bande $B = (1 + \beta)/(2\Ts)$. Une valeur de $\beta$ ne peut être donnée que comme **« valeur estimée à partir de la figure »** (≈ 0,2 : plat jusqu'à ≈ 400 Hz, nul à partir de ≈ 600 Hz, $1/\Ts = 1000$ Hz), jamais comme une valeur du cours (décision 13.4) | le poly ne nomme pas le filtre ni $\beta$ ; lecture graphique |
| C5 | Conséquence de $B \ge 1/(2\Ts)$ sur l'efficacité spectrale, **avec ses conditions** (décision 13.4) : en bande de base, avec la bande minimale $B = 1/(2\Ts)$, $\eta \le 2\log_2 M$ bits·s⁻¹·Hz⁻¹ ; en bande transposée, la borne est $\log_2 M$ | relie deux résultats des notes ; $\eta$ reste dans ce chapitre (Q6) |
| C6 | Construction du diagramme de l'œil (superposition de tranches de durée $2\Ts$ synchronisées sur l'horloge symbole) et généralisation : $M$ points de croisement uniques pour $M$ niveaux | le poly ne montre que la figure |
| C7 | Valeur aux discontinuités : le quiz p. 47 dépend des points pleins/vides de la figure | sinon la réponse paraît arbitraire |

---

## 10. Notes hors chapitre 2 (pour les analyses suivantes)

| Notes | Contenu | Poly |
|---|---|---|
| f. 2 v°, milieu-bas | « III Transmission en présence de bruit », rappels de probabilités (densité, espérance, variance, loi gaussienne, « 67 % » à ±σ et « 99 % » à ±3σ), début d'exercice $R_n = g_0 + Z_n$ | p. 70-79 (chap. 3) et p. 89-97 (chap. 4) |
| f. 3 r°, bas | probabilité d'erreur symbole et binaire, $R_n = g_0 A_n + Z'_n$ | p. 90-101 |
| f. 3 v° | seuil optimal $\gamma = \frac{\sigma^2}{2g_0}\ln\frac{p_0}{1 - p_0}$, médiatrice si $p_0 = p_1$, décibels | p. 102-113 |
| f. 4 r° | $Q(x)$, $P_s$ de la 4-PAM et de la M-PAM, $P_b \ge P_s/\log_2 M$, construction miroir du code de Gray | p. 114-123 |
| f. 4 v° | filtre adapté $h_a(t) = \lambda h^*(-t)$, $G(f) = \lambda\lvert H(f)\rvert^2$, puis $s_l(t)$ comme signal aléatoire | p. 124-131 puis p. 81 |
| f. 5 r°-v° | processus aléatoires, stationnarité, DSP, bruit blanc, cyclostationnarité, exercice menant à la formule de Bennett | p. 80-88 (chap. 3) |

Constat : **l'ordre du cours diffère de celui du poly.** Après le diagramme de l'œil, l'enseignant a ouvert une partie « III Transmission en présence de bruit » (rappels de probabilités, puis chapitre 4 du poly jusqu'au filtre adapté), et n'a traité les processus aléatoires et la DSP (chapitre 3 du poly) qu'ensuite. Cela ne change rien au chapitre 2, mais pèse sur le découpage des chapitres 3 et 4 de Bristol (Q7). Déjà repéré : les notes reprennent les valeurs 67 % et 99 % du poly (approximation signalée p. 78 dans `CONTEXTE_PROJET.md`).

---

## 11. Plan proposé pour le chapitre Bristol (structure seulement)

Fichier proposé : `cours/02-communication-sans-bruit.qmd` (Q14).

1. Introduction et objectifs
2. Bande de base et bande transposée — p. 17
3. Chaîne de transmission en bande de base — p. 19, 29, 30 (F1)
4. Modélisation des signaux
   - bits, $s_b(t)$, débit binaire — p. 21 ; notes f. 1 r°
   - association bits → symboles, constellation, étiquetage de Gray, PAM — p. 22 ; notes f. 1 r° (F2, F6 si Q3)
   - symboles, $s_a(t)$, débit symbole, $D_b = n_b D_s$ — p. 23 ; notes f. 1 r°
   - filtre de mise en forme, $s_l(t)$ ; exemples de mises en forme dont Manchester — p. 28 ; notes f. 1 r°-v° (F3, F7)
   - canal, filtre de réception, filtre global $g(t)$ — p. 29-30
   - échantillonnage, modèle discret équivalent — p. 31 ; notes f. 1 v°
   - décision, seuils — p. 32 (F5) ; exercice p. 34
5. Interférence entre symboles — p. 38 ; notes f. 1 v°
6. Critère de Nyquist
   - version temporelle, avec démonstration — p. 39 ; notes f. 1 v°
   - version fréquentielle, avec démonstration — p. 40 ; notes f. 2 r° (F9) ; AV1
   - règle de symétrie, fréquence de Nyquist — p. 41 (F10) ; AV2, AV3
   - bande minimale $B \ge 1/(2\Ts)$ — notes f. 2 r°, f. 3 r° (F12)
   - efficacité spectrale (selon Q6) — notes f. 3 r°
   - exemple : cosinus surélevé — p. 43-45 (F11)
   - exercices — p. 47-51 (F13) ; AV4
7. Diagramme de l'œil — p. 56-60 ; notes f. 2 v° (F14)
8. À retenir

Exercices : les quiz p. 25, 34, 47-51 deviennent des exercices (`exr-`) avec solution ; la réponse marquée vient du support, la justification est un *Complément*.

---

## 12. Questions pour Armand

> Toutes tranchées le 7 octobre 2026 : réponses en section 13.

**Sources**

1. **Dates des séances.** Quelles dates pour les feuillets 1 à 3 (au moins) ? Chaque recto marqué « Com numérique » est-il un début de séance ? L'ordre recto/verso reconstitué (f. 1 r°, f. 1 v°, f. 2 r°…) est-il le bon ? Les photos sont rangées dans `sources/ts227/notes/a-dater/` en attendant d'être regroupées en un PDF par séance (`notes/AAAA-MM-JJ.pdf`).
2. **Exemples 1 et 2.** Les notes commencent à « Exemple 3 : Code Manchester ». Manque-t-il une page, ou les exemples 1 et 2 sont-ils ceux du bas de f. 1 r° (bloqueur, OOK) ? Si tu te souviens de ce qu'ils étaient (NRZ ? RZ ?), le dire ; sinon je signalerai le manque.
3. **Schéma OOK (f. 1 r°, bas).** Ma lecture : l'enseignant compare, à puissance moyenne égale (0,5 W), la constellation antipodale $\{-\sqrt{1/2}, \sqrt{1/2}\}$ (écart $\sqrt{2}$) et l'OOK $\{0, 1\}$ (écart 1), pour montrer que l'antipodale sépare mieux les symboles. Est-ce bien ça ? Que représentent les croix en $-1$ et $1$ ?
4. **$s_e(t)$ et « blocage ».** Est-ce le même signal que $s_l(t)$ du poly ? L'enseignant a-t-il présenté la porte comme un bloqueur d'ordre 0 ? (Je reprendrais $s_l(t)$ et signalerais la correspondance.)
5. **Croquis de $s_a(t)$ (f. 1 r°)** : confirmes-tu « exemple 4-PAM, $n_b = 2$, $\Ts = 2\Tb$ » ? Et $M = 16 = 2^4$ : simple exemple oral ?

**Périmètre et organisation**

6. **Périmètre du chapitre 2.** J'y mets la bande minimale $B \ge 1/(2\Ts)$ (notes) et l'efficacité spectrale $\eta = D_b/B$ (notes, alors que le poly la place au chapitre 6). D'accord, ou $\eta$ va au chapitre 6 avec un renvoi ?
7. **Découpage des chapitres 3 et 4.** Le cours a suivi un autre ordre que le poly (section 10). Pour Bristol : garder le plan du poly (numéros 3 = DSP, 4 = bruit) ou suivre l'ordre du cours ? Pas bloquant pour le chapitre 2, mais à décider avant l'analyse suivante.
8. **Numéros de page.** Je cite les pages du PDF (1 à 180), comme dans `CONTEXTE_PROJET.md`, et non les numéros imprimés sur les diapositives (« 36/161 »). On le fixe dans `conventions.md` ?

**Points *À vérifier***

9. **Signe de la TF (AV1).** On fixe $\TF[x](f) = \int x(t)\,e^{-j2\pi ft}\,\mathrm{d}t$ dans la fiche matière, et la p. 40 devient un bloc *À vérifier* ?
10. **Centre de symétrie (AV2).** L'enseignant a-t-il dit quelque chose sur l'ordonnée $g_0/2$ (normalisation $\Ts = 1$, autre définition de $g_0$) ? Sinon, bloc *À vérifier* avec la proposition $g_0\Ts/2$.
11. **Hypothèse $G$ réelle et paire (AV3)** : *Complément* (ma préférence) ou *À vérifier* ?
12. **Quiz p. 51 (AV4)** : la réponse donnée en cours était-elle « Oui » ? L'enseignant a-t-il parlé de ksymboles/s ?
13. **Fautes d'orthographe (AV6, AV7).** Proposition de convention : les fautes d'orthographe et de typographie **sans effet sur le sens** sont corrigées sans bloc *À vérifier*, mais listées dans le rapport d'analyse (comme ici). Les erreurs de fond restent en *À vérifier*. D'accord ?

**Fichiers**

14. **Noms de fichiers.** Slug du chapitre : `02-communication-sans-bruit` ? Et ce rapport : je l'ai placé dans `matieres/ts227-communications-numeriques/analyses/02-communication-sans-bruit.md` (non publié par Quarto, qui ne rend que les `.qmd`). C'est une nouvelle convention : on la garde ?
15. **TD.** Peux-tu copier `TD_TS_227.pdf` et `correction_TD_TS_227.pdf` dans `sources/ts227/support/` ? Le TD n'est pas à traiter en phase 1, mais ses notations doivent être vérifiées pour la table de correspondance.
16. **rtajan.github.io.** Ce site contient-il des ressources à inventorier (version plus récente du poly, codes des figures) ?

---

## 13. Décisions de l'étape 3

> Réponses d'Armand du 7 octobre 2026 (conversation « Bristol — TS227 Chapitre 2 — Différences »). Cette section fait foi pour la rédaction.

### 13.1 Sources

- **Dates des séances : inconnues.** Les notes sont citées sans date.
- **Rangement** (Q1) : ordre des feuillets confirmé (le contenu de chaque photo a été vérifié). Photos dans `sources/ts227/notes/date-inconnue/feuillet-N-recto.jpg` / `feuillet-N-verso.jpg`, et un PDF unique `sources/ts227/notes/date-inconnue.pdf` (10 pages, dans l'ordre f. 1 r°, f. 1 v°, …, f. 5 v°). Le dossier `a-dater/`, vide, a été supprimé par Armand.
- **Front matter** : une seule source de notes, `id: notes`, `seance: inconnue`, `pages: "f. 1 r° – f. 3 r°"`. Citation dans le texte : `[notes, f. 1 v°]`.
- **TD et correction** inventoriés (section 13.6).

### 13.2 Périmètre et organisation

| Question | Décision |
|---|---|
| Q6 — efficacité spectrale | Dans le **chapitre 2**, là où l'enseignant l'a présentée ; **renvoi depuis le chapitre 6** (à faire lors de sa rédaction, noté dans `TODO.md`) |
| Q7 — ordre des chapitres | **Ordre du poly conservé** (3 = DSP, 4 = bruit). La fiche matière indique que l'enseignant a traité le bruit avant la DSP |
| Q8 — numéros de page | **Pages du PDF** (1 à 180), pas les numéros imprimés sur les diapositives. Ajouté à `conventions.md` |
| Q14 — noms de fichiers | Slug `02-communication-sans-bruit` (`cours/`, `flashcards/`, `figures/02-…`). Rapports d'analyse : `matieres/<matiere>/analyses/NN-slug.md`, non rendus par Quarto. Ajouté à `conventions.md` |
| Q16 — rtajan.github.io | Noté dans la fiche matière comme « site de l'enseignant, non inventorié » ; tâche dans `TODO.md` |

### 13.3 Points *À vérifier*

Nouvelle convention (Q5 de l'étape 3, ajoutée à `conventions.md` § 5.2) : une correction du support décidée par Armand **reste visible** dans un bloc `::: {.a-verifier .tranche #av-…}` qui garde **Source**, **Problème**, **Proposition** et ajoute **Décision**. Seuls les blocs sans `.tranche` sont ouverts.

| Point | Décision | Présentation dans le cours |
|---|---|---|
| AV1 `av-signe-tf-nyquist` | Convention $\TF[x](f) = \int x(t)\,e^{-j2\pi ft}\,\mathrm{d}t$, fixée dans la fiche matière ; la formule de la p. 40 est une coquille | bloc **tranché** |
| AV2 `av-centre-symetrie-nyquist` | Centre de symétrie $\left(\frac{1}{2\Ts}, \frac{g_0\Ts}{2}\right)$ ; la p. 41 (et les notes, f. 2 r°) écrivent $g_0/2$ | bloc **tranché** ; figure F10 graduée en $g_0\Ts/2$ avec mention de la correction dans la légende |
| AV3 `av-symetrie-hypotheses` | Pas une erreur : condition manquante ($G$ réelle et paire) | bloc *Complément* (C2), **pas de bloc *À vérifier*** ; l'identifiant n'est pas utilisé |
| AV4 `av-quiz-debit-porte` | Coquille d'unité : « 1 ksymboles/s », réponse A conservée | bloc **tranché** + *Complément* C3 (retard d'échantillonnage) |
| AV5 `av-quiz-seuils` | Doublon des propositions A et C, sans impact | **aucun bloc** ; exercice présenté sans les choix du QCM, solution D ; mentionné ici seulement. Identifiant non utilisé |
| AV6 `av-titre-chapitre` | Faute d'orthographe sans effet sur le sens | corrigée **sans bloc** (convention 13.5) ; identifiant non utilisé |
| AV7 | Fautes d'orthographe sans effet sur le sens | corrigées **sans bloc**, liste en 13.5 |
| AV8 `av-exemples-mise-en-forme-manquants` (nouveau) | Les notes numérotent l'exemple Manchester « Exemple 3 » ; les exemples 1 et 2 ne figurent dans aucune source fournie | bloc **ouvert**, juste avant l'exemple Manchester ; aucune hypothèse sur leur contenu |

Bilan prévu dans le cours : **1 bloc ouvert** (AV8), **3 blocs tranchés** (AV1, AV2, AV4).

### 13.4 Contenu

| Point | Décision |
|---|---|
| Q3 — schéma OOK (f. 1 r°) | Lecture confirmée : comparaison, à puissance moyenne égale (0,5 W), de la constellation antipodale $\{-\sqrt{1/2}, \sqrt{1/2}\}$ (écart $\sqrt{2}$) et de l'OOK $\{0, 1\}$ (écart 1). Bloc `.notes` + figure F6. Le TD (ex. 2, q. 11) emploie aussi « 2-OOK (On Off Keying), $A_k \in \{0, 1\}$ » |
| Q2 — exemples 1 et 2 | Absents → AV8 |
| Q4 — $s_e(t)$, « blocage » | Notation du poly $s_l(t)$ ; correspondance « $s_e$ dans les notes » dans la table des notations ; mention du bloqueur en bloc `.notes`, sans interprétation |
| Q5 — croquis de $s_a(t)$, $M = 16$ | Exemple 4-PAM, $n_b = 2$, $\Ts = 2\Tb$ ; $M = 16 = 2^4$ présenté comme second exemple oral ($n_b = 4$, $\Ts = 4\Tb$) ; croquis raturé non reproduit |
| Q11 — compléments C1 à C7 | **Acceptés**, avec deux restrictions : **C4** — $\beta \approx 0{,}2$ seulement comme « valeur estimée à partir de la figure », jamais comme valeur du cours (ou pas de valeur) ; **C5** — conditions explicites : $\eta \le 2\log_2 M$ en bande de base avec la bande minimale $1/(2\Ts)$ ; en bande transposée, la borne est $\log_2 M$ |
| Q12 — quiz | Quiz p. 25, 34, 47-51 → exercices `exr-` avec solution ; réponse marquée = support officiel, justification = *Complément* |

### 13.5 Corrections orthographiques sans bloc (nouvelle convention, `conventions.md` § 5.3)

| Source | Texte de la source | Corrigé en |
|---|---|---|
| poly, en-têtes p. 15-60 | « Principes de communication en l'absence bruit » | « … en l'absence de bruit » |
| poly, p. 21 | « variables aléatoires discrètes indépendante » | « indépendantes » |
| poly, p. 37-39 | « Symbole d'Intéret » | « symbole d'intérêt » |
| poly, p. 52 | « et ceux, même en l'absence » | « et ce, même en l'absence » |
| notes, f. 1 r° | « Mapping de Grey » | « étiquetage (*mapping*) de Gray » |
| poly, p. 17 | « transmissions filaire » | « transmissions filaires » (ajouté à l'étape 4) |
| poly, p. 32 | « à égale distances entre les symboles » | « à égale distance des symboles » (ajouté à l'étape 4) |
| poly, p. 52 | « lors du choix de h(t) et ha(t)). » | parenthèse fermante en trop supprimée (ajouté à l'étape 4) |

### 13.6 Inventaire du TD et de sa correction

| id | Fichier | Description | Pages |
|---|---|---|---|
| `td` | `TD_TS_227.pdf` | « TD de communications numériques — Transmissions en bande de base », module TS227, 2020/2021, Guillaume Ferré et Romain Tajan ; PDF créé le 19 novembre 2020 | 4 |
| `td-correction` | `correction_TD_TS_227.pdf` | Correction partielle du même TD ; PDF créé le 6 janvier 2021 | 15 |

Répartition par chapitre (phase 2 : le TD n'est pas intégré au cours ; inventaire seulement) :

| Exercice du TD | Contenu | Chapitre | Correction |
|---|---|---|---|
| 1 — modulateur 8-PAM | $M$ et $n_b$, constellation avec étiquetage de Gray, bits → symboles, débit binaire, régions de décision, décision sur $r_l = [3{,}8;\ -1{,}1;\ -7{,}4]$ | **2** | p. 1-3 ; q. 5-6 sans corrigé |
| 2 — cyclostationnarité et DSP | $m_{s_l}(t)$, $R_{s_l}(t, \tau)$, formule de Bennett, DSP 2-PAM et 2-OOK | 3 | p. 4-9 ; DSP de l'OOK sans corrigé (q. 6 de la correction, q. 11 de l'énoncé) |
| 3 — critère de Nyquist et filtrage adapté | filtre adapté à une porte, causalité, $v(t)$ filtre de Nyquist, retard du premier symbole | **2** (critère) et 4 (filtre adapté) | p. 10-11 ; q. 3-5 de la correction sans corrigé |
| 4 — probabilité d'erreur et récepteur optimal | $P_b$ de la 2-PAM, bruit filtré, $E_b/N_0$ | 4 | p. 12-14 |
| 5 — étude pratique | 4-PAM, $f_e = 8$ kHz, $D_s = 2$ ksymboles/s, $g[n]$, normalisation, $s_l$ | 2 (q. 1-4), 3, 4 | p. 15 : énoncé seul, aucun corrigé |

**Attention : l'énoncé et la correction ne suivent pas la même version du TD.** La numérotation et le nombre des questions diffèrent pour les exercices 2 à 5 (ex. 2 : 11 questions dans l'énoncé, 6 regroupées dans la correction ; ex. 3 : 4 et 5 ; ex. 4 : 7 et 5 ; ex. 5 : 8 et 13). Les numéros de questions de `CONTEXTE_PROJET.md` (18.4) sont ceux de la **correction**. À préciser lors de la phase 2 (TD).

Notations du TD, à ajouter à la table de correspondance de la fiche matière (en plus de $h \leftrightarrow g$, $h_a \leftrightarrow g_a$, $g \leftrightarrow v$, déjà présentes) :

| Rôle | Cours (poly) | TD |
|---|---|---|
| Signal des symboles | $s_a(t)$ | $s_s(t)$ |
| Symboles | $a_n$ | $A_k$, $s_n$ (correction) |
| Débit symbole | $D_s$ | $R_s$ |
| Filtre du canal | $h_c(t)$ | $h_l(t)$ |
| Bruit | $z_l(t)$ | $n_l(t)$ |
| Échantillon reçu | $r_n$ | $r_l[n]$ |

Remarques pour les analyses suivantes :

- la correction de l'ex. 1 (p. 2) étiquette la 8-PAM par 000 → −7, 001 → −5, 011 → −3, 010 → −1, 110 → 1, 111 → 3, 101 → 5, 100 → 7 : même construction miroir que les notes (f. 4 r°) ;
- **chapitre 3** : l'énoncé définit $R_A[k] = \E(A_n A^*_{n+k})$ et $R_{s_l}(t, \tau) = \E(s_l(t)\,s_l^*(t + \tau))$, la correction $R_A[k] = \E(A_n A^*_{n-k})$ et $R_{s_l}(t, \tau) = \E(s_l(t)\,s_l^*(t - \tau))$ (comme le poly et les notes) : convention à signaler lors de l'analyse du chapitre 3.

### 13.8 Étape 4 — Rédaction (7 octobre 2026)

Fichier : `cours/02-communication-sans-bruit.qmd`. Plan de la section 11 suivi. Texte rédigé ; **figures F1 à F14 non intégrées** (étape 5) : leur emplacement est marqué dans le fichier par des commentaires `<!-- FIGURE Fn … -->`. Le statut reste `analyse` jusqu'à l'intégration des figures.

Blocs *À vérifier* dans le cours : **2 ouverts**, **3 tranchés**.

| Bloc | État |
|---|---|
| `av-exemples-mise-en-forme-manquants` (AV8) | ouvert |
| `av-signe-tf-nyquist` (AV1) | tranché |
| `av-centre-symetrie-nyquist` (AV2) | tranché |
| `av-quiz-debit-porte` (AV4) | tranché |
| `av-echelles-figure-cosinus-sureleve` (**AV9, nouveau**) | ouvert |

**AV9 — Échelles de la figure des p. 43-45** (`av-echelles-figure-cosinus-sureleve`), relevé pendant la rédaction : le graphe temporel donne $g(0) = 1$ et le graphe fréquentiel $G(0) = 10$, avec $\Ts = 1$ ms. Avec la règle de symétrie corrigée, $G(0) = g_0\Ts = 10^{-3}$ : les deux graphes ne semblent pas tracés avec la même normalisation. Proposition : normaliser les deux axes de la figure reconstruite F11 ($g/g_0$ et $G/(g_0\Ts)$) et le dire dans la légende. **Question pour Armand** : d'accord avec cette proposition (le bloc deviendrait alors tranché ou serait levé) ?

Autres choix de rédaction à valider :

- introduction du chapitre écrite en *Complément* (aucune source ne la fournit) ;
- Manchester : expression avec des portes d'amplitude ±1 et conventions G. E. Thomas / IEEE 802.3 en *Complément* (C1) ;
- cosinus surélevé : expression de $G(f)$ donnée en *Complément* (C4), $eta pprox 0{,}2$ présenté comme « valeur estimée à partir de la figure » ;
- exercices : énoncé (support), « Réponse du support » en `.solution`, justification en *Complément* ; pour le quiz p. 51, le bloc tranché est placé entre l'énoncé et la solution ;
- section « À retenir » : origine indiquée par les mentions *(notes)* et *(complément)*.

Corrections orthographiques supplémentaires sans bloc : voir le tableau de la section 13.5 (trois lignes ajoutées à l'étape 4).

Vérifications faites : rendu Quarto sans avertissement de référence croisée ; 417 formules compilées sans erreur par MathJax 3 (avec les macros de `_macros.qmd`) ; labels uniques ; imbrication des blocs conforme à `conventions.md` § 5.1 ; règle de symétrie, exercice p. 49 et cosinus surélevé vérifiés numériquement.

### 13.7 Conventions ajoutées à `conventions.md`

1. Pages citées : numérotation du PDF (§ 3.1).
2. Notes sans date : `sources/<code>/notes/date-inconnue.pdf`, source `seance: inconnue` (§ 2 et § 3.1).
3. Rapports d'analyse : `matieres/<matiere>/analyses/NN-slug.md` (§ 2).
4. Blocs *À vérifier* tranchés : classe `.tranche` et ligne **Décision** (§ 5.2).
5. Fautes d'orthographe sans effet sur le sens : corrigées sans bloc, listées dans le rapport d'analyse (§ 5.3).
