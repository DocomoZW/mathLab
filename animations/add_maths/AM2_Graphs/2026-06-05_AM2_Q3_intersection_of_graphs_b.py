from manim import *
import math

class TangentCondition(Scene):
    def construct(self):
        title = Text("Tangent: One Intersection Point", font_size=34)
        title.to_edge(UP)
        self.play(Write(title))

        # Three cases
        c1_title = Text("Case 1: Two Intersections (Delta > 0)", font_size=24, color=BLUE)
        c1_title.shift(UP*1.5 + LEFT*3)
        self.play(Write(c1_title))

        c2_title = Text("Case 2: Tangent (Delta = 0)", font_size=24, color=GREEN)
        c2_title.move_to(UP*1.5)
        self.play(Write(c2_title))

        c3_title = Text("Case 3: No Intersection (Delta < 0)", font_size=24, color=RED)
        c3_title.shift(UP*1.5 + RIGHT*3)
        self.play(Write(c3_title))

        # Small axes + graphs (case 1)
        ax1x = Line(LEFT*1.2, RIGHT*1.2, color=WHITE)
        ax1x.shift(LEFT*3 + DOWN*0.5)
        ax1y = Line(DOWN*0.5, UP*0.5, color=WHITE)
        ax1y.shift(LEFT*3 + DOWN*0.5)
        self.play(Create(ax1x), Create(ax1y))

        # Parabola
        pts1 = []
        for x in range(-10, 11):
            fx = x/10
            pts1.append([fx*1.0 + LEFT[0]*3, fx*fx*0.8 - 0.5, 0])
        p1 = VMobject(stroke_color=BLUE, stroke_width=2)
        p1.set_points_smoothly(pts1)
        self.play(Create(p1))

        # Line crossing twice
        l1 = Line(LEFT*4 + DOWN*0.8, RIGHT*4 + UP*0.2, color=GREEN, stroke_width=2)
        l1.shift(LEFT*3 + DOWN*0.5)
        self.play(Create(l1))

        # Case 2 - tangent
        ax2x = Line(LEFT*1.2, RIGHT*1.2, color=WHITE)
        ax2x.shift(DOWN*0.5)
        ax2y = Line(DOWN*0.5, UP*0.5, color=WHITE)
        ax2y.shift(DOWN*0.5)
        self.play(Create(ax2x), Create(ax2y))

        pts2 = []
        for x in range(-10, 11):
            fx = x/10
            pts2.append([fx*1.0, fx*fx*0.8 - 0.5, 0])
        p2 = VMobject(stroke_color=BLUE, stroke_width=2)
        p2.set_points_smoothly(pts2)
        self.play(Create(p2))

        l2 = Line(LEFT*2 + DOWN*0.2, RIGHT*2 + DOWN*0.2, color=GREEN, stroke_width=2)
        l2.shift(DOWN*0.5)
        self.play(Create(l2))

        # Case 3 - no intersection
        ax3x = Line(LEFT*1.2, RIGHT*1.2, color=WHITE)
        ax3x.shift(RIGHT*3 + DOWN*0.5)
        ax3y = Line(DOWN*0.5, UP*0.5, color=WHITE)
        ax3y.shift(RIGHT*3 + DOWN*0.5)
        self.play(Create(ax3x), Create(ax3y))

        pts3 = []
        for x in range(-10, 11):
            fx = x/10
            pts3.append([fx*1.0 + RIGHT[0]*3, fx*fx*0.8 - 0.5, 0])
        p3 = VMobject(stroke_color=BLUE, stroke_width=2)
        p3.set_points_smoothly(pts3)
        self.play(Create(p3))

        l3 = Line(LEFT*2 + DOWN*1.2, RIGHT*2 + DOWN*0.5, color=GREEN, stroke_width=2)
        l3.shift(RIGHT*3 + DOWN*0.5)
        self.play(Create(l3))

        note = Text("Discriminant of substituted equation tells which case", font_size=22, color=YELLOW)
        note.to_edge(DOWN)
        self.play(Write(note))

        self.wait(2)
