"""ATF 121 I 367 : instants des phrases dans la narration, et temps de la vidéo (pauses ajoutées, silences resserrés)."""
import json, re, unicodedata
from pathlib import Path
import os
_d = json.loads(Path(os.environ.get("M367_TIMINGS", "/home/claude/letudedudroit/voice/arrets/atf-121-i-367-minimum-vital/timings.json")).read_text())
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
    print("MOT INTROUVABLE", l, p, mot); return S(l, p) + 0.3 * (E(l, p) - S(l, p))


def B(l):
    """Frontière avant la ligne l : milieu du silence."""
    return 0.0 if l == 1 else (E(l - 1) + S(l)) / 2


CHAPITRES = (4, 15, 18, 30, 40)            # un carton de partie avant ces lignes
# ---- Rythme réglé sur le sens du texte (standard « grands arrêts », 25 novembre 2026) ----
# Blocs d'idées : une séquence qui ouvre un bloc reçoit une pause marquée avant elle ; à l'intérieur d'un bloc, pause courte.
BLOCS = {1, 3, 4, 8, 10, 12, 14, 15, 17, 18, 20, 23, 24, 27, 30, 31, 33, 36, 38, 39, 40, 43, 44}
VIRAGES = {7, 20, 31, 33, 35, 37}          # séquences qui commencent par « Pourtant », « Or », « Mais », « Surtout », « Autrement dit »
P_PHRASE, P_SEQ, P_VIRAGE, P_BLOC, P_CHAPITRE = 0.38, 0.6, 0.9, 1.0, 1.0
# Pauses voulues entre deux phrases : indications de marge de l'autrice, questions qui ouvrent une partie, deux-points lus en deux temps.
PAUSES = {((44, 1), (44, 2)): 2.2,          # réflexion après la question finale
          ((1, 2), (1, 3)): 0.8,            # 1 : « Pause avant la question »
          ((1, 3), (2, 1)): 1.0,            # question d'accroche
          ((10, 2), (10, 3)): 0.9,          # 10 : « Silence après travailler en Suisse »
          ((13, 1), (13, 2)): 0.3,          # 13 : virgule (début et fin de phrase pris dans deux prises)
          ((13, 3), (13, 4)): 1.2,          # 13 : « Pause courte avant la dernière phrase » ; allongée (demande du 25 nov., 2:30) : la question se détache
          ((13, 4), (14, 1)): 1.3,          # laisser la question « Est-ce juridiquement possible ? » résonner avant la procédure
          ((17, 1), (17, 2)): 0.5,          # 17 : deux-points
          ((23, 2), (24, 1)): 1.15,         # question qui ouvre « ce qu'il garantit »
          ((27, 2), (27, 3)): 0.9,          # 27 : « Pause après Qui peut invoquer ce droit ? »
          ((37, 2), (37, 3)): 0.8,          # 37 : « Pause avant la dernière phrase »
          ((38, 1), (38, 2)): 0.7, ((38, 2), (38, 3)): 0.55,   # 38 : solennité, deux-points
          ((39, 1), (39, 2)): 0.45,         # « Il faut être précis : » / « cet arrêt… » (phrase coupée au montage, 25 nov.)
          ((39, 2), (39, 3)): 0.6,
          ((43, 1), (43, 2)): 0.6, ((43, 2), (43, 3)): 0.8}    # 43 : « Détacher les 2 idées »
AJOUTS = [(B(l) + 0.01, 1.2) for l in CHAPITRES]
_c = sorted(PH)
for _a, _b in zip(_c, _c[1:]):
    _g = PH[_b]["debut"] - PH[_a]["fin"]; _m = (PH[_a]["fin"] + PH[_b]["debut"]) / 2; _force = True
    if (_a, _b) in PAUSES: _cible = PAUSES[(_a, _b)]; _m -= 0.02
    elif _a[0] != _b[0]:
        _cible = P_CHAPITRE if _b[0] in CHAPITRES else P_BLOC if _b[0] in BLOCS else P_VIRAGE if _b[0] in VIRAGES else P_SEQ
    else: _cible = P_PHRASE; _force = False      # dans une séquence : on raccourcit seulement
    if (_force or _g > _cible) and abs(_cible - _g) > 0.01: AJOUTS.append((_m, _cible - _g))

# Silences longs à l'intérieur d'une phrase (souffle, hésitation entre deux morceaux de prise) : ramenés à 0,35 s.
# Mesurés une fois sur narration.wav (même seuil que tools/alignement.py), gardés en cache.
def _silences_internes():
    import numpy as np, soundfile as sf
    f = Path(os.environ.get("M367_TIMINGS", "/home/claude/letudedudroit/voice/arrets/atf-121-i-367-minimum-vital/timings.json")).with_name("narration.wav")
    cache = Path("/tmp/m367v/silences.json")
    if cache.exists():
        c = json.loads(cache.read_text())
        if c.get("cle") == [str(f), f.stat().st_mtime]: return c["s"]
    x, fr = sf.read(str(f)); x = x[:, 0] if x.ndim > 1 else x
    h = int(0.01 * fr); nb = len(x) // h; env = np.sqrt((x[:nb * h].reshape(nb, h) ** 2).mean(1) + 1e-12); seuil = float(np.percentile(env, 10)) * 6
    out = []
    for p in PH.values():
        a, b = int((p["debut"] + 0.15) / 0.01), int((p["fin"] - 0.15) / 0.01); k = a
        while k < b:
            if env[k] < seuil:
                j = k
                while j < b and env[j] < seuil: j += 1
                if (j - k) * 0.01 >= 0.5: out.append([(k + j) * 0.005, 0.35 - (j - k) * 0.01])
                k = j
            else: k += 1
    cache.parent.mkdir(parents=True, exist_ok=True); cache.write_text(json.dumps({"cle": [str(f), f.stat().st_mtime], "s": out}))
    return out
INTERNES = _silences_internes()
AJOUTS += [tuple(x) for x in INTERNES]

# Pauses de marge placées dans une phrase (« un temps après aucune ressource ») : seulement là où la voix fait déjà une
# petite pause (silence d'au moins 60 ms près de la fin du mot), allongée à la cible ; sinon rien (on ne coupe pas un mot).
DANS_PHRASE = [(2, 1, "ressource", 0.55), (7, 1, "un", 0.45), (23, 1, "constitutionnel", 0.4), (38, 2, "annule", 0.4), (20, 1, "nourrir", 0.3), (20, 1, "vêtir", 0.3)]
def _pauses_mots():
    import numpy as np, soundfile as sf
    f = Path(os.environ.get("M367_TIMINGS", "/home/claude/letudedudroit/voice/arrets/atf-121-i-367-minimum-vital/timings.json")).with_name("narration.wav")
    x, fr = sf.read(str(f)); x = x[:, 0] if x.ndim > 1 else x
    h = int(0.01 * fr); nb = len(x) // h; env = np.sqrt((x[:nb * h].reshape(nb, h) ** 2).mean(1) + 1e-12); seuil = float(np.percentile(env, 10)) * 6
    out, rapport = [], []
    for l, ph, mot, cible in DANS_PHRASE:
        ms = PH[(l, ph)]["mots"]; k = next((i for i, m in enumerate(ms) if _n(m["mot"]).startswith(_n(mot))), None)
        if k is None or k + 1 >= len(ms): rapport.append((l, ph, mot, "mot introuvable")); continue
        t = (ms[k]["fin"] + ms[k + 1]["debut"]) / 2; a, b = int((t - 0.3) / 0.01), int((t + 0.35) / 0.01)
        best = None; i = a
        while i < b:
            if env[i] < seuil:
                j = i
                while j < b and env[j] < seuil: j += 1
                if (j - i) >= 6 and (best is None or abs((i + j) / 2 - t / 0.01) < abs(sum(best) / 2 - t / 0.01)): best = (i, j)
                i = j
            else: i += 1
        if best is None: rapport.append((l, ph, mot, "pas de pause naturelle")); continue
        g = (best[1] - best[0]) * 0.01
        if g < cible: out.append(((best[0] + best[1]) * 0.005, cible - g)); rapport.append((l, ph, mot, f"{g:.2f} -> {cible}"))
    return out, rapport
_PM, RAPPORT_MOTS = _pauses_mots()
AJOUTS += _PM
FIN = E(DERNIERE) + 1.0


K = 1.05   # la voix est légèrement accélérée (hauteur conservée) : le temps de la vidéo est divisé d'autant


def M0(t): return t + sum(s for x, s in AJOUTS if x < t)
def M(t): return M0(t) / K
