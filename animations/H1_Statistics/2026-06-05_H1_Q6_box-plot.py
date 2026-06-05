from manim import *
import math

class H1Q6BoxPlot(Scene):
    def construct(self):
        title = Text("Box and Whisker Plot").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Data summary
        min_val = 3
        q1 = 7
        median = 10
        q3 = 15
        max_val = 20

        stats = VGroup()
        s1 = Text(f"Min = {min_val}", font_size=18, color=BLUE)
        s2 = Text(f"Q1 = {q1}", font_size=18, color=PURPLE)
        s3 = Text(f"Median = {median}", font_size=18, color=RED)
        s4 = Text(f"Q3 = {q3}", font_size=18, color=PURPLE)
        s5 = Text(f"Max = {max_val}", font_size=18, color=BLUE)
        stats.arrange(RIGHT, buff=0.4)
        stats.shift(UP * 1.5)
        self.play(Write(s1), Write(s2), Write(s3), Write(s4), Write(s5))
        self.wait(0.3)

        # Number line
        num_line = Line(LEFT * 5, RIGHT * 5, color=WHITE)
        num_line.shift(DOWN * 0.5)
        self.play(Create(num_line))
        self.wait(0.2)

        # Scale: map values 0-25 to -5 to +5
        def scale_x(val):
            return LEFT * 5 + RIGHT * (val / 25.0) * 10

        # Tick marks
        ticks = VGroup()
        for v in range(0, 26, 5):
            x = scale_x(v)
            tick = Line(UP * 0.1, DOWN * 0.1, color=GRAY)
            tick.move_to(x + DOWN * 0.5)
            ticks.add(tick)
            lbl = Text(str(v), font_size=12, color=GRAY)
            lbl.next_to(tick, DOWN, buff=0.02)
            ticks.add(lbl)
        self.play(Create(ticks))
        self.wait(0.2)

        # Whiskers and box
        y_center = DOWN * 0.5

        # Left whisker (min to Q1)
        left_whisker = Line(scale_x(min_val), scale_x(q1), color=BLUE)
        left_whisker.shift(UP * 0.5)

        # Box (Q1 to Q3)
        box = Rectangle(width=scale_x(q3)[0] - scale_x(q1)[0], height=1.0, color=PURPLE, fill_opacity=0.3)
        box.move_to(UP * 0.5, aligned_edge=DOWN)
        box.shift(DOWN * 0.5)
        # Position box horizontally
        box_center_x = (scale_x(q1)[0] + scale_x(q3)[0]) / 2
        box.move_to(box_center_x * RIGHT + DOWN * 0.5)

        # Right whisker (Q3 to max)
        right_whisker = Line(scale_x(q3), scale_x(max_val), color=BLUE)
        right_whisker.shift(UP * 0.5)

        # Median line inside box
        median_line = Line(UP * 0.5, DOWN * 0.5, color=RED)
        median_line.move_to(scale_x(median) + DOWN * 0.5)

        # End caps
        cap_left = Line(UP * 0.3, DOWN * 0.3, color=BLUE)
        cap_left.move_to(scale_x(min_val) + DOWN * 0.5)

        cap_right = Line(UP * 0.3, DOWN * 0.3, color=BLUE)
        cap_right.move_to(scale_x(max_val) + DOWN * 0.5)

        self.play(
            Create(left_whisker),
            Create(right_whisker),
            Create(box),
            Create(median_line),
            Create(cap_left),
            Create(cap_right)
        )
        self.wait(0.5)

        # Annotations
        annotations = VGroup()
        labels_data = [
            (min_val, "Min", BLUE),
            (q1, "Q1", PURPLE),
            (median, "Median", RED),
            (q3, "Q3", PURPLE),
            (max_val, "Max", BLUE),
        ]
        for val, label, color in labels_data:
            x = scale_x(val)
            lbl = Text(label, font_size=12, color=color)
            lbl.move_to(x + UP * 1.3)
            annotations.add(lbl)

        self.play(Write(annotations))
        self.wait(0.5)

        note = Text("Box = middle 50% (IQR), Whiskers = spread to min/max", font_size=16, color=GRAY)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
