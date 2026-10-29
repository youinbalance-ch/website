# Suchmaschinen-Optimierung für youinbalance.ch

Stand der Prüfung: 29. Oktober 2026. Grundlage: GitHub-main
`3de154ffb736f22d666a6a38e106974858315448`.

## Bereits funktionierende Grundlage

- Die Hauptdomain, robots.txt und XML-Sitemap antworten über HTTPS mit HTTP 200.
- HTTP und www führen zur HTTPS-Hauptdomain.
- Nicht vorhandene Seiten liefern einen echten HTTP-404-Status.
- Die zwölf Seiten enthalten indexierbaren HTML-Text, individuelle Beschreibungen
  und Canonical-Adressen für die endgültige Domain.

## Enthaltene Verbesserungen

| Bereich | Änderung und Zweck |
| --- | --- |
| Titel und Beschreibungen | Jede der zwölf Seiten erhält eine eigene, konkrete Beschreibung. Beispiel Startseite: «Tatjana Geiter \| Ernährungs- & Trainingscoaching in Uezwil» statt nur «FIND YOUR BALANCE.» |
| Sichtbare Inhalte | Klarere Leistungsüberschriften und Standortbezug zu Uezwil im Aargau. Training und Ernährungsberatung erklären Ablauf und Umfang ausführlicher und verlinken verwandte Angebote. |
| Zuordnung von Tatjana und ihrem Angebot | JSON-LD für Person, LocalBusiness, WebSite, WebPage und die drei Dienstleistungen. Kontaktdaten stimmen mit den sichtbaren Angaben überein. |
| Rezept | Recipe-Markup mit Autorin, Bild, zwölf Zutatenangaben, sechs sichtbaren Arbeitsschritten, ca. acht Stück Ausbeute und 20 Minuten Backzeit. Keine erfundenen Bewertungen oder Nährwerte. |
| Navigation | Sichtbare Breadcrumbs und BreadcrumbList-Markup auf Unterseiten; Startseitenlinks führen direkt auf die kanonische Adresse /. |
| Bilder und Ladeverhalten | 51 responsive WebP-Varianten mit srcset/sizes und korrekten Seitenverhältnissen. Wichtige erste Bilder werden priorisiert, weiter unten platzierte Bilder verzögert geladen. Die jeweils grössten Varianten der 17 Originalbilder sind zusammen 47 % kleiner. Dies ist ein Grössenvergleich, keine gemessene Ladezeitverbesserung oder Core-Web-Vitals-Bewertung. |
| Such- und Teilenansicht | Abrufbare PNG-Favicons statt einer reinen Daten-URL; passende Vorschau-Metadaten und Bilder für geteilte Links. |
| Entdeckung neuer Inhalte | Sitemap mit den zwölf kanonischen URLs und lastmod nur bei tatsächlich geänderten HTML-Inhalten. robots.txt verweist auf die Sitemap und spart Quellcode-/Exportverzeichnisse vom Crawling aus. |
| Pflege | Der Generator und der Dateiexport enthalten die Verbesserungen; künftige Builds erhalten diese Angaben und die CNAME-Datei. |

## Prüfung vor der Veröffentlichung

- Alle zwölf HTML-Seiten auf genau eine Hauptüberschrift, Titel, Beschreibung,
  Canonical-Adresse und lesbares JSON-LD geprüft.
- Sämtliche lokalen Links, Bilddateien, srcset-Kandidaten und Rezeptanker geprüft.
- Alle zwölf Seiten sind über interne Links von der Startseite erreichbar.
- Das sichtbare Rezept und die Arbeitsschritte wurden mit der bisherigen Version
  verglichen; Inhalt und Kontaktziele bleiben erhalten.
- Ein wiederholter Build erzeugt unveränderte Dateien und unveränderte lastmod-Werte.
- Browser-Prüfung der Desktop-Startseite und aller zwölf Seiten bei schmaler
  Darstellung: kein horizontaler Überlauf, keine bereits geladenen defekten Bilder.
- Das mobile Menü wurde geöffnet und geschlossen; die Navigation ist bedienbar.

Das ist eine technische und inhaltliche Prüfung. Es liegen weder Search-Console-
Leistungsdaten noch ein bestandener externer Google-Rich-Results-Test oder
gemessene Core-Web-Vitals-Daten vor. Google und Bing entscheiden selbst über
Indexierung, angezeigte Suchergebnisse und Platzierungen.

## Nach der Veröffentlichung

1. Den erfolgreichen GitHub-Pages-Lauf und die neuen Titel unter der Live-Domain
   prüfen; auch favicon.png und die neuen Bildvarianten müssen HTTP 200 liefern.
2. Die Domain in Google Search Console bestätigen, falls noch keine passende
   Property besteht. Sitemap `https://youinbalance.ch/sitemap.xml` einreichen und
   Startseite sowie Leistungsseiten über die URL-Prüfung kontrollieren.
3. Bing Webmaster Tools einrichten bzw. die vorhandene bestätigte Property
   verwenden und dieselbe Sitemap einreichen. Die Website funktioniert ebenso
   für andere Crawler, die den üblichen HTML-, Sitemap- und robots.txt-Regeln folgen.
4. Ein bestehendes Google-Unternehmensprofil mit korrekter Coaching-Leistung,
   Domain und Kontaktangaben pflegen bzw. bei Berechtigung ein passendes Profil
   anlegen und bestätigen. Echte Kundenrezensionen und aktuelle eigene Inhalte
   ergänzen; keine Bewertungen oder Standorte erfinden.
5. Für Search Console, Webmaster Tools und Unternehmensprofil eigene Zugriffe
   vergeben lassen. GitHub-/Infomaniak-Rechte gewähren keinen automatischen
   Zugriff auf diese getrennten Konten.

Diese externen Kontoschritte wurden in dieser Überarbeitung nicht ausgeführt.
Ein vorhandenes Profil oder eine bestehende Search-Console-Property wurde nicht
als fehlend angenommen. Die Überarbeitung ist erst mit dem veröffentlichten
GitHub-Commit auf der Live-Website aktiv.

## Offizielle Grundlagen

- [Google: Seitentitel](https://developers.google.com/search/docs/appearance/title-link)
- [Google: Unternehmensdaten](https://developers.google.com/search/docs/appearance/structured-data/local-business)
- [Google: Rezeptdaten](https://developers.google.com/search/docs/appearance/structured-data/recipe)
- [Google: Richtlinien für strukturierte Daten](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google: Sitemap erstellen und einreichen](https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap)
- [Google: Favicons](https://developers.google.com/search/docs/appearance/favicon-in-search)
- [Google: Lokale Auffindbarkeit](https://support.google.com/business/answer/7091?hl=de)
- [Google/web.dev: Bilder laden und Abmessungen festlegen](https://web.dev/articles/browser-level-image-lazy-loading)
- [Bing: Webmaster-Richtlinien](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)
