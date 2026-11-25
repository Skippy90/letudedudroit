from base import *


def fond(s):
    s.add(Rectangle(width=16, height=9, stroke_width=0).set_fill(color=[ROUGE, ROUGE_3], opacity=1).set_sheen_direction(DOWN))


class MiniA(Scene):
    """Le score : 8 sur 8, 0 sur 38."""
    def construct(self):
        fond(self)
        lieu = bandeau("EMMEN (LUCERNE) · VOTE DU 12 MARS 2000", 30).to_corner(UL, buff=0.35); self.add(lieu)
        def rang(nom, score, ok, y):
            f = RoundedRectangle(corner_radius=0.25, width=13.3, height=2.3, fill_color=CREME if ok else ROUGE_4, fill_opacity=1, stroke_width=0).move_to([0, y, 0])
            c = ENCRE if ok else CREME
            n = T(nom, 50, c).move_to(f.get_left() + 0.45 * RIGHT, aligned_edge=LEFT).shift(0.4 * UP)
            e = T("naturalisés", 36, c, False).next_to(n, DOWN, buff=0.2, aligned_edge=LEFT)
            sc = T(score, 132, ROUGE if ok else CREME).move_to(f.get_right() + 0.45 * LEFT, aligned_edge=RIGHT)
            return VGroup(f, n, e, sc)
        self.add(rang("Italiens", "8 / 8", True, 1.55), rang("Ex-Yougoslaves", "0 / 38", False, -0.95))
        q = T("Le peuple peut-il voter ça ?", 58).move_to([0, -3.15, 0]); self.add(q)


class MiniB(Scene):
    """Le passeport refusé par les urnes."""
    def construct(self):
        fond(self)
        t = VGroup(T("EMMEN, 2000", 60), T("38 refusés", 112), T("pour leur origine", 72)).arrange(DOWN, buff=0.25, aligned_edge=LEFT).to_corner(UL, buff=0.55)
        f = RoundedRectangle(corner_radius=0.2, width=t[1].width + 0.6, height=t[1].height + 0.45, fill_color=CREME, fill_opacity=1, stroke_width=0).move_to(t[1]); t[1].set_color(ROUGE)
        self.add(t[0], f, t[1], t[2])
        p = passeport(3.0).rotate(-0.12).move_to([4.9, -0.7, 0]); self.add(p)
        s = tampon("REFUSÉ", 66, 0.2).move_to([4.75, -1.6, 0]); self.add(s)
        b = VGroup(T("Le peuple avait voté.", 46, CREME, False), T("Le Tribunal fédéral annule.", 54)).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_corner(DL, buff=0.55); self.add(b)
