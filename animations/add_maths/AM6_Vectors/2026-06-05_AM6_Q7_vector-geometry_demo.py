from manim import *
import math

class Am6Q7Demo(Scene):
    def construct(self):
        # Title
        title = Text("Demo: Vector Geometry", font_size=32, color=TEAL)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Visual: coordinate axes as lines (no Axes class)
        h_line = Line(LEFT*4, RIGHT*4, color=GRAY)
        v_line = Line(DOWN*3, UP*3, color=GRAY)
        origin_dot = Dot(color=WHITE)
        self.play(Create(h_line), Create(v_line), Create(origin_dot))
        self.wait(0.5)

        # Demo objects
        obj1 = Square(color=RED, side_length=0.6)
        obj1.move_to(LEFT*2 + UP)
        obj2 = Circle(color=BLUE, radius=0.4)
        obj2.move_to(RIGHT*2 + DOWN)

        label1 = Text("P", font_size=22, color=RED)
        label1.next_to(obj1, UP)
        label2 = Text("Q", font_size=22, color=BLUE)
        label2.next_to(obj2, UP)

        self.play(Create(obj1), Create(obj2), Write(label1), Write(label2))
        self.wait(1)

        # Movement
        arrow_path = Arrow(obj1.get_center(), obj2.get_center(), color=YELLOW, buff=0.2)
        self.play(Create(arrow_path))
        self.wait(1)

        # Transform
        self.play(
            obj1.animate.move_to(RIGHT*3 + UP*0.5),
            obj2.animate.move_to(LEFT*3 + DOWN*0.5),
            arrow_path.animate.become(
                Arrow(RIGHT*3 + UP*0.5, LEFT*3 + DOWN*0.5, color=YELLOW, buff=0.2)
            ),
            run_time=2
        )
        self.wait(1)

        # Formula box
        formula_box = Rectangle(width=5, height=0.7, color=TEAL)
        formula_box.to_edge(DOWN, buff=0.3)
        formula_text = Text("AM6_Vectors - AM6_Q7", font_size=20, color=WHITE)
        formula_text.move_to(formula_box.get_center())
        self.play(Create(formula_box), Write(formula_text))
        self.wait(2)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
