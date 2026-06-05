from manim import *
import math

class PolynomialExpand(Scene):
    def construct(self):
        title = Text("Multiplying Polynomials", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Expand: (x+2)(x^2-3x+1)", font_size=26, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        s1 = Text("x(x^2-3x+1) = x^3-3x^2+x", font_size=24)
        s1.next_to(ex, DOWN)
        self.play(Write(s1))
        
        s2 = Text("2(x^2-3x+1) = 2x^2-6x+2", font_size=24)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("Sum: x^3 - x^2 - 5x + 2", font_size=26, color=GREEN)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        tip = Text("Multiply each term, then collect like terms", font_size=22, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
