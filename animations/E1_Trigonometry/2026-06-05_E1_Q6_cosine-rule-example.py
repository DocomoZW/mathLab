from manim import *
import math

class E1Q6CosineRuleExample(Scene):
    def construct(self):
        # Triangle with known values
        vertices = [
            np.array([-2, -1.2, 0]),
            np.array([2, -1.2, 0]),
            np.array([0, 1.5, 0])
        ]
        triangle = Polygon(*vertices, color=WHITE)
        self.play(Create(triangle))
        
        # Known sides
        b_val = Text("7", font_size=24, color=GREEN)
        b_val.move_to(np.array([-0.5, 0.3, 0]))
        
        c_val = Text("9", font_size=24, color=RED)
        c_val.move_to(np.array([0, -1.5, 0]))
        
        self.play(Write(b_val), Write(c_val))
        
        # Known angle A
        angle_a_val = Text("60 deg", font_size=20, color=YELLOW)
        angle_a_val.move_to(vertices[0] + np.array([-0.4, -0.3, 0]))
        
        angle_arc = Arc(
            radius=0.3,
            start_angle=-math.atan2(1.2, 2),
            angle=math.atan2(2.7, 2),
            color=YELLOW
        )
        angle_arc.shift(vertices[0])
        self.play(Create(angle_arc), Write(angle_a_val))
        
        # Unknown side a
        a_q = Text("?", font_size=26, color=BLUE)
        a_q.move_to([0.5, 0.3, 0])
        self.play(Write(a_q))
        
        self.wait(0.5)
        
        # Formula
        step1 = Text("a^2 = 7^2 + 9^2 - 2(7)(9) cos 60", font_size=20, color=YELLOW)
        step1.to_edge(UP)
        self.play(Write(step1))
        
        self.wait(0.5)
        
        step2 = Text("a^2 = 49 + 81 - 126 x 0.5", font_size=20, color=YELLOW)
        step2.next_to(step1, DOWN, buff=0.1)
        self.play(Write(step2))
        
        self.wait(0.5)
        
        step3 = Text("a^2 = 130 - 63 = 67", font_size=20, color=YELLOW)
        step3.next_to(step2, DOWN, buff=0.1)
        self.play(Write(step3))
        
        self.wait(0.5)
        
        step4 = Text("a = 8.19", font_size=22, color=YELLOW)
        step4.next_to(step3, DOWN, buff=0.1)
        self.play(Write(step4))
        
        # Update unknown label
        ans_label = Text("8.19", font_size=24, color=BLUE)
        ans_label.move_to([0.5, 0.3, 0])
        self.play(Transform(a_q, ans_label))
        
        self.wait(2)
