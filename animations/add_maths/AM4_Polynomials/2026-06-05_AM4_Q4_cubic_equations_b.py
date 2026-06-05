from manim import *
import math

class CubicExample(Scene):
    def construct(self):
        title = Text("Solving a Cubic", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("x^3 - 6x^2 + 11x - 6 = 0", font_size=28, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        s1 = Text("Test x=1: 1-6+11-6=0 => (x-1) factor", font_size=24)
        s1.next_to(ex, DOWN)
        self.play(Write(s1))
        
        s2 = Text("Divide: (x^3-6x^2+11x-6)/(x-1)", font_size=24)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("= x^2-5x+6 = (x-2)(x-3)", font_size=26)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        roots = Text("Roots: x = 1, 2, 3", font_size=28, color=GREEN)
        roots.next_to(s3, DOWN)
        self.play(Write(roots))
        
        self.wait(2)
