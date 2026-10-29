"""EARF1 ch. 3 — Modulation de fréquence par un modulant sinusoïdal : modulant, fréquence instantanée et signal FM.
D'après le support [mod-ana, p. 36-37], recalculée (fp = 12 fm, Δf = 8 fm, soit β = 8)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
VERT, ROUGE, BLEU, GRIS = "#2E7D32", "#B23A3A", "#2B4C9B", "#7E889B"
fm, fp, df = 1.0, 12.0, 8.0
t = np.linspace(0, 2, 8000)
m = np.cos(2 * np.pi * fm * t)
fi = fp + df * m
s = np.cos(2 * np.pi * fp * t + (df / fm) * np.sin(2 * np.pi * fm * t))
fig, ax = plt.subplots(3, 1, figsize=(7, 4.8), sharex=True)
ax[0].plot(t, m, color=VERT); ax[0].set_ylabel("$m(t)$"); ax[0].set_yticks([-1, 0, 1]); ax[0].set_yticklabels(["$-A_m$", "0", "$A_m$"])
ax[1].plot(t, fi, color=BLEU); ax[1].set_ylabel("$f_i(t)$")
ax[1].set_yticks([fp - df, fp, fp + df]); ax[1].set_yticklabels(["$f_p - \\Delta f$", "$f_p$", "$f_p + \\Delta f$"])
ax[1].axhline(fp, color=GRIS, ls=":", lw=0.8)
ax[2].plot(t, s, color=ROUGE, lw=0.7); ax[2].set_ylabel("$s_{FM}(t)$"); ax[2].set_yticks([-1, 0, 1]); ax[2].set_yticklabels(["$-A$", "0", "$A$"])
ax[2].set_xlabel("$t\\,f_m$")
for a in ax: a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-signal-fm.svg")
