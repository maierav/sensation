"""
Animated GIF demo of global-before-local perception with truly hierarchical
textures (Campana, Rebollo, Urai, Wyart & Tallon-Baudry, 2016, J Neurosci).

Stimulus: a circular texture of short lines, randomly oriented except in a
central 4 x 18-line rectangle where lines share a LOCAL orientation; that
rectangle's own tilt is the GLOBAL orientation, always +/-45 deg from the local
one. Orientations: -67.5, -22.5, +22.5, +67.5 deg from vertical. Line
orientations follow a von Mises distribution (coherence kappa) that fades to
random over three lines outside the rectangle, so there is no contour.

Demo: several trials of the paper's GLOBAL task (report the shape's tilt),
then a surprise question about the tilt of the individual LINES.
Usage:  python3 global_local_gif.py [output.gif] [--dark]
"""
import math, random, os, sys
from PIL import Image, ImageDraw, ImageFont

DARK = "--dark" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = args[0] if args else ("global_local_dark.gif" if DARK else "global_local.gif")
FRAMEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gl_frames_dark" if DARK else "gl_frames")
os.makedirs(FRAMEDIR, exist_ok=True)

W, H = 640, 480
FONT = "/System/Library/Fonts/Helvetica.ttc"
def font(sz, bold=False):
    return ImageFont.truetype(FONT, sz, index=1 if bold else 0)
if DARK:
    BG, INK, DIM, LINE = (0, 0, 0), (235, 235, 235), (170, 170, 170), (225, 225, 225)
else:
    BG, INK, DIM, LINE = (255, 255, 255), (20, 20, 20), (60, 60, 60), (25, 25, 25)
ACCENT = (220, 60, 40) if not DARK else (255, 110, 90)

# ---- stimulus parameters -------------------------------------------------
ORIENTS = [-67.5, -22.5, 22.5, 67.5]        # deg from vertical, negative = top to the left
KAPPA = 4                                    # coherence, as in the paper's main experiments
SP, LLEN, NRAD = 8, 7, 22                    # line spacing, line length, lines on the radius (px)
RECT = (4, 18)                               # rectangle size in lines (across, along)
SS = 3
N_PRE = 6
FIX_MS, STIM_MS, BLANK_MS, Q_MS, FB_MS = 700, 1500, 500, 2500, 800

random.seed(2016)
frames, durations = [], []
def emit(img, ms): frames.append(img); durations.append(ms)
def blank(): return Image.new("RGB", (W, H), BG)

def draw_text_block(img, lines, y0=None, size=26, bold=False, spacing=14, color=INK):
    d = ImageDraw.Draw(img); rendered = []
    for ln in lines:
        t, b = ln if isinstance(ln, tuple) else (ln, bold)
        f = font(size, b); bb = d.textbbox((0, 0), t, font=f)
        rendered.append((t, f, bb[2] - bb[0], bb[3] - bb[1]))
    total = sum(h for *_, h in rendered) + spacing * (len(rendered) - 1)
    y = (H - total) // 2 if y0 is None else y0
    for t, f, tw, th in rendered:
        d.text(((W - tw) // 2, y), t, font=f, fill=color); y += th + spacing
    return y

def texture(local_deg, global_deg, kappa, seed):
    rnd = random.Random(seed)
    R = NRAD * SP; size = 2 * R + SP
    img = Image.new("RGB", (size * SS, size * SS), BG); d = ImageDraw.Draw(img)
    c = size / 2
    tg, tl = math.radians(global_deg), math.radians(local_deg)
    gu = (math.sin(tg), -math.cos(tg)); gv = (math.cos(tg), math.sin(tg))
    hw, hl = RECT[0] * SP / 2, RECT[1] * SP / 2
    for i in range(-NRAD, NRAD + 1):
        for j in range(-NRAD, NRAD + 1):
            x, y = i * SP, j * SP
            if math.hypot(x, y) > R: continue
            u = x * gu[0] + y * gu[1]; v = x * gv[0] + y * gv[1]
            du = max(abs(u) - hl, 0) / SP; dv = max(abs(v) - hw, 0) / SP
            t = min(math.hypot(du, dv) / 3.0, 1.0)
            k = kappa * (1 - (3 * t * t - 2 * t * t * t))          # smooth fall-off over 3 lines
            th = rnd.uniform(0, math.pi) if k < 0.05 else rnd.vonmisesvariate(2 * tl, k) / 2.0
            dx, dy = math.sin(th) * LLEN / 2, -math.cos(th) * LLEN / 2
            X, Y = c + x, c + y
            d.line(((X - dx) * SS, (Y - dy) * SS, (X + dx) * SS, (Y + dy) * SS), fill=LINE, width=int(1.4 * SS))
    # fixation dot in the centre (background-coloured disc so it stays visible)
    d.ellipse(((c - 4) * SS, (c - 4) * SS, (c + 4) * SS, (c + 4) * SS), fill=BG)
    d.ellipse(((c - 2) * SS, (c - 2) * SS, (c + 2) * SS, (c + 2) * SS), fill=INK)
    return img.resize((size, size), Image.LANCZOS)

def fixation():
    img = blank(); d = ImageDraw.Draw(img)
    d.ellipse((W // 2 - 3, H // 2 - 3, W // 2 + 3, H // 2 + 3), fill=INK); return img

def stimulus_frame(tex):
    img = blank(); img.paste(tex, ((W - tex.width) // 2, (H - tex.height) // 2)); return img

def bar_icon(d, cx, cy, deg, color, length=44, width=6):
    th = math.radians(deg); dx, dy = math.sin(th) * length / 2, -math.cos(th) * length / 2
    d.line((cx - dx, cy - dy, cx + dx, cy + dy), fill=color, width=width)

def options_row(img, cy, highlight=None, labels=None, mark_color=None):
    """Four tilted-bar icons with labels 1-4; optionally circle one."""
    d = ImageDraw.Draw(img)
    xs = [W // 2 + (k - 1.5) * 120 for k in range(4)]
    for k, (x, deg) in enumerate(zip(xs, ORIENTS)):
        col = INK if highlight in (None, k) else DIM
        bar_icon(d, x, cy, deg, col)
        if highlight == k:
            d.ellipse((x - 34, cy - 34, x + 34, cy + 34), outline=mark_color or INK, width=4)
        d.text((x, cy + 52), str(k + 1), font=font(26, True), fill=col, anchor="mm")
        if labels and labels[k]:
            d.text((x, cy + 82), labels[k], font=font(20), fill=mark_color or INK, anchor="mm")
    return img

def question_global():
    img = blank()
    draw_text_block(img, [("Which way was the SHAPE tilted?", True)], y0=70, size=32)
    return options_row(img, 250)
def feedback_global(k):
    img = blank()
    draw_text_block(img, [("The shape was tilted like this:", False)], y0=70, size=28, color=DIM)
    return options_row(img, 250, highlight=k)

def make_trial(seed):
    li = random.randrange(4); local = ORIENTS[li]
    cands = [g for g in ORIENTS if abs(((g - local + 90) % 180) - 90) == 45]
    glob = random.choice(cands); gi = ORIENTS.index(glob)
    return texture(local, glob, KAPPA, seed), li, gi

# ---------------------------------------------------------------- instructions
img = blank()
draw_text_block(img, [
    ("A quick demonstration", True), ("", False),
    ("Each display is a texture of small lines. In its centre, the", False),
    ("lines line up and together form an elongated SHAPE.", False), ("", False),
    ("Your task: decide silently which way the SHAPE is tilted,", False),
    ("choosing one of these four tilts:", False),
], y0=40, size=23, spacing=9)
options_row(img, 330)
emit(img, 8000)
img = blank(); draw_text_block(img, [("Ready?", True)], size=40); emit(img, 1500)

# ---------------------------------------------------------------- global-task trials
for i in range(N_PRE):
    tex, li, gi = make_trial(100 + i)
    emit(fixation(), FIX_MS); emit(stimulus_frame(tex), STIM_MS); emit(blank(), BLANK_MS)
    emit(question_global(), Q_MS); emit(feedback_global(gi), FB_MS)

# ---------------------------------------------------------------- surprise trial
tex, li, gi = make_trial(999)
emit(fixation(), FIX_MS); emit(stimulus_frame(tex), STIM_MS); emit(blank(), BLANK_MS)
img = blank(); draw_text_block(img, [("Surprise question!", True)], size=36); emit(img, 1500)
img = blank()
draw_text_block(img, [("Never mind the shape this time.", False),
                      ("Which way were the individual LINES tilted?", True)], y0=60, size=29, spacing=10)
options_row(img, 260)
draw_text_block(img, [("(Decide now, before the answer appears.)", False)], y0=400, size=24)
emit(img, 7000)

# reveal: the same texture, with both answers marked
img = blank()
small = tex.resize((int(tex.width * 0.8), int(tex.height * 0.8)), Image.LANCZOS)
img.paste(small, (30, (H - small.height) // 2))
d = ImageDraw.Draw(img)
rx = 470
d.text((rx, 95), "the SHAPE", font=font(22, True), fill=INK, anchor="mm")
bar_icon(d, rx, 150, ORIENTS[gi], INK, length=70, width=8)
d.text((rx, 200), "tilt %d" % (gi + 1), font=font(22), fill=INK, anchor="mm")
d.text((rx, 270), "the LINES", font=font(22, True), fill=ACCENT, anchor="mm")
bar_icon(d, rx, 325, ORIENTS[li], ACCENT, length=70, width=8)
d.text((rx, 375), "tilt %d" % (li + 1), font=font(22), fill=ACCENT, anchor="mm")
emit(img, 6000)

img = blank()
draw_text_block(img, [
    ("Did you know how the lines were tilted?", True), ("", False),
    ("There is no outline here. The shape exists ONLY because", False),
    ("of the lines: your visual system had to register their", False),
    ("orientation to see the shape at all. Yet the shape is what", False),
    ("reaches awareness; the lines that built it often do not.", False), ("", False),
    ("Campana et al. (2016): asked simply what they saw, people", False),
    ("named the shape's tilt on 82% of trials and the lines' on 12%.", False),
    ("The shape was reported faster, and when asked about the lines,", False),
    ("most errors were the shape's tilt (62% vs 35% for the mirror", False),
    ("error at the same angular distance).", False), ("", False),
    ("Global first. The parts are optional.", True),
], size=20, spacing=7)
emit(img, 12000)

pframes = [f.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE) for f in frames]
pframes[0].save(OUT, save_all=True, append_images=pframes[1:], duration=durations, loop=0, disposal=2, optimize=False)
for i, f in enumerate(frames): f.save(os.path.join(FRAMEDIR, "f%02d.png" % i))
print("frames:", len(frames), "total s:", sum(durations) / 1000, "surprise local idx:", li + 1, "global idx:", gi + 1)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
