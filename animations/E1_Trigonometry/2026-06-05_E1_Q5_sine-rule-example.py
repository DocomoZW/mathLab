from manim import *
import math

class E1Q5SineRuleExample(Scene):
    def construct(self):
        # Triangle with known values
        vertices = [
            np.array([-2, -1.2, 0]),
            np.array([2, -1.2, 0]),
            np.array([0, 1.5, 0])
        ]
        triangle = Polygon(*vertices, color=WHITE)
        self.play(Create(triangle))
        
        # Known angles
        angle_a_val = Text("40 deg", font_size=20, color=GREEN)
        angle_a_val.move_to(vertices[0] + np.array([-0.3, -0.3, 0]))
        
        angle_b_val = Text("70 deg", font_size=20, color=RED)
        angle_b_val.move_to(vertices[1] + np.array([0.3, -0.3, 0]))
        
        self.play(Write(angle_a_val), Write(angle_b_val))
        
        # Known side
        side_c_val = Text("12", font_size=24, color=RED)
        side_c_val.move_to([0, -1.5, 0])
        self.play(Write(side_c_val))
        
        # Unknown side
        side_a_q = Text("?", font_size=26, color=BLUE)
        side_a_q.move_to([0.6, 0.4, 0])
        self.play(Write(side_a_q))
        
        self.wait(0.5)
        
        # Find angle C
        step1 = Text("Angle C = 180 - 40 - 70 = 70 deg", font_size=20, color=YELLOW)
        step1.to_edge(UP)
        self.play(Write(step1))
        
        self.wait(0.5)
        
        # Sine rule step
        step2 = Text("a / sin 40 = 12 / sin 70", font_size=20, color=YELLOW)
        step2.next_to(step1, DOWN, buff=0.1)
        self.play(Write(step2))
        
        self.wait(0.5)
        
        step3 = Text("a = (12 x sin 40) / sin 70", font_size=20, color=YELLOW)
        step3.next_to(step2, DOWN, buff=0.1)
        self.play(Write(step3))
        
        self.wait(0.5)
        
        step4 = Text("a = 8.21", font_size=22, color=YELLOW)
        step4.next_to(step3, DOWN, buff=0.1)
        self.play(Write(step4))
        
        # Update unknown label
        ans_label = Text("8.21", font_size=24, color=BLUE)
        ans_label.move_to([0.6, 0.4, 0])
        self.play(Transform(side_a_q, ans_label))
        
        self.wait(2)
