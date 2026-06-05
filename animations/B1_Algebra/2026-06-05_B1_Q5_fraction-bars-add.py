# topic_id: B1_Q5
# track: igcse_o
# unit: B1_Algebra
# description: Visual fraction bars for adding and subtracting algebraic fractions

from manim import *

class B1Q5FractionBarsAdd(Scene):
    def construct(self):
        title = Text("Adding Algebraic Fractions", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show the fractions: 2/x + 3/(x+1)
        frac1 = Text("2/x", font_size=36, color=RED)
        frac1.shift(UP*1.5 + LEFT*2)
        plus_sign = Text("+", font_size=36, color=WHITE)
        plus_sign.next_to(frac1, RIGHT, buff=0.3)
        frac2 = Text("3/(x+1)", font_size=36, color=BLUE)
        frac2.next_to(plus_sign, RIGHT, buff=0.3)

        self.play(Write(frac1), Write(plus_sign), Write(frac2))
        self.wait(0.3)

        # Show fraction bars below
        # Bar for 2/x
        bar1 = Rectangle(width=3, height=0.4, color=RED, fill_opacity=0.5, fill_color=RED)
        bar1.shift(DOWN*0.5 + LEFT*1.5)
        bar1_label = Text("2", font_size=20, color=WHITE)
        bar1_label.move_to(bar1.get_center())
        bar1_den = Text("x", font_size=20, color=RED)
        bar1_den.next_to(bar1, DOWN, buff=0.1)
        self.play(Create(bar1), Write(bar1_label), Write(bar1_den))
        self.wait(0.2)

        # Bar for 3/(x+1)
        bar2 = Rectangle(width=3, height=0.4, color=BLUE, fill_opacity=0.5, fill_color=BLUE)
        bar2.shift(DOWN*0.5 + RIGHT*1.5)
        bar2_label = Text("3", font_size=20, color=WHITE)
        bar2_label.move_to(bar2.get_center())
        bar2_den = Text("x+1", font_size=20, color=BLUE)
        bar2_den.next_to(bar2, DOWN, buff=0.1)
        self.play(Create(bar2), Write(bar2_label), Write(bar2_den))
        self.wait(0.3)

        # Step 1: Show need for common denominator
        step1 = Text("Need common denominator: x(x+1)", font_size=22, color=YELLOW)
        step1.to_edge(DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(0.3)

        # Resize bars to same height and show the common denominator
        self.play(FadeOut(bar1), FadeOut(bar2), FadeOut(bar1_label), FadeOut(bar2_label), FadeOut(bar1_den), FadeOut(bar2_den))

        # Show transformed fractions
        new_frac1 = Text("2(x+1) / x(x+1)", font_size=28, color=RED)
        new_frac1.shift(DOWN*0.5 + LEFT*2)
        new_frac2 = Text("3x / x(x+1)", font_size=28, color=BLUE)
        new_frac2.shift(DOWN*0.5 + RIGHT*2)

        self.play(Write(new_frac1), Write(new_frac2))
        self.wait(0.3)

        # Show combined fraction bar
        combined_bar = Rectangle(width=5, height=0.5, color=GREEN, fill_opacity=0.5, fill_color=GREEN)
        combined_bar.shift(DOWN*1.5)
        combined_label = Text("2(x+1) + 3x = 5x + 2", font_size=20, color=WHITE)
        combined_label.move_to(combined_bar.get_center())
        combined_den = Text("x(x+1)", font_size=20, color=GREEN)
        combined_den.next_to(combined_bar, DOWN, buff=0.1)

        self.play(Create(combined_bar), Write(combined_label), Write(combined_den))
        self.wait(0.4)

        # Final result
        result = Text("2/x + 3/(x+1) = (5x + 2) / x(x+1)", font_size=26, color=GREEN)
        result.to_edge(DOWN, buff=0.3)
        self.play(FadeOut(step1), Write(result))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
