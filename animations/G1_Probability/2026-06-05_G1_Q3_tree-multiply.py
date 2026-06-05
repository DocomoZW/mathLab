from manim import *
import math

class G1Q3TreeMultiply(Scene):
    def construct(self):
        title = Text("Multiplying Along Branches", font_size=22, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Simple tree: two independent events (drawing marbles with replacement)
        # Bag has 3 Red, 2 Blue marbles
        # First draw
        root = Dot([-3, 0, 0], color=WHITE)
        root_label = Text("Start", font_size=16, color=WHITE)
        root_label.next_to(root, LEFT * 0.3)
        self.play(Create(root), Write(root_label))

        # Branches for first draw
        line_r1 = Line(start=[-3, 0, 0], end=[-1, 1.2, 0], color=RED)
        prob_r1 = Text("3/5", font_size=18, color=RED)
        prob_r1.shift([-2, 0.7, 0])
        label_r1 = Text("R", font_size=20, color=RED)
        label_r1.shift([-2, 1.0, 0])

        line_b1 = Line(start=[-3, 0, 0], end=[-1, -1.2, 0], color=BLUE)
        prob_b1 = Text("2/5", font_size=18, color=BLUE)
        prob_b1.shift([-2, -0.7, 0])
        label_b1 = Text("B", font_size=20, color=BLUE)
        label_b1.shift([-2, -1.0, 0])

        self.play(Create(line_r1), Write(prob_r1), Write(label_r1))
        self.play(Create(line_b1), Write(prob_b1), Write(label_b1))

        node_r = Dot([-1, 1.2, 0], color=RED)
        node_b = Dot([-1, -1.2, 0], color=BLUE)
        self.play(Create(node_r), Create(node_b))

        # Second draw - from Red node
        line_rr = Line(start=[-1, 1.2, 0], end=[1, 2.2, 0], color=RED)
        prob_rr = Text("3/5", font_size=18, color=PINK)
        prob_rr.shift([0, 1.8, 0])
        label_rr = Text("R", font_size=18, color=PINK)
        label_rr.shift([0, 2.1, 0])

        line_rb = Line(start=[-1, 1.2, 0], end=[1, 0.2, 0], color=BLUE)
        prob_rb = Text("2/5", font_size=18, color=PINK)
        prob_rb.shift([0, 0.8, 0])
        label_rb = Text("B", font_size=18, color=BLUE)
        label_rb.shift([0, 1.1, 0])

        # Second draw - from Blue node (with replacement, same probs)
        line_br = Line(start=[-1, -1.2, 0], end=[1, -0.2, 0], color=RED)
        prob_br = Text("3/5", font_size=18, color=PINK)
        prob_br.shift([0, -0.2, 0])
        label_br = Text("R", font_size=18, color=RED)
        label_br.shift([0, 0.1, 0])

        line_bb = Line(start=[-1, -1.2, 0], end=[1, -2.2, 0], color=BLUE)
        prob_bb = Text("2/5", font_size=18, color=PINK)
        prob_bb.shift([0, -1.8, 0])
        label_bb = Text("B", font_size=18, color=BLUE)
        label_bb.shift([0, -2.1, 0])

        self.play(Create(line_rr), Write(prob_rr), Write(label_rr))
        self.play(Create(line_rb), Write(prob_rb), Write(label_rb))
        self.play(Create(line_br), Write(prob_br), Write(label_br))
        self.play(Create(line_bb), Write(prob_bb), Write(label_bb))

        # Outcome probabilities
        outcome_probs = ["9/25", "6/25", "6/25", "4/25"]
        positions = [[1.5, 2.2, 0], [1.5, 0.2, 0], [1.5, -0.2, 0], [1.5, -2.2, 0]]
        outcome_group = VGroup()
        for i, (prob, pos) in enumerate(zip(outcome_probs, positions)):
            label = Text(prob, font_size=18, color=YELLOW)
            label.shift([pos[0] + 0.8, pos[1], 0])
            outcome_group.add(label)
        self.play(Write(outcome_group))

        # Formula explanation
        explanation = Text("P(R,R) = 3/5 x 3/5 = 9/25", font_size=20, color=YELLOW)
        explanation.shift(DOWN * 1.8)
        self.play(Write(explanation))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(root), FadeOut(root_label),
                  FadeOut(line_r1), FadeOut(prob_r1), FadeOut(label_r1),
                  FadeOut(line_b1), FadeOut(prob_b1), FadeOut(label_b1),
                  FadeOut(node_r), FadeOut(node_b),
                  FadeOut(line_rr), FadeOut(prob_rr), FadeOut(label_rr),
                  FadeOut(line_rb), FadeOut(prob_rb), FadeOut(label_rb),
                  FadeOut(line_br), FadeOut(prob_br), FadeOut(label_br),
                  FadeOut(line_bb), FadeOut(prob_bb), FadeOut(label_bb),
                  FadeOut(outcome_group), FadeOut(explanation))
