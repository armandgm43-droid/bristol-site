"""EARF1 ch. 3 — Fonctions de Bessel de première espèce J_n(β), n = 0 à 4.
Complément : tracé calculé (scipy), même fonctions que le tableau du support [mod-ana, p. 39]."""
import numpy as np
from scipy.special import jv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
b = np.linspace(0, 10, 1000)
fig, a = plt.subplots(figsize=(7, 3.2))
for n, c in zip(range(5), ["#2B4C9B", "#B23A3A", "#2E7D32", "#BF6014", "#6A4C93"]):
    a.plot(b, jv(n, b), color=c, label=f"$J_{n}(\\beta)$")
a.axhline(0, color="black", lw=0.5)
for z in (2.405, 5.520, 8.654):
    a.axvline(z, color="#7E889B", ls=":", lw=0.8)
a.text(2.45, -0.45, "$J_0 = 0$ :\nporteuse nulle", fontsize=7.5, color="#555")
a.set_xlabel("Indice de modulation $\\beta$"); a.set_ylabel("$J_n(\\beta)$")
a.legend(fontsize=8, ncol=5, loc="upper right"); a.set_ylim(-0.5, 1.1)
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-bessel.svg")
