"""Monte et aligne un enregistrement humain sur le tts.txt d'une vidéo.

Usage : python tools/alignement.py <matiere>/<numero-slug>

- L'enregistrement est déposé dans voice/<slug>/ sous le nom enregistrement.<ext>
  (m4a, mp3, wav…), un seul fichier pour toute la vidéo, prises ratées comprises.
- Il est transcrit une fois, avec l'instant de chaque mot, par la reconnaissance
  vocale d'ElevenLabs (modèle « scribe »). La transcription est gardée dans
  voice/<slug>/transcription.json : relancer l'outil ne coûte rien.
- Chaque phrase de tts.txt est cherchée dans la transcription. Quand elle a été lue
  plusieurs fois, la dernière prise complète est gardée : les faux départs et les
  reprises sont coupés. Le titre lu au début est coupé aussi.
- Le bruit de fond (appareil ménager, souffle) est atténué par RNNoise, un réseau de
  neurones spécialisé dans la voix (filtre arnndn de ffmpeg). Le modèle est téléchargé
  une fois dans .cache/rnnoise/ (dépôt GregorR/rnnoise-models, sur GitHub).
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
PAUSE_PHRASE = (0.25, 0.9)   # pause entre deux phrases d'une même ligne : bornes
PAUSE_LIGNE = (0.45, 1.2)    # pause entre deux lignes : bornes
PAUSE_COUPE = {"phrase": 0.35, "ligne": 0.6}  # pause imposée là où une reprise a été coupée
MODELE_BRUIT = RACINE / ".cache/rnnoise/sh.rnnn"
URL_MODELE = ("https://raw.githubusercontent.com/GregorR/rnnoise-models/master/"
              "somnolent-hogwash-2018-09-01/sh.rnnn")


def normaliser(mot: str) -> str:
    mot = unicodedata.normalize("NFC", mot.lower()).replace("’", "'")
    return re.sub(r"[^\w']", "", mot).strip("'")


def mots_texte(texte: str) -> list[str]:
    # « l'article », « trente-et-un » : la reconnaissance vocale les coupe à sa façon,
    # on compare donc après avoir séparé apostrophes et traits d'union.
    texte = re.sub(r"\d+", lambda d: en_lettres(int(d.group())) if int(d.group()) < 1000 else d.group(), texte)
    return [m for m in (normaliser(x) for x in re.split(r"[\s'’\-]+", texte)) if m]


def transcrire(fichier: Path) -> dict:
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


def prises(attendu: list[str], entendus: list[str]) -> list[tuple[int, int, float, int, int]]:
    """Toutes les lectures d'une phrase dans la transcription.

    Chaque prise : (premier mot, dernier mot, part retrouvée, mots attendus manquants au début, à la fin).
    """
    n, trouvees = len(attendu), []
    for i in range(len(entendus)):
        if entendus[i] not in attendu[:3]:
            continue
        fenetre = entendus[i:i + n + 3]
        blocs = [b for b in difflib.SequenceMatcher(None, attendu, fenetre, autojunk=False).get_matching_blocks()
                 if b.size]
        if not blocs or blocs[0].b != 0:
            continue
        part = sum(b.size for b in blocs) / n
        if part >= SEUIL_PRISE:
            queue = n - (blocs[-1].a + blocs[-1].size)
            trouvees.append((i, i + blocs[-1].b + blocs[-1].size - 1, part, blocs[0].a, queue))
    # Une même lecture peut être trouvée à partir de deux mots voisins : on garde la meilleure.
    retenues = []
    for p in trouvees:
        if retenues and p[0] <= retenues[-1][1]:
            if p[2] > retenues[-1][2]:
                retenues[-1] = p
        else:
            retenues.append(p)
    return retenues


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
    if not MODELE_BRUIT.exists():
        MODELE_BRUIT.parent.mkdir(parents=True, exist_ok=True)
        urllib.request.urlretrieve(URL_MODELE, MODELE_BRUIT)
    # RNNoise travaille à 48 kHz ; on revient ensuite à la fréquence du reste du pipeline.
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(source), "-ac", "1", "-ar", "48000",
                    "-af", f"highpass=f=80,arnndn=m={MODELE_BRUIT}", "-ar", str(FREQ),
                    "-c:a", "pcm_s16le", str(brut)], check=True)

    transcription = dossier / "transcription.json"
    empreinte = f"{source.name}:{source.stat().st_size}"
    if not (transcription.exists() and json.loads(transcription.read_text())["source"] == empreinte):
        print("Transcription de l'enregistrement…")
        mp3 = tmp / "envoi.mp3"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(brut), "-ar", "16000", "-b:a", "64k", str(mp3)],
                       check=True)
        transcription.write_text(json.dumps({"source": empreinte, "reponse": transcrire(mp3)}, ensure_ascii=False),
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

    # Phrases dans l'ordre, avec toutes leurs prises.
    phrases = [(b, p, t) for b, ph in enumerate(blocs) for p, t in enumerate(ph)]
    candidats = [prises(mots_texte(t), entendus) for _, _, t in phrases]
    manquantes = [f"  ligne {b + 1} : {t}" for (b, _, t), c in zip(phrases, candidats) if not c]
    if manquantes:
        sys.exit("Phrases introuvables dans l'enregistrement :\n" + "\n".join(manquantes))

    # En partant de la fin : pour chaque phrase, la dernière prise qui finit avant la prise
    # retenue pour la phrase suivante. Une reprise est toujours plus tardive qu'un faux départ.
    choix = [None] * len(phrases)
    limite = len(entendus)
    for k in range(len(phrases) - 1, -1, -1):
        avant = [c for c in candidats[k] if c[1] < limite]
        if not avant:
            sys.exit(f"Ligne {phrases[k][0] + 1} : aucune prise avant la phrase suivante ; ordre de lecture à vérifier.")
        choix[k] = avant[-1]
        limite = choix[k][0]

    # Un mot mal reconnu au début ou à la fin d'une phrase (« séquelles », « alignés ») ne doit pas
    # être coupé : la prise est prolongée sur les mots qui la touchent, autant qu'il en manque.
    def touche(a: int, b: int) -> bool:
        return instants[b][0] - instants[a][1] < 0.5
    for k, (i, j, part, tete, queue) in enumerate(choix):
        apres = choix[k + 1][0] if k + 1 < len(choix) else len(entendus)
        for _ in range(queue + 1 if queue else 0):
            if j + 1 < apres and touche(j, j + 1):
                j += 1
        avant = choix[k - 1][1] if k else -1
        for _ in range(tete):
            if i - 1 > avant and touche(i - 1, i):
                i -= 1
        choix[k] = (i, j, part, tete, queue)

    # Montage.
    x, fr = sf.read(brut)
    fondu = int(FONDU * fr)
    rampe = np.linspace(0, 1, fondu)
    morceaux, t, rapport = [], 0.0, []
    timings = [[] for _ in blocs]
    for k, ((b, p, texte), (i, j, part, _, _)) in enumerate(zip(phrases, choix)):
        debut, fin = instants[i][0], instants[j][1]
        if k:
            fin_prec = instants[choix[k - 1][1]][1]
            contigu = choix[k - 1][1] + 1 == i  # aucun mot (donc aucune reprise) entre les deux
            bornes = PAUSE_PHRASE if p else PAUSE_LIGNE
            if contigu:
                pause = min(max(debut - fin_prec - 2 * MARGE, bornes[0]), bornes[1])
            else:
                pause = PAUSE_COUPE["phrase" if p else "ligne"]
            morceaux.append(np.zeros(int(pause * fr)))
            t += len(morceaux[-1]) / fr
        a, z = max(0, int((debut - MARGE) * fr)), min(len(x), int((fin + MARGE) * fr))
        seg = x[a:z].copy()
        seg[:fondu] *= rampe
        seg[-fondu:] *= rampe[::-1]
        morceaux.append(seg)
        timings[b].append({"texte": texte, "debut": round(t + MARGE, 3), "fin": round(t + len(seg) / fr - MARGE, 3)})
        t += len(seg) / fr
        reprises = len([c for c in candidats[k] if c[0] < i])
        note = f"ligne {b + 1}, phrase {p + 1} : prise gardée à {debut:.1f} s"
        if reprises:
            note += f" ({reprises} prise(s) précédente(s) coupée(s))"
        if part < SEUIL_A_RELIRE:
            note += (f" — À RÉÉCOUTER, {part:.0%} des mots reconnus. Attendu : « {texte} » ; "
                     f"reconnu : « {' '.join(entendus[i:j + 1])} »")
        rapport.append(note)

    sf.write(tmp / "monte.wav", np.concatenate(morceaux), fr, subtype="PCM_16")
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(tmp / "monte.wav"),
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(FREQ), "-c:a", "pcm_s16le",
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
