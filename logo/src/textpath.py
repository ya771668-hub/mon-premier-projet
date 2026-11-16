"""Convert text to SVG path data using fontTools (text vectorized, no font dependency)."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os

FDIR = os.path.join(os.path.dirname(__file__), "f")
_cache = {}


def font(name):
    if name not in _cache:
        _cache[name] = TTFont(os.path.join(FDIR, name + ".woff2"))
    return _cache[name]


def text_path(fontname, text, size, x=0, y=0, tracking=0.0, anchor="start"):
    """Return (d, width). y is the baseline. tracking in em units (0.1 = 10%)."""
    f = font(fontname)
    upm = f["head"].unitsPerEm
    s = size / upm
    cmap = f.getBestCmap()
    gs = f.getGlyphSet()
    hmtx = f["hmtx"]
    names = [cmap[ord(c)] for c in text]
    # total width
    adv = [hmtx[n][0] * s for n in names]
    tr = tracking * size
    width = sum(adv) + tr * (len(names) - 1)
    if anchor == "middle":
        x -= width / 2
    elif anchor == "end":
        x -= width
    pen = SVGPathPen(gs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip("."))
    cx = x
    for n, a in zip(names, adv):
        tp = TransformPen(pen, (s, 0, 0, -s, cx, y))
        gs[n].draw(tp)
        cx += a + tr
    return pen.getCommands(), width


def cap_height(fontname, size):
    f = font(fontname)
    upm = f["head"].unitsPerEm
    os2 = f["OS/2"]
    ch = getattr(os2, "sCapHeight", 0) or 0.7 * upm
    return ch * size / upm
