import { Composition } from "remotion";
import { FPS } from "./charte";
import { DUREE_FIN, DUREE_OUVERTURE, Fin, Ouverture, VideoProps } from "./Video";

const parDefaut: VideoProps = {
  titre: "Titre",
  matiere: "Droit pénal général",
  numero: 1,
  narrationSynthetique: true,
};

// Remotion rend l'habillage ; ffmpeg monte ensuite ouverture, schémas Manim, fin et narration
// (tools/assembler.py), ce qui évite de recalculer chaque image des schémas dans le navigateur.
export const Root: React.FC = () => (
  <>
    <Composition id="Ouverture" component={Ouverture} width={1920} height={1080} fps={FPS}
      durationInFrames={DUREE_OUVERTURE * FPS} defaultProps={parDefaut} />
    <Composition id="Fin" component={Fin} width={1920} height={1080} fps={FPS}
      durationInFrames={DUREE_FIN * FPS} defaultProps={parDefaut} />
  </>
);
