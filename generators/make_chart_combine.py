import os
import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

base = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(base)
csv_path = os.path.join(base, "chart.csv")
out_path = os.path.join(root, "images", "social", "chart.svg")
out_path_alt = os.path.join(root, "images", "social_alt", "chart.svg")

with open(csv_path, newline="", encoding="utf-8") as f:
    rows = list(csv.reader(f))

raw_statuses = rows[0][1:]
categories = [r[0] for r in rows[1:]]
raw = np.array([[float(v) for v in r[1:]] for r in rows[1:]])

# merge the six statuses into three lifecycle groups
groups = {
    "Upcoming": ["In Planning"],
    "Maintained": ["Work In Progress", "Actively Maintained", "Matured (Only Security Patches)"],
    "End of Development": ["Matured (No Further Development)", "Abandoned"],
}
statuses = list(groups)
idx = {name: i for i, name in enumerate(raw_statuses)}
data = np.column_stack([raw[:, [idx[s] for s in cols]].sum(axis=1) for cols in groups.values()])
data[data == 0] = 0.5  # small stub so zero values still show a bar

# blue=upcoming, green=maintained, red=ended
colors = ["#369acc", "#4fa84b", "#df3065"]
bg, fg, grid = "#21283000", "#acb3be", "#373a3e"

#alt color
colors_alt = ["#369acc", "#4fa84b", "#df3065"]
bg_alt, fg_alt, grid_alt = "#21283000", "#1c1c1c", "#747a82"

n_cat, n_series = len(categories), len(statuses)
bar_w = 0.5 / n_series
x_base = np.arange(n_cat)


def render(colors, bg, fg, grid, out):
    fig, ax = plt.subplots(figsize=(15, 5))
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
