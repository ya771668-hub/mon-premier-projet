"""Géométrie vectorielle : opérations booléennes (pas de masques) via skia-pathops."""
import math
import pathops
from fontTools.svgLib.path import parse_path
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.svgPathPen import SVGPathPen


def _fmt(v):
    return ("%.2f" % v).rstrip("0").rstrip(".")


def P(d, t=(1, 0, 0, 1, 0, 0)):
    p = pathops.Path()
    parse_path(d, TransformPen(p.getPen(), t))
    return p


def D(p):
    pen = SVGPathPen(None, ntos=_fmt)
    p.draw(pen)
    return pen.getCommands()


def rrect(x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    k = 0.5523 * r
    return (f"M{x+r} {y} H{x+w-r} C{x+w-r+k} {y} {x+w} {y+r-k} {x+w} {y+r} "
            f"V{y+h-r} C{x+w} {y+h-r+k} {x+w-r+k} {y+h} {x+w-r} {y+h} "
            f"H{x+r} C{x+r-k} {y+h} {x} {y+h-r+k} {x} {y+h-r} "
            f"V{y+r} C{x} {y+r-k} {x+r-k} {y} {x+r} {y} Z")


def circle(cx, cy, r):
    return rrect(cx - r, cy - r, 2 * r, 2 * r, r)


def rot(a, cx, cy):
    a = math.radians(a)
    c, s = math.cos(a), math.sin(a)
    return (c, s, -s, c, cx - c * cx + s * cy, cy - s * cx - c * cy)


def mat(sx=1, sy=None, tx=0, ty=0):
    return (sx, 0, 0, sx if sy is None else sy, tx, ty)


def compose(*ts):
    """compose(a, b) = applique a puis b."""
    r = (1, 0, 0, 1, 0, 0)
    for t in ts:
        a, b, c, d, e, f = r
        A, B, Cc, Dd, E, F = t
        r = (A * a + Cc * b, B * a + Dd * b, A * c + Cc * d, B * c + Dd * d,
             A * e + Cc * f + E, B * e + Dd * f + F)
    return r


def union(*ps):
    out = pathops.Path()
    for p in ps:
        out = pathops.op(out, p, pathops.PathOp.UNION)
    return out


def diff(a, *bs):
    for b in bs:
        a = pathops.op(a, b, pathops.PathOp.DIFFERENCE)
    return a


def inter(a, b):
    return pathops.op(a, b, pathops.PathOp.INTERSECTION)


def tr(p, t):
    """Transforme un Path pathops."""
    out = pathops.Path()
    p.draw(TransformPen(out.getPen(), t))
    return out
