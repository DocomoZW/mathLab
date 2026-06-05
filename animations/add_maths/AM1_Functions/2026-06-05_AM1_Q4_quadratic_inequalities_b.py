from manim import *
import math

class ParabolaMethod(Scene):
    def construct(self):
        title = Text("Parabola Method for Inequalities", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("y = x^2 - x - 6", font_size=28, color=BLUE)
        ex.shift(UP*2)
        self.play(Write(ex))
        
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*1.5, UP*1.5, color=WHITE)
        y_axis.shift(RIGHT*0.5)
        self.play(Create(x_axis), Create(y_axis))
        
        r1 = Dot(LEFT*1.5 + DOWN*0.5, color=RED, radius=0.08)
        r2 = Dot(RIGHT*2.5 + DOWN*0.5, color=RED, radius=0.08)
        label_r1 = Text("-2", font_size=18)
        label_r1.next_to(r1, DOWN)
        label_r2 = Text("3", font_size=18)
        label_r2.next_to(r2, DOWN)
        
        self.play(Create(r1), Create(r2), Write(label_r1), Write(label_r2))
        
        above = Text("y > 0 (above axis)", font_size=22, color=GREEN)
        above.shift(UP*2.5)
        below = Text("y < 0 (below axis)", font_size=22, color=RED)
        below.shift(DOWN*2.5)
        
        self.play(Write(above), Write(below))
        
        sol = Text("x^2 - x - 6 > 0 where parabola is above x-axis", font_size=22, color=YELLOW)
        sol.to_edge(DOWN)
        self.play(Write(sol))
        
        self.wait(2)
