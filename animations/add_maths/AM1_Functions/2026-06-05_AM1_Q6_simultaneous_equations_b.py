from manim import *
import math

class IntersectionCase(Scene):
    def construct(self):
        title = Text("Intersection of Line and Curve", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        
        c1 = Text("Case 1: Delta > 0 -> Two intersection points", font_size=24, color=BLUE)
        c1.shift(UP*2)
        c2 = Text("Case 2: Delta = 0 -> One point (tangent)", font_size=24, color=GREEN)
        c2.next_to(c1, DOWN, buff=0.3)
        c3 = Text("Case 3: Delta < 0 -> No intersection", font_size=24, color=RED)
        c3.next_to(c2, DOWN, buff=0.3)
        
        self.play(Write(c1), Write(c2), Write(c3))
        
        dc = Text("Discriminant after substitution determines case", font_size=24, color=YELLOW)
        dc.next_to(c3, DOWN, buff=0.5)
        self.play(Write(dc))
        
        self.wait(2)
