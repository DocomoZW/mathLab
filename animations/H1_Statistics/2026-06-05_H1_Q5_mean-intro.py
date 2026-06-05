from manim import *
import math

class H1Q5MeanIntro(Scene):
    def construct(self):
        title = Text("Finding the Mean").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Data points as dots
        data = [2, 3, 4, 5, 6, 7, 8]

        # Show data points on a number line
        num_line = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        num_line.shift(DOWN * 1)
        self.play(Create(num_line))
        self.wait(0.2)

        # Tick marks and labels
        ticks = VGroup()
        dot_group = VGroup()
        for i, val in enumerate(data):
            x_pos = LEFT * 3.0 + RIGHT * val * 0.8
            tick = Line(UP * 0.15, DOWN * 0.15, color=WHITE)
            tick.move_to(x_pos + DOWN * 1)
            ticks.add(tick)
            label = Text(str(val), font_size=16)
            label.next_to(tick, DOWN, buff=0.05)
            ticks.add(label)

            # Data dots
            dot = Dot(color=BLUE, radius=0.1)
            dot.move_to(x_pos + UP * 0.3)
            dot_group.add(dot)

        self.play(Create(ticks), Create(dot_group))
        self.wait(0.5)

        # Show sum
        sum_text = Text("Sum = 2 + 3 + 4 + 5 + 6 + 7 + 8 = 35", font_size=22, color=YELLOW)
        sum_text.shift(UP * 0.5)
        self.play(Write(sum_text))
        self.wait(0.3)

        count_text = Text("Number of values = 7", font_size=22, color=GREEN)
        count_text.next_to(sum_text, DOWN, buff=0.2)
        self.play(Write(count_text))
        self.wait(0.3)

        # Mean formula
        mean_formula = VGroup()
        mean_label = Text("Mean =", font_size=28, color=WHITE)
        mean_label.shift(DOWN * 1.5)

        frac_top = Text("35", font_size=26, color=YELLOW)
        frac_bottom = Text("7", font_size=26, color=GREEN)
        frac_line = Line(LEFT * 0.8, RIGHT * 0.8, color=WHITE)
        frac = VGroup(frac_top, frac_line, frac_bottom)
        frac.arrange(DOWN, buff=0.08)
        frac.next_to(mean_label, RIGHT, buff=0.2)

        equals = Text("= 5", font_size=28, color=BLUE)
        equals.next_to(frac, RIGHT, buff=0.3)

        mean_group = VGroup(mean_label, frac, equals)
        mean_group.shift(UP * 0.5)

        self.play(Write(mean_group))
        self.wait(0.5)

        # Show balancing concept
        balance_text = Text("Mean = 5 is the balance point", font_size=20, color=PURPLE)
        balance_text.to_edge(DOWN)
        self.play(Write(balance_text))
        self.wait(0.3)

        # Highlight mean on number line
        mean_dot = Dot(color=RED, radius=0.15)
        mean_x = LEFT * 3.0 + RIGHT * 5 * 0.8
        mean_dot.move_to(mean_x + UP * 0.3)
        self.play(FadeIn(mean_dot))
        mean_label2 = Text("Mean", font_size=14, color=RED)
        mean_label2.next_to(mean_dot, UP, buff=0.05)
        self.play(Write(mean_label2))
        self.wait(2)
