from manim import *
import math

class NumLineInq(Scene):
    def construct(self):
        title = Text("Number Line Method", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Solve: x^2 - x - 6 > 0", font_size=30, color=BLUE)
        ex.shift(UP*2)
        self.play(Write(ex))
        
        cv = Text("Critical values: x = -2, x = 3", font_size=26)
        cv.next_to(ex, DOWN, buff=0.3)
        self.play(Write(cv))
        
        line = Line(LEFT*4, RIGHT*4, color=WHITE)
        line.shift(DOWN*0.5)
        self.play(Create(line))
        
        tick1 = Line(UP*0.2, DOWN*0.2, color=WHITE)
        tick1.move_to(line.get_left() + RIGHT*2)
        tick2 = Line(UP*0.2, DOWN*0.2, color=WHITE)
        tick2.move_to(line.get_right() + LEFT*2)
        
        self.play(Create(tick1), Create(tick2))
        
        label_m2 = Text("-2", font_size=22)
        label_m2.next_to(tick1, DOWN)
        label_3 = Text("3", font_size=22)
        label_3.next_to(tick2, DOWN)
        
        self.play(Write(label_m2), Write(label_3))
        
        r1 = Text("x < -2", font_size=24, color=ORANGE)
        r1.move_to(LEFT*3 + DOWN*1.5)
        r2 = Text("-2 < x < 3", font_size=24, color=ORANGE)
        r2.move_to(DOWN*1.5)
        r3 = Text("x > 3", font_size=24, color=ORANGE)
        r3.move_to(RIGHT*3 + DOWN*1.5)
        
        self.play(Write(r1), Write(r2), Write(r3))
        
        arr1 = Arrow(line.get_left(), tick1.get_center(), color=GREEN, stroke_width=3)
        arr2 = Arrow(tick2.get_center(), line.get_right(), color=GREEN, stroke_width=3)
        
        self.play(Create(arr1), Create(arr2))
        
        answer = Text("Answer: x < -2  or  x > 3", font_size=28, color=YELLOW)
        answer.to_edge(DOWN)
        self.play(Write(answer))
        
        self.wait(2)
