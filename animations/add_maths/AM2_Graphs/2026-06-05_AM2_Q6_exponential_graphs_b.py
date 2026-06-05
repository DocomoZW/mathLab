from manim import *
import math

class ExpDecay(Scene):
    def construct(self):
        title = Text("Exponential Decay: y = e^{-x}", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*0.5)
        y_axis = Line(DOWN*1, UP*2.5, color=WHITE)
        y_axis.shift(LEFT*4)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Plot y = e^{-x}
        pts = []
        for x in range(-30, 31):
            fx = x/10
            fy = math.exp(-fx)
            pts.append([fx*1.5, fy*0.5 - 0.5, 0])
        curve = VMobject(stroke_color=GREEN, stroke_width=3)
        curve.set_points_smoothly(pts)
        self.play(Create(curve), run_time=1.5)

        # Mark (0,1) - graph origin at (LEFT*4, DOWN*0.5), (0,1) at (LEFT*4, 0)
        dot01 = Dot(point=LEFT*4, color=RED, radius=0.08)
        self.play(Create(dot01))
        label01 = Text("(0, 1)", font_size=20, color=RED)
        label01.next_to(dot01, UP+RIGHT)
        self.play(Write(label01))

        # Asymptote
        asymp = DashedLine(LEFT*4, RIGHT*4, color=RED, stroke_width=2)
        asymp.shift(DOWN*0.5)
        self.play(Create(asymp))
        asymp_label = Text("y = 0 (asymptote)", font_size=18, color=RED)
        asymp_label.next_to(asymp, RIGHT, buff=0.2)
        self.play(Write(asymp_label))

        # Comparison with e^x
        comp = Text("Reflection of y = e^x in the y-axis", font_size=24, color=YELLOW)
        comp.to_edge(DOWN)
        self.play(Write(comp))

        features = [
            "Always positive",
            "Decreasing as x increases",
            "Models decay processes",
            "y = e^x reflected in y-axis"
        ]
        for i, f in enumerate(features):
            t = Text(f, font_size=20)
            t.shift(RIGHT*1.5 + UP*(1.5-i*0.5))
            self.play(Write(t), run_time=0.3)

        self.wait(2)
