# topic_id: B1_Q2
# track: igcse_o
# unit: B1_Algebra
# description: Difference of squares visualised as expanding/contracting rectangles

from manim import *

class B1Q2DifferenceOfSquares(Scene):
    def construct(self):
        title = Text("Difference of Two Squares", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Start with a large square: side length a
        big_sq = Square(side_length=3.5, color=WHITE, stroke_width=2)
        big_sq.shift(DOWN*0.5)
        a_label = Text("a", font_size=28, color=YELLOW)
        a_label.next_to(big_sq, DOWN, buff=0.1)
        a_label_right = Text("a", font_size=28, color=YELLOW)
        a_label_right.next_to(big_sq, RIGHT, buff=0.1)

        self.play(Create(big_sq), Write(a_label), Write(a_label_right))
        self.wait(0.3)

        # Cut out a smaller square from the top-right: side length b
        small_sq = Square(side_length=1.5, color=RED, stroke_width=3, fill_opacity=0.3, fill_color=RED)
        small_sq.move_to(big_sq.get_corner(UR) + LEFT*0.75 + DOWN*0.75)
        b_label = Text("b", font_size=24, color=RED)
        b_label.next_to(small_sq, DOWN, buff=0.1)
        b_label_right = Text("b", font_size=24, color=RED)
        b_label_right.next_to(small_sq, RIGHT, buff=0.1)

        self.play(Create(small_sq), Write(b_label), Write(b_label_right))
        self.wait(0.5)

        # Show the shaded region = a^2 - b^2
        area_expr = Text("Area = a^2 - b^2", font_size=26, color=GREEN)
        area_expr.shift(UP*1.5)
        self.play(Write(area_expr))
        self.wait(0.3)

        # Now transform: slide the bottom piece to form (a-b)(a+b)
        # Cut the L-shape into two rectangles
        cut_h = Line(
            big_sq.get_center() + LEFT*0.5,
            big_sq.get_center() + RIGHT*1.75,
            color=YELLOW, stroke_width=2
        )
        self.play(Create(cut_h))
        self.wait(0.3)

        # Bottom-left rectangle (a-b) x b
        rect_bot = Rectangle(width=2.0, height=1.5, color=YELLOW, fill_opacity=0.2)
        rect_bot.move_to(big_sq.get_center() + DOWN*0.25 + LEFT*0.25)
        # The remaining top-right piece
        rect_top = Rectangle(width=2.0, height=2.0, color=GREEN, fill_opacity=0.2)
        rect_top.move_to(big_sq.get_center() + UP*0.25 + RIGHT*0.5)

        # Show the result formula
        formula = Text("a^2 - b^2 = (a+b)(a-b)", font_size=28, color=GREEN)
        formula.to_edge(DOWN, buff=0.3)
        self.play(Write(formula))
        self.wait(1.0)

        # Slide the bottom rectangle to the right to form (a-b) x (a+b) rectangle
        self.play(rect_bot.animate.shift(RIGHT*2.5))
        self.wait(0.5)

        combined = Text("Forms (a-b)(a+b) rectangle", font_size=24, color=YELLOW)
        combined.next_to(formula, DOWN, buff=0.2)
        self.play(Write(combined))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
