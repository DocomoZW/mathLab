from manim import *

class D1Q6VolumeCone(Scene):
    def construct(self):
        title = Text("Volume of a Cone", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw cone
        base = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        apex = Dot([0, 2, 0], color=RED, radius=0.06)

        left_line = Line(apex.get_center(), base.get_left(), color=BLUE, stroke_width=3)
        right_line = Line(apex.get_center(), base.get_right(), color=BLUE, stroke_width=3)
        bottom_arc = ArcBetweenPoints(base.get_left(), base.get_right(), angle=-PI, color=BLUE, stroke_width=3)

        cone = VGroup(base, apex, left_line, right_line, bottom_arc)
        cone.move_to(ORIGIN)
        self.play(Create(cone))
        self.wait(0.3)

        # Fill
        fill_cone = Polygon(
            base.get_left(), base.get_right(), apex.get_center(),
            color=BLUE, fill_opacity=0.15, stroke_width=0
        )
        self.play(FadeIn(fill_cone))
        self.wait(0.3)

        # Height
        base_center = Dot(base.get_center(), color=WHITE, radius=0.03)
        height_line = DashedLine(apex.get_center(), base_center.get_center(), color=YELLOW, stroke_width=2)
        h_label = Text("h = 14 cm", font_size=18, color=YELLOW).shift(RIGHT * 0.8 + UP * 1.2)
        r_label = Text("r = 6 cm", font_size=18, color=GREEN).shift(DOWN * 1.2 + RIGHT * 0.8)

        self.play(Create(height_line), Write(h_label), Write(r_label))
        self.wait(0.3)

        formula = Text("V = (1/3) x pi x r2 x h", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.3)

        result = Text("= (1/3) x pi x 36 x 14 = 527.86 cm3", font_size=18, color=YELLOW).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)
