from manim import *
import math

class CubicShape(Scene):
    def construct(self):
        title = Text("Cubic Graph: y = x^3", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*4)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Plot y = x^3
        pts = []
        for x in range(-20, 21):
            fx = x/7
            fy = fx*fx*fx
            pts.append([fx*1.5, fy*0.5, 0])
        curve = VMobject(stroke_color=BLUE, stroke_width=3)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=1.5)

        # Mark origin
        origin = Dot(LEFT*4 + DOWN*0.5, color=RED, radius=0.08)
        # Actually origin is at (LEFT*4, DOWN*0.5)
        # Let's put it properly
        origin = Dot(LEFT*4 + DOWN*0.5, color=RED, radius=0.08)
        # But that's the axes intersection already
        self.play(Create(origin))

        label = Text("S-shaped curve", font_size=24, color=BLUE)
        label.next_to(curve, RIGHT, buff=0.3)
        self.play(Write(label))

        features = [
            "Passes through (0,0)",
            "No asymptotes",
            "One turning point or none",
            "Both ends go to infinity"
        ]
        for i, f in enumerate(features):
            t = Text(f, font_size=20)
            t.shift(RIGHT*2 + UP*(1.5-i*0.5))
            self.play(Write(t), run_time=0.3)

        self.wait(2)
