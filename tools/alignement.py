"""Monte et aligne un enregistrement humain sur le tts.txt d'une vidéo.

Usage : python tools/alignement.py <matiere>/<numero-slug>

- L'enregistrement est déposé dans voice/<slug>/ sous le nom enregistrement.<ext>
  (m4a, mp3, wav…), un seul fichier pour toute la vidéo, prises ratées comprises.
- Il est transcrit une fois, avec l'instant de chaque mot, sur la machine et gratuitement
  (faster-whisper, modèle « medium » ; WHISPER_MODELE pour un autre). Sur demande
  ({"transcription": "elevenlabs"} dans reglages.json), par la reconnaissance d'ElevenLabs (payante). La transcription est gardée dans
  voice/<slug>/transcription.json : relancer l'outil ne coûte rien.
- Chaque phrase de tts.txt est cherchée dans la transcription. Quand elle a été lue
  plusieurs fois, la dernière prise complète est gardée : les faux départs et les
  reprises sont coupés. Le titre lu au début est coupé aussi.
- Par défaut, aucun débruitage : le son brut est gardé, avec ses pauses naturelles, et le
  niveau est ajusté par un gain fixe. Sur demande (voice/<slug>/reglages.json) :
  {"nettoyage": "rnnoise"} atténue le bruit de fond par RNNoise (filtre arnndn de ffmpeg,
  modèle téléchargé une fois dans .cache/rnnoise/, dépôt GregorR/rnnoise-models) ;
  {"pauses": "silence"} remplace les pauses par un silence numérique.
- Option payante, vidéo par vidéo : si voice/<slug>/reglages.json contient
  {"isolation": true}, RNNoise n'est pas utilisé ; la narration montée passe par
  l'isolation de voix d'ElevenLabs (environ 1 000 crédits par minute). Le résultat est
  gardé dans voice/<slug>/isole-<empreinte>.mp3 : relancer l'outil ne coûte rien.
- Retouches : une phrase réenregistrée à part est ajoutée à la fin de l'enregistrement
  (lecture complète, une seconde de silence, puis les retouches, au même niveau sonore).
  Toute prise située après la dernière phrase de la lecture remplace la prise d'origine.
- Montage : les phrases gardées sont mises bout à bout, avec un court fondu à chaque
  coupe ; les pauses naturelles sont conservées quand deux phrases se suivent sans
  reprise, sinon remplacées par un silence de longueur fixe.
- Sortie, au même format que tools/narration.py : narration.wav (normalisée à -16 LUFS)
  et timings.json, avec "source": "humaine". Le détail du montage (prise gardée,
  phrases mal reconnues) est écrit dans voice/<slug>/montage.txt.

La clé API n'est jamais lue ici : soit ELEVENLABS_API_KEY est défini, soit le
proxy de l'environnement ajoute l'en-tête xi-api-key lui-même.
"""

import difflib
import hashlib
import json
import os
import re
import subprocess
import sys
import unicodedata
import urllib.request
import uuid
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parent))
from narration import FREQ, lire_blocs  # noqa: E402
from tts import en_lettres  # noqa: E402

RACINE = Path(__file__).resolve().parent.parent
SEUIL_PRISE = 0.7        # part minimale des mots d'une phrase pour reconnaître une prise
SEUIL_A_RELIRE = 0.9     # en dessous, la prise gardée est signalée dans montage.txt
MARGE = 0.12             # secondes gardées avant et après chaque phrase
FONDU = 0.015            # secondes de fondu à chaque coupe
PORTE_AVANT, PORTE_APRES = 0.10, 0.15   # secondes gardées intactes avant et après chaque mot
PORTE_FUSION = 0.35      # deux mots séparés de moins que cela : la pause entre eux reste intacte
PORTE_ATTENUATION = 26   # dB retirés entre les mots
PORTE_FONDU = 0.06       # secondes de fondu à l'ouverture et à la fermeture
PAUSE_PHRASE = (0.25, 0.9)   # pause entre deux phrases d'une même ligne : bornes
PAUSE_LIGNE = (0.45, 1.2)    # pause entre deux lignes : bornes
PAUSE_COUPE = {"phrase": 0.35, "ligne": 0.6}  # pause imposée là où une reprise a été coupée
MODELE_BRUIT = RACINE / ".cache/rnnoise/sh.rnnn"
URL_MODELE = ("https://raw.githubusercontent.com/GregorR/rnnoise-models/master/"
              "somnolent-hogwash-2018-09-01/sh.rnnn")


def normaliser(mot: str) -> str:
    mot = unicodedata.normalize("NFC", mot.lower()).replace("’", "'")
    return re.sub(r"[^\w']", "", mot).strip("'")


def nombre_en_lettres(n: int) -> str:
    """La transcription écrit « 1999 » : on le compare à « mille neuf cent nonante-neuf »."""
    if n < 1000:
        return en_lettres(n)
    if n < 10000:
        m, r = divmod(n, 1000)
        tete = "mille" if m == 1 else en_lettres(m) + " mille"
        return tete if r == 0 else f"{tete} {en_lettres(r)}"
    return str(n)


def mots_texte(texte: str) -> list[str]:
    # « l'article », « trente-et-un » : la reconnaissance vocale les coupe à sa façon,
    # on compare donc après avoir séparé apostrophes et traits d'union.
    texte = re.sub(r"\d+", lambda d: nombre_en_lettres(int(d.group())), texte)
    return [m for m in (normaliser(x) for x in re.split(r"[\s'’\-]+", texte)) if m]


MODELE_WHISPER = os.environ.get("WHISPER_MODELE", "medium")


def transcrire_local(fichier: Path) -> dict:
    """Transcription gratuite, sur la machine (faster-whisper, modèle téléchargé une fois depuis huggingface.co).
    L'enregistrement est découpé aux pauses (détecteur de voix Silero) et chaque morceau est transcrit seul :
    transcrit d'un bloc, Whisper saute souvent une phrase relue juste après sa première prise, et la reprise
    disparaît du montage. Même forme de réponse que la reconnaissance d'ElevenLabs."""
    from faster_whisper import WhisperModel
    from faster_whisper.audio import decode_audio
    from faster_whisper.vad import VadOptions, get_speech_timestamps
    fr = 16000
    son_ = decode_audio(str(fichier), sampling_rate=fr)
    zones = get_speech_timestamps(son_, VadOptions(min_silence_duration_ms=500, speech_pad_ms=200))
    # Zones voisines regroupées jusqu'à 12 s : assez de contexte, trop court pour qu'une reprise soit fusionnée.
    morceaux = []
    for z in zones:
        if morceaux and z["end"] - morceaux[-1][0] <= 12 * fr and z["start"] - morceaux[-1][1] < 0.8 * fr:
            morceaux[-1][1] = z["end"]
        else:
            morceaux.append([z["start"], z["end"]])
    modele = WhisperModel(MODELE_WHISPER, device="cpu", compute_type="int8",
                          download_root=str(RACINE / ".cache" / "whisper"))
    mots = []
    for debut, fin in morceaux:
        segments, _ = modele.transcribe(son_[debut:fin], language="fr", word_timestamps=True,
                                        condition_on_previous_text=False)
        decalage = debut / fr
        mots += [{"text": w.word.strip(), "start": round(w.start + decalage, 3), "end": round(w.end + decalage, 3),
                  "type": "word"} for seg in segments for w in (seg.words or []) if w.word.strip()]
    return {"text": " ".join(m["text"] for m in mots), "words": mots, "moteur": f"faster-whisper {MODELE_WHISPER}, par morceaux"}


def transcrire(fichier: Path, moteur: str = "local") -> dict:
    """Par défaut, transcription locale et gratuite ; {"transcription": "elevenlabs"} dans reglages.json
    utilise la reconnaissance d'ElevenLabs (payante, en crédits)."""
    if moteur != "elevenlabs":
        return transcrire_local(fichier)
    limite = uuid.uuid4().hex
    parties = [f'--{limite}\r\nContent-Disposition: form-data; name="{nom}"\r\n\r\n{valeur}\r\n'.encode()
               for nom, valeur in (("model_id", "scribe_v1"), ("language_code", "fra"),
                                   ("timestamps_granularity", "word"), ("tag_audio_events", "false"))]
    parties.append(f'--{limite}\r\nContent-Disposition: form-data; name="file"; filename="{fichier.name}"\r\n'
                   "Content-Type: audio/mpeg\r\n\r\n".encode() + fichier.read_bytes() + b"\r\n")
    entetes = {"Content-Type": f"multipart/form-data; boundary={limite}"}
    if os.environ.get("ELEVENLABS_API_KEY"):
        entetes["xi-api-key"] = os.environ["ELEVENLABS_API_KEY"]
    requete = urllib.request.Request("https://api.elevenlabs.io/v1/speech-to-text",
                                     data=b"".join(parties) + f"--{limite}--\r\n".encode(),
                                     headers=entetes, method="POST")
    with urllib.request.urlopen(requete, timeout=600) as reponse:
        return json.load(reponse)


def son(mot: str) -> str:
    """Forme comparée à l'oreille : les finales muettes tombent (« elle s'ajoute » = « elles s'ajoutent »)."""
    return re.sub(r"(ent|es|e|s|x|t)$", "", mot) if len(mot) > 3 else mot


def prises(attendu: list[str], entendus: list[str]) -> list[tuple[int, int, float, int, int]]:
    """Toutes les lectures d'une phrase dans la transcription.

    Chaque prise : (premier mot, dernier mot, part retrouvée, mots attendus manquants au début, à la fin).
    Les mots sont comparés par leur son : la transcription choisit parfois l'homophone (accord, pluriel).
    """
    attendu, entendus = [son(m) for m in attendu], [son(m) for m in entendus]
    n, trouvees = len(attendu), []
    for i in range(len(entendus)):
        if entendus[i] not in attendu[:3]:
            continue
        fenetre = entendus[i:i + n + 3]
        blocs = [b for b in difflib.SequenceMatcher(None, attendu, fenetre, autojunk=False).get_matching_blocks()
                 if b.size]
        if not blocs or blocs[0].b != 0:
            continue
        # Une prise commence par au moins deux mots attendus à la suite : un mot isolé de la phrase
        # précédente (« vouloir le résultat » devant « le tenir pour possible ») ne fait pas un début.
        if n >= 3 and blocs[0].size < 2:
            continue
        part = sum(b.size for b in blocs) / n
        if part >= SEUIL_PRISE:
            queue = n - (blocs[-1].a + blocs[-1].size)
            trouvees.append((i, i + blocs[-1].b + blocs[-1].size - 1, part, blocs[0].a, queue))
    # Une même lecture peut être trouvée à partir de deux mots voisins : on garde la meilleure.
    # À égalité, le départ le plus tardif : « Le piège classique. Le piège classique, c'est… »
    # (titre lu, puis phrase reprise) ne doit pas garder le titre.
    retenues = []
    for p in trouvees:
        if retenues and p[0] <= retenues[-1][1]:
            if p[2] >= retenues[-1][2]:
                retenues[-1] = p
        else:
            retenues.append(p)
    return retenues


def isoler(monte: Path, dossier: Path, tmp: Path) -> Path:
    """Isolation de voix ElevenLabs sur la narration montée, avec cache par empreinte."""
    empreinte = hashlib.sha256(monte.read_bytes()).hexdigest()[:16]
    cache = dossier / f"isole-{empreinte}.mp3"
    if not cache.exists():
        print("Isolation de la voix (ElevenLabs)…")
        envoi = tmp / "isolation.mp3"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(monte), "-b:a", "192k", str(envoi)], check=True)
        limite = uuid.uuid4().hex
        corps = (f'--{limite}\r\nContent-Disposition: form-data; name="audio"; filename="{envoi.name}"\r\n'
                 "Content-Type: audio/mpeg\r\n\r\n").encode() + envoi.read_bytes() + f"\r\n--{limite}--\r\n".encode()
        entetes = {"Content-Type": f"multipart/form-data; boundary={limite}"}
        if os.environ.get("ELEVENLABS_API_KEY"):
            entetes["xi-api-key"] = os.environ["ELEVENLABS_API_KEY"]
        requete = urllib.request.Request("https://api.elevenlabs.io/v1/audio-isolation", data=corps,
                                         headers=entetes, method="POST")
        with urllib.request.urlopen(requete, timeout=900) as reponse:
            cache.write_bytes(reponse.read())
        for ancien in dossier.glob("isole-*.mp3"):
            if ancien != cache:
                ancien.unlink()
    isole = tmp / "isole.wav"
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(cache), "-ac", "1", "-ar", str(FREQ),
                    "-c:a", "pcm_s16le", str(isole)], check=True)
    return isole


def caler_sur_le_son(instants: list[tuple[float, float]], x: np.ndarray, fr: int) -> list[tuple[float, float]]:
    """Recale le début et la fin de chaque mot sur le son réel.

    Les instants de Whisper sont approximatifs (souvent 0,1 à 0,4 s trop tard au début d'un mot, trop tôt à la
    fin) : une coupe faite sur eux tranche la première syllabe ou la dernière. On élargit donc chaque mot tant
    que le son reste nettement au-dessus du bruit de fond, sans empiéter sur le mot voisin, et de 0,5 s au plus."""
    h = int(0.01 * fr)
    n = len(x) // h
    env = np.sqrt((x[:n * h].reshape(n, h) ** 2).mean(1) + 1e-12)
    seuil = np.percentile(env, 10) * 6
    ordre = sorted(range(len(instants)), key=lambda k: instants[k][0])
    cales = list(instants)
    for r, k in enumerate(ordre):
        debut, fin = instants[k]
        avant = instants[ordre[r - 1]][1] if r else 0.0
        apres = instants[ordre[r + 1]][0] if r + 1 < len(ordre) else len(x) / fr
        a = int(debut / 0.01)
        borne = max(int(max(avant, debut - 0.5) / 0.01), 0)
        while a > borne and a - 1 < n and env[a - 1] > seuil:
            a -= 1
        z = int(fin / 0.01)
        borne = min(int(min(apres, fin + 0.5) / 0.01), n)
        while z < borne and env[z] > seuil:
            z += 1
        cales[k] = (min(debut, a * 0.01), max(fin, z * 0.01))
    return cales


def porte_sur_les_mots(x: np.ndarray, fr: int, instants: list[tuple[float, float]]) -> np.ndarray:
    """Atténue tout ce qui n'est pas de la parole, d'après l'instant de chaque mot transcrit.

    Pendant les mots, le son reste intact. Entre les mots (pauses, respirations bruyantes,
    gargouillis, bruit de fond), il est abaissé de PORTE_ATTENUATION dB, avec des fondus doux.
    Les micro-pauses à l'intérieur d'une phrase (moins de PORTE_FUSION s) ne sont pas touchées.
    """
    zones = []
    for debut, fin in sorted(instants):
        debut, fin = debut - PORTE_AVANT, fin + PORTE_APRES
        if zones and debut - zones[-1][1] < PORTE_FUSION:
            zones[-1][1] = max(zones[-1][1], fin)
        else:
            zones.append([debut, fin])
    plancher = 10 ** (-PORTE_ATTENUATION / 20)
    masque = np.full(len(x), plancher)
    for debut, fin in zones:
        masque[max(0, int(debut * fr)):min(len(x), int(fin * fr))] = 1.0
    # Lissage : deux moyennes glissantes (somme cumulée), soit un fondu en S de PORTE_FONDU secondes.
    n = max(1, int(PORTE_FONDU * fr / 2))
    for _ in range(2):
        c = np.concatenate([[0.0], np.cumsum(np.pad(masque, (n // 2, n - n // 2 - 1), mode="edge"))])
        masque = (c[n:] - c[:-n]) / n
    return x * masque


def main(slug: str) -> None:
    dossier = RACINE / "voice" / slug
    sources = sorted(dossier.glob("enregistrement.*"))
    if len(sources) != 1:
        sys.exit(f"Déposer un seul fichier enregistrement.<ext> dans {dossier}")
    source = sources[0]
    blocs = lire_blocs(RACINE / "scripts" / slug / "tts.txt")

    tmp = dossier / "tmp"
    tmp.mkdir(exist_ok=True)
    brut = tmp / "brut.wav"
    reglages_f = dossier / "reglages.json"
    reglages = json.loads(reglages_f.read_text(encoding="utf-8")) if reglages_f.exists() else {}
    isolation = reglages.get("isolation", False)
    # Nettoyage du bruit : aucun par défaut (l'enregistrement brut sonne mieux que ses versions
    # débruitées) ; "rnnoise" sur demande dans reglages.json.
    rnnoise = reglages.get("nettoyage", "aucun") == "rnnoise" and not isolation
    if rnnoise and not MODELE_BRUIT.exists():
        MODELE_BRUIT.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(URL_MODELE, MODELE_BRUIT)
    # RNNoise travaille à 48 kHz ; on revient ensuite à la fréquence du reste du pipeline.
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(source), "-ac", "1", "-ar", "48000",
                    "-af", "highpass=f=90,highpass=f=90" + (f",arnndn=m={MODELE_BRUIT}" if rnnoise else ""), "-ar", str(FREQ),
                    "-c:a", "pcm_s16le", str(brut)], check=True)

    transcription = dossier / "transcription.json"
    empreinte = f"{source.name}:{source.stat().st_size}"
    if not (transcription.exists() and json.loads(transcription.read_text())["source"] == empreinte):
        print("Transcription de l'enregistrement…")
        mp3 = tmp / "envoi.mp3"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut), "-ar", "16000", "-b:a", "64k", str(mp3)],
                       check=True)
        transcription.write_text(json.dumps({"source": empreinte, "reponse": transcrire(mp3, reglages.get("transcription", "local"))},
                                            ensure_ascii=False),
                                 encoding="utf-8")
    reponse = json.loads(transcription.read_text(encoding="utf-8"))["reponse"]

    # Mots reconnus avec leurs instants (« l'article » devient « l » + « article »).
    entendus, instants = [], []
    for w in reponse["words"]:
        if w.get("type", "word") != "word":
            continue
        for m in mots_texte(w["text"]):
            entendus.append(m)
            instants.append((w["start"], w["end"]))

    x, fr = sf.read(brut)
    instants = caler_sur_le_son(instants, x, fr)

    # Phrases dans l'ordre, avec toutes leurs prises.
    phrases = [(b, p, t) for b, ph in enumerate(blocs) for p, t in enumerate(ph)]
    candidats = [prises(mots_texte(t), entendus) for _, _, t in phrases]

    # En partant de la fin : pour chaque phrase, la dernière prise qui finit avant la prise
    # retenue pour la phrase suivante. Une reprise est toujours plus tardive qu'un faux départ.
    # Une phrase non reconnue (lue autrement, ou mal transcrite) est laissée de côté pour l'instant.
    choix = [None] * len(phrases)
    limite = len(entendus)
    for k in range(len(phrases) - 1, -1, -1):
        avant = [c for c in candidats[k] if c[1] < limite]
        if not avant:
            # Une prise qui déborde sur la phrase suivante (un mot commun, « un », a été pris pour la fin) :
            # on la coupe juste avant la suivante.
            avant = [(c[0], limite - 1, c[2], c[3], 0) for c in candidats[k] if c[0] < limite - 1]
        if not avant:
            if candidats[k]:
                sys.exit(f"Ligne {phrases[k][0] + 1} : aucune prise avant la phrase suivante ; "
                         "ordre de lecture à vérifier.")
            continue
        choix[k] = avant[-1]
        limite = choix[k][0]

    # Phrase non reconnue : on prend ce qui a été dit entre la phrase précédente et la suivante,
    # à condition que ce soit court (une phrase lue autrement, pas un passage entier). Elle sera
    # signalée à réécouter.
    manquantes = []
    for k, c in enumerate(choix):
        if c is not None:
            continue
        n = len(mots_texte(phrases[k][2]))
        debut_k = choix[k - 1][1] + 1 if k and choix[k - 1] else None
        fin_k = choix[k + 1][0] - 1 if k + 1 < len(choix) and choix[k + 1] else None
        if debut_k is not None and fin_k is not None and 0 <= fin_k - debut_k <= n + 4:
            choix[k] = (debut_k, fin_k, 0.0, 0, 0)
        else:
            manquantes.append(f"  ligne {phrases[k][0] + 1} : {phrases[k][2]}")
    if manquantes:
        sys.exit("Phrases introuvables dans l'enregistrement :\n" + "\n".join(manquantes))

    # Retouches : phrases réenregistrées à part et ajoutées après la lecture complète
    # (enregistrement = lecture + retouches mises bout à bout). Une prise située après la
    # dernière phrase de la lecture remplace la prise d'origine.
    fin_lecture = choix[-1][1]
    retouches = []
    for k in range(len(phrases)):
        tardives = [c for c in candidats[k] if c[0] > fin_lecture]
        if tardives:
            choix[k] = tardives[-1]
            retouches.append(k)

    # Un mot mal reconnu au début ou à la fin d'une phrase (« séquelles », « alignés ») ne doit pas
    # être coupé : la prise est prolongée sur les mots qui la touchent, autant qu'il en manque.
    def touche(a: int, b: int, limite: float = 0.5) -> bool:
        return instants[b][0] - instants[a][1] < limite
    for k, (i, j, part, tete, queue) in enumerate(choix):
        apres = choix[k + 1][0] if k + 1 < len(choix) else len(entendus)
        for _ in range(queue + 1 if queue else 0):
            if j + 1 < apres and touche(j, j + 1):
                j += 1
        avant = choix[k - 1][1] if k else -1
        # Au début, la lectrice marque souvent un temps après le premier mot (« Sofia… roule ») : jusqu'à 1 s.
        for _ in range(tete):
            if i - 1 > avant and touche(i - 1, i, 1.0):
                i -= 1
        choix[k] = (i, j, part, tete, queue)

    # Une prise ne traverse pas un long silence pour aller chercher un ou deux derniers mots : après « jour-amende »,
    # une pause de 3 s, puis « Enfin, l'amende » (faux départ de la ligne suivante) ne font pas partie de la phrase.
    for k, (i, j, part, tete, queue) in enumerate(choix):
        for g in range(j - 1, max(i, j - 3) - 1, -1):
            if instants[g + 1][0] - instants[g][1] > 1.5:
                j = g
                break
        for g in range(i, min(j, i + 2)):
            if instants[g + 1][0] - instants[g][1] > 1.5:
                i = g + 1
                break
        choix[k] = (i, j, part, tete, queue)

    # Montage.
    if reglages.get("porte", True):
        x = porte_sur_les_mots(x, fr, instants)
    # reglages.json : {"pauses": "naturelles"} garde les pauses d'origine entre les phrases
    # (plus vivant ; les bruits de fond y restent), sinon silence numérique (plus propre, plus sec).
    naturelles = reglages.get("pauses", "naturelles") == "naturelles"
    trame = int(0.5 * fr)
    blocs_calmes = [x[i:i + trame] for i in range(0, len(x) - trame, trame)]
    ambiance = min(blocs_calmes, key=lambda b: float((b ** 2).mean())) if blocs_calmes else np.zeros(trame)
    fondu = int(FONDU * fr)
    rampe = np.linspace(0, 1, fondu)
    morceaux, t, rapport = [], 0.0, []
    timings = [[] for _ in blocs]
    # Points de coupe de chaque phrase (en secondes), recalés sur le son : on recule le début (et on avance la
    # fin) jusqu'à un vrai silence de 80 ms, de 0,6 s au plus. Un mot voisin collé à la phrase (moins de 0,15 s)
    # est traversé : c'est souvent un mot de bord mal reconnu (« Grâce » pour « Reste »). Un mot séparé par une
    # pause (une prise ratée) borne la recherche. Deux phrases lues d'un trait sont coupées au point le plus calme
    # entre elles : rien n'est répété ni tranché.
    h = int(0.01 * fr)
    nb = len(x) // h
    env = np.sqrt((x[:nb * h].reshape(nb, h) ** 2).mean(1) + 1e-12)
    seuil = np.percentile(env, 10) * 6

    def coupe_debut(i):
        debut = instants[i][0]
        lim = max(debut - 0.6, 0.0)
        if i and debut - instants[i - 1][1] >= 0.15:
            lim = max(lim, instants[i - 1][1] + 0.03)
        elif i:
            # Mot collé juste avant : on ne le traverse que s'il ouvre lui-même une prise (silence avant lui),
            # comme un premier mot mal reconnu ; sinon c'est la fin d'un faux départ enchaîné sur la reprise.
            isole = i < 2 or instants[i - 1][0] - instants[i - 2][1] >= 0.3
            if not isole:
                lim = max(lim, instants[i - 1][1])
        f = int(debut / 0.01)
        while f - 8 > lim / 0.01 and env[max(f - 8, 0):f].max() > seuil:
            f -= 1
        return max(lim, min(debut - MARGE, f * 0.01 - 0.04))

    def coupe_fin(j):
        fin = instants[j][1]
        lim = min(fin + 0.6, len(x) / fr)
        if j + 1 < len(instants) and instants[j + 1][0] - fin >= 0.15:
            lim = min(lim, instants[j + 1][0] - 0.03)
        elif j + 1 < len(instants):
            isole = j + 2 >= len(instants) or instants[j + 2][0] - instants[j + 1][1] >= 0.3
            if not isole:
                lim = min(lim, instants[j + 1][0])
        f = int(fin / 0.01)
        while f + 8 < min(lim / 0.01, nb) and env[f:f + 8].max() > seuil:
            f += 1
        return min(lim, max(fin + MARGE, f * 0.01 + 0.04))

    coupes = [[coupe_debut(i), coupe_fin(j)] for i, j, *_ in choix]
    for k in range(1, len(choix)):
        if choix[k - 1][1] + 1 == choix[k][0] and coupes[k][0] < coupes[k - 1][1]:
            g, d = instants[choix[k - 1][1]][1], instants[choix[k][0]][0]
            if d - g > 0.02:
                fa, fb = int(g / 0.01), max(int(d / 0.01), int(g / 0.01) + 1)
                milieu = (fa + int(np.argmin(env[fa:fb]))) * 0.01
            else:
                milieu = (g + d) / 2
            coupes[k - 1][1] = coupes[k][0] = milieu

    # Phrase rattachée à la précédente par sa pause d'origine (copiée telle quelle) : la jonction ne reçoit
    # pas de fondu, le son passe de l'une à l'autre exactement comme dans l'enregistrement.
    rattachee = [bool(k) and naturelles and choix[k - 1][1] + 1 == choix[k][0]
                 and coupes[k][0] - coupes[k - 1][1] <= (PAUSE_PHRASE if phrases[k][1] else PAUSE_LIGNE)[1]
                 for k in range(len(choix))]
    for k, ((b, p, texte), (i, j, part, _, _)) in enumerate(zip(phrases, choix)):
        A, Z = coupes[k]
        debut = instants[i][0]
        if k:
            Zp = coupes[k - 1][1]
            contigu = choix[k - 1][1] + 1 == i  # aucun mot (donc aucune reprise) entre les deux
            bornes = PAUSE_PHRASE if p else PAUSE_LIGNE
            ecart = A - Zp
            if rattachee[k]:
                # Pause d'origine gardée telle quelle (même très courte) : la respiration et l'ambiance restent.
                morceaux.append(x[int(Zp * fr):int(A * fr)].copy())
            else:
                pause = (min(max(ecart, bornes[0]), bornes[1]) if contigu
                         else PAUSE_COUPE["phrase" if p else "ligne"])
                n = int(pause * fr)
                if naturelles:
                    # Silence d'ambiance (le passage le plus calme de l'enregistrement), pas un silence numérique.
                    morceaux.append(np.resize(ambiance, n) * np.r_[rampe, np.ones(max(0, n - 2 * fondu)), rampe[::-1]][:n])
                else:
                    morceaux.append(np.zeros(n))
            t += len(morceaux[-1]) / fr
        a, z = max(0, int(A * fr)), min(len(x), int(Z * fr))
        seg = x[a:z].copy()
        # Pas de fondu là où deux phrases lues d'un trait se rejoignent exactement : le son continue tel quel.
        if not rattachee[k]:
            seg[:fondu] *= rampe
        if not (k + 1 < len(coupes) and rattachee[k + 1]):
            seg[-fondu:] *= rampe[::-1]
        morceaux.append(seg)
        # Instant de chaque mot reconnu, dans le temps de la narration montée
        # (sert à caler un visuel sur un mot précis et aux sous-titres).
        mots = [{"mot": entendus[w], "debut": round(t + instants[w][0] - a / fr, 3),
                 "fin": round(t + instants[w][1] - a / fr, 3)} for w in range(i, j + 1)]
        timings[b].append({"texte": texte, "debut": round(t + max(0.0, instants[i][0] - a / fr), 3),
                           "fin": round(t + min(len(seg) / fr, instants[j][1] - a / fr), 3), "mots": mots})
        t += len(seg) / fr
        reprises = len([c for c in candidats[k] if c[0] < i])
        note = f"ligne {b + 1}, phrase {p + 1} : prise gardée à {debut:.1f} s (coupe {A:.2f}–{Z:.2f})"
        if k in retouches:
            note += " (retouche enregistrée à part)"
        elif reprises:
            note += f" ({reprises} prise(s) précédente(s) coupée(s))"
        if part < SEUIL_A_RELIRE:
            note += (f" — À RÉÉCOUTER, {part:.0%} des mots reconnus. Attendu : « {texte} » ; "
                     f"reconnu : « {' '.join(entendus[i:j + 1])} »")
        rapport.append(note)

    monte = tmp / "monte.wav"
    sf.write(monte, np.concatenate(morceaux), fr, subtype="PCM_16")
    if isolation:
        monte = isoler(monte, dossier, tmp)
    # Niveau : un gain fixe pour viser -16 LUFS. Pas de normalisation
    # dynamique : elle fait « pomper » le bruit de fond entre les mots.
    mesure = subprocess.run(["ffmpeg", "-i", str(monte), "-t", f"{t:.3f}", "-af", "ebur128", "-f", "null", "-"],
                            capture_output=True, text=True).stderr
    integre = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", mesure)[-1])
    gain = -16 - integre
    # Les rares crêtes isolées (consonnes, chocs) sont retenues par un limiteur doux à -1,5 dB.
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(monte), "-t", f"{t:.3f}",
                    "-af", f"volume={gain:.2f}dB,alimiter=limit=0.84:attack=5:release=80:level=disabled",
                    "-ar", str(FREQ), "-c:a", "pcm_s16le",
                    str(dossier / "narration.wav")], check=True)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()

    lignes = [{"ligne": b + 1, "debut": ps[0]["debut"], "fin": ps[-1]["fin"], "phrases": ps}
              for b, ps in enumerate(timings)]
    (dossier / "timings.json").write_text(json.dumps(
        {"voix": "Enregistrement humain", "source": "humaine", "duree": round(t, 3), "lignes": lignes},
        ensure_ascii=False, indent=1), encoding="utf-8")
    (dossier / "montage.txt").write_text("\n".join(rapport) + "\n", encoding="utf-8")
    coupees = sum(1 for r in rapport if "coupée" in r)
    a_relire = sum(1 for r in rapport if "RÉÉCOUTER" in r)
    print(f"Montage : {round(t, 1)} s, {len(phrases)} phrases, {coupees} avec reprises coupées, "
          f"{a_relire} à réécouter → {dossier}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
