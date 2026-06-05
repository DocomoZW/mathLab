from manim import *

class C1Q1ProtractorMeasure(Scene):
    def construct(self):
        title = Text("Measuring an Angle", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Vertex and rays
        vertex = np.array([0, -1.0, 0])
        ray_len = 2.5

        # First ray (horizontal, pointing right)
        ray1 = Line(vertex, vertex + np.array([ray_len, 0, 0]), color=BLUE, stroke_width=4)
        # Second ray at 55 degrees
        angle_deg = 55
        angle_rad = angle_deg * DEGREES
        ray2_end = vertex + np.array([
            ray_len * np.cos(angle_rad),
            ray_len * np.sin(angle_rad),
            0
        ])
        ray2 = Line(vertex, ray2_end, color=RED, stroke_width=4)

        self.play(Create(ray1), Create(ray2))
        self.wait(0.3)

        # Dot at vertex
        dot = Dot(vertex, color=WHITE, radius=0.05)
        self.play(Create(dot))
        self.wait(0.3)

        # Draw protractor semicircle
        prot_radius = 2.0
        protractor = Arc(
            radius=prot_radius,
            start_angle=0,
            angle=PI,
            color=GREY,
            stroke_width=2
        )
        protractor.move_arc_center_to(vertex)

        # Tick marks on protractor (every 10 degrees)
        ticks = VGroup()
        for deg in range(0, 181, 10):
            rad = deg * DEGREES
            inner = prot_radius - 0.1 if deg % 30 == 0 else prot_radius - 0.06
            outer = prot_radius
            p1 = vertex + np.array([inner * np.cos(rad), inner * np.sin(rad), 0])
            p2 = vertex + np.array([outer * np.cos(rad), outer * np.sin(rad), 0])
            tick = Line(p1, p2, color=GREY, stroke_width=1.5)
            ticks.add(tick)
            # Label every 30 degrees
            if deg % 30 == 0 and deg > 0 and deg < 180:
                lbl_pos = prot_radius + 0.3
                lbl = Text(str(deg), font_size=10, color=GREY)
                lbl.move_to(vertex + np.array([
                    lbl_pos * np.cos(rad),
                    lbl_pos * np.sin(rad),
                    0
                ]))
                ticks.add(lbl)

        # Center label "0" and "180"
        lbl_0 = Text("0", font_size=10, color=GREY)
        lbl_0.move_to(vertex + np.array([1.5, -0.3, 0]))
        lbl_180 = Text("180", font_size=10, color=GREY)
        lbl_180.move_to(vertex + np.array([-1.7, -0.3, 0]))

        self.play(Create(protractor), Create(ticks), Write(lbl_0), Write(lbl_180))
        self.wait(0.5)

        # Draw the arc between the two rays (the measured angle)
        measure_arc = Arc(
            radius=0.6,
            start_angle=0,
            angle=angle_rad,
            color=YELLOW,
            stroke_width=5
        )
        measure_arc.move_arc_center_to(vertex)
        self.play(Create(measure_arc))
        self.wait(0.3)

        # Arrow pointing at the arc from the side
        arrow_pos = vertex + np.array([0.9 * np.cos(angle_rad / 2), 0.9 * np.sin(angle_rad / 2), 0])
        arrow = Arrow(
            start=arrow_pos + np.array([0.4, 0.3, 0]),
            end=arrow_pos,
            color=YELLOW,
            stroke_width=2,
            tip_length=0.12
        )
        self.play(Create(arrow))

        # Show the measure
        measure = Text("55 degrees", font_size=22, color=YELLOW)
        measure.next_to(arrow_pos, UP * 0.8 + RIGHT * 0.3)
        self.play(Write(measure))
        self.wait(1.0)

        # Show label
        angle_label = Text("Angle = 55 deg", font_size=20, color=WHITE)
        angle_label.next_to(vertex, DOWN * 1.2)
        self.play(Write(angle_label))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
