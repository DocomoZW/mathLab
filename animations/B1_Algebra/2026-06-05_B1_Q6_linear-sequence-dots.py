# topic_id: B1_Q6
# track: igcse_o
# unit: B1_Algebra
# description: Dot patterns showing linear sequence growth

from manim import *

class B1Q6LinearSequenceDots(Scene):
    def construct(self):
        title = Text("Linear Sequences: Dot Patterns", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show sequence: 3, 7, 11, 15
        seq_text = Text("3, 7, 11, 15, ...", font_size=32, color=WHITE)
        seq_text.shift(UP*1.8)
        self.play(Write(seq_text))
        self.wait(0.3)

        # Pattern with dots for n=1, n=2, n=3
        patterns = []
        for n in range(1, 5):
            # Create dots arranged in a row for this term
            num_dots = 4*n - 1  # 3, 7, 11, 15 for n=1,2,3,4
            dots = VGroup()
            for i in range(num_dots):
                dot = Circle(radius=0.15, color=GREEN, fill_opacity=0.8, fill_color=GREEN)
                row = i // 10
                col = i % 10
                dot.move_to(LEFT*4.5 + RIGHT*col*0.4 + DOWN*row*0.4)
                dots.add(dot)
            dots.shift(DOWN*(n-1)*0.6 + RIGHT*0.5)
            patterns.append(dots)

            # Label
            n_label = Text(f"n = {n}: {num_dots} dots", font_size=18, color=YELLOW)
            n_label.next_to(dots, LEFT, buff=0.3)
            n_label.shift(UP*0.15)
            patterns.append(n_label)

        for p in patterns:
            if isinstance(p, VGroup):
                self.play(*[Create(d) for d in p])
            elif isinstance(p, Text):
                self.play(Write(p))
            self.wait(0.2)

        self.wait(0.4)

        # Show common difference
        diff_text = Text("Common difference = 4", font_size=24, color=RED)
        diff_text.shift(DOWN*2 + LEFT*1.5)
        self.play(Write(diff_text))
        self.wait(0.3)

        nth_term = Text("nth term: 4n - 1", font_size=26, color=GREEN)
        nth_term.next_to(diff_text, DOWN, buff=0.2)
        self.play(Write(nth_term))
        self.wait(0.5)

        # Show the 10th term
        term10 = Text("10th term = 4(10) - 1 = 39", font_size=24, color=YELLOW)
        term10.next_to(nth_term, DOWN, buff=0.2)
        self.play(Write(term10))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
