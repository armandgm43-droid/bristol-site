"""TSIG1 ch. 1 — Repliement spectral (fe < 2 fmax).
D'après les notes de cours [notes, f. 2 v°], redessinée. fmax = 1, fe = 1,4 ; somme des motifs en trait plein."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

fmax, fe = 1.0, 1.4
f = np.linspace(-3.5, 3.5, 2001)
tri = lambda g: np.clip(1 - np.abs(g) / fmax, 0, None)
fig, a = plt.subplots(figsize=(7, 2.6))
tot = np.zeros_like(f)
for k in range(-4, 5):
    a.plot(f, tri(f - k * fe), color="#7E889B", ls="--", lw=0.9)
    tot += tri(f - k * fe)
a.plot(f, tot, color="#2B4C9B", label="somme des motifs")
a.set_xticks([-fe, -fe / 2, 0, fe / 2, fe])
a.set_xticklabels([r"$-f_e$", r"$-f_e/2$", "0", r"$f_e/2$", r"$f_e$"])
a.set_xlabel("Fréquence $f$ (Hz)"); a.set_ylabel(r"$T_e\,|X_m(f)|$")
a.set_ylim(0, 1.6); a.legend(frameon=False, loc="upper right")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("01-repliement-spectral.svg")
