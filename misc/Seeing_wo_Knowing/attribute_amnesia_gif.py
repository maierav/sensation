"""
Animated GIF demo of the attribute-amnesia paradigm (Chen & Wyble, 2015;
reviewed in Fu, Guan, Tam, O'Donnell, Shen, Wyble & Chen, 2023, TiCS, Fig. 1A).

Pre-surprise trials: fixation -> array of one LETTER and three digits, each in a
different colour (150 ms) -> '@' masks (150 ms) -> 400 ms blank -> "Where was the
letter?" (locations 1-4). Surprise trial: same display, then an unexpected
question about the letter's IDENTITY and then its COLOUR.

Usage:  python3 attribute_amnesia_gif.py [output.gif] [--dark]
"""
import random, os, sys
from PIL import Image, ImageDraw, ImageFont

DARK = "--dark" in sys.argv
args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = args[0] if args else ("attribute_amnesia_dark.gif" if DARK else "attribute_amnesia.gif")
FRAMEDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "aa_frames_dark" if DARK else "aa_frames")
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
else:
    BG, INK, DIM = (255, 255, 255), (20, 20, 20), (60, 60, 60)
    COLORS = {"red": (220, 30, 30), "green": (0, 150, 60),
              "blue": (30, 80, 220), "yellow": (225, 175, 0)}

# ---- stimulus parameters -------------------------------------------------
N_PRE = 7                                   # pre-surprise trials
FIX_MS, ARRAY_MS, MASK_MS, BLANK_MS = 1000, 150, 150, 400
QUESTION_MS, FEEDBACK_MS = 2000, 800
OFF = 95                                    # half-spacing of the 2x2 array (px)
STIM_SIZE = 64
LETTERS = list("ACEFHJKLMNPRTUVWXY")       # not confusable with digits
DIGITS = list("23456789")
POS = {1: (-OFF, -OFF), 2: (OFF, -OFF), 3: (-OFF, OFF), 4: (OFF, OFF)}   # 1 2 / 3 4

random.seed(2023)
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

def centred_char(d, ch, cx, cy, f, fill):
    bb = d.textbbox((0, 0), ch, font=f, anchor="ls")
    # use anchor 'mm' for true centring
    d.text((cx, cy), ch, font=f, fill=fill, anchor="mm")

def fixation_cross(d, cx=W // 2, cy=H // 2, a=10):
    d.line((cx - a, cy, cx + a, cy), fill=INK, width=3)
    d.line((cx, cy - a, cx, cy + a), fill=INK, width=3)

def fixation():
    img = blank(); fixation_cross(ImageDraw.Draw(img)); return img

def array_frame(items):
    """items: {pos: (char, colour_name)}"""
    img = blank(); d = ImageDraw.Draw(img)
    fixation_cross(d)
    f = font(STIM_SIZE, True)
    for p, (ch, cname) in items.items():
        dx, dy = POS[p]
        centred_char(d, ch, W // 2 + dx, H // 2 + dy, f, COLORS[cname])
    return img

def mask_frame():
    img = blank(); d = ImageDraw.Draw(img)
    fixation_cross(d)
    f = font(STIM_SIZE, True)
    for p in POS:
        dx, dy = POS[p]
        centred_char(d, "@", W // 2 + dx, H // 2 + dy, f, INK)
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
        centred_char(d, str(p), x, y, f, INK if highlight in (None, p) else DIM)
    return img

def location_question():
    img = blank()
    draw_text_block(img, [("Where was the LETTER?", True)], y0=60, size=32)
    return location_layout(img)

def location_feedback(p):
    img = blank()
    draw_text_block(img, [("It was here:", False)], y0=60, size=30, color=DIM)
    return location_layout(img, highlight=p)

def make_trial():
    letter = random.choice(LETTERS)
    digits = random.sample(DIGITS, 3)
    cols = list(COLORS); random.shuffle(cols)
    tpos = random.randint(1, 4)
    items, k = {}, 0
    for p in (1, 2, 3, 4):
        if p == tpos:
            items[p] = (letter, cols[p - 1])
        else:
            items[p] = (digits[k], cols[p - 1]); k += 1
    return items, letter, tpos, items[tpos][1]

# ---------------------------------------------------------------- instructions
img = blank()
draw_text_block(img, [
    ("A quick demonstration", True),
    ("", False),
    ("Each display flashes four characters very briefly:", False),
    ("three digits and ONE LETTER.", True),
    ("", False),
    ("Your task: find the letter and decide silently", False),
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

for i in range(N_PRE):
    items, letter, tpos, tcol = make_trial()
    run_trial(items)
    emit(location_question(), QUESTION_MS)
    emit(location_feedback(tpos), FEEDBACK_MS)

# ---------------------------------------------------------------- surprise trial
items, letter, tpos, tcol = make_trial()
run_trial(items)

img = blank(); draw_text_block(img, [("Surprise memory test!", True)], size=36); emit(img, 2000)

others = random.sample([l for l in LETTERS if l != letter], 3)
opts = others + [letter]; random.shuffle(opts)
img = blank()
draw_text_block(img, [("Which LETTER did you just find?", True), ("", False),
                      ("        ".join(opts), True), ("", False),
                      ("(Decide now.)", False)], size=30, spacing=14)
emit(img, 5000)

img = blank()
draw_text_block(img, [("And what COLOUR was that letter?", True)], y0=110, size=30)
d = ImageDraw.Draw(img)
names = list(COLORS); sw, sh, gap = 90, 56, 40
x = (W - (len(names) * sw + (len(names) - 1) * gap)) // 2
for n in names:
    d.rectangle((x, 220, x + sw, 220 + sh), fill=COLORS[n])
    d.text((x + sw // 2, 220 + sh + 22), n, font=font(22), fill=INK, anchor="mm")
    x += sw + gap
draw_text_block(img, [("(Decide now.)", False)], y0=340, size=26)
emit(img, 5000)

# ---------------------------------------------------------------- reveal
img = array_frame(items)
draw_text_block(img, [("The letter was %s, at position %d." % (letter, tpos), False)], y0=40, size=26)
draw_text_block(img, [("It was %s." % tcol.upper(), True)], y0=H - 80, size=30, color=COLORS[tcol])
emit(img, 4000)

img = blank()
draw_text_block(img, [
    ("Could you say which letter it was, and its colour?", True),
    ("", False),
    ("You had just found that letter: telling it apart from", False),
    ("the digits is the only way to do the task. Yet the", False),
    ("moment you no longer expect a question, that", False),
    ("information can simply fail to be stored.", False),
    ("", False),
    ("Chen & Wyble (2015) called this attribute amnesia: on a", False),
    ("surprise trial like this one, only about a quarter of people", False),
    ("could report the letter they had just located. On the very", False),
    ("next trials, once they expected the question, most could.", False),
    ("", False),
    ("Attended, used, and not remembered.", True),
], size=21, spacing=8)
emit(img, 10000)

# ---------------------------------------------------------------- write
pframes = [f.quantize(colors=64, method=Image.MEDIANCUT, dither=Image.NONE) for f in frames]
pframes[0].save(OUT, save_all=True, append_images=pframes[1:], duration=durations,
                loop=0, disposal=2, optimize=False)
for i, f in enumerate(frames):
    f.save(os.path.join(FRAMEDIR, "f%02d.png" % i))
print("frames:", len(frames), "total s:", sum(durations) / 1000,
      "surprise letter:", letter, tpos, tcol, "options:", opts)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
