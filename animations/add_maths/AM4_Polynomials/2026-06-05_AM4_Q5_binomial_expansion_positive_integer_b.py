from manim import *
import math

class PascalsTriangle(Scene):
    def construct(self):
        title = Text("Pascal's Triangle", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        rows = [
            "1",
            "1  1",
            "1  2  1",
            "1  3  3  1",
            "1  4  6  4  1",
            "1  5  10  10  5  1"
        ]
        texts = []
        for i, row in enumerate(rows):
            t = Text(row, font_size=22, color=YELLOW)
            t.shift(UP*2.5 - i*0.6*DOWN)
            texts.append(t)
        
        for t in texts:
            self.play(Write(t), run_time=0.3)
        
        note = Text("Each number is sum of two above", font_size=24, color=BLUE)
        note.to_edge(DOWN)
        self.play(Write(note))
        
        note2 = Text("Used for binomial coefficients", font_size=24, color=GREEN)
        note2.next_to(note, UP)
        self.play(Write(note2))
        self.wait(2)
