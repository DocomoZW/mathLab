from manim import *

class C1Q2ParallelLines(Scene):
    def construct(self):
        title = Text("Corresponding Angles (F-Pattern)", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Two parallel horizontal lines
        line1 = Line(np.array([-4, 1.5, 0]), np.array([4, 1.5, 0]), color=BLUE, stroke_width=4)
        line2 = Line(np.array([-4, -1.5, 0]), np.array([4, -1.5, 0]), color=BLUE, stroke_width=4)

        # Arrow markers for parallel direction
        arrow1 = Arrow(np.array([-4, 1.5, 0]), np.array([-3.5, 1.5, 0]),
                       color=BLUE, stroke_width=2, tip_length=0.1)
        arrow2 = Arrow(np.array([-4, -1.5, 0]), np.array([-3.5, -1.5, 0]),
                       color=BLUE, stroke_width=2, tip_length=0.1)

        # Parallel symbol "//"
        par1 = Line(np.array([-4.0, 0.2, 0]), np.array([-4.0, -0.2, 0]), color=BLUE, stroke_width=3)
        par2 = Line(np.array([-3.85, 0.2, 0]), np.array([-3.85, -0.2, 0]), color=BLUE, stroke_width=3)

        self.play(Create(line1), Create(line2))
        self.play(Create(arrow1), Create(arrow2), Create(par1), Create(par2))
        self.wait(0.5)

        # Transversal (slanted line crossing both)
        trans = Line(np.array([-3.5, -2.5, 0]), np.array([3.5, 2.5, 0]),
                     color=WHITE, stroke_width=3)
        self.play(Create(trans))
        self.wait(0.3)

        # Intersection points
        # int1 (top): trans from (-3.5,-2.5) to (3.5,2.5), find y=1.5
        # param t: y = -2.5 + 5t = 1.5 => t = 0.8, x = -3.5 + 7*0.8 = 2.1
        int1 = np.array([2.1, 1.5, 0])
        # int2 (bottom): y = -1.5 => t = 0.2, x = -3.5 + 7*0.2 = -2.1
        int2 = np.array([-2.1, -1.5, 0])

        dot1 = Dot(int1, color=WHITE, radius=0.05)
        dot2 = Dot(int2, color=WHITE, radius=0.05)
        self.play(Create(dot1), Create(dot2))
        self.wait(0.2)

        # Angle directions
        # At int1: horizontal goes left (PI) and right (0)
        # Trans goes down-left from int1: td_angle = angle of (int2 - int1)
        td_angle = np.arctan2(-3.0, -4.2)  # ~ -2.52 rad, need positive
        if td_angle < 0:
            td_angle += 2 * PI
        # Trans goes up-right from int1: tu_angle = angle of (int1 - int2)
        tu_angle = np.arctan2(3.0, 4.2)  # ~ 0.623 rad

        # At int2: same directions but trans goes up-right from int2 = tu_angle
        # and trans goes down-left from int2 = td_angle
        r = 0.4

        # ---- TOP INTERSECTION ----
        # Top-left (RED): between left (PI) and trans-down (td_angle)
        arc_tl1 = Arc(radius=r, start_angle=PI, angle=td_angle - PI,
                      color=RED, stroke_width=6)
        arc_tl1.move_arc_center_to(int1)

        # Top-right (BLUE): between right (0) and trans-up (tu_angle)
        arc_tr1 = Arc(radius=r, start_angle=0, angle=tu_angle,
                      color=BLUE, stroke_width=6)
        arc_tr1.move_arc_center_to(int1)

        # Bottom-right (GREEN): large arc between trans-down and right
        arc_br1 = Arc(radius=r, start_angle=td_angle, angle=2*PI - td_angle,
                      color=GREEN, stroke_width=6)
        arc_br1.move_arc_center_to(int1)

        # Bottom-left (YELLOW): large arc between trans-up and left
        arc_bl1 = Arc(radius=r, start_angle=tu_angle, angle=2*PI - tu_angle,
                      color=YELLOW, stroke_width=6)
        arc_bl1.move_arc_center_to(int1)

        # ---- BOTTOM INTERSECTION ----
        # Corresponding to top-left (RED): bottom-left
        # At int2: left (PI) and trans-up (tu_angle) - the smaller angle goes upward
        # The corresponding angle to top-left is the one at same position relative to parallel lines
        # Top-left = above line, left of trans. Bottom-left = below line, left of trans.
        # At int2: left (PI) to trans-down (td_angle) going counterclockwise gives angle below line.
        arc_tl2 = Arc(radius=r, start_angle=PI, angle=td_angle - PI,
                      color=RED, stroke_width=6)
        arc_tl2.move_arc_center_to(int2)

        # Corresponding to top-right (BLUE): bottom-right
        arc_tr2 = Arc(radius=r, start_angle=0, angle=tu_angle,
                      color=BLUE, stroke_width=6)
        arc_tr2.move_arc_center_to(int2)

        # Corresponding to bottom-right (GREEN): top-right of bottom intersection
        arc_br2 = Arc(radius=r, start_angle=td_angle, angle=2*PI - td_angle,
                      color=GREEN, stroke_width=6)
        arc_br2.move_arc_center_to(int2)

        # Corresponding to bottom-left (YELLOW): top-left of bottom intersection
        arc_bl2 = Arc(radius=r, start_angle=tu_angle, angle=2*PI - tu_angle,
                      color=YELLOW, stroke_width=6)
        arc_bl2.move_arc_center_to(int2)

        # Labels for corresponding pairs
        lbl_a1 = Text("a", font_size=20, color=RED)
        lbl_a1.move_to(int1 + np.array([-0.5, 0.3, 0]))
        lbl_a2 = Text("a", font_size=20, color=RED)
        lbl_a2.move_to(int2 + np.array([-0.5, -0.3, 0]))

        lbl_b1 = Text("b", font_size=20, color=BLUE)
        lbl_b1.move_to(int1 + np.array([0.5, 0.3, 0]))
        lbl_b2 = Text("b", font_size=20, color=BLUE)
        lbl_b2.move_to(int2 + np.array([0.5, -0.3, 0]))

        lbl_c1 = Text("c", font_size=20, color=GREEN)
        lbl_c1.move_to(int1 + np.array([0.5, -0.3, 0]))
        lbl_c2 = Text("c", font_size=20, color=GREEN)
        lbl_c2.move_to(int2 + np.array([0.5, 0.3, 0]))

        lbl_d1 = Text("d", font_size=20, color=YELLOW)
        lbl_d1.move_to(int1 + np.array([-0.5, -0.3, 0]))
        lbl_d2 = Text("d", font_size=20, color=YELLOW)
        lbl_d2.move_to(int2 + np.array([-0.5, 0.3, 0]))

        # Animate all arcs in groups
        self.play(
            Create(arc_tl1), Create(arc_tl2),
            Write(lbl_a1), Write(lbl_a2)
        )
        self.wait(0.3)
        self.play(
            Create(arc_tr1), Create(arc_tr2),
            Write(lbl_b1), Write(lbl_b2)
        )
        self.wait(0.3)
        self.play(
            Create(arc_br1), Create(arc_br2),
            Write(lbl_c1), Write(lbl_c2)
        )
        self.wait(0.3)
        self.play(
            Create(arc_bl1), Create(arc_bl2),
            Write(lbl_d1), Write(lbl_d2)
        )
        self.wait(0.3)

        # Draw F-pattern highlight
        f_vert = Line(int1 + np.array([-0.3, 0, 0]),
                      int2 + np.array([-0.3, 0, 0]),
                      color=RED, stroke_width=4, stroke_opacity=0.5)
        f_top = Line(int1 + np.array([-0.3, 0, 0]),
                     int1 + np.array([-1.2, 0, 0]),
                     color=RED, stroke_width=4, stroke_opacity=0.5)
        f_mid = Line(int2 + np.array([-0.3, 0, 0]),
                     int2 + np.array([-0.8, 0, 0]),
                     color=RED, stroke_width=4, stroke_opacity=0.5)

        self.play(Create(f_vert), Create(f_top), Create(f_mid))
        f_label = Text("F Pattern", font_size=18).next_to(f_top, UP * 0.3)
        self.play(Write(f_label))
        self.wait(0.4)

        caption = Text("Corresponding angles are equal", font_size=20, color=WHITE)
        caption.next_to(int2, DOWN * 0.8)
        self.play(Write(caption))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
