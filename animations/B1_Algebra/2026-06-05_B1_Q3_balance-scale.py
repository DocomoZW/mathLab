# topic_id: B1_Q3
# track: igcse_o
# unit: B1_Algebra
# description: Balance scale model for solving linear equations

from manim import *

class B1Q3BalanceScale(Scene):
    def construct(self):
        title = Text("Linear Equations: Balance Scale", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Draw a balance scale
        base = Line(LEFT*0.5, RIGHT*0.5, color=WHITE).shift(DOWN*2)
        pole = Line(UP*0.5, DOWN*2, color=WHITE).shift(UP*0.5)
        beam = Line(LEFT*3, RIGHT*3, color=WHITE)
        beam.shift(UP*0.5)

        self.play(Create(base), Create(pole), Create(beam))
        self.wait(0.2)

        # Left pan
        left_pan = Rectangle(width=2.0, height=0.3, color=BLUE, fill_opacity=0.5)
        left_pan.move_to(beam.get_left() + DOWN*0.3)
        left_cable = Line(beam.get_left(), left_pan.get_top(), color=WHITE, stroke_width=1)
        self.play(Create(left_cable), Create(left_pan))
        self.wait(0.2)

        # Right pan
        right_pan = Rectangle(width=2.0, height=0.3, color=BLUE, fill_opacity=0.5)
        right_pan.move_to(beam.get_right() + DOWN*0.3)
        right_cable = Line(beam.get_right(), right_pan.get_top(), color=WHITE, stroke_width=1)
        self.play(Create(right_cable), Create(right_pan))
        self.wait(0.2)

        # Equation at top
        eq_label = Text("2x + 3 = 11", font_size=28, color=YELLOW)
        eq_label.to_edge(UP, buff=0.3)
        self.play(Write(eq_label))
        self.wait(0.3)

        # Put items on left pan: 2x boxes and 3 units
        left_items = VGroup()
        for i in range(2):
            box = Square(side_length=0.5, color=GREEN, fill_opacity=0.5, fill_color=GREEN)
            box.move_to(left_pan.get_top() + UP*0.3 + RIGHT*(i-0.5)*0.6)
            x_lab = Text("x", font_size=16, color=WHITE)
            x_lab.move_to(box.get_center())
            left_items.add(box, x_lab)

        for i in range(3):
            unit = Circle(radius=0.2, color=YELLOW, fill_opacity=0.8, fill_color=YELLOW)
            unit.move_to(left_pan.get_top() + UP*0.6 + RIGHT*(i-1)*0.4)
            left_items.add(unit)

        self.play(*[Create(item) for item in left_items])
        self.wait(0.3)

        # Put items on right pan: 11 units
        right_items = VGroup()
        for i in range(11):
            unit = Circle(radius=0.15, color=YELLOW, fill_opacity=0.8, fill_color=YELLOW)
            col = i % 5
            row = i // 5
            unit.move_to(right_pan.get_top() + UP*0.5 + RIGHT*(col-2)*0.3 + UP*row*0.3)
            right_items.add(unit)

        self.play(*[Create(item) for item in right_items])
        self.wait(0.5)

        # Step 1: Subtract 3 from both sides
        step1 = Text("Step 1: Subtract 3 from both sides", font_size=22, color=RED)
        step1.to_edge(DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(0.3)

        # Remove 3 units from left (animate fading)
        left_units = left_items[4:7]
        right_units_to_remove = right_items[0:3]
        self.play(
            *[FadeOut(u) for u in left_units],
            *[FadeOut(u) for u in right_units_to_remove]
        )
        self.wait(0.3)

        # Update equation
        self.play(FadeOut(eq_label))
        eq2 = Text("2x = 8", font_size=28, color=YELLOW)
        eq2.to_edge(UP, buff=0.3)
        self.play(Write(eq2))
        self.wait(0.3)

        self.play(FadeOut(step1))
        step2 = Text("Step 2: Divide both sides by 2", font_size=22, color=RED)
        step2.to_edge(DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.3)

        # Split x boxes (half remaining)
        self.play(FadeOut(left_items[0]), FadeOut(left_items[2]))
        self.wait(0.3)

        # Remove half of right items (7 through 10)
        remaining_right = right_items[3:]
        self.play(*[FadeOut(u) for u in remaining_right[3:7]])
        self.wait(0.3)

        self.play(FadeOut(eq2))
        eq3 = Text("x = 4", font_size=28, color=GREEN)
        eq3.to_edge(UP, buff=0.3)
        self.play(Write(eq3))
        self.wait(0.3)

        # Final highlight
        answer = Text("Answer: x = 4", font_size=32, color=YELLOW)
        answer.next_to(eq3, DOWN, buff=0.3)
        self.play(Write(answer))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
