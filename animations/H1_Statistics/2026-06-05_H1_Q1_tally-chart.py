from manim import *
import math

class H1Q1TallyChart(Scene):
    def construct(self):
        title = Text("Tally Marks to Frequency").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Show tally marks for different values
        # Tally for 3 (III)
        tally_3_text = Text("III  = 3", font_size=36)
        tally_3_text.shift(UP * 2 + LEFT * 4)
        self.play(Write(tally_3_text))
        self.wait(0.3)

        # Tally for 5 (four lines + strike)
        tally_5_group = VGroup()
        for i in range(4):
            line = Line(ORIGIN, UP * 0.6)
            line.shift(RIGHT * 0.15 * i)
            tally_5_group.add(line)
        # diagonal strike
        strike = Line(LEFT * 0.1, UP * 0.6 + RIGHT * 0.55)
        tally_5_group.add(strike)
        tally_5_group.shift(UP * 0.5 + LEFT * 4)

        equals_5 = Text("= 5", font_size=36)
        equals_5.next_to(tally_5_group, RIGHT, buff=0.3)
        tally_5_full = VGroup(tally_5_group, equals_5)
        tally_5_full.shift(UP * 0.5)

        self.play(Create(tally_5_group), Write(equals_5))
        self.wait(0.3)

        # Tally for 7 (5 + 2)
        tally_7_group = VGroup()
        for i in range(4):
            line = Line(ORIGIN, UP * 0.6)
            line.shift(RIGHT * 0.15 * i)
            tally_7_group.add(line)
        strike7 = Line(LEFT * 0.1, UP * 0.6 + RIGHT * 0.55)
        tally_7_group.add(strike7)
        # two more
        for i in range(2):
            line = Line(ORIGIN, UP * 0.6)
            line.shift(RIGHT * 0.15 * (i + 5))
            tally_7_group.add(line)
        tally_7_group.shift(DOWN * 0.8 + LEFT * 4)

        equals_7 = Text("= 7", font_size=36)
        equals_7.next_to(tally_7_group, RIGHT, buff=0.3)

        self.play(Create(tally_7_group), Write(equals_7))
        self.wait(0.5)

        # Build a tally-frequency table
        table_title = Text("Tally Frequency Table", font_size=28)
        table_title.shift(RIGHT * 2 + UP * 2)
        self.play(Write(table_title))

        # Draw table grid
        grid = VGroup()
        cols = 3
        rows = 6
        cell_w = 2.0
        cell_h = 0.6
        top_left = RIGHT * 2 + UP * 1.0

        # headers
        headers = ["Value", "Tally", "Frequency"]
        for j, h in enumerate(headers):
            rect = Rectangle(width=cell_w, height=cell_h, color=WHITE)
            rect.move_to(top_left + RIGHT * cell_w * j)
            grid.add(rect)
            txt = Text(h, font_size=18)
            txt.move_to(rect.get_center())
            grid.add(txt)

        # data rows
        data = [
            ("A", "IIII", "4"),
            ("B", "III", "3"),
            ("C", "II", "2"),
            ("D", "IIII", "4"),
            ("E", "I", "1"),
        ]
        for i, (val, tally, freq) in enumerate(data):
            y_offset = DOWN * cell_h * (i + 1)
            row_data = [val, tally, freq]
            for j, d in enumerate(row_data):
                rect = Rectangle(width=cell_w, height=cell_h, color=GRAY)
                rect.move_to(top_left + RIGHT * cell_w * j + y_offset)
                grid.add(rect)
                txt = Text(d, font_size=18)
                txt.move_to(rect.get_center())
                grid.add(txt)

        self.play(Create(grid))
        self.wait(0.5)

        # Highlight total
        total_box = Rectangle(width=cell_w * 3, height=cell_h, color=YELLOW)
        total_box.move_to(top_left + DOWN * cell_h * 6 + RIGHT * cell_w)
        total_label = Text("Total = 14", font_size=20, color=YELLOW)
        total_label.move_to(total_box.get_center())
        self.play(Create(total_box), Write(total_label))
        self.wait(2)
