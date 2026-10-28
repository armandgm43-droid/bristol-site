"""Applique les modifications de la refonte à _quarto.yml, sans toucher aux
barres latérales (sidebar) ni au reste. Idempotent. Usage : python3 patch_quarto_yml.py _quarto.yml"""
import sys, re

path = sys.argv[1]
s = open(path, encoding="utf-8").read()
orig = s

def sub1(pattern, repl, flags=0):
    global s
    new, n = re.subn(pattern, repl, s, count=1, flags=flags)
    if n != 1:
        raise SystemExit(f"motif introuvable : {pattern[:60]!r}")
    s = new

if "pre-render:" not in s:
    # 1. pre-render + ressources
    sub1(r"(  render:\n(?:    - .*\n)+)",
         r"""\1  # Avant chaque rendu complet : catalogue des matières (accueil, page des
  # annales, en-têtes des chapitres). Script Deno fourni par Quarto, aucune
  # dépendance. Voir architecture.md § 4 et scripts/catalogue.ts.
  pre-render: scripts/catalogue.ts
""")
    sub1(r"(    # Jetons de DA : aussi lus par revision/index\.html \(\.\./assets/bristol-tokens\.css\)\.\n    - \"assets/bristol-tokens\.css\"\n)",
         r"""\1    # Polices Geist auto-hébergées (lues par bristol-tokens.css).
    - "assets/fonts/**"
""")

    # 2. Navigation : Matières, Annales, Révisions ; recherche en champ texte ; pied de page
    sub1(r"  search: true\n",
         """  search:
    location: navbar
    type: textbox
    copy-button: false
""")
    sub1(r"  navbar:\n    left:\n(?:      - .*\n        href: .*\n)+",
         """  navbar:
    left:
      - text: "Matières"
        href: index.qmd
      - text: "Annales"
        href: annales.qmd
      - text: "Révisions"
        href: revision/index.html
  page-footer:
    left: "Bristol · cours, annales et flashcards"
    right:
      - text: "Conventions de lecture"
        href: demo-conventions.qmd
""")

    # 3. Thème
    sub1(r"      light: \[cosmo, assets/bristol\.scss\]\n      dark: \[cosmo, assets/bristol\.scss, assets/bristol-sombre\.scss\]\n",
         """      light: [default, assets/bristol.scss]
      dark: [default, assets/bristol.scss, assets/bristol-sombre.scss]
""")
    sub1(r"(    css: assets/bristol-tokens\.css\n)",
         r"""\1    # Contexte des chapitres et des matières (en-tête, « Pour continuer »),
    # script du site (assets/bristol.js) : voir assets/bristol.lua.
    filters:
      - assets/bristol.lua
    template-partials:
      - assets/partials/title-block.html
    grid:
      sidebar-width: 272px
      body-width: 760px
      margin-width: 232px
      gutter-width: 2.5rem
    smooth-scroll: true
""")

if "search-text-placeholder" not in s:
    sub1(r"(lang: fr\n)", r"""\1language:
  search-text-placeholder: "Rechercher…"
""")

if s != orig:
    open(path, "w", encoding="utf-8", newline="").write(s)
    print("_quarto.yml modifié")
else:
    print("déjà à jour")
