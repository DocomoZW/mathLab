from manim import *
import math

class ReduceToLinear(Scene):
    def construct(self):
        title = Text("Linear Law: Reducing to Straight Line", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))

        # Step 1: Show non-linear equation
        eq1 = Text("y = a x^n  (non-linear)", font_size=28, color=BLUE)
        eq1.shift(UP*1.5)
        self.play(Write(eq1))

        # Arrow
        arr = Arrow(LEFT*0.5, RIGHT*0.5, color=YELLOW)
        arr.next_to(eq1, DOWN)
        self.play(Create(arr))

        # Step 2: Take logs
        eq2 = Text("Take logs: log y = log a + n log x", font_size=26, color=GREEN)
        eq2.next_to(arr, DOWN)
        self.play(Write(eq2))

        # Step 3: Identify Y = mX + c
        eq3 = Text("Y = log y,  X = log x,  m = n,  c = log a", font_size=24, color=ORANGE)
        eq3.next_to(eq2, DOWN, buff=0.5)
        self.play(Write(eq3))

        # Step 4: Linear form
        eq4 = Text("Now plot log y against log x => straight line!", font_size=26, color=YELLOW)
        eq4.next_to(eq3, DOWN, buff=0.5)
        self.play(Write(eq4))

        # Second example
        self.wait(0.5)
        eq5 = Text("y = a b^x", font_size=28, color=BLUE)
        eq5.next_to(eq4, DOWN, buff=0.5)
        self.play(Write(eq5))

        eq6 = Text("log y = log a + x log b", font_size=26, color=GREEN)
        eq6.next_to(eq5, DOWN, buff=0.3)
        self.play(Write(eq6))

        eq7 = Text("Plot log y against x => gradient=log b, int=log a", font_size=24, color=ORANGE)
        eq7.next_to(eq6, DOWN, buff=0.3)
        self.play(Write(eq7))

        note = Text("Constants found from gradient and intercept", font_size=24, color=GREY)
        note.to_edge(DOWN)
        self.play(Write(note))

        self.wait(2)
