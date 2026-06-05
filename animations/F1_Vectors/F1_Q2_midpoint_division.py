from manim import *
import math

class MidpointDivision(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.2)

        a_pos = LEFT*1.5 + DOWN*1.0
        b_pos = RIGHT*1.5 + UP*1.0
        a_dot = Dot(a_pos, color=BLUE)
        b_dot = Dot(b_pos, color=GREEN)
        a_label = Text("A").scale(0.35).next_to(a_dot, DOWN+LEFT)
        b_label = Text("B").scale(0.35).next_to(b_dot, UP+RIGHT)
        self.play(FadeIn(a_dot), FadeIn(b_dot), Write(a_label), Write(b_label))

        line_ab = Line(a_pos, b_pos, color=YELLOW)
        self.play(Create(line_ab))
        self.wait(0.3)

        mid = (a_pos + b_pos) / 2
        mid_dot = Dot(mid, color=RED)
        mid_label = Text("M").scale(0.35).next_to(mid_dot, DOWN+RIGHT)
        self.play(FadeIn(mid_dot), Write(mid_label))
        self.wait(0.4)

        mid_text = Text("Midpoint = (A + B) / 2", color=WHITE).scale(0.35).to_edge(DOWN)
        self.play(Write(mid_text))
        self.wait(0.5)

        p = (b_pos * 3 + a_pos) / 4
        p_dot = Dot(p, color=PURPLE)
        p_label = Text("P").scale(0.35).next_to(p_dot, DOWN+LEFT)
        self.play(FadeIn(p_dot), Write(p_label))
        self.wait(0.3)

        ratio_text = Text("Section formula: P = (3B + A)/4", color=WHITE).scale(0.3).next_to(mid_text, DOWN)
        self.play(Write(ratio_text))
        self.wait(1.0)
