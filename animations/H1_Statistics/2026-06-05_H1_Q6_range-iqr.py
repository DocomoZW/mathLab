from manim import *
import math

class H1Q6RangeIQR(Scene):
    def construct(self):
        title = Text("Range and Interquartile Range").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Data points
        data = [3, 5, 7, 8, 9, 10, 12, 14, 15, 18, 20]
        n = len(data)

        # Number line
        num_line = Line(LEFT * 4.5, RIGHT * 4.5, color=WHITE)
        num_line.shift(DOWN * 1.5)
        self.play(Create(num_line))
        self.wait(0.2)

        # Dots
        dots = VGroup()
        for i, val in enumerate(data):
            x_pos = LEFT * 4.0 + RIGHT * val * 0.35
            dot = Dot(color=BLUE, radius=0.1)
            dot.move_to(x_pos + UP * 0.2)
            dots.add(dot)

        self.play(Create(dots))
        self.wait(0.3)

        # Show min and max
        min_val = min(data)
        max_val = max(data)
        min_x = LEFT * 4.0 + RIGHT * min_val * 0.35
        max_x = LEFT * 4.0 + RIGHT * max_val * 0.35

        min_label = Text(f"Min={min_val}", font_size=16, color=GREEN)
        min_label.move_to(min_x + DOWN * 0.8)
        max_label = Text(f"Max={max_val}", font_size=16, color=RED)
        max_label.move_to(max_x + DOWN * 0.8)

        self.play(Write(min_label), Write(max_label))
        self.wait(0.3)

        # Range arrow
        range_arrow = DoubleArrow(min_x + UP * 0.2, max_x + UP * 0.2, color=YELLOW)
        self.play(Create(range_arrow))
        range_text = Text(f"Range = {max_val} - {min_val} = {max_val - min_val}", font_size=18, color=YELLOW)
        range_text.next_to(range_arrow, UP, buff=0.1)
        self.play(Write(range_text))
        self.wait(0.5)

        # Quartiles
        q1_pos = n // 4  # 2nd element (index 2 -> value 7)
        q3_pos = 3 * n // 4  # 8th element (index 8 -> value 15)
        q1_val = data[q1_pos]
        q3_val = data[q3_pos]

        q1_x = LEFT * 4.0 + RIGHT * q1_val * 0.35
        q3_x = LEFT * 4.0 + RIGHT * q3_val * 0.35

        q1_label = Text(f"Q1={q1_val}", font_size=16, color=PURPLE)
        q1_label.move_to(q1_x + DOWN * 0.8)
        q3_label = Text(f"Q3={q3_val}", font_size=16, color=PURPLE)
        q3_label.move_to(q3_x + DOWN * 0.8)

        self.play(Write(q1_label), Write(q3_label))
        self.wait(0.3)

        # IQR arrow
        iqr_arrow = DoubleArrow(q1_x + UP * 0.5, q3_x + UP * 0.5, color=PURPLE)
        self.play(Create(iqr_arrow))
        iqr_text = Text(f"IQR = {q3_val} - {q1_val} = {q3_val - q1_val}", font_size=18, color=PURPLE)
        iqr_text.next_to(iqr_arrow, UP, buff=0.1)
        self.play(Write(iqr_text))
        self.wait(0.5)

        # Explanation
        note1 = Text("Range: spread from min to max (affected by outliers)", font_size=16, color=YELLOW)
        note2 = Text("IQR: spread of middle 50% (not affected by outliers)", font_size=16, color=PURPLE)
        note_group = VGroup(note1, note2)
        note_group.arrange(DOWN, buff=0.1)
        note_group.to_edge(DOWN)
        note_group.shift(UP * 0.3)
        self.play(Write(note1), Write(note2))
        self.wait(2)
