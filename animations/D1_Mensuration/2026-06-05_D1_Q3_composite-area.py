from manim import *

class D1Q3CompositeArea(Scene):
    def construct(self):
        title = Text("Area of Composite Shape", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw L-shape
        points = [
            [-2, 1, 0], [2, 1, 0], [2, -1, 0],
            [0.5, -1, 0], [0.5, -2.5, 0], [-2, -2.5, 0]
        ]
        l_shape = Polygon(*points, color=BLUE, stroke_width=3, fill_opacity=0.2)
        l_shape.move_to(ORIGIN)
        self.play(Create(l_shape))
        self.wait(0.3)

        # Split into two rectangles
        rect1 = Polygon([-2, 1, 0], [2, 1, 0], [2, -1, 0], [-2, -1, 0],
                        color=GREEN, stroke_width=2, fill_opacity=0.3)
        rect2 = Polygon([-2, -1, 0], [0.5, -1, 0], [0.5, -2.5, 0], [-2, -2.5, 0],
                        color=ORANGE, stroke_width=2, fill_opacity=0.3)
        rect1.move_to(l_shape.get_center())
        rect2.move_to(l_shape.get_center())

        self.play(Transform(l_shape, rect1))
        self.wait(0.3)
        self.play(FadeIn(rect2))
        self.wait(0.3)

        label1 = Text("A = 5 x 8 = 40 m2", font_size=18, color=GREEN).shift(UP * 1.2)
        label2 = Text("B = 3 x 4 = 12 m2", font_size=18, color=ORANGE).shift(DOWN * 1.8)
        self.play(Write(label1), Write(label2))
        self.wait(0.3)

        total = Text("Total = 40 + 12 = 52 m2", font_size=22, color=YELLOW).to_edge(DOWN)
        self.play(Write(total))
        self.wait(1)
