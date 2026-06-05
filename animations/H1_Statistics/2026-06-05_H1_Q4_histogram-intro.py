from manim import *
import math

class H1Q4HistogramIntro(Scene):
    def construct(self):
        title = Text("Histogram with Unequal Class Widths").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Axes
        x_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        x_axis.shift(DOWN * 2.5)
        y_axis = Line(DOWN * 2.5, UP * 2.5, color=WHITE)
        y_axis.shift(LEFT * 4)

        self.play(Create(x_axis), Create(y_axis))
        self.wait(0.2)

        y_label = Text("Frequency Density", font_size=14)
        y_label.shift(LEFT * 5 + UP * 1.5)
        self.play(Write(y_label))

        # Histogram bars with unequal widths
        # Data: Class intervals with different widths
        # [0-10) width=10, height=1.2 -> area=12
        # [10-20) width=10, height=1.8 -> area=18
        # [20-35) width=15, height=1.0 -> area=15
        # [35-50) width=15, height=0.8 -> area=12
        bars_data = [
            (0, 10, 1.2, BLUE),
            (10, 20, 1.8, GREEN),
            (20, 35, 1.0, YELLOW),
            (35, 50, 1.5, PURPLE),
        ]

        scale_w = 0.15  # width scale
        scale_h = 0.6   # height scale
        y_base = -2.5
        x_start = -4.0

        bars = VGroup()
        for start, end, height, color in bars_data:
            w = (end - start) * scale_w
            h = height * scale_h
            x_center = x_start + (start + (end - start) / 2) * scale_w
            bar = Rectangle(width=w, height=h, color=color, fill_opacity=0.7)
            bar.move_to(x_center + y_base, aligned_edge=DOWN)
            bar.shift(UP * h / 2)
            bars.add(bar)

            # Width label below
            w_label = Text(f"{start}-{end}", font_size=12)
            w_label.next_to(bar, DOWN, buff=0.05)
            bars.add(w_label)

            # Height (frequency density) label
            h_label = Text(f"FD={height:.1f}", font_size=11)
            h_label.next_to(bar, UP, buff=0.05)
            bars.add(h_label)

        for bar in bars:
            self.play(Create(bar), run_time=0.4)

        self.wait(0.5)

        note = Text("Histogram: area = frequency, no gaps between bars", font_size=18, color=GRAY)
        note.to_edge(DOWN)
        note.shift(UP * 0.3)
        self.play(Write(note))
        self.wait(2)
