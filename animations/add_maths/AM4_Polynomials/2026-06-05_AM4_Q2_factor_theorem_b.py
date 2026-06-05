from manim import *
import math

class FactoriseCubic(Scene):
    def construct(self):
        title = Text("Factorising a Cubic", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("f(x) = x^3 + 2x^2 - 5x - 6", font_size=26, color=YELLOW)
        ex.shift(UP*0.5)
        self.play(Write(ex))
        
        test = Text("Test x=-1: -1+2+5-6=0 => (x+1) factor", font_size=24)
        test.next_to(ex, DOWN)
        self.play(Write(test))
        
        div = Text("Divide: f(x)/(x+1) = x^2+x-6", font_size=24)
        div.next_to(test, DOWN)
        self.play(Write(div))
        
        factor = Text("x^2+x-6 = (x+3)(x-2)", font_size=26)
        factor.next_to(div, DOWN)
        self.play(Write(factor))
        
        result = Text("f(x) = (x+1)(x+3)(x-2)", font_size=26, color=GREEN)
        result.next_to(factor, DOWN)
        self.play(Write(result))
        
        self.wait(2)
