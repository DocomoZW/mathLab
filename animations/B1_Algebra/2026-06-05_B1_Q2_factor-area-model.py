# topic_id: B1_Q2
# track: igcse_o
# unit: B1_Algebra
# description: Factorisation as area model reverse - factoring x^2 + 5x + 6

from manim import *

class B1Q2FactorAreaModel(Scene):
    def construct(self):
        title = Text("Factorisation: Area Model", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Show the expression
        expr = Text("x^2 + 5x + 6", font_size=36, color=WHITE)
        expr.shift(UP*2)
        self.play(Write(expr))
        self.wait(0.3)

        # Build the area model backward (factorisation)
        rect = Rectangle(width=4, height=3, color=WHITE, stroke_width=2)
        rect.shift(DOWN*0.5)
        self.play(Create(rect))
        self.wait(0.2)

        # Vertical divider - split so left part is wider (x area)
        v_div = Line(
            rect.get_corner(UL) + RIGHT * 2.4,
            rect.get_corner(DL) + RIGHT * 2.4,
            color=YELLOW, stroke_width=3
        )
        h_div = Line(
            rect.get_corner(UL) + DOWN * 1.8,
            rect.get_corner(UR) + DOWN * 1.8,
            color=YELLOW, stroke_width=3
        )
        self.play(Create(v_div), Create(h_div))
        self.wait(0.3)

        # Animate filling each quadrant
        # Top-left: x^2
        tl_rect = Rectangle(width=2.4, height=1.8, color=GREEN, fill_opacity=0.3, stroke_width=2)
        tl_rect.move_to(rect.get_corner(UL) + RIGHT*1.2 + DOWN*0.9)
        tl_label = Text("x^2", font_size=26, color=GREEN)
        tl_label.move_to(tl_rect.get_center())
        self.play(Create(tl_rect), Write(tl_label))
        self.wait(0.3)

        # Top-right: 3x
        tr_rect = Rectangle(width=1.6, height=1.8, color=RED, fill_opacity=0.3, stroke_width=2)
        tr_rect.move_to(rect.get_corner(UR) + LEFT*0.8 + DOWN*0.9)
        tr_label = Text("3x", font_size=26, color=RED)
        tr_label.move_to(tr_rect.get_center())
        self.play(Create(tr_rect), Write(tr_label))
        self.wait(0.3)

        # Bottom-left: 2x
        bl_rect = Rectangle(width=2.4, height=1.2, color=RED, fill_opacity=0.3, stroke_width=2)
        bl_rect.move_to(rect.get_corner(DL) + RIGHT*1.2 + UP*0.6)
        bl_label = Text("2x", font_size=26, color=RED)
        bl_label.move_to(bl_rect.get_center())
        self.play(Create(bl_rect), Write(bl_label))
        self.wait(0.3)

        # Bottom-right: 6
        br_rect = Rectangle(width=1.6, height=1.2, color=PURPLE, fill_opacity=0.3, stroke_width=2)
        br_rect.move_to(rect.get_corner(DR) + LEFT*0.8 + UP*0.6)
        br_label = Text("6", font_size=26, color=PURPLE)
        br_label.move_to(br_rect.get_center())
        self.play(Create(br_rect), Write(br_label))
        self.wait(0.4)

        # Side labels
        left_label = Text("x + 2", font_size=24, color=YELLOW)
        left_label.next_to(rect, LEFT, buff=0.3)
        top_label = Text("x + 3", font_size=24, color=YELLOW)
        top_label.next_to(rect, UP, buff=0.3)

        self.play(Write(left_label), Write(top_label))
        self.wait(0.4)

        result = Text("x^2 + 5x + 6 = (x+2)(x+3)", font_size=28, color=GREEN)
        result.to_edge(DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
