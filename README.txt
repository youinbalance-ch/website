YOUINBALANCE.CH – Veröffentlichung bei Infomaniak vorbereiten

Stand: 29. Oktober 2026
Grundlage: freigegebene Demo, Version 5, inklusive aller Korrekturen vom 19. Oktober.
Zieldomain: https://youinbalance.ch/

AUFBAU
Repository: https://github.com/Tatjanavivg/website
Hosting: Infomaniak Starter (10 MB Speicherplatz).
Die zwölf HTML-Seiten liegen im Hauptverzeichnis, Bilder, CSS und JavaScript
unter assets. quellcode/build.py ist die bearbeitbare Quelle der HTML-Seiten.
GitHub dient der Versionierung; Infomaniak liefert die Website aus.
Ein Commit auf GitHub wird derzeit noch nicht automatisch zu Infomaniak
übertragen. Nach einer Änderung muss auch der Hosting-Stand aktualisiert werden.

BEARBEITUNG
Texte werden in quellcode/build.py gepflegt. Mit Python 3 ausführen:
python quellcode/build.py
Dabei werden auch robots.txt und sitemap.xml neu erzeugt.
Die erzeugten HTML-Dateien zusammen mit der Quelle auf GitHub aktualisieren.
CSS und JavaScript liegen unter assets und werden direkt dort bearbeitet.

VERÖFFENTLICHUNGSPAKET
Mit Python 3 ausführen:
python quellcode/package.py
Dies erzeugt release/YouInBalance_Infomaniak.zip. Die ZIP enthält nur die
öffentlichen HTML-Seiten, die benötigten assets, robots.txt und sitemap.xml.
Die ZIP nach dem Hochladen auf Infomaniak im Website-Verzeichnis entpacken;
index.html muss direkt dort liegen. Das hochgeladene Archiv anschliessend
entfernen. README.txt, quellcode und das Git-Repository gehören nicht ins
öffentliche Website-Verzeichnis. Vorhandene Hosting-Dateien vorab sichern.

STAND DER VORBEREITUNG
Demo-Hinweise sind entfernt; die Seiten erlauben Suchmaschinen-Indexierung.
Canonical-Adressen und Sitemap verwenden https://youinbalance.ch/.
Die Datenschutzhinweise beschreiben Infomaniak sowie Gmail und WhatsApp.
Das Kontaktformular öffnet einen E-Mail-Entwurf und sendet nicht automatisch.
WhatsApp ist mit 079 267 50 37 verknüpft. Rezept und Bilder sind enthalten.

NOCH BEIM HOSTING ZU PRÜFEN
SSL-Zertifikat für youinbalance.ch und www.youinbalance.ch fertigstellen.
HTTPS und die Weiterleitung von www auf die Hauptadresse einrichten.
Seiten, Bilder, Menü und Kontaktfunktionen unter der Domain prüfen.
Dieses Repository enthält keine Zugangsdaten und keine automatische
Bereitstellung. Der bestehende Demo-Auftritt bei ChatGPT Sites wird durch
die Änderungen in diesem Repository nicht verändert.
