from manim import *
import math

class BinomialApprox(Scene):
    def construct(self):
        title = Text("Binomial Approximations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Estimate (1.01)^5 using binomial", font_size=26, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        s1 = Text("(1+0.01)^5 = 1 + 5(0.01) + 10(0.0001) + ...", font_size=24)
        s1.next_to(ex, DOWN)
        self.play(Write(s1))
        
        s2 = Text("= 1 + 0.05 + 0.001 + 0.00001 + ...", font_size=24)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("= 1.05101 (accurate to 5 d.p.)", font_size=26, color=GREEN)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        tip = Text("Only first few terms needed for small x", font_size=22, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
