"""EANA1, partiel 2013-2014, ex. III q. 2 a — LM555 en monostable. Reconstruite (Claude) :
Vcc = 15 V, e(t) = 12 V sauf une impulsion à 0 V de durée te << RC ; temps en unités de RC.
Durée de l'impulsion de sortie : RC ln 3 ; décharge de C supposée instantanée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

Vcc, te, Tm = 15.0, 0.08, np.log(3)
t = np.linspace(-0.4, 2.0, 2401)
e = np.where((t >= 0) & (t < te), 0.0, 12.0)
vc = np.where((t >= 0) & (t < Tm), Vcc * (1 - np.exp(-np.clip(t, 0, None))), 0.0)
s = np.where((t >= 0) & (t < Tm), Vcc, 0.0)
fig, axs = plt.subplots(3, 1, figsize=(7, 5.6), sharex=True)
for ax, y, nom in ((axs[0], e, "$e(t)$ (V)"), (axs[1], vc, "$V_C$ (V)"), (axs[2], s, "$s(t)$ (V)")):
    ax.plot(t, y, color="#2B4C9B", lw=1.5)
    ax.axhline(0, color="k", lw=0.5); ax.set_ylabel(nom)
    ax.axvline(0, color="#7E889B", ls=":", lw=0.7); ax.axvline(Tm, color="#7E889B", ls=":", lw=0.7)
    ax.spines[["top", "right"]].set_visible(False)
axs[0].axhline(5, color="#BF6014", ls="--", lw=0.8); axs[0].text(2.02, 5, "$V_{cc}/3$", color="#BF6014", va="center")
axs[0].set_yticks([0, 5, 12])
axs[1].axhline(10, color="#BF6014", ls="--", lw=0.8); axs[1].text(2.02, 10, "$2V_{cc}/3$", color="#BF6014", va="center")
axs[1].plot(t, Vcc * (1 - np.exp(-np.clip(t, 0, None))) * (t >= Tm), color="#7E889B", ls="--", lw=0.8)
axs[1].set_yticks([0, 10, 15])
axs[2].set_yticks([0, 15])
axs[2].set_xticks([0, te, Tm]); axs[2].set_xticklabels(["0", "$t_e$", r"$RC\,\ln 3$"])
axs[2].set_xlabel("Temps (unité : $RC$) ; pointillés gris : charge que $V_C$ suivrait sans la décharge")
fig.tight_layout()
fig.savefig("ann1314-555-monostable.svg")
