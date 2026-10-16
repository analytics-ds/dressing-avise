# -*- coding: utf-8 -*-
"""Identité du média et textes transverses. UN SEUL endroit à remplir pour tout ce qui
n'est pas du contenu éditorial (nom, baseline, CTA, méthode, critères du comparateur).

Rempli par Claude à l'étape 4 de la skill pbn-ao-geo. Tout ce qui est marqué OBLIGATOIRE
doit être adapté au secteur : la QA (check_site.py) refuse les valeurs d'exemple.
"""

# ------------------------------------------------------------------ identité
NOM = "Dressing Avisé"
SLUG = "dressing-avise"                      # OBLIGATOIRE nom du dossier et du repo GitHub (ascii, minuscules, tirets)
OWNER = "analytics-ds"                    # compte GitHub qui héberge le repo (rempli par scripts/prereqs.sh)
SITE = f"https://{OWNER}.github.io/{SLUG}"  # racine publique, sans slash final (canonical, JSON-LD, sitemap)
LANG = "fr"
ACCENT = "#123B2F"                        # couleur d'accent, réécrite par scripts/recolor.py (theme-color)
CSS_V = "8"                               # cache-buster des assets

# ------------------------------------------------------------------ vocabulaire
UNIT = "marques"
UNIT_ONE = "marque"
CTA = "Comparer 2 marques"
CTA_LONG = "Comparer deux marques"
BASELINE = "Le magazine des sacs, du prêt-à-porter et des accessoires féminins premium. Nous essayons, nous relevons, nous classons."
TAGLINE_FOOTER = "Le magazine de la mode femme et de la maroquinerie premium."
AUTHOR = "La rédaction Dressing Avisé"
AUTHOR_INITIAL = "D"

# Liste « Marques » du pied de page : (libellé, href). Mettre le client en premier.
FOOTER_BRANDS = [("Sézane", "pret-a-porter/"), ("Polène", "sacs/"), ("Longchamp", "cabas/"), ("ba&amp;sh", "cadeaux/")]

# ------------------------------------------------------------------ textes transverses
NEWSLETTER_P = "Un email le vendredi, le classement de la semaine, les nouveaux comparatifs et les pièces qui reviennent en stock."
NEWSLETTER_NOTE = "Un email par semaine, désinscription en un clic."
ASIDE_NEWS_P = "Le classement de la semaine et les nouveaux comparatifs, chaque vendredi."

# Encart « Notre méthode » en bas de chaque article. OBLIGATOIRE : 5 puces propres au secteur.
METHOD_INTRO = "Ce classement repose sur des relevés faits sur les sites officiels et en boutique, refaits chaque mois."
METHOD_ITEMS = [
 "Les prix sont relevés sur les sites officiels des marques en France, hors soldes et hors code promo, à la date indiquée",
 "Les matières, l'origine de fabrication et les dimensions sont celles affichées sur les fiches produit",
 "Chaque sac est porté et rempli en conditions réelles, ordinateur, trousse, gourde et parapluie compris",
 "Les avis clients vérifiés sont lus un par un sur la tenue des anses, des coins et des finitions",
 "Les services (livraison, retours, réparation, seconde main) sont testés sur une commande réelle par marque",
]

# Critères du comparateur 2 entités de l'accueil : 5 critères, le dernier est la note globale.
CRITERIA = [
 ("Prix", "rapport entre le prix et ce que l'on reçoit"),
 ("Matières", "cuir, toile, soie, laine et finitions"),
 ("Style", "pièces qui durent au-delà d'une saison"),
 ("Service", "livraison, retours, boutiques, réparation"),
 ("Note globale", "moyenne pondérée"),
]

# Liens internes supplémentaires pour linkify : (fragment de titre présent dans le libellé du lien, chemin).
# Les titres complets des articles publiés sont branchés automatiquement.
EXTRA_LINKS = []

# Google Fonts : réécrit par scripts/recolor.py --display/--text
FONTS_HREF = "https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700;800&family=Inter:wght@300;400;500;600&display=swap"
COMPARED = "comparées"                  # accord du participe dans l en-tête d article : comparées (marques), comparés (comptes, contrats)
