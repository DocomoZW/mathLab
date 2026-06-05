# topic_id: B1_Q1
# track: igcse_o
# unit: B1_Algebra
# description: Visual area model for expanding brackets (x+2)(x+3) = x^2 + 5x + 6

from manim import *

class B1Q1ExpandBrackets(Scene):
    def construct(self):
        title = Text("Expanding Brackets: Area Model", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Build an area model rectangle for (x+2)(x+3)
        # Create the base rectangle
        big_rect = Rectangle(width=5, height=4, color=WHITE, stroke_width=2)
        big_rect.shift(DOWN*0.5)
        self.play(Create(big_rect))
        self.wait(0.2)

        # Vertical divider at position representing x (width 3 of 5 = 60%)
        v_div = Line(
            big_rect.get_corner(UL) + RIGHT * 3,
            big_rect.get_corner(DL) + RIGHT * 3,
            color=YELLOW, stroke_width=3
        )
        # Horizontal divider at position representing x (height 2.5 of 4 = 62.5%)
        h_div = Line(
            big_rect.get_corner(UL) + DOWN * 2.5,
            big_rect.get_corner(UR) + DOWN * 2.5,
            color=YELLOW, stroke_width=3
        )
        self.play(Create(v_div), Create(h_div))
        self.wait(0.3)

        # Labels for side lengths
        left_top = Text("x", font_size=28, color=YELLOW)
        left_top.next_to(v_div, UP, buff=0.3)
        left_bot = Text("2", font_size=28, color=YELLOW)
        left_bot.next_to(v_div, DOWN, buff=0.3)

        top_left = Text("x", font_size=28, color=YELLOW)
        top_left.next_to(h_div, LEFT, buff=0.3)
        top_right = Text("3", font_size=28, color=YELLOW)
        top_right.next_to(h_div, RIGHT, buff=0.3)

        self.play(Write(left_top), Write(left_bot), Write(top_left), Write(top_right))
        self.wait(0.3)

        # Label each quadrant with its area
        # Top-left: x * x = x^2
        tl_label = Text("x^2", font_size=26, color=GREEN)
        tl_center = big_rect.get_corner(UL) + RIGHT*1.5 + DOWN*1.25
        tl_label.move_to(tl_center)
        # Top-right: 3 * x = 3x
        tr_label = Text("3x", font_size=26, color=RED)
        tr_center = big_rect.get_corner(UR) + LEFT*1.0 + DOWN*1.25
        tr_label.move_to(tr_center)
        # Bottom-left: 2 * x = 2x
        bl_label = Text("2x", font_size=26, color=RED)
        bl_center = big_rect.get_corner(DL) + RIGHT*1.5 + UP*0.75
        bl_label.move_to(bl_center)
        # Bottom-right: 2 * 3 = 6
        br_label = Text("6", font_size=26, color=PURPLE)
        br_center = big_rect.get_corner(DR) + LEFT*1.0 + UP*0.75
        br_label.move_to(br_center)

        self.play(Write(tl_label))
        self.wait(0.3)
        self.play(Write(tr_label))
        self.wait(0.3)
        self.play(Write(bl_label))
        self.wait(0.3)
        self.play(Write(br_label))
        self.wait(0.4)

        # Highlight and group to show sum
        result = Text("(x+2)(x+3) = x^2 + 5x + 6", font_size=28, color=GREEN)
        result.to_edge(DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(1.0)

        # Fade out
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.1)
