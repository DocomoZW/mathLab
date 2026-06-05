from manim import *
import math

class NewtonRaphsonB(Scene):
    def construct(self):
        t = Text("NewtonRaphson - Part B", font_size=40, color=WHITE)
        self.play(Write(t))
        self.wait(2)
        self.clear()
        s = Square(side_length=3, color=GREEN)
        self.play(Create(s))
        arr = Arrow(LEFT*2, RIGHT*2, color=ORANGE)
        self.play(GrowArrow(arr))
        self.wait(2)
