"""EARF1 ch. 2 — AM double bande sans porteuse, modulant sinusoïdal : allures temporelles.
D'après le support [mod-ana, p. 21], recalculée (fp = 20 fm)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, VERT, ROUGE, GRIS = "#2B4C9B", "#2E7D32", "#B23A3A", "#7E889B"
fm, fp = 1.0, 20.0
t = np.linspace(0, 2, 6000)
m = np.cos(2 * np.pi * fm * t); p = np.cos(2 * np.pi * fp * t)
fig, ax = plt.subplots(3, 1, figsize=(7, 4.6), sharex=True)
ax[0].plot(t, p, color=BLEU, lw=0.8); ax[0].set_ylabel("$p(t)$")
ax[1].plot(t, m, color=VERT); ax[1].set_ylabel("$m(t)$")
ax[2].plot(t, m * p, color=ROUGE, lw=0.8)
ax[2].plot(t, m, color=GRIS, ls="--", lw=1); ax[2].plot(t, -m, color=GRIS, ls="--", lw=1)
ax[2].set_ylabel("$s_{AMDBSP}(t)$")
ax[2].set_title("Enveloppe $|m(t)|$ ; la phase de la porteuse s'inverse quand $m(t)$ change de signe", fontsize=8.5)
ax[2].set_xlabel("$t$ (en périodes du modulant $1/f_m$)")
for a in ax:
    a.set_ylim(-1.3, 1.3); a.set_yticks([-1, 0, 1]); a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("02-amdbsp-temporel.svg")
