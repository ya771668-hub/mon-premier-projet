"""KARIBU BRAISE — 3 directions créatives, 100 % vectoriel (texte en tracés, aucun masque)."""
from textpath import text_path
from geo import P, D, rrect, circle, rot, mat, compose, union, diff, tr

# Palette (4 couleurs max)
C = dict(noir="#1C1714", or_="#F2B138", rouge="#C7361F", orange="#F47A20")

RAM = "rammetto-one-latin-400-normal"
LIL = "lilita-one-latin-400-normal"
SHR = "shrikhand-latin-400-normal"
BC8 = "barlow-condensed-latin-800-normal"
B6 = "barlow-latin-600-normal"
SLOGAN = "Le feu de nos îles, le goût de l’Afrique."

# Rôles -> couleur, selon le fond
THEMES = {
    "dark":  dict(flame=C["orange"], core=C["or_"], meat=C["rouge"], veg=C["or_"], stick=C["or_"],
                  word=C["or_"], sub=C["orange"], accent=C["rouge"], ring=C["or_"], disc=C["noir"]),
    "light": dict(flame=C["orange"], core=C["or_"], meat=C["rouge"], veg=C["or_"], stick=C["noir"],
                  word=C["noir"], sub=C["rouge"], accent=C["orange"], ring=C["noir"], disc=C["noir"]),
}


def theme(mode):
    if mode.startswith("mono:"):
        col = mode.split(":")[1]
        return {k: col for k in THEMES["dark"]}, True
    return THEMES[mode], False


def svg(w, h, body, bg=None, title="KARIBU BRAISE"):
    b = f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" '
            f'width="{w:g}" height="{h:g}" role="img" aria-label="{title}">'
            f'<title>{title}</title>{b}{body}</svg>')


def emit(layers, th, mono):
    """layers: liste (role, Path). En mono, tout est fusionné en un seul tracé."""
    if mono:
        u = union(*[p for _, p in layers])
        return f'<path d="{D(u)}" fill="{th["word"]}"/>'
    return "".join(f'<path d="{D(p)}" fill="{th[r]}"/>' for r, p in layers)


# ------------------------------------------------------------------ symbole
FLAME = ("M50 2 C57 17 73 28 80 44 C88 61 84 81 69 91 C62 96 56 98 50 98 "
         "C44 98 38 96 31 91 C16 81 12 61 21 45 C25 37 30 33 33 26 "
         "C35 37 38 43 43 46 C40 31 44 15 50 2 Z")
CORE = ("M50 44 C55 54 66 60 66 73 C66 84 59 90 50 90 C41 90 34 84 34 73 "
        "C34 65 38 61 42 57 C43 63 45 65 47 66 C46 58 47 51 50 44 Z")


def skewer_parts(t, chunk_w=23, chunk_h=19, ys=(38, 59, 80), stick=(8, 102), sw=5.4, gap=3.6, r=5.5):
    """Brochette verticale centrée x=50 puis transformée par t.
    Retourne (stick, [chunks], halo) en Paths."""
    st = P(rrect(50 - sw / 2, stick[0], sw, stick[1] - stick[0], sw / 2), t)
    chunks = [P(rrect(50 - chunk_w / 2, y - chunk_h / 2, chunk_w, chunk_h, r), t) for y in ys]
    halo = union(P(rrect(50 - sw / 2 - gap, stick[0] - gap, sw + 2 * gap, stick[1] - stick[0] + 2 * gap, sw / 2 + gap), t),
                 *[P(rrect(50 - chunk_w / 2 - gap, y - chunk_h / 2 - gap, chunk_w + 2 * gap, chunk_h + 2 * gap, r + gap), t) for y in ys])
    return st, chunks, halo


def symbol_layers(t=(1, 0, 0, 1, 0, 0), angle=-20, extra_cut=None):
    """Flamme + brochette dans une boîte 100x100, transformée par t."""
    st_t = compose(rot(angle, 50, 60), t)
    st, chunks, halo = skewer_parts(st_t)
    flame = diff(P(FLAME, t), halo)
    core = diff(P(CORE, t), halo)
    if extra_cut is not None:
        flame, core = diff(flame, extra_cut), diff(core, extra_cut)
    layers = [("flame", flame), ("core", core), ("stick", st)]
    for i, c in enumerate(chunks):
        layers.append(("veg" if i == 1 else "meat", c))
    return layers


# ------------------------------------------------------------------ Direction A
# Emblème : la flamme-brochette jaillit du cratère du Karthala, dans un médaillon.
VOLCANO = ("M0 100 L34 58 C37 54 41 53 44 56 L50 61 L56 56 C59 53 63 54 66 58 L100 100 Z")


def dir_a(mode="dark"):
    th, mono = theme(mode)
    if not mono:
        th = THEMES["dark"]  # l'emblème porte son propre fond
    W = 600
    out = []
    if mono:
        ring = diff(P(circle(300, 300, 296)), P(circle(300, 300, 284)))
        ring = union(ring, diff(P(circle(300, 300, 272)), P(circle(300, 300, 268))))
        out.append(("ring", ring))
    else:
        out.append(("disc", P(circle(300, 300, 296))))
        out.append(("ring", diff(P(circle(300, 300, 280)), P(circle(300, 300, 272)))))
    # volcan
    vt = mat(2.6, 1.15, 170, 172)
    vol = P(VOLCANO, vt)
    # flamme posée dans le cratère
    ft = mat(1.95, 1.95, 300 - 97.5, 52)
    halo = P(VOLCANO, compose(mat(1, 1, 0, -6), vt))  # volcan remonté = liseré de séparation
    sym = symbol_layers(ft, extra_cut=halo)
    # la flamme ne doit pas mordre sous le volcan : on coupe aussi stick/chunks qui dépassent en bas
    clipped = []
    for r, p in sym:
        if r in ("stick", "meat", "veg"):
            p = diff(p, halo)
        clipped.append((r, p))
    out += clipped
    out.append(("accent", vol))
    # texte
    d, _ = text_path(RAM, "KARIBU", 88, 300, 412, tracking=0.02, anchor="middle")
    out.append(("word", P(d)))
    d, _ = text_path(BC8, "BRAISE", 54, 300, 480, tracking=0.34, anchor="middle")
    out.append(("sub", P(d)))
    out.append(("ring", union(P(rrect(146, 459, 46, 6, 3)), P(rrect(408, 459, 46, 6, 3)))))
    return W, W, emit(out, th, mono)


def a_icon(mode="dark"):
    """Icône A : le médaillon simplifié (sans texte) – flamme + volcan."""
    th, mono = theme(mode)
    if not mono:
        th = THEMES["dark"]
    out = []
    if not mono:
        out.append(("disc", P(circle(50, 50, 50))))
    else:
        out.append(("ring", diff(P(circle(50, 50, 50)), P(circle(50, 50, 46)))))
    vt = mat(0.86, 0.38, 7, 56)
    vol = P(VOLCANO, vt)
    ft = mat(0.72, 0.72, 50 - 36, 10)
    halo = P(VOLCANO, compose(mat(1, 1, 0, -6), vt))
    sym = [(r, diff(p, halo)) for r, p in symbol_layers(ft)]
    out += sym
    out.append(("accent", vol))
    # on rogne au cercle
    clip = P(circle(50, 50, 44 if not mono else 43))
    from geo import inter
    out = [out[0]] + [(r, inter(p, clip)) for r, p in out[1:]]
    return 100, 100, emit(out, th, mono)


# ------------------------------------------------------------------ Direction B
# Monogramme : le fût du K est une brochette, la branche haute est une flamme.
K_FLAME = ("M38 49 C47 42 56 34 60 21 C63 29 61 36 58 41 C67 34 77 22 75 3 "
           "C88 15 94 33 85 47 C80 54 71 56 61 56 L38 56 Z")
K_LEG = "M38 54 L60 54 L94 98 L67 98 Z"


def k_layers(t=(1, 0, 0, 1, 0, 0)):
    out = []
    stick = P(rrect(16, 1, 6, 98, 3), t)
    out.append(("stick", stick))
    for i, y in enumerate((11, 39, 67)):
        out.append(("veg" if i == 1 else "meat", P(rrect(6, y, 26, 24, 5.5), t)))
    out.append(("word_k", P(K_LEG, t)))
    out.append(("flame", P(K_FLAME, t)))
    return out


WAVE = "M0 10 C12 0 24 0 36 10 C48 20 60 20 72 10 C84 0 96 0 108 10"


def wave_path(t, sw=6):
    # tracé de vague converti en forme pleine (pas de stroke) : on épaissit par échantillonnage
    import math
    pts = []
    for i in range(0, 109):
        x = i
        y = 10 - 10 * math.sin(math.pi * x / 36) * 1.0
        pts.append((x, y))
    up = [(x, y - sw / 2) for x, y in pts]
    dn = [(x, y + sw / 2) for x, y in reversed(pts)]
    d = "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in up + dn) + " Z"
    caps = union(P(circle(0, 10, sw / 2)), P(circle(108, 10, sw / 2)))
    return tr(union(P(d), caps), t)


def b_theme(th, mono):
    th = dict(th)
    if not mono:
        th["word_k"] = th["word"] if th["word"] != C["noir"] else C["noir"]
    else:
        th["word_k"] = th["word"]
    return th


def dir_b(mode="dark"):
    th, mono = theme(mode)
    th = b_theme(th, mono)
    out = k_layers(mat(1.9, 1.9, 300 - 95, 36))
    d, _ = text_path(LIL, "KARIBU", 116, 300, 360, tracking=0.03, anchor="middle")
    out.append(("word", P(d)))
    d, _ = text_path(BC8, "BRAISE", 52, 300, 430, tracking=0.44, anchor="middle")
    out.append(("sub", P(d)))
    out.append(("accent", wave_path(mat(0.75, 0.75, 300 - 40.5, 458), sw=7)))
    return 600, 500, emit(out, th, mono)


def b_icon(mode="dark"):
    th, mono = theme(mode)
    th = b_theme(th, mono)
    return 100, 100, emit(k_layers(mat(0.8, 0.8, 11, 10)), th, mono)


# ------------------------------------------------------------------ Direction C
# Logotype : le « I » de KARIBU devient une brochette surmontée d'une flamme.
def torch_layers(t, chunk_w=32, flame_s=0.5, sw=8):
    out = []
    out.append(("stick", P(rrect(-sw / 2, -112, sw, 124, sw / 2), t)))
    for i, y in enumerate((-80, -51, -22)):
        out.append(("veg" if i == 1 else "meat", P(rrect(-chunk_w / 2, y, chunk_w, 25, 6), t)))
    ft = compose(mat(flame_s, flame_s, -50 * flame_s, -116 - 98 * flame_s + 8), t)
    out.append(("flame", P(FLAME, ft)))
    out.append(("core", P(CORE, ft)))
    return out


def skew(a_deg):
    import math
    return (1, 0, math.tan(math.radians(a_deg)), 1, 0, 0)


def dir_c(mode="dark"):
    th, mono = theme(mode)
    th = dict(th)
    if mode == "dark":
        th["word"] = C["or_"]
    size, base, x0 = 156, 236, 30
    d1, w1 = text_path(SHR, "KAR", size, x0, base)
    gi = 56
    d2, w2 = text_path(SHR, "BU", size, x0 + w1 + gi, base)
    out = [("word", P(d1)), ("word", P(d2))]
    ix = x0 + w1 + gi / 2 - 2
    out += torch_layers(compose(skew(-12), mat(1, 1, ix, base)))
    total = w1 + gi + w2
    out.append(("accent", wave_path(mat(2.2, 1.0, x0 + total / 2 + 6 - 119, base + 20), sw=7)))
    d, _ = text_path(BC8, "BRAISE", 60, x0 + total / 2 + 6, base + 104, tracking=0.52, anchor="middle")
    out.append(("sub", P(d)))
    return x0 * 2 + total + 10, 360, emit(out, th, mono)


def c_icon(mode="dark"):
    """Icône C : la torche-brochette en grand dans un disque."""
    th, mono = theme(mode)
    if not mono:
        th = THEMES["dark"]
    out = []
    if not mono:
        out.append(("disc", P(circle(50, 50, 50))))
    else:
        out.append(("ring", diff(P(circle(50, 50, 50)), P(circle(50, 50, 46)))))
    out += torch_layers(compose(mat(0.47, 0.47, 50, 86)), chunk_w=50, flame_s=0.62, sw=12)
    return 100, 100, emit(out, th, mono)


# ------------------------------------------------------------------ Direction D
# Évolution du logo actuel : on garde sa structure (flamme centrale, 2 brochettes
# croisées, KARIBU serif or avec la vague dans le A, BRAISE rouge entre filets),
# mais en aplats simples. Touche insulaire : la vague du A (le volcan est retiré).
CIN = "cinzel-latin-900-normal"


def crossed_layers(t=(1, 0, 0, 1, 0, 0), ang=44, cx=50, cy=80):
    kw = dict(chunk_w=15, chunk_h=13, ys=(16, 31, 46), stick=(6, 104), sw=4.2, gap=3.0, r=3.2)
    s1, c1, h1 = skewer_parts(compose(rot(-ang, 50, cy), mat(1, 1, cx - 50, 0), t), **kw)
    s2, c2, h2 = skewer_parts(compose(rot(ang, 50, cy), mat(1, 1, cx - 50, 0), t), **kw)
    ft = compose(mat(0.74, 0.74, cx - 37, -1), t)
    flame = diff(P(FLAME, ft), h1, h2)
    core = diff(P(CORE, ft), h1, h2)
    # la brochette 2 passe sous la 1 : on la coupe par le halo de la 1
    s2 = diff(s2, h1)
    c2 = [diff(c, h1) for c in c2]
    out = [("flame", flame), ("core", core), ("stick", s2)]
    out += [("veg" if i == 1 else "meat", c) for i, c in enumerate(c2)]
    out += [("stick", s1)]
    out += [("veg" if i == 1 else "meat", c) for i, c in enumerate(c1)]
    return out


def karibu_wave(x, y, size, anchor="middle"):
    """KARIBU en Cinzel Black, avec la vague qui traverse le A (signature du logo actuel)."""
    d, w = text_path(CIN, "KARIBU", size, x, y, tracking=0.04, anchor=anchor)
    word = P(d)
    x0 = x - w / 2 if anchor == "middle" else x
    # vague à hauteur de la barre du A
    _, wk = text_path(CIN, "K", size, 0, 0)
    _, wa = text_path(CIN, "A", size, 0, 0)
    ax = x0 + wk + 0.04 * size          # début du A
    ww = wa * 1.25                       # la vague déborde un peu du A
    wt = mat(ww / 108, 0.11 * size / 20, ax + wa / 2 - ww / 2, y - 0.33 * size)
    wave = wave_path(wt, sw=0.11 * size / (0.11 * size / 20) / 2.2)
    halo = wave_path(wt, sw=0.24 * size / (0.11 * size / 20) / 2.2)
    return diff(word, halo), wave, w


def dir_d(mode="dark"):
    th, mono = theme(mode)
    out = crossed_layers(mat(2.3, 2.3, 300 - 115, 20))
    word, wave, w = karibu_wave(300, 370, 104)
    out += [("word", word), ("accent", wave)]
    d, bw = text_path(BC8, "BRAISE", 56, 300, 444, tracking=0.34, anchor="middle")
    out.append(("sub", P(d)))
    lw = 70
    out.append(("ring", union(P(rrect(300 - bw / 2 - 24 - lw, 421, lw, 5, 2.5)),
                              P(rrect(300 + bw / 2 + 24, 421, lw, 5, 2.5)))))
    th = dict(th)
    if not mono:
        th["accent"] = C["rouge"]
        th["sub"] = C["rouge"] if mode == "light" else C["orange"]
    return 600, 470, emit(out, th, mono)


def d_icon(mode="dark"):
    th, mono = theme(mode)
    return 100, 100, emit(crossed_layers(mat(0.92, 0.92, 4, 4)), th, mono)
