import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

base = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(base, "chart.csv")
out_path = os.path.join(base, "chart.svg")
out_path_alt = os.path.join(base, "chart_alt.svg")

with open(csv_path, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

statuses = rows[0][1:]
categories = [r[0] for r in rows[1:]]
data = np.array([[float(v) for v in r[1:]] for r in rows[1:]])
data[data == 0] = 0.1  # small stub so zero values still show a bar

# colors map to project health: blue=planning, amber=building,
# green=active, teal=stable, orange=stale, red=dead
colors = ["#58a6ff", "#e3b341", "#3fb950", "#39c5cf", "#db6d28", "#f85149"]
bg, fg, grid = "#ffffff00", "#7d8590", "#373a3e"

# make charts alt
colors_alt = ["#58a6ff", "#e3b341", "#3fb950", "#39c5cf", "#db6d28", "#f85149"]
bg_alt, fg_alt, grid_alt = "#ffffff00", "#252525", "#505050"

n_cat, n_series = len(categories), len(statuses)
bar_w = 0.8 / n_series
x_base = np.arange(n_cat)


def render(colors, bg, fg, grid, out):
    fig, ax = plt.subplots(figsize=(13, 7))
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    for i in range(n_series):
        offset = (i - (n_series - 1) / 2) * bar_w
        ax.bar(x_base + offset, data[:, i], width=bar_w * 0.85,
               color=colors[i % len(colors)], zorder=3)

    ax.set_xticks(x_base)
    ax.set_xticklabels(categories, color=fg, fontsize=11,
                       rotation=20, ha="right", rotation_mode="anchor")

    ax.tick_params(axis="y", colors=fg)
    ax.set_ylim(0, data.max() + 1)
    ax.set_ylabel("Number of projects", color=fg, fontsize=11)
    ax.yaxis.grid(True, color=grid, linestyle="--", linewidth=1, zorder=0)
    ax.set_axisbelow(True)
    for spine in ax.spines.values():
        spine.set_visible(False)

    # hollow circle markers to match the legend style
    handles = [Line2D([0], [0], marker="o", linestyle="none", markerfacecolor="none",
                      markeredgecolor=colors[i % len(colors)], markeredgewidth=2,
                      markersize=11, label=statuses[i]) for i in range(n_series)]
    ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.22),
              ncol=3, frameon=False, labelcolor=fg, fontsize=12)

    fig.savefig(out, format="svg", facecolor=bg, bbox_inches="tight")
    plt.close(fig)
    print("Saved", out)


render(colors, bg, fg, grid, out_path)
render(colors_alt, bg_alt, fg_alt, grid_alt, out_path_alt)
