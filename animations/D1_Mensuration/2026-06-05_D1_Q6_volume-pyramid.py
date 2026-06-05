from manim import *

class D1Q6VolumePyramid(Scene):
    def construct(self):
        title = Text("Volume of a Pyramid", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw pyramid with base and apex
        base = Polygon(
            [-1.5, -1, 0], [1.5, -1, 0], [1.5, -2, 0], [-1.5, -2, 0],
            color=BLUE, stroke_width=3, fill_opacity=0.2
        )
        apex = Dot([0, 1.5, 0], color=RED, radius=0.06)

        edges = VGroup()
        for v in base.get_vertices():
            edges.add(Line(apex.get_center(), v, color=BLUE, stroke_width=3))

        pyramid = VGroup(base, apex, edges)
        pyramid.move_to(ORIGIN)
        self.play(Create(pyramid))
        self.wait(0.3)

        # Height line (dashed)
        base_center = Dot([0, -1.5, 0], color=WHITE, radius=0.03)
        height_line = DashedLine(apex.get_center(), base_center.get_center(), color=YELLOW, stroke_width=2)
        h_label = Text("h = 12 cm", font_size=18, color=YELLOW).shift(RIGHT * 0.8 + UP * 0.5)

        self.play(Create(height_line), Write(h_label))
        self.wait(0.3)

        # Base dimensions
        base_dims = Text("Base: 8 cm x 5 cm", font_size=18, color=GREEN).shift(DOWN * 3)
        self.play(Write(base_dims))
        self.wait(0.3)

        formula = Text("V = (1/3) x l x w x h", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.3)

        result = Text("= (1/3) x 40 x 12 = 160 cm3", font_size=20, color=YELLOW).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)
