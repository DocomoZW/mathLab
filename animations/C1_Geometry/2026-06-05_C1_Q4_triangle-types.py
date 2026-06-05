from manim import *

class C1Q4TriangleTypes(Scene):
    def construct(self):
        title = Text("Types of Triangles by Sides", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # We'll show 3 triangles side by side
        # Equilateral, Isosceles, Scalene

        # ---- Triangle 1: Equilateral ----
        tri1_pos = np.array([-3.2, 0, 0])
        # All sides equal, all angles 60 deg
        side_len = 1.5
        # Equilateral triangle pointing up
        p1 = tri1_pos + np.array([0, side_len * np.sqrt(3)/3, 0])  # top
        p2 = tri1_pos + np.array([-side_len/2, -side_len * np.sqrt(3)/6, 0])  # bottom-left
        p3 = tri1_pos + np.array([side_len/2, -side_len * np.sqrt(3)/6, 0])  # bottom-right

        tri1 = Polygon(p1, p2, p3, color=BLUE, stroke_width=4)
        tri1_name = Text("Equilateral", font_size=18, color=BLUE)
        tri1_name.next_to(tri1, DOWN * 1.2)

        # Side marks (single tick on each side)
        mid12 = (p1 + p2) / 2
        mid23 = (p2 + p3) / 2
        mid31 = (p3 + p1) / 2
        # Perpendicular direction to each side
        def perp(p_a, p_b):
            d = p_b - p_a
            return np.array([-d[1], d[0], 0]) / np.linalg.norm(d) * 0.12

        tick1_1 = Line(mid12 + perp(p1, p2), mid12 - perp(p1, p2), color=BLUE, stroke_width=2)
        tick1_2 = Line(mid23 + perp(p2, p3), mid23 - perp(p2, p3), color=BLUE, stroke_width=2)
        tick1_3 = Line(mid31 + perp(p3, p1), mid31 - perp(p3, p1), color=BLUE, stroke_width=2)

        tri1_prop = Text("3 equal sides", font_size=14, color=BLUE)
        tri1_prop.next_to(tri1_name, DOWN * 0.5)

        # ---- Triangle 2: Isosceles ----
        tri2_pos = np.array([0, 0, 0])
        # Two equal sides
        base_w = 1.8
        height = 1.6
        q1 = tri2_pos + np.array([0, height * 0.6, 0])  # top vertex
        q2 = tri2_pos + np.array([-base_w/2, -height * 0.4, 0])  # bottom-left
        q3 = tri2_pos + np.array([base_w/2, -height * 0.4, 0])  # bottom-right

        tri2 = Polygon(q1, q2, q3, color=GREEN, stroke_width=4)
        tri2_name = Text("Isosceles", font_size=18, color=GREEN)
        tri2_name.next_to(tri2, DOWN * 1.2)

        # Side marks: equal sides get double ticks, base gets single
        mid_eq1 = (q1 + q2) / 2
        mid_eq2 = (q1 + q3) / 2
        mid_base = (q2 + q3) / 2

        # Double tick on equal sides
        def perp_d(p_a, p_b, offset=0.06):
            d = p_b - p_a
            return np.array([-d[1], d[0], 0]) / np.linalg.norm(d)

        perp_dir = perp_d(q1, q2)
        tick2_1a = Line(mid_eq1 + perp_dir * 0.06, mid_eq1 - perp_dir * 0.06, color=GREEN, stroke_width=2)
        tick2_1b = Line(mid_eq1 + perp_dir * 0.06 + perp_dir * 0.12, mid_eq1 - perp_dir * 0.06 + perp_dir * 0.12,
                        color=GREEN, stroke_width=2)

        perp_dir2 = perp_d(q1, q3)
        tick2_2a = Line(mid_eq2 + perp_dir2 * 0.06, mid_eq2 - perp_dir2 * 0.06, color=GREEN, stroke_width=2)
        tick2_2b = Line(mid_eq2 + perp_dir2 * 0.06 + perp_dir2 * 0.12, mid_eq2 - perp_dir2 * 0.06 + perp_dir2 * 0.12,
                        color=GREEN, stroke_width=2)

        # Single tick on base
        tick2_3 = Line(mid_base + perp_d(q2, q3) * 0.1, mid_base - perp_d(q2, q3) * 0.1, color=GREEN, stroke_width=2)

        tri2_prop = Text("2 equal sides", font_size=14, color=GREEN)
        tri2_prop.next_to(tri2_name, DOWN * 0.5)

        # ---- Triangle 3: Scalene ----
        tri3_pos = np.array([3.2, 0, 0])
        # All sides different
        r1 = tri3_pos + np.array([0, 1.5, 0])
        r2 = tri3_pos + np.array([-1.2, -0.8, 0])
        r3 = tri3_pos + np.array([0.8, -0.5, 0])

        tri3 = Polygon(r1, r2, r3, color=RED, stroke_width=4)
        tri3_name = Text("Scalene", font_size=18, color=RED)
        tri3_name.next_to(tri3, DOWN * 1.2)

        # Different tick marks for each side
        mid_s1 = (r1 + r2) / 2
        mid_s2 = (r2 + r3) / 2
        mid_s3 = (r3 + r1) / 2

        def perp_d2(p_a, p_b):
            d = p_b - p_a
            return np.array([-d[1], d[0], 0]) / np.linalg.norm(d)

        # Single tick
        tick3_1 = Line(mid_s1 + perp_d2(r1, r2) * 0.1, mid_s1 - perp_d2(r1, r2) * 0.1, color=RED, stroke_width=2)
        # Double tick
        tick3_2a = Line(mid_s2 + perp_d2(r2, r3) * 0.06, mid_s2 - perp_d2(r2, r3) * 0.06, color=RED, stroke_width=2)
        tick3_2b = Line(mid_s2 + perp_d2(r2, r3) * 0.06 + perp_d2(r2, r3) * 0.12,
                        mid_s2 - perp_d2(r2, r3) * 0.06 + perp_d2(r2, r3) * 0.12, color=RED, stroke_width=2)
        # Triple tick
        tick3_3a = Line(mid_s3 + perp_d2(r3, r1) * 0.04, mid_s3 - perp_d2(r3, r1) * 0.04, color=RED, stroke_width=2)
        tick3_3b = Line(mid_s3 + perp_d2(r3, r1) * 0.04 + perp_d2(r3, r1) * 0.1,
                        mid_s3 - perp_d2(r3, r1) * 0.04 + perp_d2(r3, r1) * 0.1, color=RED, stroke_width=2)
        tick3_3c = Line(mid_s3 + perp_d2(r3, r1) * 0.04 + perp_d2(r3, r1) * 0.2,
                        mid_s3 - perp_d2(r3, r1) * 0.04 + perp_d2(r3, r1) * 0.2, color=RED, stroke_width=2)

        tri3_prop = Text("No equal sides", font_size=14, color=RED)
        tri3_prop.next_to(tri3_name, DOWN * 0.5)

        # Animate triangles appearing one by one
        # Triangle 1: Equilateral
        self.play(Create(tri1))
        self.play(Write(tri1_name))
        self.play(
            Create(tick1_1), Create(tick1_2), Create(tick1_3),
            Write(tri1_prop)
        )
        self.wait(0.4)

        # Short animation: show sides changing length (pulse effect)
        self.play(
            tri1.animate.set_stroke(width=6),
            run_time=0.2
        )
        self.play(
            tri1.animate.set_stroke(width=4),
            run_time=0.2
        )
        self.wait(0.2)

        # Triangle 2: Isosceles
        self.play(Create(tri2))
        self.play(Write(tri2_name))
        self.play(
            Create(tick2_1a), Create(tick2_1b),
            Create(tick2_2a), Create(tick2_2b),
            Create(tick2_3),
            Write(tri2_prop)
        )
        self.wait(0.4)

        # Pulse effect
        self.play(
            tri2.animate.set_stroke(width=6),
            run_time=0.2
        )
        self.play(
            tri2.animate.set_stroke(width=4),
            run_time=0.2
        )
        self.wait(0.2)

        # Triangle 3: Scalene
        self.play(Create(tri3))
        self.play(Write(tri3_name))
        self.play(
            Create(tick3_1), Create(tick3_2a), Create(tick3_2b),
            Create(tick3_3a), Create(tick3_3b), Create(tick3_3c),
            Write(tri3_prop)
        )
        self.wait(0.4)

        # Pulse effect
        self.play(
            tri3.animate.set_stroke(width=6),
            run_time=0.2
        )
        self.play(
            tri3.animate.set_stroke(width=4),
            run_time=0.2
        )
        self.wait(0.3)

        # Summary
        summary = Text("Triangles classified by side lengths", font_size=18, color=WHITE)
        summary.next_to(tri3_prop, DOWN * 1.5)
        self.play(Write(summary))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
