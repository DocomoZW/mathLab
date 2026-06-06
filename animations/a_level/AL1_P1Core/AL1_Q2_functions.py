from manim import *
import math

class FunctionMap(Scene):
    def construct(self):
        title = Text("Function Machine", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Input box
        input_box = Rectangle(width=1.5, height=0.8, color=BLUE)
        input_label = Text("x", font_size=28, color=BLUE)
        input_label.move_to(input_box.get_center())
        input_group = VGroup(input_box, input_label)
        input_group.move_to(LEFT * 4)
        self.play(Create(input_group))
        self.wait(0.5)
        
        # Function box
        func_box = Rectangle(width=2, height=1.2, color=GREEN)
        func_label = Text("f(x) = 2x + 1", font_size=22, color=GREEN)
        func_label.move_to(func_box.get_center())
        func_group = VGroup(func_box, func_label)
        func_group.move_to(ORIGIN)
        self.play(Create(func_group))
        self.wait(0.5)
        
        # Output box
        output_box = Rectangle(width=1.5, height=0.8, color=YELLOW)
        output_label = Text("f(x)", font_size=28, color=YELLOW)
        output_label.move_to(output_box.get_center())
        output_group = VGroup(output_box, output_label)
        output_group.move_to(RIGHT * 4)
        self.play(Create(output_group))
        self.wait(0.5)
        
        # Arrow from input to function
        arrow1 = Arrow(input_group.get_right(), func_group.get_left(), buff=0.1)
        self.play(Create(arrow1))
        
        # Arrow from function to output
        arrow2 = Arrow(func_group.get_right(), output_group.get_left(), buff=0.1)
        self.play(Create(arrow2))
        self.wait(1)
        
        # Specific example
        self.play(FadeOut(title))
        
        input_val = Text("x = 3", font_size=28, color=BLUE)
        input_val.next_to(input_group, DOWN, buff=0.3)
        self.play(Write(input_val))
        self.wait(0.5)
        
        output_val = Text("f(3) = 2(3)+1 = 7", font_size=28, color=YELLOW)
        output_val.next_to(output_group, DOWN, buff=0.3)
        self.play(Write(output_val))
        self.wait(2)


class GraphTrans(Scene):
    def construct(self):
        title = Text("Function Transformations", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show the transformations
        transforms = [
            ("y = f(x) + a", "Vertical shift up by a"),
            ("y = f(x + a)", "Horizontal shift left by a"),
            ("y = -f(x)", "Reflection in x-axis"),
            ("y = f(-x)", "Reflection in y-axis"),
            ("y = af(x)", "Vertical stretch by factor a"),
            ("y = f(ax)", "Horizontal stretch by factor 1/a")
        ]
        
        lines = []
        for i, (form, desc) in enumerate(transforms):
            text = Text(f"{form:20s}  {desc}", font_size=22)
            text.next_to(title, DOWN, buff=0.3 + i * 0.4)
            lines.append(text)
            self.play(Write(text), run_time=0.3)
        
        self.wait(2)
        
        # Highlight key insight
        insight = Text("Note: y = f(x+a) shifts LEFT when a > 0", font_size=22, color=YELLOW)
        insight.next_to(lines[-1], DOWN, buff=0.5)
        self.play(Write(insight))
        self.wait(2)
