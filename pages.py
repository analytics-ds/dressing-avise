# -*- coding: utf-8 -*-
"""Pages fixes de Dressing Avisé. Pas de coordonnées réelles inventées."""
import config as C

CRIT_TABLE = """<div class="table-wrap"><div class="table-scroll"><table><thead><tr><th>Critère</th><th>Poids</th><th>Ce que nous regardons</th></tr></thead><tbody>
<tr><td class="brand">Matières</td><td>30 %</td><td>Nature du cuir (pleine fleur, refendu, enduit), grammage de la toile, composition des tissus, doublure</td></tr>
<tr><td class="brand">Tenue dans le temps</td><td>20 %</td><td>Coutures, base des anses, coins, fermetures, avis vérifiés après six mois d'usage</td></tr>
<tr><td class="brand">Style et polyvalence</td><td>20 %</td><td>Pièce portable au-delà d'une saison, du bureau au week-end, choix de tailles et de coloris</td></tr>
<tr><td class="brand">Prix</td><td>20 %</td><td>Prix catalogue en France hors soldes, rapporté à la matière et à l'origine de fabrication</td></tr>
<tr><td class="brand">Service</td><td>10 %</td><td>Livraison, retours, boutiques en France, réparation, seconde main</td></tr>
</tbody></table></div><div class="table-note">Grille appliquée aux sacs et aux cabas. Pour le prêt-à-porter, « Tenue dans le temps » devient « Coupe et finitions ». Les poids sont rappelés en tête de chaque classement.</div></div>"""

PAGES = [
 dict(slug="a-propos", title=f"Qui sommes-nous ? La rédaction {C.NOM}", desc=f"{C.NOM}, magazine de la mode femme et de la maroquinerie premium. Qui écrit, comment nous relevons les prix, comment nous classons les marques.",
  h1="Qui sommes-nous", lead=C.BASELINE,
  sections=[
   ("Ce que nous faisons", [f"{C.NOM} compare les sacs, les cabas, le prêt-à-porter et les accessoires des maisons de mode féminine présentes en France, de la maroquinerie de créateur aux grandes maisons parisiennes. Chaque classement répond à une question que se posent nos lectrices avant d'acheter, quel cabas pour tous les jours, quel sac pour le bureau, quelle robe pour un mariage d'automne.",
                            "Nous publions un classement chaque semaine et des guides pratiques sur l'entretien du cuir, les tailles de sacs ou la construction d'une garde-robe. Tous les articles indiquent leur date de mise à jour, le nombre de marques comparées et la grille de notation."]),
   ("La rédaction", [f"{C.NOM} est écrit par une rédaction spécialisée dans la mode et la maroquinerie, qui essaie les pièces avant d'en parler. Chaque article est relu par une deuxième personne de la rédaction avant publication, et toute correction est datée en tête d'article."]),
   ("Comment nous notons", ["Cinq critères notés sur 10, pondérés dans une note globale. Les critères et leurs poids sont publiés en tête de chaque classement et ne changent pas d'un article à l'autre. Le détail est sur notre page <a href=\"../methodologie/\">méthodologie</a>."]),
   ("Contact", ["Pour signaler une erreur, demander une mise à jour d'un prix ou proposer un sujet, écrivez à la rédaction via le formulaire de la newsletter. Nous répondons sous cinq jours ouvrés et chaque correction est signalée dans l'article concerné."]),
  ]),
 dict(slug="methodologie", title=f"Comment nous classons les sacs et les marques ? Méthodologie {C.NOM}", desc="Critères, poids, sources et calendrier de mise à jour des classements Dressing Avisé. Cinq critères notés sur 10, prix relevés chaque mois sur les sites officiels.",
  h1="Notre méthodologie", lead="Les mêmes critères, les mêmes poids et les mêmes sources pour chaque classement. Voici comment une note est construite.",
  sections=[
   ("Cinq critères, des poids publiés", ["Chaque marque ou chaque modèle reçoit une note sur 10 pour cinq critères, puis une note globale pondérée. Les poids sont fixés avant le relevé et affichés en tête de l'article.", CRIT_TABLE]),
   ("D'où viennent les données", ["<ul><li>Les prix sont relevés sur les sites officiels des marques en France, hors soldes, hors ventes privées et hors code promo, à la date indiquée dans chaque tableau.</li><li>Les matières, l'origine de fabrication et les dimensions sont celles affichées sur les fiches produit, vérifiées en boutique quand c'est possible.</li><li>La tenue dans le temps s'appuie sur nos propres essais et sur les avis clients vérifiés qui décrivent l'état du produit après plusieurs mois.</li><li>Les services sont testés sur une commande réelle par marque, livraison, retour et contact du service client.</li></ul>"]),
   ("Comment se fait un essai", ["Un sac est rempli avec le même contenu pour toutes les marques, un ordinateur 14 pouces, une trousse, une gourde de 50 cl, un portefeuille et un pull fin, puis porté une semaine. Nous mesurons ce qui rentre, le confort à l'épaule par-dessus un manteau et l'état des anses à la fin.",
                                "Une robe ou une maille est portée, lavée ou nettoyée selon l'étiquette, puis comparée à son état d'origine."]),
   ("Mise à jour et corrections", ["Les classements sont revus chaque semaine et les prix relevés chaque mois. Une note ne bouge que si un relevé ou un essai la fait bouger, la flèche à côté de chaque note indique le sens de l'évolution depuis le relevé précédent.",
                                   "Une erreur signalée est corrigée sous cinq jours ouvrés, avec la date de correction en tête d'article."]),
   ("Classements avec et sans marques de mode", ["Certains de nos classements ne portent pas sur les maisons de prêt-à-porter, baskets blanches ou lingerie française par exemple. La méthode est la même, seuls les critères changent, confort et construction pour une basket, maintien et matières pour la lingerie."]),
  ]),
 dict(slug="mentions-legales", title=f"Mentions légales, {C.NOM}", desc=f"Mentions légales du site {C.NOM}.",
  h1="Mentions légales", lead="Informations légales relatives à l'édition et à l'hébergement du site.",
  sections=[
   ("Éditeur", [f"Le site {C.NOM} est édité par sa rédaction. Directeur de la publication, la rédaction {C.NOM}."]),
   ("Hébergement", ["Le site est hébergé par GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis."]),
   ("Propriété intellectuelle", ["Les textes et la structure du site sont la propriété de l'éditeur. Les logos et marques cités appartiennent à leurs propriétaires respectifs et sont reproduits à des fins d'identification des produits comparés. Les photographies proviennent de banques d'images libres de droits, la source de chaque visuel est conservée par la rédaction."]),
   ("Données personnelles", ["Le site ne dépose aucun cookie de suivi et ne collecte aucune donnée personnelle en dehors de l'adresse email volontairement transmise pour la newsletter."]),
  ]),
]
