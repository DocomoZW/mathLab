from manim import *
import math

class CompSquare(Scene):
    def construct(self):
        title = Text("Completing the Square", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show x^2 + 6x + 11 = (x+3)^2 + 2
        step1 = Text("x^2 + 6x + 11", font_size=28)
        step1.next_to(title, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(1)
        
        step2 = Text("= (x^2 + 6x) + 11", font_size=28)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(1)
        
        step3 = Text("= (x + 3)^2 - 9 + 11", font_size=28)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(1)
        
        step4 = Text("= (x + 3)^2 + 2", font_size=28)
        step4.next_to(step3, DOWN, buff=0.3)
        self.play(Write(step4))
        self.wait(1)
        
        # Highlight the vertex
        box = Rectangle(width=3.5, height=0.5, color=YELLOW)
        box.move_to(step4.get_center())
        self.play(Create(box))
        self.wait(0.5)
        
        vertex = Text("Vertex: (-3, 2)", font_size=28, color=YELLOW)
        vertex.next_to(step4, DOWN, buff=0.5)
        self.play(Write(vertex))
        self.wait(2)


class DiscriminantNature(Scene):
    def construct(self):
        title = Text("The Discriminant b^2 - 4ac", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        items = [
            Text("Delta > 0 : Two distinct real roots", font_size=26, color=GREEN),
            Text("Delta = 0 : One repeated real root", font_size=26, color=YELLOW),
            Text("Delta < 0 : No real roots", font_size=26, color=RED)
        ]
        
        for i, item in enumerate(items):
            item.next_to(title, DOWN, buff=0.5 + i * 0.6)
            self.play(Write(item))
            self.wait(0.5)
        
        self.wait(1)
        
        # Example
        example = Text("Example: 2x^2 - 3x + 5 = 0", font_size=26)
        example.next_to(items[-1], DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        calc = Text("Delta = (-3)^2 - 4(2)(5) = 9 - 40 = -31", font_size=24)
        calc.next_to(example, DOWN, buff=0.3)
        self.play(Write(calc))
        self.wait(0.5)
        
        result = Text("-31 < 0, so no real roots", font_size=24, color=RED)
        result.next_to(calc, DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(2)
