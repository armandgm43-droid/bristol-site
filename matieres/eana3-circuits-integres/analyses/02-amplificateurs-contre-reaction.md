# EANA3 — Chapitre 2 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow (`CONTEXTE_PROJET.md`, section 11), session « Bristol — Circuits intégrés — Chapitres 1 à 5 » (8 octobre 2026).
> Chapitre : *Amplificateurs en contre-réaction*. Fichier : `cours/02-amplificateurs-contre-reaction.qmd`. Statut : `redige`.
> Règle appliquée : `conventions.md` § 14.

---

## 0. Résumé

- Support : plan seulement (p. 1-2) et énoncé du TD 1 « Où est la contre-réaction ? » (p. 11-12). Le cours vient des **notes externes** : notes de 2023 (cours 4 et 6, les quatre contre-réactions et la synthèse) et tableau de 2020 (cours 3 p. 5-6 et cours 4 : trois contre-réactions, sans la tension-parallèle).
- Les deux jeux concordent sur tous les résultats ; tous les calculs ont été refaits.
- Exercice intégré : **TD 1** (« Où est la contre-réaction ? »), solutions des notes de 2023 (cours 8, où l'exercice a été fait en 2023) et du corrigé externe de 2023.
- **Aucun bloc *À vérifier*** : les seuls doutes sont des lectures que le contexte tranche sans ambiguïté (section 8).
- **6 figures** circuitikz.
- Changement de rattachement par rapport à l'inventaire : `notes-2023-c08` (« Où est la contre-réaction ? ») est utilisé ici avec le TD 1, et non au chapitre 3 ; les TD 2 (« Un circuit pour l'espace ») et TD 3 (« Modulation d'amplitude »), qui sont des applications complètes de la contre-réaction, sont intégrés au chapitre 3 (section 10).

---

## 1. Inventaire des sources

| id | Fichier (`sources/eana3/`) | Nature | Pages utilisées | Remarque |
|---|---|---|---|---|
| `support` | `support/support-cours-2025.pdf` | officielle | 1-2, 11-12 | énoncé du TD 1 (= `td/td01-ou-est-la-contre-reaction.pdf`) |
| `tableau-2020-c03` | `notes/2020-tableau-cours-03.pdf` | externe | 5-6 | topologies, début courant-série |
| `tableau-2020-c04` | `notes/2020-tableau-cours-04.pdf` | externe | 1-9 | courant-série, tension-série, courant-parallèle |
| `notes-2023-c04-06` | `notes/2023-cours-04-06-rivet.pdf` | externe | 1-8 | quatre contre-réactions et synthèse |
| `notes-2023-c08` | `notes/2023-cours-08-rivet.pdf` | externe | 1-4 | TD 1 traité en cours |
| `corr-2023-recueil` | `corriges/2023-recueil-corriges-td.pdf` | externe | 3 | corrigé du TD 1 (même auteur que les notes de 2023) |

Non utilisés (énoncé absent, section 5) : `corriges/2023-td01-amplificateur-contre-reaction.pdf` (et recueil p. 4) : contre-réaction tension-parallèle d'un étage bipolaire à résistance base-collecteur ; `corriges/2023-td02-contre-reaction-mode-commun.pdf` (et recueil p. 5) : contre-réaction de mode commun.

---

## 2. Plan du support pour le chapitre 2

| Point du plan [support, p. 1-2] | Séance | Sources |
|---|---|---|
| 0. Topologies des quadripôles | cours 4 | tableau c03 p. 5 ; notes c04-06 p. 1 |
| 1. Tension-parallèle | cours 4 | notes c04-06 p. 6-7 (tableau : absent) |
| 2. Courant-parallèle | cours 4 | tableau c04 p. 7-9 ; notes c04-06 p. 3-4 |
| 3. Tension-série | cours 6 | tableau c04 p. 4-6 ; notes c04-06 p. 5-6 |
| 4. Courant-série | cours 6 | tableau c03 p. 6, c04 p. 1-3 ; notes c04-06 p. 1-3 |
| 5. Synthèse | cours 6 | notes c04-06 p. 8 |

Ordre des notes : courant-série, courant-parallèle, tension-série, tension-parallèle (2023) ; courant-série, tension-série, courant-parallèle (2020). Le chapitre suit l'ordre du support (choix 1).

---

## 3. Correspondance entre les deux jeux de notes

| Contenu | tableau-2020 | notes-2023 | Accord |
|---|---|---|---|
| 4 possibilités de transfert, Norton/Thévenin | c03 p. 5 | c04-06 p. 1 | identique ; notes : remarques sur $Z_s$ |
| Courant-série | c03 p. 6, c04 p. 1-3 | p. 1-3 | identique ; tableau : charge $Z_L \ll Z_s$ |
| Tension-série | c04 p. 4-6 | p. 5-6 | identique |
| Courant-parallèle | c04 p. 7-9 | p. 3-4 | identique |
| Tension-parallèle | — | p. 6-7 | notes seules |
| Synthèse | — | p. 8 | notes seules |

---

## 4. Contenu présent uniquement dans les notes

Tout le cours. Propre à un seul jeu : noms anglais *series-series*, *series-shunt*, *shunt-series* et « on éteint les générateurs indépendants » (tableau) ; équivalences source de courant éteinte = circuit ouvert, source de tension éteinte = court-circuit, remarques sur $Z_s$, tableau de synthèse, remarque « transistors 20 nm » (notes de 2023).

---

## 5. Informations redondantes et sources non utilisées

- Les deux jeux de notes se recouvrent : un seul exposé, deux citations.
- Le corrigé `2023-recueil` p. 3 recoupe les notes `c08` (même auteur) : cité pour $Z_i = r_{be}(1 + g_mR_x)$, plus complet que les notes.
- **Non intégrés**, faute d'énoncé : corrigé « TD1 Amplificateur à contre-réaction » (2023 ; contre-réaction tension-parallèle, $\beta_F = -1/R_2$, transimpédance) et corrigé « TD2 Contre-réaction de mode commun » (2023 ; tension-série, $\beta_F = 1$). Ils pourront illustrer la tension-parallèle et la tension-série si Armand retrouve les énoncés (question 2, section 14).

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Modèles Norton et Thévenin | `02-modeles-quadripoles.tex` | `fig-modeles-quadripoles` | notes c04-06 p. 1 ; tableau c03 p. 5 | circuitikz |
| Tension-parallèle | `02-cr-tension-parallele.tex` | `fig-cr-tension-parallele` | notes c04-06 p. 6 | circuitikz |
| Courant-parallèle | `02-cr-courant-parallele.tex` | `fig-cr-courant-parallele` | notes c04-06 p. 3 ; tableau c04 p. 7 | circuitikz |
| Tension-série | `02-cr-tension-serie.tex` | `fig-cr-tension-serie` | notes c04-06 p. 5 ; tableau c04 p. 4 | circuitikz |
| Courant-série | `02-cr-courant-serie.tex` | `fig-cr-courant-serie` | notes c04-06 p. 1 ; tableau c03 p. 6, c04 p. 1 | circuitikz |
| TD 1 : montage et quadripôles | `02-ou-est-la-contre-reaction.tex` | `fig-ou-est-la-contre-reaction` | support p. 11 ; notes c08 p. 2-3 ; recueil p. 3 | circuitikz |

Les quatre schémas de contre-réaction ont la même disposition (bloc $A$ en haut, $\beta_F$ en bas), pour pouvoir les comparer.

---

## 7. Incohérences, contradictions et coquilles

Aucun bloc *À vérifier*. Points traités sans bloc :

- notes c08 p. 4 : $Z_i = g_m r_{be} R_x$, $Z_{out} = g_m r_{ce} R_x$ (le « 1 + » est omis) : approximations pour $g_m R_x \gg 1$ ; le corrigé du même auteur donne $r_{be}(1 + g_mR_x)$ ; les deux sont cités, condition ajoutée en complément ;
- notes c08 p. 1 : « montage source commune » pour un transistor bipolaire : précisé en complément (émetteur commun) ;
- notes c04-06 p. 2-3 : $Z_{out} = v_o/i_o = v_s/i_o$ (le port de prélèvement de $\beta_F$, un fil, a une tension nulle) : calcul repris sous la forme du tableau, $v_o = Z_s(i_o - Av_e)$ ;
- sources commandées dessinées avec le même losange (courant ou tension) : type déduit de la topologie (Norton : en parallèle ; Thévenin : en série avec $Z_s$), redessinées avec les symboles distincts de circuitikz.

Vérifié (recalculé) : fonctions de transfert, $Z_i$ et $Z_o$ des quatre contre-réactions ; TD 1 q. 4-8.

---

## 8. Passages illisibles ou ambigus

| Où | Lecture | Traitement |
|---|---|---|
| tableau c04 p. 2 | titre « fonction de transfert $v_o/v_i$ » ? | lu $i_o/v_i$ : annoncé p. 1 et seul compatible avec le calcul (pas de question) |
| notes c04-06 p. 2 | indice de $A$ dans $Z_i = Z_e(1 + A_?)$ : « α » ou « OL » | lu $A_{OL}$ (écrit nettement aux pages suivantes ; égal à $A\beta_F$ dans le calcul) |
| tableau c04, toutes pages | indice « fs » ou « fb » | lu $fb$ (net p. 3-4) |
| tableau c04 p. 6, p. 9 | « l'amplificateur [de boucle / de base] » | mot non repris (« l'impédance de sortie est celle de l'amplificateur… ») |
| tableau c04 p. 9 | « $A_{OC}$ » | lu $A_{OL}$ |
| notes c08 p. 1 | « $R_1$ (ou $R_L$) fait la polarisation » | écrit « la résistance de polarisation » (la figure la nomme $R_b$) |
| notes c04-06 p. 5 | « En analogique on se limite à des transistors 20 nm » | repris tel quel, signalé « sans lien explicite avec le calcul » |

---

## 9. Compléments ajoutés

| # | Complément | Justification |
|---|---|---|
| C1 | Introduction : nature des signaux | relie au chapitre 1 |
| C2 | Prélèvement/réinjection : série ou parallèle ; noms anglais complets ; notations ($v_i$/$v_e$ inversées par rapport au ch. 1) ; hypothèses des quadripôles idéaux | les notes ne les explicitent pas |
| C3 | Règle à retenir, quadripôle idéal, nature et unités de $A$ et $\beta_F$, renvoi au chapitre 1 | synthèse |
| C4 | TD 1 : émetteur commun, conditions des approximations, robustesse par rapport de résistances, limites du découpage en quadripôles | précision |

---

## 10. Exercices intégrés

| Énoncé | Où | Solutions |
|---|---|---|
| TD 1 « Où est la contre-réaction ? » (q. 1-8) | `exr-ou-est-la-contre-reaction` | notes c08 p. 1-4 ; recueil p. 3 |
| TD 2 « Un circuit pour l'espace » | **chapitre 3** | — |
| TD 3 « Modulation d'amplitude » | **chapitre 3** | — |
| TD additionnel « VDD is not your BFF » | **chapitre 3** | — |

---

## 11. Plan retenu

1. Introduction (`sec-intro-amplificateurs-cr`)
2. Topologies des quadripôles (`sec-topologies-quadripoles`)
3. Tension-parallèle (`sec-cr-tension-parallele`)
4. Courant-parallèle (`sec-cr-courant-parallele`)
5. Tension-série (`sec-cr-tension-serie`)
6. Courant-série (`sec-cr-courant-serie`)
7. Synthèse (`sec-synthese-cr`, `tbl-synthese-contre-reaction`)
8. Exercice : où est la contre-réaction ? (`sec-td-ou-est-la-contre-reaction`)
9. À retenir (`sec-retenir-amplificateurs-cr`)

---

## 12. Choix appliqués par défaut

1. Ordre du support (tension-parallèle, courant-parallèle, tension-série, courant-série), différent de celui des deux jeux de notes (signalé en tête de chapitre).
2. Notations des énoncés et des notes du chapitre ($v_i$ entrée du montage, $v_e$ entrée de $A$), inverses de celles du chapitre 1 : signalé en complément et dans la fiche matière.
3. Un seul exposé quand les deux jeux concordent ; calcul de $Z_o$ du courant-série et du courant-parallèle sous la forme du tableau ($v_o = Z_s(i_o - \dots)$), plus explicite que celle des notes de 2023.
4. Tableau de synthèse des notes en tableau Markdown labellisé ; libellés « C+ », « C// »… conservés entre parenthèses.
5. TD 1 rattaché à ce chapitre (identification du type et application directe des formules) ; TD 2, TD 3 et « VDD is not your BFF » au chapitre 3 (applications plus longues, mêlant statique, contre-réaction et bande passante).
6. Figures : schémas redessinés avec des symboles distincts pour les sources de courant et de tension commandées ; disposition commune aux quatre topologies ; ponts aux croisements de fils sans connexion (comme dans les notes).

---

## 13. Corrections orthographiques sans bloc

| Source | Texte de la source | Corrigé en |
|---|---|---|
| support, p. 1 | « Chapitre 2 : Amplificateurs en Contré Réaction » | « Amplificateurs en contre-réaction » |
| support, p. 12 | « de part leur proximité physique » | « du fait de leur proximité physique » |
| notes c04-06 p. 3 | « L'impédance de sortie est multiplié » | « multipliée » |
| notes c04-06 p. 7 | deuxième « b – impédance de sortie » | « c. Impédance de sortie » |

---

## 14. Questions bloquantes pour Armand

Aucune question bloquante sur le contenu. Deux demandes non bloquantes :

1. Les notes de 2023 et le tableau de 2020 suivent l'ordre courant-série → … ; le chapitre suit l'ordre du support (tension-parallèle d'abord). Si le cours de 2026 suit un autre ordre, le dire.
2. Si tu as les énoncés des corrigés « TD1 Amplificateur à contre-réaction » et « TD2 Contre-réaction de mode commun » (2023), ils pourraient servir d'exemples de tension-parallèle et de tension-série.

## 15. Validation et flashcards (étapes 6 à 8)

Décisions d'Armand du 14 octobre 2026 (« fais les démos » : décisions déléguées à Claude, sauf indication), appliquées le 18 octobre 2026 (le travail du 14 octobre n'avait pas été copié sur le PC). Vérification : références croisées, formules des cartes compilées avec MathJax 3.2.2 sans erreur. Chapitre validé, statut `flashcards`.

- Aucun bloc *À vérifier*.
- 23 cartes (`flashcards/02-amplificateurs-contre-reaction.yml`), centrées sur les impédances d'entrée et de sortie selon le type de contre-réaction (règle générale, une carte par montage, cartes inverses « impédances → topologie »).
