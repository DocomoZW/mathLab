# topic_id: A1_Q3
# track: igcse_o
# unit: A1_Number
# description: Visual fraction addition 1/4 + 1/3 = 7/12 using pie charts

from manim import *
import math

class FractionAdditionPies(Scene):
    def construct(self):
        # Title
        title = Text("Fraction Addition: 1/4 + 1/3 = ?", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Helper: create a filled sector
        def create_sector(radius, start_angle, end_angle, color, opacity=0.7):
            """Create a sector of a circle from start_angle to end_angle (radians, measured from 3-o'clock, CCW)"""
            # Start from center
            start_point = radius * np.array([math.cos(start_angle), math.sin(start_angle), 0])
            end_point = radius * np.array([math.cos(end_angle), math.sin(end_angle), 0])

            # Build the sector as a Polygon from center + arc points
            n_points = 30
            arc_points = [
                radius * np.array([math.cos(start_angle + t * (end_angle - start_angle)),
                                   math.sin(start_angle + t * (end_angle - start_angle)), 0])
                for t in np.linspace(0, 1, n_points)
            ]
            vertices = [np.array([0, 0, 0])] + arc_points
            sector = Polygon(*vertices, color=color, fill_color=color, fill_opacity=opacity, stroke_width=2)
            return sector

        # First fraction: 1/4 (green)
        frac1_label = Text("1/4", font_size=28, color=GREEN)
        frac1_label.shift(UP * 0.5 + LEFT * 3.0)

        pie1 = VGroup()
        # Whole circle outline
        circle1 = Circle(radius=1.2, color=GREEN, stroke_width=2)
        circle1.shift(LEFT * 3.0 + DOWN * 0.5)

        # Sector for 1/4 (90 degrees, starting from top = PI/2)
        sector1 = create_sector(1.2, math.pi/2, math.pi, GREEN)
        sector1.shift(LEFT * 3.0 + DOWN * 0.5)
        pie1.add(circle1, sector1)

        self.play(
            Write(frac1_label),
            Create(circle1),
            Create(sector1)
        )
        self.wait(0.3)

        # Second fraction: 1/3 (blue)
        frac2_label = Text("1/3", font_size=28, color=BLUE)
        frac2_label.shift(UP * 0.5 + RIGHT * 0)

        pie2 = VGroup()
        circle2 = Circle(radius=1.2, color=BLUE, stroke_width=2)
        circle2.shift(RIGHT * 0 + DOWN * 0.5)

        # Sector for 1/3 (120 degrees)
        sector2 = create_sector(1.2, math.pi/2, math.pi/2 + 2*math.pi/3, BLUE)
        sector2.shift(RIGHT * 0 + DOWN * 0.5)
        pie2.add(circle2, sector2)

        self.play(
            Write(frac2_label),
            Create(circle2),
            Create(sector2)
        )
        self.wait(0.3)

        # Plus sign
        plus = Text("+", font_size=40, color=WHITE)
        plus.shift(LEFT * 1.5)
        self.play(Write(plus))
        self.wait(0.3)

        # Equals sign and result
        equals = Text("=", font_size=40, color=WHITE)
        equals.shift(RIGHT * 1.5)
        self.play(Write(equals))
        self.wait(0.2)

        # Result pie: 7/12 (orange)
        result_label = Text("7/12", font_size=28, color=ORANGE)
        result_label.shift(UP * 0.5 + RIGHT * 3.0)

        pie3 = VGroup()
        circle3 = Circle(radius=1.2, color=ORANGE, stroke_width=2)
        circle3.shift(RIGHT * 3.0 + DOWN * 0.5)

        # Show 7/12 by splitting into 12 sectors and filling 7
        for i in range(12):
            start_angle = math.pi/2 - i * 2*math.pi/12
            end_angle = math.pi/2 - (i+1) * 2*math.pi/12
            if i < 7:  # Fill first 7
                sec = create_sector(1.2, end_angle, start_angle, ORANGE)
                sec.shift(RIGHT * 3.0 + DOWN * 0.5)
                pie3.add(sec)

        pie3.add(circle3)

        self.play(
            Write(result_label),
            Create(circle3),
            *[Create(s) for s in pie3[:-1]]
        )
        self.wait(0.5)

        # Show the common denominator method
        method_box = Rectangle(width=8, height=1.5, color=WHITE, fill_opacity=0.1)
        method_box.to_edge(DOWN, buff=0.5)

        method_text = Text(
            "1/4 + 1/3 = 3/12 + 4/12 = 7/12",
            font_size=32, color=WHITE
        )
        method_text.move_to(method_box.get_center())

        method_label = Text("Common Denominator: LCM(4,3) = 12", font_size=20, color=YELLOW)
        method_label.next_to(method_box, UP, buff=0.1)

        self.play(
            Create(method_box),
            Write(method_text),
            Write(method_label)
        )
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = FractionAdditionPies()
    scene.render()
