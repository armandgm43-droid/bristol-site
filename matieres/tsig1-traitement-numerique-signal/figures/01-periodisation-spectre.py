"""TSIG1 ch. 1 — Périodisation du spectre par l'échantillonnage.
D'après les notes de cours [notes, f. 2 r°], redessinée. Spectre triangulaire normalisé (fmax = 1, fe = 3)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

fmax, fe = 1.0, 3.0
f = np.linspace(-5, 5, 2001)
tri = lambda g: np.clip(1 - np.abs(g) / fmax, 0, None)

fig, (a1, a2) = plt.subplots(2, 1, figsize=(7, 4.2), sharex=True)
a1.plot(f, tri(f), color="#2B4C9B")
a1.set_ylabel("$|X_a(f)|$")
a1.set_title("Signal analogique à bande limitée", fontsize=10)
a1.set_xticks([-fmax, fmax]); a1.set_xticklabels([r"$-f_{\max}$", r"$f_{\max}$"])
for k in range(-2, 3):
    a2.plot(f, tri(f - k * fe), color="#2B4C9B" if k == 0 else "#7E889B",
            ls="-" if k == 0 else "--")
for x in (-fe / 2, fe / 2):
    a2.axvline(x, color="#BF6014", lw=0.8, ls=":")
a2.set_ylabel(r"$T_e\,|X_m(f)|$")
a2.set_title("Signal échantillonné : motifs répétés tous les $f_e$", fontsize=10)
a2.set_xticks([-fe, -fe / 2, 0, fe / 2, fe])
a2.set_xticklabels([r"$-f_e$", r"$-f_e/2$", "0", r"$f_e/2$", r"$f_e$"])
a2.set_xlabel("Fréquence $f$ (Hz)")
for a in (a1, a2):
    a.set_ylim(0, 1.15); a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("01-periodisation-spectre.svg")
