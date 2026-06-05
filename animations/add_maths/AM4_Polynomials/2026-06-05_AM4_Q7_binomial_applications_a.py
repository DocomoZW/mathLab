from manim import *
import math

class BinomialApplications(Scene):
    def construct(self):
        title = Text("Binomial Applications", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Expand (1+2x)^5(1-x)^3 up to x^2", font_size=26, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        exp1 = Text("(1+2x)^5 = 1 + 10x + 40x^2 + ...", font_size=24)
        exp1.next_to(ex, DOWN)
        self.play(Write(exp1))
        
        exp2 = Text("(1-x)^3 = 1 - 3x + 3x^2 - ...", font_size=24)
        exp2.next_to(exp1, DOWN)
        self.play(Write(exp2))
        
        prod = Text("Product = 1 + 7x + 13x^2 + ...", font_size=26, color=GREEN)
        prod.next_to(exp2, DOWN)
        self.play(Write(prod))
        
        tip = Text("Expand each factor, then multiply term by term", font_size=22, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
