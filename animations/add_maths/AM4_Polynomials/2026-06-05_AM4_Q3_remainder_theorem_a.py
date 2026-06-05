from manim import *
import math

class RemainderTheorem(Scene):
    def construct(self):
        title = Text("Remainder Theorem", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        theorem = Text("When f(x) / (x-a), remainder = f(a)", font_size=28, color=YELLOW)
        theorem.shift(UP*1)
        self.play(Write(theorem))
        
        ex = Text("f(x) = 2x^3 - 3x^2 + 5x - 7", font_size=26)
        ex.next_to(theorem, DOWN)
        self.play(Write(ex))
        
        calc = Text("f(2) = 16 - 12 + 10 - 7 = 7", font_size=26, color=GREEN)
        calc.next_to(ex, DOWN)
        self.play(Write(calc))
        
        result = Text("Remainder when divided by (x-2) is 7", font_size=26, color=ORANGE)
        result.next_to(calc, DOWN)
        self.play(Write(result))
        
        tip = Text("Much faster than long division!", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
