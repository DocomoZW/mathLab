from manim import *
import math

class EnlargeThenTranslate(Scene):
    def construct(self):
        # Manual axes (no Axes to avoid LaTeX dependency)
        horiz = Line(LEFT * 4, RIGHT * 4.5, color=GRAY)
        vert = Line(DOWN * 3.5, UP * 4, color=GRAY)
        x_lab = Text("x").scale(0.3).next_to(horiz, DOWN+RIGHT)
        y_lab = Text("y").scale(0.3).next_to(vert, UP+LEFT)
        origin = Text("O").scale(0.25).next_to(Dot(ORIGIN, radius=0.05), DOWN+LEFT)
        self.play(Create(horiz), Create(vert), Write(x_lab), Write(y_lab), Write(origin))
        self.wait(0.2)

        # Original triangle
        tri = Polygon([1, 1, 0], [3, 1, 0], [1, 3, 0], color=BLUE, fill_opacity=0.3)
        tri_label = Text("A").scale(0.25).next_to(tri, DOWN+RIGHT)
        self.play(Create(tri), Write(tri_label))
        self.wait(0.3)

        # Enlarged by factor 2 about origin
        tri_enl = Polygon([2, 2, 0], [6, 2, 0], [2, 6, 0], color=GREEN, fill_opacity=0.3)
        enl_label = Text("B: k=2").scale(0.2).next_to(tri_enl, UP+RIGHT)
        self.play(Create(tri_enl), Write(enl_label))
        self.wait(0.3)

        # Translated by [3,2]
        tri_final = Polygon([5, 4, 0], [9, 4, 0], [5, 8, 0], color=RED, fill_opacity=0.3)
        final_label = Text("C: +[3,2]").scale(0.2).next_to(tri_final, UP+RIGHT)
        self.play(Create(tri_final), Write(final_label))
        self.wait(0.4)

        arrow_enl = Arrow(tri.get_center(), tri_enl.get_center(), color=GREEN, stroke_width=2)
        arrow_tr = Arrow(tri_enl.get_center(), tri_final.get_center(), color=RED, stroke_width=2)
        self.play(Create(arrow_enl), Create(arrow_tr))
        self.wait(0.4)

        info = Text("Enlarge about O by 2, then translate by [3,2]").scale(0.25).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
