from manim import *
import math

class LogRealWorld(Scene):
    def construct(self):
        title = Text("Real-World Logarithms", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Earthquake: M = log(I/I_0)", font_size=28, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        ex2 = Text("If I = 1000 x I_0:", font_size=26)
        ex2.next_to(ex, DOWN)
        self.play(Write(ex2))
        
        ex3 = Text("M = log(1000) = 3", font_size=28, color=GREEN)
        ex3.next_to(ex2, DOWN)
        self.play(Write(ex3))
        
        ex4 = Text("pH = -log[H+]", font_size=28, color=YELLOW)
        ex4.next_to(ex3, DOWN)
        self.play(Write(ex4))
        
        ex5 = Text("If [H+] = 10^{-5}, pH = 5", font_size=26, color=GREEN)
        ex5.next_to(ex4, DOWN)
        self.play(Write(ex5))
        
        self.wait(2)
