from manim import *
import math

class H1Q2CumulativeFrequency(Scene):
    def construct(self):
        title = Text("Cumulative Frequency").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw cumulative frequency table
        grid = VGroup()
        cols = 3
        rows = 6
        cell_w = 2.8
        cell_h = 0.6
        top_left = LEFT * (cell_w * 1.5) + UP * 1.5

        headers = ["Class", "Freq (f)", "Cumul. Freq (cf)"]
        for j, h in enumerate(headers):
            rect = Rectangle(width=cell_w, height=cell_h, color=WHITE)
            rect.move_to(top_left + RIGHT * cell_w * j)
            grid.add(rect)
            txt = Text(h, font_size=16)
            txt.move_to(rect.get_center())
            grid.add(txt)

        # Data with running total
        data = [
            ("0 - 9", "6", "6"),
            ("10 - 19", "7", "13"),
            ("20 - 29", "8", "21"),
            ("30 - 39", "9", "30"),
        ]
        rows_group = VGroup()
        for i, (cls, freq, cf) in enumerate(data):
            y_offset = DOWN * cell_h * (i + 1)
            vals = [cls, freq, cf]
            row_elems = VGroup()
            for j, d in enumerate(vals):
                rect = Rectangle(width=cell_w, height=cell_h, color=GRAY)
                rect.move_to(top_left + RIGHT * cell_w * j + y_offset)
                txt = Text(d, font_size=18)
                txt.move_to(rect.get_center())
                row_elems.add(rect, txt)
            rows_group.add(row_elems)

        self.play(Create(grid))
        self.wait(0.3)

        # Animate each row appearing
        for row in rows_group:
            self.play(Create(row), run_time=0.5)
            self.wait(0.2)

        self.wait(0.3)

        # Show running total explanation
        arrow = Arrow(UP * 0.5, DOWN * 0.5, color=YELLOW)
        arrow.next_to(grid, RIGHT, buff=0.3)
        arrow.shift(UP * 0.3)
        self.play(Create(arrow))

        cf_label = Text("Running Total", font_size=22, color=YELLOW)
        cf_label.next_to(arrow, RIGHT, buff=0.2)
        self.play(Write(cf_label))
        self.wait(0.3)

        # Show addition animation: cumulative freq building
        add_text = Text("6 + 7 = 13,  13 + 8 = 21,  21 + 9 = 30", font_size=20, color=GREEN)
        add_text.next_to(grid, DOWN, buff=0.5)
        self.play(Write(add_text))
        self.wait(0.5)

        # Final note
        final_note = Text("Cumulative frequency: sum of frequencies up to that class", font_size=20, color=BLUE)
        final_note.to_edge(DOWN)
        self.play(Write(final_note))
        self.wait(2)
