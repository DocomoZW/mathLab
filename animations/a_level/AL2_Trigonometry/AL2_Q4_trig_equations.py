from manim import *
import math

class CASTDiagram(Scene):
    def construct(self):
        title = Text("CAST Diagram - Solving Trig Equations", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        quad1 = Text("Q1: All positive (A)", font_size=24, color=GREEN)
        quad1.next_to(title, DOWN, buff=0.5).shift(LEFT*3)
        self.play(Write(quad1))
        self.wait(0.3)
        
        quad2 = Text("Q2: Sine positive (S)", font_size=24, color=BLUE)
        quad2.next_to(title, DOWN, buff=0.5).shift(RIGHT*3)
        self.play(Write(quad2))
        self.wait(0.3)
        
        quad3 = Text("Q3: Tangent positive (T)", font_size=24, color=YELLOW)
        quad3.next_to(quad1, DOWN, buff=0.5)
        self.play(Write(quad3))
        self.wait(0.3)
        
        quad4 = Text("Q4: Cosine positive (C)", font_size=24, color=ORANGE)
        quad4.next_to(quad2, DOWN, buff=0.5)
        self.play(Write(quad4))
        self.wait(0.5)
        
        # Example
        example = Text("Example: sin(x) = 1/2", font_size=26)
        example.next_to(quad4, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        pv = Text("Principal: x = 30 deg (pi/6 rad)", font_size=24)
        pv.next_to(example, DOWN, buff=0.3)
        self.play(Write(pv))
        self.wait(0.3)
        
        sv = Text("Second: x = 180 - 30 = 150 deg (5pi/6 rad)", font_size=24)
        sv.next_to(pv, DOWN, buff=0.3)
        self.play(Write(sv))
        self.wait(0.3)
        
        hint = Text("Always adjust range for (ax+b) arguments!", font_size=24, color=YELLOW)
        hint.next_to(sv, DOWN, buff=0.4)
        self.play(Write(hint))
        self.wait(2)


class QuadraticTrigEquations(Scene):
    def construct(self):
        title = Text("Quadratic Trig Equations", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        method = Text("Method: Substitute u = sin(x), cos(x), or tan(x)", font_size=26)
        method.next_to(title, DOWN, buff=0.5)
        self.play(Write(method))
        self.wait(0.5)
        
        step1 = Text("Step 1: Write equation in terms of u", font_size=24)
        step1.next_to(method, DOWN, buff=0.4)
        self.play(Write(step1))
        self.wait(0.3)
        
        step2 = Text("Step 2: Solve the quadratic: au^2 + bu + c = 0", font_size=24)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.3)
        
        step3 = Text("Step 3: Solve each trig equation: sin(x) = u", font_size=24)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(0.3)
        
        example = Text("Example: 2sin^2(x) - sin(x) - 1 = 0", font_size=24)
        example.next_to(step3, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        sol1 = Text("Let u = sin(x): 2u^2 - u - 1 = 0", font_size=22)
        sol1.next_to(example, DOWN, buff=0.3)
        self.play(Write(sol1))
        self.wait(0.3)
        
        sol2 = Text("(2u+1)(u-1) = 0 => u = 1 or u = -1/2", font_size=22)
        sol2.next_to(sol1, DOWN, buff=0.3)
        self.play(Write(sol2))
        self.wait(0.3)
        
        sol3 = Text("sin(x) = 1 => x = pi/2", font_size=22, color=GREEN)
        sol3.next_to(sol2, DOWN, buff=0.3)
        self.play(Write(sol3))
        self.wait(0.3)
        
        sol4 = Text("sin(x) = -1/2 => x = 7pi/6, 11pi/6", font_size=22, color=GREEN)
        sol4.next_to(sol3, DOWN, buff=0.3)
        self.play(Write(sol4))
        self.wait(2)
