"""Draw the five manoeuvre diagrams using JSSDM 2022 Section 17 army symbols only.

Colours per para 1704: blue = own, red = enemy, green = obstacles/demolitions,
black = grid/superscription and explanatory notes. Writes svg/<name>.svg.
"""
import math
import os

BLUE, RED, GREEN, BLACK = "#1546b0", "#d0231b", "#137a2c", "#222"
W, H = 800, 460
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")


def f(v):
    return f"{v:.1f}"


# ---------- terrain ----------
def base(title):
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" role="img" aria-label="{title}" font-family="Arial, Helvetica, sans-serif">',
         f'<rect width="{W}" height="{H}" fill="#f6f6f0"/>']
    for x in range(0, W + 1, 80):  # grid lines in black (1704e)
        s.append(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="{BLACK}" stroke-opacity=".07"/>')
    for y in range(0, H + 1, 80):
        s.append(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{BLACK}" stroke-opacity=".07"/>')
    return s


def road(d):
    return (f'<path d="{d}" fill="none" stroke="#9a968a" stroke-width="7" stroke-linecap="round"/>'
            f'<path d="{d}" fill="none" stroke="#f6f6f0" stroke-width="4" stroke-linecap="round"/>')


def river(d):
    return f'<path d="{d}" fill="none" stroke="#b9d2dc" stroke-width="14" stroke-linecap="round"/>'


def note(x, y, txt, anchor="middle", size=11):
    """Explanatory note (not a symbol) - black, italic."""
    return f'<text x="{x}" y="{y}" font-size="{size}" font-style="italic" fill="#555" text-anchor="{anchor}" stroke="#f6f6f0" stroke-width="3" paint-order="stroke">{txt}</text>'


def label(x, y, txt, color, anchor="start", size=11, weight="700"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}" text-anchor="{anchor}" stroke="#fff" stroke-width="3" paint-order="stroke">{txt}</text>'


# ---------- unit symbols (1706, Annex A, Annex B) ----------
def unit(cx, cy, color, role="inf", size="II", right="", left="", w=44, h=28, dashed=False):
    x, y = cx - w / 2, cy - h / 2
    da = ' stroke-dasharray="4 3"' if dashed else ""
    s = [f'<rect x="{f(x)}" y="{f(y)}" width="{w}" height="{h}" fill="#fff" stroke="{color}" stroke-width="2"{da}/>']
    if role in ("inf", "mech", "airmob"):  # Annex A ser 9: diagonals
        s.append(f'<path d="M{f(x)} {f(y)}L{f(x+w)} {f(y+h)}M{f(x+w)} {f(y)}L{f(x)} {f(y+h)}" stroke="{color}" stroke-width="1.6"{da}/>')
    if role in ("armd", "mech"):  # Annex A ser 4 / functions ser 7: ellipse
        s.append(f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{w*.3:.1f}" ry="{h*.24:.1f}" fill="#fff" stroke="{color}" stroke-width="1.6"/>')
    if role == "airmob":  # Annex A functions ser 2: line with V notch
        ly = y + h * .28
        s.append(f'<path d="M{f(x)} {f(ly)}H{f(cx-5)}L{f(cx)} {f(ly+5)}L{f(cx+5)} {f(ly)}H{f(x+w)}" fill="none" stroke="{color}" stroke-width="1.6"/>')
    if role == "arty":  # Annex A ser 5: dot
        s.append(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="4" fill="{color}"/>')
    if size:  # Annex B: size indicator on top
        s.append(label(cx, y - 4, size, color, "middle", 10))
    if right:
        s.append(label(x + w + 4, cy + 4, right, color, "start", 10))
    if left:
        s.append(label(x - 4, cy + 4, left, color, "end", 10))
    return "".join(s)


def hq(cx, cy, color, size="X", right=""):
    """1706b: HQ = unit box on a staff; location at foot of staff (1719a)."""
    w, h = 40, 24
    x, y = cx, cy - 40
    return (f'<path d="M{f(x)} {f(cy)}V{f(y)}" stroke="{color}" stroke-width="2"/>'
            f'<rect x="{f(x)}" y="{f(y)}" width="{w}" height="{h}" fill="#fff" stroke="{color}" stroke-width="2"/>'
            + label(x + w / 2, y - 4, size, color, "middle", 10)
            + (label(x + w + 4, y + 16, right, color, "start", 10) if right else ""))


def goose(cx, cy, rx, ry, color, size="", text="", dashed=False, sw=2):
    """1709a: area in a state of defence - size indicator on the line. 17F para 5: usage text inside."""
    da = ' stroke-dasharray="7 5"' if dashed else ""
    s = [f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{rx}" ry="{ry}" fill="none" stroke="{color}" stroke-width="{sw}"{da}/>']
    if size:
        s.append(f'<rect x="{f(cx-9)}" y="{f(cy-ry-7)}" width="18" height="12" fill="#f6f6f0"/>')
        s.append(label(cx, cy - ry + 4, size, color, "middle", 10))
    if text:
        tw = 7.6 * len(text) + 8
        s.append(f'<rect x="{f(cx-tw/2)}" y="{f(cy-8)}" width="{f(tw)}" height="16" fill="#f6f6f0"/>')
        s.append(label(cx, cy + 4, text, color, "middle", 11))
    return "".join(s)


def strong_point(cx, cy, rx, ry, color, size="", right=""):
    """17F para 6c: strong point - outline with outward spikes."""
    s = [f'<rect x="{f(cx-rx)}" y="{f(cy-ry)}" width="{2*rx}" height="{2*ry}" rx="{ry}" fill="none" stroke="{color}" stroke-width="2.2"/>']
    for a in (200, 160, 20, -20, 250, 290, 110, 70):
        r = math.radians(a)
        px, py = cx + (rx - 4) * math.cos(r), cy - ry * math.sin(r)
        qx, qy = cx + (rx + 12) * math.cos(r), cy - (ry + 12) * math.sin(r)
        s.append(f'<line x1="{f(px)}" y1="{f(py)}" x2="{f(qx)}" y2="{f(qy)}" stroke="{color}" stroke-width="2"/>')
    if size:
        s.append(label(cx, cy - ry - 16, size, color, "middle", 10))
    if right:
        s.append(label(cx + rx + 16, cy + 4, right, color, "start", 10))
    return "".join(s)


def op(cx, cy, color, arty=False):
    """1706c: observation post (triangle); own artillery OP has a dot."""
    s = f'<path d="M{f(cx)} {f(cy-11)}L{f(cx+10)} {f(cy+7)}L{f(cx-10)} {f(cy+7)}Z" fill="#fff" stroke="{color}" stroke-width="2"/>'
    if arty:
        s += f'<circle cx="{f(cx)}" cy="{f(cy+1)}" r="2.2" fill="{color}"/>'
    return s


def jam(cx, cy, color):
    """Annex E, activities ser 4: jamming - inverted triangle with zigzag."""
    zz = " ".join(f"L{f(cx-11+i*3.67)} {f(cy-11+(4 if i % 2 else 0))}" for i in range(7))
    return (f'<path d="M{f(cx-15)} {f(cy-16)}H{f(cx+15)}L{f(cx)} {f(cy+12)}Z" fill="#fff" stroke="{color}" stroke-width="2"/>'
            f'<path d="M{f(cx-11)} {f(cy-11)}{zz}" fill="none" stroke="{color}" stroke-width="1.5"/>')


# ---------- fire planning (17F paras 7-10) ----------
def conc(cx, cy, color):
    return f'<path d="M{f(cx-9)} {f(cy)}H{f(cx+9)}M{f(cx)} {f(cy-9)}V{f(cy+9)}" stroke="{color}" stroke-width="2"/>'


def linear_conc(x1, y1, x2, y2, color):
    ang = math.atan2(y2 - y1, x2 - x1)
    nx, ny = -math.sin(ang) * 8, math.cos(ang) * 8
    mx, my = (x1 + x2) / 2, (y1 + y2) / 2
    return (f'<path d="M{f(x1)} {f(y1)}L{f(x2)} {f(y2)}M{f(x1-nx)} {f(y1-ny)}L{f(x1+nx)} {f(y1+ny)}'
            f'M{f(x2-nx)} {f(y2-ny)}L{f(x2+nx)} {f(y2+ny)}" stroke="{color}" stroke-width="2"/>'
            f'<circle cx="{f(mx)}" cy="{f(my)}" r="4.5" fill="{color}"/>')


def arc_of_fire(x, y, a1, a2, length, color):
    """17F para 10a: broken lines either side with arrowheads."""
    s = []
    for a in (a1, a2):
        r = math.radians(a)
        ex, ey = x + length * math.cos(r), y + length * math.sin(r)
        s.append(f'<line x1="{f(x)}" y1="{f(y)}" x2="{f(ex)}" y2="{f(ey)}" stroke="{color}" stroke-width="1.5" stroke-dasharray="5 4"/>')
        s.append(head(ex, ey, r, color, 7))
    return "".join(s)


def firing_position(cx, cy, ang, color, w=30, depth=7):
    """17F para 6b: firing position - bracket oriented in the direction of firing.
    (cx, cy) is the centre of the bracket's front bar; ang is the firing direction in degrees (0 = east, 90 = south)."""
    r = math.radians(ang)
    fx, fy = math.cos(r), math.sin(r)          # direction of fire
    px, py = -fy * w / 2, fx * w / 2            # half-width along the bar
    bx, by = -fx * depth, -fy * depth           # short legs back towards the unit
    return (f'<path d="M{f(cx+px+bx)} {f(cy+py+by)}L{f(cx+px)} {f(cy+py)}L{f(cx-px)} {f(cy-py)}L{f(cx-px+bx)} {f(cy-py+by)}" '
            f'fill="none" stroke="{color}" stroke-width="2"/>')


def head(x, y, ang, color, size=8):
    lx, ly = x - size * math.cos(ang - .45), y - size * math.sin(ang - .45)
    rx, ry = x - size * math.cos(ang + .45), y - size * math.sin(ang + .45)
    return f'<path d="M{f(lx)} {f(ly)}L{f(x)} {f(y)}L{f(rx)} {f(ry)}" fill="none" stroke="{color}" stroke-width="1.8"/>'


# ---------- obstacles (green) ----------
def roadblock(cx, cy, ang=0):
    """17F para 25c: road block completed - two crossed pairs of lines."""
    s = []
    for a in (45 + ang, -45 + ang):
        r = math.radians(a)
        dx, dy = 13 * math.cos(r), 13 * math.sin(r)
        nx, ny = -math.sin(r) * 3, math.cos(r) * 3
        for k in (-1, 1):
            s.append(f'<line x1="{f(cx-dx+k*nx)}" y1="{f(cy-dy+k*ny)}" x2="{f(cx+dx+k*nx)}" y2="{f(cy+dy+k*ny)}" stroke="{GREEN}" stroke-width="2"/>')
    return "".join(s)


def demolition_fired(cx, cy, r=13):
    """17F para 31d: demolition executed/fired - circle with crossed double lines."""
    s = [f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{r}" fill="#fff" stroke="{GREEN}" stroke-width="2"/>']
    for a in (45, -45):
        rr = math.radians(a)
        dx, dy = (r - 1) * math.cos(rr), (r - 1) * math.sin(rr)
        nx, ny = -math.sin(rr) * 2.5, math.cos(rr) * 2.5
        for k in (-1, 1):
            s.append(f'<line x1="{f(cx-dx+k*nx)}" y1="{f(cy-dy+k*ny)}" x2="{f(cx+dx+k*nx)}" y2="{f(cy+dy+k*ny)}" stroke="{GREEN}" stroke-width="1.6"/>')
    return "".join(s)


def tank_obstacle(pts):
    """17F para 23c: tank obstacle, type unspecified - line with diamonds."""
    d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts)
    out = [f'<path d="{d}" fill="none" stroke="{GREEN}" stroke-width="2"/>']
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        out.append(f'<path d="M{f(mx-9)} {f(my)}L{f(mx)} {f(my-11)}L{f(mx+9)} {f(my)}L{f(mx)} {f(my+11)}Z" fill="#fff" stroke="{GREEN}" stroke-width="2"/>')
    return "".join(out)


# ---------- lines ----------
def front_line(pts, color, bulge=1, step=16):
    """17F para 3a: front line - curved scallops, convex side towards the opposing force."""
    d = [f"M{f(pts[0][0])} {f(pts[0][1])}"]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        L = math.hypot(x2 - x1, y2 - y1)
        n = max(1, round(L / step))
        for i in range(1, n + 1):
            px, py = x1 + (x2 - x1) * i / n, y1 + (y2 - y1) * i / n
            d.append(f"A{step*.55:.1f} {step*.55:.1f} 0 0 {1 if bulge > 0 else 0} {f(px)} {f(py)}")
    return f'<path d="{"".join(d)}" fill="none" stroke="{color}" stroke-width="2"/>'


def ring_front(cx, cy, rx, ry, color, n=60, inward=True):
    pts = [(cx + rx * math.cos(2 * math.pi * i / n), cy + ry * math.sin(2 * math.pi * i / n)) for i in range(n + 1)]
    return front_line(pts, color, -1 if inward else 1, step=14)


def route(pts, color, dashed=False):
    """1710 / 17F para 14a: movement on a route - single arrow. Broken = projected (1714)."""
    d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts)
    da = ' stroke-dasharray="6 4"' if dashed else ""
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    return (f'<path d="{d}" fill="none" stroke="{color}" stroke-width="2"{da}/>'
            + head(x2, y2, math.atan2(y2 - y1, x2 - x1), color, 10))


def bez(p0, p1, p2, p3, t):
    u = 1 - t
    return (u**3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t**3 * p3[0],
            u**3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t**3 * p3[1])


def axis(p0, p1, p2, p3, color, width=18, main=False, repulsed_by=None, halted_by=None, dashed=False, letter=""):
    """17F para 14b axis of advance (hollow arrow); 14g main effort (double head);
    14e attack repulsed (X of the other side at the tip); 14f attack halted (bar)."""
    N = 60
    pts = [bez(p0, p1, p2, p3, i / N) for i in range(N + 1)]
    seg = [math.hypot(pts[i + 1][0] - pts[i][0], pts[i + 1][1] - pts[i][1]) for i in range(N)]
    total, hl = sum(seg), width * 1.5
    acc, cut = 0, N
    for i, sl in enumerate(seg):
        if acc + sl >= total - hl:
            cut = i
            break
        acc += sl
    left, right = [], []
    for i in range(cut + 1):
        a, b = pts[max(i - 1, 0)], pts[min(i + 1, N)]
        ang = math.atan2(b[1] - a[1], b[0] - a[0])
        nx, ny = -math.sin(ang) * width / 2, math.cos(ang) * width / 2
        left.append((pts[i][0] + nx, pts[i][1] + ny))
        right.append((pts[i][0] - nx, pts[i][1] - ny))
    bx, by = pts[cut]
    tip = pts[-1]
    ang = math.atan2(tip[1] - by, tip[0] - bx)
    hx, hy = -math.sin(ang) * width, math.cos(ang) * width
    poly = left + [(bx + hx, by + hy), tip, (bx - hx, by - hy)] + right[::-1]
    d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in poly) + "Z"
    da = ' stroke-dasharray="7 4"' if dashed else ""
    s = [f'<path d="{d}" fill="#fff" fill-opacity=".85" stroke="{color}" stroke-width="2.2" stroke-linejoin="round"{da}/>']
    if main:  # second, offset arrowhead
        o = 9
        ox, oy = math.cos(ang) * o, math.sin(ang) * o
        s.append(f'<path d="M{f(bx+hx*1.15+ox)} {f(by+hy*1.15+oy)}L{f(tip[0]+ox*1.3)} {f(tip[1]+oy*1.3)}L{f(bx-hx*1.15+ox)} {f(by-hy*1.15+oy)}" fill="none" stroke="{color}" stroke-width="2.2" stroke-linejoin="miter"/>')
    if repulsed_by:
        tx, ty = tip
        s.append(f'<path d="M{f(tx-11)} {f(ty-11)}L{f(tx+11)} {f(ty+11)}M{f(tx+11)} {f(ty-11)}L{f(tx-11)} {f(ty+11)}" stroke="{repulsed_by}" stroke-width="2.6"/>')
    if halted_by:
        tx, ty = tip
        nx, ny = -math.sin(ang) * 16, math.cos(ang) * 16
        s.append(f'<line x1="{f(tx+nx)}" y1="{f(ty+ny)}" x2="{f(tx-nx)}" y2="{f(ty-ny)}" stroke="{halted_by}" stroke-width="2.6"/>')
    if letter:
        mx, my = pts[N // 2]
        s.append(label(mx, my + 4, letter, color, "middle", 11))
    return "".join(s)


def finish(s):
    s.append("</svg>")
    return "\n".join(s)


# ======================= diagrams =======================
def envelopment():
    s = base("Single envelopment drawn with JSSDM Section 17 symbols")
    s.append(road("M0 330 C 200 320, 400 300, 800 310"))
    s.append(road("M470 0 C 470 60, 480 120, 480 300"))
    # enemy main position: front line convex towards own troops (17F 3a), coy defended areas (1709a)
    s.append(front_line([(250, 225), (720, 225)], RED, bulge=-1))
    s.append(goose(340, 190, 55, 26, RED, "I", "A"))
    s.append(goose(480, 190, 55, 26, RED, "I", "B"))
    s.append(goose(620, 190, 55, 26, RED, "I", "C"))
    s.append(hq(520, 150, RED, "II", "4 EN"))
    s.append(note(232, 180, "ASSAILABLE", "end"))
    s.append(note(232, 194, "FLANK", "end"))
    # secondary attack on the front; main effort round the flank to OBJ in the rear on the escape route
    s.append(unit(560, 420, BLUE, "inf", "I", "B"))
    s.append(axis((560, 388), (560, 340), (545, 290), (540, 242), BLUE, width=16))
    s.append(note(580, 350, "SECONDARY ATTK", "start"))
    s.append(unit(150, 420, BLUE, "mech", "II", "2 EB"))
    s.append(axis((150, 386), (40, 250), (110, 50), (410, 60), BLUE, width=22, main=True))
    s.append(goose(470, 62, 44, 22, BLUE, "", "OBJ"))
    s.append(note(560, 50, "IN REAR, ON EN", "start"))
    s.append(note(560, 64, "ESCAPE ROUTE", "start"))
    s.append(note(128, 305, "MAIN EFFORT", "start"))
    s.append(note(400, 452, "MAIN EFFORT AGAINST THE FLANK, TOWARDS AN OBJ IN THE REAR THAT CUTS HIS ROUTES OF ESCAPE.", "middle"))
    return finish(s)


def double_envelopment():
    s = base("Double envelopment drawn with JSSDM Section 17 symbols")
    s.append(road("M400 0 V460"))
    s.append(front_line([(240, 235), (560, 235)], RED, bulge=-1))
    s.append(goose(330, 200, 55, 26, RED, "I", "A"))
    s.append(goose(470, 200, 55, 26, RED, "I", "B"))
    s.append(hq(560, 175, RED, "II", "4 EN"))
    s.append(unit(400, 420, BLUE, "inf", "I", "B"))
    s.append(axis((400, 388), (400, 340), (400, 290), (400, 252), BLUE, width=16))
    s.append(note(430, 320, "SECONDARY ATTK", "start"))
    s.append(unit(110, 420, BLUE, "mech", "II", "2 EB"))
    s.append(axis((110, 386), (30, 230), (120, 80), (330, 90), BLUE, width=20, main=True))
    s.append(unit(690, 420, BLUE, "armd", "II", "7 H"))
    s.append(axis((690, 386), (770, 230), (680, 80), (470, 90), BLUE, width=20, main=True))
    s.append(goose(400, 90, 44, 22, BLUE, "", "OBJ"))
    s.append(note(400, 452, "BOTH FLANKS DEALT WITH SIMULTANEOUSLY. NEEDS ADEQUATE TROOPS AND PRECISE TIMING.", "middle"))
    return finish(s)


def turning():
    s = base("Turning movement drawn with JSSDM Section 17 symbols")
    # terrain: en L of C runs from his position to the rear (north); lateral road gives the xrd
    s.append(road("M330 460 C 330 380, 330 300, 330 230 C 340 160, 420 110, 560 70 L 800 40"))
    s.append(road("M470 0 C 520 40, 560 70, 600 110 S 720 200, 800 230"))
    # en principal def posns: front line convex towards own tps, coy def areas, bde HQ
    s.append(front_line([(60, 300), (560, 300)], RED, bulge=-1))
    for x, t in ((120, "A"), (240, "B"), (380, "C"), (500, "D")):
        s.append(goose(x, 268, 50, 22, RED, "I", t))
    s.append(hq(110, 222, RED, "X", "9 EN"))
    # OBJ: xrd deep in en rear, on his L of C
    s.append(goose(560, 72, 46, 26, BLUE, "", "OBJ"))
    s.append(note(612, 18, "XRD ON EN L OF C,", "start"))
    s.append(note(612, 32, "DEEP IN HIS REAR", "start"))
    # turning force passes round, clear of the en main force
    s.append(unit(720, 425, BLUE, "armd", "X", "10 ARMD", w=44, h=26))
    s.append(axis((720, 398), (790, 300), (770, 180), (612, 92), BLUE, width=22, main=True))
    s.append(note(728, 320, "PASSES AROUND", "end"))
    # secondary attk on his front (OW fig 12.2)
    s.append(unit(440, 425, BLUE, "inf", "I", "C", w=44, h=26))
    s.append(axis((440, 398), (440, 360), (440, 335), (440, 316), BLUE, width=14))
    s.append(note(462, 365, "SECONDARY ATTK", "start"))
    # en projected moves (broken, 1714): abandon posn / divert maj forces to meet the threat
    s.append(route([(380, 244), (420, 170), (520, 100)], RED, dashed=True))
    s.append(route([(500, 244), (540, 180), (575, 108)], RED, dashed=True))
    s.append(note(398, 182, "EN FORCED TO ABANDON", "end"))
    s.append(note(398, 196, "POSN OR DIVERT MAJ FORCES", "end"))
    s.append(note(400, 452, "MAIN EFFORT AVOIDS EN MAIN FORCE; SECURES AN OBJ DEEP IN HIS REAR / ON HIS L OF C.", "middle"))
    return finish(s)


def encirclement():
    s = base("Encirclement drawn with JSSDM Section 17 symbols")
    cx, cy = 400, 235
    for d in ("M400 0 V460", "M0 235 H800", "M120 20 L680 450", "M690 20 L110 450"):
        s.append(road(d))
    # enemy force in the pocket
    s.append(goose(cx, cy, 70, 42, RED, "X", "7 EN"))
    # own front line forms a closed ring, convex towards the enemy (inward)
    s.append(ring_front(cx, cy, 200, 150, BLUE))
    for a, t in ((-90, "1"), (-20, "2"), (40, "3"), (110, "4"), (170, "5"), (225, "6")):
        r = math.radians(a)
        ux, uy = cx + 238 * math.cos(r), cy + 182 * math.sin(r)
        s.append(unit(ux, uy, BLUE, "inf", "II", t + " EB", w=36, h=22))
    # every ground route blocked where it meets the ring
    for x, y, a in ((400, 85, 0), (400, 385, 0), (200, 235, 90), (600, 235, 90),
                    (259, 128, 37), (541, 342, 37), (539, 130, -37), (262, 340, -37)):
        s.append(roadblock(x, y, a))
    # breakout and relief attempts repulsed
    s.append(axis((440, 250), (500, 290), (540, 320), (560, 330), RED, width=12, repulsed_by=BLUE))
    s.append(axis((790, 40), (740, 60), (690, 90), (650, 120), RED, width=12, repulsed_by=BLUE))
    s.append(note(700, 30, "EN RELIEF ATTEMPT", "middle"))
    s.append(note(520, 272, "BREAKOUT", "start"))
    s.append(note(400, 452, "ALL GRD ROUTES OF EVACUATION AND RFT CTRL BY OWN TROOPS.", "middle"))
    return finish(s)


def investment():
    s = base("Investment drawn with JSSDM Section 17 symbols")
    cx, cy = 360, 225
    for d in ("M360 0 V460", "M0 225 H800", "M90 30 L640 440"):
        s.append(road(d))
    # enemy garrison in a strong point (the town), future OBJ in broken line (1714)
    s.append(strong_point(cx, cy, 60, 32, RED, "II", ""))
    s.append(label(cx, cy + 56, "TOWN", RED, "middle", 11))
    s.append(goose(cx, cy, 110, 70, BLUE, "", "", dashed=True, sw=1.6))
    s.append(label(cx + 118, cy - 52, "OBJ", BLUE, "start", 11))
    # minor opposition: en outposts being driven in
    s.append(unit(150, 105, RED, "inf", "●●●", "", w=32, h=20))
    s.append(axis((110, 150), (120, 130), (130, 120), (145, 115), BLUE, width=10))
    s.append(unit(560, 340, RED, "inf", "●●●", "", w=32, h=20))
    s.append(axis((600, 380), (590, 365), (580, 355), (570, 350), BLUE, width=10))
    s.append(note(150, 80, "OUTPOSTS DRIVEN IN", "middle"))
    # own companies all round, dominating by fire and observation
    for (ux, uy, t, a1, a2) in ((360, 70, "A", 70, 110), (560, 170, "B", 160, 200), (360, 390, "C", 250, 290),
                                (160, 280, "D", -20, 20), (170, 150, "E", 10, 45)):
        s.append(unit(ux, uy, BLUE, "inf", "I", t, w=34, h=22))
        s.append(arc_of_fire(ux, uy, a1, a2, 85, BLUE))
    s.append(op(250, 120, BLUE, arty=True))
    s.append(op(470, 330, BLUE, arty=True))
    s.append(op(480, 120, BLUE))
    for x, y in ((325, 225), (395, 225)):
        s.append(conc(x, y, BLUE))
        # mobile reserve facing outward; enemy relief column repulsed
    s.append(unit(640, 260, BLUE, "armd", "I", ""))
    s.append(label(640, 300, "(MOBILE RES)", BLUE, "middle", 10))
    s.append(axis((790, 300), (760, 290), (735, 275), (700, 266), RED, width=14, repulsed_by=BLUE))
    s.append(note(735, 330, "EN RELIEF FORCE", "middle"))
    s.append(note(400, 452, "ISOLATE, DOMINATE BY FIRE AND OBSN, DRIVE IN OUTPOSTS, HOLD A MOBILE RES, THEN CAPR.", "middle"))
    return finish(s)


def minefield(pts):
    """17F para 29b(1): unfenced minefield boundary, drawn to scale, letter M in the line."""
    d = "M" + " L".join(f"{f(x)} {f(y)}" for x, y in pts) + "Z"
    out = [f'<path d="{d}" fill="none" stroke="{GREEN}" stroke-width="2"/>']
    for (x1, y1), (x2, y2) in zip(pts, pts[1:] + pts[:1]):
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2
        out.append(f'<rect x="{f(mx-7)}" y="{f(my-7)}" width="14" height="14" fill="#f6f6f0"/>')
        out.append(f'<text x="{f(mx)}" y="{f(my+5)}" font-size="13" font-weight="700" fill="{GREEN}" text-anchor="middle">M</text>')
    return "".join(out)


def hill(cx, cy, rx, ry):
    """Base-map relief (not a symbol)."""
    return "".join(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx*k:.0f}" ry="{ry*k:.0f}" fill="none" stroke="#b9ae93" stroke-width="1.2"/>' for k in (1, .7, .4))


def isolation():
    s = base("Isolation drawn with JSSDM Section 17 symbols")
    # relief forming a defile on the eastern route
    s.append(hill(660, 250, 70, 46))
    s.append(hill(790, 250, 60, 46))
    # river between the en fwd fmn and his depth
    s.append(river("M0 170 C 160 150, 300 200, 450 175 S 680 140, 800 160"))
    # routes from his depth to the fwd fmn: two bridges and one defile
    s.append(road("M200 0 C 210 80, 230 170, 270 300"))
    s.append(road("M560 0 C 540 80, 520 160, 380 300"))
    s.append(road("M800 90 C 760 140, 730 210, 728 260 C 720 320, 560 330, 420 320"))
    # en fwd fmn being isolated - in contact to its front, NOT surrounded
    s.append(goose(330, 305, 80, 40, RED, "X", "5 EN"))
    s.append(front_line([(220, 360), (450, 360)], RED, bulge=-1))
    s.append(unit(330, 425, BLUE, "inf", "X", "OWN BDE", w=44, h=26))
    # en fol-up fmn in depth; its projected move (1714) towards the fwd fmn
    s.append(unit(640, 40, RED, "armd", "X", "EN FOL-UP FMN", w=44, h=26))
    s.append(route([(616, 40), (562, 14), (554, 24), (547, 48), (539, 74), (528, 100), (512, 130), (502, 148)], RED, dashed=True))
    # bridges destroyed (17F 31d)
    s.append(demolition_fired(234, 175))
    s.append(demolition_fired(491, 168))
    s.append(note(234, 208, "BRIDGE", "middle"))
    s.append(note(512, 200, "BRIDGE", "start"))
    # defile blocked (17F 25c)
    s.append(roadblock(728, 250))
    s.append(note(728, 300, "DEFILE", "middle"))
    # minefield belt between the en fmns (OW 03200)
    s.append(minefield([(120, 70), (330, 60), (335, 108), (125, 118)]))
    s.append(note(340, 138, "OBS BELT BETWEEN EN FMNS", "middle"))
    # routes in depth obstructed by fire (17F 7, 8)
    s.append(linear_conc(790, 102, 757, 150, BLUE))
    s.append(unit(70, 425, BLUE, "arty", "II", "OWN ARTY", w=36, h=22))
    s.append(note(520, 452, "NO RING OF TROOPS. BRIDGES DESTROYED, DEFILE BLOCKED, ROUTES OBSTRUCTED.", "middle"))
    return finish(s)


def key():
    """Small swatches for the legend, keyed by id."""
    items = {
        "unit-inf": unit(30, 24, BLUE, "inf", "II", w=36, h=22),
        "unit-armd": unit(30, 24, BLUE, "armd", "I", w=36, h=22),
        "unit-mech": unit(30, 24, BLUE, "mech", "II", w=36, h=22),
        "unit-airmob": unit(30, 24, BLUE, "airmob", "II", w=36, h=22),
        "unit-arty": unit(30, 24, BLUE, "arty", "II", w=36, h=22),
        "unit-en": unit(30, 24, RED, "inf", "●●●", w=36, h=22),
        "hq": hq(14, 46, RED, "X"),
        "goose": goose(30, 26, 26, 14, RED, "I"),
        "obj": goose(30, 26, 26, 14, BLUE, "", "OBJ"),
        "obj-future": goose(30, 26, 26, 14, BLUE, "", "OBJ", dashed=True, sw=1.6),
        "strong": strong_point(30, 28, 18, 10, RED, ""),
        "front": front_line([(4, 30), (56, 30)], RED, -1, 13),
        "axis": axis((4, 30), (20, 30), (36, 30), (58, 30), BLUE, width=10),
        "main": axis((2, 30), (18, 30), (34, 30), (52, 30), BLUE, width=10, main=True),
        "repulsed": axis((4, 30), (20, 30), (36, 30), (50, 30), RED, width=10, repulsed_by=BLUE),
        "minefield": minefield([(6, 14), (58, 14), (58, 44), (6, 44)]),
        "route-proj": route([(4, 30), (56, 30)], RED, dashed=True),
        "roadblock": roadblock(30, 28),
        "demo": demolition_fired(30, 28),
        "conc": conc(30, 28, BLUE),
        "linconc": linear_conc(6, 28, 54, 28, BLUE),
        "arc": arc_of_fire(10, 28, -25, 25, 45, BLUE),
        "op": op(30, 30, BLUE, arty=True),
        "obstacle": tank_obstacle([(4, 28), (60, 28)]),
    }
    return {k: f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -4 64 56" font-family="Arial, Helvetica, sans-serif">{v}</svg>' for k, v in items.items()}


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for name, fn in (("envelopment", envelopment), ("double", double_envelopment), ("turning", turning), ("encirclement", encirclement),
                     ("investment", investment), ("isolation", isolation)):
        with open(os.path.join(OUT, f"{name}.svg"), "w") as fh:
            fh.write(fn())
    for k, v in key().items():
        with open(os.path.join(OUT, f"key-{k}.svg"), "w") as fh:
            fh.write(v)
    print("ok", len(os.listdir(OUT)))
