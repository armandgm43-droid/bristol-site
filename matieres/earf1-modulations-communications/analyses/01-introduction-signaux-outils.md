# EARF1 ch. 1 — Introduction : signaux et outils d'analyse : rapport d'analyse

> 29 octobre 2026. Document de travail. Étapes 2 à 7 faites dans la même session, à la demande d'Armand (« fais toutes les étapes jusqu'à ce que ce cours soit considéré comme validé ») : les blocs *À vérifier* ont été tranchés par Claude sur délégation d'Armand.

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `mod-ana` | `sources/earf1/support/cours-01-modulations-analogiques.pdf` (54 p., version « Student ») | officielle | p. 1-18 |
| `notes-2023-ana` | `sources/earf1/notes/2023-notes-modulations-analogiques.pdf` | externe (ancien élève, promotion 2023) | p. 1-3 |

Pas de notes d'Armand pour cette matière. Le support « Student » ne comporte **aucun trou** (vérifié page par page) : Armand l'a confirmé (« t'as le cours complet »).

## 2. Correspondance et contenu repris

| Support | Contenu | Section |
|---|---|---|
| p. 1-3, 9 | titre, sommaires (non repris) | — |
| p. 4 | signal, exemples, télécommunications | `sec-signal-telecom` |
| p. 5-6 | antenne, $L_0 = c/2f = \lambda/2$, exemples 15 km / 15 cm | `sec-antenne` |
| p. 7 | moduler / démoduler, chaîne Tx-Rx | `sec-moduler-demoduler`, figure F1 |
| p. 8 | types de modulations, deux étapes | `sec-types-modulations` |
| p. 10 | classification des signaux | `sec-classification-signaux` |
| p. 11-12 | TF, cos et sin, représentations | `sec-transformee-fourier` |
| p. 13 | série de Fourier, amplitude et phase | `sec-serie-fourier` |
| p. 14 | signaux non périodiques | `sec-signaux-non-periodiques` |
| p. 15 | puissance, Parseval | `sec-puissance-signal` |
| p. 16-18 | mélangeur, modulant sinusoïdal et quelconque | `sec-decalage-frequence`, figure F2 |

Notes externes : p. 1 (maximum de puissance transmise à l'antenne ; « angulaires + robustes »), p. 2 (TF, série de Fourier : doublons sauf la phase, voir § 6), p. 3 (mélangeur : doublon).

## 3. Blocs *À vérifier* (tous tranchés)

| id | Question | Décision |
|---|---|---|
| `av-tf-pulsation-frequence` | p. 11 : TF notée « TFD », mélange $f$ / $\omega$ (Dirac en $\omega$, facteur $2\pi$), unité $i$ | écrire tout en $f$, noter « TF » |
| `av-indices-fourier` | p. 13 : $n$ manquant dans $a_n$, $b_n$ ; p. 14 : $\varphi_x(n)$ pour $\varphi_x(f)$ | corrigé |

## 4. Corrections de forme (sans bloc, conventions § 5.3)

- p. 10 : « Tranformée » → « Transformée » ; p. 14 : « signal quelconque non période » → « non périodique ».
- p. 13 : « $\varphi_x(n) = \_\arctan$ » (signe moins mal rendu dans le PDF) lu « $-\arctan$ », confirmé par la reconstruction du calcul.

## 5. Choix par défaut (conventions § 14)

- Convention de la TF : $e^{-j2\pi ft}$, unité imaginaire $j$ (forme de la p. 14) ; notée dans la fiche matière.
- Figures : F1 chaîne de transmission (matplotlib, redessinée), F2 spectres du mélangeur (deux cas sur une figure). Les antennes et les dessins humoristiques des p. 5-6 ne sont pas repris (valeurs dans le texte).
- Compléments : vérification numérique des longueurs d'antenne, phase $-\pi/2$ du sinus, signe de $\varphi_x$, facteur 2 de $A_x(f)$, forme usuelle de Parseval, théorème de modulation.
- La remarque « Cas des télécommunications → aléatoire » (flèche de la p. 10) est rédigée en phrase.

## 6. Sources externes : erreurs non reprises

- [notes-2023-ana, p. 2] : $\varphi_x(n) = \arctan(b_n/a_n)$ sans le signe moins : signalé en *Complément*, le support est juste.
- [notes-2023-ana, p. 1] : « grosses antennes ⇒ − d'atténuation car en HF atténuation + rapide » : lecture et sens incertains, non repris.

## 7. Vérification (étape 6)

- Toutes les diapositives de contenu reprises (tableau du § 2).
- Formules recalculées : longueurs d'antenne, TF du sinus (signe), Parseval (cohérence avec $A_x = 2|X|$), produit de cosinus.
- Rendu Quarto 1.10.19 (projet minimal) sans avertissement ; références croisées résolues ; formules des 4 chapitres compilées avec MathJax 3.2.2 (1094 formules, 0 erreur).

## 8. Validation (étape 7)

Validé le 29 octobre 2026 sur délégation d'Armand ; statut `valide`. Flashcards non générées (hors du périmètre demandé).
