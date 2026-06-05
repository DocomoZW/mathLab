from manim import *
import math

class EnlargeFractionalNegative(Scene):
    def construct(self):
        x_axis = Line(LEFT*4, RIGHT*4, color=GRAY)
        y_axis = Line(DOWN*4, UP*4, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        origin = Dot(ORIGIN, color=WHITE, radius=0.08)
        o_label = Text("O").scale(0.3).next_to(origin, DOWN+LEFT)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label), FadeIn(origin), Write(o_label))
        self.wait(0.2)

        tri_pts = [RIGHT*0.8+UP*0.5, RIGHT*2.0+UP*0.5, RIGHT*0.8+UP*1.5]
        tri = Polygon(*tri_pts, color=BLUE, fill_opacity=0.3)
        tri_label = Text("Object").scale(0.2).next_to(tri, DOWN+RIGHT)
        self.play(Create(tri), Write(tri_label))
        self.wait(0.4)

        k_small = 0.5
        tri_small_pts = [p * k_small for p in tri_pts]
        tri_small = Polygon(*tri_small_pts, color=GREEN, fill_opacity=0.4)
        small_label = Text("k=0.5").scale(0.2).next_to(tri_small, DOWN+LEFT)
        self.play(Create(tri_small), Write(small_label))
        self.wait(0.4)

        k_neg = -1.0
        tri_neg_pts = [p * k_neg for p in tri_pts]
        tri_neg = Polygon(*tri_neg_pts, color=RED, fill_opacity=0.3)
        neg_label = Text("k=-1").scale(0.2).next_to(tri_neg, DOWN+LEFT)
        self.play(Create(tri_neg), Write(neg_label))
        self.wait(0.4)

        info = Text("Fractional k reduces, negative k flips 180 deg", color=WHITE).scale(0.3).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
