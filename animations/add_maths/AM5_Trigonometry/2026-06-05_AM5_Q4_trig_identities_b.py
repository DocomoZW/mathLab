from manim import *
import math

class ProveIdentity(Scene):
    def construct(self):
        title = Text("Proving an Identity", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Prove: (sin A + cos A)^2 = 1 + 2 sin A cos A", font_size=22, color=YELLOW)
        ex.shift(UP*0.5)
        self.play(Write(ex))
        
        s1 = Text("LHS = sin^2 A + cos^2 A + 2 sin A cos A", font_size=24)
        s1.next_to(ex, DOWN)
        self.play(Write(s1))
        
        s2 = Text("= (sin^2 A + cos^2 A) + 2 sin A cos A", font_size=24)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        s3 = Text("= 1 + 2 sin A cos A", font_size=28, color=GREEN)
        s3.next_to(s2, DOWN)
        self.play(Write(s3))
        
        s4 = Text("= RHS (proven)", font_size=28, color=ORANGE)
        s4.next_to(s3, DOWN)
        self.play(Write(s4))
        
        note = Text("Work from one side to match the other", font_size=22, color=BLUE)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
