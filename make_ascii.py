from PIL import Image, ImageOps, ImageFilter
import json

SRC = "/mnt/user-data/uploads/IMG_7301_900x900.jpg"
COLS = 58          # character columns
ASPECT = 0.52       # chars are taller than wide -> compress rows

# darkest -> lightest ramp (kept short & clean so it reads well at small size)
RAMP = "@%#*+=-:. "

def main():
    im = Image.open(SRC).convert("L")
    im = ImageOps.autocontrast(im, cutoff=1)
    im = im.filter(ImageFilter.SHARPEN)

    w, h = im.size
    rows = max(1, int(COLS * (h / w) * ASPECT))
    im_small = im.resize((COLS, rows))

    px = im_small.load()
    lines = []
    for y in range(rows):
        row_chars = []
        for x in range(COLS):
            v = px[x, y]  # 0 dark .. 255 light
            idx = int((255 - v) / 255 * (len(RAMP) - 1))
            row_chars.append(RAMP[idx])
        lines.append("".join(row_chars))

    with open("/home/claude/ascii.json", "w") as f:
        json.dump(lines, f)

    print(f"{COLS}x{rows}")
    print("\n".join(lines))

if __name__ == "__main__":
    main()
