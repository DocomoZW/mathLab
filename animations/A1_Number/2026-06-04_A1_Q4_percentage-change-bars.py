# topic_id: A1_Q4
# track: igcse_o
# unit: A1_Number
# description: Percentage change visualized as bars growing (increase) and shrinking (decrease)

from manim import *

class PercentageChangeBars(Scene):
    def construct(self):
        # Title
        title = Text("Percentage Change: Bar Growth & Shrink", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        base_bottom = DOWN * 0.5

        # Example 1: 15% increase - bar grows
        ex1_label = Text("15% Increase: $200 -> $230", font_size=24, color=GREEN)
        ex1_label.shift(LEFT * 3 + UP * 0.5)

        # Original bar
        bar_orig = Rectangle(width=1.0, height=2.0, color=GREEN, fill_color=GREEN, fill_opacity=0.5)
        bar_orig.move_to(np.array([-3.0, -0.5 + 1.0, 0]))
        bar_orig.align_to(base_bottom, DOWN)

        # New bar (taller)
        bar_new = Rectangle(width=1.0, height=2.3, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        bar_new.move_to(np.array([-1.5, -0.5 + 1.15, 0]))
        bar_new.align_to(base_bottom, DOWN)

        # Value labels
        val_orig = Text("$200", font_size=18, color=GREEN)
        val_orig.next_to(bar_orig, UP, buff=0.1)

        val_new = Text("$230", font_size=18, color=YELLOW)
        val_new.next_to(bar_new, UP, buff=0.1)

        self.play(Write(ex1_label))
        self.play(Create(bar_orig), Write(val_orig))
        self.wait(0.3)
        self.play(
            Transform(bar_orig, bar_new),
            Transform(val_orig, val_new)
        )
        self.wait(0.3)

        # Show the multiplier
        mult1 = Text("x 1.15", font_size=28, color=YELLOW)
        mult1.next_to(bar_new, RIGHT, buff=0.3)
        self.play(Write(mult1))
        self.wait(0.5)

        # Example 2: 20% decrease - bar shrinks
        ex2_label = Text("20% Decrease: $80 -> $64", font_size=24, color=RED)
        ex2_label.shift(RIGHT * 2 + UP * 0.5)

        bar_orig2 = Rectangle(width=1.0, height=2.0, color=BLUE, fill_color=BLUE, fill_opacity=0.5)
        bar_orig2.move_to(np.array([2.0, -0.5 + 1.0, 0]))
        bar_orig2.align_to(base_bottom, DOWN)

        bar_new2 = Rectangle(width=1.0, height=1.6, color=RED, fill_color=RED, fill_opacity=0.5)
        bar_new2.move_to(np.array([3.5, -0.5 + 0.8, 0]))
        bar_new2.align_to(base_bottom, DOWN)

        val_orig2 = Text("$80", font_size=18, color=BLUE)
        val_orig2.next_to(bar_orig2, UP, buff=0.1)

        val_new2 = Text("$64", font_size=18, color=RED)
        val_new2.next_to(bar_new2, UP, buff=0.1)

        self.play(Write(ex2_label))
        self.play(Create(bar_orig2), Write(val_orig2))
        self.wait(0.3)
        self.play(
            Transform(bar_orig2, bar_new2),
            Transform(val_orig2, val_new2)
        )
        self.wait(0.3)

        mult2 = Text("x 0.80", font_size=28, color=RED)
        mult2.next_to(bar_new2, RIGHT, buff=0.3)
        self.play(Write(mult2))
        self.wait(0.5)

        # Formula at bottom
        formula = Text(
            "Percentage change = (New - Original) / Original x 100%",
            font_size=28, color=WHITE
        )
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = PercentageChangeBars()
    scene.render()
