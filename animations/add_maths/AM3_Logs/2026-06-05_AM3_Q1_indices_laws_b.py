from manim import *
import math

class IndicesPowerLaw(Scene):
    def construct(self):
        title = Text("Power of a Power", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("(3^2)^4 = ?", font_size=32, color=YELLOW)
        eq.shift(UP*0.5)
        self.play(Write(eq))
        
        expand = Text("= 3^2 x 3^2 x 3^2 x 3^2", font_size=26)
        expand.next_to(eq, DOWN)
        self.play(Write(expand))
        
        add = Text("= 3^(2+2+2+2) = 3^8", font_size=26)
        add.next_to(expand, DOWN)
        self.play(Write(add))
        
        result = Text("= 6561", font_size=28, color=GREEN)
        result.next_to(add, DOWN)
        self.play(Write(result))
        
        law = Text("Rule: (a^m)^n = a^(m*n)", font_size=28, color=BLUE)
        law.to_edge(DOWN)
        self.play(Write(law))
        self.wait(2)
