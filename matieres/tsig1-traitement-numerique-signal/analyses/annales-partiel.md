# TSIG1 — Analyse des annales (préparation du partiel)

> 19 octobre 2026. Document de travail (`.md`, non rendu par Quarto).
> Sources : `sources/tsig1/annales/` (6 sujets lus en entier : 2014-2015, 2015-2016, 2016-2017, 2017-2018, 2022-2023, 2025-2026).
> Partiel 2026-2027 annoncé par Armand : **jeudi 22 octobre 2026**. Le partiel 2025-2026 a eu lieu le 23/10/2025 : même place dans l'année.

## 1. Format constant

- Enseignant : Yannick Berthoumieu (TS201, devenu TSIG1).
- **1 h 20**, **sans document**, **calculatrice autorisée**.
- 5 à 6 exercices courts, 1,5 à 7 points chacun.
- Rappels fournis en fin de sujet : échelon $u[n]$, $\delta(n-k) \leftrightarrow z^{-k}$, $a^n u(n) \leftrightarrow \frac{1}{1-az^{-1}}$ ($|a|<1$), somme géométrique $\sum_{n=N_1}^{N_2}\alpha^n = \frac{\alpha^{N_1}-\alpha^{N_2+1}}{1-\alpha}$.

## 2. Thèmes par sujet

| Thème | 14-15 | 15-16 | 16-17 | 17-18 | 22-23 | 25-26 | Total |
|---|---|---|---|---|---|---|---|
| Équation aux différences → $H(z)$, pôles/zéros, RIF/RII, causalité, stabilité, $h(n)$ par TZ inverse | ex. 3 | ex. 4 | ex. 4 | ex. 4 | ex. 3 | ex. 3 | **6/6** |
| Convolution discrète (séquences finies ou $a^n u(n)$) | ex. 1, 2 | ex. 1 | ex. 2 | — | — | ex. 1 | **4/6** |
| Échantillonnage, repliement, ambiguïté, choix de $f_e$ | — | ex. 2 | ex. 1 | ex. 1 | ex. 1 | — | **4/6** |
| Phase minimale, passe-tout, phase linéaire | — | ex. 3, 4 | — | — | ex. 4 | ex. 4 | **3/6** |
| Question de cours : définition TFTD / TFD sur $N$ (ou $2N$) points | — | — | ex. 5 | — | ex. 6 | ex. 6 | **3/6** |
| Diagramme pôles/zéros → nature du filtre (passe-bas, passe-haut, passe-bande, réjection) ou classe | — | — | — | — | ex. 4 | ex. 5 | 2/6 (les 2 derniers) |
| Cascade de RIF | — | ex. 5 | ex. 3 | ex. 3 | — | — | 3/6 |
| Conception par placement de pôles/zéros (notch, passe-bande) | — | — | — | ex. 2 | ex. 6 | — | 2/6 |
| Réponse à une entrée sinusoïdale via $H(e^{j2\pi f})$ | (ex. 2) | — | — | — | — | ex. 2 | 2/6 |
| Propriétés de la TF des séquences (décalage, modulation, $x(-n)$, $x(2n)$, convolution) | — | — | — | — | ex. 2 | — | 1/6 |
| Propriétés d'un système (linéaire, invariant, causal) à partir de sa relation | ex. 1 | — | — | — | — | — | 1/6 |

## 3. Exercices repris à l'identique

- **« Filtre RII et cascade »** ($y(n)=\alpha y(n-1)+\beta w(n)$, $w(n)=\tfrac12 w(n-1)+x(n)$, identification avec $y(n)=-\tfrac18 y(n-2)+\tfrac34 y(n-1)+x(n)$) : **2016-2017, 2017-2018 et 2022-2023**. À savoir refaire sans hésiter.
- Question de cours sur la **définition de la TFD** : 2016-2017 ($2N$ points), 2022-2023, 2025-2026 (avec la TFTD).

## 4. Priorités de révision (déduites)

1. Transformée en $z$ : équation aux différences ↔ $H(z)$, pôles et zéros, région de convergence, causalité et stabilité (pôles dans le cercle unité pour un système causal), RIF/RII, $h(n)$ par décomposition en éléments simples.
2. Convolution discrète (calcul graphique ou par tableau ; séquences exponentielles avec la somme géométrique).
3. Échantillonnage : spectre périodisé, repliement, choix de $T$.
4. Phase minimale et passe-tout : zéros hors du cercle remplacés par leurs inverses conjugués ; $H = H_{\min} H_{pt}$.
5. Lecture d'un diagramme pôles/zéros (gain près des pôles, nul aux zéros sur le cercle).
6. Définitions TFTD et TFD à connaître par cœur.

## 5. Suite prévue

- Rédaction des chapitres utiles d'après `notes-2023` (en *Notes externes*) et le recueil de TD ; les notes d'Armand, attendues, passeront en *Notes de cours*.
- Corrigés des annales, en commençant par 2025-2026, 2022-2023 et l'exercice « RII et cascade ».
