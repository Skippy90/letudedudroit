"""FR-01 Morsang-sur-Orge : instants des phrases dans la narration, et temps de la vidéo (pauses réglées sur le sens).
Avant l'enregistrement : instants estimés (FR01_TIMINGS=/tmp/fr01v/timings_estimes.json, 2,8 mots par seconde, débit mesuré
de l'autrice). Après : timings.json de l'enregistrement aligné ; les silences internes sont alors resserrés comme pour l'ATF 121 I 367."""
import json, re, unicodedata, os
from pathlib import Path
_F = Path(os.environ.get("FR01_TIMINGS", "/home/claude/letudedudroit/voice/arrets-francais/fr-01-morsang-sur-orge/timings.json"))
_d = json.loads(_F.read_text())
ESTIMATION = _d.get("voix") == "estimation"
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
    for m in PH[(l, p)].get("mots", []):
        x = m["mot"]
        if any(_n(c).startswith(_n(mot)) for c in (x, x.split("'")[-1], x.split("’")[-1])):
            k += 1
            if k == n: return m["debut"]
    print("MOT INTROUVABLE", l, p, mot); return S(l, p) + 0.3 * (E(l, p) - S(l, p))


def B(l):
    """Frontière avant la ligne l : milieu du silence."""
    return 0.0 if l == 1 else (E(l - 1) + S(l)) / 2


# Parties à l'écran (fil conducteur et cartons) : les actes de l'autrice servent de repères de montage, pas de titres à l'écran.
CHAPITRES = (4, 8, 17, 29, 39)
BLOCS = {1, 3, 4, 7, 8, 9, 12, 14, 15, 17, 18, 20, 21, 23, 26, 27, 29, 30, 32, 34, 36, 37, 39, 41, 42, 43, 45}
VIRAGES = {8, 11, 20, 23, 30}            # « Seulement », « Or », « Encore faut-il », « Mais »
P_PHRASE, P_SEQ, P_VIRAGE, P_BLOC, P_CHAPITRE = 0.38, 0.6, 0.9, 1.0, 1.0
PAUSES = {((1, 3), (1, 4)): 0.8,          # 1 : « silence avant la question »
          ((1, 4), (2, 1)): 1.0,          # question d'accroche
          ((8, 2), (8, 3)): 0.6,          # 8 : « légère pause » avant la question
          ((13, 1), (13, 2)): 0.5,
          ((16, 1), (17, 1)): 1.2,        # question centrale
          ((18, 2), (19, 1)): 1.2,        # 18 : « silence après la règle »
          ((27, 1), (28, 1)): 1.0,        # 27 : « pause »
          ((28, 1), (28, 2)): 0.8,        # 28 : « une phrase ferme, puis pause »
          ((34, 2), (35, 1)): 1.0,        # question ouverte
          ((43, 2), (44, 1)): 2.2}        # réflexion après la question finale
AJOUTS = [(B(l) + 0.01, 1.2) for l in CHAPITRES]
_c = sorted(PH)
for _a, _b in zip(_c, _c[1:]):
    _g = PH[_b]["debut"] - PH[_a]["fin"]; _m = (PH[_a]["fin"] + PH[_b]["debut"]) / 2; _force = True
    if (_a, _b) in PAUSES: _cible = PAUSES[(_a, _b)]; _m -= 0.02
    elif _a[0] != _b[0]:
        _cible = P_CHAPITRE if _b[0] in CHAPITRES else P_BLOC if _b[0] in BLOCS else P_VIRAGE if _b[0] in VIRAGES else P_SEQ
    else: _cible = P_PHRASE; _force = False
    if (_force or _g > _cible) and abs(_cible - _g) > 0.01: AJOUTS.append((_m, _cible - _g))
FIN = E(DERNIERE) + 1.0
K = 1.0 if ESTIMATION else 1.05   # la voix réelle est légèrement accélérée (hauteur conservée)


def M0(t): return t + sum(s for x, s in AJOUTS if x < t)
def M(t): return M0(t) / K
