from manim import *
import math

class ConjugateRationalise(Scene):
    def construct(self):
        title = Text("Rationalising with Conjugates", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        expr = Text("Rationalise: 2/(3-sqrt(5))", font_size=28, color=YELLOW)
        expr.shift(UP*1)
        self.play(Write(expr))
        
        step1 = Text("Multiply by conjugate (3+sqrt5):", font_size=24)
        step1.next_to(expr, DOWN)
        self.play(Write(step1))
        
        step2 = Text("= 2(3+sqrt5) / (9-5)", font_size=26)
        step2.next_to(step1, DOWN)
        self.play(Write(step2))
        
        step3 = Text("= (6+2sqrt5)/4 = (3+sqrt5)/2", font_size=26, color=GREEN)
        step3.next_to(step2, DOWN)
        self.play(Write(step3))
        
        tip = Text("Conjugate of a+sqrtb is a-sqrtb", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
