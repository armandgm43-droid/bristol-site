"""Partiel 2014-2015, ex. 1 q. 2 : h[n] = 2^{-n} u[n]. Régénérer : python ann-2014-reponse-impulsionnelle.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
n = np.arange(-3, 9)
h = np.where(n >= 0, 0.5 ** n.clip(0), 0.0)
fig, a = plt.subplots(figsize=(6, 2.4))
a.stem(n, h, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
for k, v in zip(n[3:7], h[3:7]):
    a.annotate(["1", "1/2", "1/4", "1/8"][k], (k, v), textcoords="offset points", xytext=(9, 4))
a.plot(n[n >= 0], 0.5 ** n[n >= 0], color="#7E889B", ls="--", lw=0.8)
a.set_xticks(n); a.set_ylim(0, 1.2)
a.set_xlabel("$n$"); a.set_ylabel("$h[n]$")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
