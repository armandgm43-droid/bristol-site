# Annales 2025-2026, ex. 1 : y1 = x * h et y2 = y3 = y1(n+2). Régénérer : python ann-2025-convolution.py
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
y1 = {-1: 2, 0: 4, 1: 2, 2: 2, 3: 0, 4: -2}
fig, axs = plt.subplots(1, 2, figsize=(8, 2.6), sharey=True)
for ax, (titre, d) in zip(axs, [("$y_1[n] = x[n] * h[n]$", 0), ("$y_2[n] = y_3[n] = y_1[n+2]$", -2)]):
    n = [k + d for k in y1]; v = list(y1.values())
    ax.stem(n, v, basefmt="k-", linefmt="#2D4A8A", markerfmt="o")
    for a, b in zip(n, v): ax.annotate(f"{b}", (a, b), textcoords="offset points", xytext=(0, 6 if b >= 0 else -14), ha="center")
    ax.set_xticks(range(-4, 6)); ax.set_xlim(-4.5, 5.5); ax.set_ylim(-3.2, 5.2)
    ax.set_title(titre); ax.set_xlabel("$n$"); ax.grid(alpha=.25)
    for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
