# topic_id: B1_Q6
# track: igcse_o
# unit: B1_Algebra
# description: Quadratic sequence dot patterns showing n^2 growth

from manim import *

class B1Q6QuadraticSequence(Scene):
    def construct(self):
        title = Text("Quadratic Sequences: Dot Patterns", font_size=28, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show sequence: 2, 6, 12, 20
        seq_text = Text("2, 6, 12, 20, ...", font_size=32, color=WHITE)
        seq_text.shift(UP*1.8)
        self.play(Write(seq_text))
        self.wait(0.3)

        # Show first differences
        diffs = Text("First diffs: 4, 6, 8, ...", font_size=22, color=YELLOW)
        diffs.shift(UP*1.0)
        self.play(Write(diffs))
        self.wait(0.3)

        # Show second difference
        second_diff = Text("Second diff: 2 (constant! => quadratic)", font_size=22, color=RED)
        second_diff.next_to(diffs, DOWN, buff=0.2)
        self.play(Write(second_diff))
        self.wait(0.4)

        # Build square patterns to show n^2
        sq1 = Square(side_length=0.5, color=GREEN, fill_opacity=0.4)
        sq1.shift(LEFT*3.5 + DOWN*1)
        sq1_label = Text("1", font_size=14)
        sq1_label.move_to(sq1.get_center())
        self.play(Create(sq1), Write(sq1_label))
        self.wait(0.15)

        # n=2: 2x2 grid = 4 squares
        sq2_group = VGroup()
        for r in range(2):
            for c in range(2):
                s = Square(side_length=0.4, color=GREEN, fill_opacity=0.4)
                s.move_to(LEFT*2 + RIGHT*c*0.45 + UP*(1-r)*0.45)
                sq2_group.add(s)
        sq2_group.shift(DOWN*1)
        sq2_label = Text("4", font_size=14)
        sq2_label.move_to(sq2_group.get_center())
        self.play(Create(sq2_group), Write(sq2_label))
        self.wait(0.15)

        # n=3: 3x3 grid = 9
        sq3_group = VGroup()
        for r in range(3):
            for c in range(3):
                s = Square(side_length=0.35, color=GREEN, fill_opacity=0.4)
                s.move_to(RIGHT*0.3 + RIGHT*c*0.4 + UP*(1-r)*0.4)
                sq3_group.add(s)
        sq3_group.shift(DOWN*1)
        sq3_label = Text("9", font_size=14)
        sq3_label.move_to(sq3_group.get_center())
        self.play(Create(sq3_group), Write(sq3_label))
        self.wait(0.15)

        # n=4: 4x4 grid = 16
        sq4_group = VGroup()
        for r in range(4):
            for c in range(4):
                s = Square(side_length=0.3, color=GREEN, fill_opacity=0.4)
                s.move_to(RIGHT*2.2 + RIGHT*c*0.35 + UP*(1.5-r)*0.35)
                sq4_group.add(s)
        sq4_group.shift(DOWN*1)
        sq4_label = Text("16", font_size=14)
        sq4_label.move_to(sq4_group.get_center())
        self.play(Create(sq4_group), Write(sq4_label))
        self.wait(0.4)

        # Formula
        formula = Text("u_n = n^2 + n", font_size=28, color=GREEN)
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(0.3)

        check = Text("Check:  n=1: 1+1=2,  n=2: 4+2=6,  n=3: 9+3=12", font_size=18, color=WHITE)
        check.next_to(formula, DOWN, buff=0.2)
        self.play(Write(check))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
