"""TSIG1 ch. 4 — Cellule d'ordre 1 : zone de convergence |z| > |alpha| et h[n] = alpha^n u[n].
D'après les notes de cours [notes, f. 10 v°], redessinée ; réponses impulsionnelles ajoutées (alpha = ±0,8)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
al = 0.8
fig, ax = plt.subplots(1, 3, figsize=(9, 2.9), gridspec_kw={"width_ratios": [1, 1.2, 1.2]})
a = ax[0]
th = np.linspace(0, 2 * np.pi, 400)
a.add_patch(plt.Rectangle((-1.6, -1.6), 3.2, 3.2, color="#2B4C9B", alpha=0.12, lw=0))
a.add_patch(plt.Circle((0, 0), al, color="white", lw=0))
a.plot(np.cos(th), np.sin(th), color="k", lw=0.8, label="cercle unité")
a.plot(al * np.cos(th), al * np.sin(th), color="#2B4C9B", ls="--", lw=0.8)
a.plot([al], [0], "x", color="#BF6014", ms=8, mew=2)
a.plot([0], [0], "o", mfc="none", mec="k", ms=6)
a.text(al, 0.12, r"$\alpha$", ha="center")
a.text(0, -1.45, r"zone $|z| > |\alpha|$", ha="center", fontsize=8)
a.set_aspect("equal"); a.set_xlim(-1.6, 1.6); a.set_ylim(-1.6, 1.6)
a.axhline(0, color="k", lw=0.4); a.axvline(0, color="k", lw=0.4)
a.set_xlabel(r"$\mathrm{Re}(z)$"); a.set_ylabel(r"$\mathrm{Im}(z)$")
n = np.arange(0, 16)
for b, alpha in zip(ax[1:], (al, -al)):
    b.stem(n, alpha ** n, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
    b.set_title(rf"$h[n] = ({alpha:+.1f})^n\,u[n]$".replace(".", "{,}"), fontsize=10)
    b.set_xlabel("$n$"); b.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("04-cellule-ordre-1.svg")
