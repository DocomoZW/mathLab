from manim import *

class D1Q4SaCuboid(Scene):
    def construct(self):
        title = Text("Surface Area of a Cuboid", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw cuboid net or 3D
        # Front face
        front = Rectangle(width=3, height=2, color=BLUE, stroke_width=3, fill_opacity=0.3)
        front.shift(LEFT * 0.5 + UP * 0.3)
        self.play(Create(front))
        self.wait(0.2)

        # Back face (shifted)
        back = Rectangle(width=3, height=2, color=BLUE_D, stroke_width=3, fill_opacity=0.2)
        back.shift(RIGHT * 1 + UP * 0.1)
        self.play(Create(back))
        self.wait(0.2)

        # Connecting lines
        lines = VGroup()
        for start, end in zip(front.get_vertices(), back.get_vertices()):
            lines.add(Line(start, end, color=GRAY, stroke_width=2))
        self.play(Create(lines))
        self.wait(0.3)

        # Labels
        l = Text("l = 5 cm", font_size=16, color=YELLOW).shift(DOWN * 2 + LEFT * 0.5)
        w = Text("w = 3 cm", font_size=16, color=GREEN).shift(DOWN * 2 + RIGHT * 1.5)
        h = Text("h = 4 cm", font_size=16, color=ORANGE).shift(UP * 1.8 + RIGHT * 0.5)

        self.play(Write(l), Write(w), Write(h))
        self.wait(0.3)

        formula = Text("SA = 2(lw + lh + wh)", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(formula))
        self.wait(0.3)

        result = Text("= 2(15 + 20 + 12) = 94 cm2", font_size=20, color=YELLOW).shift(DOWN * 0.5)
        self.play(Write(result))
        self.wait(1)
