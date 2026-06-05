from manim import *
import math

class ShadingRegion(Scene):
    def construct(self):
        title = Text("Inequalities on Graphs", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))

        # Axes
        x_axis = Line(LEFT*4, RIGHT*4, color=WHITE)
        x_axis.shift(DOWN*1.5)
        y_axis = Line(DOWN*2.5, UP*1.5, color=WHITE)
        y_axis.shift(LEFT*4)
        self.play(Create(x_axis), Create(y_axis))

        xl = Text("x", font_size=20)
        xl.next_to(x_axis, RIGHT)
        yl = Text("y", font_size=20)
        yl.next_to(y_axis, UP)
        self.play(Write(xl), Write(yl))

        # Draw boundary line y = x + 1
        boundary = Line(LEFT*3 + DOWN*1, RIGHT*3 + UP*2, color=GREEN)
        self.play(Create(boundary))

        label = Text("y = x + 1", font_size=22, color=GREEN)
        label.next_to(boundary, UP, buff=0.1)
        self.play(Write(label))

        # Dashed vs solid explanation
        solid_info = Text("Solid line: y <= x + 1 or y >= x + 1", font_size=22, color=WHITE)
        solid_info.shift(DOWN*2.5)
        self.play(Write(solid_info))

        dashed_info = Text("Dashed line: y < x + 1 or y > x + 1", font_size=22, color=GREY)
        dashed_info.next_to(solid_info, DOWN, buff=0.3)
        self.play(Write(dashed_info))

        self.wait(0.5)

        # Shading info
        test = Text("Test (0,0): 0 <= 0+1 = 1 (True) => shade below", font_size=22, color=YELLOW)
        test.next_to(dashed_info, DOWN, buff=0.5)
        self.play(Write(test))

        # Create a shaded polygon (below the line)
        shade = Polygon(
            LEFT*3 + DOWN*1.5,
            LEFT*3 + DOWN*2.5,
            RIGHT*3 + DOWN*2.5,
            RIGHT*3 + DOWN*2,
            color=BLUE, fill_opacity=0.3, stroke_opacity=0
        )
        self.play(Create(shade))

        shade_label = Text("Shaded region satisfies the inequality", font_size=22, color=BLUE)
        shade_label.next_to(shade, DOWN, buff=0.3)
        self.play(Write(shade_label))

        self.wait(2)
