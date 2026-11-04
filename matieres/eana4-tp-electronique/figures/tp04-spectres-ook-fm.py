"""EANA4 TP 4/5 — Spectres théoriques (Complément).
En haut : OOK, porteuse 455 kHz modulée par un carré 0/4 V à 1 kHz, rapports cycliques 50, 20 et 10 %
(raie de rang k : |sinc(k·α)| relativement à la porteuse, sinc(x) = sin(πx)/(πx)).
En bas : FM, FM = 1 kHz, m = 0,4 ; 2,405 ; 10 (raie de rang n : |Jn(m)| relativement à la porteuse non modulée).
Valeurs des réglages : [poly, p. 46 et p. 51-52]."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.special import jv
plt.rcParams.update({"font.family": "sans-serif", "font.size": 9.5, "svg.fonttype": "none"})
BLEU, GRIS = "#2B4C9B", "#7E889B"
PLANCHER = -50


def barres(a, k, db, couleur):
    db = np.maximum(db, PLANCHER)
    a.vlines(k, PLANCHER, db, color=couleur, lw=2)
    a.set_ylim(PLANCHER, 3)
    a.grid(alpha=0.3)


fig, axes = plt.subplots(2, 3, figsize=(9.6, 5.2), sharey=True)
k = np.arange(-25, 26)
for a, alpha in zip(axes[0], [0.5, 0.2, 0.1]):
    amp = np.abs(np.sinc(k * alpha)) * alpha / 0.5      # porteuse à 50 % prise comme référence 0 dB
    with np.errstate(divide="ignore"):
        db = 20 * np.log10(amp)
    barres(a, k, db, BLEU)
    a.set_title(f"OOK, rapport cyclique {int(alpha * 100)} %")
    a.set_xlabel("f − 455 kHz (kHz)")
axes[0][0].set_ylabel("niveau (dB)\nréf. : porteuse à 50 %")

n = np.arange(-16, 17)
for a, m in zip(axes[1], [0.4, 2.405, 10]):
    with np.errstate(divide="ignore"):
        db = 20 * np.log10(np.abs(jv(np.abs(n), m)))
    barres(a, n, db, BLEU)
    carson = (m + 1)          # demi-bande de Carson en kHz (ΔF + FM)
    a.axvspan(-carson, carson, color=GRIS, alpha=0.15, lw=0)
    a.set_title(f"FM, m = {str(m).replace('.', ',')} (Carson grisé)")
    a.set_xlabel("f − 455 kHz (kHz)")
axes[1][0].set_ylabel("niveau (dBc)\nréf. : porteuse non modulée")
fig.tight_layout()
fig.savefig("tp04-spectres-ook-fm.svg")
