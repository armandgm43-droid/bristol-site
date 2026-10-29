"""EARF1 ch. 4 — Densités spectrales théoriques (enveloppe complexe, centrées sur la porteuse)
des modulations BPSK (et OOK hors raie), QPSK et MSK pour un même débit binaire D.
Complément : formules classiques (impulsions rectangulaires pour BPSK et QPSK), calculées."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
x = np.linspace(-4, 4, 4001) + 1e-9            # (f - fp) / D
bpsk = np.sinc(x) ** 2
qpsk = np.sinc(2 * x) ** 2                     # R = D/2
msk = (np.cos(2 * np.pi * x) / (1 - 16 * x ** 2)) ** 2
db = lambda s: 10 * np.log10(np.maximum(s / s.max(), 1e-8))
fig, a = plt.subplots(figsize=(7.5, 3.3))
a.plot(x, db(bpsk), color="#2B4C9B", label="BPSK (lobe principal $2D$)")
a.plot(x, db(qpsk), color="#B23A3A", label="QPSK (lobe principal $D$)")
a.plot(x, db(msk), color="#2E7D32", label="MSK (lobe principal $1{,}5D$)")
a.set_ylim(-50, 3); a.set_xlim(-4, 4)
a.set_xlabel("$(f - f_p)/D$"); a.set_ylabel("DSP normalisée (dB)")
a.legend(fontsize=8, loc="upper right"); a.grid(alpha=0.3)
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("04-dsp-numeriques.svg")
