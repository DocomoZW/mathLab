from manim import *
import math

class AdvancedTrigEquations(Scene):
    def construct(self):
        title = Text("Advanced Trig Equations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("Solve: 2sin^2 x - sin x - 1 = 0", font_size=26, color=YELLOW)
        eq.shift(UP*1.5)
        self.play(Write(eq))
        
        s1 = Text("Let u = sin x", font_size=26)
        s1.next_to(eq, DOWN)
        self.play(Write(s1))
        
        s2 = Text("2u^2 - u - 1 = 0", font_size=26)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("(2u+1)(u-1) = 0 => u = -1/2 or u = 1", font_size=24)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        s4 = Text("sin x = 1 => x = 90 deg", font_size=24, color=GREEN)
        s4.next_to(s3, DOWN)
        self.play(Write(s4))
        
        s5 = Text("sin x = -1/2 => x = 210, 330 deg", font_size=24, color=GREEN)
        s5.next_to(s4, DOWN)
        self.play(Write(s5))
        
        self.wait(2)
