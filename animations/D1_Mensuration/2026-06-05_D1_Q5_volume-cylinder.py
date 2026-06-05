from manim import *

class D1Q5VolumeCylinder(Scene):
    def construct(self):
        title = Text("Volume of a Cylinder", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw cylinder
        top_ellipse = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        bottom_ellipse = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        bottom_ellipse.shift(DOWN * 2.5)
        left = Line(top_ellipse.get_left(), bottom_ellipse.get_left(), color=BLUE, stroke_width=3)
        right = Line(top_ellipse.get_right(), bottom_ellipse.get_right(), color=BLUE, stroke_width=3)

        cyl = VGroup(top_ellipse, bottom_ellipse, left, right)
        cyl.move_to(ORIGIN)
        self.play(Create(cyl))
        self.wait(0.3)

        # Fill
        fill_top = Ellipse(width=3, height=1, color=BLUE, fill_opacity=0.4, stroke_width=0)
        fill_bottom = Ellipse(width=3, height=1, color=BLUE, fill_opacity=0.4, stroke_width=0)
        fill_bottom.shift(DOWN * 2.5)
        fill = Rectangle(width=3, height=2.5, color=BLUE, fill_opacity=0.15, stroke_width=0)
        fill.shift(DOWN * 1.25)
        fill_cyl = VGroup(fill, fill_top, fill_bottom)
        fill_cyl.move_to(ORIGIN)
        self.play(FadeIn(fill_cyl))
        self.wait(0.3)

        # Labels
        r_label = Text("r = 4 cm", font_size=18, color=YELLOW).shift(DOWN * 0.5 + RIGHT * 0.5)
        h_label = Text("h = 10 cm", font_size=18, color=GREEN).shift(RIGHT * 2.2)
        self.play(Write(r_label), Write(h_label))
        self.wait(0.3)

        formula = Text("V = pi x r2 x h", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.3)

        result = Text("= pi x 16 x 10 = 502.72 cm3", font_size=20, color=YELLOW).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)
