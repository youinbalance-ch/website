YOUINBALANCE.CH – Veröffentlichung mit GitHub Pages vorbereiten

Stand: 29. Oktober 2026
Grundlage: freigegebene Demo, Version 5, inklusive aller Korrekturen vom 19. Oktober.
Zieldomain: https://youinbalance.ch/

AUFBAU
Repository: https://github.com/youinbalance-ch/website
Hosting: GitHub Pages. Infomaniak verwaltet die Domain und die DNS-Zone.
Die zwölf HTML-Seiten liegen im Hauptverzeichnis, Bilder, CSS und JavaScript
unter assets. quellcode/build.py ist die bearbeitbare Quelle der HTML-Seiten.
Sobald Pages auf main / (root) eingerichtet ist, werden Änderungen an den
veröffentlichten Dateien in main automatisch auf der Website bereitgestellt.
Das Python-Skript wird bei dieser Veröffentlichung nicht automatisch ausgeführt.

BEARBEITUNG
Texte werden in quellcode/build.py gepflegt. Mit Python 3 ausführen:
python quellcode/build.py
Dabei werden auch robots.txt und sitemap.xml neu erzeugt.
Die erzeugten HTML-Dateien zusammen mit der Quelle auf GitHub aktualisieren.
CSS und JavaScript liegen unter assets und werden direkt dort bearbeitet.

EINMALIGE EINRICHTUNG
Das Repository gehört der Organisation youinbalance-ch. Tatjana verwaltet die
Organisation als Eigentümerin. Wicki-Digital hat die Adminrolle für dieses
Repository und kann Pages, die eigene Domain und die Website-Dateien über
das eigene GitHub-Konto verwalten.
Settings > Pages > Build and deployment:
Source: Deploy from a branch; Branch: main; Folder: / (root).
Custom domain: youinbalance.ch. Zuerst auf GitHub speichern, danach DNS ändern.
Bei Infomaniak die Web-DNS-Einträge gemäss der aktuellen GitHub-Dokumentation
auf GitHub Pages umstellen; die www-Subdomain zeigt per CNAME auf
youinbalance-ch.github.io (ohne /website). E-Mail-DNS-Einträge beibehalten.
GitHub Pages stellt das HTTPS-Zertifikat bereit. Sobald verfügbar,
Enforce HTTPS aktivieren und beide Domainvarianten prüfen.
Aktuelle Anleitung:
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
Bei einer Veröffentlichung aus main erzeugt die Domain-Einstellung die
CNAME-Datei im Repository. Diese Datei bei künftigen Updates beibehalten.

OPTIONALER DATEIEXPORT
Mit Python 3 ausführen:
python quellcode/package.py
Dies erzeugt release/YouInBalance_Website_Export.zip mit den öffentlichen
HTML-Seiten, den benötigten assets, robots.txt und sitemap.xml.
Für GitHub Pages ist dieser ZIP-Export nicht erforderlich.

STAND DER VORBEREITUNG
Demo-Hinweise sind entfernt; die Seiten erlauben Suchmaschinen-Indexierung.
Canonical-Adressen und Sitemap verwenden https://youinbalance.ch/.
Die Datenschutzhinweise beschreiben GitHub Pages sowie Gmail und WhatsApp.
Das Kontaktformular öffnet einen E-Mail-Entwurf und sendet nicht automatisch.
WhatsApp ist mit 079 267 50 37 verknüpft. Rezept und Bilder sind enthalten.
Die Einrichtung von Pages, DNS und HTTPS ist noch nicht abgeschlossen.
Vor dem Abschluss Seiten, Bilder, Menü und Kontaktfunktionen unter der Domain
prüfen. Dieses Repository enthält keine Zugangsdaten.
Der bestehende Demo-Auftritt bei ChatGPT Sites wird durch Änderungen in
diesem Repository nicht verändert.
