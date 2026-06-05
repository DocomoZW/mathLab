# topic_id: A1_Q7
# track: igcse_o
# unit: A1_Number
# description: Scientific notation - moving decimal point to convert 4500000 to 4.5 x 10^6

from manim import *
import numpy as np

class StandardFormDecimal(Scene):
    def construct(self):
        # Title
        title = Text("Scientific Notation: 4,500,000 -> 4.5 x 10^6", font_size=32, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Show the original number
        original = Text("4500000", font_size=48, color=WHITE)
        original.shift(UP * 1.5)
        self.play(Write(original))
        self.wait(0.3)

        # Show it with commas for readability
        with_commas = Text("4,500,000", font_size=40, color=WHITE)
        with_commas.next_to(original, DOWN, buff=0.3)
        self.play(Write(with_commas))
        self.wait(0.3)

        # Show the decimal point (at the end)
        dec_point = Text(".", font_size=40, color=YELLOW)
        dec_point.move_to(with_commas.get_center() + RIGHT * 3.2)
        self.play(Write(dec_point))
        self.wait(0.3)

        # Step: Move decimal 6 places to the left
        arrow = Arrow(
            dec_point.get_center(),
            with_commas.get_center() + LEFT * 1.0,
            color=YELLOW, stroke_width=3
        )
        count_label = Text("Move decimal 6 places left", font_size=20, color=YELLOW)
        count_label.next_to(arrow, UP, buff=0.1)

        self.play(Create(arrow), Write(count_label))
        self.wait(0.5)

        # Transform to show the new position
        result = Text("4.5 x 10^6", font_size=48, color=YELLOW)
        result.next_to(with_commas, DOWN, buff=0.5)

        # Show the intermediate form
        intermediate = Text("4.500000 x 10^6", font_size=36, color=GREEN)
        intermediate.next_to(with_commas, DOWN, buff=0.3)

        self.play(Write(intermediate))
        self.wait(0.3)

        # Trim the trailing zeros
        self.play(
            Transform(intermediate, result)
        )
        self.wait(0.5)

        # Small numbers example
        small_title = Text("Small Numbers: 0.0000072 -> 7.2 x 10^-6", font_size=28, color=BLUE)
        small_title.to_edge(DOWN, buff=0.8)

        self.play(Write(small_title))
        self.wait(0.3)

        # Show small number on screen
        small_num = Text("0.0000072", font_size=36, color=WHITE)
        small_num.shift(DOWN * 2.0 + LEFT * 0.5)
        self.play(Write(small_num))
        self.wait(0.3)

        # Arrow showing the decimal move right
        small_arrow = Arrow(
            small_num.get_center() + LEFT * 2.0,
            small_num.get_center() + RIGHT * 1.5,
            color=YELLOW, stroke_width=2
        )
        small_count = Text("Move decimal 6 places right -> exponent -6", font_size=18, color=YELLOW)
        small_count.next_to(small_arrow, UP, buff=0.1)

        self.play(Create(small_arrow), Write(small_count))
        self.wait(0.3)

        # Final result for small number
        small_result = Text("7.2 x 10^-6", font_size=36, color=YELLOW)
        small_result.next_to(small_num, DOWN, buff=0.3)
        self.play(Write(small_result))
        self.wait(0.5)

        # Show the general form
        general = Text(
            "A x 10^n  where 1 <= A < 10,  n is integer",
            font_size=28, color=WHITE
        )
        general.to_edge(DOWN, buff=0.1)
        self.play(Write(general))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = StandardFormDecimal()
    scene.render()
