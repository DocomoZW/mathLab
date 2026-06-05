from manim import *
import math

class G1Q1SingleEvent(Scene):
    def construct(self):
        title = Text("Single Event Probability", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Draw a spinner (circle divided into 4 equal parts)
        center = [0, 0, 0]
        radius = 1.2
        spinner = Circle(radius=radius, color=WHITE)
        self.play(Create(spinner))

        # Draw lines dividing into 4 quarters
        line_h = Line(
            start=[-radius, 0, 0],
            end=[radius, 0, 0],
            color=WHITE
        )
        line_v = Line(
            start=[0, -radius, 0],
            end=[0, radius, 0],
            color=WHITE
        )
        self.play(Create(line_h), Create(line_v))

        # Label each section
        label_r = Text("Red", font_size=18, color=RED)
        label_r.shift([radius * 0.5, radius * 0.5, 0])
        label_b = Text("Blue", font_size=18, color=BLUE)
        label_b.shift([-radius * 0.5, radius * 0.5, 0])
        label_g = Text("Green", font_size=18, color=GREEN)
        label_g.shift([-radius * 0.5, -radius * 0.5, 0])
        label_y = Text("Yellow", font_size=18, color=YELLOW)
        label_y.shift([radius * 0.5, -radius * 0.5, 0])

        self.play(Write(label_r), Write(label_b), Write(label_g), Write(label_y))
        self.wait(1)

        # Text showing probability of Red
        formula = Text("P(Red) = 1 / 4", font_size=24, color=RED)
        formula.next_to(spinner, DOWN * 2)
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(spinner), FadeOut(line_h), FadeOut(line_v),
                  FadeOut(label_r), FadeOut(label_b), FadeOut(label_g), FadeOut(label_y), FadeOut(formula))
