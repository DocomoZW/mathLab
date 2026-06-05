from manim import *
import math

class FindConstants(Scene):
    def construct(self):
        title = Text("Finding Constants from Linear Graph", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*3.5)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("X", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("Y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Draw a straight line
        line = Line(LEFT*2.5 + DOWN*1.2, RIGHT*2.5 + UP*1.5, color=GREEN)
        self.play(Create(line))

        # Mark intercept
        int_point = Dot(LEFT*3.5 + DOWN*0.5, color=RED, radius=0.08)
        int_label = Text("Intercept = c", font_size=22, color=RED)
        int_label.next_to(int_point, DOWN+LEFT)
        self.play(Create(int_point), Write(int_label))

        # Mark two points for gradient
        p1 = Dot(LEFT*1 + DOWN*0.22, color=ORANGE, radius=0.08)
        p2 = Dot(RIGHT*1 + UP*0.5, color=ORANGE, radius=0.08)

        self.play(Create(p1), Create(p2))

        pt1 = Text("(X1,Y1)", font_size=18, color=ORANGE)
        pt1.next_to(p1, DOWN)
        pt2 = Text("(X2,Y2)", font_size=18, color=ORANGE)
        pt2.next_to(p2, UP)

        self.play(Write(pt1), Write(pt2))

        # Gradient
        grad = Text("Gradient m = (Y2-Y1)/(X2-X1)", font_size=24, color=YELLOW)
        grad.shift(DOWN*2.5)
        self.play(Write(grad))

        const = Text("Then convert back: a = 10^c, n = m", font_size=24, color=BLUE)
        const.next_to(grad, DOWN, buff=0.3)
        self.play(Write(const))

        self.wait(2)
