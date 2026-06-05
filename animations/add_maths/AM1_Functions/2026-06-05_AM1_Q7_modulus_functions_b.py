from manim import *
import math

class ModulusEq(Scene):
    def construct(self):
        title = Text("Solving |ax + b| = c", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Solve |2x - 3| = 5", font_size=30, color=BLUE)
        ex.shift(UP*2)
        self.play(Write(ex))
        
        c1_label = Text("Case 1: 2x - 3 = 5", font_size=26, color=GREEN)
        c1_label.shift(UP*1)
        self.play(Write(c1_label))
        
        c1_sol = Text("2x = 8 => x = 4", font_size=26)
        c1_sol.next_to(c1_label, DOWN, buff=0.2)
        self.play(Write(c1_sol))
        
        c2_label = Text("Case 2: 2x - 3 = -5", font_size=26, color=ORANGE)
        c2_label.next_to(c1_sol, DOWN, buff=0.4)
        self.play(Write(c2_label))
        
        c2_sol = Text("2x = -2 => x = -1", font_size=26)
        c2_sol.next_to(c2_label, DOWN, buff=0.2)
        self.play(Write(c2_sol))
        
        answer = Text("Answer: x = 4 or x = -1", font_size=28, color=YELLOW)
        answer.next_to(c2_sol, DOWN, buff=0.5)
        self.play(Write(answer))
        
        note = Text("Always verify solutions in original equation!", font_size=22, color=GREY)
        note.to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(2)
