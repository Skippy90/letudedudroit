"""Télécharge un recueil sur Fedlex et affiche le texte en vigueur de certains articles.

Usage :
    python tools/fedlex.py cp 2026-10-01 1 2 12 123
    python tools/fedlex.py cp 2026-10-01 --compare 2026-11-01 1 2 12   # signale les articles qui changent
    python tools/fedlex.py cc en-vigueur 302                         # cherche la version en vigueur aujourd'hui

Le texte vient du « filestore » de Fedlex (version consolidée HTML à la date donnée).
Les fichiers téléchargés sont gardés dans .cache/fedlex/ (non versionné).
Les notes de bas de page (historique des modifications) sont retirées.
"""

import html
import re
import sys
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
CACHE = RACINE / ".cache" / "fedlex"
RECUEILS = {
    "cp": ("54/757_781_799", "Code pénal suisse, RS 311.0"),
    "lcr": ("1959/679_705_685", "Loi fédérale sur la circulation routière, RS 741.01"),
    "cst": ("1999/404", "Constitution fédérale, RS 101"),
    "cpp": ("2010/267", "Code de procédure pénale, RS 312.0"),
    "dpmin": ("2006/551", "Droit pénal des mineurs, RS 311.1"),
    "cc": ("24/233_245_233", "Code civil suisse, RS 210"),
}


def adresse(recueil: str, date: str) -> str:
    eli, _ = RECUEILS[recueil]
    d = date.replace("-", "")
    nom = f"fedlex-data-admin-ch-eli-cc-{eli.replace('/', '-')}-{d}-fr-html.html"
    return f"https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/{eli}/{d}/fr/html/{nom}"


def texte_html(recueil: str, date: str) -> str:
    fichier = CACHE / f"{recueil}-{date}.html"
    if not fichier.exists():
        CACHE.mkdir(parents=True, exist_ok=True)
        contenu = urllib.request.urlopen(adresse(recueil, date), timeout=60).read()
        # Une date sans version publiée renvoie la page d'accueil de Fedlex (environ 77 ko).
        if b'<article id="art_' not in contenu:
            sys.exit(f"Pas de version de « {recueil} » au {date} sur Fedlex.")
        fichier.write_bytes(contenu)
    return fichier.read_text(encoding="utf-8")


def existe(recueil: str, date: str) -> bool:
    if (CACHE / f"{recueil}-{date}.html").exists():
        return True
    requete = urllib.request.Request(adresse(recueil, date), method="GET", headers={"Range": "bytes=0-200000"})
    try:
        debut = urllib.request.urlopen(requete, timeout=60).read()
    except Exception:
        return False
    return b'<article id="art_' in debut or len(debut) > 150000


def derniere_version(recueil: str, date: str) -> str:
    """Date de la dernière version consolidée publiée au plus tard à la date donnée.

    Fedlex publie une version à chaque entrée en vigueur d'une modification, le plus souvent
    un 1er du mois. On cherche le dernier 1er du mois qui a une version, puis on vérifie,
    jour par jour, qu'aucune version plus récente n'a été publiée jusqu'à la date demandée.
    """
    from concurrent.futures import ThreadPoolExecutor
    from datetime import date as D, timedelta
    cible = D.fromisoformat(date)
    mois, trouve = D(cible.year, cible.month, 1), None
    for _ in range(60):
        if existe(recueil, mois.isoformat()):
            trouve = mois
            break
        mois = D(mois.year - (mois.month == 1), 12 if mois.month == 1 else mois.month - 1, 1)
    if trouve is None:
        sys.exit(f"Aucune version de « {recueil} » trouvée dans les cinq dernières années.")
    jours = [trouve + timedelta(days=k) for k in range(1, (cible - trouve).days + 1)]
    with ThreadPoolExecutor(8) as pool:
        presents = [j for j, ok in zip(jours, pool.map(lambda j: existe(recueil, j.isoformat()), jours)) if ok]
    return max(presents, default=trouve).isoformat()


def article(source: str, numero: str) -> str | None:
    m = re.search(r'<article id="art_%s">(.*?)</article>' % re.escape(numero.replace(" ", "_")), source, re.S)
    if not m:
        return None
    t = re.sub(r'<div class="footnotes">.*', "", m.group(1), flags=re.S)
    # Numéros d'alinéa (« 1 ») suffixes (« 172ter », « 1er ») gardés ;
    # les autres exposants sont des appels de note.
    t = re.sub(r"<sup>(\d+[a-z]*)</sup>", r"\1 ", t)
    t = re.sub(r"<sup>([a-z]+)</sup>", r"\1", t)
    t = re.sub(r"<sup>.*?</sup>", "", t, flags=re.S)
    t = re.sub(r"</p>|</h6>|<br\s*/?>|</dd>", "\n", t)
    t = re.sub(r"</?(?:b|i|a|em|strong|span)\b[^>]*>", "", t)  # balises en ligne : « 193<i>a</i> » → « 193a »
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    lignes = [" ".join(l.split()) for l in t.splitlines()]
    return "\n".join(l for l in lignes if l)


def main(args: list[str]) -> None:
    recueil, date, *reste = args
    if date == "en-vigueur":
        from datetime import date as D
        date = derniere_version(recueil, D.today().isoformat())
    comparer = None
    if reste and reste[0] == "--compare":
        comparer, reste = reste[1], reste[2:]
    source = texte_html(recueil, date)
    autre = texte_html(recueil, comparer) if comparer else None
    print(f"# {RECUEILS[recueil][1]}, état au {date}\n# {adresse(recueil, date)}\n")
    for n in [re.sub(r"(\d)(bis|ter|quater)$", r"\1_\2", x) for x in reste]:
        t = article(source, n)
        print(f"== Art. {n}\n{t or 'INTROUVABLE'}\n")
        if autre is not None and article(autre, n) != t:
            print(f"!! Art. {n} : le texte change dans la version du {comparer}\n")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    main(sys.argv[1:])
