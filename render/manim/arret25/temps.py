"""Arrêt 25 : instants des phrases dans la narration, et temps de la vidéo (pauses ajoutées, silences resserrés)."""
import json, re, unicodedata
from pathlib import Path
import os
_d = json.loads(Path(os.environ.get("A25_TIMINGS", "/home/claude/letudedudroit/voice/arrets/25-atf-146-i-145/timings.json")).read_text())
PH = {(l["ligne"], i + 1): p for l in _d["lignes"] for i, p in enumerate(l["phrases"])}
NB = {l["ligne"]: len(l["phrases"]) for l in _d["lignes"]}
DUREE = _d["duree"]; DERNIERE = max(NB)


def S(l, p=1): return PH[(l, p)]["debut"]
def E(l, p=None): return PH[(l, p or NB[l])]["fin"]
def P(l, p, f): return S(l, p) + f * (E(l, p) - S(l, p))


def _n(s): return "".join(c for c in unicodedata.normalize("NFD", s.lower()) if c.isalnum())


def W(l, p, mot, n=1):
    """Début du n-ième mot commençant par « mot » dans la phrase (instants approchés)."""
    k = 0
    for m in PH[(l, p)]["mots"]:
        if _n(m["mot"]).startswith(_n(mot)):
            k += 1
            if k == n: return m["debut"]
    ws = re.findall(r"[\w]+", PH[(l, p)]["texte"]); tot = sum(len(x) + 1 for x in ws); c = 0; k = 0
    for x in ws:
        if _n(x).startswith(_n(mot)):
            k += 1
            if k == n: return S(l, p) + (E(l, p) - S(l, p)) * c / tot
        c += len(x) + 1
    raise KeyError((l, p, mot))


def B(l):
    """Frontière avant la ligne l : milieu du silence."""
    return 0.0 if l == 1 else (E(l - 1) + S(l)) / 2


CHAPITRES = (4, 14, 19, 36, 44)            # un carton de partie avant ces lignes
PAUSES = {((18, NB[18]), (19, 1)): 2.6, ((49, 3), (49, 4)): 2.8}   # silences de réflexion voulus (durée cible)
AJOUTS = [(B(l) + 0.01, 1.2) for l in CHAPITRES]
_c = sorted(PH)
for _a, _b in zip(_c, _c[1:]):
    _g = PH[_b]["debut"] - PH[_a]["fin"]; _m = (PH[_a]["fin"] + PH[_b]["debut"]) / 2
    if (_a, _b) in PAUSES: _cible = PAUSES[(_a, _b)]; _m -= 0.02
    elif _a[0] != _b[0]: _cible = 1.0 if _b[0] in CHAPITRES else 0.85
    else: _cible = 0.5
    if (_a, _b) in PAUSES or _g > _cible:
        if abs(_cible - _g) > 0.01: AJOUTS.append((_m, _cible - _g))
FIN = E(DERNIERE) + 1.0


def M(t): return t + sum(s for x, s in AJOUTS if x < t)
