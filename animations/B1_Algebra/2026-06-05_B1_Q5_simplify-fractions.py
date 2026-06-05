# topic_id: B1_Q5
# track: igcse_o
# unit: B1_Algebra
# description: Simplifying algebraic fractions by factorising and cancelling

from manim import *

class B1Q5SimplifyFractions(Scene):
    def construct(self):
        title = Text("Simplifying Algebraic Fractions", font_size=28, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show the fraction
        frac = Text("(x^2 - 9) / (x^2 - x - 6)", font_size=30, color=WHITE)
        frac.shift(UP*1.2)
        self.play(Write(frac))
        self.wait(0.3)

        # Step 1: Factorise numerator
        step1 = Text("Step 1: Factorise numerator", font_size=22, color=YELLOW)
        step1.shift(UP*0.3 + LEFT*2)
        self.play(Write(step1))
        self.wait(0.3)

        num_factor = Text("x^2 - 9 = (x + 3)(x - 3)", font_size=24, color=RED)
        num_factor.next_to(step1, DOWN, buff=0.2)
        self.play(Write(num_factor))
        self.wait(0.3)

        # Step 2: Factorise denominator
        step2 = Text("Step 2: Factorise denominator", font_size=22, color=YELLOW)
        step2.next_to(num_factor, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.3)

        den_factor = Text("x^2 - x - 6 = (x + 2)(x - 3)", font_size=24, color=BLUE)
        den_factor.next_to(step2, DOWN, buff=0.2)
        self.play(Write(den_factor))
        self.wait(0.3)

        # Step 3: Show the factorised fraction
        step3 = Text("Step 3: Cancel common factor (x-3)", font_size=22, color=GREEN)
        step3.next_to(den_factor, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(0.3)

        factor_frac = Text("(x+3)(x-3) / (x+2)(x-3)", font_size=26, color=WHITE)
        factor_frac.next_to(step3, DOWN, buff=0.2)
        self.play(Write(factor_frac))
        self.wait(0.3)

        # Highlight and cross out (x-3) in numerator and denominator
        box_num = SurroundingRectangle(factor_frac[8:13], color=RED, buff=0.05)
        box_den = SurroundingRectangle(factor_frac[20:25], color=RED, buff=0.05)
        self.play(Create(box_num), Create(box_den))
        self.wait(0.3)

        # Cross them out
        cross1 = Line(LEFT*0.3, RIGHT*0.3, color=RED, stroke_width=4)
        cross1.move_to(box_num.get_center())
        cross1.rotate(45*DEGREES)
        cross1b = Line(LEFT*0.3, RIGHT*0.3, color=RED, stroke_width=4)
        cross1b.move_to(box_num.get_center())
        cross1b.rotate(-45*DEGREES)

        cross2 = Line(LEFT*0.3, RIGHT*0.3, color=RED, stroke_width=4)
        cross2.move_to(box_den.get_center())
        cross2.rotate(45*DEGREES)
        cross2b = Line(LEFT*0.3, RIGHT*0.3, color=RED, stroke_width=4)
        cross2b.move_to(box_den.get_center())
        cross2b.rotate(-45*DEGREES)

        self.play(Create(cross1), Create(cross1b), Create(cross2), Create(cross2b))
        self.wait(0.5)

        # Final answer
        self.play(
            FadeOut(box_num), FadeOut(box_den),
            FadeOut(cross1), FadeOut(cross1b),
            FadeOut(cross2), FadeOut(cross2b),
            FadeOut(factor_frac),
        )

        result = Text("Answer: (x+3)/(x+2),  x =/= -2, 3", font_size=28, color=GREEN)
        result.to_edge(DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
