from manim import *
import math

class ExpQuadraticForm(Scene):
    def construct(self):
        title = Text("Quadratic Form Exponential", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("Solve: 3^{2x} - 10(3^x) + 9 = 0", font_size=26, color=YELLOW)
        eq.shift(UP*0.5)
        self.play(Write(eq))
        
        s1 = Text("Let y = 3^x", font_size=26)
        s1.next_to(eq, DOWN)
        self.play(Write(s1))
        
        s2 = Text("y^2 - 10y + 9 = 0", font_size=26)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("(y-1)(y-9) = 0 => y=1 or y=9", font_size=26)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        s4 = Text("3^x = 1 => x=0", font_size=24, color=GREEN)
        s4.next_to(s3, DOWN)
        self.play(Write(s4))
        
        s5 = Text("3^x = 9 => x=2", font_size=24, color=GREEN)
        s5.next_to(s4, DOWN)
        self.play(Write(s5))
        
        self.wait(2)
