from manim import *
import math

class DiscriminantNature(Scene):
    def construct(self):
        title = Text("The Discriminant", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        formula = Text("Delta = b^2 - 4ac", font_size=32, color=YELLOW)
        formula.shift(UP*0.5)
        self.play(Write(formula))
        
        c1 = Text("Delta > 0 : Two distinct real roots", font_size=26, color=BLUE)
        c1.shift(LEFT*2 + DOWN*1.5)
        c2 = Text("Delta = 0 : One repeated root", font_size=26, color=GREEN)
        c2.next_to(c1, DOWN, buff=0.5, aligned_edge=LEFT)
        c3 = Text("Delta < 0 : No real roots", font_size=26, color=RED)
        c3.next_to(c2, DOWN, buff=0.5, aligned_edge=LEFT)
        
        self.play(Write(c1), Write(c2), Write(c3))
        
        ex = Text("Example: x^2 - 5x + 6", font_size=26)
        ex.next_to(c3, DOWN, buff=0.8)
        self.play(Write(ex))
        
        ex_calc = Text("Delta = 25 - 24 = 1 > 0, Two roots", font_size=26, color=ORANGE)
        ex_calc.next_to(ex, DOWN, buff=0.3)
        self.play(Write(ex_calc))
        
        self.wait(2)
