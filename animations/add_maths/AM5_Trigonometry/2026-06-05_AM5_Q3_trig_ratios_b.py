from manim import *
import math

class ExactValues(Scene):
    def construct(self):
        title = Text("Exact Trig Values", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        vals = [
            "sin 0 = 0",
            "sin 30 = 1/2",
            "sin 45 = 1/sqrt2",
            "sin 60 = sqrt3/2",
            "sin 90 = 1",
            "",
            "cos 0 = 1",
            "cos 30 = sqrt3/2",
            "cos 45 = 1/sqrt2",
            "cos 60 = 1/2",
            "cos 90 = 0"
        ]
        left_col = []
        right_col = []
        for i, v in enumerate(vals):
            if i < 5:
                left_col.append(v)
            elif i > 5:
                right_col.append(v)
        
        for i, v in enumerate(left_col):
            if v:
                t = Text(v, font_size=22, color=YELLOW)
                t.shift(LEFT*3 + UP*2.5 - i*0.7*DOWN)
                self.play(Write(t), run_time=0.2)
        
        for i, v in enumerate(right_col):
            if v:
                t = Text(v, font_size=22, color=BLUE)
                t.shift(RIGHT*3 + UP*2.5 - i*0.7*DOWN)
                self.play(Write(t), run_time=0.2)
        
        note = Text("Memorise these for non-calculator exams", font_size=22, color=GREEN)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
