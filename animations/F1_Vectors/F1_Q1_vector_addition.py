from manim import *
import math

class VectorAddition(Scene):
    def construct(self):
        # Coordinate lines
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        origin = Dot(ORIGIN, color=WHITE, radius=0.05)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label), FadeIn(origin))
        self.wait(0.2)

        # Vector a: [3,1] from origin
        end_a = RIGHT*1.5 + UP*0.5
        vec_a = Arrow(ORIGIN, end_a, color=BLUE, stroke_width=4)
        label_a = Text("a=[3,1]").scale(0.35).next_to(end_a, UP+RIGHT)
        self.play(GrowArrow(vec_a), Write(label_a))
        self.wait(0.5)

        # Vector b: [2,3] from tip of a
        end_b = end_a + RIGHT*1.0 + UP*1.5
        vec_b = Arrow(end_a, end_b, color=GREEN, stroke_width=4)
        label_b = Text("b=[2,3]").scale(0.35).next_to(end_b, UP+RIGHT)
        self.play(GrowArrow(vec_b), Write(label_b))
        self.wait(0.5)

        # Resultant a+b = [5,4]
        vec_sum = Arrow(ORIGIN, end_b, color=YELLOW, stroke_width=4)
        label_sum = Text("a+b=[5,4]").scale(0.35).next_to(end_b, UP+RIGHT)
        self.play(Create(vec_sum), Write(label_sum))
        self.wait(1.0)

        info = Text("Tip-to-tail vector addition", color=WHITE).scale(0.4).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
