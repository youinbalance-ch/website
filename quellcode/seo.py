"""Search metadata and shared navigation for the static public website.

Only information already published by Tatjana is used for structured data.
This module and build.py require only the Python standard library.
"""
from html import escape
from html.parser import HTMLParser
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = 'https://youinbalance.ch/'
BRAND = 'Tatjana Geiter - FIND YOUR BALANCE.'

TITLES = {
    'index': 'Tatjana Geiter | Ernährungs- & Trainingscoaching in Uezwil',
    'coaching': 'Coaching in Uezwil & online | Training, Ernährung & Alltag',
    'training': 'Individuelle Trainingspläne in Uezwil & online | Tatjana Geiter',
    'ernaehrung': 'Ernährungsberatung in Uezwil & online | Tatjana Geiter',
    'zyklus': 'Lifestyle-Coaching: Wohlbefinden & Leistung | Tatjana Geiter',
    'ueber-tatjana': 'Über Tatjana Geiter | Fitness, Ernährung & Coaching in Uezwil',
    'preise': 'Coaching-Preise: Training & Ernährungsberatung | Tatjana Geiter',
    'wissen': 'Ernährung, Training & Rezepte für den Alltag | Tatjana Geiter',
    'schoko-muffins': 'Dattel-Schoko-Muffins mit Mandeln: Rezept | Tatjana Geiter',
    'kontakt': 'Kontakt & Beratung in Uezwil | Tatjana Geiter',
    'impressum': 'Impressum | Tatjana Geiter - FIND YOUR BALANCE.',
    'datenschutz': 'Datenschutz | Tatjana Geiter - FIND YOUR BALANCE.',
}

DESCRIPTIONS = {
    'index': 'Tatjana Geiter begleitet Frauen und Männer bei Training, Ernährung und Wohlbefinden. Persönliches Coaching in Uezwil (Aargau) und online.',
    'coaching': 'Trainingsplanung, Ernährungsberatung und Lifestyle-Coaching mit Tatjana Geiter. Entdecke die Angebote für Frauen und Männer in Uezwil und online.',
    'training': 'Dein individueller Trainingsplan mit Tatjana Geiter: Muskelaufbau, Kraft und Periodisierung bis 12 Monate. In Uezwil und online, CHF 70 bis 200.',
    'ernaehrung': 'Persönliche Ernährungsberatung in Uezwil und online: Ernährungs- inkl. Supplementplan mit Tatjana Geiter für CHF 150. Erstgespräch ca. 1-2 Stunden.',
    'zyklus': 'Lifestyle-Coaching für Frauen und Männer: Ernährung, Schlaf, Regeneration, Supplemente und Wohlbefinden. In Uezwil und online, CHF 100 pro Stunde.',
    'ueber-tatjana': 'Lerne Tatjana Geiter kennen: Fitnessinstruktorin mit eidgenössischem Fachausweis, über 15 Jahre Kraftsport und persönliches Coaching in Uezwil.',
    'preise': 'Alle Coaching-Preise bei Tatjana Geiter: Trainingsplan CHF 70 bis 200, Ernährungs- inkl. Supplementplan CHF 150, Lifestyle-Beratung CHF 100 pro Stunde.',
    'wissen': 'Alltagsnahe Impulse zu Training, Ernährung und Wohlbefinden von Tatjana Geiter. Entdecke das Rezept für Dattel-Schoko-Muffins mit Mandeln.',
    'schoko-muffins': 'Dattel-Schoko-Muffins von Tatjana Geiter: Zutaten und Schritt-für-Schritt-Rezept mit Mandeln, Banane, Datteln und Ganache. Für ca. 8 Stück.',
    'kontakt': 'Beratung bei Tatjana Geiter anfragen: persönlich in 5619 Uezwil (Aargau) oder online. Kontakt per WhatsApp, Telefon oder E-Mail. Termine nach Vereinbarung.',
    'impressum': 'Anbieterinformationen, Anschrift und Kontakt von Tatjana Geiter - FIND YOUR BALANCE., Bodenacker 24, 5619 Uezwil, Schweiz.',
    'datenschutz': 'Informationen zur Datenbearbeitung auf youinbalance.ch: GitHub Pages als Hosting, Kontakt per E-Mail und WhatsApp sowie deine Datenschutzrechte.',
}

LABELS = {
    'index': 'Start', 'coaching': 'Coaching & Angebote', 'training': 'Trainingspläne',
    'ernaehrung': 'Ernährungsberatung', 'zyklus': 'Wohlbefinden & Leistung',
    'ueber-tatjana': 'Über Tatjana', 'preise': 'Preise', 'wissen': 'Wissen & Alltag',
    'schoko-muffins': 'Dattel-Schoko-Muffins', 'kontakt': 'Kontakt',
    'impressum': 'Impressum', 'datenschutz': 'Datenschutz',
}

SERVICES = {
    'training': ('Individuelle Trainingsplanung', 'Trainingspläne für Muskelaufbau und Kraft, bis zur Trainingsperiodisierung über zwölf Monate.'),
    'ernaehrung': ('Ernährungsberatung inklusive Supplementplan', 'Persönliche Ernährungsberatung und individuelle Planung für eine alltagstaugliche Ernährung.'),
    'zyklus': ('Lifestyle-Coaching für Wohlbefinden und Leistung', 'Persönliche Lifestyle-Beratung für Frauen und Männer zu Ernährung, Regeneration, Supplementen und Wohlbefinden.'),
}


def url(slug):
    return BASE + ('' if slug == 'index' else slug + '.html')


def trail(slug):
    if slug == 'index':
        return []
    middle = ['coaching'] if slug in SERVICES else ['wissen'] if slug == 'schoko-muffins' else []
    return ['index'] + middle + [slug]


def breadcrumbs(slug):
    items = trail(slug)
    if not items:
        return ''
    parts = []
    for item in items:
        label = escape(LABELS[item])
        if item == slug:
            parts.append(f'<li><span aria-current="page">{label}</span></li>')
        else:
            href = '/' if item == 'index' else item + '.html'
            parts.append(f'<li><a href="{href}">{label}</a></li>')
    return '<nav class="breadcrumb wrap" aria-label="Brotkrumennavigation"><ol>' + ''.join(parts) + '</ol></nav>'


class RecipeContent(HTMLParser):
    """Read ingredients and instructions from the rendered, visible recipe."""
    def __init__(self):
        super().__init__()
        self.aside = False
        self.in_steps = False
        self.capture = None
        self.ingredients = []
        self.steps = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'aside':
            self.aside = True
        if tag == 'ol' and 'recipe-steps' in attrs.get('class', '').split():
            self.in_steps = True
        if tag == 'li' and (self.aside or self.in_steps):
            self.capture = []

    def handle_data(self, data):
        if self.capture is not None:
            self.capture.append(data)

    def handle_endtag(self, tag):
        if tag == 'li' and self.capture is not None:
            text = ' '.join(' '.join(self.capture).split())
            (self.ingredients if self.aside else self.steps).append(text)
            self.capture = None
        if tag == 'aside':
            self.aside = False
        if tag == 'ol':
            self.in_steps = False


def service_node(slug):
    name, description = SERVICES[slug]
    return {
        '@type': 'Service', '@id': url(slug) + '#service',
        'name': name, 'description': description, 'url': url(slug),
        'provider': {'@id': BASE + '#business'},
    }


def graph(slug, body):
    page_type = {'ueber-tatjana': 'AboutPage', 'kontakt': 'ContactPage',
                 'wissen': 'CollectionPage', 'coaching': 'CollectionPage'}.get(slug, 'WebPage')
    page = {
        '@type': page_type, '@id': url(slug) + '#webpage', 'url': url(slug),
        'name': TITLES[slug], 'description': DESCRIPTIONS[slug],
        'inLanguage': 'de-CH', 'isPartOf': {'@id': BASE + '#website'},
        'publisher': {'@id': BASE + '#business'},
    }
    nodes = [page]
    if slug in ('index', 'kontakt'):
        nodes.extend([
            {'@type': 'Person', '@id': BASE + '#tatjana', 'name': 'Tatjana Geiter',
             'url': url('ueber-tatjana'), 'image': BASE + 'assets/tatjana-portrait.webp',
             'worksFor': {'@id': BASE + '#business'}},
            {'@type': 'LocalBusiness', '@id': BASE + '#business', 'name': BRAND,
             'url': BASE, 'image': BASE + 'assets/tatjana-portrait.webp',
             'logo': BASE + 'assets/logo.png', 'telephone': '+41792675037',
             'email': 'tatjana.geiter1994@gmail.com',
             'address': {'@type': 'PostalAddress', 'streetAddress': 'Bodenacker 24',
                         'postalCode': '5619', 'addressLocality': 'Uezwil',
                         'addressRegion': 'AG', 'addressCountry': 'CH'},
             'founder': {'@id': BASE + '#tatjana'},
             'description': 'Persönliches Coaching für Training, Ernährung und Wohlbefinden in Uezwil und online.'},
        ])
    if slug == 'index':
        nodes.append({'@type': 'WebSite', '@id': BASE + '#website', 'url': BASE,
                      'name': BRAND, 'alternateName': 'youinbalance.ch',
                      'inLanguage': 'de-CH', 'publisher': {'@id': BASE + '#business'}})
    if slug == 'ueber-tatjana':
        page['mainEntity'] = {'@id': BASE + '#tatjana'}
    if slug == 'kontakt':
        page['mainEntity'] = {'@id': BASE + '#business'}
    if slug in SERVICES:
        nodes.append(service_node(slug))
        page['mainEntity'] = {'@id': url(slug) + '#service'}
    if slug == 'schoko-muffins':
        recipe = RecipeContent()
        recipe.feed(body)
        if not recipe.ingredients or not recipe.steps:
            raise ValueError('Recipe structured data needs visible ingredients and instructions')
        nodes.append({
            '@type': 'Recipe', '@id': url(slug) + '#recipe', 'name': 'Dattel-Schoko-Muffins',
            'description': DESCRIPTIONS[slug], 'image': BASE + 'assets/muffins.webp',
            'author': {'@type': 'Person', '@id': BASE + '#tatjana',
                       'name': 'Tatjana Geiter', 'url': url('ueber-tatjana')},
            'recipeYield': 'ca. 8 Stück', 'cookTime': 'PT20M',
            'recipeIngredient': recipe.ingredients,
            'recipeInstructions': [
                {'@type': 'HowToStep', 'text': text, 'url': url(slug) + f'#zubereitung-{i}'}
                for i, text in enumerate(recipe.steps, 1)
            ],
            'mainEntityOfPage': {'@id': url(slug) + '#webpage'},
        })
        page['mainEntity'] = {'@id': url(slug) + '#recipe'}
    items = trail(slug)
    if items:
        crumb_id = url(slug) + '#breadcrumb'
        nodes.append({'@type': 'BreadcrumbList', '@id': crumb_id,
                      'itemListElement': [
                          {'@type': 'ListItem', 'position': i, 'name': LABELS[item], 'item': url(item)}
                          for i, item in enumerate(items, 1)]})
        page['breadcrumb'] = {'@id': crumb_id}
    return {'@context': 'https://schema.org', '@graph': nodes}


def head_html(slug, body):
    title, description = TITLES[slug], DESCRIPTIONS[slug]
    img = 'muffins.webp' if slug in ('wissen', 'schoko-muffins') else 'tatjana-portrait.webp'
    image_alt = 'Illustratives Bild der Dattel-Schoko-Muffins' if img == 'muffins.webp' else 'Tatjana Geiter - FIND YOUR BALANCE.'
    esc = lambda text: escape(text, quote=True)
    schema = json.dumps(graph(slug, body), ensure_ascii=False, separators=(',', ':')).replace('<', '\\u003c')
    return ''.join([
        '<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">',
        '<meta name="robots" content="index,follow,max-image-preview:large">',
        f'<title>{esc(title)}</title><meta name="description" content="{esc(description)}">',
        f'<link rel="canonical" href="{url(slug)}">',
        '<link rel="icon" type="image/png" sizes="96x96" href="/assets/favicon.png">',
        '<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">',
        f'<meta name="author" content="Tatjana Geiter"><meta property="og:site_name" content="{esc(BRAND)}">',
        '<meta property="og:type" content="website"><meta property="og:locale" content="de_CH">',
        f'<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}">',
        f'<meta property="og:url" content="{url(slug)}"><meta property="og:image" content="{BASE}assets/{img}">',
        f'<meta property="og:image:alt" content="{esc(image_alt)}">',
        '<meta name="twitter:card" content="summary_large_image">',
        f'<meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}">',
        f'<meta name="twitter:image" content="{BASE}assets/{img}"><meta name="twitter:image:alt" content="{esc(image_alt)}">',
        '<link rel="stylesheet" href="assets/style.css"><script src="assets/app.js" defer></script>',
        f'<script type="application/ld+json">{schema}</script>',
    ])


def image_tag(name, alt, cls=''):
    manifest = json.loads((ROOT / 'assets/image-manifest.json').read_text(encoding='utf-8'))
    info = manifest[name]
    candidates = info['variants']
    srcset = ', '.join(f"assets/{v['file']} {v['width']}w" for v in candidates)
    if 'portrait-photo' in cls:
        sizes = '(max-width: 800px) calc(100vw - 40px), (max-width: 1336px) 45vw, 580px'
    elif 'recipe' in cls:
        sizes = '(max-width: 800px) calc(100vw - 40px), (max-width: 1336px) calc(100vw - 96px), 1240px'
    elif name in ('tatjana-paris', 'tatjana-seaside', 'tatjana-roadtrip', 'tatjana-paris-arc'):
        sizes = '(max-width: 380px) calc(100vw - 40px), (max-width: 800px) 44vw, 280px'
    else:
        sizes = '(max-width: 800px) calc(100vw - 40px), (max-width: 1336px) 44vw, 580px'
    return (f'<img class="{escape(cls, quote=True)}" src="assets/{candidates[-1]["file"]}" '
            f'srcset="{srcset}" sizes="{sizes}" alt="{escape(alt, quote=True)}" '
            f'width="{info["width"]}" height="{info["height"]}" loading="lazy" decoding="async">')
