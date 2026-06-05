from manim import *
import math

class LogApplications(Scene):
    def construct(self):
        title = Text("Log Equations: Applications", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("Solve: log_2 x + log_2(x-2) = 3", font_size=28, color=YELLOW)
        eq.shift(UP*0.5)
        self.play(Write(eq))
        
        s1 = Text("log_2[x(x-2)] = 3", font_size=26)
        s1.next_to(eq, DOWN)
        self.play(Write(s1))
        
        s2 = Text("x(x-2) = 8", font_size=26)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("x^2 - 2x - 8 = 0", font_size=26)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        s4 = Text("(x-4)(x+2)=0 => x=4 (x=-2 invalid)", font_size=28, color=GREEN)
        s4.next_to(s3, DOWN)
        self.play(Write(s4))
        
        tip = Text("Always check: log arguments must be positive", font_size=24, color=RED)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
