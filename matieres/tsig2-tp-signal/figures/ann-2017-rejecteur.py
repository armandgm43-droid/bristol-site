"""TSIG2, partiels 2016-2017 et 2017-2018 — Filtre RIF réjecteur
H(z) = 1 - 2 r cos(2 pi f0/fe) z^-1 + r^2 z^-2 pour f0/fe = 0,3 (valeur du partiel
2017-2018) et r = 0,9 ; 0,95 ; 1 : module et phase. Figure calculée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
th = 2 * np.pi * 0.3
fn = np.linspace(0, 0.5, 2001); e = np.exp(-2j * np.pi * fn)
fig, ax = plt.subplots(1, 2, figsize=(10, 3.3))
for r, c in [(0.9, "#9DB0D8"), (0.95, "#5A78BE"), (1.0, "#1F3470")]:
    H = 1 - 2 * r * np.cos(th) * e + r**2 * e**2
    ax[0].plot(fn, 20 * np.log10(np.abs(H) + 1e-6), color=c, label=f"$r$ = {r:g}".replace(".", ","))
    ax[1].plot(fn, np.angle(H), color=c)
ax[0].set_ylim(-40, 12); ax[0].legend(fontsize=8)
ax[0].set_ylabel(r"$20\log_{10}|H(f)|$ (dB)")
ax[1].set_ylabel(r"$\arg H(f)$ (rad)")
for a in ax:
    a.axvline(0.3, color="#7E889B", ls=":", lw=0.8)
    a.set_xlabel("Fréquence normalisée $f/f_e$")
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("ann-2017-rejecteur.svg")
