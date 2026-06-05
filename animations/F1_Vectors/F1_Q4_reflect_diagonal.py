from manim import *
import math

class ReflectDiagonal(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.2)

        line_yx = Line(DOWN*3+LEFT*3, UP*3+RIGHT*3, color=YELLOW, stroke_width=2)
        line_ynegx = Line(UP*3+LEFT*3, DOWN*3+RIGHT*3, color=ORANGE, stroke_width=2)
        label_yx = Text("y=x").scale(0.3).next_to(UP*3+RIGHT*3, UP+RIGHT)
        label_ynegx = Text("y=-x").scale(0.3).next_to(DOWN*3+RIGHT*3, DOWN+RIGHT)
        self.play(Create(line_yx), Write(label_yx), Create(line_ynegx), Write(label_ynegx))
        self.wait(0.3)

        p_pos = LEFT*1.0 + UP*1.5
        dot = Dot(p_pos, color=BLUE)
        dot_label = Text("P(1,3)").scale(0.2).next_to(dot, UP+RIGHT)
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(0.3)

        pyx_pos = UP*1.0 + LEFT*1.5
        refl_yx = Dot(pyx_pos, color=GREEN)
        refl_yx_label = Text("P'(3,1)").scale(0.2).next_to(refl_yx, UP+RIGHT)
        refl_line = Line(p_pos, pyx_pos, color=GREEN, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(refl_line), FadeIn(refl_yx), Write(refl_yx_label))
        self.wait(0.4)

        pynx_pos = RIGHT*1.0 + DOWN*1.5
        refl_ynx = Dot(pynx_pos, color=PURPLE)
        refl_ynx_label = Text("P''(-3,-1)").scale(0.2).next_to(refl_ynx, DOWN+LEFT)
        refl_line2 = Line(p_pos, pynx_pos, color=PURPLE, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(refl_line2), FadeIn(refl_ynx), Write(refl_ynx_label))
        self.wait(0.4)

        info = Text("y=x: (x,y)->(y,x)  y=-x: (x,y)->(-y,-x)", color=WHITE).scale(0.25).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
