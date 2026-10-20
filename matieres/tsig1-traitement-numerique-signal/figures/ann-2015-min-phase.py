"""TSIG1, partiel 2015-2016, exercice 4 : H(z) = (2z+3)(4z-1)/((z+0,4)(z-0,6)) et le filtre
à minimum de phase G(z) = (3z+2)(4z-1)/((z+0,4)(z-0,6)) (zéro -3/2 remplacé par -2/3),
de même module. Figure calculée. Régénérer : python ann-2015-min-phase.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
w = np.linspace(0, np.pi, 200); e = np.exp(1j * w)
assert np.allclose(np.abs((2 * e + 3) * (4 * e - 1)), np.abs((3 * e + 2) * (4 * e - 1)))
poles = [-0.4, 0.6]
th = np.linspace(0, 2 * np.pi, 400)
fig, axs = plt.subplots(1, 2, figsize=(8, 3.2))
for ax, titre, zeros in ((axs[0], "$H(z)$", [-1.5, 0.25]), (axs[1], "$G(z)$ (minimum de phase)", [-2 / 3, 0.25])):
    ax.plot(np.cos(th), np.sin(th), color="#7E889B", lw=0.8, ls="--")
    ax.plot(poles, [0, 0], "x", color="#BF6014", ms=9, mew=2)
    ax.plot(zeros, [0, 0], "o", mfc="none", mec="#2B4C9B", ms=7, mew=1.5)
    for p in poles:
        ax.annotate(f"{p:g}".replace(".", ","), (p, 0), xytext=(0, 9), textcoords="offset points", ha="center", fontsize=8, color="#BF6014")
    for q, t in zip(zeros, ("-3/2" if zeros[0] == -1.5 else "-2/3", "1/4")):
        ax.annotate(t, (q, 0), xytext=(0, -16), textcoords="offset points", ha="center", fontsize=8, color="#2B4C9B")
    ax.set_aspect("equal"); ax.set_xlim(-1.8, 1.4); ax.set_ylim(-1.3, 1.3)
    ax.axhline(0, color="k", lw=0.4); ax.axvline(0, color="k", lw=0.4)
    ax.set_title(titre); ax.set_xlabel(r"$\mathrm{Re}(z)$"); ax.set_ylabel(r"$\mathrm{Im}(z)$")
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
