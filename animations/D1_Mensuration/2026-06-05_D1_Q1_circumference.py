from manim import *

class D1Q1Circumference(Scene):
    def construct(self):
        title = Text("Circumference of a Circle", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        circle = Circle(radius=1.8, color=BLUE, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.3)

        # Radius line
        center = Dot(circle.get_center(), color=WHITE, radius=0.05)
        radius_point = circle.point_at_angle(0)
        radius_line = Line(circle.get_center(), radius_point, color=YELLOW, stroke_width=3)
        r_label = Text("r", font_size=20, color=YELLOW).next_to(radius_line.get_midpoint(), DOWN, buff=0.15)
        self.play(FadeIn(center), Create(radius_line), Write(r_label))
        self.wait(0.3)

        # Formula
        f1 = Text("C = 2 x pi x r", font_size=22, color=WHITE).shift(DOWN * 1.5)
        self.play(Write(f1))
        self.wait(0.3)

        # Animate arrow around circumference
        arc = Arc(radius=1.8, angle=TAU, color=RED, stroke_width=6)
        self.play(Create(arc), run_time=1.5)
        self.wait(0.3)

        f2 = Text("C = 2 x pi x 7 = 44 cm", font_size=22, color=YELLOW).shift(DOWN * 2.5)
        self.play(Write(f2))
        self.wait(1)
