from manim import *
import math

class H1Q7LineOfBestFit(Scene):
    def construct(self):
        title = Text("Line of Best Fit").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Axes
        x_axis = Line(LEFT * 4, RIGHT * 4, color=WHITE)
        x_axis.shift(DOWN * 2.0)
        y_axis = Line(DOWN * 2.0, UP * 2.5, color=WHITE)
        y_axis.shift(LEFT * 4)

        self.play(Create(x_axis), Create(y_axis))
        self.wait(0.2)

        x_label = Text("x", font_size=18, color=GRAY)
        x_label.shift(RIGHT * 4.2 + DOWN * 2.0)
        y_label = Text("y", font_size=18, color=GRAY)
        y_label.shift(LEFT * 4.2 + UP * 2.5)

        # Scatter points (positive correlation)
        points_data = [(0.5, 0.4), (1.0, 0.8), (1.5, 1.2), (2.0, 1.6),
                       (2.5, 2.0), (3.0, 2.4), (3.5, 2.8), (4.0, 3.2)]

        def coord(x, y):
            return LEFT * 3.5 + RIGHT * x * 1.2 + DOWN * 2.0 + UP * y * 0.8

        dots = VGroup()
        for px, py in points_data:
            dot = Dot(color=BLUE, radius=0.08)
            dot.move_to(coord(px, py))
            dots.add(dot)

        self.play(Create(dots))
        self.wait(0.3)

        # Line of best fit
        # y = 0.8 * x - 0.05 (approximately through the points)
        line_start_x = 0.0
        line_start_y = 0.0
        line_end_x = 4.5
        line_end_y = 3.55

        line_of_fit = Line(
            coord(line_start_x, line_start_y),
            coord(line_end_x, line_end_y),
            color=RED
        )
        self.play(Create(line_of_fit))
        self.wait(0.3)

        line_label = Text("Line of best fit", font_size=18, color=RED)
        line_label.shift(UP * 2.0 + RIGHT * 2.0)
        self.play(Write(line_label))
        self.wait(0.3)

        # Interpolation: estimate y at x=2.2
        interp_x = 2.2
        interp_y = 0.8 * interp_x - 0.05
        interp_dot = Dot(color=YELLOW, radius=0.12)
        interp_dot.move_to(coord(interp_x, interp_y))

        interp_arrow = Arrow(
            coord(interp_x, interp_y) + UP * 0.5,
            coord(interp_x, interp_y),
            color=YELLOW
        )
        interp_label = Text("Interpolation\n(estimate within data)", font_size=14, color=YELLOW)
        interp_label.move_to(coord(interp_x, interp_y) + UP * 1.0)

        self.play(Create(interp_dot), Create(interp_arrow), Write(interp_label))
        self.wait(0.5)

        # Extrapolation: predict y at x=5.0
        extra_x = 5.0
        extra_y = 0.8 * extra_x - 0.05
        extra_dot = Dot(color=GREEN, radius=0.12)
        extra_dot.move_to(coord(extra_x, extra_y))

        extra_arrow = Arrow(
            coord(extra_x, extra_y) + DOWN * 0.5,
            coord(extra_x, extra_y),
            color=GREEN
        )
        extra_label = Text("Extrapolation\n(predict beyond data)", font_size=14, color=GREEN)
        extra_label.move_to(coord(extra_x, extra_y) + DOWN * 1.2)

        self.play(Create(extra_dot), Create(extra_arrow), Write(extra_label))
        self.wait(0.5)

        # Dashed line showing extrapolation
        dashed_line = DashedLine(
            coord(4.0, 3.15),
            coord(extra_x, extra_y),
            color=GREEN
        )
        self.play(Create(dashed_line))
        self.wait(0.5)

        note = Text("Interpolation: reliable | Extrapolation: less reliable", font_size=16, color=GRAY)
        note.to_edge(DOWN)
        note.shift(UP * 0.3)
        self.play(Write(note))
        self.wait(2)
