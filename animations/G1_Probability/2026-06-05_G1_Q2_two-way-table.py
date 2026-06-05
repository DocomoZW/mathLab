from manim import *
import math

class G1Q2TwoWayTable(Scene):
    def construct(self):
        title = Text("Two-Way Table", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Draw a 3x3 grid for a two-way table (Gender x Subject preference)
        # Grid lines
        grid = VGroup()
        # Vertical lines
        for i in range(4):
            x = -2 + i * 1.5
            line = Line(start=[x, 1.5, 0], end=[x, -1.5, 0], color=WHITE)
            grid.add(line)
        # Horizontal lines
        for j in range(4):
            y = 1.5 - j * 1.0
            line = Line(start=[-2, y, 0], end=[2.5, y, 0], color=WHITE)
            grid.add(line)

        self.play(Create(grid))

        # Labels
        header_s = Text("Science", font_size=16, color=BLUE)
        header_s.shift([-1.25, 1.75, 0])
        header_a = Text("Arts", font_size=16, color=BLUE)
        header_a.shift([0.25, 1.75, 0])
        header_t = Text("Total", font_size=16, color=BLUE)
        header_t.shift([1.75, 1.75, 0])

        row_b = Text("Boys", font_size=16, color=GREEN)
        row_b.shift([-2.75, 0.75, 0])
        row_g = Text("Girls", font_size=16, color=PINK)
        row_g.shift([-2.75, -0.25, 0])
        row_t = Text("Total", font_size=16, color=WHITE)
        row_t.shift([-2.75, -1.25, 0])

        self.play(Write(header_s), Write(header_a), Write(header_t),
                  Write(row_b), Write(row_g), Write(row_t))

        # Data values
        val_bs = Text("12", font_size=20, color=WHITE)
        val_bs.shift([-1.25, 0.75, 0])
        val_ba = Text("8", font_size=20, color=WHITE)
        val_ba.shift([0.25, 0.75, 0])
        val_bt = Text("20", font_size=20, color=GREEN)
        val_bt.shift([1.75, 0.75, 0])

        val_gs = Text("15", font_size=20, color=WHITE)
        val_gs.shift([-1.25, -0.25, 0])
        val_ga = Text("5", font_size=20, color=WHITE)
        val_ga.shift([0.25, -0.25, 0])
        val_gt = Text("20", font_size=20, color=PINK)
        val_gt.shift([1.75, -0.25, 0])

        val_ts = Text("27", font_size=20, color=BLUE)
        val_ts.shift([-1.25, -1.25, 0])
        val_ta = Text("13", font_size=20, color=BLUE)
        val_ta.shift([0.25, -1.25, 0])
        val_tt = Text("40", font_size=20, color=YELLOW)
        val_tt.shift([1.75, -1.25, 0])

        self.play(Write(val_bs), Write(val_ba), Write(val_bt),
                  Write(val_gs), Write(val_ga), Write(val_gt),
                  Write(val_ts), Write(val_ta), Write(val_tt))
        self.wait(1)

        # Highlight a probability
        prob = Text("P(Boy | Science) = 12/27", font_size=20, color=YELLOW)
        prob.next_to(grid, DOWN * 0.5)
        self.play(Write(prob))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(grid), FadeOut(header_s), FadeOut(header_a), FadeOut(header_t),
                  FadeOut(row_b), FadeOut(row_g), FadeOut(row_t),
                  FadeOut(val_bs), FadeOut(val_ba), FadeOut(val_bt),
                  FadeOut(val_gs), FadeOut(val_ga), FadeOut(val_gt),
                  FadeOut(val_ts), FadeOut(val_ta), FadeOut(val_tt), FadeOut(prob))
