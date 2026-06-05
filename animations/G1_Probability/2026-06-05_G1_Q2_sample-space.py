from manim import *
import math

class G1Q2SampleSpace(Scene):
    def construct(self):
        title = Text("Sample Space: Two Dice", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Show Die A and Die B as squares with dots
        die1 = Square(side_length=1.0, color=WHITE)
        die1.shift(LEFT * 2 + DOWN * 0.5)
        die1_label = Text("Die A", font_size=18, color=WHITE)
        die1_label.next_to(die1, UP * 0.3)
        self.play(Create(die1), Write(die1_label))

        die2 = Square(side_length=1.0, color=WHITE)
        die2.shift(RIGHT * 2 + DOWN * 0.5)
        die2_label = Text("Die B", font_size=18, color=WHITE)
        die2_label.next_to(die2, UP * 0.3)
        self.play(Create(die2), Write(die2_label))

        # Dot patterns for dice showing 3 and 5
        # Die A (3) - three dots in diagonal
        dot1 = Dot([-2 - 0.25, -0.5 + 0.25, 0], color=WHITE)
        dot2 = Dot([-2, -0.5, 0], color=WHITE)
        dot3 = Dot([-2 + 0.25, -0.5 - 0.25, 0], color=WHITE)
        self.play(Create(dot1), Create(dot2), Create(dot3))

        # Die B (5) - four corners + center
        dot4 = Dot([2 - 0.25, -0.5 + 0.25, 0], color=WHITE)
        dot5 = Dot([2 + 0.25, -0.5 + 0.25, 0], color=WHITE)
        dot6 = Dot([2, -0.5, 0], color=WHITE)
        dot7 = Dot([2 - 0.25, -0.5 - 0.25, 0], color=WHITE)
        dot8 = Dot([2 + 0.25, -0.5 - 0.25, 0], color=WHITE)
        self.play(Create(dot4), Create(dot5), Create(dot6), Create(dot7), Create(dot8))

        # Arrow and outcome
        arrow = Arrow(start=LEFT * 1.5 + DOWN * 0.5, end=RIGHT * 1.5 + DOWN * 0.5, color=YELLOW)
        self.play(Create(arrow))

        outcome = Text("Sum = 8", font_size=24, color=YELLOW)
        outcome.next_to(arrow, DOWN * 0.5)
        self.play(Write(outcome))

        # List sample space
        outcomes_text = Text("Sample Space: 36 outcomes", font_size=20, color=BLUE)
        outcomes_text.next_to(die2_label, UP * 1.5)
        outcomes_text.to_edge(RIGHT)
        self.play(Write(outcomes_text))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(die1), FadeOut(die2), FadeOut(die1_label), FadeOut(die2_label),
                  FadeOut(dot1), FadeOut(dot2), FadeOut(dot3), FadeOut(dot4), FadeOut(dot5),
                  FadeOut(dot6), FadeOut(dot7), FadeOut(dot8), FadeOut(arrow), FadeOut(outcome),
                  FadeOut(outcomes_text))
