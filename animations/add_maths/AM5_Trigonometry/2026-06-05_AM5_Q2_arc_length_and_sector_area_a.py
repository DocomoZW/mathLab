from manim import *
import math

class ArcSector(Scene):
    def construct(self):
        title = Text("Arc Length and Sector Area", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        arc = Text("Arc Length: s = r * theta", font_size=28, color=YELLOW)
        arc.shift(UP*1.5)
        self.play(Write(arc))
        
        area = Text("Sector Area: A = (1/2)r^2 * theta", font_size=28, color=YELLOW)
        area.next_to(arc, DOWN)
        self.play(Write(area))
        
        ex = Text("For r=6, theta=pi/3:", font_size=24)
        ex.next_to(area, DOWN)
        self.play(Write(ex))
        
        ex_a = Text("Arc = 6*pi/3 = 2pi = 6.28 cm", font_size=26, color=GREEN)
        ex_a.next_to(ex, DOWN)
        self.play(Write(ex_a))
        
        ex_b = Text("Area = 0.5*36*pi/3 = 6pi = 18.85 cm^2", font_size=26, color=GREEN)
        ex_b.next_to(ex_a, DOWN)
        self.play(Write(ex_b))
        
        note = Text("Use radians only!", font_size=24, color=RED)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
