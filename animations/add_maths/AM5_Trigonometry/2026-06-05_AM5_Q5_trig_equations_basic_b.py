from manim import *
import math

class TrigRadians(Scene):
    def construct(self):
        title = Text("Solving in Radians", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Solve sin x = 1/2 for 0 <= x <= 2pi", font_size=26, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        pv = Text("Principal: x = sin^-1(1/2) = pi/6", font_size=24)
        pv.next_to(ex, DOWN)
        self.play(Write(pv))
        
        cast = Text("Sin positive in Q1 and Q2", font_size=24)
        cast.next_to(pv, DOWN)
        self.play(Write(cast))
        
        q1 = Text("Q1: x = pi/6", font_size=24, color=GREEN)
        q1.next_to(cast, DOWN)
        self.play(Write(q1))
        
        q2 = Text("Q2: x = pi - pi/6 = 5pi/6", font_size=24, color=GREEN)
        q2.next_to(q1, DOWN)
        self.play(Write(q2))
        
        self.wait(2)
