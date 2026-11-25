// Word modifiable du script d'un grand arrêt. Appelé par tools/script_arret_annote.py : node script_arret_docx.js donnees.json sortie.docx
const fs = require("fs");
const { Document, Packer, Paragraph, TextRun, Table, TableRow, TableCell, WidthType, ShadingType, BorderStyle, PageOrientation, AlignmentType, LevelFormat, UnderlineType } = require("docx");
const d = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const ROUGE = "DA291C", F = "Arial", L = 14400, C1 = 3900, C2 = L - C1;
const fin = { style: BorderStyle.SINGLE, size: 4, color: "DDDDDD" }, rien = { style: BorderStyle.NONE, size: 0, color: "FFFFFF" };
const run = (t, o = {}) => new TextRun({ text: t, font: F, size: 24, ...o });
const texte = (s) => [run(`${s.n}. `)].concat(s.morceaux.map(([t, c]) =>
  c === "tie" ? run("‿", { color: ROUGE, bold: true, font: "Segoe UI Symbol" })
  : c === "l" ? run(t, { color: ROUGE, underline: { type: UnderlineType.SINGLE, color: ROUGE } }) : run(t)));
const cel = (enfants, w, o = {}) => new TableCell({ children: enfants, width: { size: w, type: WidthType.DXA }, margins: { top: 110, bottom: 110, left: 140, right: 140 },
  borders: { top: rien, left: o.gauche || rien, right: rien, bottom: fin }, ...(o.fond ? { shading: { type: ShadingType.CLEAR, fill: o.fond, color: "auto" } } : {}) });
const lignes = [new TableRow({ tableHeader: true, children: ["MARGE · DIRECTION VOCALE", "TEXTE À ENREGISTRER"].map((t, i) =>
  cel([new Paragraph({ children: [run(t, { size: 16, color: "888888", bold: true })] })], i ? C2 : C1)) })]
  .concat(d.sequences.map((s) => new TableRow({ cantSplit: true, children: [
    cel([new Paragraph({ children: [run(String(s.n).padStart(2, "0") + "  ", { size: 19, bold: true, color: ROUGE }), run(s.etiquette, { size: 19, bold: true }), run(" | " + s.ton, { size: 19, color: "777777" })] }),
         new Paragraph({ spacing: { before: 50 }, children: [run(s.direction, { size: 19, italics: true, color: s.dm ? "8A5A00" : "555555" })] })], C1),
    cel([new Paragraph({ spacing: { line: 340 }, children: texte(s) })], C2, s.m ? { gauche: { style: BorderStyle.SINGLE, size: 18, color: "E0A526" } } : {})] })));
const p = (enf, o = {}) => new Paragraph({ children: enf, ...o });
const doc = new Document({
  numbering: { config: [{ reference: "puces", levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 500, hanging: 260 } } } }] }] },
  sections: [{ properties: { page: { size: { width: 11906, height: 16838, orientation: PageOrientation.LANDSCAPE }, margin: { top: 900, bottom: 900, left: 1200, right: 1200 } } },
    children: [
      p([run("L’ÉTUDE DU DROIT / SCRIPT DE VOIX OFF · VERSION DÉFINITIVE", { size: 16, color: "888888" })], { alignment: AlignmentType.RIGHT }),
      p([run(d.titre, { size: 40, bold: true })], { spacing: { before: 120, after: 40 } }),
      p([run(d.sous_titre, { size: 21, color: "555555" })], { spacing: { after: 160 } }),
      p([run("Mode d’emploi. ", { size: 20, bold: true }), run("Lire uniquement la colonne de droite. Les consignes en marge dirigent l’intention, le débit et les silences. Les numéros restent fixes pour le montage.", { size: 20 })]),
      p([run("Liaisons. ", { size: 20, bold: true }), run("Le signe ", { size: 20 }), run("‿", { size: 20, color: ROUGE, bold: true, font: "Segoe UI Symbol" }), run(" et les deux lettres ", { size: 20 }),
         run("soulignées en rouge", { size: 20, color: ROUGE, underline: { type: UnderlineType.SINGLE, color: ROUGE } }),
         run(" marquent une liaison à faire. Seules les liaisons obligatoires ou attendues en lecture soignée sont marquées ; ailleurs, lire naturellement.", { size: 20 })]),
      p([run("Repères. ", { size: 20, bold: true }), run("Trait ambre à gauche du texte : séquence corrigée après l’audit. Consigne en brun : consigne ajustée.", { size: 20 })], { spacing: { after: 200 } }),
      new Table({ width: { size: L, type: WidthType.DXA }, columnWidths: [C1, C2], rows: lignes }),
      p([run("Notes juridiques · Ne pas lire à l’antenne", { size: 26, bold: true })], { pageBreakBefore: true, spacing: { after: 140 } }),
      ...d.notes.map((n) => p([run(n, { size: 20 })], { numbering: { reference: "puces", level: 0 }, spacing: { after: 90 } })),
      p([run(d.direction_generale, { size: 20 })], { spacing: { before: 200 } }),
    ] }] });
Packer.toBuffer(doc).then((b) => fs.writeFileSync(process.argv[3], b));
