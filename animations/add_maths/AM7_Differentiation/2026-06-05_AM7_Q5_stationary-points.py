from manim import *
import math

class Am7Q5Scene(Scene):
    def construct(self):
        # Title
        title = Text("Stationary Points", font_size=36, color=BLUE)
        subtitle = Text("AM7_Q5 | Differentiation", font_size=20, color=GRAY)
        subtitle.next_to(title, DOWN)
        self.play(Write(title), Write(subtitle))
        self.wait(1)
        self.play(FadeOut(title), FadeOut(subtitle))

        # Main visual: basic shapes
        circle = Circle(color=YELLOW)
        square = Square(color=GREEN)
        square.next_to(circle, RIGHT, buff=0.5)
        arrow = Arrow(circle.get_center(), square.get_center(), color=RED)
        
        label_a = Text("A", font_size=24, color=YELLOW)
        label_a.next_to(circle, UP)
        label_b = Text("B", font_size=24, color=GREEN)
        label_b.next_to(square, UP)
        
        self.play(Create(circle), Create(square), Create(arrow), Write(label_a), Write(label_b))
        self.wait(2)

        # Animate movement
        self.play(
            circle.animate.shift(RIGHT*2),
            square.animate.shift(RIGHT*2),
            arrow.animate.shift(RIGHT*2),
            label_a.animate.shift(RIGHT*2),
            label_b.animate.shift(RIGHT*2),
            run_time=1.5
        )
        self.wait(1)

        # Show concept text
        concept = Text("Stationary Points: AM7_Q5", font_size=28, color=WHITE)
        concept.to_edge(DOWN)
        self.play(Write(concept))
        self.wait(2)

        # Summary box
        box = Rectangle(width=6, height=0.8, color=BLUE)
        box.to_edge(DOWN, buff=0.2)
        summary = Text("AM7_Differentiation - Concept Visualised", font_size=20, color=WHITE)
        summary.move_to(box.get_center())
        self.play(Transform(concept, summary), Create(box))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(0.5)
