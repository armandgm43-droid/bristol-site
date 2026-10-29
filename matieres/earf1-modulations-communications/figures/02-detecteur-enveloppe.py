"""EARF1 ch. 2 — Détecteur d'enveloppe (diode idéale, R1C1) sur le signal OOK du TD 3.
Simulation (Complément) : porteuse 10 MHz, débit 1 Mbit/s, bits 1 1 0 1, tau = R1C1 = 0,3 µs."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
ROUGE, BLEU, ORANGE = "#B23A3A", "#2B4C9B", "#BF6014"
fp, D, tau = 10e6, 1e6, 0.3e-6
t = np.linspace(0, 3.8e-6, 40000); dt = t[1] - t[0]
bits = np.array([1, 1, 0, 1])
v = bits[np.minimum((t * D).astype(int), 3)] * np.sin(2 * np.pi * fp * t)
out = np.zeros_like(t)
for i in range(1, len(t)):
    dec = out[i - 1] * np.exp(-dt / tau)      # diode bloquée : décharge de C1 dans R1
    out[i] = max(v[i], dec)                   # diode passante : Vout suit VAM
fig, a = plt.subplots(figsize=(7.5, 2.8))
a.plot(t * 1e6, v, color=ROUGE, lw=0.5, label="$V_{AM}(t)$")
a.plot(t * 1e6, out, color=BLEU, lw=1.6, label="$V_{out}(t)$, $R_1C_1 = 0{,}3\\ \\mu$s")
a.axhline(0.5, color=ORANGE, ls=":", lw=1); a.text(3.82, 0.5, "0,5 V", va="center", fontsize=8, color=ORANGE)
a.set_xlabel("$t$ (µs)"); a.set_ylabel("Tension (V)"); a.set_ylim(-1.2, 1.35)
for k, b in enumerate(bits):
    a.text(k + 0.5, 1.2, f"« {b} »", ha="center", fontsize=8)
a.legend(loc="lower right", fontsize=8, ncol=2); a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("02-detecteur-enveloppe.svg")
