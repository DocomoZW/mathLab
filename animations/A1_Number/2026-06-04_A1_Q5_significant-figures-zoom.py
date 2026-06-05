# topic_id: A1_Q5
# track: igcse_o
# unit: A1_Number
# description: Number line zoom showing significant figures - rounding 20458 to 2 s.f. = 20000

from manim import *
import numpy as np

class SignificantFiguresZoom(Scene):
    def construct(self):
        # Title
        title = Text("Significant Figures: Rounding 20458 to 2 s.f.", font_size=34, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Step 1: Show the number
        number = Text("20458", font_size=48, color=YELLOW)
        number.shift(UP * 1.5)
        self.play(Write(number))
        self.wait(0.3)

        # Step 2: Identify significant figures
        sf_label = Text("1st s.f. = 2,  2nd s.f. = 0", font_size=24, color=GREEN)
        sf_label.next_to(number, DOWN, buff=0.3)

        # Highlight the first two digits
        highlight = SurroundingRectangle(
            number,
            color=GREEN, buff=0.1
        )

        self.play(Write(sf_label))
        self.play(Create(highlight))
        self.wait(0.3)

        # Step 3: Show the third digit (4) - which determines rounding
        third_label = Text("3rd digit = 4 < 5 -> round down", font_size=22, color=RED)
        third_label.next_to(number, DOWN, buff=0.8)

        self.play(Write(third_label))
        self.wait(0.5)

        # Step 4: Wide number line using basic shapes
        line_x_start = -5.0
        line_x_end = 5.0
        line_y = -0.5
        line = Line(np.array([line_x_start, line_y, 0]), np.array([line_x_end, line_y, 0]), color=WHITE)

        # Tick marks at 0, 5000, 10000, 15000, 20000, 25000, 30000
        tick_positions = {
            0: "0",
            5000: "5000",
            10000: "10000",
            15000: "15000",
            20000: "20000",
            25000: "25000",
            30000: "30000"
        }
        ticks = VGroup()
        tick_lbls = VGroup()
        for val, lbl in tick_positions.items():
            x = line_x_start + (val / 30000) * (line_x_end - line_x_start)
            tick = Line(np.array([x, line_y, 0]), np.array([x, line_y - 0.15, 0]), color=WHITE, stroke_width=1.5)
            ticks.add(tick)
            t = Text(lbl, font_size=14, color=WHITE)
            t.next_to(tick, DOWN, buff=0.1)
            tick_lbls.add(t)

        # Dot at 20458
        dot_x = line_x_start + (20458 / 30000) * (line_x_end - line_x_start)
        dot = Dot(np.array([dot_x, line_y, 0]), color=YELLOW, radius=0.1)
        dot_label = Text("20458", font_size=16, color=YELLOW)
        dot_label.next_to(dot, UP, buff=0.1)

        self.play(
            FadeOut(highlight),
            FadeOut(third_label),
            FadeOut(sf_label),
        )
        self.play(
            Create(line),
            Create(ticks),
            Write(tick_lbls),
            Create(dot),
            Write(dot_label)
        )
        self.wait(0.5)

        # Step 5: Show the two possible rounded values: 20000 or 21000 (to 2 s.f.)
        x_20000 = line_x_start + (20000 / 30000) * (line_x_end - line_x_start)
        x_21000 = line_x_start + (21000 / 30000) * (line_x_end - line_x_start)

        round_down = Text("20000", font_size=36, color=GREEN)
        round_down.move_to(np.array([x_20000, line_y - 0.8, 0]))
        round_up = Text("21000", font_size=36, color=RED)
        round_up.move_to(np.array([x_21000, line_y - 0.8, 0]))

        # Arrow from dot to 20000
        arrow_down = Arrow(dot.get_center(), round_down.get_top(), color=GREEN, buff=0.1)
        arrow_up = Arrow(dot.get_center(), round_up.get_top(), color=RED, buff=0.1)

        self.play(Write(round_down), Write(round_up))
        self.play(Create(arrow_down), Create(arrow_up))
        self.wait(0.3)

        # Check-mark near 20000 (the correct answer since 4 < 5)
        check = Text("OK (4 < 5, round down)", font_size=18, color=GREEN)
        check.next_to(round_down, DOWN, buff=0.2)
        self.play(Write(check))
        self.wait(0.5)

        # Step 6: Zoom into the relevant region
        zoom_box = Rectangle(width=4, height=3, color=YELLOW, stroke_width=2)
        zoom_box.move_to(np.array([dot_x, line_y - 0.4, 0]))

        self.play(Create(zoom_box))
        self.wait(0.3)

        # Zoomed number line
        zoom_line_y = -2.5
        zoom_start_x = -4.0
        zoom_end_x = 4.0

        zoom_line = Line(np.array([zoom_start_x, zoom_line_y, 0]), np.array([zoom_end_x, zoom_line_y, 0]), color=WHITE)

        # Zoom ticks at 19000, 20000, 21000, 22000
        zoom_ticks_data = {19000: "19000", 20000: "20000", 21000: "21000", 22000: "22000"}
        zoom_ticks = VGroup()
        zoom_tick_lbls = VGroup()
        for val, lbl in zoom_ticks_data.items():
            x = zoom_start_x + ((val - 19000) / 3000) * (zoom_end_x - zoom_start_x)
            zt = Line(np.array([x, zoom_line_y, 0]), np.array([x, zoom_line_y - 0.15, 0]), color=WHITE, stroke_width=1.5)
            zoom_ticks.add(zt)
            zl = Text(lbl, font_size=16, color=WHITE)
            zl.next_to(zt, DOWN, buff=0.1)
            zoom_tick_lbls.add(zl)

        # Dot on zoomed line
        zoom_dot_x = zoom_start_x + ((20458 - 19000) / 3000) * (zoom_end_x - zoom_start_x)
        zoom_dot = Dot(np.array([zoom_dot_x, zoom_line_y, 0]), color=YELLOW, radius=0.1)

        self.play(
            Create(zoom_line),
            Create(zoom_ticks),
            Write(zoom_tick_lbls),
            Create(zoom_dot)
        )
        self.wait(0.5)

        # Final answer
        answer = Text("20458 approx= 20000 (2 s.f.)", font_size=36, color=YELLOW)
        answer.to_edge(DOWN, buff=0.3)
        self.play(Write(answer))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = SignificantFiguresZoom()
    scene.render()
