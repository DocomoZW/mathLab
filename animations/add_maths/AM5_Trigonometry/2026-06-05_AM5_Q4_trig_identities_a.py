from manim import *
import math

class TrigIdentities(Scene):
    def construct(self):
        title = Text("Trigonometric Identities", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        id1 = Text("sin^2 A + cos^2 A = 1", font_size=28, color=YELLOW)
        id1.shift(UP*1)
        self.play(Write(id1))
        
        id2 = Text("tan A = sin A / cos A", font_size=28, color=YELLOW)
        id2.next_to(id1, DOWN)
        self.play(Write(id2))
        
        id3 = Text("1 + tan^2 A = sec^2 A", font_size=28, color=YELLOW)
        id3.next_to(id2, DOWN)
        self.play(Write(id3))
        
        ex = Text("Simplify: (1-cos^2)/(1-sin^2) = tan^2", font_size=26, color=GREEN)
        ex.next_to(id3, DOWN)
        self.play(Write(ex))
        
        tip = Text("Use identities to rewrite and simplify", font_size=22, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
