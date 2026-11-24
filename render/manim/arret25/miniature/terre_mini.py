import sys; sys.path.insert(0, "/home/claude/a25")
from base import *
class TerreNue(Scene):
    def construct(self):
        t = terre(3.2, None)
        for x in t.get_family(): x.clear_updaters()
        self.add(t)
