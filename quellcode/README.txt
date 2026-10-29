Bearbeitbare Quelle der Website

build.py
  Erzeugt die zwölf öffentlichen HTML-Seiten, robots.txt und sitemap.xml.
  Texte, Angebote und sichtbare Inhalte werden hier gepflegt.

seo.py
  Seitentitel, Meta-Beschreibungen, Canonical-Adressen, Open-Graph-Angaben,
  JSON-LD, Breadcrumbs und responsive Bild-Tags.
  Zutaten und Zubereitung im Recipe-Markup werden aus dem sichtbaren Rezept
  gelesen. Es werden keine erfundenen Bewertungen, Nährwerte oder Zeiten ergänzt.

optimize_images.py
  Erzeugt responsive WebP-Varianten aus den Originalbildern im assets-Ordner
  und schreibt assets/image-manifest.json. Ausführen, wenn Originalbilder
  hinzugefügt oder ersetzt wurden. Benötigt Pillow. Die vorhandenen PNG-Icons
  bleiben auf Rechnern ohne den verwendeten Schriftfont erhalten.

package.py
  Führt den HTML-Build aus und exportiert die öffentlichen Dateien inklusive
  Bildvarianten, Icons und CNAME in release/YouInBalance_Website_Export.zip.

Normaler Ablauf:
  python quellcode/build.py
  Erzeugte HTML-Dateien und bearbeitete Quellen nach main veröffentlichen.

Nach Änderungen an Originalbildern:
  python -m pip install Pillow
  python quellcode/optimize_images.py
  python quellcode/build.py
  Auch assets/image-manifest.json und assets/responsive/ veröffentlichen.

Sitemap-lastmod wird nur bei tatsächlicher Änderung der erzeugten HTML-Seite
aktualisiert. Unveränderte Builds behalten vorhandene Zeitangaben bei.
Preisänderungen werden in den sichtbaren Angeboten in build.py gepflegt.
Das Service-Markup enthält bewusst keine separat zu wartenden Preisangaben.

CNAME mit youinbalance.ch erhalten. GitHub Pages führt Python nicht selbst aus.
Weitere Hinweise und offene externe Schritte stehen in SEO.md.
