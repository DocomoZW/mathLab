from manim import *

class C1Q1AngleTypes(Scene):
    def construct(self):
        title = Text("Types of Angles", font_size=28).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # 5 angle demonstrations arranged horizontally
        # Each vertex at same y, spaced across screen
        vertices_x = [-4.5, -2.3, 0, 2.3, 4.5]
        base_y = -0.3
        ray_len = 1.3
        arc_rad = 0.45

        # (name, second_ray_angle_deg, angle_label, color, is_reflex)
        # second_ray_angle measured from +x axis (right=0, up=90, left=180, down=270)
        angles = [
            ("ACUTE", 140, "0-90 deg", BLUE, False),
            ("RIGHT", 90, "= 90 deg", GREEN, False),
            ("OBTUSE", 50, "90-180 deg", YELLOW, False),
            ("STRAIGHT", 0, "= 180 deg", ORANGE, False),
            ("REFLEX", 300, "180-360 deg", RED, True),
        ]

        all_groups = []
        for i, (name, ray2_deg, label_text, color, is_reflex) in enumerate(angles):
            x = vertices_x[i]
            vertex = np.array([x, base_y, 0])

            # Left ray (horizontal, pointing left)
            left_ray = Line(
                vertex,
                vertex + np.array([-ray_len, 0, 0]),
                color=WHITE, stroke_width=3
            )

            # Second ray
            ray2_rad = ray2_deg * DEGREES
            ray2_end = vertex + np.array([
                ray_len * np.cos(ray2_rad),
                ray_len * np.sin(ray2_rad),
                0
            ])
            right_ray = Line(vertex, ray2_end, color=color, stroke_width=3)

            # Dot at vertex
            dot = Dot(vertex, color=WHITE, radius=0.04)

            if name == "RIGHT":
                # Right angle square indicator
                sq = Square(side_length=0.25, color=GREEN, stroke_width=3)
                sq.move_to(vertex + np.array([-0.125, 0.125, 0]))
                indicator = sq
            elif name == "STRAIGHT":
                # Semicircle on top
                indicator = Arc(
                    radius=arc_rad,
                    start_angle=0,
                    angle=PI,
                    color=color, stroke_width=3
                )
                indicator.move_arc_center_to(vertex)
            elif is_reflex:
                # Reflex arc: from second ray (300 deg) going counterclockwise to left ray (180 deg)
                # That's 240 degrees sweep
                indicator = Arc(
                    radius=arc_rad,
                    start_angle=ray2_rad,
                    angle=240 * DEGREES,
                    color=color, stroke_width=3
                )
                indicator.move_arc_center_to(vertex)
            else:
                # Acute or obtuse: arc from second ray to left ray
                # Second ray is at ray2_deg (e.g. 140 for acute, 50 for obtuse)
                # Left ray is at 180 deg
                # Arc sweeps counterclockwise from ray2_rad to PI
                sweep = PI - ray2_rad  # positive
                indicator = Arc(
                    radius=arc_rad,
                    start_angle=ray2_rad,
                    angle=sweep,
                    color=color, stroke_width=3
                )
                indicator.move_arc_center_to(vertex)

            # Labels
            name_label = Text(name, font_size=17, color=color)
            name_label.next_to(vertex, DOWN * 0.9)

            range_lbl = Text(label_text, font_size=13, color=GREY)
            range_lbl.next_to(name_label, DOWN * 0.5)

            group = VGroup(left_ray, right_ray, dot, indicator, name_label, range_lbl)
            all_groups.append(group)

            if i == 0:
                self.play(
                    Create(left_ray), Create(right_ray),
                    Create(dot), Create(indicator),
                    Write(name_label), Write(range_lbl)
                )
            else:
                self.play(
                    Create(left_ray), Create(right_ray),
                    Create(dot), Create(indicator),
                    Write(name_label), Write(range_lbl),
                    run_time=0.6
                )
            self.wait(0.3)

        self.wait(1.5)
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
