from manim import *
import math

class SubMethod(Scene):
    def construct(self):
        title = Text("Substitution Method", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        eq1 = Text("y = 2x + 1", font_size=28, color=BLUE)
        eq1.shift(UP*1.5)
        eq2 = Text("y = x^2 - 2x + 3", font_size=28, color=GREEN)
        eq2.next_to(eq1, DOWN, buff=0.2)
        
        self.play(Write(eq1), Write(eq2))
        
        sub = Text("Substitute: 2x + 1 = x^2 - 2x + 3", font_size=26, color=YELLOW)
        sub.next_to(eq2, DOWN, buff=0.5)
        self.play(Write(sub))
        
        rearr = Text("=> x^2 - 4x + 2 = 0", font_size=26, color=ORANGE)
        rearr.next_to(sub, DOWN, buff=0.3)
        self.play(Write(rearr))
        
        sol = Text("=> x = 2 +/- sqrt(2)", font_size=26, color=GREEN)
        sol.next_to(rearr, DOWN, buff=0.3)
        self.play(Write(sol))
        
        y_sol = Text("Substitute back to find y values", font_size=24, color=GREY)
        y_sol.next_to(sol, DOWN, buff=0.5)
        self.play(Write(y_sol))
        
        self.wait(2)
