"""Contours simplifiés de la Suisse et des 26 cantons, pour les schémas Manim (thème « constitution »).

Usage : python tools/carte_suisse.py <ch-combined.json> [sortie.json]

Source : paquet npm « swiss-maps » (Interactive Things, licence BSD-3-Clause), TopoJSON généré à partir des limites
généralisées de l'Office fédéral de la statistique (OFS) / swisstopo, millésime 2026. La sortie
(render/manim/donnees/suisse.json) contient des coordonnées normalisées (largeur du pays = 1, centre à l'origine),
projection équirectangulaire corrigée de la latitude, lignes simplifiées (Douglas-Peucker).
"""

import json
import math
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
SIGLES = ["ZH", "BE", "LU", "UR", "SZ", "OW", "NW", "GL", "ZG", "FR", "SO", "BS", "BL", "SH", "AR", "AI", "SG", "GR",
          "AG", "TG", "TI", "VD", "VS", "NE", "GE", "JU"]  # numéros OFS 1 à 26


def arcs_absolus(topo):
    sx, sy = topo["transform"]["scale"]
    tx, ty = topo["transform"]["translate"]
    sortie = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx
            y += dy
            pts.append((x * sx + tx, y * sy + ty))
        sortie.append(pts)
    return sortie


def anneau(arcs, indices):
    pts = []
    for i in indices:
        a = arcs[i] if i >= 0 else list(reversed(arcs[~i]))
        pts.extend(a if not pts else a[1:])
    return pts


def rdp(pts, eps):
    if len(pts) < 3:
        return pts
    (x1, y1), (x2, y2) = pts[0], pts[-1]
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy) or 1e-12
    dmax, idx = 0, 0
    for i in range(1, len(pts) - 1):
        d = abs(dy * pts[i][0] - dx * pts[i][1] + x2 * y1 - y2 * x1) / n
        if d > dmax:
            dmax, idx = d, i
    if dmax > eps:
        return rdp(pts[:idx + 1], eps)[:-1] + rdp(pts[idx:], eps)
    return [pts[0], pts[-1]]


def main(source, cible=None):
    topo = json.loads(Path(source).read_text(encoding="utf-8"))
    arcs = arcs_absolus(topo)

    def anneaux(geom):
        polys = geom["arcs"] if geom["type"] == "MultiPolygon" else [geom["arcs"]]
        return [anneau(arcs, r) for p in polys for r in p]

    pays = [r for g in topo["objects"]["country"]["geometries"] for r in anneaux(g)]
    tous = [p for r in pays for p in r]
    lat0 = sum(p[1] for p in tous) / len(tous)
    k = math.cos(math.radians(lat0))
    xs, ys = [p[0] * k for p in tous], [p[1] for p in tous]
    cx, cy, larg = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2, max(xs) - min(xs)

    def norm(r, eps=0.0025):
        pts = [((x * k - cx) / larg, (y - cy) / larg) for x, y in r]
        # Anneau fermé (premier point = dernier) : on le coupe au point le plus éloigné, puis on simplifie les deux moitiés.
        loin = max(range(len(pts)), key=lambda i: (pts[i][0] - pts[0][0]) ** 2 + (pts[i][1] - pts[0][1]) ** 2)
        s = rdp(pts[:loin + 1], eps)[:-1] + rdp(pts[loin:], eps) if eps else pts
        return [[round(x, 4), round(y, 4)] for x, y in s] if len(s) >= 4 else None

    def centre(r):
        a = cxs = cys = 0.0
        for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]):
            c = x1 * y2 - x2 * y1
            a += c
            cxs += (x1 + x2) * c
            cys += (y1 + y2) * c
        return [round(cxs / (3 * a), 4), round(cys / (3 * a), 4)] if a else r[0]

    sortie = {"source": "swiss-maps 4.7.0 (BSD-3-Clause), limites généralisées OFS/swisstopo 2026",
              "pays": [n for n in (norm(r, 0.002) for r in pays) if n], "cantons": {}, "lacs": []}
    for g in topo["objects"]["cantons"]["geometries"]:
        rs = [n for n in (norm(r, 0.0015) for r in anneaux(g)) if n] or [n for n in (norm(r, 0.0) for r in anneaux(g)) if n]
        exterieur = max(rs, key=lambda r: abs(sum(x1 * y2 - x2 * y1 for (x1, y1), (x2, y2) in zip(r, r[1:] + r[:1]))))
        sortie["cantons"][SIGLES[int(g["id"]) - 1]] = {"anneaux": rs, "centre": centre(exterieur)}
    for g in topo["objects"]["lakes"]["geometries"]:
        sortie["lacs"] += [n for n in (norm(r, 0.003) for r in anneaux(g)) if n]
    cible = Path(cible) if cible else RACINE / "render/manim/donnees/suisse.json"
    cible.write_text(json.dumps(sortie, ensure_ascii=False), encoding="utf-8")
    print(f"Carte : {cible} ({len(sortie['cantons'])} cantons, {sum(len(r) for r in sortie['pays'])} points pour le pays)")


if __name__ == "__main__":
    main(*sys.argv[1:3])
