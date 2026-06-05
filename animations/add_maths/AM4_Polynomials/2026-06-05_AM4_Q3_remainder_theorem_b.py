from manim import *
import math

class RemainderExample(Scene):
    def construct(self):
        title = Text("Remainder Theorem in Action", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Find remainder: 2x^3-3x^2+4x-5 divided by 2x-1", font_size=22, color=YELLOW)
        ex.shift(UP*0.5)
        self.play(Write(ex))
        
        rule = Text("For divisor (ax-b), remainder = f(b/a)", font_size=24)
        rule.next_to(ex, DOWN)
        self.play(Write(rule))
        
        calc = Text("f(1/2) = 2(1/8) - 3(1/4) + 4(1/2) - 5", font_size=22)
        calc.next_to(rule, DOWN)
        self.play(Write(calc))
        
        calc2 = Text("= 0.25 - 0.75 + 2 - 5 = -3.5", font_size=24, color=GREEN)
        calc2.next_to(calc, DOWN)
        self.play(Write(calc2))
        
        result = Text("Remainder = -3.5", font_size=28, color=ORANGE)
        result.next_to(calc2, DOWN)
        self.play(Write(result))
        
        self.wait(2)
