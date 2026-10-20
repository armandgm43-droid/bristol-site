"""TSIG1 ch. 4 — Exemple y[n] + 1/4 y[n-1] - 3/8 y[n-2] = x[n] : pôles 1/2 et -3/4, zéro double en 0,
h[n] = [2/5 (1/2)^n + 3/5 (-3/4)^n] u[n]. D'après les notes de cours [notes, f. 10 v°], redessinée ; h[n] calculée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
fig, (a, b) = plt.subplots(1, 2, figsize=(8, 3), gridspec_kw={"width_ratios": [1, 1.6]})
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color="k", lw=0.8)
a.plot([0.5, -0.75], [0, 0], "x", color="#BF6014", ms=9, mew=2)
a.plot([0], [0], "o", mfc="none", mec="#2B4C9B", ms=7, mew=1.5)
a.text(0.04, 0.12, "(2)", fontsize=8, color="#2B4C9B")
a.text(0.5, -0.25, r"$\frac{1}{2}$", ha="center"); a.text(-0.75, -0.25, r"$-\frac{3}{4}$", ha="center")
a.set_aspect("equal"); a.set_xlim(-1.3, 1.3); a.set_ylim(-1.3, 1.3)
a.axhline(0, color="k", lw=0.4); a.axvline(0, color="k", lw=0.4)
a.set_xlabel(r"$\mathrm{Re}(z)$"); a.set_ylabel(r"$\mathrm{Im}(z)$")
n = np.arange(0, 13)
h = 0.4 * 0.5 ** n + 0.6 * (-0.75) ** n
# contrôle par récurrence
y = np.zeros(13)
for k in range(13):
    y[k] = (k == 0) - 0.25 * (y[k - 1] if k >= 1 else 0) + 0.375 * (y[k - 2] if k >= 2 else 0)
assert np.allclose(y, h)
b.stem(n, h, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
b.set_xlabel("$n$"); b.set_ylabel("$h[n]$"); b.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("04-exemple-poles-zeros.svg")
