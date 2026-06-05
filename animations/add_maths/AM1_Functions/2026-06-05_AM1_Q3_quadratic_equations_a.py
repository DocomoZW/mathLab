from manim import *
import math

class QuadFormula(Scene):
    def construct(self):
        title = Text("Quadratic Formula", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        gen = Text("ax^2 + bx + c = 0", font_size=32)
        gen.shift(UP*1)
        self.play(Write(gen))
        
        formula = Text("x = [ -b +/- sqrt(b^2 - 4ac) ] / (2a)", font_size=28, color=YELLOW)
        formula.next_to(gen, DOWN, buff=0.8)
        self.play(Write(formula))
        
        ex_label = Text("Example: 2x^2 - 7x + 3 = 0", font_size=28, color=BLUE)
        ex_label.next_to(formula, DOWN, buff=0.8)
        self.play(Write(ex_label))
        
        s1 = Text("a = 2, b = -7, c = 3", font_size=24)
        s1.next_to(ex_label, DOWN, buff=0.4)
        self.play(Write(s1))
        
        s2 = Text("x = [7 +/- sqrt(49 - 24)] / 4", font_size=24)
        s2.next_to(s1, DOWN, buff=0.3)
        self.play(Write(s2))
        
        s3 = Text("x = [7 +/- 5] / 4", font_size=24, color=ORANGE)
        s3.next_to(s2, DOWN, buff=0.3)
        self.play(Write(s3))
        
        s4 = Text("x = 3  or  x = 1/2", font_size=28, color=GREEN)
        s4.next_to(s3, DOWN, buff=0.4)
        self.play(Write(s4))
        
        self.wait(2)
