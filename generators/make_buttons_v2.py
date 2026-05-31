import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
from matplotlib.font_manager import FontProperties

plt.rcParams["svg.fonttype"] = "path"  # bake text into vector paths so any viewer renders the fonts

base = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(base)

# Fira Code - point this at your install if the path differs
font_candidates = [
    r"C:\Windows\Fonts\JetBrainsMono-VariableFont_wght.ttf",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\JetBrainsMono-VariableFont_wght.ttf"),
    r"C:\Windows\Fonts\FiraCodeNerdFont-VariableFont_wght.ttf",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\FiraCodeNerdFont-VariableFont_wght.ttf"),
]
sub_font_path = r"C:\Windows\Fonts\verdana.ttf"

# header, subheader, filename
buttons = [
    ("Development State of My Repositories ↗", "Check out which ones are being worked on,maintained and abandoned", "button_dev_state.svg"),
    ("Categorised List of My Repositories ↗", "Grouped under easy to find categories like dev tools, maya plugin, etc", "button_all_work.svg"),
]

bg = "#00000000"
#dark theme
text_color = "#23c4ff"
sub_text = "#000"          # subheader font color
border_color = "#9d9d9d"   # border + subheader background
#light theme
text_color_alt = "#b03b00"
sub_text_alt = "#dadada"          # subheader font color
border_color_alt = "#252525"   # border + subheader background


font_size = 30             # header
sub_font_size = 20         # subheader, smaller to fit
pad_x = 28
pad_y = 16                 # header vertical padding
pad_y_sub = 12             # subheader vertical padding
radius = 14
border_w = 3
dpi = 72                   # 1pt = 1px, so sizes below are in pixels

ref = "Ayg↗"               # tall reference so every button shares one header height
sub_ref = "Ayg"

def find_font():
    for path in font_candidates:
        if os.path.exists(path):
            return path
    raise SystemExit("Fira Code not found - install it or fix font_candidates.")

fp = FontProperties(fname=find_font(), size=font_size)
fp_sub = FontProperties(fname=sub_font_path, size=sub_font_size)

def measure(text, font):
    fig = plt.figure(dpi=dpi)
    t = fig.text(0, 0, text, fontproperties=font)
    fig.canvas.draw()
    ext = t.get_window_extent()
    plt.close(fig)
    return ext.width, ext.height

header_h = measure(ref, fp)[1] + 2 * pad_y
sub_h = measure(sub_ref, fp_sub)[1] + 2 * pad_y_sub
H = header_h + sub_h

# widest of every header and subheader sets the shared width
all_text = [(h, fp) for h, _, _ in buttons] + [(s, fp_sub) for _, s, _ in buttons]
W = max(measure(t, f)[0] for t, f in all_text) + 2 * pad_x

def make_button(header, sub, filename, color, out_dir):
    fig = plt.figure(figsize=(W / dpi, H / dpi), dpi=dpi)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")

    m = border_w / 2 + 1  # keep stroke off the canvas edge
    shape = FancyBboxPatch((m, m), W - 2 * m, H - 2 * m,
                           boxstyle=f"round,pad=0,rounding_size={radius}",
                           facecolor=bg, edgecolor="none", linewidth=0)
    ax.add_patch(shape)

    # lower band filled with border color, clipped to the rounded shape so corners match
    band = Rectangle((0, 0), W, sub_h, facecolor=border_color, edgecolor="none")
    ax.add_patch(band)
    band.set_clip_path(shape)

    # one border around both stacks
    border = FancyBboxPatch((m, m), W - 2 * m, H - 2 * m,
                            boxstyle=f"round,pad=0,rounding_size={radius}",
                            facecolor="none", edgecolor=border_color, linewidth=border_w)
    ax.add_patch(border)

    ax.text(W / 2, sub_h + header_h / 2, header, ha="center", va="center_baseline",
            fontproperties=fp, color=color)
    ax.text(W / 2, sub_h / 2, sub, ha="center", va="center_baseline",
            fontproperties=fp_sub, color=sub_text)

    out = os.path.join(out_dir, filename)
    fig.savefig(out, format="svg", transparent=True, pad_inches=0)
    plt.close(fig)
    print("Saved", out)

variants = [
    (text_color, os.path.join(root, "images", "project_button")),
    (text_color_alt, os.path.join(root, "images", "project_button_alt")),
]

for color, out_dir in variants:
    for header, sub, filename in buttons:
        make_button(header, sub, filename, color, out_dir)
