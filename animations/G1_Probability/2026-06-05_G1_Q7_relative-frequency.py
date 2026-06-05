from manim import *
import math

class G1Q7RelativeFrequency(Scene):
    def construct(self):
        title = Text("Relative Frequency", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Table header
        header_label = Text("Number of trials vs Relative Frequency", font_size=18, color=WHITE)
        header_label.shift(UP * 0.8)
        self.play(Write(header_label))

        # Draw a simple grid for data
        grid = VGroup()
        # Vertical lines
        for i in range(3):
            x = -2.5 + i * 2.5
            line = Line(start=[x, 1.5, 0], end=[x, -1.5, 0], color=WHITE)
            grid.add(line)
        # Horizontal lines
        for j in range(4):
            y = 1.5 - j * 1.0
            line = Line(start=[-2.5, y, 0], end=[2.5, y, 0], color=WHITE)
            grid.add(line)
        self.play(Create(grid))

        # Headers
        h1 = Text("Trials", font_size=16, color=WHITE)
        h1.shift([-1.25, 1.75, 0])
        h2 = Text("Heads", font_size=16, color=WHITE)
        h2.shift([1.25, 1.75, 0])
        self.play(Write(h1), Write(h2))

        # Row labels
        trials = ["10", "50", "200"]
        heads = ["7", "28", "98"]
        rel_freq = ["0.700", "0.560", "0.490"]

        for i in range(3):
            t = Text(trials[i], font_size=16, color=WHITE)
            t.shift([-1.25, 0.75 - i * 1.0, 0])
            self.play(Write(t))
            h = Text(heads[i], font_size=16, color=WHITE)
            h.shift([1.25, 0.75 - i * 1.0, 0])
            self.play(Write(h))

        # Relative frequency explanation below
        formula = Text("Relative Frequency = Heads / Trials", font_size=18, color=YELLOW)
        formula.shift(DOWN * 1.8)
        self.play(Write(formula))

        # Show convergence
        convergence = Text("As trials increase, rel. freq. -> 0.5", font_size=18, color=GREEN)
        convergence.shift(DOWN * 2.2)
        self.play(Write(convergence))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(header_label), FadeOut(grid),
                  FadeOut(h1), FadeOut(h2),
                  FadeOut(formula), FadeOut(convergence))
