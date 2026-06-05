from manim import *
import numpy as np

class C1Q7TangentRadius(Scene):
    def construct(self):
        title = Text("Tangent-Radius Theorem", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw circle centered at origin
        circle = Circle(radius=2.5, color=BLUE, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.3)

        # Add center point
        center = Dot(ORIGIN, color=WHITE, radius=0.06)
        center_label = Text("O", font_size=20, color=WHITE)
        center_label.next_to(ORIGIN, DOWN, buff=0.15)
        self.play(Create(center), Write(center_label))
        self.wait(0.2)

        # Point of tangency (top-right of circle)
        tangency_angle = 0.5  # radians ~28 degrees
        tangency_point = np.array([2.5 * np.cos(tangency_angle), 2.5 * np.sin(tangency_angle), 0])
        tangency_dot = Dot(tangency_point, color=RED, radius=0.08)
        tangency_label = Text("T", font_size=22, color=RED)
        tangency_label.next_to(tangency_point, UR, buff=0.1)
        self.play(Create(tangency_dot), Write(tangency_label))

        # Draw radius to point of tangency
        radius = Line(ORIGIN, tangency_point, color=YELLOW, stroke_width=3)
        self.play(Create(radius))
        self.wait(0.2)

        # Draw tangent line
        # Tangent direction is perpendicular to radius
        tangent_dir = np.array([-np.sin(tangency_angle), np.cos(tangency_angle), 0])
        tangent_start = tangency_point - tangent_dir * 3.5
        tangent_end = tangency_point + tangent_dir * 3.5
        tangent_line = Line(tangent_start, tangent_end, color=GREEN, stroke_width=3)
        self.play(Create(tangent_line))
        self.wait(0.3)

        # Show right angle between radius and tangent
        ra_size = 0.3
        # Perpendicular direction to radius (tangent direction)
        p1 = tangency_point - tangent_dir * ra_size
        p2 = tangency_point - tangent_dir * ra_size - (tangency_point / np.linalg.norm(tangency_point)) * ra_size
        p3 = tangency_point - (tangency_point / np.linalg.norm(tangency_point)) * ra_size

        right_angle = Polygon(tangency_point, p1, p2, p3,
                              color=YELLOW, stroke_width=2.5, fill_opacity=0)

        angle_label = Text("90 degrees", font_size=18, color=YELLOW)
        angle_label.next_to(right_angle, RIGHT, buff=0.3)
        self.play(Create(right_angle), Write(angle_label))
        self.wait(0.3)

        # Theorem text
        theorem1 = Text("Radius is perpendicular to tangent", font_size=22, color=ORANGE)
        theorem1.to_edge(DOWN, buff=0.8)
        self.play(Write(theorem1))
        self.wait(0.5)

        self.play(FadeOut(theorem1))

        # --- Second part: Two tangents from an external point ---
        part2_label = Text("Two tangents from an external point", font_size=24, color=YELLOW)
        part2_label.next_to(title, DOWN, buff=0.4)
        self.play(Write(part2_label))
        self.wait(0.2)

        # External point
        ext_point = np.array([4, 1.5, 0])
        ext_dot = Dot(ext_point, color=PURPLE, radius=0.08)
        ext_label = Text("P", font_size=22, color=PURPLE)
        ext_label.next_to(ext_point, UR, buff=0.1)
        self.play(Create(ext_dot), Write(ext_label))
        self.wait(0.2)

        # Find tangent points from external point to circle
        # Using geometry: from point P outside circle, find tangent points
        d = np.linalg.norm(ext_point)
        a = 2.5  # radius
        # Distance from center to tangent point along line to P
        l = np.sqrt(d*d - a*a)
        # Angle from center to P
        theta = np.arctan2(ext_point[1], ext_point[0])
        # Angle offset for tangent points
        phi = np.arccos(a / d)

        t1_angle = theta + phi
        t2_angle = theta - phi

        t1_pos = np.array([a * np.cos(t1_angle), a * np.sin(t1_angle), 0])
        t2_pos = np.array([a * np.cos(t2_angle), a * np.sin(t2_angle), 0])

        # Tangent lines from P
        tangent1 = Line(ext_point, t1_pos, color=GREEN, stroke_width=3)
        tangent2 = Line(ext_point, t2_pos, color=GREEN, stroke_width=3)

        # Radius to tangent points
        radius1 = Line(ORIGIN, t1_pos, color=YELLOW, stroke_width=2.5, stroke_opacity=0.7)
        radius2 = Line(ORIGIN, t2_pos, color=YELLOW, stroke_width=2.5, stroke_opacity=0.7)

        # Labels for tangent points
        t1_label = Text("Q", font_size=20, color=RED)
        t1_label.next_to(t1_pos, UP, buff=0.15)
        t2_label = Text("R", font_size=20, color=RED)
        t2_label.next_to(t2_pos, DOWN, buff=0.15)

        self.play(
            Create(tangent1), Create(tangent2),
            Create(radius1), Create(radius2),
            Write(t1_label), Write(t2_label)
        )
        self.wait(0.3)

        # Right angles at tangent points
        # At Q
        t1_rad_dir = t1_pos / np.linalg.norm(t1_pos)
        t1_tan_dir = np.array([-t1_rad_dir[1], t1_rad_dir[0], 0])
        # Direction from Q to P
        qp_dir = ext_point - t1_pos
        qp_dir = qp_dir / np.linalg.norm(qp_dir)
        # Use the tangent direction for the square
        q1 = t1_pos + t1_tan_dir * ra_size
        q2 = t1_pos + t1_tan_dir * ra_size - t1_rad_dir * ra_size
        q3 = t1_pos - t1_rad_dir * ra_size
        ra_q = Polygon(t1_pos, q1, q2, q3, color=YELLOW, stroke_width=2, fill_opacity=0)

        # At R
        t2_rad_dir = t2_pos / np.linalg.norm(t2_pos)
        t2_tan_dir = np.array([-t2_rad_dir[1], t2_rad_dir[0], 0])
        rp_dir = ext_point - t2_pos
        rp_dir = rp_dir / np.linalg.norm(rp_dir)
        r1 = t2_pos + t2_tan_dir * ra_size
        r2 = t2_pos + t2_tan_dir * ra_size - t2_rad_dir * ra_size
        r3 = t2_pos - t2_rad_dir * ra_size
        ra_r = Polygon(t2_pos, r1, r2, r3, color=YELLOW, stroke_width=2, fill_opacity=0)

        self.play(Create(ra_q), Create(ra_r))
        self.wait(0.3)

        # Show equal lengths
        equal_text = Text("PQ = PR (both tangents are equal)", font_size=20, color=GREEN)
        equal_text.to_edge(DOWN)
        self.play(Write(equal_text))

        # Highlight the tangent segments
        t1_highlight = Line(ext_point, t1_pos, color=RED, stroke_width=6)
        t2_highlight = Line(ext_point, t2_pos, color=RED, stroke_width=6)
        self.play(
            Transform(tangent1.copy(), t1_highlight),
            Transform(tangent2.copy(), t2_highlight),
        )
        self.wait(0.5)

        # Mark tick marks on tangents
        tick1 = draw_tick_on_line(ext_point, t1_pos, WHITE)
        tick2 = draw_tick_on_line(ext_point, t2_pos, WHITE)
        self.play(Create(tick1), Create(tick2))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])


def draw_tick_on_line(start, end, color=WHITE):
    """Draw a tick mark at the midpoint of a line."""
    mid = (start + end) / 2
    direction = end - start
    perp = np.array([-direction[1], direction[0], 0])
    norm = np.linalg.norm(perp[:2])
    if norm > 0:
        perp = perp / norm * 0.15
    else:
        perp = np.array([0, 0.15, 0])
    return Line(mid - perp, mid + perp, color=color, stroke_width=2.5)
