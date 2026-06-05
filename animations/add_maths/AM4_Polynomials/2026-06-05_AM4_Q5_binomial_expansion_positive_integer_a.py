from manim import *
import math

class BinomialExpansion(Scene):
    def construct(self):
        title = Text("Binomial Theorem", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        formula = Text("(a+b)^n = sum C(n,r) a^{n-r} b^r", font_size=26, color=YELLOW)
        formula.shift(UP*1.5)
        self.play(Write(formula))
        
        ex = Text("(2x-3)^4", font_size=30)
        ex.next_to(formula, DOWN)
        self.play(Write(ex))
        
        pascals = Text("Coefficients: 1, 4, 6, 4, 1", font_size=26, color=BLUE)
        pascals.next_to(ex, DOWN)
        self.play(Write(pascals))
        
        ex1 = Text("= 1(16x^4) + 4(8x^3)(-3) + 6(4x^2)(9)", font_size=22)
        ex1.next_to(pascals, DOWN)
        self.play(Write(ex1))
        
        ex2 = Text("+ 4(2x)(-27) + 1(1)(81)", font_size=22)
        ex2.next_to(ex1, DOWN)
        self.play(Write(ex2))
        
        result = Text("= 16x^4 - 96x^3 + 216x^2 - 216x + 81", font_size=24, color=GREEN)
        result.next_to(ex2, DOWN)
        self.play(Write(result))
        
        self.wait(2)
