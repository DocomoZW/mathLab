# topic_id: A1_Q2
# track: igcse_o
# unit: A1_Number
# description: Prime factorization tree animation for 60 showing step-by-step decomposition

from manim import *

class PrimeFactorTree(Scene):
    def construct(self):
        # Title
        title = Text("Prime Factorisation: Factor Tree for 60", font_size=36, color=BLUE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title))
        self.wait(0.3)

        # Root: 60
        root = Text("60", font_size=48, color=YELLOW)
        root.move_to(UP * 2.5)
        self.play(Write(root))
        self.wait(0.3)

        # Level 1: Split 60 = 6 × 10
        l1_left = Text("6", font_size=40, color=GREEN)
        l1_right = Text("10", font_size=40, color=GREEN)
        l1_left.shift(UP * 0.5 + LEFT * 2.0)
        l1_right.shift(UP * 0.5 + RIGHT * 2.0)

        # Lines from root to children
        line1_l = Line(root.get_bottom(), l1_left.get_top(), color=WHITE)
        line1_r = Line(root.get_bottom(), l1_right.get_top(), color=WHITE)

        self.play(
            Create(line1_l), Create(line1_r),
            TransformFromCopy(root.copy(), l1_left),
            TransformFromCopy(root.copy(), l1_right),
        )
        self.wait(0.3)

        # Level 2: Split 6 = 2 × 3, 10 = 2 × 5
        l2_ll = Text("2", font_size=36, color=RED)
        l2_lr = Text("3", font_size=36, color=RED)
        l2_ll.shift(DOWN * 1.2 + LEFT * 3.0)
        l2_lr.shift(DOWN * 1.2 + LEFT * 1.0)

        l2_rl = Text("2", font_size=36, color=RED)
        l2_rr = Text("5", font_size=36, color=RED)
        l2_rl.shift(DOWN * 1.2 + RIGHT * 1.0)
        l2_rr.shift(DOWN * 1.2 + RIGHT * 3.0)

        # Lines from 6
        line2_ll = Line(l1_left.get_bottom(), l2_ll.get_top(), color=WHITE)
        line2_lr = Line(l1_left.get_bottom(), l2_lr.get_top(), color=WHITE)
        # Lines from 10
        line2_rl = Line(l1_right.get_bottom(), l2_rl.get_top(), color=WHITE)
        line2_rr = Line(l1_right.get_bottom(), l2_rr.get_top(), color=WHITE)

        self.play(
            Create(line2_ll), Create(line2_lr),
            Create(line2_rl), Create(line2_rr),
        )
        self.wait(0.2)

        # Show 2, 3, 2, 5 as the primes
        self.play(
            Write(l2_ll), Write(l2_lr),
            Write(l2_rl), Write(l2_rr),
        )
        self.wait(0.3)

        # Highlight all prime numbers (they're all primes here)
        primes = VGroup(l2_ll, l2_lr, l2_rl, l2_rr)
        for p in primes:
            self.play(Indicate(p, color=RED, scale_factor=1.3))
            self.wait(0.15)

        # Final result box
        result_box = Rectangle(width=7, height=0.8, color=YELLOW)
        result_box.to_edge(DOWN, buff=0.8)
        result_text = Text(
            "60 = 2 × 2 × 3 × 5 = 2² × 3 × 5",
            font_size=36, color=YELLOW
        )
        result_text.move_to(result_box.get_center())

        self.play(
            Create(result_box),
            Write(result_text)
        )
        self.wait(1.5)

        # Fade out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


if __name__ == "__main__":
    scene = PrimeFactorTree()
    scene.render()
