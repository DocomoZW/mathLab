from manim import *
import math

class CombinedTranslations(Scene):
    def construct(self):
        x_axis = Line(LEFT*4, RIGHT*4, color=GRAY)
        y_axis = Line(DOWN*3, UP*3, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.2)

        p0 = LEFT*2.0 + DOWN*0.5
        dot = Dot(p0, color=BLUE)
        dot_label = Text("P").scale(0.3).next_to(dot, DOWN)
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(0.2)

        v1 = RIGHT*2.0 + UP*1.0
        arrow1 = Arrow(p0, p0+v1, color=YELLOW, stroke_width=4)
        v1_label = Text("[4,2]").scale(0.25).next_to(arrow1.get_end(), UP)
        self.play(GrowArrow(arrow1), Write(v1_label))
        self.wait(0.3)

        p1 = p0 + v1
        dot2 = Dot(p1, color=GREEN)
        dot2_label = Text("P1").scale(0.3).next_to(dot2, DOWN)
        self.play(FadeIn(dot2), Write(dot2_label))
        self.wait(0.2)

        v2 = RIGHT*1.5 + DOWN*1.5
        arrow2 = Arrow(p1, p1+v2, color=RED, stroke_width=4)
        v2_label = Text("[3,-3]").scale(0.25).next_to(arrow2.get_end(), DOWN)
        self.play(GrowArrow(arrow2), Write(v2_label))
        self.wait(0.3)

        p2 = p1 + v2
        dot3 = Dot(p2, color=PURPLE)
        dot3_label = Text("P2").scale(0.3).next_to(dot3, DOWN+RIGHT)
        self.play(FadeIn(dot3), Write(dot3_label))
        self.wait(0.3)

        result = Arrow(p0, p2, color=ORANGE, stroke_width=4)
        result_label = Text("[7,-1] total").scale(0.25).next_to(result, UP)
        self.play(Create(result), Write(result_label))
        self.wait(0.5)

        info = Text("Successive translations add as vectors", color=WHITE).scale(0.3).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
