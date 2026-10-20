"""TSIG1, partiel 2017-2018, exercice 4 : S(z) = 1 / ((1 - z^-1/2)(1 - z^-1/4)) = z^2 / ((z - 1/2)(z - 1/4)).
Pôles 1/2 et 1/4, zéro double en 0 ; h[n] = [2 (1/2)^n - (1/4)^n] u[n]. Figure calculée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
fig, (a, b) = plt.subplots(1, 2, figsize=(8, 3), gridspec_kw={"width_ratios": [1, 1.6]})
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color="#7E889B", lw=0.8, ls="--")
a.plot([0.5, 0.25], [0, 0], "x", color="#BF6014", ms=9, mew=2)
a.plot([0], [0], "o", mfc="none", mec="#2B4C9B", ms=7, mew=1.5)
a.text(-0.2, 0.12, "(2)", fontsize=8, color="#2B4C9B")
a.text(0.5, -0.28, r"$\frac{1}{2}$", ha="center"); a.text(0.25, -0.28, r"$\frac{1}{4}$", ha="center")
a.set_aspect("equal"); a.set_xlim(-1.3, 1.3); a.set_ylim(-1.3, 1.3)
a.axhline(0, color="k", lw=0.4); a.axvline(0, color="k", lw=0.4)
a.set_xlabel(r"$\mathrm{Re}(z)$"); a.set_ylabel(r"$\mathrm{Im}(z)$")
n = np.arange(0, 11)
h = 2 * 0.5 ** n - 0.25 ** n
# contrôle par la récurrence y(n) = 3/4 y(n-1) - 1/8 y(n-2) + x(n)
y = np.zeros(len(n))
for k in n:
    y[k] = (k == 0) + 0.75 * (y[k - 1] if k >= 1 else 0) - 0.125 * (y[k - 2] if k >= 2 else 0)
assert np.allclose(y, h)
b.stem(n, h, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
b.set_xlabel("$n$"); b.set_ylabel("$h(n)$"); b.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("ann-2017-poles-zeros.svg")
