"""EAEP1, partiels 2016-2017 (ex. 3) et 2022-2023 (q. 13) — courant de grille d'un MOSFET
commandé par un push-pull (+15 V, RG = 10 ohms, Ciss = 1200 pF, VCEsat = 1 V).
Reconstruite (Claude) : i_G(t) = IG exp(-t/tau) à la fermeture, symétrique à l'ouverture."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

IG, tau = 1.4, 12.0                       # A, ns
t = np.linspace(0, 160, 3001)
t_off = 80
i = np.where(t < t_off, IG * np.exp(-t / tau), -IG * np.exp(-(t - t_off) / tau))
fig, ax = plt.subplots(figsize=(7, 3.4))
ax.plot(t, i, color="#2B4C9B")
ax.axhline(0, color="k", lw=0.6)
ax.plot([tau], [IG / np.e], "o", color="#BF6014")
ax.annotate(r"$t = \tau$ : 0,515 A ($\approx$ 0,518 A)", (tau, IG / np.e), (22, 0.85),
            arrowprops=dict(arrowstyle="->", color="#BF6014"))
t70 = tau * np.log(IG / 0.07)
ax.plot([t70], [0.07], "o", color="#BF6014")
ax.annotate(r"$t \approx 3\tau$ : 70 mA", (t70, 0.07), (45, 0.45),
            arrowprops=dict(arrowstyle="->", color="#BF6014"))
ax.plot([0, tau], [IG, 0], ls="--", color="#7E889B", lw=0.8)
ax.text(1, -0.15, r"$\tau = R_G C_{iss} = 12$ ns", color="#7E889B")
ax.set_yticks([-IG, 0, IG]); ax.set_yticklabels([r"$-I_G$", "0", r"$I_G = 1{,}4$ A"])
ax.set_xlabel("Temps (ns)"); ax.set_ylabel("$i_G(t)$")
ax.text(t_off + 2, 0.15, "ouverture (PNP)", color="#7E889B"); ax.text(30, 1.2, "fermeture (NPN)", color="#7E889B")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("ann-courant-grille.svg")
