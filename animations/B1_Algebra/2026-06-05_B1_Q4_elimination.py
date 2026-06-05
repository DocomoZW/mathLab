# topic_id: B1_Q4
# track: igcse_o
# unit: B1_Algebra
# description: Elimination method animated step by step with equation highlighting

from manim import *

class B1Q4EliminationMethod(Scene):
    def construct(self):
        title = Text("Elimination Method", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show the system
        eq1 = Text("3x + 2y = 14", font_size=28, color=YELLOW)
        eq1.shift(UP*1.3)
        eq2 = Text("5x - 2y = 6", font_size=28, color=YELLOW)
        eq2.next_to(eq1, DOWN, buff=0.2)

        self.play(Write(eq1), Write(eq2))
        self.wait(0.3)

        # Highlight the y coefficients: +2y and -2y
        box1 = SurroundingRectangle(eq1[4:7], color=RED, buff=0.05)  # 2y
        box2 = SurroundingRectangle(eq2[4:7], color=RED, buff=0.05)  # -2y
        self.play(Create(box1), Create(box2))
        self.wait(0.3)
        self.play(FadeOut(box1), FadeOut(box2))

        # Show elimination step - ADD the equations
        op_text = Text("Add the equations: y cancels!", font_size=22, color=GREEN)
        op_text.next_to(eq2, DOWN, buff=0.4)
        self.play(Write(op_text))
        self.wait(0.3)

        # Show the adding visually
        plus = Text("+", font_size=28, color=WHITE)
        plus.next_to(eq2, RIGHT, buff=0.5)
        self.play(Write(plus))
        self.wait(0.2)

        # Show 8x = 20
        result_eq = Text("8x = 20", font_size=28, color=GREEN)
        result_eq.next_to(plus, RIGHT, buff=0.5)
        self.play(Write(result_eq))
        self.wait(0.3)

        # Solve for x
        self.play(FadeOut(eq1), FadeOut(eq2), FadeOut(plus), FadeOut(op_text))
        step1 = Text("8x = 20", font_size=28, color=GREEN)
        step1.shift(UP*0.5)
        step2 = Text("x = 20/8 = 2.5", font_size=28, color=YELLOW)
        step2.next_to(step1, DOWN, buff=0.3)

        self.play(Transform(result_eq, step1))
        self.wait(0.3)
        self.play(Write(step2))
        self.wait(0.5)

        # Sub back
        self.play(FadeOut(step1), FadeOut(step2), FadeOut(result_eq))
        sub_text = Text("Substitute x = 2.5 into 3x + 2y = 14", font_size=22, color=WHITE)
        sub_text.shift(UP*1.5)
        self.play(Write(sub_text))
        self.wait(0.3)

        sub_expr = Text("3(2.5) + 2y = 14", font_size=26, color=YELLOW)
        sub_expr.next_to(sub_text, DOWN, buff=0.3)
        self.play(Write(sub_expr))
        self.wait(0.3)

        sub_step1 = Text("7.5 + 2y = 14", font_size=26, color=WHITE)
        sub_step1.next_to(sub_expr, DOWN, buff=0.2)
        self.play(Write(sub_step1))
        self.wait(0.2)

        sub_step2 = Text("2y = 6.5", font_size=26, color=YELLOW)
        sub_step2.next_to(sub_step1, DOWN, buff=0.2)
        self.play(Write(sub_step2))
        self.wait(0.2)

        sub_step3 = Text("y = 3.25", font_size=26, color=GREEN)
        sub_step3.next_to(sub_step2, DOWN, buff=0.2)
        self.play(Write(sub_step3))
        self.wait(0.3)

        # Final answer
        answer = Text("Solution: x = 2.5, y = 3.25", font_size=30, color=GREEN)
        answer.to_edge(DOWN, buff=0.3)
        self.play(Write(answer))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
