from manim import *
import math

class IntersectionVisual(Scene):
    def construct(self):
        title = Text("Intersection of Graphs", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*1)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*4)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Draw parabola y = x^2
        points = []
        for x in range(-30, 31):
            fx = x/10
            fy = fx*fx
            points.append([fx*2.5, fy*1.5 - 1, 0])

        parabola = VMobject(stroke_color=BLUE, stroke_width=3)
        parabola.set_points_smoothly(points)
        self.play(Create(parabola), run_time=1)

        # Draw line y = 2x + 1
        line = Line(LEFT*3 + DOWN*0.5, RIGHT*3 + UP*2.5, color=GREEN)
        self.play(Create(line))

        # Label
        pl = Text("y = x^2", font_size=20, color=BLUE)
        pl.next_to(parabola, RIGHT, buff=0.2)
        ll = Text("y = 2x+1", font_size=20, color=GREEN)
        ll.next_to(line, RIGHT, buff=0.2)
        self.play(Write(pl), Write(ll))

        # Mark intersection points
        inter1 = Dot(LEFT*1 + DOWN*0.33, color=RED, radius=0.1)
        inter2 = Dot(RIGHT*1.5 + UP*0.5, color=RED, radius=0.1)

        self.play(Create(inter1), Create(inter2))

        inter_label = Text("Intersection points", font_size=24, color=RED)
        inter_label.to_edge(DOWN)
        self.play(Write(inter_label))

        method = Text("Solve f(x) = g(x) to find coordinates", font_size=22, color=YELLOW)
        method.next_to(inter_label, UP)
        self.play(Write(method))

        self.wait(2)
