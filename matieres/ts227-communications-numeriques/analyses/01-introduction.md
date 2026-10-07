# TS227 — Chapitre 1 — Rapport d'analyse des sources

> Étapes 2 à 5 du workflow (`CONTEXTE_PROJET.md`, section 11), enchaînées dans la même session que le chapitre 4 (conversation « Bristol — TS227 Chapitres 1 et 4 — Rédaction », 7 octobre 2026).
> Chapitre : *Introduction*. Fichier : `cours/01-introduction.qmd`. Statut : `redige`.
> Règle appliquée : `conventions.md` § 14.

---

## 0. Résumé

- Le support couvre le chapitre 1 aux **pages 1 à 14** du PDF (diapositives 1 à 14/161) ; après suppression de la page de titre et des 5 pages de plan, il reste **8 pages utiles** (p. 2, 5, 7, 9, 11-14).
- **Aucune note de cours ne porte sur ce chapitre** : les notes commencent au feuillet 1 recto par le contenu du chapitre 2 (signal $s_b(t)$, voir le rapport du chapitre 2). Le chapitre est **rédigé à partir du poly seul** ; il ne contient aucun bloc `.notes`.
- Aucun exercice du TD ne porte sur ce chapitre ; le support n'y contient ni quiz ni démonstration.
- Blocs *À vérifier* : **2 ouverts** (section 7) ; **2 questions bloquantes** (section 14).
- 1 figure TikZ (modèle de Shannon et Weaver) ; historique et couches OSI en tableaux.

---

## 1. Inventaire des sources

| id | Fichier | Nature | Pages utilisées | Remarque |
|---|---|---|---|---|
| `poly` | `sources/ts227/support/poly_ts227.pdf` | officielle | 1-14 | version du 9 octobre 2025 |

Notes, TD, correction : rien pour ce chapitre.

---

## 2. Plan du support pour le chapitre 1

| Partie du poly | Pages PDF | Pages utiles | Pages écartées |
|---|---|---|---|
| Titre, plan général | 1-3 | 2 (plan du cours), 3 (plan du chapitre, repris en une phrase) | 1 (titre) |
| Définition | 4-5 | 5 | 4 (plan) |
| Historique | 6-7 | 7 | 6 (plan) |
| Modèle OSI | 8-9 | 9 | 8 (plan) |
| Modèle de Shannon et Weaver | 10-14 | 11, 12, 13, 14 | 10 (plan) |

Les p. 11 à 14 répètent le même schéma en mettant en évidence un bloc différent : une seule figure.

---

## 3-5. Correspondance avec les notes, contenu propre aux notes, redondances

Sans objet (aucune note). Redondance du support : schéma des p. 11-14.

---

## 6. Figures

| Figure | Fichier (`figures/`) | Label | Source | Outil |
|---|---|---|---|---|
| Modèle de Shannon et Weaver | `01-shannon-weaver.tex` → `.svg` | `fig-shannon-weaver` | poly p. 11-14 | TikZ → SVG (`latex` + `dvisvgm`, rendu sur le PC d'Armand) |

Tableaux : historique (`tbl-historique`), couches OSI (`tbl-couches-osi`).

---

## 7. Incohérences, contradictions et coquilles — blocs *À vérifier*

| Bloc | État | Source | Résumé |
|---|---|---|---|
| `av-osi-couches-identiques` | ouvert | poly p. 9 | couches 7, 6 et 5 décrites toutes trois par « Point d'accès aux services réseau » (copier-coller probable) ; proposition : rôles usuels de Présentation et Session |
| `av-recepteur-destination` | ouvert | poly p. 14 | « message compréhensible par la sources » ; proposition : « par la destination » |

Points traités sans bloc :

- p. 12 : diapositive intitulée « Source d'information », texte décrivant l'émetteur → texte du support conservé sous l'intertitre « Source d'information et émetteur », *Complément* sur la source (choix 3).
- p. 7 : dates conservées telles quelles ; *Complément* ajoutant l'article de Nyquist de 1928, l'article de Shannon (1948) et le livre de Shannon et Weaver (1949) sans contredire le support (choix 5).

---

## 8. Passages illisibles ou ambigus

Aucun (pas de notes ; le support est lisible).

---

## 9. Compléments ajoutés

| # | Complément | Justification |
|---|---|---|
| C1 | Place du chapitre, lien avec les chapitres 2 et 4 | aucune source |
| C2 | Échantillonnage et quantification → suite de bits, lien avec la chaîne du ch. 2 | explicite la définition p. 5 |
| C3 | Nyquist 1924 et 1928, Shannon 1948 et livre de 1949, « générations » = téléphonie mobile | connaissances générales, sans contradiction |
| C4 | Ce cours = couche 1 (PHY) | situe le cours |
| C5 | Rôle de la source d'information | titre de la p. 12 |
| C6 | Supports filaires / sans fil ↔ bande de base / bande transposée (ch. 2) ; modèle $h_c$ + bruit | relie les chapitres |
| C7 | Origine des erreurs (bruit), renvoi au ch. 4 | explicite la mise en garde p. 14 |

---

## 10. TD intégré

Aucun exercice du TD ne porte sur ce chapitre.

---

## 11. Plan retenu

1. Objet du cours (`sec-objet-cours`) — p. 2-3
2. Définitions (`sec-definitions-telecom`) — p. 5
3. Historique (`sec-historique`) — p. 7
4. Modèle OSI (`sec-modele-osi`) — p. 9
5. Modèle de Shannon et Weaver (`sec-shannon-weaver`) : émetteur, canal, récepteur — p. 11-14
6. À retenir (`sec-retenir-introduction`)

---

## 12. Choix appliqués par défaut (`conventions.md` § 14)

1. Chapitre rédigé à partir du support seul (aucune note ; demande d'Armand).
2. Plan du cours (p. 2) repris en liste, avec les titres complets (« Modulation et démodulation numériques » pour « Modulation/ démodulation numérique »).
3. p. 12 : intertitre « Source d'information et émetteur » ; le texte du support (émetteur) est conservé, la définition de la source est un *Complément*.
4. Historique et couches OSI en tableaux plutôt qu'en figures ; « Avant 1800... » conservé tel quel (« … »), sans contenu.
5. Compléments historiques ajoutés sans modifier les dates du support.
6. Couches 5 et 6 : description du support conservée en segments orange `[…]{.a-verifier}`, proposition dans le bloc.
7. « À retenir » : mentions *(complément)* et *(à vérifier)*.
8. Figure : un seul schéma pour les p. 11-14, sans mise en évidence d'un bloc ; légende décrivant les cinq éléments.

---

## 13. Corrections orthographiques sans bloc (`conventions.md` § 5.3)

| Source | Texte de la source | Corrigé en |
|---|---|---|
| poly, p. 2 | « Principes de communication en l'absence bruit » | « … en l'absence de bruit » (comme au ch. 2) |
| poly, p. 2 | « Modulation/ démodulation numérique » | « Modulation et démodulation numériques » |
| poly, p. 7 | « Transmission trans-atlantique » | « transatlantique » |
| poly, p. 7 | « 1ère génération », « 2ème »… | « 1^re^ », « 2^e^ »… |
| poly, p. 9 | « 1 Physique : Physique Transmission des signaux » | « Physique : Transmission des signaux » (mot répété) |
| poly, p. 9 | « Adresse IP », « Adresse MAC » | « adresse IP », « adresse MAC » |
| poly, p. 12 | « en signaux transmis pouvant être transmis » | « en signaux pouvant être transmis » |
| poly, p. 13 | « ondes électro-magnétiques » | « électromagnétiques » |
| poly, p. 14 | « des erreurs de transmissions » | « de transmission » |

---

## 14. Questions bloquantes pour Armand

1. **`av-osi-couches-identiques` (poly p. 9)** : remplacer les descriptions des couches 6 et 5 par les rôles usuels (Présentation : format, codage, chiffrement ; Session : ouverture, gestion, fermeture des échanges) ? Le prof a-t-il dit autre chose ?
2. **`av-recepteur-destination` (poly p. 14)** : « compréhensible par la destination » au lieu de « par la sources » ?

---

## 15. Vérifications faites (étape 6 non encore lancée)

- Formules compilées sans erreur par MathJax 3.2.2 (contrôle commun avec le chapitre 4).
- Labels uniques dans la matière ; références `@…` et liens vers le chapitre 2 résolus ; divs équilibrés.
- Figure régénérée sur le PC d'Armand et relue en image.
- **Non vérifié** : rendu Quarto (exposants `^re^` dans le tableau, segments orange dans un tableau).

---

## 16. Décisions (étape 3, 7 octobre 2026)

Armand laisse le choix à Claude : les deux propositions sont retenues, les blocs deviennent **tranchés** (`.tranche`, **Décision**).

| Q | Bloc | Décision | Application |
|---|---|---|---|
| 1 | `av-osi-couches-identiques` | rôles usuels : 6 Présentation (format, codage, compression, chiffrement), 5 Session (ouverture, gestion, fermeture des échanges) | segments orange remplacés dans `tbl-couches-osi`, mention « corrigé » ; légende et « À retenir » mises à jour |
| 2 | `av-recepteur-destination` | « compréhensible par la destination » | texte corrigé, mention du texte du support |

Bilan : **0 bloc ouvert, 2 tranchés**.
