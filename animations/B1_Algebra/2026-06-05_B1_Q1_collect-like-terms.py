# topic_id: B1_Q1
# track: igcse_o
# unit: B1_Algebra
# description: Collecting like terms with animated grouping and colour coding

from manim import *

class B1Q1CollectLikeTerms(Scene):
    def construct(self):
        title = Text("Collecting Like Terms", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show expression: 3x + 5y - 2x + 7y
        expr = Text("3x + 5y - 2x + 7y", font_size=36, color=WHITE)
        expr.shift(UP*1.5)
        self.play(Write(expr))
        self.wait(0.5)

        # Draw coloured boxes around like terms
        # x terms: "3x" and "2x" (but -2x has negative sign)
        box1 = SurroundingRectangle(expr[0:2], color=RED, buff=0.05)  # 3x
        box2 = SurroundingRectangle(expr[9:12], color=RED, buff=0.05)  # 2x (but careful with indexing)

        # Better approach: use Text objects for each term
        self.play(FadeOut(expr))
        term1 = Text("3x", font_size=36, color=RED)
        term2 = Text("+5y", font_size=36, color=GREEN)
        term3 = Text("-2x", font_size=36, color=RED)
        term4 = Text("+7y", font_size=36, color=GREEN)
        terms = VGroup(term1, term2, term3, term4).arrange(RIGHT, buff=0.2)
        terms.shift(UP*1.5)
        self.play(Write(terms))
        self.wait(0.4)

        # Highlight x terms sliding together
        self.play(
            term1.animate.shift(LEFT*1.5),
            term3.animate.shift(RIGHT*1.5),
            term2.animate.shift(RIGHT*3),
            term4.animate.shift(LEFT*3),
        )
        self.wait(0.3)

        # Group x terms and y terms
        x_group = VGroup(term1, term3)
        y_group = VGroup(term2, term4)
        x_box = SurroundingRectangle(x_group, color=RED, buff=0.1)
        y_box = SurroundingRectangle(y_group, color=GREEN, buff=0.1)
        self.play(Create(x_box), Create(y_box))
        self.wait(0.3)

        # Simplify text
        x_label = Text("3x - 2x = x", font_size=30, color=RED)
        x_label.next_to(x_box, DOWN, buff=0.5)
        y_label = Text("5y + 7y = 12y", font_size=30, color=GREEN)
        y_label.next_to(y_box, DOWN, buff=0.5)

        self.play(Write(x_label), Write(y_label))
        self.wait(0.4)

        # Final answer
        result = Text("Answer: x + 12y", font_size=36, color=YELLOW)
        result.to_edge(DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
