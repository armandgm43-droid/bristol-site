"""EANA1, partiels 2013-2014 (ex. II), 2014-2015 et 2015-2016 (ex. I) — transistor
commandé par un signal carré à travers C2. Simulation (Claude) du modèle de l'énoncé :
jonction base-émetteur VBE = 0,6 V en série avec rbe = 100 Ω, saturation VCEsat = 0,25 V
+ rsat = 10 Ω ; Vcc = 10 V, C2 = 1 nF, R1 = 1 kΩ, R2 = 40 kΩ, Rg = 10 kΩ, E = 10 V,
f = 50 kHz, rapport cyclique 0,5. Le transistor reste saturé dès que la jonction conduit
(beta = 50 ou 100 : même courbe)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

Vcc, C, R1, R2, Rg, E = 10, 1e-9, 1e3, 40e3, 10e3, 10
VBE, rbe, rsat, Vces = 0.6, 100, 10, 0.25
T, T1, dt, N = 20e-6, 10e-6, 5e-9, 6


def base(uC, eg):
    """uC = VB1 - Ve (tension du condensateur) ; renvoie VB1, Ve, courant dans Rg, IB."""
    VB = ((eg + uC) / Rg + Vcc / R2 + VBE / rbe) / (1 / Rg + 1 / R2 + 1 / rbe)
    if VB < VBE:
        VB, IB = ((eg + uC) / Rg + Vcc / R2) / (1 / Rg + 1 / R2), 0.0
    else:
        IB = (VB - VBE) / rbe
    Ve = VB - uC
    return VB, Ve, (eg - Ve) / Rg, IB


VBrepos = (Vcc / R2 + VBE / rbe) / (1 / R2 + 1 / rbe)
uC = VBrepos
t = np.arange(-0.15 * T, N * T, dt)
EG, VB1, VE, VC1 = [], [], [], []
Icsat = (Vcc - Vces) / (R1 + rsat)
for tk in t:
    eg = E if tk >= 0 and (tk % T) < T1 else 0.0
    VB, Ve, i, IB = base(uC, eg)
    EG.append(eg); VB1.append(VB); VE.append(Ve)
    VC1.append(Vces + rsat * Icsat if 50 * IB >= Icsat else Vcc - R1 * 50 * IB)
    if tk >= 0:
        uC -= i / C * dt
t = t * 1e6
fig, axs = plt.subplots(4, 1, figsize=(7, 7.2), sharex=True)
for ax, (nom, y) in zip(axs, [("$E_g$ (V)", EG), ("$V_e$ (V)", VE), ("$V_{B1}$ (V)", VB1), ("$V_{C1}$ (V)", VC1)]):
    ax.plot(t, y, color="#2B4C9B", lw=1.4)
    ax.axhline(0, color="k", lw=0.5)
    ax.set_ylabel(nom)
    for k in range(N + 1):
        ax.axvline(k * T * 1e6, color="#7E889B", ls=":", lw=0.7)
    ax.spines[["top", "right"]].set_visible(False)
axs[2].axhline(0.6, color="#BF6014", ls="--", lw=0.8)
axs[2].text(N * T * 1e6 + 0.5, 0.6, "0,6 V", color="#BF6014", va="center")
axs[3].set_xlabel("$t$ (µs)  —  $T_1 = 10$ µs, $T = 20$ µs")
fig.tight_layout()
fig.savefig("ann1314-transistor-chronogrammes.svg")
