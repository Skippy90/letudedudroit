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

// Le symbole de la chaîne (docs/marque/symbole.svg) : les trois étages s'empilent de bas en haut,
// puis le toit se dessine — la même construction que le bâtiment des vidéos.
const Symbole: React.FC<{ taille: number; retard?: number }> = ({ taille, retard = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const etage = (n: number) => spring({ frame: frame - (retard + 0.15 * n) * fps, fps, config: { damping: 200 } });
  const toit = interpolate(frame, [(retard + 0.5) * fps, (retard + 0.9) * fps], [1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const barres = [
    { y: 352, couleur: "#4CAF7D", opacite: 1 },
    { y: 284, couleur: "#F2EFE6", opacite: 0.92 },
    { y: 216, couleur: ACCENT, opacite: 1 },
  ];
  return (
    <svg viewBox="104 96 304 316" width={taille} height={taille * 316 / 304}>
      {barres.map((b, n) => (
        <rect key={n} x={150} y={b.y} width={212} height={52} rx={10} fill={b.couleur}
          fillOpacity={b.opacite * etage(n)} transform={`translate(0 ${(1 - etage(n)) * 30})`} />
      ))}
      <path d="M112 200 L256 104 L400 200" fill="none" stroke={TEXTE} strokeWidth={20} strokeLinecap="round"
        strokeLinejoin="round" pathLength={1} strokeDasharray={1} strokeDashoffset={toit} />
    </svg>
  );
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
    <Symbole taille={150} />
    <Apparition retard={0.4}>
      <div style={{ fontSize: 44, color: ACCENT, fontWeight: 600 }}>L’étude du droit</div>
    </Apparition>
    <Apparition retard={0.8}>
      <div style={{ fontSize: 88, fontWeight: 800, maxWidth: 1600, letterSpacing: -1 }}>{titre.replace(/'/g, "’")}</div>
    </Apparition>
    <Apparition retard={1.5}>
      <div style={{ fontSize: 40, color: GRIS }}>
        {matiere} · vidéo {numero}
      </div>
    </Apparition>
  </Ecran>
);

export const Fin: React.FC<VideoProps> = ({ narrationSynthetique }) => (
  <Ecran fondu="entree">
    <Symbole taille={190} retard={0.2} />
    <Apparition retard={0.9}>
      <div style={{ fontSize: 72, fontWeight: 800, color: TEXTE }}>L’étude du droit</div>
    </Apparition>
    <Apparition retard={1.3}>
      <div style={{ fontSize: 44, color: ACCENT, fontWeight: 500 }}>Le droit suisse, une notion à la fois</div>
    </Apparition>
    <Apparition retard={1.9}>
      <div style={{ fontSize: 40 }}>Script et sources sur GitHub</div>
    </Apparition>
    <Apparition retard={2.4}>
      <div style={{ fontSize: 40, color: GRIS }}>
        Licence CC BY-SA 4.0{narrationSynthetique ? " · Narration synthétique" : ""}
      </div>
    </Apparition>
  </Ecran>
);
