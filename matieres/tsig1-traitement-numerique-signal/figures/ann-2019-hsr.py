"""TSIG1, partiel 2019-2020, exercice 2 : h = δ(n) - 2δ(n-1) - δ(n-2) en cascade avec h(-n) ;
h_sr(n) = h(n) * h(-n) = {-1, 0, 6, 0, -1} pour n = -2..2. Figure calculée.
Régénérer : python ann-2019-hsr.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
h = np.array([1, -2, -1])
hsr = np.convolve(h, h[::-1])          # indices n = -2 .. 2
assert list(hsr) == [-1, 0, 6, 0, -1]
n0 = np.arange(-2, 3)
n = np.arange(-4, 5)
v = np.zeros(len(n)); v[2:7] = hsr
fig, a = plt.subplots(figsize=(6, 2.6))
a.stem(n, v, linefmt="#2B4C9B", markerfmt="o", basefmt="k-")
for k, val in zip(n0, hsr):
    if val:
        a.annotate(f"{val:d}".replace("-", "−"), (k, val), textcoords="offset points",
                   xytext=(9, 2 if val > 0 else -10))
a.set_xticks(n); a.set_ylim(-2, 7)
a.set_xlabel("$n$"); a.set_ylabel("$h_{sr}(n)$")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
