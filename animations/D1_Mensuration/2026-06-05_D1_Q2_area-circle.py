from manim import *

class D1Q2AreaCircle(Scene):
    def construct(self):
        title = Text("Area of a Circle", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        circle = Circle(radius=2, color=BLUE, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.3)

        # Show radius
        radius_line = Line(circle.get_center(), circle.point_at_angle(PI / 4), color=YELLOW, stroke_width=3)
        r_label = Text("r", font_size=20, color=YELLOW).next_to(radius_line.get_midpoint(), UP, buff=0.15)
        self.play(Create(radius_line), Write(r_label))
        self.wait(0.3)

        # Formula
        f1 = Text("A = pi x r x r", font_size=22, color=WHITE).shift(DOWN * 1.5)
        self.play(Write(f1))
        self.wait(0.3)

        # Animate area filling
        fill_circle = Circle(radius=2, color=BLUE, fill_opacity=0.4, stroke_width=0)
        fill_circle.move_to(ORIGIN)
        self.play(FadeIn(fill_circle, scale=0.5), run_time=1.0)
        self.wait(0.3)

        f2 = Text("A = pi x 7 x 7 = 154 cm2", font_size=22, color=YELLOW).shift(DOWN * 2.5)
        self.play(Write(f2))
        self.wait(1)
