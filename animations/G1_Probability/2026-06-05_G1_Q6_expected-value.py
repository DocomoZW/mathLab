from manim import *
import math

class G1Q6ExpectedValue(Scene):
    def construct(self):
        title = Text("Expected Value", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Show a fair die
        die = Square(side_length=1.5, color=WHITE)
        die.shift(UP * 0.5)
        die_label = Text("Fair Die", font_size=20, color=WHITE)
        die_label.next_to(die, UP * 0.3)
        self.play(Create(die), Write(die_label))

        # Dot pattern showing all faces (simplified: show face values)
        values = VGroup()
        for i in range(1, 7):
            val = Text(str(i), font_size=16, color=WHITE)
            x_pos = -2.5 + (i - 1) * 1.0
            val.shift([x_pos, 0.5, 0])
            values.add(val)

        # Show outcome values
        outcomes_label = Text("Outcomes: 1, 2, 3, 4, 5, 6", font_size=18, color=WHITE)
        outcomes_label.shift(DOWN * 0.3)
        self.play(Write(outcomes_label))

        # Formula for expected value
        formula = Text("E(X) = (1+2+3+4+5+6) / 6", font_size=20, color=YELLOW)
        formula.shift(DOWN * 1.2)
        self.play(Write(formula))

        # Result
        result = Text("Expected Value = 3.5", font_size=22, color=GREEN)
        result.shift(DOWN * 2.0)
        self.play(Write(result))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(die), FadeOut(die_label),
                  FadeOut(values), FadeOut(outcomes_label), FadeOut(formula), FadeOut(result))
