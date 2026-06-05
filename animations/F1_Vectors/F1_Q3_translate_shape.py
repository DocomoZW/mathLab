from manim import *
import math

class TranslateShape(Scene):
    def construct(self):
        x_axis = Line(LEFT*4, RIGHT*4, color=GRAY)
        y_axis = Line(DOWN*3, UP*3, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.2)

        tri_pts = [LEFT*1.5+DOWN*0.5, RIGHT*0.5+DOWN*0.5, LEFT*1.5+UP*1.0]
        triangle = Polygon(*tri_pts, color=BLUE, fill_opacity=0.3)
        tri_label = Text("Object").scale(0.3).next_to(triangle, DOWN+RIGHT)
        self.play(Create(triangle), Write(tri_label))
        self.wait(0.5)

        vec = Arrow(ORIGIN, RIGHT*2.5+UP*1.0, color=YELLOW, stroke_width=4)
        vec_label = Text("T=[5,2]").scale(0.3).next_to(vec.get_end(), UP)
        self.play(GrowArrow(vec), Write(vec_label))
        self.wait(0.3)

        shift_v = RIGHT*2.5+UP*1.0
        tri_img_pts = [p + shift_v for p in tri_pts]
        tri_image = Polygon(*tri_img_pts, color=GREEN, fill_opacity=0.3)
        image_label = Text("Image").scale(0.3).next_to(tri_image, UP+RIGHT)
        self.play(Create(tri_image), Write(image_label))
        self.wait(0.5)

        info = Text("Translation slides shape without rotation or resizing", color=WHITE).scale(0.3).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
