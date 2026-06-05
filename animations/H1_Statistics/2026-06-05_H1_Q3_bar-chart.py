from manim import *
import math

class H1Q3BarChart(Scene):
    def construct(self):
        title = Text("Bar Chart").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw axes
        x_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        x_axis.shift(DOWN * 2.5)
        y_axis = Line(DOWN * 2.5, UP * 2.5, color=WHITE)
        y_axis.shift(LEFT * 4)

        self.play(Create(x_axis), Create(y_axis))
        self.wait(0.2)

        # Labels
        y_label = Text("Frequency", font_size=18)
        y_label.shift(LEFT * 4.8 + UP * 1.5)
        self.play(Write(y_label))

        # Bar data
        categories = ["Apple", "Banana", "Cherry", "Date", "Elder"]
        values = [8, 5, 7, 3, 6]
        colors = [RED, YELLOW, PURPLE, BLUE, GREEN]
        bar_width = 0.8
        bar_spacing = 1.2

        bars = VGroup()
        labels = VGroup()
        for i, (cat, val, col) in enumerate(zip(categories, values, colors)):
            x_pos = LEFT * 2.8 + RIGHT * bar_spacing * i
            bar = Rectangle(width=bar_width, height=val * 0.35, color=col, fill_opacity=0.8)
            bar.move_to(x_pos + DOWN * 2.5, aligned_edge=DOWN)
            bars.add(bar)

            # Label
            lbl = Text(cat, font_size=14)
            lbl.next_to(bar, DOWN, buff=0.1)
            labels.add(lbl)

            # Value on top
            val_text = Text(str(val), font_size=14)
            val_text.next_to(bar, UP, buff=0.05)
            labels.add(val_text)

        for bar, lbl in zip(bars, labels):
            self.play(Create(bar), Write(lbl), run_time=0.4)

        self.wait(0.5)

        note = Text("Bar chart: categorical data, gaps between bars", font_size=20, color=GRAY)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
