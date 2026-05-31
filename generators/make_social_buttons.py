import os
import re
import io
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from matplotlib.font_manager import FontProperties

plt.rcParams["svg.fonttype"] = "path"  # bake text into vector paths so any viewer renders the font

base = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(base)
icon_dir = os.path.join(root, "images", "social_raw")

# Fira Code / JetBrains Mono - point this at your install if the path differs
font_candidates = [
    r"C:\Windows\Fonts\FiraCodeNerdFontPropo-Retina.ttf",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\FiraCodeNerdFontPropo-Retina.ttf"),
    r"C:\Windows\Fonts\FiraCodeNerdFontPropo-Retina.ttf",
    os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Windows\Fonts\FiraCodeNerdFontPropo-Retina.ttf"),
]

# icon file (in social_raw, chart excluded), button label
buttons = [
    ("artstation.svg", "Artstation"),
    ("website.svg", "Website"),

    ("linkedin.svg", "Linkedin"),
]

bg = "#21283015"
text_color = "#58a0ff"   # GitHub link blue, ~5.9:1 contrast on bg (WCAG AA)
text_color_alt = "#007fe0"
icon_color = "#ffa53e"   # forced on every icon, overrides their source fill

border_lighten = 0.18    # how much brighter the border is than bg
font_size = 22           # text label, ~75% of the icon size
icon_ref_size = 30       # sets the icon + button height (icon stays larger)
pad_x, pad_y = 28, 16
gap = 16                 # space between icon and text
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
    raise SystemExit("Font not found - install it or fix font_candidates.")

font_path = find_font()
fp = FontProperties(fname=font_path, size=font_size)        # text label
fp_icon = FontProperties(fname=font_path, size=icon_ref_size)  # icon/button height

def measure(text, font):
    fig = plt.figure(dpi=dpi)
    t = fig.text(0, 0, text, fontproperties=font)
    fig.canvas.draw()
    ext = t.get_window_extent()
    plt.close(fig)
    return ext.width, ext.height

def load_icon(path):
    with open(path, encoding="utf-8") as f:
        s = f.read()
    m = re.search(r"<svg\b[^>]*>", s, re.I)
    open_tag, inner = m.group(0), s[m.end():]
    inner = re.sub(r"</svg>\s*$", "", inner.rstrip(), flags=re.I)
    vb = re.search(r'viewBox\s*=\s*"([^"]+)"', open_tag, re.I).group(1)
    vx, vy, vw, vh = (float(v) for v in re.split(r"[ ,]+", vb.strip()))
    return inner, (vx, vy, vw, vh)

icon_size = measure(ref, fp_icon)[1]  # icon height, kept at the larger reference size
H = icon_size + 2 * pad_y

# preload icons and figure out the shared width from the widest icon+text group
icons = {}
for fname, label in buttons:
    inner, (vx, vy, vw, vh) = load_icon(os.path.join(icon_dir, fname))
    icon_w = icon_size * (vw / vh)
    icons[fname] = (inner, (vx, vy, vw, vh), icon_w, measure(label, fp)[0])

W = max(iw + gap + tw for _, _, iw, tw in icons.values()) + 2 * pad_x

def make_button(fname, label, color, out_dir):
    inner, (vx, vy, vw, vh), icon_w, text_w = icons[fname]
    group_w = icon_w + gap + text_w
    start_x = (W - group_w) / 2  # centre the icon+text group

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
    ax.text(start_x + icon_w + gap, H / 2, label, ha="left", va="center",
            fontproperties=fp, color=color)

    buf = io.StringIO()
    fig.savefig(buf, format="svg", transparent=True, pad_inches=0)
    plt.close(fig)
    svg = buf.getvalue()

    # map data coords to the output viewBox, then drop the icon in as a nested svg
    ow, oh = (float(v) for v in re.search(
        r'viewBox="[\d.]+ [\d.]+ ([\d.]+) ([\d.]+)"', svg).groups())
    sx, sy = ow / W, oh / H
    px = start_x * sx
    py = (H / 2 - icon_size / 2) * sy
    icon = (f'<svg x="{px:.3f}" y="{py:.3f}" width="{icon_w * sx:.3f}" '
            f'height="{icon_size * sy:.3f}" viewBox="{vx} {vy} {vw} {vh}" '
            f'preserveAspectRatio="xMidYMid meet" overflow="visible" '
            f'fill="{icon_color}">{inner}</svg>')
    i = svg.rfind("</svg>")
    svg = svg[:i] + icon + svg[i:]

    out = os.path.join(out_dir, fname)
    with open(out, "w", encoding="utf-8") as f:
        f.write(svg)
    print("Saved", out)

variants = [
    (text_color, os.path.join(root, "images", "social")),
    (text_color_alt, os.path.join(root, "images", "social_alt")),
]

for color, out_dir in variants:
    for fname, label in buttons:
        make_button(fname, label, color, out_dir)
