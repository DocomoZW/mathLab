from manim import *

class D1Q4SaCylinder(Scene):
    def construct(self):
        title = Text("Surface Area of a Cylinder", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw cylinder
        top = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        bottom = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        bottom.shift(DOWN * 2.5)

        left_line = Line(top.get_left(), bottom.get_left(), color=BLUE, stroke_width=3)
        right_line = Line(top.get_right(), bottom.get_right(), color=BLUE, stroke_width=3)

        cylinder = VGroup(top, bottom, left_line, right_line)
        cylinder.move_to(ORIGIN)
        self.play(Create(cylinder))
        self.wait(0.3)

        # Labels
        r_label = Text("r = 3 cm", font_size=18, color=YELLOW).shift(DOWN * 0.8 + RIGHT * 0.5)
        h_label = Text("h = 10 cm", font_size=18, color=GREEN).shift(RIGHT * 2.2)
        self.play(Write(r_label), Write(h_label))
        self.wait(0.3)

        # Formula breakdown
        f1 = Text("2 circles: 2 x pi x r2", font_size=18, color=WHITE).shift(DOWN * 1.5)
        f2 = Text("Curved: 2 x pi x r x h", font_size=18, color=ORANGE).shift(DOWN * 2.2)
        self.play(Write(f1))
        self.wait(0.2)
        self.play(Write(f2))
        self.wait(0.3)

        result = Text("= 2 x pi x 9 + 2 x pi x 30 = 245.08 cm2", font_size=18, color=YELLOW).to_edge(DOWN)
        self.play(Write(result))
        self.wait(1)
