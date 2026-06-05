from manim import *
import math

class FactorTheorem(Scene):
    def construct(self):
        title = Text("Factor Theorem", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        theorem = Text("If f(a)=0, then (x-a) is a factor", font_size=28, color=YELLOW)
        theorem.shift(UP*1)
        self.play(Write(theorem))
        
        ex = Text("f(x) = x^3 - 3x^2 - 4x + 12", font_size=26)
        ex.next_to(theorem, DOWN)
        self.play(Write(ex))
        
        test = Text("f(2) = 8 - 12 - 8 + 12 = 0", font_size=26, color=GREEN)
        test.next_to(ex, DOWN)
        self.play(Write(test))
        
        factor = Text("So (x-2) is a factor!", font_size=28, color=ORANGE)
        factor.next_to(test, DOWN)
        self.play(Write(factor))
        
        tip = Text("Test factors of the constant term", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
