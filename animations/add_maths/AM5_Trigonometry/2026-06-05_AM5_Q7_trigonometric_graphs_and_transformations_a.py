from manim import *
import math

class TrigGraphs(Scene):
    def construct(self):
        title = Text("Trigonometric Graphs", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        form = Text("y = a sin(bx + c) + d", font_size=28, color=YELLOW)
        form.shift(UP*1)
        self.play(Write(form))
        
        a_text = Text("a: amplitude (vertical stretch)", font_size=24)
        a_text.next_to(form, DOWN)
        self.play(Write(a_text))
        
        b_text = Text("b: frequency (period = 2pi/b)", font_size=24)
        b_text.next_to(a_text, DOWN)
        self.play(Write(b_text))
        
        c_text = Text("c: phase shift (horizontal)", font_size=24)
        c_text.next_to(b_text, DOWN)
        self.play(Write(c_text))
        
        d_text = Text("d: vertical shift", font_size=24)
        d_text.next_to(c_text, DOWN)
        self.play(Write(d_text))
        
        ex = Text("y=3 sin(2x)+1: A=3, T=pi, range=[-2,4]", font_size=24, color=GREEN)
        ex.next_to(d_text, DOWN)
        self.play(Write(ex))
        
        self.wait(2)
