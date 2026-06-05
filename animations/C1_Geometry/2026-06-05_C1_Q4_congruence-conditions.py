from manim import *

class C1Q4CongruenceConditions(Scene):
    def construct(self):
        # Title
        title = Text("Triangle Congruence Conditions", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # --- SSS Condition ---
        sss_label = Text("SSS: Three pairs of equal sides", font_size=24, color=YELLOW)
        sss_label.next_to(title, DOWN, buff=0.4)
        self.play(Write(sss_label))
        self.wait(0.3)

        # Left triangle - ABC
        A1 = [-2, 0, 0]
        B1 = [1, -1.5, 0]
        C1 = [0.5, 1.5, 0]

        tri1 = Polygon(A1, B1, C1, color=BLUE, stroke_width=3)
        tri1_label = Text("A", font_size=22, color=BLUE).next_to(A1, UL, buff=0.15)
        tri1_label_b = Text("B", font_size=22, color=BLUE).next_to(B1, DR, buff=0.15)
        tri1_label_c = Text("C", font_size=22, color=BLUE).next_to(C1, UR, buff=0.15)

        self.play(Create(tri1), Write(tri1_label), Write(tri1_label_b), Write(tri1_label_c))
        self.wait(0.3)

        # Right triangle - DEF
        A2 = [3, 0, 0]
        B2 = [6, -1.5, 0]
        C2 = [5.5, 1.5, 0]

        tri2 = Polygon(A2, B2, C2, color=GREEN, stroke_width=3)
        tri2_label = Text("D", font_size=22, color=GREEN).next_to(A2, UL, buff=0.15)
        tri2_label_e = Text("E", font_size=22, color=GREEN).next_to(B2, DR, buff=0.15)
        tri2_label_f = Text("F", font_size=22, color=GREEN).next_to(C2, UR, buff=0.15)

        self.play(Create(tri2), Write(tri2_label), Write(tri2_label_e), Write(tri2_label_f))
        self.wait(0.4)

        # Animate SSS: side pair 1
        side1_text = Text("AB = DE", font_size=20, color=RED)
        side1_text.to_edge(DOWN)
        self.play(Write(side1_text))

        side1_tri1 = Line(A1, B1, color=RED, stroke_width=6)
        side1_tri2 = Line(A2, B2, color=RED, stroke_width=6)
        self.play(
            Transform(tri1.copy(), side1_tri1),
            Transform(tri2.copy(), side1_tri2),
        )
        self.wait(0.4)

        # side pair 2
        side2_text = Text("BC = EF", font_size=20, color=ORANGE)
        side2_text.next_to(side1_text, DOWN, buff=0.2)
        self.play(Write(side2_text))

        side2_tri1 = Line(B1, C1, color=ORANGE, stroke_width=6)
        side2_tri2 = Line(B2, C2, color=ORANGE, stroke_width=6)
        self.play(
            Transform(tri1.copy(), side2_tri1),
            Transform(tri2.copy(), side2_tri2),
        )
        self.wait(0.4)

        # side pair 3
        side3_text = Text("CA = FD", font_size=20, color=PURPLE)
        side3_text.next_to(side2_text, DOWN, buff=0.2)
        self.play(Write(side3_text))

        side3_tri1 = Line(C1, A1, color=PURPLE, stroke_width=6)
        side3_tri2 = Line(C2, A2, color=PURPLE, stroke_width=6)
        self.play(
            Transform(tri1.copy(), side3_tri1),
            Transform(tri2.copy(), side3_tri2),
        )
        self.wait(0.5)

        # Clear for SAS
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])

        # --- SAS Condition ---
        sas_label = Text("SAS: Two sides and included angle", font_size=24, color=YELLOW)
        sas_label.next_to(title, DOWN, buff=0.4)
        self.play(Write(sas_label))
        self.wait(0.3)

        # Left triangle
        t1_a = [-1.5, -1, 0]
        t1_b = [1.5, -1, 0]
        t1_c = [-0.5, 1.5, 0]

        tri_sas1 = Polygon(t1_a, t1_b, t1_c, color=BLUE, stroke_width=3)
        tri_sas1_la = Text("P", font_size=22, color=BLUE).next_to(t1_a, DL, buff=0.15)
        tri_sas1_lb = Text("Q", font_size=22, color=BLUE).next_to(t1_b, DR, buff=0.15)
        tri_sas1_lc = Text("R", font_size=22, color=BLUE).next_to(t1_c, UP, buff=0.15)

        self.play(Create(tri_sas1), Write(tri_sas1_la), Write(tri_sas1_lb), Write(tri_sas1_lc))

        # Right triangle
        t2_a = [4.5, -1, 0]
        t2_b = [7.5, -1, 0]
        t2_c = [5.5, 1.5, 0]

        tri_sas2 = Polygon(t2_a, t2_b, t2_c, color=GREEN, stroke_width=3)
        tri_sas2_la = Text("S", font_size=22, color=GREEN).next_to(t2_a, DL, buff=0.15)
        tri_sas2_lb = Text("T", font_size=22, color=GREEN).next_to(t2_b, DR, buff=0.15)
        tri_sas2_lc = Text("U", font_size=22, color=GREEN).next_to(t2_c, UP, buff=0.15)

        self.play(Create(tri_sas2), Write(tri_sas2_la), Write(tri_sas2_lb), Write(tri_sas2_lc))
        self.wait(0.4)

        # Highlight first side pair
        sas_s1_text = Text("PQ = ST", font_size=20, color=RED)
        sas_s1_text.to_edge(DOWN)
        self.play(Write(sas_s1_text))
        sas_side1_p1 = Line(t1_a, t1_b, color=RED, stroke_width=6)
        sas_side1_p2 = Line(t2_a, t2_b, color=RED, stroke_width=6)
        self.play(
            Transform(tri_sas1.copy(), sas_side1_p1),
            Transform(tri_sas2.copy(), sas_side1_p2),
        )
        self.wait(0.3)

        # Highlight second side pair
        sas_s2_text = Text("PR = SU", font_size=20, color=ORANGE)
        sas_s2_text.next_to(sas_s1_text, DOWN, buff=0.2)
        self.play(Write(sas_s2_text))
        sas_side2_p1 = Line(t1_a, t1_c, color=ORANGE, stroke_width=6)
        sas_side2_p2 = Line(t2_a, t2_c, color=ORANGE, stroke_width=6)
        self.play(
            Transform(tri_sas1.copy(), sas_side2_p1),
            Transform(tri_sas2.copy(), sas_side2_p2),
        )
        self.wait(0.3)

        # Highlight included angle
        sas_angle_text = Text("Angle P = Angle S", font_size=20, color=YELLOW)
        sas_angle_text.next_to(sas_s2_text, DOWN, buff=0.2)
        self.play(Write(sas_angle_text))

        # Draw angle arcs
        angle1 = Arc(radius=0.4, start_angle=PI/2 + 0.5, angle=-1.8, color=YELLOW, stroke_width=4)
        angle1.shift(t1_a)
        angle2 = Arc(radius=0.4, start_angle=PI/2 + 0.5, angle=-1.8, color=YELLOW, stroke_width=4)
        angle2.shift(t2_a)

        self.play(Create(angle1), Create(angle2))
        self.wait(1.0)

        # Final summary
        self.play(*[FadeOut(m) for m in self.mobjects if m != title])
        summary = Text("SSS and SAS prove congruency", font_size=28, color=GREEN)
        summary.move_to(ORIGIN)
        self.play(Write(summary))
        self.wait(1.0)
        self.play(FadeOut(Group(*self.mobjects)))
