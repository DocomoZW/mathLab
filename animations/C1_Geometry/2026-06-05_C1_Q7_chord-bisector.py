from manim import *
import numpy as np

class C1Q7ChordBisector(Scene):
    def construct(self):
        title = Text("Chord Bisector Theorem", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Draw circle centered at origin
        circle = Circle(radius=2.8, color=BLUE, stroke_width=3)
        circle.move_to(ORIGIN)
        self.play(Create(circle))
        self.wait(0.3)

        # Center point
        center = Dot(ORIGIN, color=WHITE, radius=0.07)
        center_label = Text("O", font_size=22, color=WHITE)
        center_label.next_to(ORIGIN, DOWN+RIGHT, buff=0.15)
        self.play(Create(center), Write(center_label))
        self.wait(0.2)

        # Draw a chord (not horizontal, not through center)
        chord_start_angle = 2.0  # radians
        chord_end_angle = -0.8
        chord_start = np.array([2.8 * np.cos(chord_start_angle), 2.8 * np.sin(chord_start_angle), 0])
        chord_end = np.array([2.8 * np.cos(chord_end_angle), 2.8 * np.sin(chord_end_angle), 0])

        chord = Line(chord_start, chord_end, color=GREEN, stroke_width=3)
        self.play(Create(chord))
        self.wait(0.3)

        # Label chord endpoints
        label_start = Text("A", font_size=22, color=GREEN)
        label_start.next_to(chord_start, UP, buff=0.15)
        label_end = Text("B", font_size=22, color=GREEN)
        label_end.next_to(chord_end, DOWN, buff=0.15)
        self.play(Write(label_start), Write(label_end))
        self.wait(0.2)

        # Find midpoint of chord
        chord_mid = (chord_start + chord_end) / 2

        # Perpendicular from center to chord
        # Direction from center to midpoint
        perp_dir = chord_mid - ORIGIN
        perp_dir = perp_dir / np.linalg.norm(perp_dir) * 2.8

        # Perpendicular line (from center to chord)
        perp_line = Line(ORIGIN, chord_mid, color=RED, stroke_width=3)
        self.play(Create(perp_line))
        self.wait(0.3)

        # Right angle marker at intersection
        ra_size = 0.25
        chord_dir = chord_end - chord_start
        chord_perp = np.array([-chord_dir[1], chord_dir[0], 0])
        chord_perp = chord_perp / np.linalg.norm(chord_perp)

        p1 = chord_mid + chord_perp * ra_size
        p2 = chord_mid + chord_perp * ra_size + (chord_mid / np.linalg.norm(chord_mid)) * ra_size
        p3 = chord_mid + (chord_mid / np.linalg.norm(chord_mid)) * ra_size

        # Flip if needed to go the right direction
        dot_product = np.dot(chord_mid / np.linalg.norm(chord_mid), chord_perp)
        if dot_product < 0:
            chord_perp = -chord_perp
            p1 = chord_mid + chord_perp * ra_size
            p2 = chord_mid + chord_perp * ra_size + (chord_mid / np.linalg.norm(chord_mid)) * ra_size
            p3 = chord_mid + (chord_mid / np.linalg.norm(chord_mid)) * ra_size

        right_angle = Polygon(chord_mid, p1, p2, p3,
                              color=RED, stroke_width=2.5, fill_opacity=0)
        self.play(Create(right_angle))

        # Label the perpendicular
        perp_text = Text("Perpendicular from center", font_size=18, color=RED)
        perp_text.next_to(perp_line, LEFT, buff=0.3)
        self.play(Write(perp_text))
        self.wait(0.3)

        # Show that chord is bisected
        bisect_text = Text("Chord is bisected", font_size=20, color=YELLOW)
        bisect_text.to_edge(DOWN, buff=0.6)
        self.play(Write(bisect_text))
        self.wait(0.3)

        # Mark the two equal halves
        half1 = Line(chord_start, chord_mid, color=ORANGE, stroke_width=6)
        half2 = Line(chord_mid, chord_end, color=ORANGE, stroke_width=6)
        self.play(
            Transform(chord.copy(), half1),
            Transform(chord.copy(), half2),
        )
        self.wait(0.3)

        # Draw equal tick marks on both halves
        def draw_tick_on_segment(start, end, color=WHITE):
            mid = (start + end) / 2
            direction = end - start
            perp = np.array([-direction[1], direction[0], 0])
            norm = np.linalg.norm(perp[:2])
            if norm > 0:
                perp = perp / norm * 0.12
            else:
                perp = np.array([0, 0.12, 0])
            return Line(mid - perp, mid + perp, color=color, stroke_width=2.5)

        tick1 = draw_tick_on_segment(chord_start, chord_mid, WHITE)
        tick2 = draw_tick_on_segment(chord_mid, chord_end, WHITE)
        self.play(Create(tick1), Create(tick2))

        # Label the midpoint
        mid_label = Text("M", font_size=20, color=ORANGE)
        mid_label.next_to(chord_mid, DOWN+RIGHT, buff=0.1)
        self.play(Write(mid_label))

        # Equal length labels
        eq1 = Text("AM", font_size=18, color=ORANGE)
        eq1.next_to(half1, DOWN, buff=0.15)
        eq2 = Text("MB", font_size=18, color=ORANGE)
        eq2.next_to(half2, DOWN, buff=0.15)
        self.play(Write(eq1), Write(eq2))
        self.wait(0.3)

        # Theorem statement
        theorem = Text("A line from center perpendicular to a chord", font_size=22, color=YELLOW)
        theorem.next_to(bisect_text, DOWN, buff=0.2)
        theorem2 = Text("bisects the chord", font_size=22, color=YELLOW)
        theorem2.next_to(theorem, DOWN, buff=0.15)
        self.play(Write(theorem), Write(theorem2))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
