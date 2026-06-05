from manim import *
import math

class E1Q7AreaSinC(Scene):
    def construct(self):
        # Triangle with two sides and included angle
        vertices = [
            [-2, -1.2, 0],
            [2, -1.2, 0],
            [0, 1.5, 0]
        ]
        triangle = Polygon(*vertices, color=WHITE)
        self.play(Create(triangle))
        
        # Label sides
        side_a = Text("a", font_size=24, color=BLUE)
        side_a.move_to([0.5, 0.2, 0])
        
        side_b = Text("b", font_size=24, color=GREEN)
        side_b.move_to([-0.5, 0.2, 0])
        
        self.play(Write(side_a), Write(side_b))
        
        # Included angle C
        angle_c = Text("C", font_size=22, color=YELLOW)
        angle_c.move_to([0, 1.8, 0])
        
        # Arc at C
        angle_arc = Arc(
            radius=0.35,
            start_angle=math.atan2(1.2, 2),
            angle=PI - 2 * math.atan2(1.2, 2),
            color=YELLOW
        )
        angle_arc.move_to(vertices[2])
        self.play(Create(angle_arc), Write(angle_c))
        
        self.wait(0.5)
        
        # Area formula
        formula = Text("Area = 0.5 x a x b x sin C", font_size=22, color=YELLOW)
        formula.to_edge(DOWN)
        self.play(Write(formula))
        
        self.wait(0.5)
        
        # Explanation
        title = Text("Area of Triangle using Sine", font_size=24, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        
        self.wait(0.5)
        
        note1 = Text("Need two sides and", font_size=20, color=GRAY)
        note1.next_to(formula, UP, buff=0.1)
        note2 = Text("the included angle", font_size=20, color=GRAY)
        note2.next_to(note1, UP, buff=0.05)
        self.play(Write(note1), Write(note2))
        
        self.wait(2)
