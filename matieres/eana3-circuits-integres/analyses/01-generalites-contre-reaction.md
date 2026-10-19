# EANA3 — Chapitre 1 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow (`CONTEXTE_PROJET.md`, section 11), enchaînées dans la session « Bristol — Circuits intégrés — Chapitres 1 à 5 » (8 octobre 2026), à la demande d'Armand.
> Chapitre : *Rappels et généralités sur la contre-réaction*. Fichier : `cours/01-generalites-contre-reaction.qmd`. Statut : `redige`.
> Règle appliquée : `conventions.md` § 14 (choix par défaut en section 12 ; questions bloquantes en section 14).

---

## 0. Résumé

- Le support 2025 ne contient **aucun cours rédigé** pour ce chapitre : plan (p. 1), page historique sur H. S. Black (p. 3), énoncé de l'exercice guidé « Séparation des pôles » (p. 4-5). Le contenu du cours vient donc des **notes externes** (blocs `.notes-externes`, décision d'Armand du 8 octobre 2026) : tableau numérique d'un enseignant (2020, cours 1 à 3) et notes manuscrites d'un étudiant (2023, cours 1 et 2). Les deux jeux suivent le même plan et concordent, à quelques erreurs près.
- Méthode de lecture : transcription intégrale des 30 pages manuscrites (images à 200 ppp, zooms sur chaque formule), puis contrôle des points douteux sur l'image par Claude. Toutes les formules ont été recalculées.
- Exercice intégré : **exercice guidé « Séparation des pôles »** (cours 2), énoncé du support et solutions des notes externes. Le TD 3 (modulation d'amplitude, questions sur le gain-bande) est traité au chapitre 3 (applications de la contre-réaction).
- **7 blocs *À vérifier*** ouverts (section 7), tous associés à une question (section 14).
- **7 figures** : 3 TikZ/circuitikz, 4 matplotlib (dont 1 reconstruite par calcul exact).

Citations : `[support, p. N]` = page du PDF ; `[tableau-2020-cNN, p. N]` ; `[notes-2023-cNN, p. N]` (pages des PDF).

---

## 1. Inventaire des sources

| id | Fichier (`sources/eana3/`) | Nature | Pages utilisées | Remarque |
|---|---|---|---|---|
| `support` | `support/support-cours-2025.pdf` | officielle | 1-5 | plan, Black, énoncé « Séparation des pôles » (copie identique : `support/cours02-separation-des-poles.pdf`) |
| `tableau-2020-c01` | `notes/2020-tableau-cours-01.pdf` | externe | 1-7 | p. 1 plan dactylographié ; p. 4 photographies (Black, journal, ferry) |
| `tableau-2020-c02` | `notes/2020-tableau-cours-02.pdf` | externe | 1-6 | p. 5-6 : énoncé 2016-2017 (« EA211 Contre Réaction », Y. Deval et F. Rivet) annoté ; p. 6 barrée d'une croix rouge (méthode de l'enseirbien « FAUX ») |
| `tableau-2020-c03` | `notes/2020-tableau-cours-03.pdf` | externe | 1-4 | p. 5-6 : début du chapitre 2 |
| `notes-2023-c01` | `notes/2023-cours-01-rivet.pdf` | externe | 1-5 | |
| `notes-2023-c02` | `notes/2023-cours-02-rivet.pdf` | externe | 1-6 | p. 6 inachevée |
| — | `corriges/2023-recueil-corriges-td.pdf` | externe | p. 1-2 consultées | corrigé de la mise en jambe : **non repris** (résultats faux ou inachevés, section 7) |

Transcriptions de travail (non publiées) : `sources/eana3/transcriptions/`.

---

## 2. Plan du support pour le chapitre 1

| Point du plan [support, p. 1] | Séance | Sources |
|---|---|---|
| 1. Systèmes asservis en réaction négative | cours 1 | tableau c01 p. 2 ; notes c01 p. 1 |
| 2. Robustesse, reproductibilité industrielle | cours 1 | tableau c01 p. 3, 5 ; notes c01 p. 1-2 |
| 3. Linéarisation | cours 1 | tableau c01 p. 6 ; notes c01 p. 2-3 |
| 4. Compromis gain-bande passante | cours 1 | tableau c01 p. 7 ; notes c01 p. 3 |
| 5. Stabilité | cours 2 | tableau c02 p. 1-4 ; notes c01 p. 3-5, c02 p. 1 |
| Séparation des pôles (exercice guidé) | cours 2 | support p. 4-5 ; tableau c02 p. 5-6, c03 p. 1-4 ; notes c02 p. 1-6 |

En 2023, la stabilité (marges) a été vue à la fin du cours 1 [notes-2023-c01, p. 3-5] ; en 2020, au début du cours 2.

---

## 3. Correspondance entre les deux jeux de notes

| Contenu | tableau-2020 | notes-2023 | Accord |
|---|---|---|---|
| Schéma-bloc, ①②③, $A_F$ | c01 p. 2 | c01 p. 1 | identique (notes : « $\beta_P$ » pour $\beta_F$, coquille d'écriture) |
| $\mathrm{d}A_F/A_F$ (sur $A$) | c01 p. 3 | c01 p. 1-2 | identique |
| $\mathrm{d}A_F/A_F$ (sur $\beta_F$) | c01 p. 5 | c01 p. 2 | identique, signe perdu dans les deux (`av-sensibilite-beta-signe`) |
| Linéarisation | c01 p. 6 | c01 p. 2-3 | identique |
| Gain-bande | c01 p. 7 | c01 p. 3 | **niveau du palier différent** (`av-niveau-gain-boucle-fermee`) |
| Marges, Bode | c02 p. 1-3 | c01 p. 3-5 | identique (« 45° (70°) » sur le tableau seulement) |
| Stabiliser | c02 p. 4 | c02 p. 1 | identique |
| Mise en jambe | c02 p. 5 | c02 p. 1-2 | $Z_{in}$ identique ; $Z_{out}$ : deux erreurs différentes (`av-impedance-sortie-miller`) |
| Méthode de l'enseirbien | c02 p. 6 (barrée) | c02 p. 2 ($p_2$ barré), p. 5 | identique ; $R_g$ (tableau) = $R_e$ (notes) |
| Méthode de l'enseirbienne | c03 p. 1-3 | c02 p. 3, 5-6 | identique (même numérateur sans signe « − ») |
| Capacité de compensation | c03 p. 4 | c02 p. 4 | même idée, croquis différents |

---

## 4. Contenu présent uniquement dans les notes

Tout le contenu du cours (le support n'a que le plan et l'énoncé). Éléments propres à un seul jeu :

- tableau seulement : photographies historiques (c01 p. 4) ; « Robustesse ① Rentabilité ② » (c01 p. 6) ; point critique « opposition de phase », « si 1 on prélève tout et on réinjecte tout » (c02 p. 1) ; « inconditionnellement stable » (c02 p. 3) ; coupe du MOS avec $C_{GS}$, $C_{GD}$, ordres de grandeur pF/fF (c02 p. 6) ; explication haute fréquence (transistor monté en diode, c03 p. 3) ; comparaison de trois valeurs de $C$ (c03 p. 4) ;
- notes de 2023 seulement : « pour l'exam → robustesse » ; exemple $\mathrm{d}A/A = 1$ ; « pour avoir de la $M_\varphi$ il faut réduire la BP » ; $g_m \approx 10$ mS ; « l'impédance d'un générateur de courant doit être la plus forte possible » ; graphe des pôles en fonction de $C$.

---

## 5. Informations redondantes

Les deux jeux de notes se recouvrent presque entièrement : un seul exposé est rédigé, avec les deux citations. Le corrigé `2023-recueil` p. 1-2 recoupe les notes de 2023 (même auteur) avec des erreurs : non repris.

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Schéma-bloc de la réaction négative | `01-schema-bloc-contre-reaction.tex` | `fig-schema-bloc-contre-reaction` | tableau c01 p. 2 ; notes c01 p. 1 | TikZ |
| Spectres (linéarisation) | `01-linearisation-spectres.py` | `fig-linearisation-spectres` | tableau c01 p. 6 ; notes c01 p. 2 | matplotlib |
| Compromis gain-bande | `01-gain-bande.py` | `fig-gain-bande` | tableau c01 p. 7 ; notes c01 p. 3 | matplotlib (courbes recalculées) |
| Marges de phase | `01-marges-stabilite.py` | `fig-marges-stabilite` | tableau c02 p. 2-3 ; notes c01 p. 4-5 | matplotlib (courbes recalculées) |
| Effet Miller | `01-effet-miller.tex` | `fig-effet-miller` | support p. 4 fig. 1 ; (b) reconstruit | circuitikz |
| Source commune et équivalent | `01-source-commune.tex` | `fig-source-commune` | support p. 4 fig. 2 ; notes c02 p. 2, 5 ; tableau c03 p. 1 | circuitikz |
| Pôles en fonction de $C$ | `01-separation-poles.py` | `fig-separation-poles` | **reconstruite** (calcul exact) ; croquis notes c02 p. 4, tableau c03 p. 4 | matplotlib |

Non reprises : schéma « Miller » à main levée (notes c02 p. 2, remplacé par la figure 01-effet-miller b) ; diagramme multicolore à trois valeurs de $C$ (tableau c03 p. 4, chargé et en partie ambigu : décrit dans le texte) ; Bode des notes c02 p. 4 (graduation « −50° », probablement −90°) ; croquis du MOS en coupe (décrit dans le texte).

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | Source | Résumé |
|---|---|---|
| `av-sensibilite-beta-signe` | tableau c01 p. 5 ; notes c01 p. 2 | $\frac{\mathrm{d}A_F}{A_F} \simeq \frac{\mathrm{d}\beta_F}{\beta_F}$ : le facteur $\frac{-A\beta_F}{1 + A\beta_F} \to -1$ perd son signe (barré au tableau) |
| `av-niveau-gain-boucle-fermee` | notes c01 p. 3 | palier de $A_F$ étiqueté $\log\frac{1}{A\beta_F}$ ; tableau et même notes p. 4 : $\log\frac{1}{\beta_F}$ — **contradiction entre sources** |
| `av-marge-phase-70` | tableau c02 p. 2 | « ≶ 45° (70°) » : lecture et sens incertains |
| `av-impedance-sortie-miller` | notes c02 p. 1 ; tableau c02 p. 5 | $Z_{out} = \frac{Z}{1/A - 1}$ et $\frac{AZ}{1 - A}$ : signe faux ; correct $\frac{AZ}{A - 1}$ |
| `av-capacite-miller-signe` | tableau c02 p. 5 ; notes c02 p. 2-3, 5 | $C_M = C(1 - A) \simeq AC$ avec $A$ négatif pour l'étage source commune : $A$ = valeur absolue du gain ; proposé $|A|\,C$ |
| `av-enonce-separation-poles` | support p. 4-5 | $R_e$ absent de la figure 2, $i_s$ et $V_1$ non définis (q. 9-11) |
| `av-signe-transfert-separation-poles` | tableau c03 p. 2 ; notes c02 p. 3 | numérateur $(g_m - Cp)R_eR_S$ sans le signe « − » de l'inversion |

Vérifié sans problème (recalculé) : ①②③ et $A_F$ ; $\mathrm{d}A_F/\mathrm{d}A$ ; $\mathrm{d}A_F/\mathrm{d}\beta_F$ (hors signe final) ; $\omega_0(1 + A\beta_F)$ ; $Z_{in} = Z/(1 - A)$ ; dénominateur $D(p)$ de la fonction de transfert (développement complet refait) ; $p_1 \approx 1/(g_m R_e R_S C)$ ; $p_1 p_2$ ; $p_2 \approx g_m/(C_e + C_S)$ (sous l'hypothèse $C \gg C_e, C_S$, ajoutée) ; diode $1/g_m$.

Imprécisions traitées **sans bloc** (elles ne touchent pas un résultat repris) :

- tableau c03 p. 2 : étape intermédiaire $\frac{1}{CR_s(1 + g_mR_e) + CR_e} \simeq \frac{1}{CR_e(1 + g_mR_s)}$ (terme $CR_s$ perdu ; résultat final juste) : étape non reprise, la simplification est rédigée directement ;
- notes c02 p. 5 : « $C_e = C_M + C_e$ », « $C_S = C_S + C$ » (même symbole des deux côtés) : écrit « en entrée, $C_e + C_M$ ; en sortie, $C_S + C$ » ;
- notes c01 p. 1 : « $\beta_P$ » pour $\beta_F$ (section 13) ;
- corrigé `2023-recueil` p. 1-2 : $Z_{in} = \frac{1 - A}{Z}$ (inversé), $Z_{out}$ inachevé, « $v_{out}R_s$ » au lieu de $v_{out}/R_s$ : source non reprise.

---

## 8. Passages illisibles ou ambigus

| Où | Lecture | Traitement |
|---|---|---|
| tableau c02 p. 2 | « ≶ 45° (70°) » | `av-marge-phase-70` |
| tableau c02 p. 6 | mot dans une bulle reliée à $R_g$ : « $V_f$ » ou « $Y_f$ » | non repris (annotation de schéma sans contenu exploitable) |
| tableau c02 p. 4 | « 2ᵉ coupure à $M_\varphi = 45°$ » (ou −45°) | lu 45°, cohérent avec « $M_\varphi = 45°$ » des notes c02 p. 1 |
| tableau c02 p. 4 | petit symbole « 1/D » en marge | non repris |
| tableau c01 p. 3 | « $A \to 10^6$ ~> 100 % » | repris par l'exemple des notes de 2023 ($\mathrm{d}A/A = 1$), plus lisible |
| notes c02 p. 3 | « J'aurai toujours au moins 2 pôles, 1 que je maîtrise et 1 autre dû au bruit » | **non repris** : sens incertain (« bruit » ?) ; sans incidence sur les calculs |
| notes c02 p. 4 | graduation « −50° », étiquette « $A_0C$ », axe « dB » | figure non reprise (remplacée par la figure reconstruite) |
| tableau c03 p. 4 | correspondance couleurs / courbes | décrite dans le texte sans figure |

---

## 9. Compléments ajoutés (catégorie *Complément*)

| # | Complément | Justification |
|---|---|---|
| C1 | Vocabulaire ($A$, $\beta_F$, gain de boucle), réaction négative, correspondance $v_e$/$v_i$ avec les chapitres 2-3 | notations non définies ; inversion entre sources |
| C2 | Ordre de grandeur de la robustesse | illustration |
| C3 | Rapports de composants passifs, dispersions communes | justifie « maîtriser $\beta_F$ » ; relie au chapitre 2 |
| C4 | Sens de « $A$ est un polynôme », harmoniques, limite de l'approximation | étape implicite |
| C5 | Démonstration du produit gain-bande (premier ordre) | les notes ne font que la lecture graphique |
| C6 | Définitions de $M_\varphi$ et $M_G$, rôle des pôles, 45° comme marge de conception, cas du suiveur | précision (le tableau écrit « inconditionnellement stable ») |
| C7 | Pourquoi $M_\varphi = 45°$ quand le second pôle est sur l'axe 0 dB | étape implicite |
| C8 | Nom « effet Miller », $1 - A = 1 + |A|$ | nom usuel absent des sources |
| C9 | $A = -g_mR_S$, correspondance $C \approx C_{GD}$, $C_e \approx C_{GS}$ | relie la partie 1 à la partie 2 |
| C10 | Zéro à partie réelle positive ; hypothèses des simplifications | non traité par les sources |
| C11 | Compensation Miller des amplificateurs à deux étages | situe l'exercice |

---

## 10. Exercices intégrés

| Énoncé | Contenu | Où | Solutions |
|---|---|---|---|
| Séparation des pôles, partie 1 (q. 1-4) | effet Miller | `exr-mise-en-jambe` | tableau c02 p. 5 ; notes c02 p. 1-2 |
| Partie 2 a (q. 5-7) | méthode de l'enseirbien | `exr-poles-enseirbien` | tableau c02 p. 6 (barré) ; notes c02 p. 2, 5 |
| Partie 2 b (q. 8-16) | calcul des pôles | `exr-poles-enseirbienne` | tableau c03 p. 1-3 ; notes c02 p. 3, 5-6 |
| TD 3 (modulation d'amplitude), q. 8-11 | gain de boucle, bande passante | **chapitre 3** | — |

---

## 11. Plan retenu

1. Introduction (`sec-intro-generalites`), histoire (`sec-histoire-black`) — support p. 1, 3 ; tableau c01 p. 4
2. Systèmes asservis en réaction négative (`sec-reaction-negative`)
3. Robustesse (`sec-robustesse`), prix à payer (`sec-robustesse-beta`)
4. Linéarisation (`sec-linearisation`)
5. Compromis gain-bande passante (`sec-gain-bande`)
6. Stabilité : marges (`sec-marges`), stabiliser (`sec-stabiliser`)
7. Séparation des pôles : effet Miller (`sec-effet-miller`), pôles (`sec-poles-source-commune`), capacité de compensation (`sec-capacite-compensation`)
8. À retenir (`sec-retenir-generalites`)

---

## 12. Choix appliqués par défaut (`conventions.md` § 14)

**Plan et rédaction**

1. Plan du support ; la stabilité (point 5) est traitée avant l'exercice, comme dans les deux jeux de notes.
2. Contenu des notes en blocs `.notes-externes` ; un seul exposé quand les deux jeux concordent, avec les deux citations.
3. Notations des notes conservées ($v_e$ entrée, $v_i$ entrée de l'amplificateur, $v_f$, $v_s$, $A_{OL} = A\beta_F$) ; inversion $v_e$/$v_i$ avec les énoncés des chapitres 2-3 signalée en complément (C1) et dans la fiche matière.
4. Formules à erreur de signe : écrites corrigées dans le texte, la version des sources étant citée dans le bloc *À vérifier* placé juste après (comme pour TS227).
5. Exercice guidé : énoncé du support dans `exr-` (texte de l'énoncé conservé, y compris $i_s$ et $V_1$), solutions en `.solution` contenant un bloc `.notes-externes`.
6. Page historique (support p. 3) résumée, sans recopie intégrale.
7. Remarque « dû au bruit » (notes c02 p. 3) non reprise (section 8).
8. « Inconditionnellement stable » (tableau) cité entre guillemets et nuancé en complément (C6), sans bloc : ce n'est pas une erreur de calcul.
9. Section « À retenir » : mentions *(notes externes)*, *(complément)*, *(à vérifier)*.

**Figures**

10. Gain-bande : premier ordre, $A_0 = 10^4$, $\beta_F = 10^{-2}$, axe en $\omega/\omega_0$.
11. Marges : deux pôles, $A_0 = 10^4$, $\omega_2 = 100\,\omega_1$, $\beta_F = 0{,}1$ et $0{,}001$ ($M_\varphi \approx 18°$ et $90°$).
12. Linéarisation : positions $2f_0$, $3f_0$ et amplitudes arbitraires (signalé en légende).
13. Effet Miller (b) : schéma équivalent reconstruit, en pointillés gris.
14. Pôles en fonction de $C$ : figure reconstruite par calcul exact des racines de $D(p)$, avec $g_m = 10$ mS (ordre de grandeur des notes), $R_e = R_S = 10$ kΩ, $C_e = C_S = 10$ fF ; elle montre en plus le $p_2$ faux de l'enseirbien.
15. Diagramme à trois valeurs de $C$ du tableau (c03 p. 4) décrit en texte plutôt que redessiné (ambiguïtés de couleurs).

---

## 13. Corrections orthographiques sans bloc (`conventions.md` § 5.3)

| Source | Texte de la source | Corrigé en |
|---|---|---|
| support, p. 1 | « Fonction de transfert à analyse des conséquences » | « fonction de transfert, analyse des conséquences » (comme le tableau c01 p. 1) |
| support, p. 1 | « Chapitre 2 : Amplificateurs en Contré Réaction » | (chapitre 2) « Amplificateurs en contre-réaction » |
| support, p. 5 | « déterminer effort calculatoire » | « déterminer sans effort calculatoire » (mot ajouté à la main sur l'énoncé du tableau c02 p. 6) |
| notes c01 p. 1 | « $\beta_P$ » | $\beta_F$ |
| tableau c01 p. 3 | « En ce qu'une variation de A change $A_F$ ? » | « Une variation de $A$ change-t-elle $A_F$ ? » |

---

## 14. Questions bloquantes pour Armand

> Une question par bloc ouvert ; la proposition est déjà écrite dans le bloc. Les notes n'étant pas les tiennes, une réponse du type « je ne sais pas, garde la proposition » suffit quand le point est un calcul.

1. **`av-sensibilite-beta-signe`** : retenir $\frac{\mathrm{d}A_F}{A_F} \approx -\frac{\mathrm{d}\beta_F}{\beta_F}$ (signe rétabli) ?
2. **`av-niveau-gain-boucle-fermee`** : palier de $A_F$ à $\log(1/\beta_F)$ (tableau) et non $\log(1/(A\beta_F))$ (notes de 2023) ?
3. **`av-marge-phase-70`** : sais-tu ce que représente « 70° » (marge recommandée en pratique ?) ; sinon, on garde le seul critère de 45°.
4. **`av-impedance-sortie-miller`** : retenir $Z_{out} = \frac{AZ}{A - 1}$ ?
5. **`av-capacite-miller-signe`** : retenir $C_M \approx |A|\,C$ (gain négatif de l'étage source commune) ?
6. **`av-enonce-separation-poles`** : $R_e$ = résistance de la source d'entrée, $i_s = i_e$, $V_1 = v_{gs}$ ?
7. **`av-signe-transfert-separation-poles`** : numérateur $-(g_m - Cp)R_eR_S$ ?

## 15. Validation et flashcards (étapes 6 à 8)

Décisions d'Armand du 14 octobre 2026 (« fais les démos » : décisions déléguées à Claude, sauf indication), appliquées le 18 octobre 2026 (le travail du 14 octobre n'avait pas été copié sur le PC). Vérification : références croisées, formules des cartes compilées avec MathJax 3.2.2 sans erreur. Chapitre validé, statut `flashcards`.

- `av-sensibilite-beta-signe` : tranché par Armand, résultat retenu en valeur absolue ($|\mathrm{d}A_F/A_F| \approx |\mathrm{d}\beta_F/\beta_F|$), signe « − » conservé dans l'équation.
- `av-niveau-gain-boucle-fermee`, `av-impedance-sortie-miller`, `av-capacite-miller-signe`, `av-signe-transfert-separation-poles` : propositions retenues (`.tranche`).
- `av-marge-phase-70`, `av-enonce-separation-poles` : pas des erreurs de source ; blocs retirés, contenu réintégré en complément.
- 32 cartes (`flashcards/01-generalites-contre-reaction.yml`).
