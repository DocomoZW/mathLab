from manim import *
import math

class ChangeOfBase(Scene):
    def construct(self):
        title = Text("Change of Base Formula", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        formula = Text("log_a b = log_c b / log_c a", font_size=30, color=YELLOW)
        formula.shift(UP*1)
        self.play(Write(formula))
        
        ex = Text("Example: log_2 10", font_size=28)
        ex.next_to(formula, DOWN)
        self.play(Write(ex))
        
        ex2 = Text("= ln(10) / ln(2) = 3.32", font_size=28, color=GREEN)
        ex2.next_to(ex, DOWN)
        self.play(Write(ex2))
        
        tip = Text("Use base 10 or e for calculator work", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
