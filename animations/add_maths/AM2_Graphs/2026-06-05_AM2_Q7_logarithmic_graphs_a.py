from manim import *
import math

class LogGraph(Scene):
    def construct(self):
        title = Text("Logarithmic Graph: y = ln x", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*1, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*2, UP*2, color=WHITE)
        y_axis.shift(LEFT*1)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Plot y = ln x
        pts = []
        for x in range(2, 60):
            fx = x/10
            fy = math.log(fx)
            pts.append([fx*1.0 - 1, fy*0.5, 0])
        curve = VMobject(stroke_color=BLUE, stroke_width=3)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=1.5)

        # Mark (1,0) - graph origin at (LEFT*1, DOWN*0.5), (1,0) at (LEFT*1+1*1.0, DOWN*0.5+0*0.5) = (LEFT*1+1, DOWN*0.5)
        dot10 = Dot(point=LEFT*1 + RIGHT*1 + DOWN*0.5, color=RED, radius=0.08)
        self.play(Create(dot10))
        label10 = Text("(1, 0)", font_size=20, color=RED)
        label10.next_to(dot10, DOWN+RIGHT)
        self.play(Write(label10))

        # Asymptote
        asymp = DashedLine(DOWN*2, UP*2, color=RED, stroke_width=2)
        asymp.shift(LEFT*1)
        self.play(Create(asymp))
        asymp_label = Text("x = 0 (asymptote)", font_size=18, color=RED)
        asymp_label.next_to(asymp, UP, buff=0.2)
        self.play(Write(asymp_label))

        features = [
            "Domain: x > 0",
            "Increasing slowly",
            "Vertical asymptote at x = 0",
            "Inverse of exponential"
        ]
        for i, f in enumerate(features):
            t = Text(f, font_size=20)
            t.shift(RIGHT*1.5 + UP*(1.5-i*0.5))
            self.play(Write(t), run_time=0.3)

        self.wait(2)
