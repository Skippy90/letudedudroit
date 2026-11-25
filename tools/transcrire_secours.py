"""Transcription de secours (huggingface.co inaccessible) : Whisper medium via sherpa-onnx, modèle pris sur GitHub.

Usage : python tools/transcrire_secours.py voice/arrets/<slug>/enregistrement.m4a voice/arrets/<slug>/transcription.json
Modèle : dossier donné par la variable MODELE_SHERPA (défaut ~/modeles/sherpa-onnx-whisper-medium), à télécharger une fois :
  https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/sherpa-onnx-whisper-medium.tar.bz2
Lent (environ la durée de l'enregistrement sur 2 cœurs) : à lancer en arrière-plan (setsid nohup … &).
Limite connue : le dernier mot d'une zone courte est parfois tronqué ; l'alignement peut alors déborder sur la zone
voisine (sherpa-onnx signale alors « decode stopped at the token limit » ; piste non essayée : augmenter
l'option « max_tokens_per_second »). Contrôler avec tools/controle_voix.py et corriger transcription.json à la main (en le notant dans le fichier).
Même découpage aux pauses que tools/alignement.py, mais sans regroupement : un morceau par zone de voix.
Les instants des mots sont répartis dans chaque morceau au prorata des lettres (approximation)."""
import json, os, sys
from pathlib import Path
import sherpa_onnx
from faster_whisper.audio import decode_audio
from faster_whisper.vad import VadOptions, get_speech_timestamps
src, sortie = Path(sys.argv[1]), Path(sys.argv[2])
M = Path(os.environ.get("MODELE_SHERPA", Path.home() / "modeles" / "sherpa-onnx-whisper-medium"))
fr = 16000
son = decode_audio(str(src), sampling_rate=fr)
zones = get_speech_timestamps(son, VadOptions(min_silence_duration_ms=350, speech_pad_ms=150))
rec = sherpa_onnx.OfflineRecognizer.from_whisper(encoder=str(M/"medium-encoder.int8.onnx"), decoder=str(M/"medium-decoder.int8.onnx"),
    tokens=str(M/"medium-tokens.txt"), language="fr", task="transcribe", num_threads=2)
mots = []
for k, z in enumerate(zones):
    a, b = z["start"], z["end"]
    # Whisper : 30 s au plus par morceau
    for d in range(a, b, 28 * fr):
        f = min(b, d + 28 * fr)
        s = rec.create_stream(); s.accept_waveform(fr, son[d:f]); rec.decode_stream(s)
        ws = s.result.text.strip().split()
        if not ws: continue
        tot = sum(len(w) + 1 for w in ws); t = d / fr; dur = (f - d) / fr
        for w in ws:
            e = t + dur * (len(w) + 1) / tot
            mots.append({"text": w, "start": round(t, 3), "end": round(e, 3), "type": "word", "zone": k}); t = e
    if k % 20 == 0: print(k, len(zones), flush=True)
sortie.write_text(json.dumps({"source": f"{src.name}:{src.stat().st_size}", "reponse": {"text": " ".join(m["text"] for m in mots),
    "words": mots, "moteur": "whisper medium (sherpa-onnx), un morceau par zone de voix, instants des mots répartis"}}, ensure_ascii=False), encoding="utf-8")
print("FIN", len(mots))
