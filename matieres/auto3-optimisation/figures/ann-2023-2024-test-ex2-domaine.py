"""Épreuve du 20/12/2023, ex. 2 : courbes iso-critères de
J(x, y) = -8x^2 - 32x - 2y^2 + 4y - 29 (mêmes niveaux que la figure du sujet),
droites g1 = 0 et g2 = 0, domaine admissible (grisé), optimum contraint (-2, -1).
Figure calculée (données du sujet).
Régénérer : python ann-2023-2024-test-ex2-domaine.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none",
                     "contour.negative_linestyle": "solid"})
fig, a = plt.subplots(figsize=(5.4, 4.6))
x, y = np.meshgrid(np.linspace(-4, 0, 400), np.linspace(-2, 3, 400))
J = -8 * x ** 2 - 32 * x - 2 * y ** 2 + 4 * y - 29
cs = a.contour(x, y, J, levels=[-30, -25, -20, -15, -10, -5, -3, 0, 2, 4], colors="k", linewidths=0.6)
a.clabel(cs, fmt=lambda v: f"{v:g}".replace("-", "−"), fontsize=8)
xs = np.linspace(-4, 0, 401)
haut = np.minimum(-2 * xs - 5, 2 * xs + 3)
a.fill_between(xs, -2, haut, where=haut > -2, color="#2B4C9B", alpha=0.22, lw=0)
a.plot(xs, -2 * xs - 5, color="#BF6014", lw=1.6, label=r"$g_1 = y + 2x + 5 = 0$")
a.plot(xs, 2 * xs + 3, color="#2B4C9B", lw=1.6, label=r"$g_2 = y - 2x - 3 = 0$")
a.plot([-2], [1], "+", color="k", ms=10, mew=1.5)
a.annotate("maximum non contraint\n(−2, 1), $J = 5$", (-2, 1), (-1.3, 2.3), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
a.plot([-2], [-1], "o", color="#BF6014", ms=7, zorder=5)
a.annotate("optimum contraint\n(−2, −1), $J = -3$", (-2, -1), (-1.2, -1.75), fontsize=9,
           arrowprops=dict(arrowstyle="->", lw=0.7))
for px in (-2.5, -1.5):
    a.plot([px], [0], "o", mfc="white", mec="#7E889B", ms=6)
a.text(-3.95, -1.85, "domaine admissible", fontsize=9, color="#2B4C9B")
a.set_xlim(-4, 0); a.set_ylim(-2, 3)
a.set_xlabel(r"$x$"); a.set_ylabel(r"$y$")
a.legend(loc="upper left", fontsize=8)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
