from manim import *
import math

class G1Q3TreeDiagram(Scene):
    def construct(self):
        title = Text("Tree Diagram", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Root point
        root = Dot([-3.5, 0, 0], color=WHITE)
        root_label = Text("Start", font_size=16, color=WHITE)
        root_label.next_to(root, LEFT * 0.3)
        self.play(Create(root), Write(root_label))

        # First branch level: Toss 1
        # Branch 1: Head
        line_h1 = Line(start=[-3.5, 0, 0], end=[-1.0, 1.5, 0], color=BLUE)
        label_h1 = Text("H", font_size=20, color=BLUE)
        label_h1.shift([-2.2, 0.9, 0])
        prob_h1 = Text("1/2", font_size=16, color=WHITE)
        prob_h1.shift([-2.2, 0.5, 0])
        # Branch 2: Tail
        line_t1 = Line(start=[-3.5, 0, 0], end=[-1.0, -1.5, 0], color=RED)
        label_t1 = Text("T", font_size=20, color=RED)
        label_t1.shift([-2.2, -0.9, 0])
        prob_t1 = Text("1/2", font_size=16, color=WHITE)
        prob_t1.shift([-2.2, -0.5, 0])

        self.play(Create(line_h1), Write(label_h1), Write(prob_h1))
        self.play(Create(line_t1), Write(label_t1), Write(prob_t1))

        # Nodes at end of first branches
        node_h = Dot([-1.0, 1.5, 0], color=BLUE)
        node_t = Dot([-1.0, -1.5, 0], color=RED)
        self.play(Create(node_h), Create(node_t))

        # Second branch level: Toss 2
        # From Head
        line_hh = Line(start=[-1.0, 1.5, 0], end=[1.5, 2.5, 0], color=BLUE)
        label_hh = Text("H", font_size=20, color=BLUE)
        label_hh.shift([0.3, 2.2, 0])
        line_ht = Line(start=[-1.0, 1.5, 0], end=[1.5, 0.5, 0], color=RED)
        label_ht = Text("T", font_size=20, color=RED)
        label_ht.shift([0.3, 1.2, 0])

        # From Tail
        line_th = Line(start=[-1.0, -1.5, 0], end=[1.5, -0.5, 0], color=BLUE)
        label_th = Text("H", font_size=20, color=BLUE)
        label_th.shift([0.3, -0.2, 0])
        line_tt = Line(start=[-1.0, -1.5, 0], end=[1.5, -2.5, 0], color=RED)
        label_tt = Text("T", font_size=20, color=RED)
        label_tt.shift([0.3, -2.2, 0])

        self.play(Create(line_hh), Write(label_hh))
        self.play(Create(line_ht), Write(label_ht))
        self.play(Create(line_th), Write(label_th))
        self.play(Create(line_tt), Write(label_tt))

        # Outcome labels
        outcomes = ["HH", "HT", "TH", "TT"]
        positions = [[1.5, 2.5, 0], [1.5, 0.5, 0], [1.5, -0.5, 0], [1.5, -2.5, 0]]
        outcome_group = VGroup()
        for i, (outcome, pos) in enumerate(zip(outcomes, positions)):
            label = Text(outcome, font_size=18, color=YELLOW)
            label.shift([pos[0] + 0.5, pos[1], 0])
            outcome_group.add(label)
        self.play(Write(outcome_group))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(root), FadeOut(root_label),
                  FadeOut(line_h1), FadeOut(label_h1), FadeOut(prob_h1),
                  FadeOut(line_t1), FadeOut(label_t1), FadeOut(prob_t1),
                  FadeOut(node_h), FadeOut(node_t),
                  FadeOut(line_hh), FadeOut(label_hh),
                  FadeOut(line_ht), FadeOut(label_ht),
                  FadeOut(line_th), FadeOut(label_th),
                  FadeOut(line_tt), FadeOut(label_tt),
                  FadeOut(outcome_group))
