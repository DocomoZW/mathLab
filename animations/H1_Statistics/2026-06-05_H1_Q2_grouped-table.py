from manim import *
import math

class H1Q2GroupedTable(Scene):
    def construct(self):
        title = Text("Grouped Frequency Table").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Raw data
        data_title = Text("Raw Scores:", font_size=24)
        data_title.shift(LEFT * 5 + UP * 1.5)
        self.play(Write(data_title))

        raw_data = [3, 7, 12, 15, 18, 22, 25, 28, 31, 35,
                    4, 8, 11, 16, 19, 23, 26, 29, 33, 37,
                    5, 9, 13, 17, 20, 24, 27, 30, 34, 39]
        data_str = " ".join(str(x) for x in raw_data)
        data_text = Text(data_str, font_size=16, line_spacing=0.8)
        data_text.next_to(data_title, DOWN, buff=0.2)
        data_text.shift(RIGHT * 1.5)
        self.play(Write(data_text))
        self.wait(0.5)

        # Move raw data up and fade
        self.play(FadeOut(data_text), FadeOut(data_title))
        self.wait(0.2)

        # Draw grouped frequency table
        table_title = Text("Grouped Frequency Table", font_size=28)
        table_title.to_edge(UP)
        self.play(Write(table_title))
        self.wait(0.2)

        grid = VGroup()
        cols = 3
        rows = 6
        cell_w = 2.8
        cell_h = 0.6
        top_left = LEFT * (cell_w * 1.5) + UP * 1.5

        headers = ["Class Interval", "Tally", "Frequency"]
        for j, h in enumerate(headers):
            rect = Rectangle(width=cell_w, height=cell_h, color=WHITE)
            rect.move_to(top_left + RIGHT * cell_w * j)
            grid.add(rect)
            txt = Text(h, font_size=18)
            txt.move_to(rect.get_center())
            grid.add(txt)

        # Grouped data: 0-9, 10-19, 20-29, 30-39
        group_data = [
            ("0 - 9", "IIII I", "6"),
            ("10 - 19", "IIII II", "7"),
            ("20 - 29", "IIII III", "8"),
            ("30 - 39", "IIII IIII", "9"),
        ]
        for i, (interval, tally, freq) in enumerate(group_data):
            y_offset = DOWN * cell_h * (i + 1)
            vals = [interval, tally, freq]
            for j, d in enumerate(vals):
                rect = Rectangle(width=cell_w, height=cell_h, color=GRAY)
                rect.move_to(top_left + RIGHT * cell_w * j + y_offset)
                grid.add(rect)
                txt = Text(d, font_size=18)
                txt.move_to(rect.get_center())
                grid.add(txt)

        self.play(Create(grid))
        self.wait(0.5)

        # Explanation
        note = Text("Class intervals group continuous data into ranges", font_size=20, color=BLUE)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
