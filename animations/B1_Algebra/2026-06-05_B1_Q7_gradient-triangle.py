# topic_id: B1_Q7
# track: igcse_o
# unit: B1_Algebra
# description: Plotting a linear graph with gradient triangle and y-intercept

from manim import *

class B1Q7GradientTriangle(Scene):
    def construct(self):
        title = Text("Gradient and y-intercept", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Create coordinate axes
        # x from -4 to 4, y from -2 to 8 (to fit y=2x+1 for x in [-1,3]: y in [-1,7])
        x_min, x_max = -4, 4
        y_min, y_max = -2, 8
        x_len = x_max - x_min  # 8
        y_len = y_max - y_min  # 10

        x_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE, stroke_width=1.5)
        x_axis.shift(DOWN * 1.5)
        y_axis = Line(DOWN * 1.5, UP * 6, color=WHITE, stroke_width=1.5)
        y_axis.shift(DOWN * 0.5)  # bottom at y=-2 shifted down by 0.5 → total y∈[-2, 8]

        # Shift everything to centre
        offset = RIGHT * 0.5
        x_axis.shift(offset)
        y_axis.shift(offset)

        def x_to_prop(x):
            return (x - x_min) / x_len

        def y_to_prop(y):
            return (y - y_min) / y_len

        # Tick marks on x-axis (show -2 to 4)
        ticks = VGroup()
        for i in range(-2, 5):
            if i == 0:
                continue
            tick = Line(UP * 0.1, DOWN * 0.1, color=WHITE, stroke_width=1)
            tick.move_to(x_axis.point_from_proportion(x_to_prop(i)))
            label = Text(str(i), font_size=14, color=WHITE)
            label.next_to(tick, DOWN, buff=0.1)
            ticks.add(tick, label)

        # Tick marks on y-axis (show -1 to 7)
        for i in range(-1, 8):
            if i == 0:
                continue
            tick = Line(LEFT * 0.1, RIGHT * 0.1, color=WHITE, stroke_width=1)
            tick.move_to(y_axis.point_from_proportion(y_to_prop(i)))
            label = Text(str(i), font_size=14, color=WHITE)
            label.next_to(tick, LEFT, buff=0.1)
            ticks.add(tick, label)

        origin = Text("0", font_size=14, color=WHITE)
        origin.move_to(y_axis.get_start() + RIGHT * 0.15 + DOWN * 0.2)
        x_lab = Text("x", font_size=16).next_to(x_axis, RIGHT, buff=0.1)
        y_lab = Text("y", font_size=16).next_to(y_axis, UP, buff=0.1)

        self.play(Create(x_axis), Create(y_axis), Create(ticks), Write(origin), Write(x_lab), Write(y_lab))
        self.wait(0.3)

        # Show equation
        eq = Text("y = 2x + 1", font_size=28, color=YELLOW)
        eq.shift(UP * 2.2 + LEFT * 1)
        self.play(Write(eq))
        self.wait(0.3)

        # Mark y-intercept at (0,1)
        inter_pt_pos = y_axis.point_from_proportion(y_to_prop(1))
        inter_pt = Dot(inter_pt_pos, color=RED, radius=0.1)
        inter_label = Text("y-int = 1", font_size=18, color=RED)
        inter_label.next_to(inter_pt, LEFT, buff=0.2)
        self.play(Create(inter_pt), Write(inter_label))
        self.wait(0.3)

        # Draw the line y = 2x + 1, from x=-1: y=-1 to x=3: y=7
        p1_x = x_axis.point_from_proportion(x_to_prop(-1))
        p1_y = y_axis.point_from_proportion(y_to_prop(-1))
        p2_x = x_axis.point_from_proportion(x_to_prop(3))
        p2_y = y_axis.point_from_proportion(y_to_prop(7))
        line = Line(
            [p1_x[0], p1_y[1], 0],
            [p2_x[0], p2_y[1], 0],
            color=GREEN, stroke_width=2.5
        )
        self.play(Create(line))
        self.wait(0.4)

        # Show gradient triangle between (0,1) and (2,5)
        pt1_x = x_axis.point_from_proportion(x_to_prop(0))[0]
        pt1_y = y_axis.point_from_proportion(y_to_prop(1))[1]
        pt2_x = x_axis.point_from_proportion(x_to_prop(2))[0]
        pt3_y = y_axis.point_from_proportion(y_to_prop(5))[1]

        pt1 = [pt1_x, pt1_y, 0]
        pt2 = [pt2_x, pt1_y, 0]
        pt3 = [pt2_x, pt3_y, 0]

        triangle = VGroup(
            Line(pt1, pt2, color=RED, stroke_width=2),
            Line(pt2, pt3, color=RED, stroke_width=2),
            Line(pt3, pt1, color=RED, stroke_width=2),
        )
        self.play(Create(triangle))
        self.wait(0.3)

        # Add labels for rise and run
        rise_label = Text("Rise = 4", font_size=18, color=RED)
        rise_label.next_to(triangle[1], RIGHT, buff=0.15)
        run_label = Text("Run = 2", font_size=18, color=RED)
        run_label.next_to(triangle[0], DOWN, buff=0.1)

        self.play(Write(rise_label), Write(run_label))
        self.wait(0.3)

        # Gradient value
        grad_text = Text("Gradient = Rise/Run = 4/2 = 2", font_size=22, color=YELLOW)
        grad_text.to_edge(DOWN, buff=0.3)
        self.play(Write(grad_text))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
