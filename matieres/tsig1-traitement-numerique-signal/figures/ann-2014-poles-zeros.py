"""Partiel 2014-2015, ex. 3 q. 1 : H(z) = z(z - 1) / ((z - 1/2)(z + 3/4)) ; zéros 0 et 1, pôles 1/2 et -3/4.
Régénérer : python ann-2014-poles-zeros.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
fig, a = plt.subplots(figsize=(3.8, 3.6))
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color="#7E889B", ls="--", lw=0.9)
a.plot([0.5, -0.75], [0, 0], "x", color="#BF6014", ms=9, mew=2)
a.plot([0, 1], [0, 0], "o", mfc="white", mec="#2B4C9B", ms=8, mew=1.6)
a.text(0.5, -0.22, r"$\frac{1}{2}$", ha="center"); a.text(-0.75, -0.22, r"$-\frac{3}{4}$", ha="center")
a.text(0.06, 0.12, "0"); a.text(1.08, 0.12, "1")
a.set_aspect("equal"); a.set_xlim(-1.4, 1.4); a.set_ylim(-1.3, 1.3)
a.axhline(0, color="k", lw=0.4); a.axvline(0, color="k", lw=0.4)
a.set_xlabel(r"$\mathrm{Re}(z)$"); a.set_ylabel(r"$\mathrm{Im}(z)$")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
