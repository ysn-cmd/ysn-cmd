#!/usr/bin/env python3
# Generates an animated dark.svg GitHub profile hero banner (pure SMIL, no JS)
import html, json, os

_here = os.path.dirname(os.path.abspath(__file__))

# ASCII art (produced by make_ascii.py from the user's photo)
with open(os.path.join(_here, "ascii.json")) as f:
    ASCII_ART = json.load(f)

ROLES = ["Penetration Tester", "Red Teamer", "Security Researcher", "Software Engineer", "Software Intern"]

INFO = [
    ("~/university", "Konya Technical University"),
    ("~/role",       "VP, Cyber Security Community"),
    ("~/focus",      "Web Pentesting - Vuln Research - AI Red Teaming"),
    ("~/goal",       "OSCP+ Certification"),
    ("~/github",     "github.com/ysn-cmd"),
    ("~/linkedin",   "/in/yasin-bedirhan-rengul"),
]

SKILLS = ["Java", "JavaScript", "C", "Python", "Burp Suite", "Kali Linux",
          "PortSwigger", "Git", "VS Code", "Linux"]

PAL = dict(
    bg="#030712", panel="#0F172A", border="rgba(255,255,255,.08)",
    text="#F8FAFC", muted="#94A3B8",
    g1="#E5534B", g2="#56C2D6", g3="#D16FD1",
    glow1="#56C2D6", glow2="#E5534B", scan="rgba(86,194,214,.06)",
    pillfill="rgba(213,111,209,.10)",
)


def gen():
    p = PAL
    W, H = 1180, 640
    s = []
    A = s.append

    A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%" role="img" '
      f'aria-label="Yasin Bedirhan Rengul - offensive security profile banner" '
      f'font-family="\'JetBrains Mono\',\'Fira Code\',Consolas,monospace">')

    # ---- defs ----
    A('<defs>')
    A(f'<linearGradient id="acc" x1="0%" y1="0%" x2="100%" y2="0%">'
      f'<stop offset="0%" stop-color="{p["g1"]}"/><stop offset="50%" stop-color="{p["g2"]}"/><stop offset="100%" stop-color="{p["g3"]}"/>'
      f'<animate attributeName="x1" values="0%;-60%;0%" dur="9s" repeatCount="indefinite"/>'
      f'<animate attributeName="x2" values="100%;160%;100%" dur="9s" repeatCount="indefinite"/></linearGradient>')
    A(f'<linearGradient id="ascg" x1="0%" y1="0%" x2="100%" y2="100%">'
      f'<stop offset="0%" stop-color="{p["g2"]}"><animate attributeName="stop-color" values="{p["g2"]};{p["g1"]};{p["g3"]};{p["g2"]}" dur="12s" repeatCount="indefinite"/></stop>'
      f'<stop offset="100%" stop-color="{p["g1"]}"><animate attributeName="stop-color" values="{p["g1"]};{p["g3"]};{p["g2"]};{p["g1"]}" dur="12s" repeatCount="indefinite"/></stop></linearGradient>')
    A(f'<linearGradient id="shimmer" x1="0%" y1="0%" x2="100%" y2="0%">'
      f'<stop offset="0%" stop-color="{p["g1"]}" stop-opacity="0"/><stop offset="50%" stop-color="{p["g2"]}" stop-opacity=".9"/><stop offset="100%" stop-color="{p["g3"]}" stop-opacity="0"/>'
      f'<animate attributeName="x1" values="-100%;100%" dur="4s" repeatCount="indefinite"/>'
      f'<animate attributeName="x2" values="0%;200%" dur="4s" repeatCount="indefinite"/></linearGradient>')
    A(f'<radialGradient id="glowA" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{p["glow1"]}" stop-opacity=".14"/><stop offset="100%" stop-color="{p["glow1"]}" stop-opacity="0"/></radialGradient>')
    A(f'<radialGradient id="glowB" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{p["glow2"]}" stop-opacity=".12"/><stop offset="100%" stop-color="{p["glow2"]}" stop-opacity="0"/></radialGradient>')
    A(f'<radialGradient id="glowC" cx="50%" cy="50%" r="50%"><stop offset="0%" stop-color="{p["g3"]}" stop-opacity=".10"/><stop offset="100%" stop-color="{p["g3"]}" stop-opacity="0"/></radialGradient>')
    A('<filter id="tiny" x="-40%" y="-40%" width="180%" height="180%"><feGaussianBlur stdDeviation="0.6"/></filter>')
    A(f'<linearGradient id="glass" x1="0" y1="0" x2="0" y2="1"><stop offset="0%" stop-color="#fff" stop-opacity=".05"/><stop offset="18%" stop-color="#fff" stop-opacity="0"/></linearGradient>')

    # typing clips for rotating roles (generic for any number of roles)
    role_w = [len(r) * 8.6 for r in ROLES]
    N = len(ROLES)
    cyc = N * 4  # 4 "units" (seconds) per role: 1.4 type + 1.7 hold + 0.6 delete + 0.3 gap
    for i, w in enumerate(role_w):
        b = i * 4
        A(f'<clipPath id="role{i}"><rect x="512" y="188" height="26" width="0">'
          f'<animate attributeName="width" dur="{cyc}s" repeatCount="indefinite" calcMode="linear" '
          f'keyTimes="0;{b/cyc:.4f};{(b+1.4)/cyc:.4f};{(b+3.1)/cyc:.4f};{(b+3.7)/cyc:.4f};1" '
          f'values="0;0;{w:.0f};{w:.0f};0;0"/></rect></clipPath>')
    A('</defs>')

    # ---- background ----
    A(f'<rect width="{W}" height="{H}" rx="24" fill="{p["bg"]}"/>')
    A(f'<circle cx="200" cy="120" r="300" fill="url(#glowB)"><animateTransform attributeName="transform" type="translate" values="0 0;30 20;0 0" dur="14s" repeatCount="indefinite"/></circle>')
    A(f'<circle cx="980" cy="520" r="320" fill="url(#glowA)"><animateTransform attributeName="transform" type="translate" values="0 0;-25 -18;0 0" dur="17s" repeatCount="indefinite"/></circle>')
    A(f'<circle cx="620" cy="80" r="220" fill="url(#glowC)"><animateTransform attributeName="transform" type="translate" values="0 0;15 25;0 0" dur="12s" repeatCount="indefinite"/></circle>')

    for (cx, cy, r, dur, dy) in [(140,540,2,9,-70),(330,90,1.6,12,60),(700,560,2.2,11,-80),
                                  (900,120,1.5,10,70),(1080,320,1.8,13,-60),(60,320,1.4,8,50)]:
        A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{p["g2"]}" opacity=".35">'
          f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {dy};0 0" dur="{dur}s" repeatCount="indefinite"/>'
          f'<animate attributeName="opacity" values=".1;.5;.1" dur="{dur}s" repeatCount="indefinite"/></circle>')

    A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="23" fill="none" stroke="{p["border"]}" stroke-width="1.5"/>')
    A(f'<rect x="1.5" y="1.5" width="{W-3}" height="{H-3}" rx="23" fill="none" stroke="url(#shimmer)" stroke-width="1.5" opacity=".8"/>')

    # ===== LEFT PANEL (ASCII portrait) =====
    LP_X, LP_Y, LP_W, LP_H = 32, 32, 404, 576
    A('<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="7s" repeatCount="indefinite"/>')
    A(f'<rect x="{LP_X}" y="{LP_Y}" width="{LP_W}" height="{LP_H}" rx="18" fill="{p["panel"]}" stroke="{p["border"]}"/>')
    A(f'<rect x="{LP_X}" y="{LP_Y}" width="{LP_W}" height="{LP_H}" rx="18" fill="url(#glass)"/>')
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        A(f'<circle cx="{LP_X+24+i*22}" cy="{LP_Y+24}" r="6" fill="{c}" opacity=".9"/>')
    A(f'<text x="{LP_X+LP_W/2}" y="{LP_Y+29}" text-anchor="middle" font-size="12" fill="{p["muted"]}">yasin@ysn-cmd: ~/portrait</text>')

    n_rows = len(ASCII_ART)
    n_cols = max(len(l) for l in ASCII_ART)
    avail_w = LP_W - 28
    avail_h = LP_H - 92
    fs = min(avail_w / n_cols / 0.62, avail_h / n_rows / 1.18)
    lh = fs * 1.18
    y0 = LP_Y + 60

    for i, line in enumerate(ASCII_ART):
        t = html.escape(line).replace(" ", "&#160;")
        A(f'<text x="{LP_X+14}" y="{y0+i*lh:.1f}" font-size="{fs:.2f}" xml:space="preserve" fill="url(#ascg)" filter="url(#tiny)" opacity="0">'
          f'<animate attributeName="opacity" values="0;1" dur=".15s" begin="{0.3+i*0.05:.2f}s" fill="freeze"/>{t}</text>')

    A(f'<rect x="{LP_X+2}" y="{LP_Y+2}" width="{LP_W-4}" height="24" fill="{p["scan"]}">'
      f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {LP_H-4};0 0" dur="6.5s" repeatCount="indefinite"/></rect>')
    A(f'<rect x="{LP_X+18}" y="{LP_Y+LP_H-24}" width="9" height="15" fill="{p["g2"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')
    A('</g>')

    # ===== RIGHT PANEL (terminal) =====
    RP_X, RP_Y, RP_W, RP_H = 460, 32, 688, 576
    A(f'<rect x="{RP_X}" y="{RP_Y}" width="{RP_W}" height="{RP_H}" rx="18" fill="{p["panel"]}" stroke="{p["border"]}"/>')
    A(f'<rect x="{RP_X}" y="{RP_Y}" width="{RP_W}" height="{RP_H}" rx="18" fill="url(#glass)"/>')
    for i, c in enumerate(["#FF5F57", "#FEBC2E", "#28C840"]):
        A(f'<circle cx="{RP_X+26+i*22}" cy="{RP_Y+24}" r="6" fill="{c}" opacity=".9"/>')
    A(f'<text x="{RP_X+RP_W/2}" y="{RP_Y+29}" text-anchor="middle" font-size="12" fill="{p["muted"]}">ysn-cmd &#8212; zsh &#8212; 120x34</text>')

    def reveal(el, t):
        return el.replace("<text ", '<text opacity="0" ', 1).replace(
            "</text>", f'<animate attributeName="opacity" values="0;1" dur=".5s" begin="{t}s" fill="freeze"/></text>')

    A(reveal(f'<text x="492" y="112" font-size="15" fill="{p["muted"]}">$ whoami</text>', 0.4))
    A(reveal(f'<text x="492" y="152" font-size="32" font-weight="700" fill="{p["text"]}">'
              f'Hi &#128075; I&#8217;m <tspan fill="url(#acc)">Yasin</tspan></text>', 0.8))

    A(f'<text x="492" y="207" font-size="17" fill="{p["muted"]}">&gt;</text>')
    for i, r in enumerate(ROLES):
        A(f'<g clip-path="url(#role{i})"><text x="512" y="208" font-size="17" fill="url(#acc)" font-weight="600">{html.escape(r)}</text></g>')

    # generic cursor-position animation matching the per-role type/hold/delete/gap keyframes
    kt_list = [0.0]
    vals_list = ["0 0"]
    for i, w in enumerate(role_w):
        b = i * 4
        ta, tb, tc, td = b / cyc, (b + 1.4) / cyc, (b + 3.1) / cyc, (b + 3.7) / cyc
        if i > 0:
            kt_list.append(ta); vals_list.append("0 0")
        kt_list.append(tb); vals_list.append(f"{w:.0f} 0")
        kt_list.append(tc); vals_list.append(f"{w:.0f} 0")
        kt_list.append(td); vals_list.append("0 0")
    kt_list.append(1.0)
    vals_list.append("0 0")
    kt = ";".join(f"{v:.5f}" for v in kt_list)
    vals = ";".join(vals_list)

    A(f'<rect x="512" y="193" width="9" height="19" fill="{p["g2"]}"><animate attributeName="opacity" values="1;0;1" dur=".9s" repeatCount="indefinite"/>'
      f'<animateTransform attributeName="transform" type="translate" dur="{cyc}s" repeatCount="indefinite" calcMode="linear" keyTimes="{kt}" values="{vals}"/></rect>')

    y = 258
    for i, (k, v) in enumerate(INFO):
        A(reveal(f'<text x="492" y="{y}" font-size="14"><tspan fill="{p["g2"]}">{k}</tspan>'
                  f'<tspan fill="{p["muted"]}" dx="10">&#8594;</tspan>'
                  f'<tspan fill="{p["text"]}" dx="10">{html.escape(v)}</tspan></text>', 1.4 + i * 0.3))
        y += 27

    A(reveal(f'<text x="492" y="{y+16}" font-size="13" fill="{p["muted"]}" letter-spacing="2">SKILLS</text>', 3.0))
    px, py = 492, y + 34
    t0 = 3.2
    right_edge = RP_X + RP_W - 24
    for i, sk in enumerate(SKILLS):
        w = len(sk) * 7.6 + 26
        if px + w > right_edge:
            px = 492
            py += 40
        A(f'<g opacity="0"><animate attributeName="opacity" values="0;1" dur=".4s" begin="{t0+i*0.12:.2f}s" fill="freeze"/>'
          f'<rect x="{px:.0f}" y="{py}" width="{w:.0f}" height="28" rx="14" fill="{p["pillfill"]}" stroke="url(#acc)" stroke-width="1">'
          f'<animate attributeName="stroke-width" values="1;1.6;1" dur="3s" begin="{i*0.4:.1f}s" repeatCount="indefinite"/></rect>'
          f'<text x="{px+w/2:.0f}" y="{py+19}" text-anchor="middle" font-size="13" fill="{p["text"]}">{html.escape(sk)}</text></g>')
        px += w + 12
    py += 40

    sy = max(py + 30, RP_Y + RP_H - 34)
    A(reveal(f'<text x="492" y="{sy}" font-size="14"><tspan fill="{p["muted"]}">$ connect --with</tspan>'
              f'<tspan dx="14" fill="url(#acc)" font-weight="600">GitHub</tspan>'
              f'<tspan dx="16" fill="{p["muted"]}">&#183;</tspan>'
              f'<tspan dx="16" fill="url(#acc)" font-weight="600">LinkedIn</tspan></text>', 5.0))
    A(f'<rect x="756" y="{sy-13}" width="9" height="15" fill="{p["g2"]}"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>')

    A(f'<rect x="{RP_X+2}" y="{RP_Y+2}" width="{RP_W-4}" height="20" fill="{p["scan"]}">'
      f'<animateTransform attributeName="transform" type="translate" values="0 0;0 {RP_H-4};0 0" dur="9s" repeatCount="indefinite"/></rect>')

    A('</svg>')
    H_final = int(max(H, sy + 40))
    svg = "".join(s)
    if H_final != H:
        svg = svg.replace(f'viewBox="0 0 {W} {H}"', f'viewBox="0 0 {W} {H_final}"', 1)
        svg = svg.replace(f'<rect width="{W}" height="{H}" rx="24"', f'<rect width="{W}" height="{H_final}" rx="24"', 1)
    return svg


if __name__ == "__main__":
    out = gen()
    with open(os.path.join(_here, "dark.svg"), "w", encoding="utf-8") as f:
        f.write(out)
    print("wrote dark.svg,", len(ASCII_ART), "ascii lines")
