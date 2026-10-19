# EANA3 — Chapitre 3 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow, session « Bristol — Circuits intégrés — Chapitres 1 à 5 » (8 octobre 2026).
> Chapitre : *Applications de la théorie de la contre-réaction*. Fichier : `cours/03-applications-contre-reaction.qmd`. Statut : `redige`.
> Règle appliquée : `conventions.md` § 14.

---

## 0. Résumé

- Chapitre d'**exercices** : le support donne les énoncés des deux exercices guidés du plan (dégénérescence inductive, cours 8 ; bandgap de Widlar, cours 11) ; Bristol y rattache les TD d'application de F. Rivet (TD 2, TD 3, « VDD is not your BFF ») et la partie Rivet du sujet du 24 octobre 2025 (bandgap de Brokaw, distribué comme TD 3 en 2026).
- Solutions disponibles : notes de 2023 (Widlar, cours 11), corrigé manuscrit externe du sujet 2016-2017 (dégénérescence inductive, q. 1-8), corrigé du recueil 2023 (Widlar, erroné, non repris). **Les 4 TD n'ont aucun corrigé** : solutions proposées par Claude en *Complément*, explicitement signalées comme telles.
- « Stabilité et compensation » (cours 11) : **aucune note** ; renvoi au chapitre 1.
- **2 blocs *À vérifier*** (section 7).
- **6 figures** circuitikz (énoncés redessinés).

---

## 1. Inventaire des sources

| id | Fichier (`sources/eana3/`) | Nature | Pages | Remarque |
|---|---|---|---|---|
| `support` | `support/support-cours-2025.pdf` | officielle | 2, 6-10, 13-19, 29-30 | énoncés (copies séparées identiques dans `support/` et `td/`) |
| `td03-2026` | `td/td03-2026-bandgap-brokaw.pdf` | officielle | 1-2 | sujet EANA3 du 24/10/2025 (partie Rivet) |
| `notes-2023-c11` | `notes/2023-cours-11-rivet.pdf` | externe | 1-2 | Widlar |
| `annale-2016-2017` | `annales/2016-2017-corrige-manuscrit.pdf` | externe | 1-2 | corrigé de la dégénérescence inductive, q. 1-8 |
| `corr-2023-recueil` | `corriges/2023-recueil-corriges-td.pdf` | externe | 11 | Widlar, q. 1-5, erreurs : cité, non repris |

Non utilisés : `corriges/2023-td03-circuit-immunise.pdf` et recueil p. 6-7 (autre version du TD 2 : deux résistances, autre plan) ; `annales/2017-2018-corrige-manuscrit.pdf` (« amplificateur large bande », énoncé absent).

---

## 2. Plan du support pour le chapitre 3

| Point du plan [support, p. 2] | Séance | Sources |
|---|---|---|
| 1. Adaptation d'impédance par dégénérescence inductive (exercice guidé) | cours 8 | support p. 6-7 ; annale 2016-2017 |
| 2. Bandgap de Widlar (exercice guidé) | cours 11 | support p. 8-10 ; notes c11 |
| Stabilité et compensation | cours 11 | **aucune** |

---

## 3-5. Correspondances, contenu propre aux notes, redondances

- Widlar : notes c11 (q. 1-11) ; recueil p. 11 (q. 1, 2, 4, 5, avec deux erreurs) : les notes sont reprises, le recueil seulement cité.
- Dégénérescence : seul le corrigé externe 2016-2017 (le sujet 2016-2017 est l'énoncé du cours 8 de 2025).
- Pas de notes de cours sur le cours 8 de 2025 (en 2023, le cours 8 portait sur « Où est la contre-réaction ? », intégré au chapitre 2).

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| LNA et quadripôles | `03-lna-degenerescence.tex` | `fig-lna-degenerescence` | support p. 6 ; annale 2016-2017 p. 1 | circuitikz |
| Bandgap de Widlar | `03-bandgap-widlar.tex` | `fig-bandgap-widlar` | support p. 8 | circuitikz |
| Générateur dual-$V_T$ | `03-dual-vt.tex` | `fig-dual-vt` | support p. 15 | circuitikz |
| Modulateur AM | `03-modulateur-am.tex` | `fig-modulateur-am` | support p. 17 | circuitikz |
| LDO | `03-ldo.tex` | `fig-ldo` | support p. 29 | circuitikz |
| Bandgap de Brokaw | `03-bandgap-brokaw.tex` | `fig-bandgap-brokaw` | td03-2026 p. 1 | circuitikz |

Non redessinées (décrites dans l'énoncé) : figure 2 de Widlar (circuit redessiné en quadripôles), figures 1-2 et 4-5 du TD 2 (irradiation, circuit complet, OTA, schéma-bloc), gabarits de gain du TD 3 et du LDO.

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | Source | Résumé |
|---|---|---|
| `av-application-numerique-lna` | annale 2016-2017 p. 2 | « $\omega = 2\pi f = 900$ MHz » ; unité de $L$ illisible (nH/mH) ; proposé : 12,5 nH (recalculé) |
| `av-widlar-contre-reaction` | notes c11 p. 2 | $A = -g_mR_3$ (gain en tension, et non transimpédance), $\beta_F = 1/R_2$ (signe), $Z_o$ et conclusions incohérents ; proposé : $A = -\beta R_3$, $\beta_F = -1/R_2$, $Z_o \approx \frac{1/g_m}{1 + \beta R_3/R_2}$ |

Vérifié (recalculé) : dégénérescence q. 3-8 ($\beta_F$, $Z_i$, $\omega_0$, 12,5 nH) ; Widlar q. 1-7 ($-2{,}2$ mV/K arrondi à −2 dans les notes) ; énoncé TD 2 q. 7 (formule de $A_r$ redémontrée, identique à l'énoncé).

Traités sans bloc : recueil p. 11 (erreurs, non repris) ; notes c11 p. 1 : $V_{ref}$ écrit avec $V_{be_1}$ puis $V_{be_{err}}$ (égaux à l'équilibre, précisé en complément) ; « $V_{3G}$ » lu $V_{BG}$.

---

## 8. Passages illisibles ou ambigus

| Où | Lecture | Traitement |
|---|---|---|
| notes c11 p. 2 | numérateur « $Z_s$ » ou « $Z_1$ » de $Z_o$ | dans `av-widlar-contre-reaction` |
| notes c11 p. 2 | titre « III – Qerr, ac » ; pas de titre « acte 3 » | numérotation de l'énoncé utilisée |
| annale 2016-2017 p. 2 | unité « nH » / « mH » | `av-application-numerique-lna` |
| support p. 15 (texte extrait) | formule de $A_r$ illisible dans l'extraction | lue sur l'image : $A_r = r_{DS}\frac{1 - g_m R}{1 + g_m r_{DS}}$ |

---

## 9. Compléments ajoutés

| # | Complément | Justification |
|---|---|---|
| C1 | Méthode commune | synthèse des chapitres 1-2 |
| C2 | Dégénérescence, q. 9-10 ($V_o/V_i = jR_L/(L\omega_0)$, module ≈ 9,9) ; $\omega_T$ | sans corrigé |
| C3 | Widlar : CTAT/PTAT, égalité des tensions dans les $R_2$, $V_{BG}$, rôle de $Q_{err}$ | précisions |
| C4 | TD 2 complet (q. 1-10) | sans corrigé de cette version |
| C5 | TD 3 complet (q. 1-10) | sans corrigé |
| C6 | VDD is not your BFF (q. 1-10) ; q. 6 signalée « lecture proposée, à confirmer » | sans corrigé |
| C7 | Brokaw (q. 1-10) ; remarque $g_mR_2 = \ln 8$ ; remarque d'unités | sans corrigé |

Les solutions C4-C7 sont des **propositions** : elles appliquent la méthode du cours, mais aucune source ne permet de les vérifier. À relire en priorité à la validation.

---

## 10. Exercices intégrés

| Énoncé | Où | Solutions |
|---|---|---|
| Dégénérescence inductive (cours 8), q. 1-10 | `exr-degenerescence-inductive` | annale 2016-2017 (q. 1-8) ; complément (q. 9-10) |
| Widlar (cours 11), q. 1-11 | `exr-bandgap-widlar` | notes c11 ; AV (q. 9-11) ; complément |
| TD 2 « Un circuit pour l'espace » | `exr-circuit-espace` | complément |
| TD 3 « Modulation d'amplitude » | `exr-modulation-amplitude` | complément |
| TD additionnel « VDD is not your BFF » | `exr-vdd-bff` | complément |
| Sujet 2025 « Une référence des circuits intégrés » (Brokaw, partie Rivet) | `exr-bandgap-brokaw` | complément |

---

## 11. Plan retenu

1. Introduction et méthode (`sec-intro-applications-cr`)
2. Dégénérescence inductive (`sec-degenerescence-inductive`)
3. Bandgap de Widlar (`sec-bandgap-widlar`), stabilité et compensation (`sec-stabilite-compensation`)
4. TD 2 (`sec-td-circuit-espace`) ; TD 3 (`sec-td-modulation-amplitude`) ; VDD (`sec-td-vdd`) ; Brokaw (`sec-td-brokaw`)
5. À retenir (`sec-retenir-applications-cr`)

---

## 12. Choix appliqués par défaut

1. Énoncés reproduits (questions intégrales ; textes d'introduction des TD 2 et VDD résumés, figures non redessinées décrites entre parenthèses).
2. TD sans corrigé : solution en `.complement` intitulée « Proposition de solution (aucun corrigé) » ; points incertains signalés dans le texte (VDD q. 6, Brokaw q. 6-7).
3. Sujet de Brokaw : partie Rivet ici (contre-réaction), partie Deval au chapitre 5 (référence de tension).
4. « Stabilité et compensation » : section courte qui signale l'absence de notes et renvoie au chapitre 1.
5. Notation de l'énoncé du TD 2 conservée ($A_r$).
6. Figures : sources de courant de polarisation orientées vers le bas (courant fourni par l'alimentation) ; ponts aux croisements de fils sans connexion.

---

## 13. Corrections orthographiques sans bloc

| Source | Texte | Corrigé en |
|---|---|---|
| support, p. 9 | « Proportional To Absolut Temperature » | « Absolute » |
| support, p. 17 | « Collpits » | « Colpitts » |
| support, p. 18 | « un premier noté « A » … avec pour entrée, la la tension » | « avec pour entrée la tension » |
| td03-2026, p. 2 | « Quel type de contre-réaction est mise en œuvre » | « est mis en œuvre » |

---

## 14. Questions bloquantes pour Armand

1. **`av-widlar-contre-reaction`** : retenir l'identification proposée ($A$ transimpédance $-\beta R_3$, $\beta_F = -1/R_2$, $Z_o$ très faible) ? Sinon, que donnait la correction de l'enseignant ?
2. **`av-application-numerique-lna`** : $L = 12{,}5$ nH (avec $\omega_0 = 2\pi \times 900$ MHz) ?

Non bloquant : si un corrigé officiel des TD 2, TD 3, « VDD is not your BFF » ou du sujet 2025 existe, le fournir permettrait de remplacer les compléments.

## 15. Validation et flashcards (étapes 6 à 8)

Décisions d'Armand du 14 octobre 2026 (« fais les démos » : décisions déléguées à Claude, sauf indication), appliquées le 18 octobre 2026 (le travail du 14 octobre n'avait pas été copié sur le PC). Vérification : références croisées, formules des cartes compilées avec MathJax 3.2.2 sans erreur. Chapitre validé, statut `flashcards`.

- `av-application-numerique-lna`, `av-widlar-contre-reaction` : propositions retenues (`.tranche`).
- Les solutions des TD restent en complément, sans corrigé officiel.
- 25 cartes (`flashcards/03-applications-contre-reaction.yml`).
