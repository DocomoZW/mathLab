from manim import *
import math

class ExponentialEquations(Scene):
    def construct(self):
        title = Text("Exponential Equations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("Solve: 2^x = 7", font_size=32, color=YELLOW)
        eq.shift(UP*0.5)
        self.play(Write(eq))
        
        step1 = Text("Take logs: ln(2^x) = ln(7)", font_size=26)
        step1.next_to(eq, DOWN)
        self.play(Write(step1))
        
        step2 = Text("x ln(2) = ln(7)", font_size=26)
        step2.next_to(step1, DOWN)
        self.play(Write(step2))
        
        step3 = Text("x = ln(7)/ln(2) = 2.81", font_size=28, color=GREEN)
        step3.next_to(step2, DOWN)
        self.play(Write(step3))
        
        tip = Text("Method: take logs of both sides", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
