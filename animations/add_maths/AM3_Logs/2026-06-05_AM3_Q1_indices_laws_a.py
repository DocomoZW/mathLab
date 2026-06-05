from manim import *
import math

class IndicesLaws(Scene):
    def construct(self):
        title = Text("Indices: Multiplication Law", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Show 2^3 * 2^4
        eq1 = Text("2^3 x 2^4 = ?", font_size=32, color=YELLOW)
        eq1.shift(UP*0.5)
        self.play(Write(eq1))
        
        # Expand
        expand = Text("= (2x2x2) x (2x2x2x2)", font_size=28)
        expand.next_to(eq1, DOWN)
        self.play(Write(expand))
        
        # Count
        result = Text("= 2^7 = 128", font_size=32, color=GREEN)
        result.next_to(expand, DOWN)
        self.play(Write(result))
        
        # Law
        law = Text("Rule: a^m x a^n = a^(m+n)", font_size=28, color=BLUE)
        law.to_edge(DOWN)
        self.play(Write(law))
        self.wait(2)
