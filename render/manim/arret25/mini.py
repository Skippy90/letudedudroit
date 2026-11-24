from base import *


class Mini(Scene):
    """Deux tribunaux, deux réponses : le Tribunal fédéral rejette, Strasbourg condamne la Suisse."""
    def construct(self):
        self.add(Rectangle(width=16, height=9, stroke_width=0).set_fill(color=[ROUGE, ROUGE_3], opacity=1).set_sheen_direction(DOWN))
        for c, r, o in (([-6.2, 2.6, 0], 3.0, 0.10), ([6.4, -2.2, 0], 3.6, 0.08), ([0, 0.3, 0], 2.4, 0.06)):
            self.add(Circle(r, fill_color=BLANC, fill_opacity=o, stroke_width=0).move_to(c))
        def fige(m):
            for x in m.get_family(): x.clear_updaters()
            return m
        def cote(dessin, nom, an, lignes, x):
            f = RoundedRectangle(corner_radius=0.3, width=5.5, height=5.5, fill_color=ROUGE_4, fill_opacity=0.9, stroke_width=0).move_to([x, 0.85, 0])
            n = T(nom, 40, CREME).move_to(f.get_top() + 0.55 * DOWN)
            a = T(an, 30, CREME, False).next_to(n, DOWN, buff=0.14)
            dessin.move_to(f.get_center() + (0.25 * UP if len(lignes) > 1 else 0.2 * DOWN))
            tx = VGroup(*[T(l, 44, ROUGE) for l in lignes]).arrange(DOWN, buff=0.12)
            cadre = RoundedRectangle(corner_radius=0.08, width=tx.width + 0.55, height=tx.height + 0.45, color=ROUGE, stroke_width=7, fill_color=CREME, fill_opacity=1)
            t = VGroup(cadre, tx).rotate(-0.08); t.move_to(f.get_bottom() + (1.0 if len(lignes) > 1 else 0.6) * UP)
            return VGroup(f, n, a, dessin, t)
        self.add(cote(tribunal(2.7), "Tribunal fédéral", "2020", ["REJETÉ"], -4.2), cote(cour(2.7), "Strasbourg", "2024", ["SUISSE", "CONDAMNÉE"], 4.2))
        t = fige(terre(1.1, "inquiet")).move_to([0, 1.75, 0]); self.add(t)
        q = VGroup(*[fige(ainee(1.15, ROBES[k], "content" if k % 2 else "neutre")) for k in range(4)]).arrange(RIGHT, buff=0.02, aligned_edge=DOWN)
        q.move_to([0, -0.75, 0]); self.add(q)
        self.add(bandeau("COMMENT EST-CE POSSIBLE ?", 46).move_to([0, -3.35, 0]))
