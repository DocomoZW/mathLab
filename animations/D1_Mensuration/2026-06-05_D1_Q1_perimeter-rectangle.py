from manim import *

class D1Q1PerimeterRect(Scene):
    def construct(self):
        title = Text("Perimeter of a Rectangle", font_size=26).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        rect = Rectangle(width=4, height=2.5, color=BLUE, stroke_width=3)
        rect.move_to(ORIGIN)
        self.play(Create(rect))
        self.wait(0.3)

        # Label sides
        l_label = Text("length = 12 cm", font_size=18, color=YELLOW).next_to(rect, DOWN, buff=0.3)
        w_label = Text("width = 8 cm", font_size=18, color=GREEN).next_to(rect, RIGHT, buff=0.3)
        self.play(Write(l_label), Write(w_label))
        self.wait(0.3)

        # Formula
        formula = Text("P = 2(l + w) = 2(12 + 8) = 40 cm", font_size=22, color=WHITE)
        formula.next_to(rect, DOWN, buff=1.0)
        self.play(Write(formula))
        self.wait(0.5)

        # Highlight perimeter
        vmobject = SurroundingRectangle(rect, color=RED, buff=0.05)
        self.play(Create(vmobject))
        self.wait(0.5)

        result = Text("Perimeter = 40 cm", font_size=28, color=YELLOW).to_edge(DOWN)
        self.play(Write(result))
        self.wait(1)
