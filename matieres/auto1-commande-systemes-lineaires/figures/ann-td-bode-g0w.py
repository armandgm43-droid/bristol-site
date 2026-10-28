"""Partiels AU205 « Commande à temps discret » (2015-2016 à 2017-2018), question sur
G0(w) : pseudo-réponse en fréquences G0(jv) = 0,11 (1 + jv/96)(1 - jv) / (jv (1 + jv/0,03125)),
transmittance donnée par le sujet (T = 0,01 s). Gain et phase réels en trait plein,
diagrammes asymptotiques en pointillés gris, pseudo-pulsation au gain unité imposée
vu = tg(wu T/2) = tg(0,1) en trait mixte. Régénérer : python ann-td-bode-g0w.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
K, v1, v2, v3 = 0.11, 0.03125, 1.0, 96.0
vu = np.tan(20 * 0.01 / 2)
v = np.logspace(-3, 3.5, 3000); w = 1j * v
G = K * (1 + w / v3) * (1 - w) / (w * (1 + w / v1))
g = 20 * np.log10(abs(G))
ph = -90 - np.degrees(np.arctan(v / v1)) - np.degrees(np.arctan(v / v2)) + np.degrees(np.arctan(v / v3))
assert abs(np.degrees(np.angle(K * (1 + 1j * vu / v3) * (1 - 1j * vu) / (1j * vu * (1 + 1j * vu / v1)))) + 168.37) < 0.01
# Asymptotes : -20 dB/déc, puis -40, puis -20 (zéro instable en v = 1), puis 0 (zéro en v = 96)
ga = 20 * np.log10(K / v)
ga = np.where(v > v1, ga - 20 * np.log10(v / v1), ga)
ga = np.where(v > v2, ga + 20 * np.log10(v / v2), ga)
ga = np.where(v > v3, ga + 20 * np.log10(v / v3), ga)
pa = np.where(v < v1, -90, np.where(v < v2, -180, np.where(v < v3, -270, -180)))
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.6, 5.6), sharex=True)
a1.semilogx(v, g, color="#2B4C9B", lw=1.6, label="gain réel")
a1.semilogx(v, ga, "--", color="#7E889B", lw=1.3, label="asymptotes")
a2.semilogx(v, ph, color="#2B4C9B", lw=1.6, label="phase réelle")
a2.semilogx(v, pa, "--", color="#7E889B", lw=1.3, label="asymptotes")
for a in (a1, a2):
    for x in (v1, v2, v3):
        a.axvline(x, color="k", ls=":", lw=0.6)
    a.axvline(vu, color="#B5452B", ls="-.", lw=1.0)
    a.grid(alpha=0.25, which="both"); a.spines[["top", "right"]].set_visible(False)
a1.axhline(0, color="k", lw=0.6)
a1.text(v1 * 1.1, 45, "$1/32$", fontsize=9); a1.text(v2 * 1.1, 45, "$1$", fontsize=9)
a1.text(v3 * 1.1, 45, "$96$", fontsize=9)
a1.text(vu * 1.1, -25, "$\\nu_u \\approx 0{,}1$\n$-9{,}7$ dB", fontsize=9, color="#B5452B")
a1.text(2e-3, 20, "$-20$ dB/déc", fontsize=9); a1.text(0.15, -40, "$-40$ dB/déc", fontsize=9)
a1.text(4, -70, "$-20$ dB/déc", fontsize=9); a1.text(300, -100, "0 dB/déc", fontsize=9)
a1.set_ylim(-120, 60); a1.set_ylabel("$|G_0(j\\nu)|$ (dB)")
a1.legend(fontsize=8, frameon=False, loc="lower left")
a2.text(vu * 1.1, -150, "$-168{,}4°$", fontsize=9, color="#B5452B")
a2.set_ylim(-290, -70); a2.set_yticks([-270, -225, -180, -135, -90])
a2.set_ylabel("$\\arg G_0(j\\nu)$ (°)"); a2.set_xlabel("pseudo-pulsation $\\nu$ (sans unité)")
a2.legend(fontsize=8, frameon=False, loc="lower left")
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
