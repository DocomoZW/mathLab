# topic_id: A1_Q1
# track: igcse_o
# unit: A1_Number
# description: Venn diagram of number classifications (N subset Z subset Q subset R) with example numbers

from manim import *

class VennDiagramClassification(Scene):
    def construct(self):
        # Title
        title = Text("Number Classification: Venn Diagram", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Create nested circles for R, Q, Z, N
        # R - largest (outermost)
        r_circle = Circle(radius=3.0, color=PURPLE, stroke_width=3)
        r_label = Text("R", color=PURPLE, font_size=40)
        r_label.move_to(r_circle.get_center() + UP * 2.5 + RIGHT * 3.5)

        # Q - inside R
        q_circle = Circle(radius=2.3, color=YELLOW, stroke_width=3)
        q_label = Text("Q", color=YELLOW, font_size=36)
        q_label.move_to(q_circle.get_center() + UP * 1.5 + RIGHT * 2.8)

        # Z - inside Q
        z_circle = Circle(radius=1.6, color=BLUE, stroke_width=3)
        z_label = Text("Z", color=BLUE, font_size=32)
        z_label.move_to(z_circle.get_center() + UP * 0.5 + RIGHT * 1.8)

        # N - inside Z (center)
        n_circle = Circle(radius=0.9, color=GREEN, stroke_width=3)
        n_label = Text("N", color=GREEN, font_size=28)

        all_circles = VGroup(r_circle, q_circle, z_circle, n_circle)
        all_circles.shift(DOWN * 0.3 + LEFT * 0.5)

        self.play(
            Create(r_circle),
            Write(r_label)
        )
        self.wait(0.2)
        self.play(
            Create(q_circle),
            Write(q_label)
        )
        self.wait(0.2)
        self.play(
            Create(z_circle),
            Write(z_label)
        )
        self.wait(0.2)
        self.play(
            Create(n_circle),
            Write(n_label)
        )
        self.wait(0.3)

        # Add example numbers with arrows into the right regions
        examples = VGroup()

        # Natural numbers -> center (N)
        nat_ex = Text("1, 2, 3, ...", color=GREEN, font_size=22)
        nat_ex.next_to(n_circle, UP, buff=0.1)

        # Integers but not natural -> Z \ N region
        int_ex = Text("-3, -2, -1", color=BLUE, font_size=22)
        int_ex.move_to(z_circle.get_center() + LEFT * 0.3 + DOWN * 0.2)

        # Rational but not integer -> Q \ Z region
        rat_ex = Text("1/2, 3/4, 0.3...", color=YELLOW, font_size=22)
        rat_ex.move_to(q_circle.get_center() + LEFT * 0.5 + DOWN * 1.0)

        # Irrational (R \ Q)
        irr_ex = Text("pi, e, sqrt(2)", color=RED, font_size=22)
        irr_ex.move_to(r_circle.get_center() + RIGHT * 1.0 + DOWN * 0.3)

        self.play(
            Write(nat_ex),
            Write(int_ex),
            Write(rat_ex),
            Write(irr_ex),
        )
        self.wait(0.5)

        # Animate each example appearing with a flash
        for ex, text in [(nat_ex, "Natural"), (int_ex, "Integers"), (rat_ex, "Rational"), (irr_ex, "Irrational")]:
            box = SurroundingRectangle(ex, color=WHITE, buff=0.05)
            label = Text(text, font_size=16, color=WHITE)
            label.next_to(ex, RIGHT, buff=0.2)
            self.play(Create(box), Write(label))
            self.wait(0.2)
            self.play(FadeOut(box), FadeOut(label))

        # Summary inference at bottom
        summary = Text(
            "Every natural is an integer.\nEvery integer is rational.\nEvery rational is real.\nBut not every real is rational!",
            font_size=20, color=WHITE, line_spacing=1.3
        )
        summary.to_edge(DOWN, buff=0.3)
        self.play(Write(summary))
        self.wait(1.5)

        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = VennDiagramClassification()
    scene.render()
