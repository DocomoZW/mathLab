from manim import *
import math

class DirectProof(Scene):
    def construct(self):
        title = Text("Direct Proof", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        concept = Text("Start from known facts, reach the conclusion logically", font_size=24)
        concept.next_to(title, DOWN, buff=0.5)
        self.play(Write(concept))
        self.wait(0.5)
        
        # Example: sum of two odds is even
        ex_title = Text("Example: Sum of two odd numbers is even", font_size=24, color=YELLOW)
        ex_title.next_to(concept, DOWN, buff=0.5)
        self.play(Write(ex_title))
        
        step1 = Text("Let odd numbers be 2m+1 and 2n+1", font_size=22)
        step1.next_to(ex_title, DOWN, buff=0.3)
        self.play(Write(step1))
        
        step2 = Text("Sum = (2m+1) + (2n+1) = 2m + 2n + 2", font_size=22)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        
        step3 = Text("= 2(m + n + 1)", font_size=22)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        
        step4 = Text("Since m+n+1 is an integer, sum is even.", font_size=22, color=GREEN)
        step4.next_to(step3, DOWN, buff=0.3)
        self.play(Write(step4))
        
        self.wait(2)


class ContradictionProof(Scene):
    def construct(self):
        title = Text("Proof by Contradiction", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        concept = Text("Assume the opposite, derive a contradiction", font_size=24)
        concept.next_to(title, DOWN, buff=0.5)
        self.play(Write(concept))
        self.wait(0.5)
        
        # Example: sqrt(2) irrational
        ex_title = Text("Example: sqrt(2) is irrational", font_size=24, color=YELLOW)
        ex_title.next_to(concept, DOWN, buff=0.5)
        self.play(Write(ex_title))
        
        step1 = Text("Assume sqrt(2) = p/q in lowest terms", font_size=22)
        step1.next_to(ex_title, DOWN, buff=0.3)
        self.play(Write(step1))
        
        step2 = Text("Then 2 = p^2/q^2 => p^2 = 2q^2", font_size=22)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        
        step3 = Text("So p^2 is even => p is even => p = 2k", font_size=22)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        
        step4 = Text("Then q^2 = 2k^2 => q is also even", font_size=22)
        step4.next_to(step3, DOWN, buff=0.3)
        self.play(Write(step4))
        
        step5 = Text("Contradiction: p and q both even!", font_size=22, color=RED)
        step5.next_to(step4, DOWN, buff=0.3)
        self.play(Write(step5))
        
        step6 = Text("Therefore sqrt(2) is irrational.", font_size=22, color=GREEN)
        step6.next_to(step5, DOWN, buff=0.3)
        self.play(Write(step6))
        
        self.wait(2)
