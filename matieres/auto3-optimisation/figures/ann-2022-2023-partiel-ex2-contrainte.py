"""Épreuve du 05/05/2022 (fichiers 2022-2023), ex. 2 : courbes iso-critères de
J(x, y) = 3x^2 - 6x + 8y^2 - 48y + 123, contrainte g = x + y - 10 >= 0 (domaine grisé),
optimum non contraint (1, 3) et optimum contraint (59/11, 51/11). Figure calculée.
Régénérer : python ann-2022-2023-partiel-ex2-contrainte.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none",
                     "contour.negative_linestyle": "solid"})
fig, a = plt.subplots(figsize=(5.6, 4.6))
x, y = np.meshgrid(np.linspace(-2, 9, 400), np.linspace(-1, 9, 400))
J = 3 * x ** 2 - 6 * x + 8 * y ** 2 - 48 * y + 123
Jc = 1392 / 11
cs = a.contour(x, y, J, levels=[50, 60, 80, 100, Jc, 160, 200], colors="k", linewidths=0.6)
a.clabel(cs, fmt=lambda v: f"{v:.0f}" if abs(v - Jc) > 1e-6 else "126,5", fontsize=8)
xs = np.array([-2, 9])
a.fill_between(xs, 10 - xs, 9, color="#2B4C9B", alpha=0.18, lw=0)
a.plot(xs, 10 - xs, color="#2B4C9B", lw=1.6, label=r"$x + y - 10 = 0$")
a.plot([1], [3], "+", color="k", ms=10, mew=1.5)
a.annotate("optimum non contraint\n(1, 3), $J = 48$", (1, 3), (-1.8, 7.6), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
xc, yc = 59 / 11, 51 / 11
a.plot([xc], [yc], "o", color="#BF6014", ms=7, zorder=5)
a.annotate("optimum contraint\n(59/11, 51/11), $J ≈ 126{,}5$", (xc, yc), (5.4, 6.8), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
a.text(6.3, 8.3, "domaine admissible\n$x + y \\geq 10$", fontsize=9, color="#2B4C9B")
a.set_aspect("equal"); a.set_xlim(-2, 9); a.set_ylim(-1, 9)
a.set_xlabel(r"$x$"); a.set_ylabel(r"$y$")
a.legend(loc="lower right", fontsize=8)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
