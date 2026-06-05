from manim import *
import math

class FunctionMap(Scene):
    def construct(self):
        title = Text("Functions: Mapping Diagram", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        input_box = Rectangle(width=2, height=3, color=BLUE)
        input_box.shift(LEFT*3)
        in_label = Text("Domain", font_size=24, color=BLUE)
        in_label.next_to(input_box, UP)
        
        output_box = Rectangle(width=2, height=3, color=GREEN)
        output_box.shift(RIGHT*3)
        out_label = Text("Range", font_size=24, color=GREEN)
        out_label.next_to(output_box, UP)
        
        self.play(Create(input_box), Create(output_box), Write(in_label), Write(out_label))
        
        in_vals = [Text(str(i), font_size=28) for i in [1, 2, 3]]
        for i, t in enumerate(in_vals):
            t.move_to(input_box.get_left() + RIGHT*0.5 + DOWN*(i-1)*0.8)
            self.play(Write(t), run_time=0.3)
        
        out_vals = [Text(st, font_size=28) for st in ["3", "5", "7"]]
        for i, t in enumerate(out_vals):
            t.move_to(output_box.get_left() + RIGHT*0.5 + DOWN*(i-1)*0.8)
            self.play(Write(t), run_time=0.3)
        
        func_text = Text("f(x) = 2x + 1", font_size=28, color=YELLOW)
        func_text.next_to(input_box, DOWN)
        self.play(Write(func_text))
        
        for i in range(3):
            start = in_vals[i].get_right()
            end = out_vals[i].get_left()
            arrow = Arrow(start, end, color=ORANGE, stroke_width=2)
            self.play(Create(arrow), run_time=0.4)
        
        self.wait(2)
