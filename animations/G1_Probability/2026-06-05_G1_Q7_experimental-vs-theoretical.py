from manim import *
import math

class G1Q7ExperimentalVsTheoretical(Scene):
    def construct(self):
        title = Text("Experimental vs Theoretical", font_size=22, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Coin flip scenario
        coin = Circle(radius=0.8, color=WHITE)
        coin.shift(UP * 0.5)
        coin_label = Text("Coin", font_size=20, color=WHITE)
        coin_label.next_to(coin, UP * 0.3)
        self.play(Create(coin), Write(coin_label))

        # Head/Tail label on coin
        h_label = Text("H", font_size=24, color=BLUE)
        h_label.shift(UP * 0.5 + LEFT * 0.3)
        t_label = Text("T", font_size=24, color=RED)
        t_label.shift(UP * 0.5 + RIGHT * 0.3)
        self.play(Write(h_label), Write(t_label))

        # Theoretical probability
        theoretical = Text("Theoretical: P(H) = 1/2", font_size=20, color=BLUE)
        theoretical.shift(DOWN * 0.3 + LEFT * 1.2)
        self.play(Write(theoretical))

        # Experimental result after 10 flips
        experimental = Text("Experimental (10 flips): 7 H", font_size=18, color=RED)
        experimental.shift(DOWN * 1.0 + LEFT * 1.5)
        self.play(Write(experimental))

        # Experimental probability
        exp_prob = Text("P(H) = 7/10 = 0.7", font_size=20, color=RED)
        exp_prob.shift(DOWN * 1.5 + LEFT * 1.2)
        self.play(Write(exp_prob))

        # Comparing
        comparison = Text("0.5 vs 0.7 - different!", font_size=20, color=YELLOW)
        comparison.shift(DOWN * 2.2)
        self.play(Write(comparison))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(coin), FadeOut(coin_label),
                  FadeOut(h_label), FadeOut(t_label),
                  FadeOut(theoretical), FadeOut(experimental), FadeOut(exp_prob), FadeOut(comparison))
