from manim import *
import math

class PascalsTriangle(Scene):
    def construct(self):
        title = Text("Pascal's Triangle", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Build Pascal's triangle
        rows_data = [
            ["1"],
            ["1", "1"],
            ["1", "2", "1"],
            ["1", "3", "3", "1"],
            ["1", "4", "6", "4", "1"],
            ["1", "5", "10", "10", "5", "1"]
        ]
        
        all_texts = []
        for i, row in enumerate(rows_data):
            row_texts = []
            for j, num in enumerate(row):
                t = Text(num, font_size=24)
                x_pos = (j - i / 2) * 0.7
                y_pos = -i * 0.5
                t.move_to(np.array([x_pos, y_pos + 1.5, 0]))
                row_texts.append(t)
                self.play(FadeIn(t, scale=0.5), run_time=0.1)
            
            all_texts.append(row_texts)
        
        self.wait(1)
        
        # Label for coefficients
        label = Text("Binomial coefficients (a+b)^n", font_size=24, color=YELLOW)
        label.next_to(all_texts[-1][2], DOWN, buff=0.5)
        self.play(Write(label))
        self.wait(2)
        
        # Highlight a row
        for t in all_texts[4]:
            self.play(t.animate.set_color(YELLOW), run_time=0.1)
        
        n_label = Text("Row n = 4: (a+b)^4", font_size=22, color=YELLOW)
        n_label.next_to(label, DOWN, buff=0.3)
        self.play(Write(n_label))
        self.wait(2)


class BinomialTerm(Scene):
    def construct(self):
        title = Text("Binomial Theorem", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        formula = Text("(a + b)^n = Sum C(n,r) a^(n-r) b^r", font_size=28)
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula))
        self.wait(1)
        
        coeff = Text("C(n,r) = n! / (r!(n-r)!)", font_size=26)
        coeff.next_to(formula, DOWN, buff=0.3)
        self.play(Write(coeff))
        self.wait(1)
        
        # Example
        example = Text("Example: Find term in x^2 in (3+x)^6", font_size=24)
        example.next_to(coeff, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        step1 = Text("r = 2 (need x^2, so r=2)", font_size=22)
        step1.next_to(example, DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(0.5)
        
        step2 = Text("Term = C(6,2) * 3^(4) * x^2", font_size=22)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.5)
        
        step3 = Text("= 15 * 81 * x^2 = 1215 x^2", font_size=22, color=YELLOW)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(2)
