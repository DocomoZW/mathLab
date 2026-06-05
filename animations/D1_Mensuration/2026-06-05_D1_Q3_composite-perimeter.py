from manim import *

class D1Q3CompositePerimeter(Scene):
    def construct(self):
        title = Text("Perimeter of Composite Shape", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw L-shape
        points = [
            [-2.5, 1.5, 0], [2, 1.5, 0], [2, -0.5, 0],
            [0.5, -0.5, 0], [0.5, -2.5, 0], [-2.5, -2.5, 0]
        ]
        l_shape = Polygon(*points, color=BLUE, stroke_width=3, fill_opacity=0.15)
        l_shape.move_to(ORIGIN)
        self.play(Create(l_shape))
        self.wait(0.3)

        # Trace perimeter in red
        perimeter = Polygon(*points, color=RED, stroke_width=5)
        perimeter.move_to(ORIGIN)
        self.play(Create(perimeter), run_time=1.5)
        self.wait(0.3)

        # Show exterior sides with lengths
        sides_text = Text("Trace only the outer boundary", font_size=20, color=RED).shift(DOWN * 1.5)
        self.play(Write(sides_text))
        self.wait(0.3)

        note = Text("Do NOT count interior edges", font_size=20, color=YELLOW).shift(DOWN * 2.5)
        self.play(Write(note))
        self.wait(0.5)

        result = Text("P = 10 + 6 + 4 + 3 + 6 + 3 = 32 m", font_size=22, color=WHITE).to_edge(DOWN)
        self.play(Write(result))
        self.wait(1)
