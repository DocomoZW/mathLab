from manim import *
import math

class CubicEquations(Scene):
    def construct(self):
        title = Text("Solving Cubic Equations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("x^3 - 2x^2 - 5x + 6 = 0", font_size=28, color=YELLOW)
        eq.shift(UP*1)
        self.play(Write(eq))
        
        s1 = Text("Test x=1: 1-2-5+6=0 => (x-1) is factor", font_size=24)
        s1.next_to(eq, DOWN)
        self.play(Write(s1))
        
        s2 = Text("Divide: (x^3-2x^2-5x+6)/(x-1) = x^2-x-6", font_size=24)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("x^2-x-6 = (x-3)(x+2) = 0", font_size=26)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        roots = Text("Roots: x = 1, 3, -2", font_size=28, color=GREEN)
        roots.next_to(s3, DOWN)
        self.play(Write(roots))
        
        self.wait(2)
