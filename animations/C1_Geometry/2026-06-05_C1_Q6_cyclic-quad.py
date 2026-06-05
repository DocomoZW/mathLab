from manim import *
import numpy as np

class C1Q6CyclicQuad(Scene):
    def construct(self):
        title = Text("Cyclic Quadrilateral Theorem", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw circle
        circle = Circle(radius=2.8, color=BLUE, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.3)

        # Place 4 points on circumference
        angles = [PI/2 + 0.4, 0.3, -PI/2 - 0.3, PI + 0.2]
        points = []
        labels = []
        colors = [RED, GREEN, YELLOW, PURPLE]
        label_names = ["A", "B", "C", "D"]

        for i, (angle, col, name) in enumerate(zip(angles, colors, label_names)):
            x = 2.8 * np.cos(angle)
            y = 2.8 * np.sin(angle)
            pos = np.array([x, y, 0])
            points.append(pos)
            dot = Dot(pos, color=col, radius=0.08)
            lbl = Text(name, font_size=22, color=col)
            # Position label outside the circle
            lbl.next_to(pos, pos / np.linalg.norm(pos) * 0.4)
            self.play(Create(dot), Write(lbl), run_time=0.3)
            labels.append(lbl)

        self.wait(0.3)

        # Connect to form cyclic quadrilateral
        lines = []
        for i in range(4):
            line = Line(points[i], points[(i+1) % 4], color=WHITE, stroke_width=2.5)
            lines.append(line)
            self.play(Create(line), run_time=0.2)

        self.wait(0.4)

        # Show first pair of opposite angles (A and C)
        pair1_label = Text("Opposite angles: A and C", font_size=22, color=YELLOW)
        pair1_label.to_edge(DOWN, buff=0.8)
        self.play(Write(pair1_label))
        self.wait(0.2)

        # Highlight vertices A and C
        a_dot = Dot(points[0], color=RED, radius=0.12)
        c_dot = Dot(points[2], color=RED, radius=0.12)
        self.play(
            Transform(Dot(points[0], radius=0.08).copy(), a_dot),
            Transform(Dot(points[2], radius=0.08).copy(), c_dot),
        )
        self.wait(0.2)

        # Draw angle arcs at A and C
        # Angle at A
        ab_dir = points[1] - points[0]
        ad_dir = points[3] - points[0]
        angle_a_start = np.arctan2(ad_dir[1], ad_dir[0])
        angle_a_end = np.arctan2(ab_dir[1], ab_dir[0])
        if angle_a_start > angle_a_end:
            angle_a_start, angle_a_end = angle_a_end, angle_a_start
        arc_a = Arc(radius=0.4, start_angle=angle_a_start, angle=angle_a_end - angle_a_start,
                    color=RED, stroke_width=4)
        arc_a.shift(points[0])

        # Angle at C
        cb_dir = points[1] - points[2]
        cd_dir = points[3] - points[2]
        angle_c_start = np.arctan2(cd_dir[1], cd_dir[0])
        angle_c_end = np.arctan2(cb_dir[1], cb_dir[0])
        if angle_c_start > angle_c_end:
            angle_c_start, angle_c_end = angle_c_end, angle_c_start
        arc_c = Arc(radius=0.4, start_angle=angle_c_start, angle=angle_c_end - angle_c_start,
                    color=RED, stroke_width=4)
        arc_c.shift(points[2])

        self.play(Create(arc_a), Create(arc_c))
        self.wait(0.3)

        # Show sum = 180
        sum_text1 = Text("A + C = 180 degrees", font_size=20, color=RED)
        sum_text1.next_to(pair1_label, DOWN, buff=0.3)
        self.play(Write(sum_text1))
        self.wait(0.5)

        # Clear first pair
        self.play(FadeOut(arc_a), FadeOut(arc_c), FadeOut(a_dot), FadeOut(c_dot),
                  FadeOut(pair1_label), FadeOut(sum_text1))

        # Show second pair of opposite angles (B and D)
        pair2_label = Text("Opposite angles: B and D", font_size=22, color=YELLOW)
        pair2_label.to_edge(DOWN, buff=0.8)
        self.play(Write(pair2_label))
        self.wait(0.2)

        # Highlight vertices B and D
        b_dot = Dot(points[1], color=GREEN, radius=0.12)
        d_dot = Dot(points[3], color=GREEN, radius=0.12)
        self.play(
            Transform(Dot(points[1], radius=0.08).copy(), b_dot),
            Transform(Dot(points[3], radius=0.08).copy(), d_dot),
        )

        # Draw angle arcs at B and D
        ba_dir = points[0] - points[1]
        bc_dir = points[2] - points[1]
        angle_b_start = np.arctan2(bc_dir[1], bc_dir[0])
        angle_b_end = np.arctan2(ba_dir[1], ba_dir[0])
        if angle_b_start > angle_b_end:
            angle_b_start, angle_b_end = angle_b_end, angle_b_start
        arc_b = Arc(radius=0.4, start_angle=angle_b_start, angle=angle_b_end - angle_b_start,
                    color=GREEN, stroke_width=4)
        arc_b.shift(points[1])

        da_dir = points[0] - points[3]
        dc_dir = points[2] - points[3]
        angle_d_start = np.arctan2(dc_dir[1], dc_dir[0])
        angle_d_end = np.arctan2(da_dir[1], da_dir[0])
        if angle_d_start > angle_d_end:
            angle_d_start, angle_d_end = angle_d_end, angle_d_start
        arc_d = Arc(radius=0.4, start_angle=angle_d_start, angle=angle_d_end - angle_d_start,
                    color=GREEN, stroke_width=4)
        arc_d.shift(points[3])

        self.play(Create(arc_b), Create(arc_d))
        self.wait(0.3)

        sum_text2 = Text("B + D = 180 degrees", font_size=20, color=GREEN)
        sum_text2.next_to(pair2_label, DOWN, buff=0.3)
        self.play(Write(sum_text2))
        self.wait(0.5)

        self.play(FadeOut(arc_b), FadeOut(arc_d), FadeOut(b_dot), FadeOut(d_dot),
                  FadeOut(pair2_label), FadeOut(sum_text2))

        # Final theorem statement
        theorem = Text("Opposite angles in a cyclic quadrilateral", font_size=24, color=YELLOW)
        theorem.to_edge(DOWN, buff=0.5)
        theorem2 = Text("sum to 180 degrees", font_size=24, color=YELLOW)
        theorem2.next_to(theorem, DOWN, buff=0.2)
        self.play(Write(theorem), Write(theorem2))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
