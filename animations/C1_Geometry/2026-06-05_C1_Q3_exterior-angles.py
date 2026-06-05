from manim import *

class C1Q3ExteriorAngles(Scene):
    def construct(self):
        title = Text("Exterior Angles of a Polygon", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        subtitle = Text("Sum of exterior angles = 360 degrees", font_size=18, color=GREY)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.3)

        # Draw a regular pentagon
        center = np.array([0, 0, 0])
        n = 5
        radius = 2.0
        verts = []
        for i in range(n):
            angle = PI/2 - i * 2*PI/n
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)
            verts.append(np.array([x, y, 0]))

        # Draw pentagon
        pentagon = VGroup()
        for i in range(n):
            edge = Line(verts[i], verts[(i+1) % n], color=BLUE, stroke_width=3)
            pentagon.add(edge)

        self.play(Create(pentagon))
        self.wait(0.3)

        # Dot at each vertex
        dots = VGroup(*[Dot(v, color=WHITE, radius=0.05) for v in verts])
        self.play(Create(dots))
        self.wait(0.2)

        # Draw exterior angles at each vertex
        # Exterior angle: extend one side outward, draw arc between the extension and the next side
        ext_len = 0.9
        ext_arcs = []
        ext_labels = []
        ext_arrows = []
        ext_values = [72, 72, 72, 72, 72]  # Regular pentagon: 360/5 = 72

        for i in range(n):
            v = verts[i]
            # Direction from current vertex to next vertex
            to_next = (verts[(i+1) % n] - v)
            to_next = to_next / np.linalg.norm(to_next)
            # Direction from previous vertex to current vertex
            from_prev = (v - verts[(i-1) % n])
            from_prev = from_prev / np.linalg.norm(from_prev)

            # The exterior angle is outside the polygon
            # Extension of the side going OUT from the vertex (away from polygon interior)
            # Polygon interior is to one side; exterior is the other side
            ext_dir = to_next  # extending the next side outward from the vertex

            # Let's draw the extension line (dashed)
            ext_line = Line(v, v + ext_dir * ext_len,
                           color=RED, stroke_width=2)

            # To find which side is exterior vs interior, compute the cross product
            # For a regular pentagon with vertices going clockwise from top,
            # the interior is to the right of each edge direction
            # The exterior angle arc should be drawn on the outside

            # Exterior arc between the extension and the previous side
            # Arc from ext_dir direction to from_prev direction (going the SHORT way on the outside)
            ext_angle_rad = 72 * DEGREES

            # Direction of the extension
            ext_ang = np.arctan2(ext_dir[1], ext_dir[0])
            # Direction of the previous side (from prev vertex to this vertex)
            prev_ang = np.arctan2(from_prev[1], from_prev[0])

            # For a clockwise polygon, the exterior angle is the one that goes
            # from the extension direction to the previous side direction,
            # going in the direction that keeps the polygon on the other side

            # For a regular pentagon going clockwise from top:
            # Vertex 0 (top): ext_dir points to-next = down-right
            # from_prev points from previous to current = up-left... wait
            # Actually, from_prev is from verts[4] to verts[0] which goes... let me compute
            # verts[4] is to the left, verts[0] is at top
            # So from_prev goes from left to top = up-right

            # Hmm, let me just draw the arc properly by computing the angle range
            # The exterior arc should be on the outside of the polygon

            r_ext = 0.35

            # Let me compute the exterior arc angles directly
            # For vertex at index i, the interior angle of regular pentagon is 108 deg
            # Exterior = 180 - 108 = 72 deg
            # The arc goes from the direction of the extended side to the direction of the previous side

            # Extended side direction = direction from v to next vertex = to_next
            # Previous side direction = direction from v to prev vertex = -from_prev
            prev_side_dir = (verts[(i-1) % n] - v)
            prev_side_dir = prev_side_dir / np.linalg.norm(prev_side_dir)

            ext_start_angle = np.arctan2(to_next[1], to_next[0])
            ext_end_angle = np.arctan2(prev_side_dir[1], prev_side_dir[0])

            # The arc should go from to_next direction to prev_side_dir direction
            # We want the smaller positive angle between them that's on the OUTSIDE
            # For a regular pentagon going clockwise from top, the exterior is 
            # clockwise from to_next to prev_side_dir

            # Let me just compute the angle difference
            angle_diff = ext_end_angle - ext_start_angle
            # Normalize to [-PI, PI]
            while angle_diff > PI:
                angle_diff -= 2*PI
            while angle_diff < -PI:
                angle_diff += 2*PI

            # The exterior angle should be the one that goes AWAY from the polygon
            # For a convex polygon, the exterior angle is the supplement of interior
            # Since interior = 108 deg, exterior = 72 deg
            # Arc from to_next to prev_side_dir, positive angle (counterclockwise) gives interior
            # Negative angle (clockwise) gives exterior

            # Let's check: for vertex 0 (top):
            # to_next points to verts[1] which is bottom-right
            # prev_side_dir points from verts[0] to verts[4] which is bottom-left
            # Going counterclockwise from bottom-right to bottom-left = about 90 deg (interior side, going through top)
            # Going clockwise from bottom-right to bottom-left = about 270 deg... no
            # Hmm let me think differently

            # Actually for a simple approach, I'll just draw the arc manually:
            # The exterior angle is the supplement of the interior angle
            # For a regular pentagon (interior 108), exterior = 72 deg

            # Let me draw the arc on the exterior side by starting at to_next direction
            # and going AWAY from the polygon

            # Let me just use a fixed approach: draw the arc, try both directions
            # and it'll look right because we're drawing on the outside

            # For vertex 0 (top, 90 deg):
            # to_next = direction to next vertex = down-right (~ -30 deg from +x = 330 deg)
            # prev_side_dir = direction to prev vertex = down-left (~ 210 deg)
            # Going counterclockwise: 330 -> 210 = going through 360, 0 = 240 deg (no, that's 210-330+360=240)
            # Wait: counterclockwise from 330 to 210 = (360-330) + 210 = 240 deg - that's the interior side
            # Going clockwise from 330 to 210 = 330 - 210 = 120 deg - that's the exterior side
            # So we want the clockwise direction = negative angle

            # Actually for vertex 0:
            # to_next direction: from (0, 2) to... let me compute actual values
            # verts[0] = (0, 2) (top)
            # verts[1] = (2*cos(90-72), 2*sin(90-72)) = (2*cos(18), 2*sin(18)) = (1.9, 0.62)
            # to_next = (1.9, -1.38), angle ~ -36 deg or 324 deg
            # prev_side_dir: verts[4] = (2*cos(90+72), 2*sin(90+72)) = (2*cos(162), 2*sin(162)) = (-1.9, 0.62)
            # prev_side_dir = (-1.9, -1.38), angle ~ -144 deg or 216 deg
            # to_next angle = 324 deg (or -36 deg)
            # prev_side_dir angle = 216 deg (or -144 deg)
            # Going counterclockwise from 324 to 216: (360-324) + 216 = 252 deg (interior)
            # Going clockwise from 324 to 216: 324-216 = 108 deg... but exterior should be 72!
            # 
            # Hmm, I think I have the prev_side_dir backwards.
            # prev_side_dir should be the direction from vertex to PREV vertex
            # verts[4] to verts[0]: verts[4] is at (-1.9, 0.62), verts[0] is at (0, 2)
            # So prev_side_dir = (1.9, 1.38), angle ~ 36 deg
            # 
            # to_next angle = 324 deg (-36 deg)
            # prev_side_dir angle = 36 deg
            # Counterclockwise from 324 to 36: (360-324) + 36 = 72 deg! That's the exterior!
            # So exterior arc = start_angle = to_next_angle, angle = +72 deg counterclockwise

            # Let me verify: from 324 deg going counterclockwise, we reach 360 (=0), then 36.
            # Total = (360-324) + 36 = 72 deg. That goes through the outside of the pentagon at the top.
            # Yes! That's correct.

            # So exterior arc: start_angle = angle of to_next, angle = 72 deg (counterclockwise)

            ext_arc = Arc(
                radius=r_ext,
                start_angle=np.arctan2(to_next[1], to_next[0]),
                angle=72 * DEGREES,
                color=RED,
                stroke_width=5
            )
            ext_arc.move_arc_center_to(v)

            # Arrow showing the exterior angle direction
            mid_angle = np.arctan2(to_next[1], to_next[0]) + 36 * DEGREES
            arrow_tip = v + np.array([
                (r_ext + 0.15) * np.cos(mid_angle),
                (r_ext + 0.15) * np.sin(mid_angle),
                0
            ])
            ext_arrow = Arrow(
                start=arrow_tip + np.array([0.2, 0, 0]),
                end=arrow_tip,
                color=RED,
                stroke_width=2,
                tip_length=0.08
            )

            # Label
            lbl = Text("72 deg", font_size=12, color=RED)
            lbl.move_to(v + np.array([
                (r_ext + 0.4) * np.cos(mid_angle),
                (r_ext + 0.4) * np.sin(mid_angle),
                0
            ]))

            ext_arcs.append(ext_arc)
            ext_labels.append(lbl)
            ext_arrows.append(ext_arrow)

        # Show the exterior angles one by one
        for i in range(n):
            self.play(
                Create(ext_arcs[i]),
                Write(ext_labels[i]),
                run_time=0.5
            )
            self.wait(0.3)

        # Show the collection animation: gather all exterior angles to one point
        self.wait(0.5)

        # Transition text
        collect_text = Text("Collecting all exterior angles...", font_size=18, color=YELLOW)
        collect_text.next_to(subtitle, DOWN * 0.8)
        self.play(Write(collect_text))
        self.wait(0.4)

        # Fade out everything except the arcs
        self.play(
            FadeOut(title), FadeOut(subtitle), FadeOut(pentagon),
            FadeOut(dots), FadeOut(collect_text),
            *[FadeOut(l) for l in ext_labels],
            *[FadeOut(a) for a in ext_arrows]
        )
        self.wait(0.3)

        # Animate arcs moving to center and stacking into a full circle
        gather_center = np.array([0, 0, 0])
        # Position each arc around the center to form a full circle
        for i in range(n):
            arc = ext_arcs[i]
            target_angle = i * 72 * DEGREES
            target = gather_center

            # Animate the arc moving to the center
            self.play(
                arc.animate.move_arc_center_to(target),
                run_time=0.6
            )
            self.wait(0.15)

        # The 5 arcs should now form a semicircle... wait, 5 x 72 = 360 = full circle
        # Show a circle around them
        circle = Circle(radius=0.5, color=YELLOW, stroke_width=3)
        self.play(Create(circle))
        self.wait(0.3)

        # Show sum = 360
        sum_text = Text("5 x 72 = 360 degrees", font_size=22, color=YELLOW)
        sum_text.next_to(gather_center, DOWN * 0.8)
        self.play(Write(sum_text))
        self.wait(0.5)

        conclusion = Text("Sum of exterior angles = 360 deg", font_size=20, color=WHITE)
        conclusion.next_to(sum_text, DOWN * 0.6)
        self.play(Write(conclusion))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
