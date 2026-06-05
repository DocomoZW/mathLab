from manim import *
import math

class SurdRationalise(Scene):
    def construct(self):
        title = Text("Rationalising Surds", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        expr = Text("Simplify: 1/(sqrt(2))", font_size=32, color=YELLOW)
        expr.shift(UP*1)
        self.play(Write(expr))
        
        step1 = Text("Multiply by sqrt(2)/sqrt(2):", font_size=28)
        step1.next_to(expr, DOWN)
        self.play(Write(step1))
        
        step2 = Text("= sqrt(2) / (sqrt(2)*sqrt(2))", font_size=28)
        step2.next_to(step1, DOWN)
        self.play(Write(step2))
        
        step3 = Text("= sqrt(2) / 2", font_size=32, color=GREEN)
        step3.next_to(step2, DOWN)
        self.play(Write(step3))
        
        rule = Text("Multiply top and bottom by the surd", font_size=24, color=BLUE)
        rule.to_edge(DOWN)
        self.play(Write(rule))
        self.wait(2)
