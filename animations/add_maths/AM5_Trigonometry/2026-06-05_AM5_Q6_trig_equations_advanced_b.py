from manim import *
import math

class MultipleAngle(Scene):
    def construct(self):
        title = Text("Multiple Angle Equations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Solve cos 2x = 1/2 for 0 <= x <= 360", font_size=24, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        s1 = Text("2x = 60, 300, 420, 660 degrees", font_size=24)
        s1.next_to(ex, DOWN)
        self.play(Write(s1))
        
        s2 = Text("x = 30, 150, 210, 330 degrees", font_size=26, color=GREEN)
        s2.next_to(s1, DOWN)
        self.play(Write(s2))
        
        note = Text("Solve for the angle first, then divide", font_size=24, color=BLUE)
        note.next_to(s2, DOWN)
        self.play(Write(note))
        
        note2 = Text("Remember to adjust the range!", font_size=22, color=ORANGE)
        note2.next_to(note, DOWN)
        self.play(Write(note2))
        
        self.wait(2)
