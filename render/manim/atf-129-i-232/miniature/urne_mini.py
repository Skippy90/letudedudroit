import sys; sys.path.insert(0, "/home/claude/z232")
from base import *
class UrneNue(Scene):
    def construct(self):
        u = urne(3.4)
        for x in u.get_family(): x.clear_updaters()
        c = cadenas(2.2).move_to(u[1].get_center() + 0.25 * DOWN)
        self.add(u, c)
