from manim import *
import math

class H1Q7ScatterPlot(Scene):
    def construct(self):
        title = Text("Scatter Diagrams - Correlation").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Show three types of correlation side by side

        # Positive correlation
        pos_group = VGroup()
        pos_title = Text("Positive", font_size=18, color=GREEN)
        pos_title.shift(LEFT * 4 + UP * 1.5)
        pos_group.add(pos_title)

        # Axes for positive
        pos_x = Line(LEFT * 0.5, RIGHT * 2.5, color=WHITE)
        pos_x.shift(LEFT * 5.5 + DOWN * 0.5)
        pos_y = Line(DOWN * 0.5, UP * 2.0, color=WHITE)
        pos_y.shift(LEFT * 5.5 + DOWN * 0.5)
        pos_group.add(pos_x, pos_y)

        # Positive correlation points
        pos_points = [(0.2, 0.3), (0.5, 0.6), (0.8, 0.5), (1.0, 1.0),
                      (1.3, 1.2), (1.6, 1.5), (1.9, 1.8), (2.2, 1.7)]
        for px, py in pos_points:
            dot = Dot(color=GREEN, radius=0.06)
            dot.move_to(LEFT * 5.5 + RIGHT * px + DOWN * 0.5 + UP * py * 0.8)
            pos_group.add(dot)

        self.play(Create(pos_group))
        self.wait(0.2)

        # Negative correlation
        neg_group = VGroup()
        neg_title = Text("Negative", font_size=18, color=RED)
        neg_title.shift(UP * 1.5)
        neg_group.add(neg_title)

        neg_x = Line(LEFT * 0.5, RIGHT * 2.5, color=WHITE)
        neg_x.shift(LEFT * 1.5 + DOWN * 0.5)
        neg_y = Line(DOWN * 0.5, UP * 2.0, color=WHITE)
        neg_y.shift(LEFT * 1.5 + DOWN * 0.5)
        neg_group.add(neg_x, neg_y)

        neg_points = [(0.2, 1.8), (0.5, 1.5), (0.8, 1.3), (1.0, 1.0),
                      (1.3, 0.8), (1.6, 0.6), (1.9, 0.3), (2.2, 0.2)]
        for px, py in neg_points:
            dot = Dot(color=RED, radius=0.06)
            dot.move_to(LEFT * 1.5 + RIGHT * px + DOWN * 0.5 + UP * py * 0.8)
            neg_group.add(dot)

        self.play(Create(neg_group))
        self.wait(0.2)

        # No correlation
        none_group = VGroup()
        none_title = Text("No Correlation", font_size=18, color=GRAY)
        none_title.shift(RIGHT * 2.5 + UP * 1.5)
        none_group.add(none_title)

        none_x = Line(LEFT * 0.5, RIGHT * 2.5, color=WHITE)
        none_x.shift(RIGHT * 2.5 + DOWN * 0.5)
        none_y = Line(DOWN * 0.5, UP * 2.0, color=WHITE)
        none_y.shift(RIGHT * 2.5 + DOWN * 0.5)
        none_group.add(none_x, none_y)

        # Random scattered points
        import random
        random.seed(42)
        none_pts = [(0.3, 1.5), (0.6, 0.3), (0.9, 1.8), (1.2, 0.8),
                    (1.5, 0.2), (1.8, 1.0), (2.0, 1.6), (2.3, 0.5)]
        for px, py in none_pts:
            dot = Dot(color=GRAY, radius=0.06)
            dot.move_to(RIGHT * 2.5 + RIGHT * px + DOWN * 0.5 + UP * py * 0.8)
            none_group.add(dot)

        self.play(Create(none_group))
        self.wait(0.5)

        # Explanation
        note = Text("Positive: as x increases, y increases | Negative: as x increases, y decreases", font_size=14, color=GRAY)
        note.to_edge(DOWN)
        note.shift(UP * 0.2)
        self.play(Write(note))
        self.wait(2)
