# -*- coding: utf-8 -*-
"""Pages fixes : a-propos/, methodologie/ et mentions-legales/ (un paragraphe qui commence par « < » est inséré tel quel, pour un tableau ou une liste), depuis pages.py (PAGES).
Chaque page : dict(slug, title, desc, h1, lead, sections=[(h2, [paragraphes])])."""
import os
import config as C
from common import head, header, footer, strip, jsonld, org, write
from pages import PAGES
from linkify import linkify

import re, unicodedata
def sid(t):
    t = unicodedata.normalize("NFD", strip(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def render(p):
    R = "../"
    url = f'{C.SITE}/{p["slug"]}/'
    body = "".join(f'<h2 id="{sid(h2)}">{h2}</h2>' + "".join(x if x.lstrip().startswith("<") else f"<p>{x}</p>" for x in ps) for h2, ps in p["sections"])
    ld = jsonld(org(), {"@context": "https://schema.org", "@type": "WebPage", "name": strip(p["title"]), "url": url, "inLanguage": "fr-FR"})
    return f'''<!doctype html>
<html lang="{C.LANG}">
<head>
{head(R, p["title"], p["desc"], url, ld)}</head>
<body>

{header(R, scrolled=True)}

<section class="art-head" style="padding-top:110px">
  <div class="wrap">
    <div class="art-card" style="margin-top:0">
      <nav class="crumbs" aria-label="Fil d'Ariane"><a href="{R}">Accueil</a><i></i><span>{strip(p["h1"])}</span></nav>
      <h1>{p["h1"]}</h1>
      <p class="art-lead">{p["lead"]}</p>
    </div>
  </div>
</section>

<section class="art-body">
  <div class="wrap">
    <article class="prose" style="max-width:820px">
      {body}
    </article>
  </div>
</section>

{footer(R)}
</body>
</html>
'''

if __name__ == "__main__":
    for p in PAGES:
        write(os.path.join(p["slug"], "index.html"), linkify(render(p), "../"))
