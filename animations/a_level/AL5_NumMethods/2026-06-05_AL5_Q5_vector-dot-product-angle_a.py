from manim import *
import math

class DotProductAngleA(Scene):
    def construct(self):
        t = Text("DotProduct ngle - Part A", font_size=40, color=WHITE)
        self.play(Write(t))
        self.wait(2)
        self.clear()
        c = Circle(radius=2, color=BLUE)
        self.play(Create(c))
        l = Line(LEFT*2.5, RIGHT*2.5, color=YELLOW)
        self.play(Create(l))
        d = Dot(color=RED)
        self.play(FadeIn(d))
        self.wait(2)
