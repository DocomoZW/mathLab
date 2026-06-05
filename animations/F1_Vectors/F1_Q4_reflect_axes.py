from manim import *
import math

class ReflectAxes(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.2)

        x_axis_hl = Line(LEFT*3.5, RIGHT*3.5, color=YELLOW, stroke_width=3)
        y_axis_hl = Line(DOWN*3.5, UP*3.5, color=YELLOW, stroke_width=3)
        self.play(Create(x_axis_hl), Create(y_axis_hl))
        self.wait(0.2)

        p_pos = RIGHT*1.0 + UP*1.5
        dot = Dot(p_pos, color=BLUE)
        dot_label = Text("P(2,3)").scale(0.25).next_to(dot, UP+RIGHT)
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(0.3)

        px_pos = RIGHT*1.0 + DOWN*1.5
        refl_x = Dot(px_pos, color=GREEN)
        refl_x_label = Text("Px(2,-3)").scale(0.2).next_to(refl_x, DOWN+RIGHT)
        refl_x_line = Line(p_pos, px_pos, color=GREEN, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(refl_x_line), FadeIn(refl_x), Write(refl_x_label))
        self.wait(0.4)

        py_pos = LEFT*1.0 + UP*1.5
        refl_y = Dot(py_pos, color=RED)
        refl_y_label = Text("Py(-2,3)").scale(0.2).next_to(refl_y, UP+LEFT)
        refl_y_line = Line(p_pos, py_pos, color=RED, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(refl_y_line), FadeIn(refl_y), Write(refl_y_label))
        self.wait(0.4)

        info = Text("Reflect x-axis: (x,y)->(x,-y)  y-axis: (x,y)->(-x,y)", color=WHITE).scale(0.25).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
