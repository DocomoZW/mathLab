# topic_id: A1_Q7
# track: igcse_o
# unit: A1_Number
# description: Laws of indices visualized as expanding powers — showing a^m × a^n = a^(m+n)

from manim import *

class LawsOfIndices(Scene):
    def construct(self):
        # Title
        title = Text("Laws of Indices: Multiplying Powers", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Starting expression
        expression = Text("2³ × 2² = ?", font_size=48, color=YELLOW)
        expression.shift(UP * 1.0)
        self.play(Write(expression))
        self.wait(0.5)

        # Step 1: Expand 2³
        expand_3 = Text(
            "2³ = 2 × 2 × 2",
            font_size=32, color=GREEN
        )
        expand_3.next_to(expression, DOWN, buff=0.5, aligned_edge=LEFT)

        # Show the expanding animation
        dots_3 = VGroup()
        for i in range(3):
            d = Text("2", font_size=28, color=GREEN)
            d.shift(LEFT * 4.5 + DOWN * 0.3 + RIGHT * i * 0.7)
            dots_3.add(d)
            if i < 2:
                times = Text("×", font_size=24, color=WHITE)
                times.next_to(d, RIGHT, buff=0.1)
                dots_3.add(times)

        self.play(
            Write(expand_3),
            LaggedStart(*[Write(c) for c in dots_3], lag_ratio=0.2)
        )
        self.wait(0.3)

        # Step 2: Expand 2²
        expand_2 = Text(
            "2² = 2 × 2",
            font_size=32, color=BLUE
        )
        expand_2.next_to(expand_3, DOWN, buff=0.4, aligned_edge=LEFT)

        dots_2 = VGroup()
        for i in range(2):
            d = Text("2", font_size=28, color=BLUE)
            d.shift(LEFT * 4.5 + DOWN * 1.8 + RIGHT * i * 0.7)
            dots_2.add(d)
            if i < 1:
                times = Text("×", font_size=24, color=WHITE)
                times.next_to(d, RIGHT, buff=0.1)
                dots_2.add(times)

        self.play(
            Write(expand_2),
            LaggedStart(*[Write(c) for c in dots_2], lag_ratio=0.2)
        )
        self.wait(0.3)

        # Step 3: Combine all factors = 2⁵
        all_factors = Text(
            "2 × 2 × 2 × 2 × 2 = 2⁵",
            font_size=32, color=YELLOW
        )
        all_factors.next_to(expand_2, DOWN, buff=0.4, aligned_edge=LEFT)

        # Show the consolidation
        combined = VGroup()
        for i in range(5):
            d = Text("2", font_size=28, color=YELLOW)
            d.shift(LEFT * 4.5 + DOWN * 3.3 + RIGHT * i * 0.7)
            combined.add(d)
            if i < 4:
                times = Text("×", font_size=24, color=WHITE)
                times.next_to(d, RIGHT, buff=0.1)
                combined.add(times)

        right_side = Text("= 2⁵", font_size=32, color=YELLOW)
        right_side.next_to(combined, RIGHT, buff=0.3)

        self.play(
            LaggedStart(*[Write(c) for c in combined], lag_ratio=0.1),
            Write(right_side)
        )
        self.wait(0.5)

        # Step 4: Show the law
        law_box = Rectangle(width=8, height=1.0, color=YELLOW, fill_opacity=0.1)
        law_box.to_edge(DOWN, buff=0.3)

        law_text = Text(
            "aᵐ × aⁿ = aᵐ⁺ⁿ",
            font_size=36, color=YELLOW
        )
        law_text.move_to(law_box.get_center())

        example_text = Text(
            "2³ × 2² = 2³⁺² = 2⁵ = 32",
            font_size=28, color=WHITE
        )
        example_text.next_to(law_text, DOWN, buff=0.15)

        self.play(
            Create(law_box),
            Write(law_text),
            Write(example_text)
        )
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = LawsOfIndices()
    scene.render()
