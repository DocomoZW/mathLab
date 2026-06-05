from manim import *

class D1Q7VolumeSphere(Scene):
    def construct(self):
        title = Text("Volume of a Sphere", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        sphere = Circle(radius=2, color=BLUE, stroke_width=3)
        sphere.move_to(ORIGIN)
        self.play(Create(sphere))
        self.wait(0.3)

        # Fill
        fill = Circle(radius=2, color=BLUE, fill_opacity=0.4, stroke_width=0)
        fill.move_to(ORIGIN)
        self.play(FadeIn(fill, scale=0.5), run_time=0.8)
        self.wait(0.3)

        # Radius line
        radius_line = Line(sphere.get_center(), sphere.point_at_angle(PI / 4), color=YELLOW, stroke_width=3)
        r_label = Text("r = 6 cm", font_size=18, color=YELLOW).next_to(radius_line.get_midpoint(), UP, buff=0.15)

        self.play(Create(radius_line), Write(r_label))
        self.wait(0.3)

        # Central cross-section
        h_line = Line(sphere.get_left(), sphere.get_right(), color=GRAY, stroke_width=1)
        v_line = Line(sphere.get_top(), sphere.get_bottom(), color=GRAY, stroke_width=1)
        self.play(Create(h_line), Create(v_line))
        self.wait(0.3)

        formula = Text("V = (4/3) x pi x r3", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.3)

        result = Text("= (4/3) x pi x 216 = 904.90 cm3", font_size=20, color=YELLOW).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)
