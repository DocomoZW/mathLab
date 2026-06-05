from manim import *
import math

class FeasibleRegion(Scene):
    def construct(self):
        title = Text("Feasible Region (Linear Programming)", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*0.5, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*2)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*0.5)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # x >= 0 (shade right of y-axis)
        # y >= 0 (shade above x-axis)

        # Line: x + y <= 5
        line1 = Line(LEFT*0.5 + UP*2, RIGHT*4 + DOWN*2, color=GREEN)
        self.play(Create(line1))
        l1_label = Text("x + y = 5", font_size=20, color=GREEN)
        l1_label.next_to(line1, RIGHT, buff=0.1)
        self.play(Write(l1_label))

        # Line: x <= 3
        line2 = Line(RIGHT*2.5 + UP*2, RIGHT*2.5 + DOWN*2, color=ORANGE)
        self.play(Create(line2))
        l2_label = Text("x = 3", font_size=20, color=ORANGE)
        l2_label.next_to(line2, UP)
        self.play(Write(l2_label))

        # Shade feasible region
        feas = Polygon(
            LEFT*0.5 + DOWN*2,    # (0,0)
            RIGHT*2.5 + DOWN*2,   # (3,0)
            RIGHT*2.5 + UP*0.5,   # (3,2)
            LEFT*0.5 + UP*2,      # (0,5)
            color=YELLOW, fill_opacity=0.3, stroke_opacity=0
        )
        self.play(Create(feas))

        # Mark vertices
        verts = [
            (LEFT*0.5 + DOWN*2, "(0,0)"),
            (RIGHT*2.5 + DOWN*2, "(3,0)"),
            (RIGHT*2.5 + UP*0.5, "(3,2)"),
            (LEFT*0.5 + UP*2, "(0,5)")
        ]
        for pos, label in verts:
            d = Dot(pos, color=RED, radius=0.08)
            l = Text(label, font_size=18)
            l.next_to(d, DOWN+LEFT)
            self.play(Create(d), Write(l))

        note = Text("Optimum occurs at a vertex", font_size=24, color=YELLOW)
        note.next_to(feas, DOWN, buff=0.3)
        self.play(Write(note))

        self.wait(2)
