from manim import *
import math

class RotateNonOrigin(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.2)

        centre_pos = RIGHT*0.5 + DOWN*0.5
        centre_dot = Dot(centre_pos, color=WHITE, radius=0.08)
        centre_label = Text("C(2,1)").scale(0.2).next_to(centre_dot, DOWN)
        self.play(FadeIn(centre_dot), Write(centre_label))
        self.wait(0.2)

        p_pos = RIGHT*2.0 + UP*0.5
        dot = Dot(p_pos, color=BLUE)
        dot_label = Text("P(5,2)").scale(0.2).next_to(dot, UP+RIGHT)
        self.play(FadeIn(dot), Write(dot_label))
        self.wait(0.3)

        conn = Line(centre_pos, p_pos, color=GRAY, stroke_width=1)
        self.play(Create(conn))
        self.wait(0.2)

        dx = p_pos[0] - centre_pos[0]
        dy = p_pos[1] - centre_pos[1]
        dist = math.sqrt(dx*dx + dy*dy)
        angle = math.atan2(dy, dx)
        new_angle = angle + math.pi/2
        px = centre_pos[0] + dist * math.cos(new_angle)
        py = centre_pos[1] + dist * math.sin(new_angle)
        p_rot = np.array([px, py, 0])

        dot_rot = Dot(p_rot, color=GREEN)
        dot_rot_label = Text("P'(1,4)").scale(0.2).next_to(dot_rot, UP)
        conn2 = Line(centre_pos, p_rot, color=GREEN, stroke_width=1)
        self.play(Create(conn2), FadeIn(dot_rot), Write(dot_rot_label))
        self.wait(0.5)

        arc = ArcBetweenPoints(p_pos, p_rot, color=YELLOW, stroke_width=2)
        self.play(Create(arc))
        self.wait(0.4)

        info = Text("Rotation 90 deg anticlockwise about C(2,1)", color=WHITE).scale(0.3).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
