from manim import *
import math

class G1Q1ProbabilityScale(Scene):
    def construct(self):
        # Title
        title = Text("Probability Scale", font_size=28, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Draw a number line from 0 to 1
        line = Line(LEFT * 3, RIGHT * 3, color=WHITE)
        line.shift(DOWN * 0.5)
        self.play(Create(line))

        # Tick marks at 0, 0.25, 0.5, 0.75, 1
        ticks_pos = [-3, -1.5, 0, 1.5, 3]
        labels_text = ["0", "0.25", "0.5", "0.75", "1"]
        labels_prob = ["Impossible", "Unlikely", "Even", "Likely", "Certain"]

        ticks = VGroup()
        tick_labels = VGroup()
        prob_labels = VGroup()

        for i, pos in enumerate(ticks_pos):
            tick = Line(
                start=[pos, -0.5 - 0.15, 0],
                end=[pos, -0.5 + 0.15, 0],
                color=WHITE
            )
            ticks.add(tick)
            label = Text(labels_text[i], font_size=20, color=WHITE)
            label.next_to(tick, DOWN * 0.3)
            tick_labels.add(label)
            prob = Text(labels_prob[i], font_size=16, color=BLUE)
            prob.next_to(tick, UP * 0.3)
            prob_labels.add(prob)

        self.play(Create(ticks), Write(tick_labels))
        self.wait(1)
        self.play(Write(prob_labels))
        self.wait(2)
        self.play(FadeOut(title), FadeOut(line), FadeOut(ticks), FadeOut(tick_labels), FadeOut(prob_labels))
