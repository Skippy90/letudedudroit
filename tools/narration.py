"""Génère la narration d'une vidéo à partir de son tts.txt.

Usage : python tools/narration.py <matiere>/<numero-slug>

- Un bloc de tts.txt (lignes séparées par une ligne vide) = une ligne du script.
- Chaque bloc est synthétisé séparément avec la voix fixée dans voice/config.json,
  via l'API ElevenLabs « with-timestamps », qui renvoie l'instant de chaque caractère.
- Les blocs sont mis en cache : un bloc dont le texte et la voix n'ont pas changé
  n'est pas régénéré (pas de crédits dépensés).
- Sortie dans voice/<slug>/ : blocs/NN.mp3, narration.wav (normalisée à -16 LUFS), timings.json.

La clé API n'est jamais lue ici : soit ELEVENLABS_API_KEY est défini, soit le
proxy de l'environnement ajoute l'en-tête xi-api-key lui-même.
"""

import base64
import hashlib
import json
import os
import subprocess
import sys
import urllib.request
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PAUSE_ENTRE_BLOCS = 0.45  # secondes de silence entre deux lignes du script
FREQ = 44100


def lire_blocs(tts: Path) -> list[list[str]]:
    blocs, courant = [], []
    for ligne in tts.read_text(encoding="utf-8").splitlines():
        if ligne.strip():
            courant.append(ligne.strip())
        elif courant:
            blocs.append(courant)
            courant = []
    if courant:
        blocs.append(courant)
    return blocs


def synthese(texte: str, config: dict) -> dict:
    corps = json.dumps({
        "text": texte,
        "model_id": config["modele"],
        "voice_settings": config["reglages"],
    }).encode()
    url = (f"https://api.elevenlabs.io/v1/text-to-speech/{config['voice_id']}"
           f"/with-timestamps?output_format={config['format_sortie']}")
    entetes = {"Content-Type": "application/json"}
    if os.environ.get("ELEVENLABS_API_KEY"):
        entetes["xi-api-key"] = os.environ["ELEVENLABS_API_KEY"]
    requete = urllib.request.Request(url, data=corps, headers=entetes, method="POST")
    with urllib.request.urlopen(requete, timeout=120) as reponse:
        return json.load(reponse)


def phrases_alignees(phrases: list[str], alignement: dict) -> list[dict]:
    """Retrouve début et fin de chaque phrase dans l'alignement caractère par caractère."""
    car = alignement["characters"]
    debuts = alignement["character_start_times_seconds"]
    fins = alignement["character_end_times_seconds"]
    texte = "".join(car)
    resultat, curseur = [], 0
    for phrase in phrases:
        i = texte.find(phrase, curseur)
        if i < 0:
            raise ValueError(f"Phrase introuvable dans l'alignement : {phrase!r}")
        j = i + len(phrase) - 1
        resultat.append({"texte": phrase, "debut": debuts[i], "fin": fins[j]})
        curseur = j + 1
    return resultat


def duree(fichier: Path) -> float:
    sortie = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(fichier)],
        capture_output=True, text=True, check=True)
    return float(sortie.stdout)


def main(slug: str) -> None:
    config = json.loads((RACINE / "voice/config.json").read_text(encoding="utf-8"))
    # MODELE_ECO=1 : même voix, modèle « flash » d'ElevenLabs, deux fois moins cher en crédits.
    # Pour une narration provisoire (avant un enregistrement humain), quand le crédit manque.
    if os.environ.get("MODELE_ECO"):
        config["modele"] = config.get("modele_eco", "eleven_flash_v2_5")
    if config["voice_id"].startswith("À"):
        sys.exit("Aucune voix fixée dans voice/config.json")
    blocs = lire_blocs(RACINE / "scripts" / slug / "tts.txt")
    dossier = RACINE / "voice" / slug
    (dossier / "blocs").mkdir(parents=True, exist_ok=True)

    tmp = dossier / "tmp"
    tmp.mkdir(exist_ok=True)
    lignes, t = [], 0.0
    for n, phrases in enumerate(blocs, 1):
        texte = "\n".join(phrases)
        empreinte = hashlib.sha256(json.dumps([texte, config["voice_id"], config["modele"],
                                               config["reglages"]]).encode()).hexdigest()[:16]
        mp3 = dossier / "blocs" / f"{n:02d}.mp3"
        meta = dossier / "blocs" / f"{n:02d}.json"
        if not (meta.exists() and json.loads(meta.read_text())["empreinte"] == empreinte and mp3.exists()):
            print(f"Synthèse ligne {n}/{len(blocs)}")
            reponse = synthese(texte, config)
            mp3.write_bytes(base64.b64decode(reponse["audio_base64"]))
            meta.write_text(json.dumps({"empreinte": empreinte, "alignement": reponse["alignment"]},
                                       ensure_ascii=False))
        alignement = json.loads(meta.read_text())["alignement"]
        # Durée mesurée sur l'audio décodé : celle du MP3 inclut un rembourrage
        # qui décalerait peu à peu les timings.
        wav = tmp / f"{n:02d}.wav"
        subprocess.run(["ffmpeg", "-y", "-v", "error", "-i", str(mp3), "-ar", str(FREQ), "-ac", "1",
                        "-c:a", "pcm_s16le", str(wav)], check=True)
        d = duree(wav)
        lignes.append({
            "ligne": n,
            "debut": round(t, 3),
            "fin": round(t + d, 3),
            "phrases": [{"texte": p["texte"], "debut": round(t + p["debut"], 3), "fin": round(t + p["fin"], 3)}
                        for p in phrases_alignees(phrases, alignement)],
        })
        t += d + PAUSE_ENTRE_BLOCS

    # Assemblage : chaque bloc suivi d'un silence, en WAV pour un montage sans perte.
    # Les blocs décodés plus haut servent ici : le démultiplexeur concat de ffmpeg
    # n'accepte pas un mélange de formats.
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "lavfi", "-i", f"anullsrc=r={FREQ}:cl=mono",
                    "-t", str(PAUSE_ENTRE_BLOCS), "-c:a", "pcm_s16le", str(tmp / "silence.wav")], check=True)
    with (tmp / "concat.txt").open("w") as f:
        for n in range(1, len(blocs) + 1):
            f.write(f"file '{n:02d}.wav'\nfile 'silence.wav'\n")
    # Normalisation du volume à -16 LUFS (niveau courant des plateformes vidéo).
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(tmp / "concat.txt"),
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(FREQ), "-c:a", "pcm_s16le",
                    str(dossier / "narration.wav")], check=True)
    for fichier in tmp.iterdir():
        fichier.unlink()
    tmp.rmdir()

    (dossier / "timings.json").write_text(json.dumps(
        {"voix": config["nom_voix"], "duree": round(t, 3), "lignes": lignes},
        ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Narration : {round(t, 1)} s, {len(blocs)} lignes → {dossier}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
