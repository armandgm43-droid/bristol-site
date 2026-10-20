# TSIG1 ch. 1 — Échantillonnage et signal discret : rapport d'analyse

> 20 octobre 2026. Document de travail (`.md`, non rendu). Étapes 2 à 5 faites dans la même session (accord d'Armand : rédaction et vérification le jour même, flashcards après sa relecture).

## 1. Sources

| id | Fichier | Nature | Partie utilisée |
|---|---|---|---|
| `notes` | `sources/tsig1/notes/date-inconnue.pdf` (photos `date-inconnue/feuillet-NN-recto/verso.jpg`) | personnelle | f. 1 r° à f. 3 v° |
| `notes-2023-ch01` | `sources/tsig1/notes/2023-cours-ch01-generalites-signaux-systemes.pdf` | externe (ancien élève, promotion 2023) | p. 1-7 |
| `fiche-rappels` | `sources/tsig1/notes/externe-fiche-rappels-traitement-signal.pdf` | externe (fiche de synthèse d'un tiers) | p. 1-2 |
| `illustrations` | `sources/tsig1/support/illustrations-berthoumieu.pdf` (version « TS201 ») | officielle | p. 1-2 |

Aucun support de cours rédigé. Les notes d'Armand sont la source principale ; le plan des chapitres suit leur découpage (choix d'Armand, 20 octobre 2026), et non le plan de l'inventaire (notes 2023).

Correspondance feuillets / photos et numéros écrits par Armand : voir `sources/tsig1/transcriptions/notes-2026.md`.

## 2. Contenu des notes repris

Contexte (chaîne CAN – algorithme – CNA) ; définition de l'échantillonnage ; Dirac et peigne ; $x_m = x_a\,\text{Ш}_{T_e}$ ; TFSD comme TF du signal échantillonné ; TF du peigne par série de Fourier ; périodisation du spectre ; Shannon-Nyquist et repliement ; débit $D = f_e B$ ; filtre de reconstruction idéal et calcul de $h_\mathrm{rec}$ ; signaux discrets (cosinus, échelon, impulsion, séquence finie) ; décomposition $x[n] = \sum_k x[k]\delta[n-k]$.

Tout le contenu est en bloc *Notes de cours* ; les ajouts sont en *Complément*.

## 3. Blocs *À vérifier* (questions bloquantes)

| id | Question |
|---|---|
| `av-indices-entiers-naturels` | $n \in \mathbb{N}$ écrit, alors que $x[-1]$ apparaît : $n \in \mathbb{Z}$ ? |

## 4. Corrections de forme (sans bloc, § 5.3)

- f. 2 v° : premier calcul de $h_\mathrm{rec}$ (signe de l'exponentielle, facteur $T_e$ absent) repris correctement au f. 3 r° : seule la seconde version est reproduite (signalé en *Complément*).
- f. 3 v° : $\delta(nT_e)$ etc. écrit pour l'impulsion discrète : noté $\delta[n]$ (signalé en *Complément*).

## 5. Choix appliqués par défaut (§ 14)

- Peigne noté $\text{Ш}_{T_e}$ (notes : lettre proche de $s_{T_e}$), comme TS227 ; sa TF notée $S_{T_e}(f)$ comme dans les notes.
- Convention $\sinc(x) = \sin(\pi x)/(\pi x)$ (celle des notes) ; TF en $e^{-j2\pi ft}$.
- Compléments : fréquence de Nyquist, débit numérique (1,536 Mbit/s), formule d'interpolation de Shannon, cas limite $f_e = 2f_0$ pour une sinusoïde (inégalité stricte), ordres de grandeur audio.
- Figures (matplotlib, `figures/01-*.py`) : périodisation (triangle, $f_{\max} = 1$, $f_e = 3$), repliement ($f_e = 1{,}4$), reconstruction par sinus cardinaux (signal d'exemple arbitraire), signaux discrets.

## 6. Sources externes

Intégrées le 20 octobre 2026 à partir de `externes-ch1-3.md` (lecture de toutes les pages). Aucun exercice des TD 1 à 3 ne relève de l'échantillonnage : pas de section « Exercices du TD ».

**Notes 2023 et fiche de rappels** (7 blocs *Notes externes*, dont 1 remplacement) :

- [notes-2023-ch01, p. 1] : paramètres des convertisseurs ($T_e$, $B$ « support binaire »), remarque sur le choix de $T_e$ ; `sec-contexte-traitement-numerique`.
- [fiche-rappels, p. 1] : propriété de modulation de la TF ; `sec-interpretation-frequentielle-echantillonnage`.
- [notes-2023-ch01, p. 4] [fiche-rappels, p. 1] : vocabulaire « intégrité », « recouvrement spectral » ; `sec-shannon`.
- [notes-2023-ch01, p. 5] : domaine $[-f_e/2, f_e/2]$, BF/HF, gain $C = T_e$ par identification ; `sec-reconstruction`.
- [notes-2023-ch01, p. 6] [fiche-rappels, p. 2] : démonstration de la formule de reconstruction. **Remplacement** : le bloc *Complément* qui portait `eq-interpolation-shannon` devient un bloc *Notes externes* (label conservé), suivi d'un *Complément* sur les conventions du sinus cardinal (`sinCard` de la fiche).
- [notes-2023-ch01, p. 7] : cas limite $T_e = T_0/2$ ; forme vectorielle du signal ; `sec-signaux-discrets`.
- Pages 2, 3 et 6 (reste) : doublons de nos notes (confirment la lettre « $s_{T_e}$ » du peigne).

**Support d'illustrations (officiel)** [illustrations, p. 1-2] : exemples d'ouverture (parole, signal périodique, égaliseur, MP3), en texte normal dans `sec-contexte-traitement-numerique`. La phrase d'introduction du chapitre mentionne désormais ce support et les notes 2023 (sans retirer l'information d'origine).

**AV existant** : `av-indices-entiers-naturels` reste ouvert ; ligne **Autres sources** ajoutée (les notes 2023 écrivent aussi $n \in \mathbb{N}$ ; toutes les sommes vont de $-\infty$ à $+\infty$).

**Erreurs des sources externes non reprises** : aucune dans ce chapitre (la condition de Shannon de la fiche, lue « $F_e / \frac{F_e}{2} \geq f_{\max}$ », n'est pas reprise).

**Passages illisibles ou douteux** :

- [notes-2023-ch01, p. 7] : « si $T_e = \frac{T_0}{2}$, $x(\ ) = 0$ » : argument vide dans la source, reproduit tel quel.
- [notes-2023-ch01, p. 7] : annotation en marge du vecteur, lue « $x(n)$ / $m(nT_0)$ » (lettre et indice douteux) ; non reprise.
- [notes-2023-ch01, p. 1] : « B : support binaire » : lecture sûre, sens non précisé (interprété « nombre de bits » d'après nos notes).
- [fiche-rappels, p. 1] : condition de Shannon encadrée, premier « $F_e$ / » peut-être barré ; non reprise.
- [illustrations, p. 1] : graduations des spectres trop petites pour être lues.
- Fiche de rappels : texte de l'autre face visible par transparence (p. 1-3), ignoré.

## 7. Vérification (étape 6, 20 octobre 2026)

- (a) 38 blocs de formules relus et recalculés (peigne, périodisation, $h_\mathrm{rec} = \sinc(f_e t)$, débit 1,536 Mbit/s) ; AV et notes 2023 (p. 1, 5, 7) contrôlés sur la photo a et les pages PNG.
- (b) Aucune correction.
- (c) AV `av-indices-entiers-naturels` : citation fidèle, gardé tel quel.
- (d) Rien de nouveau. AV ouverts : 1.

Détail : `verification.md`.
