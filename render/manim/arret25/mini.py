from base import *
from s_a import quatre


class Mini(Scene):
    """Deux tribunaux, deux réponses."""
    def construct(self):
        self.add(Rectangle(width=16, height=9, stroke_width=0).set_fill(color=[ROUGE, ROUGE_3], opacity=1).set_sheen_direction(DOWN))
        self.add(bandeau("LES AÎNÉES POUR LE CLIMAT CONTRE LA SUISSE", 30).move_to([0, 3.35, 0]))
        def rang(nom, an, verdict, ok, y):
            f = RoundedRectangle(corner_radius=0.25, width=8.2, height=2.2, fill_color=CREME if ok else ROUGE_4, fill_opacity=1, stroke_width=0).move_to([-2.65, y, 0])
            c = ENCRE if ok else CREME
            n = T(nom, 38, c).move_to(f.get_left() + 0.4 * RIGHT, aligned_edge=LEFT).shift(0.55 * UP)
            a = T(an, 30, c, False).next_to(n, DOWN, buff=0.18, aligned_edge=LEFT)
            v = T(verdict, 62, ROUGE if ok else CREME).move_to(f.get_right() + 0.4 * LEFT + 0.35 * DOWN, aligned_edge=RIGHT)
            return VGroup(f, n, a, v)
        self.add(rang("Tribunal fédéral", "2020", "REJETÉ", False, 1.6), rang("Strasbourg", "2024", "GAGNÉ", True, -0.85))
        q = VGroup(*[ainee(2.0, ROBES[k], "content") for k in range(4)]).arrange(RIGHT, buff=0.02, aligned_edge=DOWN); q.clear_updaters()
        for x in q: x.clear_updaters()
        q.move_to([4.2, -0.3, 0]); self.add(q)
        self.add(T("Comment est-ce possible ?", 58).move_to([0, -3.3, 0]))
