# topic_id: B1_Q7
# track: igcse_o
# unit: B1_Algebra
# description: Function notation visualisation with input-output mapping

from manim import *

class B1Q7FunctionMachine(Scene):
    def construct(self):
        title = Text("Function Machine: f(x) = 2x + 3", font_size=28, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Draw a function machine
        machine = Rectangle(width=3, height=2, color=YELLOW, stroke_width=2)
        machine.shift(DOWN*0.5)
        machine_label = Text("f(x)", font_size=28, color=YELLOW)
        machine_label.move_to(machine.get_center())
        machine_func = Text("2x + 3", font_size=20, color=RED)
        machine_func.next_to(machine_label, DOWN, buff=0.2)

        self.play(Create(machine), Write(machine_label), Write(machine_func))
        self.wait(0.3)

        # Input arrows
        input_box = Rectangle(width=1, height=0.6, color=GREEN, fill_opacity=0.3, fill_color=GREEN)
        input_box.shift(LEFT*3 + UP*0.5)
        input_label = Text("Input:", font_size=18, color=GREEN)
        input_label.next_to(input_box, LEFT, buff=0.1)
        input_val = Text("x", font_size=22, color=WHITE)
        input_val.move_to(input_box.get_center())

        in_arrow = Arrow(input_box.get_right(), machine.get_left(), color=GREEN, stroke_width=2)

        self.play(Create(input_box), Write(input_label), Write(input_val), Create(in_arrow))
        self.wait(0.3)

        # Output arrows
        output_box = Rectangle(width=1, height=0.6, color=RED, fill_opacity=0.3, fill_color=RED)
        output_box.shift(RIGHT*3 + UP*0.5)
        output_label = Text("Output:", font_size=18, color=RED)
        output_label.next_to(output_box, RIGHT, buff=0.1)
        output_val = Text("2x+3", font_size=22, color=WHITE)
        output_val.move_to(output_box.get_center())

        out_arrow = Arrow(machine.get_right(), output_box.get_left(), color=RED, stroke_width=2)

        self.play(Create(output_box), Write(output_label), Write(output_val), Create(out_arrow))
        self.wait(0.5)

        # Now animate with specific input
        self.play(FadeOut(input_val))
        input_2 = Text("2", font_size=22, color=WHITE)
        input_2.move_to(input_box.get_center())
        self.play(Write(input_2))
        self.wait(0.3)

        # Transform output
        self.play(FadeOut(output_val))
        output_7 = Text("7", font_size=22, color=WHITE)
        output_7.move_to(output_box.get_center())
        self.play(Write(output_7))
        self.wait(0.3)

        # Show f(2) = 7
        eval_text = Text("f(2) = 2(2)+3 = 7", font_size=24, color=GREEN)
        eval_text.to_edge(DOWN, buff=0.3)
        self.play(Write(eval_text))
        self.wait(0.5)

        # Now try x = -1
        self.play(FadeOut(input_2))
        input_neg1 = Text("-1", font_size=22, color=WHITE)
        input_neg1.move_to(input_box.get_center())
        self.play(Write(input_neg1))
        self.wait(0.2)

        self.play(FadeOut(output_7))
        output_1 = Text("1", font_size=22, color=WHITE)
        output_1.move_to(output_box.get_center())
        self.play(Write(output_1))
        self.wait(0.2)

        self.play(FadeOut(eval_text))
        eval2 = Text("f(-1) = 2(-1)+3 = 1", font_size=24, color=GREEN)
        eval2.to_edge(DOWN, buff=0.3)
        self.play(Write(eval2))
        self.wait(0.5)

        # Show mapping summary
        self.play(FadeOut(eval2))
        mapping = Text("f(x) maps each input to exactly one output", font_size=20, color=YELLOW)
        mapping.to_edge(DOWN, buff=0.3)
        self.play(Write(mapping))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
