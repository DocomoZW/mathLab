from manim import *
import math

class PartialFracIntro(Scene):
    def construct(self):
        title = Text("Partial Fractions", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show the concept
        concept = Text("Split a single fraction into simpler parts", font_size=24)
        concept.next_to(title, DOWN, buff=0.5)
        self.play(Write(concept))
        self.wait(0.5)
        
        # Example
        example = Text("(5x+1) / ((x+2)(x-1))", font_size=26)
        example.next_to(concept, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        arrow = Text("--- decomposes to --->", font_size=20, color=YELLOW)
        arrow.next_to(example, DOWN, buff=0.3)
        self.play(Write(arrow))
        self.wait(0.5)
        
        result = Text("3/(x+2) + 2/(x-1)", font_size=26, color=GREEN)
        result.next_to(arrow, DOWN, buff=0.3)
        self.play(Write(result))
        self.wait(1)
        
        # Cases
        cases_title = Text("Three Cases:", font_size=22, color=YELLOW)
        cases_title.next_to(result, DOWN, buff=0.5)
        self.play(Write(cases_title))
        
        cases = [
            Text("1. Distinct linear factors: A/(ax+b) + B/(cx+d)", font_size=20),
            Text("2. Repeated factor: A/(ax+b) + B/(ax+b)^2", font_size=20),
            Text("3. Quadratic factor: A/(ax+b) + (Bx+C)/(x^2+c^2)", font_size=20)
        ]
        
        for i, case in enumerate(cases):
            case.next_to(cases_title, DOWN, buff=0.3 + i * 0.35)
            self.play(Write(case), run_time=0.3)
        
        self.wait(2)


class FactorisationMethod(Scene):
    def construct(self):
        title = Text("Partial Fractions Method", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Steps
        steps = [
            "Step 1: Check if fraction is proper",
            "Step 2: Factorise denominator",
            "Step 3: Write the decomposition form",
            "Step 4: Multiply through by denominator",
            "Step 5: Substitute x values or equate coefficients",
            "Step 6: Write final answer"
        ]
        
        step_objects = []
        for i, step_text in enumerate(steps):
            t = Text(step_text, font_size=22)
            t.next_to(title, DOWN, buff=0.3 + i * 0.4)
            step_objects.append(t)
            if i < 2:
                self.play(Write(t), run_time=0.3)
            else:
                self.play(Write(t), run_time=0.3)
            self.wait(0.2)
        
        self.wait(1)
        
        # Example quick demo
        demo_title = Text("Example:", font_size=22, color=YELLOW)
        demo_title.next_to(step_objects[-1], DOWN, buff=0.3)
        self.play(Write(demo_title))
        
        ex = Text("4/((x-1)(x+3)) = 1/(x-1) - 1/(x+3)", font_size=22, color=GREEN)
        ex.next_to(demo_title, DOWN, buff=0.3)
        self.play(Write(ex))
        self.wait(2)
