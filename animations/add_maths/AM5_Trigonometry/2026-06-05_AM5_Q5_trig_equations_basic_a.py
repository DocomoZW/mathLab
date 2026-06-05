from manim import *
import math

class BasicTrigEquations(Scene):
    def construct(self):
        title = Text("Basic Trig Equations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("Solve cos x = 0.5 for 0 to 360 deg", font_size=28, color=YELLOW)
        eq.shift(UP*1)
        self.play(Write(eq))
        
        pv = Text("Principal value: x = cos^-1(0.5) = 60 deg", font_size=24)
        pv.next_to(eq, DOWN)
        self.play(Write(pv))
        
        cast = Text("Cos positive in Q1 and Q4", font_size=24)
        cast.next_to(pv, DOWN)
        self.play(Write(cast))
        
        q1 = Text("Q1: x = 60 deg", font_size=24, color=GREEN)
        q1.next_to(cast, DOWN)
        self.play(Write(q1))
        
        q4 = Text("Q4: x = 360 - 60 = 300 deg", font_size=24, color=GREEN)
        q4.next_to(q1, DOWN)
        self.play(Write(q4))
        
        tip = Text("Use CAST to find all solutions in range", font_size=22, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
