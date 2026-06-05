from manim import *

class C1Q5QuadrilateralProperties(Scene):
    def construct(self):
        title = Text("Quadrilateral Properties", font_size=32)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # --- SQUARE ---
        sq_label = Text("Square", font_size=26, color=YELLOW)
        sq_label.next_to(title, DOWN, buff=0.4)
        self.play(Write(sq_label))
        self.wait(0.2)

        square = Square(side_length=2.5, color=BLUE, stroke_width=3)
        square.move_to(ORIGIN)
        self.play(Create(square))
        self.wait(0.3)

        # Property labels
        p1 = Text("4 equal sides", font_size=20, color=GREEN)
        p1.next_to(square, LEFT, buff=0.5)
        self.play(Write(p1))

        p2 = Text("4 right angles", font_size=20, color=GREEN)
        p2.next_to(square, RIGHT, buff=0.5)
        self.play(Write(p2))

        p3 = Text("Opposite sides parallel", font_size=20, color=GREEN)
        p3.next_to(square, DOWN, buff=0.5)
        self.play(Write(p3))

        # Right angle marks
        ra_size = 0.3
        ra1 = Polygon([0, 0, 0], [ra_size, 0, 0], [ra_size, ra_size, 0], [0, ra_size, 0],
                       color=YELLOW, stroke_width=2).move_to(square.get_corner(UL), DL)
        ra2 = Polygon([0, 0, 0], [ra_size, 0, 0], [ra_size, ra_size, 0], [0, ra_size, 0],
                       color=YELLOW, stroke_width=2).move_to(square.get_corner(UR), DR)
        ra3 = Polygon([0, 0, 0], [ra_size, 0, 0], [ra_size, ra_size, 0], [0, ra_size, 0],
                       color=YELLOW, stroke_width=2).move_to(square.get_corner(DL), UL)
        ra4 = Polygon([0, 0, 0], [ra_size, 0, 0], [ra_size, ra_size, 0], [0, ra_size, 0],
                       color=YELLOW, stroke_width=2).move_to(square.get_corner(DR), UR)
        self.play(Create(ra1), Create(ra2), Create(ra3), Create(ra4))
        self.wait(0.5)

        # Side length marks (single ticks)
        tick_len = 0.15
        for side_start, side_end, direction in [
            (square.get_corner(UL), square.get_corner(UR), UP),
            (square.get_corner(UR), square.get_corner(DR), RIGHT),
            (square.get_corner(DR), square.get_corner(DL), DOWN),
            (square.get_corner(DL), square.get_corner(UL), LEFT),
        ]:
            mid = (side_start + side_end) / 2
            perp = np.array([-(side_end[1]-side_start[1]), side_end[0]-side_start[0], 0])
            perp = perp / np.linalg.norm(perp[:2])
            t1 = Line(mid + perp * tick_len, mid - perp * tick_len, color=WHITE, stroke_width=2)
            self.play(Create(t1), run_time=0.1)
        self.wait(0.5)

        # --- MORPH TO RECTANGLE ---
        rect_label = Text("Rectangle", font_size=26, color=YELLOW)
        rect_label.next_to(title, DOWN, buff=0.4)

        # Stretch square into rectangle
        target_rect = Square(side_length=2.5, color=BLUE, stroke_width=3)
        target_rect.stretch(1.6, dim=0)

        self.play(
            Transform(square, target_rect),
            FadeOut(p1),
            FadeOut(p2),
            FadeOut(p3),
            Transform(sq_label, rect_label),
            FadeOut(ra1), FadeOut(ra2), FadeOut(ra3), FadeOut(ra4),
        )

        rp1 = Text("Opposite sides equal", font_size=20, color=GREEN)
        rp1.next_to(square, LEFT, buff=0.5)
        rp2 = Text("4 right angles", font_size=20, color=GREEN)
        rp2.next_to(square, RIGHT, buff=0.5)
        rp3 = Text("Opposite sides parallel", font_size=20, color=GREEN)
        rp3.next_to(square, DOWN, buff=0.5)

        self.play(Write(rp1), Write(rp2), Write(rp3))
        self.wait(0.5)
        self.play(FadeOut(rp1), FadeOut(rp2), FadeOut(rp3))
        self.wait(0.2)

        # --- MORPH TO RHOMBUS ---
        rhombus_label = Text("Rhombus", font_size=26, color=YELLOW)
        rhombus_label.next_to(title, DOWN, buff=0.4)

        # Create a rhombus shape (tilted square)
        rhombus_points = [
            [1.8, 0, 0],
            [0.6, 1.5, 0],
            [-1.8, 0, 0],
            [-0.6, -1.5, 0],
        ]
        rhombus = Polygon(*rhombus_points, color=BLUE, stroke_width=3)

        self.play(
            Transform(square, rhombus),
            Transform(sq_label, rhombus_label),
        )

        rh1 = Text("4 equal sides", font_size=20, color=GREEN)
        rh1.next_to(rhombus, LEFT, buff=0.5)
        rh2 = Text("Opposite sides parallel", font_size=20, color=GREEN)
        rh2.next_to(rhombus, RIGHT, buff=0.5)
        rh3 = Text("Opposite angles equal", font_size=20, color=GREEN)
        rh3.next_to(rhombus, DOWN, buff=0.5)

        self.play(Write(rh1), Write(rh2), Write(rh3))
        self.wait(0.5)
        self.play(FadeOut(rh1), FadeOut(rh2), FadeOut(rh3))
        self.wait(0.2)

        # --- MORPH TO PARALLELOGRAM ---
        para_label = Text("Parallelogram", font_size=26, color=YELLOW)
        para_label.next_to(title, DOWN, buff=0.4)

        para_points = [
            [2.2, 0, 0],
            [0.5, 1.5, 0],
            [-2.2, 0, 0],
            [-0.5, -1.5, 0],
        ]
        para = Polygon(*para_points, color=BLUE, stroke_width=3)

        self.play(
            Transform(square, para),
            Transform(sq_label, para_label),
        )

        pp1 = Text("Opposite sides equal", font_size=20, color=GREEN)
        pp1.next_to(para, LEFT, buff=0.5)
        pp2 = Text("Opposite sides parallel", font_size=20, color=GREEN)
        pp2.next_to(para, RIGHT, buff=0.5)
        pp3 = Text("Opposite angles equal", font_size=20, color=GREEN)
        pp3.next_to(para, DOWN, buff=0.5)

        self.play(Write(pp1), Write(pp2), Write(pp3))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
