from manim import *
import math

class PythagoreanIdentity(Scene):
    def construct(self):
        title = Text("Pythagorean Identity", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        ident = Text("sin^2(theta) + cos^2(theta) = 1", font_size=30, color=YELLOW)
        ident.next_to(title, DOWN, buff=0.5)
        self.play(Write(ident))
        self.wait(1)
        
        unit_circle = Text("From the unit circle: x^2 + y^2 = 1", font_size=26)
        unit_circle.next_to(ident, DOWN, buff=0.4)
        self.play(Write(unit_circle))
        self.wait(0.5)
        
        point = Text("Point P = (cos(theta), sin(theta))", font_size=26)
        point.next_to(unit_circle, DOWN, buff=0.3)
        self.play(Write(point))
        self.wait(0.5)
        
        deriv = Text("cos^2(theta) + sin^2(theta) = 1", font_size=26, color=GREEN)
        deriv.next_to(point, DOWN, buff=0.3)
        self.play(Write(deriv))
        self.wait(1)
        
        # Tangent identity
        t_ident = Text("tan(theta) = sin(theta)/cos(theta)", font_size=30, color=BLUE)
        t_ident.next_to(deriv, DOWN, buff=0.5)
        self.play(Write(t_ident))
        self.wait(1)
        
        proof_hint = Text("Prove LHS = RHS by starting from one side only", font_size=24, color=ORANGE)
        proof_hint.next_to(t_ident, DOWN, buff=0.4)
        self.play(Write(proof_hint))
        self.wait(2)


class TrigIdentityProof(Scene):
    def construct(self):
        title = Text("Proving Trig Identities", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        step1 = Text("1. Start with the harder side", font_size=26)
        step1.next_to(title, DOWN, buff=0.5)
        self.play(Write(step1))
        self.wait(0.5)
        
        step2 = Text("2. Replace trig functions using identities", font_size=26)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.5)
        
        step3 = Text("3. Combine fractions, factor, simplify", font_size=26)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(0.5)
        
        step4 = Text("4. Aim to match the other side exactly", font_size=26)
        step4.next_to(step3, DOWN, buff=0.3)
        self.play(Write(step4))
        self.wait(0.5)
        
        warn = Text("NEVER cross-multiply or move terms between sides!", font_size=24, color=RED)
        warn.next_to(step4, DOWN, buff=0.5)
        self.play(Write(warn))
        self.wait(0.5)
        
        example = Text("Example: Prove cos^2(t)(tan^2(t)+1) = 1", font_size=24)
        example.next_to(warn, DOWN, buff=0.4)
        self.play(Write(example))
        self.wait(0.5)
        
        sol = Text("= cos^2(t)(sin^2/cos^2 + 1) = sin^2+cos^2 = 1", font_size=22, color=GREEN)
        sol.next_to(example, DOWN, buff=0.3)
        self.play(Write(sol))
        self.wait(2)
