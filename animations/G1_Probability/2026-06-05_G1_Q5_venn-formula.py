from manim import *
import math

class G1Q5VennFormula(Scene):
    def construct(self):
        title = Text("Venn Diagram Formula", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Show the formula
        formula1 = Text("P(A U B) = P(A) + P(B) - P(A n B)", font_size=22, color=YELLOW)
        formula1.shift(UP * 0.5)
        self.play(Write(formula1))

        # Draw a simple Venn with example values
        rect = Rectangle(width=4.5, height=2.5, color=WHITE)
        rect.shift(DOWN * 0.5)
        self.play(Create(rect))

        circle_a = Circle(radius=1.0, color=BLUE)
        circle_a.shift(LEFT * 0.7 + DOWN * 0.5)
        label_a = Text("A: 10", font_size=18, color=BLUE)
        label_a.next_to(circle_a, UP * 0.6 + LEFT * 0.4)
        self.play(Create(circle_a), Write(label_a))

        circle_b = Circle(radius=1.0, color=GREEN)
        circle_b.shift(RIGHT * 0.7 + DOWN * 0.5)
        label_b = Text("B: 8", font_size=18, color=GREEN)
        label_b.next_to(circle_b, UP * 0.6 + RIGHT * 0.4)
        self.play(Create(circle_b), Write(label_b))

        # Values
        a_val = Text("7", font_size=20, color=BLUE)
        a_val.shift(LEFT * 1.1 + DOWN * 0.5)
        overlap_val = Text("3", font_size=20, color=YELLOW)
        overlap_val.shift(DOWN * 0.5)
        b_val = Text("5", font_size=20, color=GREEN)
        b_val.shift(RIGHT * 1.1 + DOWN * 0.5)

        self.play(Write(a_val), Write(overlap_val), Write(b_val))

        # Demonstrate the formula with numbers
        formula2 = Text("P(A U B) = 10 + 8 - 3 = 15", font_size=20, color=YELLOW)
        formula2.shift(DOWN * 2.2)
        self.play(Write(formula2))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(formula1), FadeOut(rect),
                  FadeOut(circle_a), FadeOut(label_a),
                  FadeOut(circle_b), FadeOut(label_b),
                  FadeOut(a_val), FadeOut(overlap_val), FadeOut(b_val), FadeOut(formula2))
