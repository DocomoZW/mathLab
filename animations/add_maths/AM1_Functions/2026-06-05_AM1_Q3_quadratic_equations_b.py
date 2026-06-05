from manim import *
import math

class FactorisationMethod(Scene):
    def construct(self):
        title = Text("Solving by Factorisation", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("x^2 - 5x + 6 = 0", font_size=32, color=BLUE)
        eq.shift(UP*1.5)
        self.play(Write(eq))
        
        s1 = Text("Find factors of 6 that sum to -5", font_size=26)
        s1.next_to(eq, DOWN, buff=0.5)
        self.play(Write(s1))
        
        factors = Text("(-2) x (-3) = 6  and  (-2)+(-3) = -5", font_size=26)
        factors.next_to(s1, DOWN, buff=0.3)
        self.play(Write(factors))
        
        s2 = Text("Write as (x - 2)(x - 3) = 0", font_size=26, color=YELLOW)
        s2.next_to(factors, DOWN, buff=0.5)
        self.play(Write(s2))
        
        s3 = Text("Therefore x = 2 or x = 3", font_size=28, color=GREEN)
        s3.next_to(s2, DOWN, buff=0.5)
        self.play(Write(s3))
        
        note = Text("If AB = 0 then A = 0 or B = 0", font_size=22, color=GREY)
        note.to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(2)
