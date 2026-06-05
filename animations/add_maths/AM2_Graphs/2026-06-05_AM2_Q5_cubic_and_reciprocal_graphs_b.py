from manim import *
import math

class ReciprocalShape(Scene):
    def construct(self):
        title = Text("Reciprocal Graph: y = 1/x", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes (offset for visibility)
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*4)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Plot y = 1/x (positive branch)
        pts1 = []
        for x in range(5, 40):
            fx = x/10
            fy = 1.0/fx
            pts1.append([fx*1.5, fy*1.5 - 0.5, 0])
        branch1 = VMobject(stroke_color=BLUE, stroke_width=3)
        branch1.set_points_smoothly(pts1)
        self.play(Create(branch1), run_time=1)

        # Plot y = 1/x (negative branch)
        pts2 = []
        for x in range(-39, -4):
            fx = x/10
            fy = 1.0/fx
            pts2.append([fx*1.5, fy*1.5 - 0.5, 0])
        branch2 = VMobject(stroke_color=BLUE, stroke_width=3)
        branch2.set_points_smoothly(pts2)
        self.play(Create(branch2), run_time=1)

        # Dashed asymptotes
        asymp_v = DashedLine(UP*2, DOWN*2, color=RED, stroke_width=2)
        asymp_v.shift(LEFT*4 + DOWN*0.5)
        asymp_h = DashedLine(LEFT*4, RIGHT*4, color=RED, stroke_width=2)
        asymp_h.shift(DOWN*0.5)

        self.play(Create(asymp_v), Create(asymp_h))

        vl = Text("x = 0 (vertical asymptote)", font_size=18, color=RED)
        vl.next_to(asymp_v, UP, buff=0.1)
        hl = Text("y = 0 (horizontal asymptote)", font_size=18, color=RED)
        hl.next_to(asymp_h, LEFT, buff=0.1)

        self.play(Write(vl), Write(hl))

        info = Text("Hyperbola with two branches", font_size=24, color=YELLOW)
        info.to_edge(DOWN)
        self.play(Write(info))

        self.wait(2)
