"""
Animated GIF demo of the Kanizsa "seeing without knowing" paradigm
(Eitam, Shoval & Yeshurun, 2015, Ann NY Acad Sci, Experiment 1,
rectangle-relevant condition).

Timeline per trial (as in the paper): fixation 500 ms -> stimulus 500 ms ->
blank 500 ms -> question. Every trial shows an ILLUSORY (Kanizsa) rectangle:
no real rectangle is ever drawn; four solid discs with a white rectangle
superimposed guarantee inward-facing inducers. Baseline trials use random
inducer colors (8 colors); the critical trial uses green and is followed by
the orientation question and then the surprise color question.

Usage:  python3 seeing_without_knowing_gif.py [output.gif] [--dark]
        --dark renders the black-background version.
"""
import random, os, sys
from PIL import Image, ImageDraw, ImageFont

DARK = "--dark" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = args[0] if args else ("seeing_without_knowing_dark.gif" if DARK else "seeing_without_knowing.gif")
FRAMEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "frames_dark" if DARK else "frames")
os.makedirs(FRAMEDIR, exist_ok=True)

W, H = 640, 480
SS = 3                      # supersampling factor for antialiased shapes
PX_PER_CM = 70              # stimulus scale: rectangle 2 x 2.5 cm, inducer r = 0.5 cm
RECT_SHORT, RECT_LONG = 2.0 * PX_PER_CM, 2.5 * PX_PER_CM
IND_R = 0.5 * PX_PER_CM

# ---- theme: light (white background) or dark (black background) -----------
if DARK:
    BG = (0, 0, 0)
    INK = (235, 235, 235)          # main text
    DIM = (170, 170, 170)          # feedback text
    BASELINE_COLORS = {            # brightened so every colour reads on black
        "yellow":      (255, 225, 40),
        "blue":        (70, 120, 255),
        "light blue":  (130, 200, 255),
        "brown":       (200, 135, 70),
        "purple":      (180, 95, 240),
        "orange":      (255, 150, 30),
        "pink":        (255, 130, 195),
        "light green": (160, 240, 130),
    }
    CRITICAL_COLOR = (20, 185, 80)
else:
    BG = (255, 255, 255)
    INK = (20, 20, 20)
    DIM = (60, 60, 60)
    BASELINE_COLORS = {
        "yellow":      (250, 215, 0),
        "blue":        (35, 70, 220),
        "light blue":  (120, 190, 255),
        "brown":       (140, 85, 35),
        "purple":      (135, 45, 185),
        "orange":      (255, 140, 0),
        "pink":        (255, 120, 185),
        "light green": (150, 230, 120),
    }
    CRITICAL_COLOR = (0, 150, 60)
CRITICAL_COLOR_NAME = "green"

FONT = "/System/Library/Fonts/Helvetica.ttc"
def font(sz, bold=False):
    return ImageFont.truetype(FONT, sz, index=1 if bold else 0)

random.seed(2015)

frames, durations = [], []
def emit(img, ms):
    frames.append(img)
    durations.append(ms)

def blank():
    return Image.new("RGB", (W, H), BG)

def draw_text_block(img, lines, y0=None, size=26, bold=False, spacing=14, color=INK):
    """Center a list of lines (each may be (text, bold) or str). Returns bottom y."""
    d = ImageDraw.Draw(img)
    rendered = []
    for ln in lines:
        if isinstance(ln, tuple):
            t, b = ln
        else:
            t, b = ln, bold
        f = font(size, b)
        bbox = d.textbbox((0, 0), t, font=f)
        rendered.append((t, f, bbox[2] - bbox[0], bbox[3] - bbox[1]))
    total = sum(h for *_, h in rendered) + spacing * (len(rendered) - 1)
    y = (H - total) // 2 if y0 is None else y0
    for t, f, tw, th in rendered:
        d.text(((W - tw) // 2, y), t, font=f, fill=color)
        y += th + spacing
    return y

def fixation():
    img = blank()
    d = ImageDraw.Draw(img)
    cx, cy, a = W // 2, H // 2, 12
    d.line((cx - a, cy, cx + a, cy), fill=INK, width=3)
    d.line((cx, cy - a, cx, cy + a), fill=INK, width=3)
    return img

def stimulus(orientation, color, illusory=True, missing=None):
    """Kanizsa rectangle, 'vertical' or 'horizontal'. Four solid discs are
    centred on the rectangle's corners and a solid WHITE rectangle is drawn on
    top of them: this guarantees every inducer's notch faces inward, so the
    illusory contour is present on every trial. No real rectangle is ever drawn."""
    big = Image.new("RGB", (W * SS, H * SS), BG)
    d = ImageDraw.Draw(big)
    rw, rh = (RECT_SHORT, RECT_LONG) if orientation == "vertical" else (RECT_LONG, RECT_SHORT)
    cx, cy = W / 2, H / 2
    x0, y0, x1, y1 = cx - rw / 2, cy - rh / 2, cx + rw / 2, cy + rh / 2
    r = IND_R
    for px, py in [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]:
        d.ellipse([(px - r) * SS, (py - r) * SS, (px + r) * SS, (py + r) * SS], fill=color)
    d.rectangle([x0 * SS, y0 * SS, x1 * SS, y1 * SS], fill=BG)   # white, no outline
    return big.resize((W, H), Image.LANCZOS)

def orientation_question(prefix=None):
    img = blank()
    lines = []
    if prefix:
        lines.append((prefix, False))
    lines += [("Was the rectangle", False), ("HORIZONTAL  or  VERTICAL ?", True)]
    draw_text_block(img, lines, size=30)
    return img

def feedback(orientation):
    img = blank()
    draw_text_block(img, [("Correct answer:", False), (orientation.upper(), True)], size=30, color=DIM)
    return img

# ---------------------------------------------------------------- instructions
img = blank()
draw_text_block(img, [
    ("A quick demonstration", True),
    ("", False),
    ("You will see a rectangle surrounded by four shapes,", False),
    ("shown very briefly, one display at a time.", False),
    ("", False),
    ("Your task: after each display, decide silently", False),
    ("whether the rectangle was", False),
    ("HORIZONTAL  or  VERTICAL.", True),
    ("", False),
    ("Keep your eyes on the centre of the screen.", False),
], size=24, spacing=10)
emit(img, 7000)

img = blank()
draw_text_block(img, [("Ready?", True)], size=40)
emit(img, 1500)

# ---------------------------------------------------------------- baseline trials
N_BASELINE = 6
names = list(BASELINE_COLORS)
# fixed, reproducible sequence; avoid 'light green' on the last two trials so it
# doesn't prime the critical colour, and avoid immediate repeats
seq = []
while len(seq) < N_BASELINE:
    c = random.choice(names)
    if seq and c == seq[-1]:
        continue
    if len(seq) >= N_BASELINE - 2 and c == "light green":
        continue
    seq.append(c)
orients = ["vertical", "horizontal"] * 3
random.shuffle(orients)

for i, (cname, ori) in enumerate(zip(seq, orients)):
    emit(fixation(), 500)
    emit(stimulus(ori, BASELINE_COLORS[cname]), 500)
    emit(blank(), 500)
    emit(orientation_question(), 2000)
    emit(feedback(ori), 900)

# ---------------------------------------------------------------- critical trial
crit_ori = "horizontal" if orients[-1] == "vertical" else "vertical"
emit(fixation(), 500)
emit(stimulus(crit_ori, CRITICAL_COLOR), 500)
emit(blank(), 500)
emit(orientation_question(), 2000)

img = blank()
draw_text_block(img, [("One more question.", True)], size=34)
emit(img, 1500)

img = blank()
draw_text_block(img, [
    ("What COLOUR were the four shapes", False),
    ("around the rectangle?", False),
    ("", False),
    ("Blue        Green        Orange        Purple", True),
    ("", False),
    ("(Decide now, before the answer appears.)", False),
], size=28, spacing=12)
emit(img, 6000)

# ---------------------------------------------------------------- reveal
img = stimulus(crit_ori, CRITICAL_COLOR)
draw_text_block(img, [("The rectangle was %s." % crit_ori.upper(), False)], y0=40, size=26)
draw_text_block(img, [("The shapes were %s." % CRITICAL_COLOR_NAME.upper(), True)], y0=H - 90, size=30)
emit(img, 4000)

img = blank()
draw_text_block(img, [
    ("Did you know the colour, or did you guess?", True),
    ("", False),
    ("You must have seen the shapes: without them there is", False),
    ("no rectangle at all. Its edges were an illusion created", False),
    ("by the shapes themselves.", False),
    ("", False),
    ("In Eitam, Shoval & Yeshurun (2015), nearly everyone reported", False),
    ("the rectangle's orientation correctly, yet almost 30% could", False),
    ("not report the colour of the shapes they had just looked at.", False),
    ("", False),
    ("Seeing without knowing.", True),
], size=22, spacing=9)
emit(img, 9000)

# ---------------------------------------------------------------- write
# quantize each frame to a palette (GIF), keep per-frame durations
pframes = [f.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE) for f in frames]
pframes[0].save(OUT, save_all=True, append_images=pframes[1:], duration=durations,
                loop=0, disposal=2, optimize=False)

for i, f in enumerate(frames):
    f.save(os.path.join(FRAMEDIR, "f%02d.png" % i))
print("frames:", len(frames), "total ms:", sum(durations), "critical:", crit_ori, "baseline seq:", seq, orients)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
