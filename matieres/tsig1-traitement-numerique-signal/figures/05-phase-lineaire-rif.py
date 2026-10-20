"""TSIG1 ch. 5 — Phase linéaire : h~[n] symétrique non causale, puis h[n] = h~[n - D] causale.
D'après les notes de cours [notes, f. 12 r°], redessinée. RIF : sinus cardinal tronqué, longueur 9, D = 4."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
D = 4
k = np.arange(-D, D + 1)
ht = np.sinc(k / 2.5)
fig, (a, b) = plt.subplots(1, 2, figsize=(8, 2.6), sharey=True)
a.stem(k, ht, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
a.set_title(r"$\tilde h[n]$ : phase nulle, non causale", fontsize=10)
b.stem(k + D, ht, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
b.set_title(r"$h[n] = \tilde h[n - D]$ : causale", fontsize=10)
for ax in (a, b):
    ax.axvline(0, color="k", lw=0.5); ax.set_xlabel("$n$"); ax.set_xlim(-5, 9)
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("05-phase-lineaire-rif.svg")
