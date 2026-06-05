from manim import *

class D1Q5VolumeCuboid(Scene):
    def construct(self):
        title = Text("Volume of a Cuboid", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw 3D box
        face = Rectangle(width=3, height=2, color=BLUE, stroke_width=3, fill_opacity=0.3)
        face.shift(LEFT * 0.5 + UP * 0.3)

        back = Rectangle(width=3, height=2, color=BLUE_D, stroke_width=3, fill_opacity=0.2)
        back.shift(RIGHT * 1.2 + UP * 0)

        edges = VGroup()
        for s, e in zip(face.get_vertices(), back.get_vertices()):
            edges.add(Line(s, e, color=GRAY, stroke_width=2))

        cuboid = VGroup(face, back, edges)
        cuboid.move_to(ORIGIN)
        self.play(Create(cuboid))
        self.wait(0.3)

        # Dimension labels
        l = Text("l = 6 cm", font_size=16, color=YELLOW).shift(DOWN * 2 + LEFT * 0.3)
        w = Text("w = 5 cm", font_size=16, color=GREEN).shift(DOWN * 2 + RIGHT * 1.5)
        h = Text("h = 4 cm", font_size=16, color=ORANGE).shift(UP * 1.8 + RIGHT * 0.5)
        self.play(Write(l), Write(w), Write(h))
        self.wait(0.3)

        formula = Text("V = l x w x h", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.3)

        result = Text("= 6 x 5 x 4 = 120 cm3", font_size=20, color=YELLOW).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)
