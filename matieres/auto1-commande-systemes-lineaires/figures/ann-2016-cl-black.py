"""Partiel AU201 du 13 janvier 2017, question 2 : lieu de Black de la boucle ouverte
beta(jw) = K G0 / (1 + jw/w0) de la boucle élémentaire issue de la restructuration,
G0 = 10, w0 = 1 rad/s ; K n'est pas donné par le sujet : K = 10 (K G0 = 100) pour l'exemple.
Régénérer : python ann-2016-cl-black.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
G0, w0, K = 10.0, 1.0, 10.0
w = np.logspace(-3, 4, 3000)
b = K * G0 / (1 + 1j * w / w0)
wu = w0 * np.sqrt((K * G0) ** 2 - 1)
Mp = 180 - np.degrees(np.arctan(wu / w0))
fig, ax = plt.subplots(figsize=(6.0, 4.0))
ax.plot(np.degrees(np.angle(b)), 20 * np.log10(abs(b)), color="#2B4C9B", lw=1.6)
ax.plot([-180], [0], "x", color="k", ms=8, mew=1.5)
ax.annotate("point critique", (-180, 0), (-172, 12), fontsize=9)
ax.axhline(0, color="k", lw=0.6); ax.axvline(-90, color="#7E889B", ls="--", lw=0.9)
ax.annotate(f"$\\omega_u \\approx K G_0\\,\\omega_0$ : $M_\\varphi = {Mp:.1f}°$", (-90 + 0.6, 0), (-150, -22),
            fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.6))
ax.annotate("$\\omega \\to 0$ : $20\\log(K G_0) = 40$ dB", (0, 40), (-75, 46), fontsize=9,
            arrowprops=dict(arrowstyle="->", lw=0.6))
ax.text(-88, -35, "asymptote $-90°$\n($\\omega \\to \\infty$)", color="#7E889B", fontsize=9)
ax.set_xlim(-190, 5); ax.set_ylim(-45, 55)
ax.set_xlabel("arg $\\beta(j\\omega)$ (°)"); ax.set_ylabel("$|\\beta(j\\omega)|$ (dB)")
ax.grid(alpha=0.25); ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
