# The Swiss Tree: copia calcada de la portada y textos legales; sin el spam inyectado en el WordPress
DOMAIN = "theswisstree.com"
PAGES = {"": "", "aviso-legal-y-privacidad/": "aviso-legal-y-privacidad/", "politica-de-cookies/": "politica-de-cookies/"}
REDIRECTS = {p: "" for p in ["the-swiss-tree/", "home-hina/", "home2/", "dental-clinic/", "home/", "sample-page/", "hello-world/",
                              "terms-and-conditions/", "legal-notice/", "privacy-policy/", "category/", "author/"]}
REDIRECTS["legal-notice/"] = "aviso-legal-y-privacidad/"
REDIRECTS["privacy-policy/"] = "aviso-legal-y-privacidad/"
REDIRECTS["terms-and-conditions/"] = "aviso-legal-y-privacidad/"
EXTERNAL = {}
INSTAGRAM = "https://www.instagram.com/theswisstree/"
INSTAGRAM_TXT = "Ver The Swiss Tree en Instagram"
EVENTON_STATIC = None
WA = "https://wa.me/34644632663"
BOTONES = ('<div class="elementor-widget-container" style="text-align:center;display:flex;gap:12px;justify-content:center;flex-wrap:wrap;padding:12px 0">'
           f'<a class="elementor-button elementor-button-link elementor-size-sm" href="{WA}" target="_blank" rel="noopener">'
           '<span class="elementor-button-content-wrapper"><span class="elementor-button-text">ESCRÍBENOS POR WHATSAPP</span></span></a>'
           '<a class="elementor-button elementor-button-link elementor-size-sm" href="mailto:info@theswisstree.com?subject=Proyecto">'
           '<span class="elementor-button-content-wrapper"><span class="elementor-button-text">ESCRÍBENOS POR CORREO</span></span></a></div>')
WIDGETS = {"elementor-widget-form": BOTONES}
SUBS = [
    # bloque oculto de enlaces basura (inyectado en el WordPress hackeado)
    (r'<div style="overflow: hidden; height: 1px;">.*?</div>', ''),
    (r'href="tel:=\+?34(\d{9})"', r'href="tel:+34\1"'),
]
EXTRA_PAGES = []
LIVE_JSON = None
