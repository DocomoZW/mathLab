from manim import *
import math

class LogEval(Scene):
    def construct(self):
        title = Text("Evaluating Logarithms", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Find: log_3 81", font_size=32, color=YELLOW)
        ex.shift(UP*0.5)
        self.play(Write(ex))
        
        q = Text("What power of 3 gives 81?", font_size=26)
        q.next_to(ex, DOWN)
        self.play(Write(q))
        
        ans = Text("3^4 = 81, so log_3 81 = 4", font_size=28, color=GREEN)
        ans.next_to(q, DOWN)
        self.play(Write(ans))
        
        ex2 = Text("Find: log_5 (1/25)", font_size=32, color=YELLOW)
        ex2.next_to(ans, DOWN)
        self.play(Write(ex2))
        
        ans2 = Text("5^{-2} = 1/25, so log_5 (1/25) = -2", font_size=28, color=GREEN)
        ans2.next_to(ex2, DOWN)
        self.play(Write(ans2))
        
        self.wait(2)
