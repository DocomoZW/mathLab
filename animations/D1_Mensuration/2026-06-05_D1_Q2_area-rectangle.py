from manim import *

class D1Q2AreaRect(Scene):
    def construct(self):
        title = Text("Area of a Rectangle", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        rect = Rectangle(width=5, height=3, color=BLUE, stroke_width=3)
        rect.move_to(ORIGIN)
        self.play(Create(rect))
        self.wait(0.3)

        # Fill with squares
        cols, rows = 5, 3
        squares = VGroup()
        for i in range(cols):
            for j in range(rows):
                sq = Square(side_length=1, color=BLUE_E, fill_opacity=0.3, stroke_width=1)
                sq.move_to(rect.get_corner(UL) + RIGHT * (i + 0.5) + DOWN * (j + 0.5))
                squares.add(sq)
        self.play(*[Create(sq) for sq in squares], run_time=1.5)
        self.wait(0.3)

        count_text = Text("5 x 3 = 15 unit squares", font_size=20, color=WHITE).shift(DOWN * 2)
        self.play(Write(count_text))
        self.wait(0.3)

        area_text = Text("Area = length x width = l x w", font_size=22, color=YELLOW).shift(DOWN * 3)
        self.play(Write(area_text))
        self.wait(1)
