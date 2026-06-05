from manim import *
import math

class LogTransform(Scene):
    def construct(self):
        title = Text("Transforming Logarithmic Graphs", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))

        # Show base y = ln x
        base_title = Text("Base: y = ln x", font_size=26, color=BLUE)
        base_title.shift(UP*1.5 + LEFT*3)
        self.play(Write(base_title))

        # Axes for base
        x_axis = Line(LEFT*3, RIGHT*1, color=WHITE)
        x_axis.shift(DOWN*2)
        y_axis = Line(DOWN*2.5, UP*1, color=WHITE)
        y_axis.shift(LEFT*3)
        self.play(Create(x_axis), Create(y_axis))

        pts = []
        for x in range(2, 40):
            fx = x/10
            fy = math.log(fx)
            pts.append([fx*0.5 - 2.5, fy*0.4 - 0.3, 0])
        curve = VMobject(stroke_color=BLUE, stroke_width=2)
        curve.set_points_smoothly(pts)
        self.play(Create(curve))

        self.wait(0.5)

        # Show transformed: y = ln(x-1) + 2
        trans_title = Text("Transformed: y = ln(x-1) + 2", font_size=26, color=GREEN)
        trans_title.shift(UP*1.5 + RIGHT*2)
        self.play(Write(trans_title))

        # Axes for transformed
        x_axis2 = Line(LEFT*1, RIGHT*3, color=WHITE)
        x_axis2.shift(DOWN*2)
        y_axis2 = Line(DOWN*2.5, UP*1, color=WHITE)
        y_axis2.shift(RIGHT*1)
        self.play(Create(x_axis2), Create(y_axis2))

        pts2 = []
        for x in range(12, 50):
            fx = x/10
            fy = math.log(fx-1) + 2
            pts2.append([fx*0.5 - 1.5, fy*0.4 - 2.3, 0])
        curve2 = VMobject(stroke_color=GREEN, stroke_width=2)
        curve2.set_points_smoothly(pts2)
        self.play(Create(curve2))

        # Asymptote shifted
        asymp = DashedLine(DOWN*2.5, UP*1, color=RED, stroke_width=2)
        asymp.shift(RIGHT*2)
        self.play(Create(asymp))

        al = Text("x = 1", font_size=18, color=RED)
        al.next_to(asymp, UP, buff=0.1)
        self.play(Write(al))

        # Transformation description
        info1 = Text("Shift right by 1", font_size=20, color=ORANGE)
        info1.shift(DOWN*2.5 + LEFT*1)
        info2 = Text("Shift up by 2", font_size=20, color=ORANGE)
        info2.next_to(info1, DOWN)
        self.play(Write(info1), Write(info2))

        self.wait(2)
