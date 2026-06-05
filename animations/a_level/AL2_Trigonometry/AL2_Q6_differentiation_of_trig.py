from manim import *
import math

class DerivativeTrigRules(Scene):
    def construct(self):
        title = Text("Differentiating Trig Functions", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        warn = Text("IMPORTANT: x must be in RADIANS!", font_size=26, color=RED)
        warn.next_to(title, DOWN, buff=0.4)
        self.play(Write(warn))
        self.wait(0.5)
        
        d_sin = Text("d/dx [sin(x)] = cos(x)", font_size=28, color=BLUE)
        d_sin.next_to(warn, DOWN, buff=0.4)
        self.play(Write(d_sin))
        self.wait(0.5)
        
        d_cos = Text("d/dx [cos(x)] = -sin(x)", font_size=28, color=GREEN)
        d_cos.next_to(d_sin, DOWN, buff=0.3)
        self.play(Write(d_cos))
        self.wait(0.5)
        
        d_sin_ax = Text("d/dx [sin(ax+b)] = a*cos(ax+b)", font_size=26, color=BLUE)
        d_sin_ax.next_to(d_cos, DOWN, buff=0.3)
        self.play(Write(d_sin_ax))
        self.wait(0.5)
        
        d_cos_ax = Text("d/dx [cos(ax+b)] = -a*sin(ax+b)", font_size=26, color=GREEN)
        d_cos_ax.next_to(d_sin_ax, DOWN, buff=0.3)
        self.play(Write(d_cos_ax))
        self.wait(0.5)
        
        # Product example
        prod = Text("Product rule: d/dx[x*sin(x)] = sin(x) + x*cos(x)", font_size=24)
        prod.next_to(d_cos_ax, DOWN, buff=0.5)
        self.play(Write(prod))
        self.wait(0.5)
        
        # Tangent
        grad = Text("Gradient of tangent = f'(x) at the point", font_size=24, color=YELLOW)
        grad.next_to(prod, DOWN, buff=0.4)
        self.play(Write(grad))
        self.wait(0.5)
        
        sp = Text("Stationary points: set f'(x) = 0", font_size=24, color=YELLOW)
        sp.next_to(grad, DOWN, buff=0.3)
        self.play(Write(sp))
        self.wait(2)


class TangentToTrigCurve(Scene):
    def construct(self):
        title = Text("Finding Tangents to Trig Curves", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        method_title = Text("Method:", font_size=28)
        method_title.next_to(title, DOWN, buff=0.4)
        self.play(Write(method_title))
        self.wait(0.3)
        
        step1 = Text("1. Find y-coordinate: f(a)", font_size=24)
        step1.next_to(method_title, DOWN, buff=0.3)
        self.play(Write(step1))
        self.wait(0.3)
        
        step2 = Text("2. Find gradient: f'(a)", font_size=24)
        step2.next_to(step1, DOWN, buff=0.3)
        self.play(Write(step2))
        self.wait(0.3)
        
        step3 = Text("3. Use: y - f(a) = f'(a)(x - a)", font_size=24)
        step3.next_to(step2, DOWN, buff=0.3)
        self.play(Write(step3))
        self.wait(0.3)
        
        step4 = Text("4. Normal gradient = -1/f'(a)", font_size=24)
        step4.next_to(step3, DOWN, buff=0.3)
        self.play(Write(step4))
        self.wait(0.5)
        
        example = Text("Example: y = 3sin(2x - pi/3) at x = pi/2", font_size=22)
        example.next_to(step4, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        sol1 = Text("y = 3sin(2pi/3) = 3*sqrt(3)/2", font_size=22, color=GREEN)
        sol1.next_to(example, DOWN, buff=0.3)
        self.play(Write(sol1))
        self.wait(0.3)
        
        sol2 = Text("dy/dx = 6cos(2x - pi/3), at pi/2: 6cos(2pi/3) = -3", font_size=22, color=GREEN)
        sol2.next_to(sol1, DOWN, buff=0.3)
        self.play(Write(sol2))
        self.wait(0.3)
        
        sol3 = Text("Tangent: y = -3x + 3pi/2 + 3*sqrt(3)/2", font_size=22, color=GREEN)
        sol3.next_to(sol2, DOWN, buff=0.3)
        self.play(Write(sol3))
        self.wait(2)
