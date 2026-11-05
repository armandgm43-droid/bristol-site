"""EANA1, partiel 2013-2014, ex. I q. 1 — caractéristique linéarisée de la diode.
Reconstruite (Claude) : VD = 0,6 V et RD = 50 Ω (données du sujet)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

VD, RD = 0.6, 50.0
v = np.linspace(-0.5, 1.2, 500)
i = np.where(v > VD, (v - VD) / RD, 0.0) * 1e3   # en mA
fig, ax = plt.subplots(figsize=(5.5, 3.6))
ax.plot(v, i, color="#2B4C9B", lw=2)
ax.axhline(0, color="k", lw=0.6); ax.axvline(0, color="k", lw=0.6)
ax.axvline(VD, color="#7E889B", ls=":", lw=0.8)
ax.annotate("pente $1/R_D$", xy=(1.0, (1.0 - VD) / RD * 1e3), xytext=(0.55, 9),
            arrowprops=dict(arrowstyle="->", color="#BF6014"), color="#BF6014")
ax.text(-0.45, 0.6, "bloquée : $I_D = 0$", color="#2B4C9B")
ax.text(-0.45, 6.0, "passante :\n$V = V_D + R_D I_D$", color="#2B4C9B")
ax.set_xticks([0, VD, 1.0]); ax.set_xticklabels(["0", "$V_D = 0{,}6$", "1"])
ax.set_xlabel("$V$ aux bornes de la diode (V)"); ax.set_ylabel("$I_D$ (mA)")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("ann1314-diode-lineaire.svg")
