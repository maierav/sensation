"""
Animated GIF demo of the POP-OUT COLOUR attribute-amnesia task (Chen & Wyble,
2015; Fig. 1B "Pop-out color" in Fu et al., 2023, TiCS).

Pre-surprise trials: fixation -> array of four LETTERS, three in the default
ink colour and ONE in a pop-out colour (150 ms) -> '@' masks (150 ms) -> 400 ms
blank -> "Where was the coloured letter?" (locations 1-4). Surprise trial: same
display, then an unexpected question about the colour that was just used to
find the target.

Usage:  python3 popout_amnesia_gif.py [output.gif] [--dark]
"""
import random, os, sys
from PIL import Image, ImageDraw, ImageFont

DARK = "--dark" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = args[0] if args else ("popout_amnesia_dark.gif" if DARK else "popout_amnesia.gif")
FRAMEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "po_frames_dark" if DARK else "po_frames")
os.makedirs(FRAMEDIR, exist_ok=True)

W, H = 640, 480
FONT = "/System/Library/Fonts/Helvetica.ttc"
def font(sz, bold=False):
    return ImageFont.truetype(FONT, sz, index=1 if bold else 0)

# ---- theme --------------------------------------------------------------
if DARK:
    BG, INK, DIM = (0, 0, 0), (235, 235, 235), (170, 170, 170)
    COLORS = {"red": (255, 75, 75), "green": (70, 220, 100),
              "blue": (95, 150, 255), "yellow": (255, 225, 60)}
    DISTRACTOR_NAME = "white"
else:
    BG, INK, DIM = (255, 255, 255), (20, 20, 20), (60, 60, 60)
    COLORS = {"red": (220, 30, 30), "green": (0, 150, 60),
              "blue": (30, 80, 220), "yellow": (225, 175, 0)}
    DISTRACTOR_NAME = "black"
DISTRACTOR = INK                            # the three non-target letters

# ---- stimulus parameters -------------------------------------------------
N_PRE = 7
FIX_MS, ARRAY_MS, MASK_MS, BLANK_MS = 1000, 150, 150, 400
QUESTION_MS, FEEDBACK_MS = 2000, 800
OFF = 95
STIM_SIZE = 64
LETTERS = list("ABCDEFGHJKLMNPRSTUVWXYZ")
POS = {1: (-OFF, -OFF), 2: (OFF, -OFF), 3: (-OFF, OFF), 4: (OFF, OFF)}

random.seed(2015)
frames, durations = [], []
def emit(img, ms):
    frames.append(img); durations.append(ms)

def blank():
    return Image.new("RGB", (W, H), BG)

def draw_text_block(img, lines, y0=None, size=26, bold=False, spacing=14, color=INK):
    d = ImageDraw.Draw(img)
    rendered = []
    for ln in lines:
        t, b = ln if isinstance(ln, tuple) else (ln, bold)
        f = font(size, b)
        bb = d.textbbox((0, 0), t, font=f)
        rendered.append((t, f, bb[2] - bb[0], bb[3] - bb[1]))
    total = sum(h for *_, h in rendered) + spacing * (len(rendered) - 1)
    y = (H - total) // 2 if y0 is None else y0
    for t, f, tw, th in rendered:
        d.text(((W - tw) // 2, y), t, font=f, fill=color)
        y += th + spacing
    return y

def fixation_cross(d, cx=W // 2, cy=H // 2, a=10):
    d.line((cx - a, cy, cx + a, cy), fill=INK, width=3)
    d.line((cx, cy - a, cx, cy + a), fill=INK, width=3)

def fixation():
    img = blank(); fixation_cross(ImageDraw.Draw(img)); return img

def array_frame(items):
    """items: {pos: (letter, rgb)}"""
    img = blank(); d = ImageDraw.Draw(img)
    fixation_cross(d)
    f = font(STIM_SIZE, True)
    for p, (ch, rgb) in items.items():
        dx, dy = POS[p]
        d.text((W // 2 + dx, H // 2 + dy), ch, font=f, fill=rgb, anchor="mm")
    return img

def mask_frame():
    img = blank(); d = ImageDraw.Draw(img)
    fixation_cross(d)
    f = font(STIM_SIZE, True)
    for p in POS:
        dx, dy = POS[p]
        d.text((W // 2 + dx, H // 2 + dy), "@", font=f, fill=INK, anchor="mm")
    return img

def location_layout(img, highlight=None, cy=H // 2 + 50, scale=0.6):
    d = ImageDraw.Draw(img)
    f = font(int(STIM_SIZE * 0.75), True)
    for p in POS:
        dx, dy = POS[p]
        x, y = W // 2 + int(dx * scale), cy + int(dy * scale)
        if p == highlight:
            r = 30
            d.ellipse((x - r, y - r, x + r, y + r), outline=INK, width=4)
        d.text((x, y), str(p), font=f, fill=INK if highlight in (None, p) else DIM, anchor="mm")
    return img

def location_question():
    img = blank()
    draw_text_block(img, [("Where was the COLOURED letter?", True)], y0=60, size=32)
    return location_layout(img)

def location_feedback(p):
    img = blank()
    draw_text_block(img, [("It was here:", False)], y0=60, size=30, color=DIM)
    return location_layout(img, highlight=p)

def make_trial(avoid_color=None):
    letters = random.sample(LETTERS, 4)
    cname = random.choice([c for c in COLORS if c != avoid_color])
    tpos = random.randint(1, 4)
    items = {p: (letters[p - 1], COLORS[cname] if p == tpos else DISTRACTOR) for p in (1, 2, 3, 4)}
    return items, letters[tpos - 1], tpos, cname

# ---------------------------------------------------------------- instructions
img = blank()
draw_text_block(img, [
    ("A quick demonstration", True),
    ("", False),
    ("Each display flashes four letters very briefly.", False),
    ("Three are %s. ONE is in a different colour." % DISTRACTOR_NAME, True),
    ("", False),
    ("Your task: find the coloured letter and decide silently", False),
    ("WHERE it was (position 1, 2, 3 or 4).", True),
    ("", False),
    ("Keep your eyes on the central cross.", False),
], size=24, spacing=10)
emit(img, 7000)
img = blank(); draw_text_block(img, [("Ready?", True)], size=40); emit(img, 1500)

# ---------------------------------------------------------------- pre-surprise trials
def run_trial(items):
    emit(fixation(), FIX_MS)
    emit(array_frame(items), ARRAY_MS)
    emit(mask_frame(), MASK_MS)
    emit(blank(), BLANK_MS)

last_color = None
for i in range(N_PRE):
    items, letter, tpos, cname = make_trial(avoid_color=last_color)
    last_color = cname
    run_trial(items)
    emit(location_question(), QUESTION_MS)
    emit(location_feedback(tpos), FEEDBACK_MS)

# ---------------------------------------------------------------- surprise trial
items, letter, tpos, cname = make_trial(avoid_color=last_color)
run_trial(items)

img = blank(); draw_text_block(img, [("Surprise memory test!", True)], size=36); emit(img, 2000)

img = blank()
draw_text_block(img, [("What COLOUR was the odd-one-out letter", True),
                      ("you just located?", True)], y0=90, size=30, spacing=8)
d = ImageDraw.Draw(img)
names = list(COLORS); sw, sh, gap = 90, 56, 40
x = (W - (len(names) * sw + (len(names) - 1) * gap)) // 2
for n in names:
    d.rectangle((x, 230, x + sw, 230 + sh), fill=COLORS[n])
    d.text((x + sw // 2, 230 + sh + 22), n, font=font(22), fill=INK, anchor="mm")
    x += sw + gap
draw_text_block(img, [("(Decide now, before the answer appears.)", False)], y0=350, size=24)
emit(img, 6000)

# ---------------------------------------------------------------- reveal
img = array_frame(items)
draw_text_block(img, [("The coloured letter was %s, at position %d." % (letter, tpos), False)], y0=40, size=26)
draw_text_block(img, [("It was %s." % cname.upper(), True)], y0=H - 80, size=30, color=COLORS[cname])
emit(img, 4000)

img = blank()
draw_text_block(img, [
    ("Could you say what colour it was?", True),
    ("", False),
    ("The colour was not a detail you could have ignored:", False),
    ("it was the ONLY thing that made the target stand out,", False),
    ("and you used it to find the letter a moment ago.", False),
    ("", False),
    ("Chen & Wyble (2015) found that on a surprise trial like", False),
    ("this one, most people could not report the colour they", False),
    ("had just used. A few trials later, once they expected", False),
    ("the question, nearly everyone could.", False),
    ("", False),
    ("Attended, used, and not remembered.", True),
], size=22, spacing=9)
emit(img, 10000)

# ---------------------------------------------------------------- write
pframes = [f.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE) for f in frames]
pframes[0].save(OUT, save_all=True, append_images=pframes[1:], duration=durations,
                loop=0, disposal=2, optimize=False)
for i, f in enumerate(frames):
    f.save(os.path.join(FRAMEDIR, "f%02d.png" % i))
print("frames:", len(frames), "total s:", sum(durations) / 1000,
      "surprise:", letter, tpos, cname)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
