from manim import *
import math

class CompoundAngleFormulas(Scene):
    def construct(self):
        title = Text("Compound Angle Formulas", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        sin_ab = Text("sin(A +/- B) = sinA cosB +/- cosA sinB", font_size=24, color=BLUE)
        sin_ab.next_to(title, DOWN, buff=0.5)
        self.play(Write(sin_ab))
        self.wait(0.5)
        
        cos_ab = Text("cos(A +/- B) = cosA cosB -/+ sinA sinB", font_size=24, color=GREEN)
        cos_ab.next_to(sin_ab, DOWN, buff=0.3)
        self.play(Write(cos_ab))
        self.wait(0.5)
        
        tan_ab = Text("tan(A +/- B) = (tanA +/- tanB) / (1 -/+ tanA tanB)", font_size=22, color=YELLOW)
        tan_ab.next_to(cos_ab, DOWN, buff=0.3)
        self.play(Write(tan_ab))
        self.wait(0.5)
        
        # Double angle
        dbl_title = Text("Double Angle Formulas", font_size=30)
        dbl_title.next_to(tan_ab, DOWN, buff=0.5)
        self.play(Write(dbl_title))
        self.wait(0.5)
        
        sin2 = Text("sin(2A) = 2 sinA cosA", font_size=24, color=BLUE)
        sin2.next_to(dbl_title, DOWN, buff=0.3)
        self.play(Write(sin2))
        self.wait(0.3)
        
        cos2 = Text("cos(2A) = cos^2A - sin^2A = 2cos^2A - 1 = 1 - 2sin^2A", font_size=22, color=GREEN)
        cos2.next_to(sin2, DOWN, buff=0.3)
        self.play(Write(cos2))
        self.wait(0.3)
        
        tan2 = Text("tan(2A) = 2tanA / (1 - tan^2A)", font_size=24, color=YELLOW)
        tan2.next_to(cos2, DOWN, buff=0.3)
        self.play(Write(tan2))
        self.wait(2)


class RForm(Scene):
    def construct(self):
        title = Text("R cos(theta - alpha) Form", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        form = Text("a cos(theta) + b sin(theta) = R cos(theta - alpha)", font_size=24)
        form.next_to(title, DOWN, buff=0.5)
        self.play(Write(form))
        self.wait(0.5)
        
        r_formula = Text("R = sqrt(a^2 + b^2)", font_size=26, color=YELLOW)
        r_formula.next_to(form, DOWN, buff=0.3)
        self.play(Write(r_formula))
        self.wait(0.3)
        
        alpha_form = Text("alpha = tan^(-1)(b/a) [if a > 0]", font_size=26, color=YELLOW)
        alpha_form.next_to(r_formula, DOWN, buff=0.3)
        self.play(Write(alpha_form))
        self.wait(0.5)
        
        # Uses
        uses = Text("Applications:", font_size=26, color=PURPLE)
        uses.next_to(alpha_form, DOWN, buff=0.5)
        self.play(Write(uses))
        self.wait(0.3)
        
        u1 = Text("Maximum = R, Minimum = -R", font_size=24)
        u1.next_to(uses, DOWN, buff=0.3)
        self.play(Write(u1))
        self.wait(0.3)
        
        u2 = Text("Solve equations: cos(theta - alpha) = c/R", font_size=24)
        u2.next_to(u1, DOWN, buff=0.3)
        self.play(Write(u2))
        self.wait(0.3)
        
        u3 = Text("Sketch graphs quickly", font_size=24)
        u3.next_to(u2, DOWN, buff=0.3)
        self.play(Write(u3))
        self.wait(0.5)
        
        example = Text("Example: 3sin(t) + 4cos(t) = 5sin(t + 0.927)", font_size=22)
        example.next_to(u3, DOWN, buff=0.4)
        self.play(Write(example))
        self.wait(2)
