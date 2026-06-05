from manim import *
import math

class LogLawsExample(Scene):
    def construct(self):
        title = Text("Log Laws in Action", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Simplify: log_2 8 + log_2 16 - log_2 4", font_size=26, color=YELLOW)
        ex.shift(UP*0.5)
        self.play(Write(ex))
        
        s1 = Text("= log_2(8 x 16 / 4)", font_size=26)
        s1.next_to(ex, DOWN)
        self.play(Write(s1))
        
        s2 = Text("= log_2(32)", font_size=26)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("= log_2(2^5) = 5", font_size=28, color=GREEN)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        note = Text("Product, quotient, then evaluate", font_size=24, color=BLUE)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
