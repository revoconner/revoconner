import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.font_manager import FontProperties

plt.rcParams["svg.fonttype"] = "path"  # bake text into vector paths so any viewer renders Fira Code

base = os.path.dirname(os.path.abspath(__file__))

# Fira Code - point this at your install if the path differs
font_candidates = [
    r"C:\Windows\Fonts\JetBrainsMono-VariableFont_wght.ttf",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\JetBrainsMono-VariableFont_wght.ttf"),
    r"C:\Windows\Fonts\FiraCodeNerdFont-VariableFont_wght.ttf",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\JetBrainsMono-VariableFont_wght.ttf"),
]

buttons = [
    ("My Repos — Active/Inactive State ↗", "button_dev_state.svg"),
    ("My Repos — Categorized for Usage ↗", "button_all_work.svg"),
]

bg = "#262626"
text_color = "#ffffff"   # GitHub link blue, ~5.9:1 contrast on bg (WCAG AA)
# alt text color
text_color_alt = "#ffffff"

border_lighten = 0.18    # how much brighter the border is than bg
font_size = 30
pad_x, pad_y = 28, 16
radius = 14
border_w = 3
dpi = 72                 # 1pt = 1px, so sizes below are in pixels

ref = "Ayg↗"             # tall reference so every button shares one height

def lighten(hex_color, factor):
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#{:02x}{:02x}{:02x}".format(*(round(c + (255 - c) * factor) for c in (r, g, b)))

border_color = lighten(bg, border_lighten)

def find_font():
    for path in font_candidates:
        if os.path.exists(path):
            return path
    raise SystemExit("Fira Code not found - install it or fix font_candidates.")

fp = FontProperties(fname=find_font(), size=font_size)

def measure(text):
    fig = plt.figure(dpi=dpi)
    t = fig.text(0, 0, text, fontproperties=fp)
    fig.canvas.draw()
    ext = t.get_window_extent()
    plt.close(fig)
    return ext.width, ext.height

H = measure(ref)[1] + 2 * pad_y
W = max(measure(text)[0] for text, _ in buttons) + 2 * pad_x  # widest label sets the shared width

root = os.path.dirname(base)

def make_button(text, filename, color, out_dir):
    fig = plt.figure(figsize=(W / dpi, H / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    m = border_w / 2 + 1  # keep stroke off the canvas edge
    box = FancyBboxPatch((m, m), W - 2 * m, H - 2 * m,
                         boxstyle=f"round,pad=0,rounding_size={radius}",
                         facecolor=bg, edgecolor=border_color, linewidth=border_w)
    box.set_mutation_scale(1.0)
    ax.add_patch(box)
    ax.text(W / 2, H / 2, text, ha="center", va="center_baseline",
            fontproperties=fp, color=color)

    out = os.path.join(out_dir, filename)
    fig.savefig(out, format="svg", transparent=True, pad_inches=0)
    plt.close(fig)
    print("Saved", out)

variants = [
    (text_color, os.path.join(root, "images", "project_button")),
    (text_color_alt, os.path.join(root, "images", "project_button_alt")),
]

for color, out_dir in variants:
    for text, filename in buttons:
        make_button(text, filename, color, out_dir)
