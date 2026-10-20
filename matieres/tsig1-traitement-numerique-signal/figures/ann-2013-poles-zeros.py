"""Examen de mars 2014, ex. 2 a) : zéros en -1 et +1, pôles en 0,2 et 0,5 ± 0,5j (données du sujet).
Régénérer : python ann-2013-poles-zeros.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
fig, a = plt.subplots(figsize=(3.8, 3.6))
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color="#7E889B", ls="--", lw=0.9)
poles = [0.2, 0.5 + 0.5j, 0.5 - 0.5j]
a.plot(np.real(poles), np.imag(poles), "x", color="#BF6014", ms=9, mew=2)
a.plot([-1, 1], [0, 0], "o", mfc="white", mec="#2B4C9B", ms=8, mew=1.6)
a.text(0.2, -0.2, "0,2", ha="center")
a.text(0.6, 0.55, "0,5 + 0,5j"); a.text(0.6, -0.65, "0,5 − 0,5j")
a.text(-1.05, 0.12, "−1", ha="right"); a.text(1.05, 0.12, "1")
a.plot([0], [0], "x", color="none")
a.annotate("", (np.cos(np.pi / 4), np.sin(np.pi / 4)), (0, 0), arrowprops=dict(arrowstyle="-", color="#7E889B", lw=0.6, ls=":"))
a.text(0.36, 0.14, r"$\pi/4$", fontsize=9, color="#7E889B")
a.set_aspect("equal"); a.set_xlim(-1.4, 1.6); a.set_ylim(-1.3, 1.3)
a.axhline(0, color="k", lw=0.4); a.axvline(0, color="k", lw=0.4)
a.set_xlabel(r"$\mathrm{Re}(z)$"); a.set_ylabel(r"$\mathrm{Im}(z)$")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
