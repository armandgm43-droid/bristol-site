"""EANA4 TP 5/4 — Gain de boucle T(jω) = VR/Vin de l'oscillateur LC (Complément).
Modèle : T(jω) = −gm·Rs / [1 − ω²LC4 − ω²·Rs·r·C3·C4 + j(ω·r·C4 + Rs·ω(C3 + C4) − Rs·ω³·L·C3·C4)].
L1 = 220 µH, Q0 = 88 à 455 kHz (r ≈ 7,15 Ω), C3 = 1 nF, C4 = 3,3 nF [poly, p. 62-63].
|Av| = gm·Rs = 16,8 (mesure du compte rendu de 2023, notes externes) ; deux valeurs de Rs pour montrer
l'effet de l'impédance de sortie sur la sélectivité : 213 Ω (mesure de 2023) et 2 kΩ (hypothèse)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, GRIS = "#2B4C9B", "#7E889B"

L, r, C3, C4, Av = 220e-6, 7.147, 1e-9, 3.3e-9, 16.8
f = np.linspace(250e3, 550e3, 3001)
w = 2 * np.pi * f
fig, (a1, a2) = plt.subplots(2, 1, figsize=(8, 5.2), sharex=True)
for Rs, coul, ls in [(213, BLEU, "-"), (2000, GRIS, "--")]:
    gm = Av / Rs
    T = -gm * Rs / (1 - w**2 * L * C4 - w**2 * Rs * r * C3 * C4
                    + 1j * (w * r * C4 + Rs * w * (C3 + C4) - Rs * w**3 * L * C3 * C4))
    ph = np.degrees(np.unwrap(np.angle(T)))
    ph = ph - 360 * np.round(ph[np.argmin(np.abs(T.imag) + (T.real < 0) * 1e9)] / 360)
    a1.plot(f / 1e3, np.abs(T), color=coul, ls=ls, lw=1.6, label=f"Rs = {Rs} Ω")
    a2.plot(f / 1e3, ph, color=coul, ls=ls, lw=1.6)
f0 = 1 / (2 * np.pi * np.sqrt(L * C3 * C4 / (C3 + C4)))
for a in (a1, a2):
    a.axvline(f0 / 1e3, color="black", lw=0.6, ls=":")
    a.grid(alpha=0.3)
a1.axhline(1, color="#C2410C", lw=0.8)
a1.text(f0 / 1e3 + 3, 1.3, "|T| = 1", color="#C2410C", fontsize=9)
a1.set_ylabel("|T(jω)|")
a1.set_ylim(0, 18)
a1.legend(fontsize=9)
a2.set_ylabel("arg T (°)")
a2.set_xlabel("fréquence (kHz) — pointillé : 1/(2π√(L·Ceq)) ≈ 387 kHz")
fig.tight_layout()
fig.savefig("tp05-boucle-ouverte.svg")
