"""Épreuve du 19/05/2022 (fichiers 2021-2022), ex. 3 : courbes iso-critères de
J(x) = -(x1 - 2)^2/4 - (x2 - 1)^2, frontières g1 = 0 (droite) et g2 = 0 (cercle unité),
domaine admissible (grisé), points KKT. Figure calculée (données du sujet).
Régénérer : python ann-2021-2022-partiel-ex3-domaine.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none",
                     "contour.negative_linestyle": "solid"})
fig, a = plt.subplots(figsize=(6.0, 4.6))
x1, x2 = np.meshgrid(np.linspace(-3, 6, 400), np.linspace(-3, 5, 400))
J = -0.25 * (x1 - 2) ** 2 - (x2 - 1) ** 2
cs = a.contour(x1, x2, J, levels=[-16, -12, -8, -4, -2, -1.25, -1, -0.5], colors="k", linewidths=0.6)
a.clabel(cs, fmt=lambda v: f"{v:g}".replace(".", ",").replace("-", "−"), fontsize=8)
# Domaine admissible : disque unité ∩ {x1 + x2 >= 1}
t = np.linspace(0, np.pi / 2, 200)
a.fill(np.r_[np.cos(t)], np.r_[np.sin(t)], color="#2B4C9B", alpha=0.25, lw=0)
th = np.linspace(0, 2 * np.pi, 400)
a.plot(np.cos(th), np.sin(th), color="#2B4C9B", lw=1.6, label=r"$g_2(x) = 0$")
xl = np.array([-3, 4])
a.plot(xl, 1 - xl, color="#BF6014", lw=1.6, label=r"$g_1(x) = 0$")
a.plot([1], [0], "o", color="#BF6014", ms=7, zorder=5)
a.annotate("(1, 0) : minimum global\n$J = -1{,}25$", (1, 0), (1.6, -1.6), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
a.plot([0], [1], "o", color="#2B4C9B", ms=7, zorder=5)
a.annotate("(0, 1) : minimum local\n$J = -1$", (0, 1), (-2.8, 2.3), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
a.plot([0.4], [0.6], "o", mfc="white", mec="k", ms=6, zorder=5)
a.annotate("(0,4 ; 0,6) : point KKT\nnon minimum, $J = -0{,}8$", (0.4, 0.6), (-2.8, -2.3), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7, color="#7E889B"))
a.plot([2], [1], "+", color="k", ms=10, mew=1.5)
a.annotate("maximum non contraint (2, 1), $J = 0$", (2, 1), (2.3, 3.6), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
a.set_aspect("equal"); a.set_xlim(-3, 6); a.set_ylim(-3, 5)
a.set_xlabel(r"$x_1$"); a.set_ylabel(r"$x_2$")
a.legend(loc="lower right", fontsize=8)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
