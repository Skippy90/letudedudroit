import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { ACCENT, FOND, GRIS, POLICE, TEXTE } from "./charte";

export type VideoProps = {
  titre: string;
  matiere: string;
  numero: number;
  narrationSynthetique: boolean;
};

export const DUREE_OUVERTURE = 4; // secondes, reprise par tools/assembler.py et tools/publication.py
export const DUREE_FIN = 6;

// Apparition douce, décalée de `retard` secondes.
const Apparition: React.FC<{ retard: number; children: React.ReactNode }> = ({ retard, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const p = spring({ frame: frame - retard * fps, fps, config: { damping: 200 } });
  return <div style={{ opacity: p, transform: `translateY(${(1 - p) * 24}px)` }}>{children}</div>;
};

// Écran centré, avec un fondu vers le bleu nuit en sortie (ouverture) ou en entrée (fin),
// pour que les raccords avec les schémas restent doux.
const Ecran: React.FC<{ fondu: "sortie" | "entree"; children: React.ReactNode }> = ({ fondu, children }) => {
  const frame = useCurrentFrame();
  const { durationInFrames } = useVideoConfig();
  const opacite = fondu === "sortie"
    ? interpolate(frame, [durationInFrames - 12, durationInFrames - 1], [1, 0], { extrapolateLeft: "clamp" })
    : interpolate(frame, [0, 12], [0, 1], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ backgroundColor: FOND }}>
      <AbsoluteFill
        style={{
          color: TEXTE, fontFamily: POLICE, justifyContent: "center", alignItems: "center",
          textAlign: "center", gap: 36, opacity: opacite,
        }}
      >
        {children}
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

export const Ouverture: React.FC<VideoProps> = ({ titre, matiere, numero }) => (
  <Ecran fondu="sortie">
    <Apparition retard={0}>
      <div style={{ fontSize: 44, color: ACCENT, fontWeight: 600 }}>L'étude du droit</div>
    </Apparition>
    <Apparition retard={0.6}>
      <div style={{ fontSize: 96, fontWeight: 700, maxWidth: 1600 }}>{titre}</div>
    </Apparition>
    <Apparition retard={1.4}>
      <div style={{ fontSize: 44, color: GRIS }}>
        {matiere} · vidéo {numero}
      </div>
    </Apparition>
  </Ecran>
);

export const Fin: React.FC<VideoProps> = ({ narrationSynthetique }) => (
  <Ecran fondu="entree">
    <Apparition retard={0.3}>
      <div style={{ fontSize: 72, fontWeight: 700, color: ACCENT }}>L'étude du droit</div>
    </Apparition>
    <Apparition retard={1.0}>
      <div style={{ fontSize: 48 }}>Script et sources sur GitHub</div>
    </Apparition>
    <Apparition retard={1.8}>
      <div style={{ fontSize: 40, color: GRIS }}>
        Licence CC BY-SA 4.0{narrationSynthetique ? " · Narration synthétique" : ""}
      </div>
    </Apparition>
  </Ecran>
);
