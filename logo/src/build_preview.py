import os, html
from design import *
from textpath import text_path

OUT = "/home/user/mon-premier-projet/logo"
os.makedirs(OUT + "/directions", exist_ok=True)


def inner(fn, mode, x, y, box_w, box_h=None, align="center"):
    w, h, body = fn(mode)
    box_h = box_h or box_w
    s = min(box_w / w, box_h / h)
    ox = x + (box_w - w * s) / 2
    oy = y + (box_h - h * s) / 2
    return f'<g transform="translate({ox:.2f} {oy:.2f}) scale({s:.4f})">{body}</g>'


def standalone(fn, mode, bg=None, pad=0):
    w, h, body = fn(mode)
    return svg(w, h, body, bg=bg)


def slogan(x, y, size, col, anchor="middle"):
    d, _ = text_path(B6, SLOGAN, size, x, y, anchor=anchor)
    return f'<path d="{d}" fill="{col}"/>'


DIRS = {
    "A": dict(name="Emblème « Karthala »", logo=dir_a, icon=a_icon,
              pitch=["Un médaillon rond : la flamme-brochette jaillit du cratère du Karthala, KARIBU en capitales larges (Rammetto One), BRAISE espacé.",
                     "Le badge se lit comme un sceau de qualité « grillé maison » et se pose partout : tampon kraft, sticker, broderie de tablier.",
                     "Force : très identitaire et rassurant. Limite : plus de détails, l’icône seule est la moins nette en 32 px."]),
    "B": dict(name="Monogramme « K-brochette »", logo=dir_b, icon=b_icon,
              pitch=["Le K est construit avec le produit : le fût est une brochette (viande / légume / viande), la branche haute est une flamme.",
                     "Un symbole unique, géométrique, qui fonctionne seul comme icône Glovo / Uber Eats ou photo de profil, à la manière des grandes chaînes.",
                     "Force : lisibilité maximale en 32 px et en une couleur. Typo Lilita One, ronde et gourmande ; une vague discrète pour l’île."]),
    "C": dict(name="Logotype « Torche »", logo=dir_c, icon=c_icon,
              pitch=["Le nom est le logo : KARIBU en Shrikhand, script gras et généreux, dont le I devient une brochette coiffée d’une flamme.",
                     "Style « street food » rétro et chaleureux : énergique, appétissant, mémorisable. Une vague rouge souligne le mot, comme la côte.",
                     "Force : enseigne et packaging très expressifs. Limite : l’icône (torche seule) est plus abstraite que celle de B."]),
}


def mock_sign(fn, mode="dark"):
    # enseigne façade 3 m : bandeau charbon sur mur
    W, H = 640, 300
    b = f'<rect width="{W}" height="{H}" fill="#E9E1D3"/>'
    b += f'<rect x="0" y="210" width="{W}" height="90" fill="#8B7B66"/><rect x="40" y="210" width="560" height="90" fill="#3A322B"/>'
    b += f'<rect x="20" y="24" width="600" height="170" rx="6" fill="{C["noir"]}"/>'
    b += f'<rect x="20" y="190" width="600" height="8" fill="{C["or_"]}"/>'
    b += inner(fn, mode, 40, 34, 560, 150)
    return svg(W, H, b)


def mock_cup(fn, mode="light"):
    W, H = 300, 300
    b = f'<rect width="{W}" height="{H}" fill="#EFE7DA"/>'
    b += '<ellipse cx="150" cy="276" rx="70" ry="9" fill="#00000022"/>'
    b += f'<path d="M76 40 L224 40 L206 272 L94 272 Z" fill="#FFFFFF"/>'
    b += f'<path d="M80 92 L220 92 L213 186 L87 186 Z" fill="{C["noir"]}"/>'
    b += f'<rect x="68" y="24" width="164" height="20" rx="6" fill="{C["noir"]}"/>'
    b += inner(fn, "dark" if fn is not dir_a else "dark", 92, 98, 116, 82)
    b += f'<path d="M89 196 L211 196 L210 206 L90 206 Z" fill="{C["orange"]}"/>'
    return svg(W, H, b)


def mock_bag(fn):
    W, H = 300, 300
    b = f'<rect width="{W}" height="{H}" fill="#EFE7DA"/>'
    b += '<ellipse cx="150" cy="282" rx="96" ry="8" fill="#00000022"/>'
    b += '<path d="M60 70 L240 70 L248 280 L52 280 Z" fill="#C49A6C"/>'
    b += '<path d="M60 70 L240 70 L238 92 L62 92 Z" fill="#B48A5C"/>'
    b += '<path d="M110 70 C110 30 190 30 190 70" fill="none" stroke="#A97F52" stroke-width="7"/>'
    b += inner(fn, "mono:" + C["noir"], 80, 120, 140, 130)
    return svg(W, H, b)


def mock_app(icon_fn):
    W, H = 420, 160
    b = f'<rect width="{W}" height="{H}" fill="#F4F1EC"/>'
    x = 20
    for sz in (120, 64, 48, 32):
        b += f'<g><clipPath id="cl{sz}{id(icon_fn)}"><circle cx="{x+sz/2}" cy="{80}" r="{sz/2}"/></clipPath>'
        b += f'<circle cx="{x+sz/2}" cy="80" r="{sz/2}" fill="{C["noir"]}"/>'
        b += f'<g clip-path="url(#cl{sz}{id(icon_fn)})">{inner(icon_fn, "dark", x+sz*0.08, 80-sz/2+sz*0.08, sz*0.84)}</g></g>'
        x += sz + 26
    return svg(W, H, b)


def mock_story(fn):
    W, H = 270, 480
    b = f'<rect width="{W}" height="{H}" rx="18" fill="{C["noir"]}"/>'
    b += f'<rect x="20" y="14" width="230" height="3" rx="1.5" fill="#FFFFFF55"/><rect x="20" y="14" width="90" height="3" rx="1.5" fill="#fff"/>'
    b += f'<circle cx="135" cy="560" r="230" fill="{C["rouge"]}" opacity=".9"/>'
    b += f'<circle cx="135" cy="590" r="200" fill="{C["orange"]}"/>'
    b += inner(fn, "dark", 30, 80, 210, 190)
    b += slogan(135, 310, 12.5, C["or_"])
    d, _ = text_path(BC8, "COMMANDEZ EN LIGNE", 17, 135, 419, tracking=0.08, anchor="middle")
    b += f'<rect x="35" y="394" width="200" height="38" rx="19" fill="{C["noir"]}"/><path d="{d}" fill="{C["or_"]}"/>'
    return svg(W, H, b)


def small_test(icon_fn, logo_fn):
    W, H = 420, 110
    b = f'<rect width="{W}" height="{H}" fill="#fff"/>'
    x = 14
    for mode, bg in (("dark", C["noir"]), ("mono:#000000", "#fff"), ("mono:#FFFFFF", "#000")):
        for sz in (32, 16):
            b += f'<rect x="{x}" y="{55-sz/2}" width="{sz}" height="{sz}" fill="{bg}" stroke="#ddd" stroke-width=".5"/>'
            b += inner(icon_fn, mode, x, 55 - sz / 2, sz)
            x += sz + 10
        x += 14
    b += inner(logo_fn, "mono:#000000", x + 6, 25, 110, 60)
    return svg(W, H, b)


cards = []
for k, dct in DIRS.items():
    L, I = dct["logo"], dct["icon"]
    # sauvegarde des SVG de la direction
    open(f"{OUT}/directions/{k}-logo-couleur.svg", "w").write(standalone(L, "dark"))
    open(f"{OUT}/directions/{k}-logo-clair.svg", "w").write(standalone(L, "light"))
    open(f"{OUT}/directions/{k}-logo-noir.svg", "w").write(standalone(L, "mono:#000000"))
    open(f"{OUT}/directions/{k}-icone.svg", "w").write(standalone(I, "dark"))
    pitch = "".join(f"<li>{html.escape(p)}</li>" for p in dct["pitch"])
    cards.append(f"""
<section class="dir" id="dir-{k}">
  <header><span class="tag">Direction {k}</span><h2>{html.escape(dct['name'])}</h2></header>
  <ul class="pitch">{pitch}</ul>
  <div class="grid3">
    <figure class="on-dark">{standalone(L, 'dark')}<figcaption>Fond noir</figcaption></figure>
    <figure class="on-light">{standalone(L, 'light')}<figcaption>Fond blanc</figcaption></figure>
    <figure class="on-light">{standalone(L, 'mono:#000000')}<figcaption>Une couleur (noir pur)</figcaption></figure>
  </div>
  <h3>Mises en situation</h3>
  <div class="mocks">
    <figure class="wide">{mock_sign(L)}<figcaption>Enseigne façade</figcaption></figure>
    <figure>{mock_cup(L)}<figcaption>Gobelet</figcaption></figure>
    <figure>{mock_bag(L)}<figcaption>Sac kraft, tampon 1 couleur</figcaption></figure>
    <figure class="story">{mock_story(L)}<figcaption>Story Instagram</figcaption></figure>
    <figure class="wide">{mock_app(I)}<figcaption>Icône d’appli ronde : 120 / 64 / 48 / 32 px (taille réelle)</figcaption></figure>
    <figure class="wide">{small_test(I, L)}<figcaption>Test réel 32 px et 16 px : couleur, noir, blanc</figcaption></figure>
  </div>
</section>""")

palette = "".join(f'<div class="sw"><i style="background:{v}"></i><b>{n}</b><code>{v}</code></div>'
                  for n, v in (("Noir charbon", C["noir"]), ("Or chaud", C["or_"]), ("Rouge braise", C["rouge"]), ("Orange flamme", C["orange"])))

page = f"""<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Karibu Braise – Directions</title>
<style>
:root{{--noir:{C['noir']};--or:{C['or_']};--rouge:{C['rouge']};--orange:{C['orange']};--bg:#F4F1EC;--ink:#1C1714;--muted:#6b625a}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--ink);font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
.hero{{background:var(--noir);color:#F4EDE1;padding:40px 16px}}
.wrap{{max-width:1180px;margin:0 auto;padding:0 16px}}
.hero h1{{margin:0 0 8px;font-size:clamp(26px,4vw,40px);color:var(--or)}}
.hero p{{margin:0;max-width:760px;color:#d8cfc2}}
.pal{{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px}}
.sw{{display:flex;align-items:center;gap:8px;font-size:13px}} .sw i{{width:22px;height:22px;border-radius:50%;border:1px solid #ffffff33}} .sw code{{opacity:.7}}
nav{{position:sticky;top:0;background:#F4F1ECee;backdrop-filter:blur(6px);border-bottom:1px solid #e3dccf;z-index:2}}
nav .wrap{{display:flex;gap:18px;padding-top:10px;padding-bottom:10px;font-weight:600}} nav a{{color:var(--ink);text-decoration:none}} nav a:hover{{color:var(--rouge)}}
.dir{{padding:48px 0;border-bottom:1px solid #e3dccf}}
.tag{{display:inline-block;background:var(--rouge);color:#fff;font-weight:700;font-size:12px;letter-spacing:.08em;text-transform:uppercase;padding:3px 10px;border-radius:99px}}
h2{{margin:8px 0 6px;font-size:28px}} h3{{margin:32px 0 12px;font-size:16px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}}
.pitch{{margin:0 0 20px;padding-left:20px;max-width:860px}} .pitch li{{margin:4px 0}}
figure{{margin:0;border-radius:12px;overflow:hidden;background:#fff;box-shadow:0 1px 0 #00000010,0 4px 18px #0000000d}}
figure svg{{display:block;width:100%;height:auto}}
figcaption{{font-size:13px;color:var(--muted);padding:8px 12px;background:#fff}}
.grid3{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.grid3 figure svg{{padding:28px;aspect-ratio:4/3;object-fit:contain}}
.on-dark svg{{background:var(--noir)}} .on-light svg{{background:#fff}}
.mocks{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:start}}
.mocks .wide{{grid-column:span 2}} .mocks .story{{grid-row:span 2}}
.mocks figure:has(svg[viewBox="0 0 420 160"]) svg, .mocks figure:has(svg[viewBox="0 0 420 110"]) svg{{width:420px;max-width:100%}}
.choice{{padding:40px 0 60px}} .choice p{{max-width:760px}}
@media (max-width:860px){{.grid3{{grid-template-columns:1fr}}.mocks{{grid-template-columns:1fr 1fr}}.mocks .wide{{grid-column:span 2}}.mocks .story{{grid-row:auto}}}}
</style></head><body>
<div class="hero"><div class="wrap">
<h1>KARIBU BRAISE · 3 directions</h1>
<p>« Le feu de nos îles, le goût de l’Afrique. » : flamme + brochette, noir/or/rouge braise, une seule touche insulaire par direction. Tout est en aplats vectoriels (texte vectorisé, aucune image bitmap, aucun dégradé), et chaque version tient en 4 couleurs maximum.</p>
<div class="pal">{palette}</div>
</div></div>
<nav><div class="wrap"><a href="#dir-A">A · Emblème</a><a href="#dir-B">B · Monogramme</a><a href="#dir-C">C · Logotype</a></div></nav>
<main class="wrap">
{''.join(cards)}
<section class="choice"><h2>À toi de choisir</h2>
<p>Indique la direction retenue (A, B ou C), ou un mix (ex. : « le symbole de B avec la typo de C »). Je finaliserai ensuite le kit complet : logo empilé, horizontal, icône, versions blanc / noir / or, version avec slogan, PNG 512 / 1024 / 2048 et charte graphique.</p></section>
</main></body></html>"""
open(f"{OUT}/preview.html", "w").write(page)
print("ok", len(page) // 1024, "KB")
