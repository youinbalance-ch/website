"""Create responsive WebP variants and crawlable brand icons.

Run after adding/replacing original images. Requires Pillow:
    python -m pip install Pillow
    python quellcode/optimize_images.py
The ordinary HTML build remains dependency-free.
"""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / 'assets'
DEST = ASSETS / 'responsive'
DEST.mkdir(exist_ok=True)
manifest = {}
before = after = 0
for source in sorted(ASSETS.glob('*.webp')):
    with Image.open(source) as original:
        original.load()
        width, height = original.size
        sizes = sorted({min(width, size) for size in (480, 800, 1200)})
        variants = []
        for target in sizes:
            img = original.resize((target, round(height * target / width)), Image.Resampling.LANCZOS)
            path = DEST / f'{source.stem}-{target}.webp'
            img.save(path, 'WEBP', quality=80, method=6)
            variants.append({'file': path.relative_to(ASSETS).as_posix(), 'width': target})
        manifest[source.stem] = {'width': width, 'height': height, 'variants': variants}
        before += source.stat().st_size
        after += (ASSETS / variants[-1]['file']).stat().st_size
(ASSETS / 'image-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

# Keep the existing round green "tg" monogram, now at crawlable PNG URLs.
icon = Image.new('RGBA', (768, 768), (0, 0, 0, 0))
draw = ImageDraw.Draw(icon)
draw.ellipse((0, 0, 767, 767), fill='#3a5144')
font_path = Path('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf')
if not font_path.exists():
    # The checked-in icons can be kept on systems without this font.
    if not (ASSETS / 'favicon.png').exists():
        raise RuntimeError('Provide DejaVuSerif.ttf to generate the initial brand icons')
else:
    font = ImageFont.truetype(str(font_path), 408)
    draw.text((384, 363), 'tg', font=font, fill='#f7f5ed', anchor='mm')
    for name, size in [('favicon.png', 96), ('apple-touch-icon.png', 180), ('logo.png', 512)]:
        icon.resize((size, size), Image.Resampling.LANCZOS).save(ASSETS / name, optimize=True)
print(f'Images: {len(manifest)} originals, {sum(len(i["variants"]) for i in manifest.values())} responsive variants')
print(f'Largest responsive versions: {after:,} bytes vs {before:,} original bytes ({1-after/before:.0%} smaller)')
