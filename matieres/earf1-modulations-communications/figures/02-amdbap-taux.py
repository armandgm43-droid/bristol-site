"""EARF1 ch. 2 — AM double bande avec porteuse : influence du taux de modulation k.
D'après le support [mod-ana, p. 27], recalculée (fp = 20 fm)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
ROUGE, GRIS = "#B23A3A", "#7E889B"
fm, fp, A = 1.0, 20.0, 1.0
t = np.linspace(0, 2, 6000)
fig, ax = plt.subplots(1, 3, figsize=(9.5, 3.2), sharey=True)
for a, k, titre in zip(ax, [0.5, 1.0, 1.5], ["$k < 1$ ($k = 0{,}5$)", "$k = 1$", "$k > 1$ ($k = 1{,}5$) : surmodulation"]):
    env = A * (1 + k * np.cos(2 * np.pi * fm * t))
    a.plot(t, env * np.cos(2 * np.pi * fp * t), color=ROUGE, lw=0.7)
    a.plot(t, env, color=GRIS, ls="--", lw=1.1); a.plot(t, -env, color=GRIS, ls="--", lw=1.1)
    a.set_title(titre, fontsize=9.5); a.set_xlabel("$t\\,f_m$")
    a.axhline(0, color="black", lw=0.5); a.spines[["top", "right"]].set_visible(False)
    a.set_yticks([-2.5, -1.5, -0.5, 0, 0.5, 1.5, 2.5])
ax[0].set_ylabel("$s_{AMDBAP}(t)$ (en unités de $A$)")
ax[0].annotate("$S_{max}$", (0, 1.5), (0.35, 2.1), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.7))
ax[0].annotate("$S_{min}$", (0.5, 0.5), (0.75, 1.15), fontsize=8, arrowprops=dict(arrowstyle="->", lw=0.7))
fig.tight_layout(); fig.savefig("02-amdbap-taux.svg")
