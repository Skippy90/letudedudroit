"""Réécoute « à l'aveugle » : retranscrit des extraits précis d'un fichier audio, pour vérifier un passage signalé.

Usage : python tools/extrait_audio.py <audio> 62.0-66.5 201-205 …   (bornes en secondes)
Même modèle que tools/transcrire_secours.py (variable MODELE_SHERPA)."""
import os, sys
from pathlib import Path
import sherpa_onnx
from faster_whisper.audio import decode_audio
M = Path(os.environ.get("MODELE_SHERPA", Path.home() / "modeles" / "sherpa-onnx-whisper-medium")); fr=16000
son = decode_audio(sys.argv[1], sampling_rate=fr)
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(M/"medium-encoder.int8.onnx"), decoder=str(M/"medium-decoder.int8.onnx"), tokens=str(M/"medium-tokens.txt"), language="fr", task="transcribe", num_threads=2)
for x in sys.argv[2:]:
    a,b = map(float, x.split("-"))
    s = rec.create_stream(); s.accept_waveform(fr, son[int(a*fr):int(b*fr)]); rec.decode_stream(s)
    print(x, "|", s.result.text.strip(), flush=True)
