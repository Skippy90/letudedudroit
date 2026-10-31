"""Shorts verticaux (1080 × 1920) tirés d'une vidéo : un extrait du cours, aux couleurs de la marque.

Usage : python tools/short.py <matiere>/<numero-slug> [identifiant du short]

Les shorts d'une vidéo sont décrits dans scripts/<slug>/shorts.json : identifiant, accroche, lignes du script
(de … à …). Le short reprend tel quel l'extrait de la vidéo (schémas et narration déjà audités) ; seule l'accroche
lui est propre. Mise en page : bandeau rouge et accroche en haut, scène au centre, grands sous-titres calés sur
la voix, barre de progression, rappel de la vidéo complète en bas.
Entrées : voice/<slug>/timings.json et narration.wav, render/manim/media/<slug>/schemas.mp4.
Sortie : out/shorts/<matiere>--<numero-slug>--<identifiant>.mp4.
"""

import html
import json
import subprocess
import sys
import tempfile
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RACINE / "tools"))
import sous_titres  # noqa: E402
from alignement import mots_texte  # noqa: E402

L, H = 1080, 1920
Y_SCENE, H_SCENE = 560, 608          # la scène 16:9 en pleine largeur
Y_SOUS_TITRES = Y_SCENE + H_SCENE + 90
Y_PROGRES = 1700
MOTS = 4                              # mots par sous-titre, en grand


def fond(titre_video: str, numero: str, accroche: str, sortie: Path) -> None:
    """Le cadre fixe du short (bandeau, accroche, pied), rendu en PNG par Chromium."""
    symbole = (RACINE / "docs/marque/symbole.svg").read_text(encoding="utf-8")
    page = sortie.with_suffix(".html")
    page.write_text(f"""<!doctype html><meta charset="utf-8"><style>
body{{margin:0;width:{L}px;height:{H}px;background:#0B0B0B;font-family:Inter,Helvetica,Arial,sans-serif;overflow:hidden;position:relative}}
.haut{{position:absolute;inset:0 0 auto;height:{Y_SCENE - 40}px;background:#DA291C;color:#fff;padding:70px 64px 50px;box-sizing:border-box;display:flex;flex-direction:column}}
.marque{{display:flex;align-items:center;gap:16px;font-weight:800;font-size:34px}}.marque svg{{width:64px;height:64px}}
h1{{margin:auto 0;font-size:84px;line-height:1.08;font-weight:900;letter-spacing:-1.5px;text-wrap:balance}}
.bas{{position:absolute;left:64px;right:64px;top:{Y_PROGRES + 40}px;color:#F2EFE6}}
.bas p{{margin:0;font-size:30px;opacity:.75;font-weight:600}}.bas b{{display:block;font-size:40px;font-weight:800;margin-top:6px}}
.rail{{position:absolute;left:0;right:0;top:{Y_PROGRES}px;height:10px;background:#2C2C31}}
</style><div class="haut"><div class="marque">{symbole}<span>L’étude du droit</span></div><h1>{html.escape(accroche).replace('-', '\u2011')}</h1></div>
<div class="rail"></div><div class="bas"><p>Vidéo complète sur la chaîne · vidéo {numero}</p><b>{html.escape(titre_video)}</b></div>""",
                    encoding="utf-8")
    js = ("const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{L},height:{H}}}}});await p.goto(process.argv[1]);"
          "await p.waitForTimeout(300);await p.screenshot({path:process.argv[2]});await b.close()})()")
    subprocess.run(["node", "-e", js, page.as_uri(), str(sortie)], check=True)


def sous_titres_short(timings: dict, debut: float, fin: float, sortie: Path) -> None:
    """Sous-titres de l'extrait, en grand (quatre mots au plus), calés mot à mot sur la voix."""
    sous_titres.MOTS_MAX = MOTS
    evenements = []
    for ligne in timings["lignes"]:
        for phrase in ligne["phrases"]:
            if phrase["fin"] < debut or phrase["debut"] > fin:
                continue
            mots, reconnus = phrase["texte"].split(), phrase.get("mots") or []
            pieces = [len(mots_texte(w)) for w in mots]
            exact = sum(pieces) == len(reconnus)
            rang = [sum(pieces[:i]) for i in range(len(mots) + 1)]
            for a, b in sous_titres.morceaux(mots):
                if reconnus and exact:
                    d, f = reconnus[rang[a]]["debut"], reconnus[max(rang[a], rang[b] - 1)]["fin"]
                else:
                    duree = phrase["fin"] - phrase["debut"]
                    d, f = phrase["debut"] + duree * a / len(mots), phrase["debut"] + duree * b / len(mots)
                evenements.append([d - debut, f - debut + 0.15, " ".join(mots[a:b])])
    for e, suivant in zip(evenements, evenements[1:]):
        e[1] = min(e[1], suivant[0])
    lignes = [f"""[Script Info]
ScriptType: v4.00+
PlayResX: {L}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Grand,Inter,78,&H00E6EFF2,&H00E6EFF2,&H000B0B0B,&H000B0B0B,1,0,0,0,100,100,0,0,1,0,0,8,70,70,{Y_SOUS_TITRES},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""]
    for d, f, texte in evenements:
        if f > 0:
            lignes.append(f"Dialogue: 0,{sous_titres.horodatage(max(0, d))},{sous_titres.horodatage(f)},Grand,,0,0,0,,"
                          f"{texte.replace('{', '(').replace('}', ')')}\n")
    sortie.write_text("".join(lignes), encoding="utf-8")


def main(slug: str, ident: str | None = None) -> None:
    dossier = RACINE / "scripts" / slug
    config = json.loads((dossier / "shorts.json").read_text(encoding="utf-8"))
    timings = json.loads((RACINE / "voice" / slug / "timings.json").read_text(encoding="utf-8"))
    titre = (dossier / "script.md").read_text(encoding="utf-8").splitlines()[0]
    titre = titre.split("—", 1)[-1].strip()
    numero = slug.split("/")[1][:2].lstrip("0")
    sortie_dossier = RACINE / "out" / "shorts"
    sortie_dossier.mkdir(parents=True, exist_ok=True)
    for s in config["shorts"]:
        if ident and s["id"] != ident:
            continue
        lignes = {l["ligne"]: l for l in timings["lignes"]}
        debut = max(0.0, lignes[s["de"]]["phrases"][0]["debut"] - 0.3)
        fin = lignes[s["a"]]["phrases"][-1]["fin"] + 0.7
        duree = fin - debut
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            fond(titre, numero, s["accroche"], tmp / "fond.png")
            sous_titres_short(timings, debut, fin, tmp / "st.ass")
            cible = sortie_dossier / f"{slug.replace('/', '--')}--{s['id']}.mp4"
            filtre = (f"[1:v]scale={L}:{H_SCENE},setpts=PTS-STARTPTS[scene];"
                      f"[0:v][scene]overlay=0:{Y_SCENE}:shortest=1[a];"
                      f"color=c=0xDA291C:s={L}x10:r=30[rouge];"
                      f"[a][rouge]overlay=x='-w+w*t/{duree:.3f}':y={Y_PROGRES}:shortest=1[b];"
                      f"[b]ass={tmp / 'st.ass'}[v];"
                      f"[2:a]afade=t=in:d=0.15,afade=t=out:st={duree - 0.4:.3f}:d=0.4[aud]")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", "30", "-i", str(tmp / "fond.png"),
                            "-ss", f"{debut:.3f}", "-to", f"{fin:.3f}", "-i",
                            str(RACINE / "render/manim/media" / slug / "schemas.mp4"),
                            "-ss", f"{debut:.3f}", "-to", f"{fin:.3f}", "-i", str(RACINE / "voice" / slug / "narration.wav"),
                            "-filter_complex", filtre, "-map", "[v]", "-map", "[aud]", "-t", f"{duree:.3f}",
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-r", "30",
                            "-c:a", "aac", "-b:a", "160k", str(cible)], check=True)
        print(f"Short : {cible} ({duree:.0f} s)")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2] if len(sys.argv) == 3 else None)
