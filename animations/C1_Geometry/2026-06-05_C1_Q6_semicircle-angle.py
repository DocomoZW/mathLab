from manim import *
import numpy as np

class C1Q6SemicircleAngle(Scene):
    def construct(self):
        title = Text("Angle in a Semicircle Theorem", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw circle
        circle = Circle(radius=2.5, color=BLUE, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.2)

        # Draw diameter (horizontal line through center)
        left = circle.get_left()
        right = circle.get_right()
        diameter = Line(left, right, color=YELLOW, stroke_width=3)
        self.play(Create(diameter))
        self.wait(0.2)

        # Label endpoints
        label_left = Text("A", font_size=22, color=WHITE).next_to(left, LEFT, buff=0.15)
        label_right = Text("B", font_size=22, color=WHITE).next_to(right, RIGHT, buff=0.15)
        center_label = Text("O", font_size=20, color=WHITE).next_to(ORIGIN, DOWN, buff=0.15)
        self.play(Write(label_left), Write(label_right), Write(center_label))
        self.wait(0.3)

        # Add point on circumference at top
        top_point = circle.get_top()
        moving_dot = Dot(top_point, color=RED, radius=0.08)
        point_label = Text("P", font_size=22, color=RED).next_to(top_point, UP, buff=0.15)
        self.play(Create(moving_dot), Write(point_label))
        self.wait(0.2)

        # Connect to form triangle
        line_pa = Line(top_point, left, color=GREEN, stroke_width=2.5)
        line_pb = Line(top_point, right, color=GREEN, stroke_width=2.5)
        self.play(Create(line_pa), Create(line_pb))
        self.wait(0.3)

        # Show angle at P
        angle_text = Text("Angle APB = 90 degrees", font_size=22, color=YELLOW)
        angle_text.to_edge(DOWN)
        self.play(Write(angle_text))
        self.wait(0.3)

        # Draw right angle marker at P
        # Vectors PA and PB
        v_pa = left - top_point
        v_pb = right - top_point
        angle_at_p = np.arctan2(v_pa[1], v_pa[0])
        angle_at_pb = np.arctan2(v_pb[1], v_pb[0])

        # Draw a small right angle square
        ra_size = 0.25
        # Direction from P to A and P to B, normalized
        pa_dir = v_pa / np.linalg.norm(v_pa[:2])
        pb_dir = v_pb / np.linalg.norm(v_pb[:2])

        p1 = top_point + pa_dir * ra_size
        p2 = top_point + pa_dir * ra_size + pb_dir * ra_size
        p3 = top_point + pb_dir * ra_size

        right_angle_square = Polygon(
            top_point, p1, p2, p3,
            color=YELLOW, stroke_width=2.5, fill_opacity=0
        )
        self.play(Create(right_angle_square))
        self.wait(0.5)

        # Animate point moving along circumference, showing angle stays 90
        moving_text = Text("Angle stays 90 degrees as P moves", font_size=20, color=ORANGE)
        moving_text.next_to(angle_text, DOWN, buff=0.2)
        self.play(Write(moving_text))

        # Animate the point moving along the semicircle (upper half)
        dot_copy = moving_dot.copy()
        label_copy = point_label.copy()
        self.play(FadeOut(moving_dot), FadeOut(point_label))

        # Create new dot
        new_dot = Dot(top_point, color=RED, radius=0.08)
        new_label = Text("P", font_size=22, color=RED).next_to(top_point, UP, buff=0.15)
        self.add(new_dot, new_label)

        # Move point along upper semicircle (right side then left side)
        for angle in np.linspace(PI/2, -PI/2, 30):
            x = 2.5 * np.cos(angle)
            y = 2.5 * np.sin(angle)
            new_pos = np.array([x, y, 0])
            new_dot.move_to(new_pos)
            new_label.next_to(new_pos, UP if y > 0 else (RIGHT if x > 0 else LEFT), buff=0.15)

            # Update lines
            new_line_pa = Line(new_pos, left, color=GREEN, stroke_width=2.5)
            new_line_pb = Line(new_pos, right, color=GREEN, stroke_width=2.5)

            # Update right angle square
            v_pa_new = left - new_pos
            v_pb_new = right - new_pos
            if np.linalg.norm(v_pa_new[:2]) > 0 and np.linalg.norm(v_pb_new[:2]) > 0:
                pa_dir_new = v_pa_new / np.linalg.norm(v_pa_new[:2])
                pb_dir_new = v_pb_new / np.linalg.norm(v_pb_new[:2])
                p1_new = new_pos + pa_dir_new * ra_size
                p2_new = new_pos + pa_dir_new * ra_size + pb_dir_new * ra_size
                p3_new = new_pos + pb_dir_new * ra_size

                new_ra = Polygon(new_pos, p1_new, p2_new, p3_new, color=YELLOW, stroke_width=2.5, fill_opacity=0)
                self.play(
                    Transform(line_pa, new_line_pa),
                    Transform(line_pb, new_line_pb),
                    Transform(right_angle_square, new_ra),
                    run_time=0.08
                )
            self.wait(0.02)

        self.wait(0.5)

        # Summary
        summary = Text("Theorem: Angle in a semicircle is always 90 degrees", font_size=22, color=GREEN)
        summary.to_edge(DOWN, buff=0.1)
        self.play(FadeOut(angle_text), FadeOut(moving_text), Write(summary))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
