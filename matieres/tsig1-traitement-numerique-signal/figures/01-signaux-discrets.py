"""TSIG1 ch. 1 — Échelon, impulsion et séquence finie.
D'après les notes de cours [notes, f. 3 r° et v°], redessinée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

n = np.arange(-3, 6)
sig = [("Échelon $u[n]$", (n >= 0).astype(float)),
       (r"Impulsion $\delta[n]$", (n == 0).astype(float)),
       (r"$\delta[n] + 2\delta[n-1] - \delta[n-2]$", 1.0 * (n == 0) + 2.0 * (n == 1) - 1.0 * (n == 2))]
fig, ax = plt.subplots(1, 3, figsize=(8, 2.4))
for a, (titre, y) in zip(ax, sig):
    a.stem(n, y, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
    a.set_title(titre, fontsize=10); a.set_xlabel("$n$")
    a.set_xticks(n); a.spines[["top", "right"]].set_visible(False)
ax[0].set_ylabel("Amplitude")
fig.tight_layout(); fig.savefig("01-signaux-discrets.svg")
