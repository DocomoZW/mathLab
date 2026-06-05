# topic_id: A1_Q3
# track: igcse_o
# unit: A1_Number
# description: Converting recurring decimal 0.777... to fraction 7/9 step-by-step

from manim import *

class RecurringDecimalToFraction(Scene):
    def construct(self):
        # Title
        title = Text("Recurring Decimal to Fraction: 0.777...", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Step 0: Show the decimal
        decimal = Text("0.777...", font_size=48, color=YELLOW)
        decimal.shift(UP * 1.5)
        self.play(Write(decimal))
        self.wait(0.3)

        # Explanation text
        explanation = Text(
            "The digit 7 repeats forever.",
            font_size=20, color=WHITE
        )
        explanation.next_to(decimal, DOWN, buff=0.2)
        self.play(Write(explanation))
        self.wait(0.5)

        # Step 1: Let x = 0.777...
        step1_box = Rectangle(width=8, height=0.7, color=WHITE, fill_opacity=0.1)
        step1_box.shift(UP * 0.3)

        step1 = Text(
            "Let x = 0.777...",
            font_size=32, color=WHITE
        )
        step1.move_to(step1_box.get_center())
        self.play(Create(step1_box), Write(step1))
        self.wait(0.5)

        # Step 2: Multiply by 10
        step2_box = Rectangle(width=8, height=0.7, color=WHITE, fill_opacity=0.1)
        step2_box.shift(DOWN * 0.5)

        step2 = Text(
            "10x = 7.777...",
            font_size=32, color=GREEN
        )
        step2.move_to(step2_box.get_center())
        self.play(Create(step2_box), Write(step2))
        self.wait(0.5)

        # Step 3: Subtract
        step3_box = Rectangle(width=8, height=0.7, color=WHITE, fill_opacity=0.1)
        step3_box.shift(DOWN * 1.3)

        step3 = Text(
            "10x - x = 7.777... - 0.777...",
            font_size=32, color=YELLOW
        )
        step3.move_to(step3_box.get_center())
        self.play(Create(step3_box), Write(step3))
        self.wait(0.5)

        # Step 4: Simplify
        step4_box = Rectangle(width=8, height=0.7, color=WHITE, fill_opacity=0.1)
        step4_box.shift(DOWN * 2.1)

        step4 = Text(
            "9x = 7",
            font_size=40, color=GREEN
        )
        step4.move_to(step4_box.get_center())
        self.play(Create(step4_box), Write(step4))
        self.wait(0.5)

        # Step 5: Solve
        step5_box = Rectangle(width=8, height=0.7, color=WHITE, fill_opacity=0.1)
        step5_box.shift(DOWN * 2.9)

        step5 = Text(
            "x = 7/9",
            font_size=40, color=YELLOW
        )
        step5.move_to(step5_box.get_center())
        self.play(Create(step5_box), Write(step5))
        self.wait(0.5)

        # Final answer highlight
        answer = Text("0.777... = 7/9", font_size=48, color=YELLOW)
        answer.to_edge(DOWN, buff=0.5)
        self.play(Write(answer))
        self.wait(0.5)

        # Verification
        verify = Text("Check: 7 / 9 = 0.777... OK", font_size=20, color=GREEN)
        verify.next_to(answer, DOWN, buff=0.3)
        self.play(Write(verify))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = RecurringDecimalToFraction()
    scene.render()
