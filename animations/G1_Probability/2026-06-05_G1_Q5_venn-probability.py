from manim import *
import math

class G1Q5VennProbability(Scene):
    def construct(self):
        title = Text("Venn Diagram - Probability", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Rectangle for universal set
        rect = Rectangle(width=5, height=3.0, color=WHITE)
        rect.shift(DOWN * 0.3)
        label_u = Text("U = 50", font_size=18, color=WHITE)
        label_u.next_to(rect, UP * 0.2)
        self.play(Create(rect), Write(label_u))

        # Circle A (left)
        circle_a = Circle(radius=1.2, color=BLUE)
        circle_a.shift(LEFT * 0.8 + DOWN * 0.3)
        label_a = Text("A = 20", font_size=18, color=BLUE)
        label_a.next_to(circle_a, UP * 0.8 + LEFT * 0.5)
        self.play(Create(circle_a), Write(label_a))

        # Circle B (right)
        circle_b = Circle(radius=1.2, color=GREEN)
        circle_b.shift(RIGHT * 0.8 + DOWN * 0.3)
        label_b = Text("B = 15", font_size=18, color=GREEN)
        label_b.next_to(circle_b, UP * 0.8 + RIGHT * 0.5)
        self.play(Create(circle_b), Write(label_b))

        # Region values: A only = 8, B only = 3, overlap = 12, outside = 27
        a_only = Text("8", font_size=20, color=BLUE)
        a_only.shift(LEFT * 1.2 + DOWN * 0.3)

        b_only = Text("3", font_size=20, color=GREEN)
        b_only.shift(RIGHT * 1.2 + DOWN * 0.3)

        overlap = Text("12", font_size=20, color=YELLOW)
        overlap.shift(DOWN * 0.3)

        outside = Text("27", font_size=18, color=WHITE)
        outside.shift(RIGHT * 2.2 + UP * 1.3)

        self.play(Write(a_only), Write(b_only), Write(overlap), Write(outside))

        # Probability calculation
        prob = Text("P(A) = 20/50 = 2/5", font_size=20, color=YELLOW)
        prob.shift(DOWN * 2.2)
        self.play(Write(prob))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(rect), FadeOut(label_u),
                  FadeOut(circle_a), FadeOut(label_a),
                  FadeOut(circle_b), FadeOut(label_b),
                  FadeOut(a_only), FadeOut(b_only), FadeOut(overlap), FadeOut(outside), FadeOut(prob))
