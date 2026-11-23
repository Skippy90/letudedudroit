"""Arrêt 15 : instants des phrases dans la narration, et temps de la vidéo (pauses ajoutées)."""
import json, re, unicodedata
from pathlib import Path
RACINE = Path(__file__).resolve().parents[3]
_d = json.loads((RACINE / "voice/arrets/15-atf-129-i-217/timings.json").read_text())
PH = {(l["ligne"], i + 1): p for l in _d["lignes"] for i, p in enumerate(l["phrases"])}
NB = {l["ligne"]: len(l["phrases"]) for l in _d["lignes"]}
DUREE = _d["duree"]


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
    # mot mal reconnu : position au prorata des lettres dans le texte de la phrase
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


# (instant d'origine, secondes ajoutées) : cartons de partie et deux pauses de réflexion
AJOUTS = [(B(4) + 0.01, 1.2), (B(15) + 0.01, 1.2), (B(18) + 0.01, 1.2), (B(19) - 0.01, 1.6), (B(19) + 0.01, 1.2),
          (B(37) + 0.01, 1.2), ((E(44, 2) + S(44, 3)) / 2, 1.9)]
# Rythme : les silences trop longs entre les phrases sont raccourcis (0,5 s dans une ligne, 0,85 s entre deux lignes)
_c = sorted(PH)
for _a, _b in zip(_c, _c[1:]):
    _g = PH[_b]["debut"] - PH[_a]["fin"]; _m = (PH[_a]["fin"] + PH[_b]["debut"]) / 2
    if _a[0] != _b[0]:
        if (_a[0], _b[0]) in ((3, 4), (14, 15), (17, 18), (18, 19), (36, 37)): continue
        _cible = 0.85
    else:
        if _a == (44, 2): continue
        _cible = 0.5
    if _g > _cible: AJOUTS.append((_m, _cible - _g))
FIN = E(45) + 1.0


def M(t): return t + sum(s for x, s in AJOUTS if x < t)
