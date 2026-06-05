from manim import *
import math

class E1Q6CosineRule(Scene):
    def construct(self):
        # General triangle
        vertices = [
            np.array([-2, -1.2, 0]),
            np.array([2, -1.2, 0]),
            np.array([0, 1.5, 0])
        ]
        triangle = Polygon(*vertices, color=WHITE)
        self.play(Create(triangle))
        
        # Side labels
        a_label = Text("a", font_size=24, color=BLUE)
        a_label.move_to(np.array([0.5, 0.3, 0]))
        
        b_label = Text("b", font_size=24, color=GREEN)
        b_label.move_to(np.array([-0.5, 0.3, 0]))
        
        c_label = Text("c", font_size=24, color=RED)
        c_label.move_to(np.array([0, -1.5, 0]))
        
        self.play(Write(a_label), Write(b_label), Write(c_label))
        
        # Angle A
        angle_a = Text("A", font_size=22, color=YELLOW)
        angle_a.move_to(vertices[0] + np.array([-0.3, -0.3, 0]))
        
        # Arc at angle A
        angle_arc = Arc(
            radius=0.3,
            start_angle=-math.atan2(1.2, 2),
            angle=math.atan2(2.7, 2),
            color=YELLOW
        )
        angle_arc.shift(vertices[0])
        self.play(Create(angle_arc), Write(angle_a))
        
        self.wait(0.5)
        
        # Cosine Rule formula
        formula1 = Text("a^2 = b^2 + c^2 - 2bc cos A", font_size=22, color=YELLOW)
        formula1.to_edge(DOWN)
        self.play(Write(formula1))
        
        self.wait(0.5)
        
        # Alternative forms
        note = Text("The Cosine Rule", font_size=24, color=YELLOW)
        note.to_edge(UP)
        self.play(Write(note))
        
        self.wait(0.5)
        
        formula2 = Text("Use when you know", font_size=20, color=GRAY)
        formula2.next_to(formula1, UP, buff=0.1)
        formula3 = Text("2 sides and included angle", font_size=20, color=GRAY)
        formula3.next_to(formula2, UP, buff=0.05)
        self.play(Write(formula2), Write(formula3))
        
        self.wait(2)
