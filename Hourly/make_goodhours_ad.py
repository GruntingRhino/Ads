from PIL import Image, ImageDraw, ImageFont
from math import sin, pi

W, H = 1080, 1920
font_bold = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
font_reg = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'

slides = [
    ("Students need hours. Fast.", "GoodHours makes volunteering easy.", '0F172A', '38BDF8'),
    ("Schools get cleaner tracking.", "No more spreadsheet chaos.", '0B4F6C', '67E8F9'),
    ("Students, parents, and staff stay in sync.", "One simple workflow.", '14532D', '86EFAC'),
    ("Built for real schools.", "Book a demo • Start faster with GoodHours", '312E81', 'C4B5FD'),
]

for i, (headline, sub, bg_hex, accent_hex) in enumerate(slides, start=1):
    bg = tuple(int(bg_hex[j:j+2], 16) for j in (0, 2, 4))
    accent = tuple(int(accent_hex[j:j+2], 16) for j in (0, 2, 4))
    img = Image.new('RGB', (W, H), bg)
    d = ImageDraw.Draw(img)

    # soft abstract shapes
    for y in range(H):
        # simple vertical gradient overlay
        alpha = y / H
        r = int(bg[0] * (1 - 0.12 * alpha) + 8 * alpha)
        g = int(bg[1] * (1 - 0.12 * alpha) + 10 * alpha)
        b = int(bg[2] * (1 - 0.12 * alpha) + 18 * alpha)
        d.line((0, y, W, y), fill=(r, g, b))

    # accent circles and bars
    d.ellipse((-160, 120, 420, 700), fill=(*accent, 40))
    d.ellipse((700, 1380, 1260, 1940), fill=(*accent, 38))
    d.rounded_rectangle((80, 170, 270, 250), radius=30, fill=(*accent, 70))
    d.rounded_rectangle((760, 180, 1010, 260), radius=30, fill=(255, 255, 255, 18))
    d.polygon([(0, 1280), (260, 1080), (420, 1180), (0, 1500)], fill=(*accent, 28))
    d.polygon([(1080, 610), (860, 480), (700, 590), (1080, 860)], fill=(255, 255, 255, 16))

    # faux app card
    card = (90, 640, 990, 1340)
    d.rounded_rectangle(card, radius=48, fill=(255, 255, 255), outline=(255, 255, 255), width=2)
    d.rounded_rectangle((120, 680, 960, 730), radius=20, fill=(240, 244, 255))
    d.rounded_rectangle((120, 760, 720, 1140), radius=36, fill=(244, 247, 251))
    d.rounded_rectangle((760, 760, 960, 1140), radius=36, fill=(238, 244, 250))
    d.rounded_rectangle((120, 1180, 960, 1300), radius=30, fill=(245, 250, 246))

    # header tag
    try:
        fb = ImageFont.truetype(font_bold, 44)
        f1 = ImageFont.truetype(font_bold, 84)
        f2 = ImageFont.truetype(font_reg, 42)
        f3 = ImageFont.truetype(font_reg, 32)
    except Exception:
        fb = ImageFont.load_default()
        f1 = fb
        f2 = fb
        f3 = fb

    brand = "GOODHOURS"
    bbox = d.textbbox((0, 0), brand, font=fb)
    pad = 22
    d.rounded_rectangle((80, 80, 80 + (bbox[2]-bbox[0]) + pad*2, 80 + (bbox[3]-bbox[1]) + pad*2), radius=28, fill=(255,255,255))
    d.text((80 + pad, 80 + pad - 4), brand, fill=bg, font=fb)

    # headline shadow + text
    tx = 120
    ty = 300
    for off in [(0, 5)]:
        d.text((tx+off[0], ty+off[1]), headline, fill=(0,0,0), font=f1, spacing=16)
    d.text((tx, ty), headline, fill=(255,255,255), font=f1, spacing=16)

    # subheadline panel
    sub_box = (120, 470, 960, 580)
    d.rounded_rectangle(sub_box, radius=28, fill=(0,0,0,70))
    sbbox = d.textbbox((0,0), sub, font=f2)
    sx = (W - (sbbox[2]-sbbox[0]))//2
    d.text((sx, 498), sub, fill=(255,255,255), font=f2)

    # fake UI lines / elements inside card
    d.rounded_rectangle((160, 810, 660, 870), radius=20, fill=accent)
    d.rounded_rectangle((160, 910, 590, 960), radius=18, fill=(210, 217, 228))
    d.rounded_rectangle((160, 980, 500, 1030), radius=18, fill=(210, 217, 228))
    d.rounded_rectangle((760, 810, 920, 860), radius=20, fill=(234, 240, 246))
    d.rounded_rectangle((760, 900, 920, 950), radius=20, fill=(234, 240, 246))
    d.rounded_rectangle((760, 990, 920, 1040), radius=20, fill=(234, 240, 246))

    # bottom CTA strip
    d.rounded_rectangle((120, 1180, 960, 1300), radius=30, fill=(255,255,255))
    cta_text = 'Start faster with GoodHours' if i == 4 else 'Built for school workflows'
    ctabox = d.textbbox((0,0), cta_text, font=f3)
    cx = (W - (ctabox[2]-ctabox[0]))//2
    d.text((cx, 1220), cta_text, fill=bg, font=f3)

    # footer
    footer = 'social ad test • vertical 9:16'
    fbox = d.textbbox((0,0), footer, font=f3)
    d.text(((W - (fbox[2]-fbox[0]))//2, 1780), footer, fill=(255,255,255), font=f3)

    img.save(f'/tmp/goodhours_slide_{i}.png')
    print(f'Wrote /tmp/goodhours_slide_{i}.png')
