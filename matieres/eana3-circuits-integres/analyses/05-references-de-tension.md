# EANA3 — Chapitre 5 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow, session « Bristol — Circuits intégrés — Chapitres 1 à 5 » (8 octobre 2026).
> Chapitre : *Références de tension*. Fichier : `cours/05-references-de-tension.qmd`. Statut : `redige`.
> Règle appliquée : `conventions.md` § 14.

---

## 0. Résumé

- Deuxième chapitre de la partie Deval (cours 10, 12, 13). Le support ne donne que le plan et l'énoncé du TD 5 : le cours vient des **notes externes de 2023 (cours 10)**, qui couvrent la référence bipolaire et la référence MOS ; le cours 13 (bandgap fractionnaire) n'a **aucune note**.
- Le corrigé externe `corr-2023-ref-cmos` porte sur une **autre version** du TD 5 (dual-$V_{th}$) : intégré au cours, pas comme corrigé.
- Exercices : TD 5 (référence CMOS SOI, sans corrigé de cette version), partie Deval du sujet du 24/10/2025 (Brokaw, sans corrigé), sujet du 02/04/2026 « Générateur de courant suppresseur de variations » (Deval et Rivet, sans corrigé).
- **2 blocs *À vérifier*** ; **9 figures** (7 circuitikz, 2 matplotlib).

---

## 1. Inventaire des sources

| id | Fichier (`sources/eana3/`) | Nature | Pages | Remarque |
|---|---|---|---|---|
| `support` | `support/support-cours-2025.pdf` | officielle | 2, 22-23 | plan ; énoncé TD 5 (= `td/td05-reference-tension-cmos.pdf`) |
| `td04-2026` | `td/td04-2026-recueil-sujets-deval.pdf` | officielle | 5-10 | Brokaw (Deval, 24/10/2025) ; générateur de courant (02/04/2026) |
| `notes-2023-c10` | `notes/2023-cours-10-deval.pdf` | externe | 1-6 | $V_{BE}(T)$, PTAT, Widlar, bandgap PNP, photo du tableau, bandgap CMOS, dual-$V_{th}$ |
| `corr-2023-ref-cmos` | `corriges/2023-reference-tension-cmos-dual-vth.pdf` | externe | 1-2 | autre version du TD 5 (questions 1-11) |

---

## 2. Plan du support pour le chapitre 5

| Point du plan [support, p. 2] | Séance | Sources |
|---|---|---|
| Référence bipolaire stable en température | cours 10 | notes c10 p. 1-3 ; sujet Brokaw 2025 |
| Référence MOS stable en température | cours 12 | notes c10 p. 4-6 (même jeu de notes « cours 10 ») ; corrigé dual-$V_{th}$ ; TD 5 |
| Bandgap fractionnaire | cours 13 | **aucune** (circuit à sortie fractionnaire des notes p. 3, rattachement supposé) |

---

## 3-5. Correspondances, contenu propre aux notes, redondances

- Bandgap de Widlar : déjà au chapitre 3 (exercice de F. Rivet) ; ici la version des notes de Deval (mêmes résultats), avec renvoi.
- Brokaw : partie Rivet au chapitre 3 (sujet `td03-2026`, notations $R_c$, $R_1$, $R_2$, ×8) ; partie Deval ici (`td04-2026` p. 5-6, notations $R_0$, $R_\Delta$, $R$, ×N). Figure redessinée séparément (`05-bandgap-brokaw`).
- Dual-$V_{th}$ : notes c10 p. 5 et corrigé externe concordent (notes : deux résistances « $R$ » ; corrigé : $R$ et $R_\Delta$, repris).
- Le sujet de 2026 mêle polarisation (Deval) et contre-réaction (Rivet) : rangé ici, avec renvois au chapitre 2.

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Miroir de Widlar | `05-miroir-widlar.tex` | `fig-miroir-widlar` | notes c10 p. 1 | circuitikz |
| $V_{ref}(T)$ | `05-vref-temperature.py` | `fig-vref-temperature` | notes c10 p. 3 | matplotlib (modèle usuel, valeurs choisies) |
| Bandgap à miroir PNP | `05-bandgap-pnp.tex` | `fig-bandgap-pnp` | notes c10 p. 3 | circuitikz |
| Bandgap CMOS à AOP | `05-bandgap-aop.tex` | `fig-bandgap-aop` | notes c10 p. 4 | circuitikz (polarités de l'AOP choisies par Bristol) |
| Dual-$V_{th}$ | `05-reference-dual-vth.tex` | `fig-reference-dual-vth` | notes c10 p. 5 ; corrigé | circuitikz |
| TD 5 | `05-reference-cmos-soi.tex` | `fig-reference-cmos-soi` | support p. 22 | circuitikz |
| $V_{th}(V_{BB})$ | `05-vth-vbb.py` | `fig-vth-vbb` | support p. 22 | matplotlib (droite relevée) |
| Brokaw (Deval) | `05-bandgap-brokaw.tex` | `fig-bandgap-brokaw-deval` | td04-2026 p. 5 | circuitikz |
| Générateurs de courant | `05-generateur-courant.tex` | `fig-generateur-courant` | td04-2026 p. 7-8 | circuitikz |

Non redessinés (décrits) : bandgap de Widlar des notes (p. 2, renvoi à la figure du chapitre 3), photo du tableau (p. 4), variante dual-$V_{th}$ à amplificateur (p. 6), figures 3 et 4 du sujet 2026.

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | Source | Résumé |
|---|---|---|
| `av-vref-bandgap-pnp-facteur` | notes c10 p. 3 | facteur $\frac{1}{4}$ manquant devant le terme PTAT ; conclusion TC0 inchangée |
| `av-unite-alpha-vth` | notes c10 p. 5 | $\alpha$ « 1 à 10 mV » : unité mV/K proposée |

Traités sans bloc (complément) : 1,26 V / 1,25 V et $U_T$ 26 / 25 mV (arrondis ; les sujets utilisent 1,26 V et 26 mV) ; dérivée écrite $\frac{kT}{qT}\ln N$ (= $\frac{k}{q}\ln N$) ; « Widar » pour Widlar ; dénominateur « $R_0$ » (p. 3) dans le bloc ci-dessus.

Vérifié (recalculé) : PTAT, dérivées des bandgaps (Widlar, PNP, AOP), dual-$V_{th}$ (corrigé), toutes les propositions de solution (TD 5 : 400/450 mV, 50 mV, 10 kΩ, 110 kΩ ; Brokaw ; générateur : cohérence $I_2 = I_1/e$ avec le miroir ×2,72).

---

## 8. Passages illisibles ou ambigus

| Où | Lecture | Traitement |
|---|---|---|
| notes c10 p. 2 | montage diode de $Q_1$ du bandgap de Widlar non dessiné | renvoi à la figure du chapitre 3 (support) |
| notes c10 p. 4 | photo du tableau partiellement effacée (« P' », « $\beta e^+$ ») | décrite sans ces mentions |
| notes c10 p. 4 | « $R_1$ » / « $R_x$ » | $R_1$ (cohérent avec l'annotation $\frac{R_1}{R}\Delta V_{BE}$) |
| notes c10 p. 5 | « dual » / « duel », « $\alpha$ » / « a » devant $V_{FB}$ | « dual-$V_{th}$ » ; « lié à $V_{FB}$ » |
| corr-2023-ref-cmos p. 2 | 417 ou 917 mV | non repris (données absentes) |

---

## 9. Compléments ajoutés

| # | Complément | Justification |
|---|---|---|
| C1 | Le problème des références ; lien avec le chapitre 3 | contexte |
| C2 | Sens de $\gamma$, $\alpha$, $V_{BG_0}$ | non définis dans les notes |
| C3 | 1,25 / 1,26 V, courbure | écart entre pages |
| C4 | Intérêt de la sortie fractionnaire | explication ; rattachement au cours 13 supposé |
| C5 | PNP parasite, polarités de l'AOP | explication, choix de figure |
| C6 | Analogie dual-$V_{th}$ / bandgap | explication |
| C7 | TD 5 complet | aucun corrigé de cette version |
| C8 | Brokaw (partie Deval) complet | aucun corrigé |
| C9 | Générateur de courant (parties I et II) complet | aucun corrigé |

---

## 10. Exercices intégrés

| Énoncé | Où | Solutions |
|---|---|---|
| TD 5 « Référence de tension CMOS stable en température » | `exr-reference-cmos` | complément |
| Sujet 24/10/2025, partie Deval (Brokaw) | `exr-bandgap-brokaw-deval` | complément |
| Sujet 02/04/2026 « Générateur de courant suppresseur de variations » | `exr-generateur-courant` | complément |

---

## 11. Plan retenu

1. Introduction (`sec-intro-references`)
2. Référence bipolaire : $V_{BE}(T)$, PTAT, Widlar, bandgap PNP fractionnaire
3. Référence MOS : bipolaires en CMOS, bandgap à AOP, dual-$V_{th}$
4. Bandgap fractionnaire (cours 13, vide)
5. TD 5 ; Brokaw (Deval) ; générateur de courant
6. À retenir (`sec-retenir-references`)

---

## 12. Choix appliqués par défaut

1. Cours en `.notes-externes` ; le corrigé d'une autre version du TD 5 sert de cours (dual-$V_{th}$).
2. Notations $R$ / $R_\Delta$ du corrigé pour le dual-$V_{th}$ (les notes nomment les deux résistances $R$).
3. Sujet de 2026 rangé au chapitre 5 en entier (partie II renvoie au chapitre 2).
4. Polarités de l'amplificateur de la @fig-bandgap-aop choisies par Bristol (justifiées en complément).
5. Section « Bandgap fractionnaire » laissée vide, avec renvoi au circuit fractionnaire des notes.

---

## 13. Corrections orthographiques sans bloc

| Source | Texte | Corrigé en |
|---|---|---|
| notes c10 p. 1 | « Problème de tension stables » | non cité |
| notes c10 p. 1-2 | « Widar » | « Widlar » |
| td04-2026 p. 6 | « ce qui lui vaut sont nom » | « son nom » |
| td04-2026 p. 9 | « le gain en courant Gi du de l'amplificateur » | « de l'amplificateur » |
| td04-2026 p. 9 | « type de contre-réaction mise en œuvre » | « mis en œuvre » |

---

## 14. Questions bloquantes pour Armand

1. **`av-vref-bandgap-pnp-facteur`** : facteur $\frac{1}{4}$ devant le terme PTAT ?
2. **`av-unite-alpha-vth`** : $\alpha$ en mV/K ?
3. **Bandgap fractionnaire (cours 13)** : le circuit à pont $R_1$, $R_2$ des notes est-il bien ce que l'enseignant appelle « bandgap fractionnaire » ?

Non bloquant : corrigés éventuels du TD 5 (version SOI), du sujet Brokaw 2025 et du sujet 2026.

## 15. Validation et flashcards (étapes 6 à 8)

Décisions d'Armand du 14 octobre 2026 (« fais les démos » : décisions déléguées à Claude, sauf indication), appliquées le 18 octobre 2026 (le travail du 14 octobre n'avait pas été copié sur le PC). Vérification : références croisées, formules des cartes compilées avec MathJax 3.2.2 sans erreur. Chapitre validé, statut `flashcards`.

- `av-vref-bandgap-pnp-facteur`, `av-unite-alpha-vth` : propositions retenues (`.tranche`).
- 32 cartes (`flashcards/05-references-de-tension.yml`).
