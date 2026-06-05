from manim import *
import math

class CompFunc(Scene):
    def construct(self):
        title = Text("Composite Functions", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        f_text = Text("f(x) = x + 3", font_size=30, color=BLUE)
        f_text.shift(LEFT*3 + UP*1)
        g_text = Text("g(x) = 2x", font_size=30, color=GREEN)
        g_text.shift(LEFT*3 + DOWN*1)
        
        self.play(Write(f_text), Write(g_text))
        
        arrow1 = Arrow(LEFT*1, RIGHT*1, color=YELLOW)
        arrow1.next_to(g_text, RIGHT)
        
        fg_label = Text("f(g(x))", font_size=32, color=ORANGE)
        fg_label.shift(RIGHT*3)
        
        self.play(Create(arrow1), Write(fg_label))
        
        expr = Text("f(g(x)) = f(2x) = 2x + 3", font_size=28, color=YELLOW)
        expr.next_to(fg_label, DOWN)
        self.play(Write(expr))
        
        note = Text("Apply g first, then f", font_size=24, color=GREY)
        note.to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(2)
