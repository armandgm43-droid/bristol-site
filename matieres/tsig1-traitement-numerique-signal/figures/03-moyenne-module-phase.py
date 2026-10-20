"""TSIG1 ch. 3 — Moyenne de deux échantillons : |H(f)| = |cos(pi f)|, Arg H(f) = -pi f (fréquence normalisée).
D'après les notes de cours [notes, f. 8 r°], redessinée ; gabarit idéal ajouté en pointillés gris (#7E889B)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
f = np.linspace(-0.5, 0.5, 1001)
H = np.exp(-1j * np.pi * f) * np.cos(np.pi * f)
fig, (a, b) = plt.subplots(1, 2, figsize=(8, 2.8))
a.plot(f, np.abs(H), color="#2B4C9B", label="$|H(f)|$")
a.plot([-0.5, -0.25, -0.25, 0.25, 0.25, 0.5], [0, 0, 1, 1, 0, 0], color="#7E889B", ls="--", label="passe-bas idéal")
a.set_xlabel("Fréquence normalisée $f$"); a.set_ylabel("Module")
a.legend(frameon=False, fontsize=8, loc="lower center")
b.plot(f, np.angle(H), color="#2B4C9B")
b.set_yticks([-np.pi / 2, 0, np.pi / 2]); b.set_yticklabels([r"$-\pi/2$", "0", r"$\pi/2$"])
b.set_xlabel("Fréquence normalisée $f$"); b.set_ylabel("Phase (rad)")
for ax in (a, b):
    ax.set_xticks([-0.5, -0.25, 0, 0.25, 0.5]); ax.axhline(0, color="k", lw=0.5)
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-moyenne-module-phase.svg")
