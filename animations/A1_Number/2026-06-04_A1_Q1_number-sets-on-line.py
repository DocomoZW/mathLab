# topic_id: A1_Q1
# track: igcse_o
# unit: A1_Number
# description: Visualizing number sets (natural, integer, rational, irrational) on a number line with labeled points

from manim import *

class NumberSetsOnLine(Scene):
    def construct(self):
        # Title
        title = Text("Number Sets on the Number Line", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.5)

        # Create number line from -5 to 5
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_numbers=True,
            font_size=24,
            include_tip=True,
            label_constructor=Text,
        )
        number_line.shift(DOWN * 0.5)
        self.play(Create(number_line))
        self.wait(0.3)

        # Label each set
        set_labels = VDict()
        label_y = -1.8

        # Natural numbers (N) - green dots on 1,2,3,4,5
        nat_dots = VGroup(*[
            Dot(number_line.n2p(x), color=GREEN, radius=0.12)
            for x in [1, 2, 3, 4, 5]
        ])
        nat_label = Text("ℕ", color=GREEN, font_size=32)
        nat_label.next_to(nat_dots, DOWN, buff=0.3)
        nat_text = Text("Natural: 1, 2, 3, ...", font_size=20, color=GREEN)
        nat_text.next_to(nat_label, DOWN, buff=0.1)

        self.play(
            LaggedStart(*[Create(d) for d in nat_dots], lag_ratio=0.15),
            Write(Text("ℕ", color=GREEN, font_size=24).move_to(number_line.n2p(3)).shift(DOWN * 0.5))
        )
        self.wait(0.3)

        # Integers (Z) - blue dots on all whole numbers
        int_dots = VGroup(*[
            Dot(number_line.n2p(x), color=BLUE, radius=0.10)
            for x in range(-5, 6)
        ])
        int_label = Text("ℤ", color=BLUE, font_size=32)
        int_label.next_to(int_dots, DOWN, buff=0.5)

        self.play(
            LaggedStart(*[Create(d) for d in int_dots], lag_ratio=0.08),
            Write(int_label)
        )
        self.wait(0.3)

        # Rational numbers (Q) - yellow dots at fractions between -2 and 2
        frac_positions = []
        for x in range(-4, 5):
            for frac in [0.25, 0.5, 0.75]:
                frac_positions.append(x + frac)
        # Limit to some representative ones
        sample_fracs = [-4.5, -3.25, -2.5, -1.75, -0.5, 0.5, 1.25, 2.5, 3.75, 4.5]

        rat_dots = VGroup(*[
            Dot(number_line.n2p(x), color=YELLOW, radius=0.08, fill_opacity=0.7)
            for x in sample_fracs
        ])
        rat_label = Text("ℚ", color=YELLOW, font_size=32)
        rat_label.next_to(rat_dots, DOWN, buff=0.5)

        # Add a fraction example
        frac_example = Text("3/4 = 0.75", font_size=24, color=YELLOW)
        frac_example.next_to(rat_label, DOWN, buff=0.1)

        self.play(
            LaggedStart(*[Create(d) for d in rat_dots], lag_ratio=0.1),
            Write(rat_label)
        )
        self.wait(0.3)

        # Irrational numbers (√2, π plotted approximately)
        irr_positions = {
            "√2 ≈ 1.414": 1.414,
            "π ≈ 3.142": 3.142,
        }
        irr_dots = VGroup()
        irr_labels = VGroup()
        for label_text, pos in irr_positions.items():
            dot = Dot(number_line.n2p(pos), color=RED, radius=0.15)
            lbl = Text(label_text, color=RED, font_size=20)
            lbl.next_to(number_line.n2p(pos), UP, buff=0.15)
            irr_dots.add(dot)
            irr_labels.add(lbl)

        irr_set_label = Text("ℝ", color=PURPLE, font_size=32)
        irr_set_label.next_to(irr_dots, DOWN, buff=0.5)

        self.play(
            LaggedStart(*[Create(d) for d in irr_dots], lag_ratio=0.3),
            LaggedStart(*[Write(l) for l in irr_labels], lag_ratio=0.3),
        )
        self.wait(0.3)

        # Show the hierarchy
        hierarchy = Text(
            "ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ",
            font_size=36, color=WHITE
        )
        hierarchy.to_edge(DOWN, buff=0.5)
        self.play(Write(hierarchy))
        self.wait(0.5)

        # Highlight the key insight
        highlight_box = SurroundingRectangle(hierarchy, color=YELLOW, buff=0.1)
        self.play(Create(highlight_box))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = NumberSetsOnLine()
    scene.render()
