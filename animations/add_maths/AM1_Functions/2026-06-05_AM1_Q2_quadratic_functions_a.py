from manim import *
import math

class CompSquare(Scene):
    def construct(self):
        title = Text("Completing the Square", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq = Text("x^2 + 6x + 5 = ?", font_size=32)
        eq.shift(UP*1)
        self.play(Write(eq))
        
        s1 = Text("Step 1: Half of 6 is 3", font_size=26)
        s1.next_to(eq, DOWN, buff=0.5)
        self.play(Write(s1))
        
        s2 = Text("Step 2: Write (x + 3)^2 - 9 + 5", font_size=26)
        s2.next_to(s1, DOWN, buff=0.3)
        self.play(Write(s2))
        
        s3 = Text("Step 3: Simplify: (x + 3)^2 - 4", font_size=26, color=YELLOW)
        s3.next_to(s2, DOWN, buff=0.3)
        self.play(Write(s3))
        
        vertex_info = Text("Vertex at (-3, -4)", font_size=28, color=GREEN)
        vertex_info.next_to(s3, DOWN, buff=0.5)
        self.play(Write(vertex_info))
        
        self.wait(2)
