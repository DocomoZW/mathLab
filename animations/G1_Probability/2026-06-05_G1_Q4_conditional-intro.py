from manim import *
import math

class G1Q4ConditionalIntro(Scene):
    def construct(self):
        title = Text("Conditional Probability", font_size=24, color=WHITE)
        title.to_edge(UP)
        self.play(Write(title))

        # Show a scenario: 20 students, 12 girls, 8 boys, 6 girls wear glasses, 2 boys wear glasses
        # Draw a rectangle representing all students
        rect_all = Rectangle(width=4, height=2.5, color=WHITE)
        rect_all.shift(DOWN * 0.3)
        self.play(Create(rect_all))
        label_all = Text("All: 20", font_size=20, color=WHITE)
        label_all.next_to(rect_all, UP * 0.2)
        self.play(Write(label_all))

        # Draw overlapping circles for Girls and Glasses
        circle_girls = Circle(radius=1.2, color=PINK)
        circle_girls.shift(LEFT * 0.8 + DOWN * 0.3)
        label_girls = Text("Girls: 12", font_size=18, color=PINK)
        label_girls.next_to(circle_girls, UP * 0.8)
        self.play(Create(circle_girls), Write(label_girls))

        circle_glasses = Circle(radius=1.0, color=GREEN)
        circle_glasses.shift(RIGHT * 0.8 + DOWN * 0.3)
        label_glasses = Text("Glasses: 8", font_size=18, color=GREEN)
        label_glasses.next_to(circle_glasses, UP * 0.8)
        self.play(Create(circle_glasses), Write(label_glasses))

        # Overlap label
        overlap_label = Text("6", font_size=20, color=YELLOW)
        overlap_label.shift(DOWN * 0.3)
        self.play(Write(overlap_label))

        # Show conditional probability formula
        formula = Text("P(Girl | Glasses) = 6/8", font_size=22, color=YELLOW)
        formula.shift(DOWN * 2.2)
        self.play(Write(formula))

        self.wait(2)
        self.play(FadeOut(title), FadeOut(rect_all), FadeOut(label_all),
                  FadeOut(circle_girls), FadeOut(label_girls),
                  FadeOut(circle_glasses), FadeOut(label_glasses),
                  FadeOut(overlap_label), FadeOut(formula))
