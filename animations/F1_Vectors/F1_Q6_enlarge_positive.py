from manim import *
import math

class EnlargePositive(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        origin = Dot(ORIGIN, color=WHITE, radius=0.08)
        o_label = Text("O (centre)").scale(0.25).next_to(origin, DOWN+LEFT)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label), FadeIn(origin), Write(o_label))
        self.wait(0.2)

        tri_pts = [LEFT*0.5+DOWN*0.3, RIGHT*0.5+DOWN*0.3, LEFT*0.5+UP*0.8]
        tri = Polygon(*tri_pts, color=BLUE, fill_opacity=0.3)
        tri_label = Text("Object").scale(0.2).next_to(tri, DOWN+RIGHT)
        self.play(Create(tri), Write(tri_label))
        self.wait(0.4)

        k = 2.0
        tri_big_pts = [p * k for p in tri_pts]
        tri_big = Polygon(*tri_big_pts, color=GREEN, fill_opacity=0.3)
        big_label = Text("k=2").scale(0.2).next_to(tri_big, UP+RIGHT)
        self.play(Create(tri_big), Write(big_label))
        self.wait(0.4)

        lines = []
        for p in tri_pts:
            lines.append(Line(ORIGIN, p*k, color=YELLOW, stroke_width=1, stroke_opacity=0.4))
        self.play(*[Create(l) for l in lines])
        self.wait(0.4)

        info = Text("Enlargement k=2: all distances from centre double", color=WHITE).scale(0.3).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
