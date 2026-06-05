from manim import *

class C1Q2AlternateAngles(Scene):
    def construct(self):
        title = Text("Alternate Angles (Z-Pattern)", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Two parallel horizontal lines
        line1 = Line(np.array([-4, 1.5, 0]), np.array([4, 1.5, 0]), color=BLUE, stroke_width=4)
        line2 = Line(np.array([-4, -1.5, 0]), np.array([4, -1.5, 0]), color=BLUE, stroke_width=4)

        # Arrow markers for parallel
        arrow1 = Arrow(np.array([-4, 1.5, 0]), np.array([-3.5, 1.5, 0]),
                       color=BLUE, stroke_width=2, tip_length=0.1)
        arrow2 = Arrow(np.array([-4, -1.5, 0]), np.array([-3.5, -1.5, 0]),
                       color=BLUE, stroke_width=2, tip_length=0.1)

        par1 = Line(np.array([-4.0, 0.2, 0]), np.array([-4.0, -0.2, 0]), color=BLUE, stroke_width=3)
        par2 = Line(np.array([-3.85, 0.2, 0]), np.array([-3.85, -0.2, 0]), color=BLUE, stroke_width=3)

        self.play(Create(line1), Create(line2))
        self.play(Create(arrow1), Create(arrow2), Create(par1), Create(par2))
        self.wait(0.5)

        # Transversal crossing both (slanted the other way for a clearer Z)
        trans = Line(np.array([-3.5, 2.5, 0]), np.array([3.5, -2.5, 0]),
                     color=WHITE, stroke_width=3)
        self.play(Create(trans))
        self.wait(0.3)

        # Intersection points
        # int1 (top): trans from (-3.5,2.5) to (3.5,-2.5)
        # y=1.5: param t: y = 2.5 - 5t = 1.5 => t = 0.2, x = -3.5 + 7*0.2 = -2.1
        int1 = np.array([-2.1, 1.5, 0])
        # int2 (bottom): y=-1.5 => t = 0.8, x = -3.5 + 7*0.8 = 2.1
        int2 = np.array([2.1, -1.5, 0])

        dot1 = Dot(int1, color=WHITE, radius=0.05)
        dot2 = Dot(int2, color=WHITE, radius=0.05)
        self.play(Create(dot1), Create(dot2))
        self.wait(0.2)

        # Direction angles
        # At int1 (top): trans goes down-right to int2
        # td_angle = angle of (int2 - int1) = (4.2, -3.0)
        td_angle = np.arctan2(-3.0, 4.2)
        if td_angle < 0:
            td_angle += 2 * PI
        # At int1: trans goes up-left in opposite direction
        tu_angle = np.arctan2(3.0, -4.2)
        if tu_angle < 0:
            tu_angle += 2 * PI

        r = 0.4

        # TOP INTERSECTION
        # Top-left (RED): between left (PI) and trans-up-left (tu_angle)
        # Going from PI to tu_angle counterclockwise
        if tu_angle > PI:
            arc_tl1 = Arc(radius=r, start_angle=PI, angle=tu_angle - PI,
                          color=RED, stroke_width=6)
        else:
            arc_tl1 = Arc(radius=r, start_angle=tu_angle, angle=PI - tu_angle,
                          color=RED, stroke_width=6)
        arc_tl1.move_arc_center_to(int1)

        # Top-right (ALTERNATE, RED): between right (0) and trans-down-right (td_angle)
        arc_tr1 = Arc(radius=r, start_angle=0, angle=td_angle,
                      color=RED, stroke_width=6)
        arc_tr1.move_arc_center_to(int1)

        # Bottom intersection
        # Bottom-right (RED, alternate to top-left): between right (0) and trans-down-right (td_angle)
        # Actually, the alternate angle to top-left (above line, left of trans) is
        # bottom-right (below line, right of trans)
        # At int2: right (0) and... from int2, trans goes up-left, so trans-up-left direction = 
        # from int2 to int1: (-4.2, 3.0)
        tu_angle2 = np.arctan2(3.0, -4.2)
        if tu_angle2 < 0:
            tu_angle2 += 2 * PI
        # trans-down-right from int2: (4.2, -3.0) = same as td_angle
        td_angle2 = np.arctan2(-3.0, 4.2)
        if td_angle2 < 0:
            td_angle2 += 2 * PI

        # The alternate (Z) pair: top-left (RED) and bottom-right (RED)
        # Bottom-right at int2: between right (0) and trans-down-right (td_angle2)
        arc_br2 = Arc(radius=r, start_angle=0, angle=td_angle2,
                      color=RED, stroke_width=6)
        arc_br2.move_arc_center_to(int2)

        # Second alternate pair: top-right (BLUE) and bottom-left (BLUE)
        # Top-right at int1: between right (0) and td_angle
        arc_tr1_b = Arc(radius=r, start_angle=0, angle=td_angle,
                        color=BLUE, stroke_width=6)
        arc_tr1_b.move_arc_center_to(int1)

        # Bottom-left at int2: between left (PI) and trans-up-left (tu_angle2)
        arc_bl2_b = Arc(radius=r, start_angle=tu_angle2, angle=PI - tu_angle2,
                        color=BLUE, stroke_width=6)
        arc_bl2_b.move_arc_center_to(int2)

        # Wait, I need to be more careful here. Let me compute the correct angles.
        # int1 = (-2.1, 1.5), int2 = (2.1, -1.5)
        # td_dir = int2 - int1 = (4.2, -3.0)
        td_rad = np.arctan2(-3.0, 4.2)  # -0.623 rad -> +2PI = 5.660 rad

        # tu_dir = int1 - int2 = (-4.2, 3.0)
        tu_rad = np.arctan2(3.0, -4.2)  # 2.518 rad

        # Let me just use simple computed values
        # td_rad ~ 5.660 rad (down-right)
        # tu_rad ~ 2.518 rad (up-left)

        r = 0.4

        # Top intersection (int1 = (-2.1, 1.5)):
        # Horizontal: left (PI=3.142), right (0/2PI=6.283)
        # Transversal: td_rad ~5.660 (down-right), tu_rad ~2.518 (up-left)

        # Top-left angle: between up-left (tu_rad ~2.518) and left (PI ~3.142)
        # Sweep counterclockwise: from 2.518 to 3.142 = 0.624 rad = 35.7 deg
        arc_tl = Arc(radius=r, start_angle=tu_rad, angle=PI - tu_rad,
                     color=RED, stroke_width=6)
        arc_tl.move_arc_center_to(int1)

        # Top-right angle: between right (0) and down-right (td_rad ~5.660)
        # Sweep counterclockwise: from 0 to 5.660 = 5.660 rad
        # Wait, that goes all the way around. The smaller angle is 2PI - 5.660 = 0.623 rad
        # Hmm, but we want the angle on the right side.
        # From right (0) going clockwise to down-right (300 deg = 5.236... no)
        # Actually td_rad = arctan2(-3, 4.2) = -0.623 + 2PI = 5.660 rad = 324.3 deg
        # From right (0 deg = 6.283) counterclockwise to 324.3... hmm
        # The small angle between 0 and 5.660 is min(5.660, 2PI-5.660) = min(5.660, 0.623) = 0.623
        # that's 35.7 degrees. Going counterclockwise from td_rad to 2PI = 6.283 - 5.660 = 0.623.
        # So the arc between td_rad and 2PI (which is 0/right) going counterclockwise is 0.623 rad.
        # That's the arc from down-right to right, sweeping through... below-right? 

        # top-right region at int1: above the line (y>1.5) and to the right of transversal
        # The transversal at int1 goes down-right. 
        # The region above the line on the right side of trans is between right (0) and up-left (tu_rad going opposite direction... no, up-left is 2.518)
        # Hmm, the two rays that bound the top-right region are:
        # 1. Horizontal right: 0 deg
        # 2. The transversal extended upward beyond int1: which goes from int1 AWAY from int2 = up-left direction = tu_rad
        # angle between right (0) and up-left (2.518): going counterclockwise from 0 to 2.518 = 2.518 rad = 144.3 deg
        # That's the top-right region!

        arc_tr = Arc(radius=r, start_angle=0, angle=tu_rad,
                     color=BLUE, stroke_width=6)
        arc_tr.move_arc_center_to(int1)

        # Bottom intersection (int2 = (2.1, -1.5)):
        # From int2, trans goes up-left to int1: tu_rad ~2.518
        # From int2, trans goes down-right away from int1: td_rad ~5.660

        # Alternate angle to top-left (RED): this is bottom-right
        # Bottom-right at int2: below line (y<-1.5), to the right of trans
        # Bounded by: right (0) and down-right (td_rad ~5.660)
        # The region below the line, right of trans: between right (0) and td_rad (5.660)
        # Going counterclockwise from td_rad to 2PI (which is 0) = 2PI - 5.660 = 0.623
        # Hmm but that's the small arc. The arc we want is the other one: from 0 to 5.660 counterclockwise
        arc_br_alt = Arc(radius=r, start_angle=0, angle=td_rad,
                         color=RED, stroke_width=6)
        arc_br_alt.move_arc_center_to(int2)

        # Alternate to top-right (BLUE): bottom-left
        # Bottom-left at int2: below line, left of trans
        # Bounded by: left (PI) and up-left (tu_rad ~2.518)
        # The small arc between tu_rad and PI = PI - 2.518 = 0.623 rad
        arc_bl_alt = Arc(radius=r, start_angle=tu_rad, angle=PI - tu_rad,
                         color=BLUE, stroke_width=6)
        arc_bl_alt.move_arc_center_to(int2)

        # Labels
        lbl_alt1 = Text("x", font_size=20, color=RED)
        lbl_alt1.move_to(int1 + np.array([-0.6, 0.35, 0]))
        lbl_alt2 = Text("x", font_size=20, color=RED)
        lbl_alt2.move_to(int2 + np.array([0.6, -0.35, 0]))

        lbl_alt3 = Text("y", font_size=20, color=BLUE)
        lbl_alt3.move_to(int1 + np.array([0.6, 0.35, 0]))
        lbl_alt4 = Text("y", font_size=20, color=BLUE)
        lbl_alt4.move_to(int2 + np.array([-0.6, -0.35, 0]))

        # Show alternate pair 1 (RED)
        self.play(Create(arc_tl), Create(arc_br_alt),
                  Write(lbl_alt1), Write(lbl_alt2))
        self.wait(0.5)

        equal1 = Text("x = x (Alternate angles)", font_size=18, color=RED)
        equal1.next_to(int1, UP * 0.5)
        self.play(Write(equal1))
        self.wait(0.4)

        # Show alternate pair 2 (BLUE)
        self.play(Create(arc_tr), Create(arc_bl_alt),
                  Write(lbl_alt3), Write(lbl_alt4))
        self.wait(0.5)

        equal2 = Text("y = y (Alternate angles)", font_size=18, color=BLUE)
        equal2.next_to(equal1, DOWN * 0.6)
        self.play(Write(equal2))
        self.wait(0.4)

        # Draw Z pattern
        z1 = Line(int1, int2, color=PURPLE, stroke_width=3, stroke_opacity=0.5)
        z2 = Line(int2, int2 + np.array([1.0, 0, 0]), color=PURPLE, stroke_width=3, stroke_opacity=0.5)
        z3 = Line(int1, int1 + np.array([-1.0, 0, 0]), color=PURPLE, stroke_width=3, stroke_opacity=0.5)

        self.play(Create(z1), Create(z2), Create(z3))
        z_label = Text("Z Pattern", font_size=18, color=PURPLE)
        z_label.next_to(int1, DOWN * 0.3 + RIGHT * 1.5)
        self.play(Write(z_label))
        self.wait(1.0)

        eq_final = Text("Alternate angles between parallel lines are equal",
                        font_size=18, color=WHITE)
        eq_final.next_to(int2, DOWN * 0.7)
        self.play(Write(eq_final))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
