from manim import *
import math

class ChangeBaseExample(Scene):
    def construct(self):
        title = Text("Change of Base: Example", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Evaluate: log_5 100", font_size=30, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        formula = Text("log_5 100 = ln 100 / ln 5", font_size=26)
        formula.next_to(ex, DOWN)
        self.play(Write(formula))
        
        calc = Text("= 4.605 / 1.609", font_size=26)
        calc.next_to(formula, DOWN)
        self.play(Write(calc))
        
        result = Text("= 2.86 (3 s.f.)", font_size=28, color=GREEN)
        result.next_to(calc, DOWN)
        self.play(Write(result))
        
        tip = Text("Always use ln or log_10 for calculator", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
