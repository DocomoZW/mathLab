from manim import *
import math

class E1Q1Pythagoras(Scene):
    def construct(self):
        # Right triangle
        triangle = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0],
            color=WHITE
        )
        self.play(Create(triangle))
        
        # Labels a, b, c
        a_label = Text("a", font_size=24).next_to(triangle, DOWN, buff=0.3)
        b_label = Text("b", font_size=24).next_to(triangle, LEFT, buff=0.3)
        c_label = Text("c", font_size=24).next_to(triangle.get_center(), UR, buff=0.3)
        self.play(Write(a_label), Write(b_label), Write(c_label))
        
        # Right angle marker
        right_angle = Square(side_length=0.25).move_to([-2, -1.5, 0])
        right_angle.shift(UR * 0.25)
        self.play(Create(right_angle))
        
        self.wait(0.5)
        
        # Squares on each side
        sq_a = Square(side_length=3, color=BLUE).move_to([0, -1.5, 0])
        sq_b = Square(side_length=3, color=GREEN).move_to([-2, 0, 0])
        sq_c = Square(side_length=3*math.sqrt(2), color=RED)
        sq_c.rotate(-45 * DEGREES)
        center_c = triangle.get_center() + [0.5, 0, 0]
        sq_c.move_to(center_c)
        
        self.play(Create(sq_a), Create(sq_b), Create(sq_c))
        
        # Labels on squares
        a2 = Text("a^2", font_size=20, color=BLUE).move_to(sq_a.get_center())
        b2 = Text("b^2", font_size=20, color=GREEN).move_to(sq_b.get_center())
        c2 = Text("c^2", font_size=20, color=RED).move_to(sq_c.get_center())
        self.play(Write(a2), Write(b2), Write(c2))
        
        self.wait(0.5)
        
        # Formula
        formula = Text("a^2 + b^2 = c^2", font_size=24, color=YELLOW)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        
        self.wait(2)
