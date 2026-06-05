# topic_id: B1_Q3
# track: igcse_o
# unit: B1_Algebra
# description: Number line visualisation for solving inequalities

from manim import *

class B1Q3InequalityNumberLine(Scene):
    def construct(self):
        title = Text("Inequalities on a Number Line", font_size=30, color=BLUE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title))
        self.wait(0.3)

        # Draw number line
        num_line = Line(LEFT*4.5, RIGHT*4.5, color=WHITE, stroke_width=2)
        num_line.shift(DOWN*0.5)
        self.play(Create(num_line))
        self.wait(0.2)

        # Add ticks and labels at -5 to 5
        ticks = VGroup()
        labels = VGroup()
        for i in range(-5, 6):
            tick = Line(UP*0.15, DOWN*0.15, color=WHITE, stroke_width=1)
            tick.move_to(num_line.point_from_proportion((i+5)/10))
            label = Text(str(i), font_size=16, color=WHITE)
            label.next_to(tick, DOWN, buff=0.15)
            ticks.add(tick)
            labels.add(label)

        self.play(Create(ticks), Write(labels))
        self.wait(0.3)

        # Show the inequality
        inequality = Text("2x - 3 > 5", font_size=30, color=YELLOW)
        inequality.shift(UP*1.5)
        self.play(Write(inequality))
        self.wait(0.5)

        # Step 1: Add 3
        step1 = Text("Add 3: 2x > 8", font_size=24, color=WHITE)
        step1.next_to(inequality, DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(0.3)

        # Step 2: Divide by 2
        self.play(FadeOut(step1))
        step2 = Text("Divide by 2: x > 4", font_size=24, color=GREEN)
        step2.next_to(inequality, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.3)

        # Highlight the region x > 4
        arrow = Arrow(LEFT*0.3, RIGHT*0.3, color=RED)
        arrow.move_to(num_line.point_from_proportion((4+5)/10) + UP*0.4)

        # Actually, let's mark x=4
        point4 = Dot(num_line.point_from_proportion((4+5)/10), color=RED)
        open_circle = Circle(radius=0.15, color=RED, stroke_width=3)
        open_circle.move_to(point4.get_center())
        self.play(Create(open_circle))
        self.wait(0.2)

        # Shade region to the right
        shade_line = Line(
            num_line.point_from_proportion((4+5)/10) + RIGHT*0.15,
            num_line.point_from_proportion(1),
            color=RED, stroke_width=6
        )
        self.play(Create(shade_line))
        self.wait(0.3)

        # An arrow at the end
        endpoint = Dot(num_line.get_right(), color=RED, radius=0)
        right_arrow = Arrow(RIGHT*0.1, RIGHT*0.5, color=RED)
        right_arrow.next_to(num_line.get_right(), RIGHT, buff=0)
        right_arrow.shift(UP * 0.02)
        self.play(Create(right_arrow))
        self.wait(0.4)

        # Label
        region = Text("x > 4", font_size=26, color=RED)
        region.next_to(num_line, UP, buff=0.3)
        region.shift(RIGHT*2.5)
        self.play(Write(region))
        self.wait(0.5)

        # Flip sign example
        self.play(FadeOut(inequality), FadeOut(step2), FadeOut(region))
        flip_title = Text("BUT: Multiply/Divide by Negative Flips Sign!", font_size=22, color=RED)
        flip_title.shift(UP*1.8)
        self.play(Write(flip_title))
        self.wait(0.3)

        flip_expr = Text("-2x > 6  =>  x < -3", font_size=28, color=YELLOW)
        flip_expr.next_to(flip_title, DOWN, buff=0.3)
        self.play(Write(flip_expr))
        self.wait(0.5)

        # Show x < -3 on number line
        # Mark -3 with open circle
        point_neg3 = Dot(num_line.point_from_proportion((-3+5)/10), color=GREEN)
        open_circle2 = Circle(radius=0.15, color=GREEN, stroke_width=3)
        open_circle2.move_to(point_neg3.get_center())
        self.play(Create(open_circle2))
        self.wait(0.2)

        # Shade left
        shade_left = Line(
            num_line.point_from_proportion(0),
            num_line.point_from_proportion((-3+5)/10) - LEFT*0.15,
            color=GREEN, stroke_width=6
        )
        self.play(Create(shade_left))
        self.wait(0.3)

        left_arrow = Arrow(LEFT*0.1, LEFT*0.5, color=GREEN)
        left_arrow.next_to(num_line.get_left(), LEFT, buff=0)
        left_arrow.shift(UP * 0.02)
        self.play(Create(left_arrow))

        region2 = Text("x < -3", font_size=26, color=GREEN)
        region2.next_to(num_line, UP, buff=0.3)
        region2.shift(LEFT*2.5)
        self.play(Write(region2))
        self.wait(1.0)

        self.play(*[FadeOut(m) for m in self.mobjects])
