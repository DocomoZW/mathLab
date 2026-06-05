from manim import *
import math
import numpy as np

class E1Q5SineRule(Scene):
    def construct(self):
        # General triangle
        vertices = [
            [-2, -1.2, 0],
            [2, -1.2, 0],
            [0, 1.5, 0]
        ]
        v_pts = [np.array(v) for v in vertices]
        triangle = Polygon(*v_pts, color=WHITE)
        self.play(Create(triangle))

        # Side labels
        v0, v1, v2 = v_pts
        side_a = Line(v1, v2, color=BLUE)
        side_b = Line(v0, v2, color=GREEN)
        side_c = Line(v0, v1, color=RED)

        a_label = Text("a", font_size=24, color=BLUE)
        a_label.next_to(side_a, RIGHT, buff=0.15)
        b_label = Text("b", font_size=24, color=GREEN)
        b_label.next_to(side_b, LEFT, buff=0.15)
        c_label = Text("c", font_size=24, color=RED)
        c_label.next_to(side_c, DOWN, buff=0.15)

        self.play(Write(a_label), Write(b_label), Write(c_label))

        # Angle labels
        angle_c = Text("C", font_size=22, color=BLUE)
        angle_c.next_to(v2, UP, buff=0.15)
        angle_a = Text("A", font_size=22, color=GREEN)
        angle_a.next_to(v0, DOWN + LEFT, buff=0.15)
        angle_b = Text("B", font_size=22, color=RED)
        angle_b.next_to(v1, DOWN + RIGHT, buff=0.15)

        self.play(Write(angle_c), Write(angle_a), Write(angle_b))

        self.wait(0.5)

        # Sine Rule formula
        formula = Text("a / sin A = b / sin B = c / sin C", font_size=22, color=YELLOW)
        formula.to_edge(DOWN)
        self.play(Write(formula))

        self.wait(0.5)

        # Explanation
        note = Text("The Sine Rule", font_size=24, color=YELLOW)
        note.to_edge(UP)
        self.play(Write(note))

        self.wait(2)
