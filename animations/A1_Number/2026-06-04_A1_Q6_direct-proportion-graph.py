# topic_id: A1_Q6
# track: igcse_o
# unit: A1_Number
# description: Direct proportion graph (y = kx) showing y = 4x with labeled points

from manim import *
import numpy as np

class DirectProportionGraph(Scene):
    def construct(self):
        # Title
        title = Text("Direct Proportion: y = kx  (y = 4x)", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Draw axes manually using arrows
        x_axis = Arrow(np.array([-4.5, -1.0, 0]), np.array([4.5, -1.0, 0]), color=WHITE, buff=0)
        y_axis = Arrow(np.array([-3.5, -1.8, 0]), np.array([-3.5, 2.5, 0]), color=WHITE, buff=0)

        # Axis labels
        x_label = Text("x", font_size=20, color=WHITE)
        x_label.next_to(x_axis.get_end(), DOWN, buff=0.1)
        y_label = Text("y", font_size=20, color=WHITE)
        y_label.next_to(y_axis.get_end(), LEFT, buff=0.1)

        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label))
        self.wait(0.3)

        # Scale: x from 0 to 7, y from 0 to 28
        # Origin at (-3.5, -1.0)
        # x length: 7 units -> 7.5 pixels per unit (4.5 - (-3.5)) / 7 * 2... 
        # Actually let me recalculate:
        # x range: 0 to 7, mapped to x pixels: -3.5 to 4.0 (7.5 px total)
        # y range: 0 to 28, mapped to y pixels: -1.0 to 2.0 (3.0 px total)
        def x_to_px(x_val):
            return -3.5 + (x_val / 7.0) * 7.5
        def y_to_px(y_val):
            return -1.0 + (y_val / 28.0) * 3.0

        # Tick marks
        ticks = VGroup()
        tick_labels = VGroup()
        for x_val in range(1, 8):
            px = x_to_px(x_val)
            tick = Line(np.array([px, -1.0, 0]), np.array([px, -0.85, 0]), color=WHITE, stroke_width=1)
            ticks.add(tick)
            lbl = Text(str(x_val), font_size=14, color=WHITE)
            lbl.next_to(tick, DOWN, buff=0.05)
            tick_labels.add(lbl)
        for y_val in range(4, 29, 4):
            py = y_to_px(y_val)
            tick = Line(np.array([-3.5, py, 0]), np.array([-3.35, py, 0]), color=WHITE, stroke_width=1)
            ticks.add(tick)
            lbl = Text(str(y_val), font_size=14, color=WHITE)
            lbl.next_to(tick, LEFT, buff=0.05)
            tick_labels.add(lbl)

        self.play(Create(ticks), Write(tick_labels))
        self.wait(0.3)

        # Draw the line y = 4x
        k = 4
        line_start = np.array([x_to_px(0), y_to_px(0), 0])
        line_end = np.array([x_to_px(6.5), y_to_px(6.5 * k), 0])
        graph_line = Line(line_start, line_end, color=YELLOW, stroke_width=3)
        self.play(Create(graph_line), rate_func=linear, run_time=1.0)
        self.wait(0.3)

        # Equation label
        eq_label = Text("y = 4x", font_size=32, color=YELLOW)
        eq_label.to_edge(RIGHT, buff=0.5)
        eq_label.shift(UP * 0.5)
        self.play(Write(eq_label))
        self.wait(0.3)

        # Plot specific points
        points_data = [(1, 4), (2, 8), (3, 12), (4, 16), (5, 20)]
        dots = VGroup()
        coord_labels = VGroup()

        for x_val, y_val in points_data:
            point = np.array([x_to_px(x_val), y_to_px(y_val), 0])
            dot = Dot(point, color=GREEN, radius=0.1)
            dots.add(dot)
            coord = Text(f"({x_val}, {y_val})", font_size=18, color=GREEN)
            coord.next_to(point, UP if x_val % 2 == 1 else DOWN, buff=0.1)
            coord_labels.add(coord)

        # Animate the dots appearing
        for i, (x_val, y_val) in enumerate(points_data):
            calc_text = Text(
                f"y = {k} x {x_val} = {y_val}",
                font_size=22, color=GREEN
            )
            calc_text.next_to(graph_line, DOWN, buff=0.3)
            if i == 0:
                self.play(Write(calc_text))
            else:
                self.play(Transform(prev_calc, calc_text))

            self.play(
                Create(dots[i]),
                Write(coord_labels[i])
            )
            self.wait(0.2)
            prev_calc = calc_text

        self.play(FadeOut(prev_calc))

        # Show constant of proportionality
        k_box = Rectangle(width=5, height=0.8, color=GREEN, fill_opacity=0.1)
        k_box.to_edge(DOWN, buff=0.3)
        k_text = Text(
            "k = y/x = 4 (constant for all points)",
            font_size=24, color=GREEN
        )
        k_text.move_to(k_box.get_center())

        self.play(Create(k_box), Write(k_text))
        self.wait(0.5)

        # Highlight the constant ratio property
        for dot in dots:
            self.play(Indicate(dot, color=YELLOW, scale_factor=1.3))
            self.wait(0.1)

        self.wait(0.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = DirectProportionGraph()
    scene.render()
