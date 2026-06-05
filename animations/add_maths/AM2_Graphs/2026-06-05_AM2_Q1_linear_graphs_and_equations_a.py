from manim import *
import math

class GradientVisual(Scene):
    def construct(self):
        title = Text("Gradient of a Line", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Draw axes
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*1)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*4)
        self.play(Create(x_axis), Create(y_axis))

        # Labels
        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Draw a line y = 2x
        line = Line(LEFT*3 + DOWN*0.5, RIGHT*3 + UP*2.5, color=BLUE)
        self.play(Create(line))

        # Points
        p1 = Dot(LEFT*2 + DOWN*0.17, color=RED, radius=0.08)
        p2 = Dot(RIGHT*1 + UP*1.33, color=RED, radius=0.08)
        p1_label = Text("(x1,y1)", font_size=18)
        p1_label.next_to(p1, DOWN+LEFT)
        p2_label = Text("(x2,y2)", font_size=18)
        p2_label.next_to(p2, UP+RIGHT)

        self.play(Create(p1), Create(p2), Write(p1_label), Write(p2_label))

        # Rise and run
        rise = Arrow(p1.get_center(), p2.get_center()+DOWN*1.5, color=GREEN, stroke_width=3)
        run = Arrow(p1.get_center(), p1.get_center()+RIGHT*3, color=ORANGE, stroke_width=3)

        self.play(Create(rise), Create(run))

        rise_txt = Text("Rise = y2-y1", font_size=22, color=GREEN)
        rise_txt.next_to(rise, RIGHT)
        run_txt = Text("Run = x2-x1", font_size=22, color=ORANGE)
        run_txt.next_to(run, DOWN)

        self.play(Write(rise_txt), Write(run_txt))

        formula = Text("m = Rise/Run = (y2-y1)/(x2-x1)", font_size=26, color=YELLOW)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        self.wait(2)
