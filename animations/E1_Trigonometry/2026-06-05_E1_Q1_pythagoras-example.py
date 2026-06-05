from manim import *
import math

class E1Q1PythagorasExample(Scene):
    def construct(self):
        # 3-4-5 right triangle
        triangle = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0],
            color=WHITE
        )
        self.play(Create(triangle))
        
        # Right angle marker
        right_angle = Square(side_length=0.25).move_to([-2, -1.5, 0])
        right_angle.shift(UR * 0.25)
        self.play(Create(right_angle))
        
        # Side labels with numbers
        side_a_label = Text("3", font_size=24, color=BLUE)
        side_a_label.next_to(triangle, DOWN, buff=0.3)
        
        side_b_label = Text("4", font_size=24, color=GREEN)
        side_b_label.next_to(triangle, LEFT, buff=0.3)
        
        side_c_label = Text("?", font_size=26, color=RED)
        side_c_label.move_to([0, 0.5, 0])
        
        self.play(Write(side_a_label), Write(side_b_label), Write(side_c_label))
        
        self.wait(0.5)
        
        # Show formula
        formula1 = Text("c^2 = a^2 + b^2", font_size=22, color=YELLOW)
        formula1.to_edge(UP)
        self.play(Write(formula1))
        
        self.wait(0.5)
        
        # Substitute
        formula2 = Text("c^2 = 3^2 + 4^2", font_size=22, color=YELLOW)
        formula2.to_edge(UP)
        self.play(Transform(formula1, formula2))
        
        self.wait(0.5)
        
        formula3 = Text("c^2 = 9 + 16 = 25", font_size=22, color=YELLOW)
        formula3.to_edge(UP)
        self.play(Transform(formula1, formula3))
        
        self.wait(0.5)
        
        formula4 = Text("c = 5", font_size=24, color=YELLOW)
        formula4.to_edge(UP)
        self.play(Transform(formula1, formula4))
        
        # Update hypotenuse label
        new_c_label = Text("5", font_size=24, color=RED)
        new_c_label.move_to([0, 0.5, 0])
        self.play(Transform(side_c_label, new_c_label))
        
        self.wait(2)
