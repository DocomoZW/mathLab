from manim import *
import math

class ArithmeticVisual(Scene):
    def construct(self):
        title = Text("Arithmetic Progression", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show terms
        terms_data = [("a", 0), ("a+d", 1), ("a+2d", 2), ("a+3d", 3), ("a+4d", 4)]
        
        bars = []
        for i, (label, idx) in enumerate(terms_data):
            bar_height = 0.3 + idx * 0.2
            bar = Rectangle(width=0.5, height=bar_height, color=BLUE, fill_opacity=0.6)
            bar.move_to(np.array([i * 1.2 - 2.4, bar_height / 2 - 1.5, 0]), aligned_edge=DOWN)
            bars.append(bar)
            self.play(Create(bar), run_time=0.2)
            
            term_label = Text(label, font_size=18)
            term_label.next_to(bar, DOWN, buff=0.1)
            self.play(Write(term_label), run_time=0.1)
        
        self.wait(0.5)
        
        # Show constant difference
        gap_label = Text("Common difference d is constant", font_size=22, color=YELLOW)
        gap_label.next_to(bars[-1], UP, buff=0.5)
        self.play(Write(gap_label))
        self.wait(1)
        
        # Formulas
        nth = Text("nth term: u_n = a + (n-1)d", font_size=24)
        nth.next_to(gap_label, UP, buff=0.3)
        self.play(Write(nth))
        
        sum_formula = Text("Sum: S_n = n/2 [2a + (n-1)d]", font_size=24)
        sum_formula.next_to(nth, UP, buff=0.3)
        self.play(Write(sum_formula))
        self.wait(2)


class GeometricVisual(Scene):
    def construct(self):
        title = Text("Geometric Progression", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show geometric sequence
        seq_label = Text("Sequence: a, ar, ar^2, ar^3, ...", font_size=26)
        seq_label.next_to(title, DOWN, buff=0.5)
        self.play(Write(seq_label))
        self.wait(0.5)
        
        # Growth illustration
        values = [0.3, 0.6, 1.2, 2.4, 4.8]
        bars = []
        for i, h in enumerate(values):
            bar = Rectangle(width=0.5, height=h, color=GREEN, fill_opacity=0.6)
            bar.move_to(np.array([i * 1.2 - 2.4, h / 2 - 1, 0]), aligned_edge=DOWN)
            bars.append(bar)
            self.play(Create(bar), run_time=0.2)
            
            val = Text(f"x^{i}", font_size=16)
            val.next_to(bar, DOWN, buff=0.1)
            self.play(Write(val), run_time=0.1)
        
        self.wait(0.5)
        
        # Ratio label
        ratio_label = Text("Common ratio r is constant", font_size=22, color=YELLOW)
        ratio_label.next_to(bars[-1], UP, buff=0.5)
        self.play(Write(ratio_label))
        self.wait(1)
        
        # Formulas
        nth = Text("nth term: u_n = ar^(n-1)", font_size=24)
        nth.next_to(ratio_label, UP, buff=0.3)
        self.play(Write(nth))
        
        sum_n = Text("Sum: S_n = a(1-r^n)/(1-r)", font_size=24)
        sum_n.next_to(nth, UP, buff=0.3)
        self.play(Write(sum_n))
        
        sum_inf = Text("Sum to infinity: S = a/(1-r)  (|r|<1)", font_size=24, color=YELLOW)
        sum_inf.next_to(sum_n, UP, buff=0.3)
        self.play(Write(sum_inf))
        self.wait(2)
