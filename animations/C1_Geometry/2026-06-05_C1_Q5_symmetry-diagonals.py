from manim import *
import numpy as np

class C1Q5SymmetryDiagonals(Scene):
    def construct(self):
        title = Text("Symmetry and Diagonals in Quadrilaterals", font_size=30)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Helper to draw tick marks on a line
        def draw_tick(line_obj, color=WHITE):
            mid = line_obj.get_center()
            direction = line_obj.get_end() - line_obj.get_start()
            perp = np.array([-direction[1], direction[0], 0])
            if np.linalg.norm(perp[:2]) > 0:
                perp = perp / np.linalg.norm(perp[:2]) * 0.15
            else:
                perp = np.array([0, 0.15, 0])
            return Line(mid - perp, mid + perp, color=color, stroke_width=2)

        # --- SQUARE (top-left) ---
        sq_label = Text("Square", font_size=22, color=YELLOW)
        sq_label.move_to([-3.5, 2.2, 0])
        self.play(Write(sq_label))

        sq = Square(side_length=1.8, color=BLUE, stroke_width=3)
        sq.move_to([-3.5, 0.5, 0])
        self.play(Create(sq))

        # Diagonals of square
        sq_d1 = Line(sq.get_corner(UL), sq.get_corner(DR), color=RED, stroke_width=2)
        sq_d2 = Line(sq.get_corner(UR), sq.get_corner(DL), color=RED, stroke_width=2)
        self.play(Create(sq_d1), Create(sq_d2))

        sq_lines = Text("4 lines of symmetry", font_size=16, color=GREEN)
        sq_lines.next_to(sq, DOWN, buff=0.3)
        self.play(Write(sq_lines))

        # Draw symmetry lines on square
        sq_sym1 = Line(sq.get_center(), sq.get_center() + [0, 1.2, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        sq_sym2 = Line(sq.get_center(), sq.get_center() - [0, 1.2, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        sq_sym3 = Line(sq.get_center(), sq.get_center() + [1.2, 0, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        sq_sym4 = Line(sq.get_center(), sq.get_center() - [1.2, 0, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        self.play(Create(sq_sym1), Create(sq_sym2), Create(sq_sym3), Create(sq_sym4), run_time=0.5)
        self.wait(0.3)

        # --- RECTANGLE (top-right) ---
        rect_label = Text("Rectangle", font_size=22, color=YELLOW)
        rect_label.move_to([3.5, 2.2, 0])
        self.play(Write(rect_label))

        rect = Rectangle(width=2.4, height=1.5, color=BLUE, stroke_width=3)
        rect.move_to([3.5, 0.5, 0])
        self.play(Create(rect))

        # Diagonals of rectangle
        rect_d1 = Line(rect.get_corner(UL), rect.get_corner(DR), color=RED, stroke_width=2)
        rect_d2 = Line(rect.get_corner(UR), rect.get_corner(DL), color=RED, stroke_width=2)
        self.play(Create(rect_d1), Create(rect_d2))

        rect_lines = Text("2 lines of symmetry", font_size=16, color=GREEN)
        rect_lines.next_to(rect, DOWN, buff=0.3)
        self.play(Write(rect_lines))

        # Horizontal and vertical symmetry lines
        rect_sym1 = Line(rect.get_center() + [-1.5, 0, 0], rect.get_center() + [1.5, 0, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        rect_sym2 = Line(rect.get_center() + [0, -1.0, 0], rect.get_center() + [0, 1.0, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        self.play(Create(rect_sym1), Create(rect_sym2), run_time=0.5)
        self.wait(0.3)

        # --- RHOMBUS (bottom-left) ---
        rhom_label = Text("Rhombus", font_size=22, color=YELLOW)
        rhom_label.move_to([-3.5, -2.3, 0])
        self.play(Write(rhom_label))

        r_points = [
            [-3.5 + 1.2, -3.8, 0],
            [-3.5, -2.3, 0],
            [-3.5 - 1.2, -3.8, 0],
            [-3.5, -5.3, 0],
        ]
        rhom = Polygon(*r_points, color=BLUE, stroke_width=3)
        self.play(Create(rhom))

        # Diagonals of rhombus
        rhom_d1 = Line(r_points[0], r_points[2], color=RED, stroke_width=2)
        rhom_d2 = Line(r_points[1], r_points[3], color=RED, stroke_width=2)
        self.play(Create(rhom_d1), Create(rhom_d2))

        rhom_lines = Text("2 lines of symmetry", font_size=16, color=GREEN)
        rhom_lines.next_to(rhom, DOWN, buff=0.3)
        self.play(Write(rhom_lines))

        # Symmetry lines (along diagonals)
        rhom_sym1 = Line(rhom.get_center() + [1.8, 0, 0], rhom.get_center() + [-1.8, 0, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        rhom_sym2 = Line(rhom.get_center() + [0, 1.8, 0], rhom.get_center() + [0, -1.8, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        self.play(Create(rhom_sym1), Create(rhom_sym2), run_time=0.5)
        self.wait(0.3)

        # --- KITE (bottom-right) ---
        kite_label = Text("Kite", font_size=22, color=YELLOW)
        kite_label.move_to([3.5, -2.3, 0])
        self.play(Write(kite_label))

        k_points = [
            [3.5, -3.8, 0],
            [3.5 + 1.5, -4.8, 0],
            [3.5, -5.8, 0],
            [3.5 - 1.5, -4.8, 0],
        ]
        kite = Polygon(*k_points, color=BLUE, stroke_width=3)
        self.play(Create(kite))

        # Diagonals of kite
        kite_d1 = Line(k_points[0], k_points[2], color=RED, stroke_width=2)
        kite_d2 = Line(k_points[1], k_points[3], color=RED, stroke_width=2)
        self.play(Create(kite_d1), Create(kite_d2))

        kite_lines = Text("1 line of symmetry", font_size=16, color=GREEN)
        kite_lines.next_to(kite, DOWN, buff=0.3)
        self.play(Write(kite_lines))

        # One symmetry line (vertical)
        kite_sym1 = Line(kite.get_center() + [0, 1.5, 0], kite.get_center() + [0, -1.5, 0], color=YELLOW, stroke_width=2, stroke_opacity=0.6)
        self.play(Create(kite_sym1), run_time=0.5)
        self.wait(0.5)

        # Highlight that diagonals intersect
        intersect_text = Text("Diagonals bisect each other (square, rectangle, rhombus)", font_size=18, color=ORANGE)
        intersect_text.to_edge(DOWN, buff=0.3)
        self.play(Write(intersect_text))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
