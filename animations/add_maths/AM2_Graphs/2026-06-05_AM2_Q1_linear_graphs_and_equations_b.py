from manim import *
import math

class ParallelPerp(Scene):
    def construct(self):
        title = Text("Parallel and Perpendicular Lines", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Parallel lines
        p_title = Text("Parallel: Same gradient", font_size=28, color=BLUE)
        p_title.shift(UP*1.5)
        self.play(Write(p_title))

        # Axes
        x_axis = Line(LEFT*3, RIGHT*3, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*1.5, UP*1.5, color=WHITE)
        y_axis.shift(LEFT*3)
        self.play(Create(x_axis), Create(y_axis))

        line1 = Line(LEFT*2 + DOWN*0.3, RIGHT*2 + UP*1.7, color=GREEN)
        line2 = Line(LEFT*1 + DOWN*1.7, RIGHT*3 + UP*0.3, color=GREEN)
        self.play(Create(line1), Create(line2))

        l1 = Text("y = 2x+1", font_size=22, color=GREEN)
        l1.next_to(line1, UP, buff=0.1)
        l2 = Text("y = 2x-3", font_size=22, color=GREEN)
        l2.next_to(line2, DOWN, buff=0.1)
        self.play(Write(l1), Write(l2))

        self.wait(0.5)

        # Perpendicular lines
        perp_title = Text("Perpendicular: m1*m2 = -1", font_size=28, color=ORANGE)
        perp_title.shift(DOWN*2.5)
        self.play(Write(perp_title))

        perp_line1 = Line(LEFT*3 + UP*0.5, RIGHT*3 + DOWN*0.5, color=RED)
        perp_line2 = Line(LEFT*2 + DOWN*1.5, RIGHT*2 + UP*2.5, color=RED)
        perp_line1.shift(DOWN*3.5)
        perp_line2.shift(DOWN*3.5)

        x_axis2 = Line(LEFT*3, RIGHT*3, color=WHITE)
        x_axis2.shift(DOWN*4)
        y_axis2 = Line(DOWN*5.5, UP*3, color=WHITE)
        y_axis2.shift(LEFT*3)

        self.play(Create(x_axis2), Create(y_axis2))
        self.play(Create(perp_line1), Create(perp_line2))

        pl1 = Text("y = (1/2)x", font_size=22, color=RED)
        pl1.next_to(perp_line1, DOWN, buff=0.1)
        pl2 = Text("y = -2x", font_size=22, color=RED)
        pl2.next_to(perp_line2, UP, buff=0.1)
        self.play(Write(pl1), Write(pl2))

        note = Text("m1 * m2 = (1/2) * (-2) = -1", font_size=24, color=YELLOW)
        note.next_to(perp_title, DOWN)
        self.play(Write(note))

        self.wait(2)
