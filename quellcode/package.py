"""Regenerate and export the public website files independently of GitHub Pages."""
from pathlib import Path
import runpy
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent.parent
runpy.run_path(str(root / 'quellcode' / 'build.py'), run_name='__main__')
html = sorted(root.glob('*.html'))
assets = sorted(p for p in (root / 'assets').rglob('*')
                if p.is_file() and p.suffix.lower() in {'.webp', '.css', '.js', '.png', '.svg', '.ico', '.json'})
files = html + assets + [root / 'robots.txt', root / 'sitemap.xml', root / 'CNAME']
assert len(html) == 12, 'Expected twelve HTML pages'
assert all(p.is_file() for p in files)
out = root / 'release'
out.mkdir(exist_ok=True)
archive = out / 'YouInBalance_Website_Export.zip'
with ZipFile(archive, 'w', ZIP_DEFLATED) as zip_file:
    for path in files:
        zip_file.write(path, path.relative_to(root).as_posix())
print(f'Ready: {archive} ({len(files)} files, {archive.stat().st_size} bytes)')
