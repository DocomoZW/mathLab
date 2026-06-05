# topic_id: A1_Q4
# track: igcse_o
# unit: A1_Number
# description: Compound interest animation showing $1000 growing at 5% per year over 5 years

from manim import *
import numpy as np

class CompoundInterest(Scene):
    def construct(self):
        # Title
        title = Text("Compound Interest: $1000 at 5% per year", font_size=32, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Data
        initial_amount = 1000
        rate = 0.05
        years = 5
        amounts = [initial_amount * (1 + rate) ** t for t in range(years + 1)]

        # Create bars using simple rectangles
        bars = VGroup()
        labels = VGroup()
        bar_width = 0.6
        max_height = 4.0
        max_amount = max(amounts)

        for i, amt in enumerate(amounts):
            height = (amt / max_amount) * max_height
            color = interpolate_color(GREEN, YELLOW, i / years)
            bar = Rectangle(
                width=bar_width,
                height=height,
                color=color,
                fill_color=color,
                fill_opacity=0.7,
            )
            bar.move_to(np.array([-3.5 + i * 1.5, -1.5 + height / 2, 0]))
            bars.add(bar)

            amt_label = Text(f"${amt:.0f}", font_size=14, color=color)
            amt_label.next_to(bar, UP, buff=0.1)
            labels.add(amt_label)

            year_label = Text(f"Year {i}", font_size=14, color=WHITE)
            year_label.next_to(bar, DOWN, buff=0.1)
            labels.add(year_label)

        # Animate bars appearing
        for i in range(len(amounts)):
            self.play(
                Create(bars[i]),
                Write(labels[i * 2]),
                Write(labels[i * 2 + 1])
            )
            self.wait(0.2)

            if i > 0:
                prev_amt = amounts[i - 1]
                interest = amounts[i] - prev_amt
                interest_text = Text(f"+${interest:.0f}", font_size=14, color=GREEN)
                interest_text.next_to(bars[i], RIGHT, buff=0.2)
                self.play(Write(interest_text))
                self.wait(0.2)
                self.play(FadeOut(interest_text))

        # Show the formula
        formula = Text(
            "A = P(1 + r/100)^t",
            font_size=28, color=WHITE
        )
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(0.5)

        # Annotate compounding effect
        annotation = Text(
            "Interest earns interest - exponential growth!",
            font_size=20, color=YELLOW
        )
        annotation.next_to(formula, DOWN, buff=0.2)
        self.play(Write(annotation))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = CompoundInterest()
    scene.render()
