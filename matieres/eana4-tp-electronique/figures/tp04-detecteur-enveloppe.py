"""EANA4 TP 4/5 — Modulation AM (m = 0,8) et sortie du détecteur d'enveloppe (D2, R5, C5).
Simulation (Complément) avec les valeurs de la maquette [poly, p. 45] : K = 0,1 V^-1 (AD633),
porteuse 455 kHz 10 Vcàc, modulant 1 kHz 4 Vcàc, Xo = 2,5 V ; R5 = 5,6 kΩ, C5 = 4,7 nF ;
diode Schottky modélisée par une loi exponentielle (Is = 2 nA, n = 1, soit ≈ 0,4 V à 10 mA)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, GRIS, ORANGE = "#2B4C9B", "#7E889B", "#C2410C"

K, A, Xm, f0, fm = 0.1, 5.0, 2.0, 455e3, 1e3
R, C, Is, VT = 5.6e3, 4.7e-9, 2e-9, 0.02585


def simule(Xo, duree=2.2e-3, dt=5e-9):
    t = np.arange(0, duree, dt)
    s = K * A * (Xo + Xm * np.cos(2 * np.pi * fm * t)) * np.cos(2 * np.pi * f0 * t)
    v = np.zeros_like(t)
    a = C / dt
    for k in range(1, len(t)):               # Euler implicite, résolu par Newton
        x = v[k - 1]
        for _ in range(6):
            e = np.exp(min((s[k] - x) / VT, 40.0))
            g = a * (x - v[k - 1]) + x / R - Is * (e - 1)
            dg = a + 1 / R + Is * e / VT
            x -= g / dg
        v[k] = x
    return t, s, v


fig, axes = plt.subplots(2, 1, figsize=(8.6, 5.4), sharex=True)
for a, Xo, titre in [(axes[0], 2.5, "m = 0,8 (Xo = 2,5 V)"), (axes[1], 1.5, "surmodulation : m ≈ 1,33 (Xo = 1,5 V)")]:
    t, s, v = simule(Xo)
    garde = t > 0.2e-3
    tt = (t[garde] - 0.2e-3) * 1e3
    a.plot(tt, s[garde], color=GRIS, lw=0.3, label="s(t) en J4 (modulé)")
    env = K * A * np.abs(Xo + Xm * np.cos(2 * np.pi * fm * t[garde]))
    a.plot(tt, env, color=ORANGE, lw=1.1, ls="--", label="enveloppe |K·A·x(t)|")
    a.plot(tt, v[garde], color=BLEU, lw=1.6, label="sortie J9 (simulée)")
    a.axhline(0, color="black", lw=0.5)
    a.set_title(titre, fontsize=10)
    a.set_ylabel("tension (V)")
    a.grid(alpha=0.3)
axes[0].legend(loc="upper right", fontsize=8, ncol=3)
axes[1].set_xlabel("temps (ms)")
fig.tight_layout()
fig.savefig("tp04-detecteur-enveloppe.svg")
