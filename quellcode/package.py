"""Regenerate and package only public website files for Infomaniak."""
from pathlib import Path
import runpy
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent.parent
runpy.run_path(str(root / 'quellcode' / 'build.py'), run_name='__main__')
html = sorted(root.glob('*.html'))
assets = sorted(p for p in (root / 'assets').rglob('*')
                if p.is_file() and p.suffix.lower() in {'.webp', '.css', '.js'})
files = html + assets + [root / 'robots.txt', root / 'sitemap.xml']
assert len(html) == 12, 'Expected twelve HTML pages'
assert all(p.is_file() for p in files)
assert sum(p.stat().st_size for p in files) < 10_000_000, 'Starter storage limit exceeded'
out = root / 'release'
out.mkdir(exist_ok=True)
archive = out / 'YouInBalance_Infomaniak.zip'
with ZipFile(archive, 'w', ZIP_DEFLATED) as zip_file:
    for path in files:
        zip_file.write(path, path.relative_to(root).as_posix())
print(f'Ready: {archive} ({len(files)} files, {archive.stat().st_size} bytes)')
