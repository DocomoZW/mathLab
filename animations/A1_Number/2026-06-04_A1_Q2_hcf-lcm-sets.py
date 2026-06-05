# topic_id: A1_Q2
# track: igcse_o
# unit: A1_Number
# description: HCF/LCM of 60 and 84 visual using intersecting prime factor sets

from manim import *

class HcfLcmSets(Scene):
    def construct(self):
        # Title
        title = Text("HCF and LCM: Intersecting Prime Factors", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Show the two numbers
        num1 = Text("60 = 2² × 3 × 5", font_size=32, color=GREEN)
        num2 = Text("84 = 2² × 3 × 7", font_size=32, color=BLUE)
        num1.shift(UP * 1.5 + LEFT * 3)
        num2.shift(UP * 1.5 + RIGHT * 3)

        self.play(Write(num1), Write(num2))
        self.wait(0.5)

        # Draw two overlapping circles/sets
        # Set A (factors of 60) - left
        set_a = Circle(radius=2.0, color=GREEN, stroke_width=3)
        set_a.shift(LEFT * 1.5 + DOWN * 0.5)
        set_a_label = Text("Factors of 60", color=GREEN, font_size=22)
        set_a_label.next_to(set_a, UP, buff=0.1)

        # Set B (factors of 84) - right
        set_b = Circle(radius=2.0, color=BLUE, stroke_width=3)
        set_b.shift(RIGHT * 1.5 + DOWN * 0.5)
        set_b_label = Text("Factors of 84", color=BLUE, font_size=22)
        set_b_label.next_to(set_b, UP, buff=0.1)

        self.play(
            Create(set_a), Write(set_a_label),
            Create(set_b), Write(set_b_label),
        )
        self.wait(0.3)

        # Animate prime factors appearing in the sets
        # 60's unique factor: 5 (on left, not in intersection)
        factor_5 = Text("5", font_size=36, color=GREEN)
        factor_5.move_to(set_a.get_center() + LEFT * 1.0)

        # 84's unique factor: 7 (on right, not in intersection)
        factor_7 = Text("7", font_size=36, color=BLUE)
        factor_7.move_to(set_b.get_center() + RIGHT * 1.0)

        # Common factors in intersection: 2² and 3
        factor_22 = Text("2²", font_size=36, color=YELLOW)
        factor_3 = Text("3", font_size=36, color=YELLOW)
        intersection_center = (set_a.get_center() + set_b.get_center()) / 2
        factor_22.move_to(intersection_center + UP * 0.4)
        factor_3.move_to(intersection_center + DOWN * 0.4)

        # Animate factors appearing one by one
        self.play(Write(factor_5))
        self.wait(0.2)
        self.play(Write(factor_7))
        self.wait(0.2)
        self.play(Write(factor_22))
        self.wait(0.2)
        self.play(Write(factor_3))
        self.wait(0.3)

        # Highlight intersection
        intersection_label = Text("Common Factors", font_size=18, color=YELLOW)
        intersection_label.next_to(intersection_center, DOWN, buff=0.5)
        inter_box = SurroundingRectangle(VGroup(factor_22, factor_3), color=YELLOW, buff=0.15)
        self.play(
            Create(inter_box),
            Write(intersection_label)
        )
        self.wait(0.3)

        # Show HCF = product of intersection (lowest powers)
        hcf_text = Text(
            "HCF = 2² × 3 = 12",
            font_size=32, color=YELLOW
        )
        hcf_text.to_edge(DOWN, buff=1.0)
        hcf_box = SurroundingRectangle(hcf_text, color=YELLOW, buff=0.1)

        self.play(Write(hcf_text), Create(hcf_box))
        self.wait(0.3)

        # Show LCM = product of all (highest powers)
        lcm_text = Text(
            "LCM = 2² × 3 × 5 × 7 = 420",
            font_size=32, color=ORANGE
        )
        lcm_text.next_to(hcf_text, DOWN, buff=0.4)
        lcm_box = SurroundingRectangle(lcm_text, color=ORANGE, buff=0.1)

        self.play(Write(lcm_text), Create(lcm_box))
        self.wait(1)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = HcfLcmSets()
    scene.render()
