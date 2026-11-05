"""EAEP1, partiel 2017-2018, q. 16 — boost, plan de sortie réduit pour alpha = 0,5.
Reconstruite (Claude) : y = US/UE, x = L f IS / UE ; conduction discontinue y = 1 + alpha^2/(2x)
pour x < alpha(1-alpha)/2, conduction continue y = 1/(1-alpha) au-delà (en pointillés gris)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

a = 0.5
xc = a * (1 - a) / 2
x = np.linspace(0.01, xc, 400)
fig, ax = plt.subplots(figsize=(6.5, 3.8))
ax.plot(x, 1 + a**2 / (2 * x), color="#2B4C9B", label="conduction discontinue")
ax.plot([xc, 0.25], [1 / (1 - a)] * 2, color="#7E889B", ls="--", label="conduction continue")
ax.plot([xc], [1 / (1 - a)], "o", color="#BF6014")
ax.annotate("conduction critique\n$x_c = 0{,}125$ ($I_S \\approx 94$ mA)", (xc, 2), (0.15, 4),
            arrowprops=dict(arrowstyle="->", color="#BF6014"))
ax.set_xlim(0, 0.25); ax.set_ylim(0, 8)
ax.set_xlabel("$x = L f I_S / U_E$"); ax.set_ylabel("$y = U_S / U_E$")
ax.legend(frameon=False, loc="upper right")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("ann1718-plan-sortie.svg")
