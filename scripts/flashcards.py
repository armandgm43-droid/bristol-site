#!/usr/bin/env python3
"""Conversion des flashcards Bristol (YAML) vers les paquets de l'application de révision.

Lit   matieres/<code>-<intitule>/flashcards/NN-slug.yml   (format : conventions.md § 10)
Écrit revision/cartes/<code>.json                         (un paquet par matière)
Met à jour revision/cartes/index.json                     (ajoute le paquet s'il manque)

Usage (depuis la racine du dépôt ou d'ailleurs) :
    python scripts/flashcards.py              vérifie puis écrit les paquets
    python scripts/flashcards.py --verifier   vérifie seulement, n'écrit rien

Le script s'arrête sans rien écrire au moindre problème (identifiant en double ou
retiré, type inconnu, ref introuvable, astérisque isolé, formule coupée…).

Transformations appliquées au texte des cartes :
- macros de _macros.qmd développées (\\Ts → {T_s}, \\TF → \\operatorname{TF}…), l'application ne les connaît pas ;
- lignes d'un même paragraphe jointes par une espace, comme en Markdown. Une nouvelle
  ligne commence devant une ligne « - … » et autour d'un bloc $$…$$ ; une ligne vide
  sépare deux paragraphes et est conservée.

Dépendance : PyYAML.
"""
import argparse
import json
import re
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
CARTES = RACINE / "revision" / "cartes"
MACROS = RACINE / "_macros.qmd"

TYPES = {"definition", "formule", "condition", "propriete", "methode",
         "raisonnement", "piege", "relation", "resultat", "exercice"}
SOURCES = {"officiel", "notes", "complement"}
CHAMPS_CARTE = {"id", "type", "question", "reponse", "ref", "source", "tags"}
CHAMPS_FICHIER = {"matiere", "chapitre", "cours", "ids-retires", "cartes"}
PREFIXES_HERITES = ("ts-", "res-", "ang-", "vhdl-", "cu-", "latex-")  # conventions.md § 10.3
COULEUR_DEFAUT = "#FFF0A6"

RE_LABEL = re.compile(
    r"\{[^{}\n]*?#((?:sec|eq|fig|tbl|def|thm|prp|lem|cor|exm|exr|av)-[a-z0-9-]+)[^{}\n]*\}")
RE_MATHS = re.compile(r"\$\$[\s\S]+?\$\$|\$[^$\n]+?\$")  # comme renderRich() de l'application
RE_CODE = re.compile(r"`[^`\n]+`")


class Erreurs(list):
    def ajoute(self, ou, msg):
        self.append(f"{ou} : {msg}")


def front_matter(chemin):
    texte = chemin.read_text(encoding="utf-8")
    m = re.match(r"---\s*\n(.*?)\n---\s*\n", texte, re.S)
    return (yaml.safe_load(m.group(1)) or {}) if m else {}, texte


def lire_macros():
    texte = MACROS.read_text(encoding="utf-8")
    macros = {}
    for nom, corps in re.findall(r"\\newcommand\{\\([A-Za-z]+)\}\{((?:[^{}]|\{[^{}]*\})*)\}", texte):
        macros[nom] = corps
    return macros


def developper(texte, macros):
    for nom in sorted(macros, key=len, reverse=True):
        corps = macros[nom]
        # Accolades si le corps contient un indice ou un exposant : x_\Ts → x_{T_s}.
        if "_" in corps or "^" in corps:
            corps = "{" + corps + "}"
        texte = re.sub(r"\\" + nom + r"(?![A-Za-z])", lambda m, c=corps: c, texte)
    return texte


def joindre_lignes(texte):
    """Joint les lignes d'un même paragraphe (voir l'en-tête du fichier)."""
    sortie, dans_bloc = [], False
    for brute in texte.strip().split("\n"):
        ligne = brute.strip()
        if dans_bloc:
            sortie[-1] += "\n" + ligne
            if "$$" in ligne:
                dans_bloc = False
            continue
        if not ligne:
            if sortie and sortie[-1] != "":
                sortie.append("")
            continue
        debut_bloc = ligne.startswith("$$")
        if debut_bloc and ligne.count("$$") == 1:
            dans_bloc = True
        nouvelle = (not sortie or sortie[-1] == "" or debut_bloc or ligne.startswith("- ")
                    or sortie[-1].rstrip().endswith("$$"))
        if nouvelle:
            sortie.append(ligne)
        else:
            sortie[-1] += " " + ligne
    return "\n".join(sortie).strip()


def controler_texte(texte, ou, err):
    sans_code = RE_CODE.sub("", texte)
    reste = RE_MATHS.sub("", sans_code)
    if "$" in reste:
        err.ajoute(ou, "« $ » non apparié (formule en ligne coupée sur deux lignes ?)")
    for ligne in reste.split("\n"):
        if ligne.replace("**", "").count("*") % 2:
            err.ajoute(ou, f"astérisque isolé : {ligne.strip()[:60]}")


def labels_du_cours(chemin):
    return set(RE_LABEL.findall(chemin.read_text(encoding="utf-8")))


def charger_matiere(dossier, macros, err):
    """Renvoie (code, nom du paquet, liste d'items) pour une matière."""
    fichiers = sorted((dossier / "flashcards").glob("*.yml"))
    if not fichiers:
        return None
    fiche, _ = front_matter(dossier / "index.qmd")
    code_dossier = dossier.name.split("-")[0]
    chapitres, retires, vus = [], set(), {}
    for f in fichiers:
        ou = f.relative_to(RACINE).as_posix()
        donnees = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        inconnus = set(donnees) - CHAMPS_FICHIER
        if inconnus:
            err.ajoute(ou, f"champs inconnus {sorted(inconnus)}")
        if donnees.get("matiere") != code_dossier:
            err.ajoute(ou, f"matiere « {donnees.get('matiere')} » ≠ dossier « {code_dossier} »")
        if not isinstance(donnees.get("chapitre"), int):
            err.ajoute(ou, "chapitre manquant ou non entier")
            continue
        cours = dossier / str(donnees.get("cours", ""))
        if not cours.is_file():
            err.ajoute(ou, f"cours introuvable : {donnees.get('cours')}")
            continue
        if f.stem != cours.stem:
            err.ajoute(ou, f"le fichier doit porter le nom du chapitre ({cours.stem}.yml)")
        retires |= set(donnees.get("ids-retires") or [])
        chapitres.append((donnees["chapitre"], f, ou, donnees, cours))

    items = []
    for num, f, ou, donnees, cours in sorted(chapitres, key=lambda c: c[0]):
        fm, _ = front_matter(cours)
        chap = f"Ch. {num:02d} — {fm.get('title', cours.stem)}"
        labels = labels_du_cours(cours)
        for i, carte in enumerate(donnees.get("cartes") or []):
            cid = str(carte.get("id", ""))
            ici = f"{ou}, carte {i + 1} ({cid or 'sans id'})"
            for champ in ("id", "type", "question", "reponse", "ref"):
                if not carte.get(champ):
                    err.ajoute(ici, f"champ obligatoire « {champ} » manquant")
            inconnus = set(carte) - CHAMPS_CARTE
            if inconnus:
                err.ajoute(ici, f"champs inconnus {sorted(inconnus)}")
            if not re.fullmatch(rf"{re.escape(code_dossier)}-[a-z0-9]+(-[a-z0-9]+)*", cid):
                err.ajoute(ici, f"identifiant non conforme (attendu {code_dossier}-<slug>)")
            if cid.startswith(PREFIXES_HERITES):
                err.ajoute(ici, "préfixe réservé à un paquet hérité")
            if cid in vus:
                err.ajoute(ici, f"identifiant déjà utilisé ({vus[cid]})")
            if cid in retires:
                err.ajoute(ici, "identifiant retiré (ids-retires) : ne jamais le réutiliser")
            vus[cid] = ou
            if carte.get("type") not in TYPES:
                err.ajoute(ici, f"type inconnu « {carte.get('type')} »")
            if carte.get("source") is not None and carte.get("source") not in SOURCES:
                err.ajoute(ici, f"source inconnue « {carte.get('source')} »")
            ref = str(carte.get("ref", ""))
            if "#" in ref:
                autre, label = ref.split("#", 1)
                cible = cours.parent / autre
                if not cible.is_file() or label not in labels_du_cours(cible):
                    err.ajoute(ici, f"ref introuvable : {ref}")
            elif ref and ref not in labels:
                err.ajoute(ici, f"ref introuvable dans {cours.name} : {ref}")
            faces = []
            for champ in ("question", "reponse"):
                texte = joindre_lignes(str(carte.get(champ, "")))
                controler_texte(texte, f"{ici}, {champ}", err)
                faces.append(developper(texte, macros))
            items.append({"key": cid, "chap": chap, "front": faces[0], "back": faces[1]})
    return code_dossier, fiche.get("title", code_dossier), items


def ecrire(chemin, contenu):
    ancien = chemin.read_text(encoding="utf-8") if chemin.is_file() else None
    if ancien == contenu:
        return False
    chemin.write_text(contenu, encoding="utf-8", newline="\n")
    return True


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--verifier", action="store_true", help="vérifier seulement, sans rien écrire")
    args = ap.parse_args()

    macros, err, paquets = lire_macros(), Erreurs(), []
    for dossier in sorted((RACINE / "matieres").iterdir()):
        if dossier.is_dir() and (dossier / "flashcards").is_dir():
            res = charger_matiere(dossier, macros, err)
            if res:
                paquets.append(res)

    if err:
        print(f"{len(err)} problème(s), rien n'a été écrit :")
        for e in err:
            print("  - " + e)
        return 1
    for code, nom, items in paquets:
        print(f"{code} : {len(items)} cartes vérifiées")
    if args.verifier:
        return 0

    index_chemin = CARTES / "index.json"
    index = json.loads(index_chemin.read_text(encoding="utf-8")) if index_chemin.is_file() else []
    for code, nom, items in paquets:
        chemin = CARTES / f"{code}.json"
        couleur, anciennes = COULEUR_DEFAUT, set()
        if chemin.is_file():
            ancien = json.loads(chemin.read_text(encoding="utf-8"))
            couleur = ancien.get("color", COULEUR_DEFAUT)
            anciennes = {it.get("key") for it in ancien.get("items", [])}
        paquet = {"deck": nom, "color": couleur, "items": items}
        modifie = ecrire(chemin, json.dumps(paquet, ensure_ascii=False, indent=2) + "\n")
        cles = {it["key"] for it in items}
        print(f"  {chemin.relative_to(RACINE).as_posix()} : {'écrit' if modifie else 'inchangé'}"
              f" ({len(cles - anciennes)} nouvelles clés, {len(anciennes - cles)} clés disparues)")
        if f"{code}.json" not in index:
            index.append(f"{code}.json")
    if ecrire(index_chemin, json.dumps(index, ensure_ascii=False, indent=2) + "\n"):
        print("  revision/cartes/index.json : mis à jour")
    return 0


if __name__ == "__main__":
    sys.exit(main())
