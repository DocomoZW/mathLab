from manim import *
import math

class ScalarMultiplication(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        origin = Dot(ORIGIN, color=WHITE, radius=0.05)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label), FadeIn(origin))
        self.wait(0.2)

        end_v = RIGHT*1.0 + UP*0.5
        vec_v = Arrow(ORIGIN, end_v, color=BLUE, stroke_width=4)
        label_v = Text("v=[2,1]").scale(0.35).next_to(end_v, UP+RIGHT)
        self.play(GrowArrow(vec_v), Write(label_v))
        self.wait(0.5)

        end_2v = RIGHT*2.0 + UP*1.0
        vec_2v = Arrow(ORIGIN, end_2v, color=YELLOW, stroke_width=4)
        label_2v = Text("2v=[4,2]").scale(0.35).next_to(end_2v, UP+RIGHT)
        self.play(Create(vec_2v), Write(label_2v))
        self.wait(0.5)

        end_nv = LEFT*1.0 + DOWN*0.5
        vec_nv = Arrow(ORIGIN, end_nv, color=RED, stroke_width=4)
        label_nv = Text("-v=[-2,-1]").scale(0.35).next_to(end_nv, DOWN+LEFT)
        self.play(Create(vec_nv), Write(label_nv))
        self.wait(0.5)

        info = Text("Scalar mult: 2v doubles, -v reverses direction", color=WHITE).scale(0.35).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
