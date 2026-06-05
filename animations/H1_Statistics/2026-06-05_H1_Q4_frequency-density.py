from manim import *
import math

class H1Q4FrequencyDensity(Scene):
    def construct(self):
        title = Text("Frequency Density Formula").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Formula display
        formula_parts = VGroup()

        fd_label = Text("Frequency Density =", font_size=36, color=YELLOW)
        fd_label.shift(UP * 2)
        formula_parts.add(fd_label)

        frac_top = Text("Frequency", font_size=32, color=BLUE)
        frac_bottom = Text("Class Width", font_size=32, color=GREEN)
        frac_line = Line(LEFT * 2.5, RIGHT * 2.5, color=WHITE)

        frac_group = VGroup(frac_top, frac_line, frac_bottom)
        frac_group.arrange(DOWN, buff=0.1)
        frac_group.next_to(fd_label, RIGHT, buff=0.3)
        formula_parts.add(frac_group)

        self.play(Write(formula_parts))
        self.wait(0.5)

        # Example table
        table_title = Text("Example:", font_size=24)
        table_title.shift(LEFT * 3 + DOWN * 0.5)
        self.play(Write(table_title))
        self.wait(0.2)

        # Draw table
        grid = VGroup()
        cell_w = 2.2
        cell_h = 0.5
        top_left = LEFT * 3.5 + DOWN * 0.3

        headers = ["Class", "Freq", "Width", "FD"]
        for j, h in enumerate(headers):
            rect = Rectangle(width=cell_w, height=cell_h, color=WHITE)
            rect.move_to(top_left + RIGHT * cell_w * j)
            grid.add(rect)
            txt = Text(h, font_size=16)
            txt.move_to(rect.get_center())
            grid.add(txt)

        # Data rows
        data = [
            ("0-10", "12", "10", "1.2"),
            ("10-20", "18", "10", "1.8"),
            ("20-35", "15", "15", "1.0"),
            ("35-50", "12", "15", "0.8"),
        ]
        for i, (cls, freq, width, fd) in enumerate(data):
            y_offset = DOWN * cell_h * (i + 1)
            vals = [cls, freq, width, fd]
            for j, d in enumerate(vals):
                rect = Rectangle(width=cell_w, height=cell_h, color=GRAY)
                rect.move_to(top_left + RIGHT * cell_w * j + y_offset)
                grid.add(rect)
                txt = Text(d, font_size=16)
                txt.move_to(rect.get_center())
                grid.add(txt)

        self.play(Create(grid))
        self.wait(0.5)

        # Highlight FD column
        fd_col_box = Rectangle(width=cell_w, height=cell_h * 5, color=YELLOW, fill_opacity=0.15)
        fd_col_box.move_to(top_left + RIGHT * cell_w * 3 + DOWN * cell_h * 2)
        self.play(Create(fd_col_box))
        self.wait(0.3)

        # Formula verification
        verify = Text("FD = Frequency / Class Width", font_size=20, color=GREEN)
        verify.next_to(grid, DOWN, buff=0.5)
        self.play(Write(verify))
        self.wait(0.3)

        # Show calculation
        calc = Text("e.g. 12/10 = 1.2,  18/10 = 1.8,  15/15 = 1.0", font_size=18, color=BLUE)
        calc.next_to(verify, DOWN, buff=0.2)
        self.play(Write(calc))

        note = Text("Area of bar = Frequency Density x Class Width = Frequency", font_size=16, color=GRAY)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
