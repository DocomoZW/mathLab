from manim import *
import math

class E1Q4Bearing(Scene):
    def construct(self):
        # Compass circle
        compass = Circle(radius=1.5, color=WHITE)
        self.play(Create(compass))
        
        # Cross lines
        v_line = Line([0, -1.5, 0], [0, 1.5, 0], color=GRAY)
        h_line = Line([-1.5, 0, 0], [1.5, 0, 0], color=GRAY)
        self.play(Create(v_line), Create(h_line))
        
        # Cardinal directions
        n = Text("N", font_size=24, color=WHITE).move_to([0, 1.8, 0])
        s = Text("S", font_size=24, color=WHITE).move_to([0, -1.8, 0])
        e = Text("E", font_size=24, color=WHITE).move_to([1.8, 0, 0])
        w = Text("W", font_size=24, color=WHITE).move_to([-1.8, 0, 0])
        self.play(Write(n), Write(s), Write(e), Write(w))
        
        self.wait(0.5)
        
        # North arrow
        north_arrow = Arrow([0, 0.4, 0], [0, 1.4, 0], color=RED)
        self.play(Create(north_arrow))
        n_label = Text("North", font_size=20, color=RED)
        n_label.next_to(north_arrow, RIGHT, buff=0.1)
        self.play(Write(n_label))
        
        self.wait(0.3)
        
        # Bearing arrow (clockwise from north, e.g., 060 deg)
        angle = 60 * DEGREES
        bearing_arrow = Arrow(
            [0, 0.4, 0],
            [1.5 * math.sin(angle), 1.5 * math.cos(angle), 0],
            color=YELLOW
        )
        self.play(Create(bearing_arrow))
        
        # Bearing arc from north to bearing direction
        bearing_arc = Arc(
            radius=0.5,
            start_angle=PI/2,
            angle=-angle,
            color=YELLOW
        )
        self.play(Create(bearing_arc))
        
        # Bearing label
        bearing_label = Text("060 deg", font_size=22, color=YELLOW)
        bearing_label.move_to([0.8, 0.8, 0])
        self.play(Write(bearing_label))
        
        self.wait(0.5)
        
        # Explanation
        note = Text("Measured clockwise from North", font_size=20, color=GRAY)
        note.to_edge(DOWN)
        self.play(Write(note))
        
        self.wait(2)
