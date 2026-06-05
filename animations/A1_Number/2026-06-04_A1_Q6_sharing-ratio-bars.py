# topic_id: A1_Q6
# track: igcse_o
# unit: A1_Number
# description: Sharing ratio as bar splitting animation - sharing $60 in ratio 2:3

from manim import *
import numpy as np

class SharingRatioBars(Scene):
    def construct(self):
        # Title
        title = Text("Sharing in a Ratio: $60 in 2:3", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Show the initial bar (total amount)
        total_bar = Rectangle(width=8, height=1.5, color=WHITE, fill_color=BLUE, fill_opacity=0.3)
        total_bar.shift(DOWN * 0.5)

        total_label = Text("$60", font_size=32, color=WHITE)
        total_label.move_to(total_bar.get_center())

        # Total parts label
        total_parts = Text("Total parts: 2 + 3 = 5", font_size=22, color=YELLOW)
        total_parts.next_to(total_bar, UP, buff=0.3)

        self.play(
            Create(total_bar),
            Write(total_label),
            Write(total_parts)
        )
        self.wait(0.5)

        # Step 1: Show 1 part = $12
        one_part = Text("1 part = $60 / 5 = $12", font_size=24, color=GREEN)
        one_part.next_to(total_bar, DOWN, buff=0.5)
        self.play(Write(one_part))
        self.wait(0.5)

        # Step 2: Split the bar into 5 equal parts
        split_lines = VGroup()
        part_size = 8 / 5
        bar_left = total_bar.get_left()[0]
        bar_top = total_bar.get_top()[1]
        bar_bottom = total_bar.get_bottom()[1]
        for i in range(1, 5):
            x_pos = bar_left + i * part_size
            line = Line(
                np.array([x_pos, bar_top, 0]),
                np.array([x_pos, bar_bottom, 0]),
                color=WHITE, stroke_width=2
            )
            split_lines.add(line)

        self.play(*[Create(line) for line in split_lines])
        self.wait(0.3)

        # Step 3: Color the first 2 parts (green) and last 3 parts (yellow)
        bar_center_x = total_bar.get_center()[0]
        bar_center_y = total_bar.get_center()[1]

        part1 = Rectangle(
            width=part_size * 2, height=1.5,
            color=GREEN, fill_color=GREEN, fill_opacity=0.5
        )
        part1.move_to(np.array([bar_center_x - part_size * 1.5, bar_center_y, 0]))

        part2 = Rectangle(
            width=part_size * 3, height=1.5,
            color=YELLOW, fill_color=YELLOW, fill_opacity=0.5
        )
        part2.move_to(np.array([bar_center_x + part_size * 1.5, bar_center_y, 0]))

        self.play(
            FadeIn(part1),
            FadeIn(part2),
        )
        self.wait(0.3)

        # Final labels on each portion
        first_share = Text("2 parts = $24", font_size=24, color=GREEN)
        first_share.next_to(part1, DOWN, buff=0.3)

        second_share = Text("3 parts = $36", font_size=24, color=YELLOW)
        second_share.next_to(part2, DOWN, buff=0.3)

        self.play(Write(first_share), Write(second_share))
        self.wait(0.5)

        # Show the multiplier calculation
        calc = Text(
            "2:3  ->  $24 : $36",
            font_size=36, color=WHITE
        )
        calc.to_edge(DOWN, buff=0.3)
        self.play(Write(calc))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = SharingRatioBars()
    scene.render()
