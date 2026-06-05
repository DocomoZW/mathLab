from manim import *
import math

class E1Q2TrigExample(Scene):
    def construct(self):
        # Right triangle with known angle and side
        triangle = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0],
            color=WHITE
        )
        self.play(Create(triangle))
        
        # Right angle
        right_angle = Square(side_length=0.25).move_to([-2, -1.5, 0])
        right_angle.shift(UR * 0.25)
        self.play(Create(right_angle))
        
        # Angle marker at bottom left
        theta_arc = Arc(radius=0.3, angle=math.atan2(3, 4), color=YELLOW)
        theta_arc.move_to([-2, -1.5, 0])
        theta_arc.shift(RIGHT * 0.5 * 0.3, UP * 0.6 * 0.3)
        self.play(Create(theta_arc))
        theta_label = Text("30 deg", font_size=20, color=YELLOW)
        theta_label.move_to([-1.3, -0.9, 0])
        self.play(Write(theta_label))
        
        # Known side
        adj_label = Text("10", font_size=24, color=GREEN)
        adj_label.next_to(triangle, DOWN, buff=0.3)
        self.play(Write(adj_label))
        
        # Unknown side
        opp_q = Text("?", font_size=26, color=BLUE)
        opp_q.move_to([-2.5, 0, 0])
        self.play(Write(opp_q))
        
        self.wait(0.5)
        
        # Formula
        formula1 = Text("tan 30 = opposite / 10", font_size=22, color=YELLOW)
        formula1.to_edge(UP)
        self.play(Write(formula1))
        
        self.wait(0.5)
        
        formula2 = Text("opposite = 10 x tan 30", font_size=22, color=YELLOW)
        formula2.to_edge(UP)
        self.play(Transform(formula1, formula2))
        
        self.wait(0.5)
        
        formula3 = Text("opposite = 5.77", font_size=22, color=YELLOW)
        formula3.to_edge(UP)
        self.play(Transform(formula1, formula3))
        
        # Update unknown label
        ans_label = Text("5.77", font_size=24, color=BLUE)
        ans_label.move_to([-2.5, 0, 0])
        self.play(Transform(opp_q, ans_label))
        
        self.wait(2)
