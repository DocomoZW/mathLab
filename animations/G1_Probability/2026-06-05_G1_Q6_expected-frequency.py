from manim import *
import math

class G1Q6ExpectedFrequency(Scene):
    def construct(self):
        title = Text("Expected Frequency", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Scenario: Spinner with 4 colors, spun 200 times
        # Spinner
        center = [0, 0.5, 0]
        radius = 1.0
        spinner = Circle(radius=radius, color=WHITE)
        spinner.shift(UP * 0.5)
        self.play(Create(spinner))

        # Divide into 4
        for angle in [0, 90, 180, 270]:
            rad = angle * math.pi / 180
            line = Line(
                start=center,
                end=[center[0] + radius * math.cos(rad), center[1] + radius * math.sin(rad), 0],
                color=WHITE
            )
            self.play(Create(line))

        # Labels
        labels = [("R", RED), ("B", BLUE), ("G", GREEN), ("Y", YELLOW)]
        angles = [45, 135, 225, 315]
        for (text, color), angle in zip(labels, angles):
            rad = angle * math.pi / 180
            label = Text(text, font_size=18, color=color)
            label.shift([
                center[0] + radius * 0.6 * math.cos(rad),
                center[1] + radius * 0.6 * math.sin(rad),
                0
            ])
            self.play(Write(label))

        # Formula for expected frequency
        formula = Text("Expected Frequency = P(Event) x Trials", font_size=18, color=WHITE)
        formula.shift(DOWN * 0.5)
        self.play(Write(formula))

        # Example calculation for Red
        example = Text("Red: 1/4 x 200 = 50 times", font_size=20, color=RED)
        example.shift(DOWN * 1.3)
        self.play(Write(example))

        # Summary
        summary = Text("Expected: 50 each color", font_size=20, color=GREEN)
        summary.shift(DOWN * 2.1)
        self.play(Write(summary))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(spinner), FadeOut(formula), FadeOut(example), FadeOut(summary))
