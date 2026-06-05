# topic_id: B1_Q4
# track: igcse_o
# unit: B1_Algebra
# description: Graph intersection of two lines showing the solution to simultaneous equations

from manim import *

class B1Q4GraphIntersection(Scene):
    def construct(self):
        title = Text("Simultaneous Equations: Graph Intersection", font_size=28, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Create axes
        axes = VGroup()
        # x-axis
        x_axis = Line(LEFT*4.5, RIGHT*4.5, color=WHITE, stroke_width=1.5)
        x_axis.shift(DOWN*0.5)
        # y-axis
        y_axis = Line(DOWN*2.5, UP*2.5, color=WHITE, stroke_width=1.5)
        y_axis.shift(LEFT*3.5)
        axes.add(x_axis, y_axis)

        # Tick marks
        ticks = VGroup()
        for i in range(-3, 6):
            if i == 0:
                continue
            tick = Line(UP*0.1, DOWN*0.1, color=WHITE, stroke_width=1)
            tick.move_to(x_axis.point_from_proportion((i+3)/8))
            label = Text(str(i), font_size=14, color=WHITE)
            label.next_to(tick, DOWN, buff=0.1)
            ticks.add(tick, label)

        for i in range(-2, 5):
            if i == 0:
                continue
            tick = Line(LEFT*0.1, RIGHT*0.1, color=WHITE, stroke_width=1)
            tick.move_to(y_axis.point_from_proportion((i+2)/7))
            label = Text(str(i), font_size=14, color=WHITE)
            label.next_to(tick, LEFT, buff=0.1)
            ticks.add(tick, label)

        origin = Text("0", font_size=14, color=WHITE)
        origin.next_to(y_axis.get_end() + RIGHT*0.15, DOWN+LEFT, buff=0.1)
        #axes_labels = VGroup(Text("x", font_size=16).next_to(x_axis, RIGHT), Text("y", font_size=16).next_to(y_axis, UP))
        x_lab = Text("x", font_size=16)
        x_lab.next_to(x_axis, RIGHT, buff=0.1)
        y_lab = Text("y", font_size=16)
        y_lab.next_to(y_axis, UP, buff=0.1)

        self.play(Create(axes), Create(ticks), Write(origin), Write(x_lab), Write(y_lab))
        self.wait(0.3)

        # Show first equation: y = 2x + 1
        eq1_text = Text("y = 2x + 1", font_size=24, color=GREEN)
        eq1_text.shift(UP*1.8 + LEFT*2)
        self.play(Write(eq1_text))
        self.wait(0.3)

        # Plot line: points at x=-1: y=-1, x=0: y=1, x=2: y=5
        line1 = VGroup()
        for x_val in [-1, 0, 1, 2]:
            y_val = 2*x_val + 1
            x_pos = x_axis.point_from_proportion((x_val+3)/8)
            y_pos = y_axis.point_from_proportion((y_val+2)/7)
            pt = Dot([x_pos[0], y_pos[1], 0], color=GREEN, radius=0.08)
            line1.add(pt)

        self.play(*[Create(p) for p in line1])
        self.wait(0.2)

        # Draw the line connecting dots
        line1_connect = Line(
            [x_axis.point_from_proportion((-1+3)/8)[0], y_axis.point_from_proportion((-1+2)/7)[1], 0],
            [x_axis.point_from_proportion((2+3)/8)[0], y_axis.point_from_proportion((5+2)/7)[1], 0],
            color=GREEN, stroke_width=2
        )
        self.play(Create(line1_connect))
        self.wait(0.3)

        # Show second equation: y = -x + 7
        eq2_text = Text("y = -x + 7", font_size=24, color=RED)
        eq2_text.next_to(eq1_text, DOWN, buff=0.2)
        self.play(Write(eq2_text))
        self.wait(0.3)

        # Plot line2
        line2_connect = Line(
            [x_axis.point_from_proportion((2+3)/8)[0], y_axis.point_from_proportion((5+2)/7)[1], 0],
            [x_axis.point_from_proportion((4+3)/8)[0], y_axis.point_from_proportion((3+2)/7)[1], 0],
            color=RED, stroke_width=2
        )
        line2_points = VGroup()
        for x_val in [2, 3, 4]:
            y_val = -x_val + 7
            x_pos = x_axis.point_from_proportion((x_val+3)/8)
            y_pos = y_axis.point_from_proportion((y_val+2)/7)
            pt = Dot([x_pos[0], y_pos[1], 0], color=RED, radius=0.08)
            line2_points.add(pt)

        self.play(*[Create(p) for p in line2_points])
        self.play(Create(line2_connect))
        self.wait(0.3)

        # Highlight intersection at (2,5)
        inter_x = x_axis.point_from_proportion((2+3)/8)
        inter_y = y_axis.point_from_proportion((5+2)/7)
        inter_dot = Dot([inter_x[0], inter_y[1], 0], color=YELLOW, radius=0.15)
        inter_label = Text("(2, 5)", font_size=20, color=YELLOW)
        inter_label.next_to(inter_dot, RIGHT, buff=0.2)

        self.play(Create(inter_dot), Write(inter_label))
        self.wait(0.3)

        # Flash
        flash = SurroundingRectangle(inter_dot, color=YELLOW, buff=0.3)
        self.play(Create(flash))
        self.wait(0.3)
        self.play(FadeOut(flash))

        # Solution text
        sol = Text("Solution: x = 2, y = 5", font_size=28, color=GREEN)
        sol.to_edge(DOWN, buff=0.3)
        self.play(Write(sol))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
