"""EARF1 ch. 3 — Démodulation FM par discrimination : signal FM, sa dérivée et l'enveloppe détectée.
D'après le support [mod-ana, p. 47], recalculée (fp = 12 fm, Δf = 6 fm)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
ROUGE, BLEU, VERT, GRIS = "#B23A3A", "#2B4C9B", "#2E7D32", "#7E889B"
fm, fp, df = 1.0, 12.0, 6.0
t = np.linspace(0, 2, 20000)
m = np.cos(2 * np.pi * fm * t)
phase = 2 * np.pi * fp * t + (df / fm) * np.sin(2 * np.pi * fm * t)
s = np.cos(phase)
ds = np.gradient(s, t) / (2 * np.pi * (fp + df))
env = (fp + df * m) / (fp + df)
fig, ax = plt.subplots(3, 1, figsize=(7, 4.8), sharex=True)
ax[0].plot(t, s, color=ROUGE, lw=0.7); ax[0].set_ylabel("$s_{FM}(t)$")
ax[1].plot(t, ds, color=ROUGE, lw=0.7); ax[1].plot(t, env, color=GRIS, ls="--"); ax[1].plot(t, -env, color=GRIS, ls="--")
ax[1].set_ylabel("$\\mathrm{d}s_{FM}/\\mathrm{d}t$\n(normalisée)")
ax[2].plot(t, env, color=BLEU, lw=1.6, label="sortie du détecteur d'enveloppe")
ax[2].plot(t, m * df / (fp + df) + fp / (fp + df), color=VERT, ls=":", lw=1.4, label="$m(t)$ (à un gain et un décalage près)")
ax[2].set_ylabel("$m^*(t)$"); ax[2].legend(fontsize=7.5, loc="lower right"); ax[2].set_xlabel("$t\\,f_m$")
for a in ax: a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-discriminateur.svg")
