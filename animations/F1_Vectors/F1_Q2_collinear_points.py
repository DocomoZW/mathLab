from manim import *
import math

class CollinearPoints(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        origin = Dot(ORIGIN, color=WHITE, radius=0.05)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label), FadeIn(origin))
        self.wait(0.2)

        a_pos = LEFT*1.5 + DOWN*1.0
        b_pos = LEFT*0.5 + UP*0.0
        c_pos = RIGHT*0.5 + UP*1.0

        a_dot = Dot(a_pos, color=BLUE)
        b_dot = Dot(b_pos, color=GREEN)
        c_dot = Dot(c_pos, color=RED)

        a_label = Text("A").scale(0.35).next_to(a_dot, DOWN+LEFT)
        b_label = Text("B").scale(0.35).next_to(b_dot, UP+RIGHT)
        c_label = Text("C").scale(0.35).next_to(c_dot, UP+RIGHT)

        self.play(FadeIn(a_dot), FadeIn(b_dot), FadeIn(c_dot),
                  Write(a_label), Write(b_label), Write(c_label))
        self.wait(0.3)

        line_ab = Line(a_pos, b_pos, color=YELLOW)
        line_bc = Line(b_pos, c_pos, color=YELLOW)
        ab_label = Text("AB").scale(0.3).next_to(line_ab.get_center(), UP)
        bc_label = Text("BC").scale(0.3).next_to(line_bc.get_center(), UP)
        self.play(Create(line_ab), Write(ab_label))
        self.play(Create(line_bc), Write(bc_label))
        self.wait(0.3)

        info = Text("Collinear: AB = BC so points lie on a line", color=WHITE).scale(0.35).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
