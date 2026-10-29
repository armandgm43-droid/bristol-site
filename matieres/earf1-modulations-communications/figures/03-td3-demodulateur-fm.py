"""EARF1 ch. 3 — TD 3, exercice 2 : intégrateur puis détecteur d'enveloppe sur un signal à deux fréquences.
Complément : simulation (f_FM1 = 3 kHz de 0 à 2 ms et de 3 à 4 ms, f_FM2 = 6 kHz de 2 à 3 ms ; valeurs
choisies d'après l'allure de la figure 4 de l'énoncé [td3, p. 3] ; R0C0 normalisé, R1C1 = 1 ms ; V1 tracée en régime établi, sans la constante d'intégration)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
ROUGE, BLEU, GRIS = "#B23A3A", "#2B4C9B", "#7E889B"
t = np.linspace(0, 4e-3, 80000); dt = t[1] - t[0]
f = np.where((t >= 2e-3) & (t < 3e-3), 6e3, 3e3)
ph = 2 * np.pi * np.cumsum(f) * dt
v = np.sin(ph)
w0 = 2 * np.pi * 3e3                       # normalisation : R0C0 = 1/w0 (amplitude 1 à 3 kHz)
v1 = (w0 / (2 * np.pi * f)) * np.cos(ph)   # régime établi de l'intégrateur : U cos(wt) / (R0C0 w)
tau = 1e-3; out = np.zeros_like(t)
for i in range(1, len(t)):
    out[i] = max(v1[i], out[i - 1] * np.exp(-dt / tau))
fig, ax = plt.subplots(2, 1, figsize=(7.5, 4), sharex=True)
ax[0].plot(t * 1e3, v, color=ROUGE, lw=0.7); ax[0].set_ylabel("$V_{FM}(t)$ / $U$")
ax[1].plot(t * 1e3, v1, color=ROUGE, lw=0.7, label="$V_1(t)$")
ax[1].plot(t * 1e3, out, color=BLEU, lw=1.6, label="$V_{out}(t)$")
ax[1].axhline(0.5, color=GRIS, ls=":", lw=0.8); ax[1].axhline(1, color=GRIS, ls=":", lw=0.8)
ax[1].set_yticks([-1, -0.5, 0, 0.5, 1]); ax[1].set_yticklabels(["$-\\frac{U}{R_0C_0\\omega_1}$", "", "0", "$\\frac{U}{R_0C_0\\omega_2}$", "$\\frac{U}{R_0C_0\\omega_1}$"])
ax[1].legend(fontsize=8, loc="lower right"); ax[1].set_xlabel("$t$ (ms)")
for a in ax: a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-td3-demodulateur-fm.svg")
