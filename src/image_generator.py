from PIL import Image, ImageDraw, ImageFont
from .config import IMAGES_DIR, FONT_PATH

WIDTH, HEIGHT = 1280, 720
BACKGROUND = (10, 10, 10)
TEXT_COLOR = (245, 245, 245)
PADDING = 100


def wrap_text(text, font, max_width, draw):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines


def create_image(text, output_file):
    img = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(img)

    font = ImageFont.truetype(str(FONT_PATH), size=56)
    max_text_width = WIDTH - 2 * PADDING

    lines = wrap_text(text, font, max_text_width, draw)

    line_height = font.getbbox("Ay")[3]
    total_text_height = line_height * len(lines)
    y = (HEIGHT - total_text_height) // 2

    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        x = (WIDTH - bbox[2]) // 2
        draw.text((x, y), line, fill=TEXT_COLOR, font=font)
        y += line_height + 10

    img.save(output_file)
