from manim import *
import math

class ReflectionsToRotation(Scene):
    def construct(self):
        # Manual axes
        horiz = Line(LEFT * 3.5, RIGHT * 3.5, color=GRAY)
        vert = Line(DOWN * 3.5, UP * 3.5, color=GRAY)
        x_lab = Text("x").scale(0.3).next_to(horiz, DOWN+RIGHT)
        y_lab = Text("y").scale(0.3).next_to(vert, UP+LEFT)
        origin = Text("O").scale(0.25).next_to(Dot(ORIGIN, radius=0.05), DOWN+LEFT)
        self.play(Create(horiz), Create(vert), Write(x_lab), Write(y_lab), Write(origin))
        self.wait(0.2)

        line_yx = Line(LEFT * 3 + DOWN * 3, RIGHT * 3 + UP * 3, color=YELLOW, stroke_width=2)
        line_ynegx = Line(LEFT * 3 + UP * 3, RIGHT * 3 + DOWN * 3, color=ORANGE, stroke_width=2)
        label_yx = Text("m1: y=x").scale(0.25).next_to(RIGHT * 3 + UP * 3, UP+RIGHT)
        label_ynegx = Text("m2: y=-x").scale(0.25).next_to(RIGHT * 3 + DOWN * 3, DOWN+RIGHT)
        self.play(Create(line_yx), Write(label_yx), Create(line_ynegx), Write(label_ynegx))
        self.wait(0.3)

        dot = Dot(RIGHT * 2 + UP * 1, color=BLUE)
        dot_label = Text("P").scale(0.3).next_to(dot, UP+RIGHT)
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(0.3)

        p1 = Dot(RIGHT * 1 + UP * 2, color=GREEN)
        p1_label = Text("P1 (in y=x)").scale(0.2).next_to(p1, UP+LEFT)
        line1 = Line(RIGHT * 2 + UP * 1, RIGHT * 1 + UP * 2, color=GREEN, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(line1), FadeIn(p1), Write(p1_label))
        self.wait(0.3)

        p2 = Dot(LEFT * 2 + DOWN * 1, color=RED)
        p2_label = Text("P2 (then y=-x)").scale(0.2).next_to(p2, DOWN+LEFT)
        line2 = Line(RIGHT * 1 + UP * 2, LEFT * 2 + DOWN * 1, color=RED, stroke_width=1, stroke_opacity=0.5)
        self.play(Create(line2), FadeIn(p2), Write(p2_label))
        self.wait(0.3)

        arc = ArcBetweenPoints(RIGHT * 2 + UP * 1, LEFT * 2 + DOWN * 1, color=PURPLE, stroke_width=2)
        label_rot = Text("= 180 deg rotation").scale(0.25).next_to(LEFT * 2 + DOWN * 1, DOWN+RIGHT)
        self.play(Create(arc), Write(label_rot))
        self.wait(0.5)

        info = Text("Two reflections in intersecting lines = rotation about intersection").scale(0.25).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
