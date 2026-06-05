# topic_id: A1_Q5
# track: igcse_o
# unit: A1_Number
# description: Upper/lower bounds with error intervals for a measurement of 7.3 cm (1 d.p.)

from manim import *
import numpy as np

class BoundsErrorIntervals(Scene):
    def construct(self):
        # Title
        title = Text("Bounds & Error Intervals: 7.3 cm (1 d.p.)", font_size=34, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Show the measurement
        measurement = Text("7.3 cm", font_size=48, color=YELLOW)
        measurement.shift(UP * 1.2)
        self.play(Write(measurement))
        self.wait(0.3)

        # Explanation
        explanation = Text(
            "Rounded to 1 decimal place -> error interval:",
            font_size=20, color=WHITE
        )
        explanation.next_to(measurement, DOWN, buff=0.2)
        self.play(Write(explanation))
        self.wait(0.3)

        # Show the bounds
        bounds = Text(
            "7.25 <= x < 7.35",
            font_size=40, color=YELLOW
        )
        bounds.next_to(explanation, DOWN, buff=0.3)
        self.play(Write(bounds))
        self.wait(0.5)

        # Draw a manual number line using shapes
        line = Line(np.array([-4.5, -0.5, 0]), np.array([4.5, -0.5, 0]), color=WHITE)
        # Tick marks and labels
        ticks = VGroup()
        tick_labels = VGroup()
        values = [7.1, 7.15, 7.2, 7.25, 7.3, 7.35, 7.4, 7.45, 7.5]
        for v in values:
            x = -4.5 + (v - 7.1) / (7.5 - 7.1) * 9.0
            tick = Line(np.array([x, -0.5, 0]), np.array([x, -0.35, 0]), color=WHITE, stroke_width=1.5)
            ticks.add(tick)
            if v in [7.1, 7.25, 7.3, 7.35, 7.5]:
                lbl = Text(f"{v:.2f}", font_size=14, color=WHITE)
                lbl.next_to(tick, DOWN, buff=0.15)
                tick_labels.add(lbl)

        self.play(Create(line), Create(ticks), Write(tick_labels))
        self.wait(0.3)

        # Mark LB at 7.25
        lb_x = -4.5 + (7.25 - 7.1) / (7.5 - 7.1) * 9.0
        ub_x = -4.5 + (7.35 - 7.1) / (7.5 - 7.1) * 9.0
        mid_x = (lb_x + ub_x) / 2

        # Filled interval band
        interval = Rectangle(
            width=ub_x - lb_x,
            height=0.15,
            color=YELLOW,
            fill_color=YELLOW,
            fill_opacity=0.3,
        )
        interval.move_to(np.array([mid_x, -0.5, 0]))

        # Solid dot at LB (inclusive), hollow at UB (exclusive)
        lb_dot = Dot(np.array([lb_x, -0.5, 0]), color=GREEN, radius=0.1)
        ub_dot = Circle(radius=0.1, color=RED, stroke_width=3)
        ub_dot.move_to(np.array([ub_x, -0.5, 0]))

        lb_label = Text("LB 7.25", font_size=20, color=GREEN)
        lb_label.next_to(lb_dot, DOWN, buff=0.4)
        ub_label = Text("UB 7.35", font_size=20, color=RED)
        ub_label.next_to(ub_dot, DOWN, buff=0.4)

        self.play(
            Create(interval),
            Create(lb_dot),
            Create(ub_dot),
            Write(lb_label),
            Write(ub_label)
        )
        self.wait(0.5)

        # Add the measured value point
        mv_x = -4.5 + (7.3 - 7.1) / (7.5 - 7.1) * 9.0
        measured_dot = Dot(np.array([mv_x, -0.5, 0]), color=YELLOW, radius=0.12)
        measured_label = Text("7.3", font_size=22, color=YELLOW)
        measured_label.next_to(measured_dot, UP, buff=0.2)

        self.play(
            Create(measured_dot),
            Write(measured_label)
        )
        self.wait(0.3)

        # Animate the interval boundaries pulsing
        self.play(
            Indicate(lb_dot, color=GREEN, scale_factor=1.5),
            Indicate(ub_dot, color=RED, scale_factor=1.5),
        )
        self.wait(0.3)

        # Key rule box
        rule_box = Rectangle(width=9, height=1.2, color=WHITE, fill_opacity=0.1)
        rule_box.to_edge(DOWN, buff=0.4)

        rule_text = Text(
            "True value lies in: [LB, UB) = [7.25, 7.35)\n"
            "7.35 would round to 7.4, so it is NOT included.",
            font_size=18, color=WHITE, line_spacing=1.3
        )
        rule_text.move_to(rule_box.get_center())

        self.play(Create(rule_box), Write(rule_text))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = BoundsErrorIntervals()
    scene.render()
