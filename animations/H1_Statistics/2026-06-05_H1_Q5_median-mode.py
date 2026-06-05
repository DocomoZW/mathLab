from manim import *
import math

class H1Q5MedianMode(Scene):
    def construct(self):
        title = Text("Median and Mode").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Sorted data as dots
        data = [2, 3, 4, 5, 5, 5, 7, 8, 9]

        # Number line
        num_line = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        num_line.shift(DOWN * 1.5)
        self.play(Create(num_line))
        self.wait(0.2)

        # Dots for each value
        dots = VGroup()
        labels = VGroup()
        for i, val in enumerate(data):
            x_pos = LEFT * 3.5 + RIGHT * val * 0.7
            dot = Dot(color=BLUE, radius=0.12)
            dot.move_to(x_pos + UP * 0.3)
            dots.add(dot)
            lbl = Text(str(val), font_size=14)
            lbl.next_to(dot, DOWN, buff=0.05)
            labels.add(lbl)

        self.play(Create(dots), Write(labels))
        self.wait(0.5)

        # Position indices
        indices_text = Text("Positions: 1  2  3  4  5  6  7  8  9", font_size=16, color=GRAY)
        indices_text.shift(UP * 0.5)
        self.play(Write(indices_text))
        self.wait(0.3)

        # Highlight median
        median_pos = 5  # (9+1)/2 = 5th position
        median_val = data[median_pos - 1]  # 5
        median_x = LEFT * 3.5 + RIGHT * median_val * 0.7

        median_box = Square(side_length=0.4, color=RED)
        median_box.move_to(median_x + UP * 0.3)
        self.play(Create(median_box))
        median_label = Text("Median = 5", font_size=20, color=RED)
        median_label.next_to(median_box, UP, buff=0.3)
        self.play(Write(median_label))
        self.wait(0.5)

        # Show mode
        mode_text = Text("Mode = 5 (appears 3 times)", font_size=20, color=GREEN)
        mode_text.shift(DOWN * 0.5)
        self.play(Write(mode_text))
        self.wait(0.3)

        # Highlight the three 5s
        for i, val in enumerate(data):
            if val == 5:
                x_pos = LEFT * 3.5 + RIGHT * val * 0.7
                highlight = Circle(radius=0.25, color=GREEN)
                highlight.move_to(x_pos + UP * 0.3)
                self.play(Create(highlight), run_time=0.2)

        self.wait(0.5)

        # Summary
        summary = VGroup()
        m1 = Text("Median: middle value when sorted (position (n+1)/2)", font_size=16, color=RED)
        m2 = Text("Mode: most frequent value", font_size=16, color=GREEN)
        summary.arrange(DOWN, buff=0.1, center=False, aligned_edge=LEFT)
        summary.to_edge(DOWN)
        summary.shift(UP * 0.3)
        self.play(Write(m1), Write(m2))
        self.wait(2)
