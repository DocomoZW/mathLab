from manim import *
import math

class PolynomialOps(Scene):
    def construct(self):
        title = Text("Polynomial Operations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        p = Text("P(x) = 2x^3 - 3x^2 + 4x - 5", font_size=28, color=YELLOW)
        p.shift(UP*1)
        self.play(Write(p))
        
        q = Text("Divide by (x-2)", font_size=26)
        q.next_to(p, DOWN)
        self.play(Write(q))
        
        r1 = Text("Step 1: 2x^3 / x = 2x^2", font_size=24)
        r1.next_to(q, DOWN)
        self.play(Write(r1))
        
        r2 = Text("Step 2: Multiply back, subtract", font_size=24)
        r2.next_to(r1, DOWN)
        self.play(Write(r2))
        
        result = Text("Quotient: 2x^2 + x + 6, Remainder: 7", font_size=26, color=GREEN)
        result.next_to(r2, DOWN)
        self.play(Write(result))
        
        note = Text("Dividend = Divisor x Quotient + Remainder", font_size=24, color=BLUE)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
