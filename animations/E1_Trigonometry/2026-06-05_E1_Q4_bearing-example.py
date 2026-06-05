from manim import *
import math

class E1Q4BearingExample(Scene):
    def construct(self):
        # Title
        title = Text("Bearing Problem", font_size=24, color=YELLOW)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Point A
        dot_a = Dot([-2, 0, 0], color=BLUE)
        label_a = Text("A", font_size=24, color=BLUE)
        label_a.next_to(dot_a, LEFT, buff=0.2)
        self.play(Create(dot_a), Write(label_a))
        
        # North line at A
        north_line = Line([-2, 0, 0], [-2, 1.5, 0], color=RED)
        n_label = Text("N", font_size=20, color=RED)
        n_label.move_to([-2, 1.7, 0])
        self.play(Create(north_line), Write(n_label))
        
        self.wait(0.3)
        
        # Bearing of 045 degrees from A
        angle = 45 * DEGREES
        bearing_line = Line(
            [-2, 0, 0],
            [-2 + 2.5 * np.sin(angle), 2.5 * np.cos(angle), 0],
            color=YELLOW
        )
        self.play(Create(bearing_line))
        
        # Arc
        bearing_arc = Arc(
            radius=0.4,
            start_angle=PI/2,
            angle=-angle,
            color=YELLOW
        )
        bearing_arc.move_to([-2, 0, 0])
        self.play(Create(bearing_arc))
        
        bearing_label = Text("045 deg", font_size=20, color=YELLOW)
        bearing_label.move_to([-1.4, 0.6, 0])
        self.play(Write(bearing_label))
        
        self.wait(0.3)
        
        # Point B on the bearing line
        dist = 2.0
        bx = -2 + dist * np.sin(angle)
        by = dist * np.cos(angle)
        dot_b = Dot([bx, by, 0], color=GREEN)
        label_b = Text("B", font_size=24, color=GREEN)
        label_b.next_to(dot_b, UR, buff=0.2)
        self.play(Create(dot_b), Write(label_b))
        
        # Distance label
        mid_x = (-2 + bx) / 2
        mid_y = by / 2
        dist_label = Text("10 km", font_size=20, color=WHITE)
        dist_label.move_to([mid_x + 0.2, mid_y + 0.2, 0])
        self.play(Write(dist_label))
        
        self.wait(0.5)
        
        # Position of B
        result = Text("B is 10 km from A", font_size=22, color=GREEN)
        result.next_to(title, DOWN, buff=0.1)
        result2 = Text("at a bearing of 045 deg", font_size=22, color=GREEN)
        result2.next_to(result, DOWN, buff=0.05)
        self.play(Write(result), Write(result2))
        
        self.wait(2)
