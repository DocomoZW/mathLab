from manim import *
import math

class IntegrationTrigRules(Scene):
    def construct(self):
        title = Text("Integrating Trig Functions", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        int_sin = Text("Integral of sin(x) dx = -cos(x) + C", font_size=28, color=BLUE)
        int_sin.next_to(title, DOWN, buff=0.5)
        self.play(Write(int_sin))
        self.wait(0.5)
        
        int_cos = Text("Integral of cos(x) dx = sin(x) + C", font_size=28, color=GREEN)
        int_cos.next_to(int_sin, DOWN, buff=0.3)
        self.play(Write(int_cos))
        self.wait(0.5)
        
        int_sin_ax = Text("Integral of sin(ax+b) dx = -1/a * cos(ax+b) + C", font_size=24, color=BLUE)
        int_sin_ax.next_to(int_cos, DOWN, buff=0.3)
        self.play(Write(int_sin_ax))
        self.wait(0.5)
        
        int_cos_ax = Text("Integral of cos(ax+b) dx = 1/a * sin(ax+b) + C", font_size=24, color=GREEN)
        int_cos_ax.next_to(int_sin_ax, DOWN, buff=0.3)
        self.play(Write(int_cos_ax))
        self.wait(0.5)
        
        warn = Text("Check by differentiating your answer!", font_size=24, color=YELLOW)
        warn.next_to(int_cos_ax, DOWN, buff=0.4)
        self.play(Write(warn))
        self.wait(0.5)
        
        # Area
        def_int = Text("Definite integral = area under curve", font_size=26)
        def_int.next_to(warn, DOWN, buff=0.4)
        self.play(Write(def_int))
        self.wait(0.5)
        
        area = Text("Area = integral from a to b of f(x) dx", font_size=24)
        area.next_to(def_int, DOWN, buff=0.3)
        self.play(Write(area))
        self.wait(2)


class IntegratePowersTrig(Scene):
    def construct(self):
        title = Text("Integrating sin^2 and cos^2", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        hint = Text("Use double angle formulas to rewrite:", font_size=26)
        hint.next_to(title, DOWN, buff=0.4)
        self.play(Write(hint))
        self.wait(0.5)
        
        sin2_form = Text("sin^2(x) = [1 - cos(2x)] / 2", font_size=28, color=BLUE)
        sin2_form.next_to(hint, DOWN, buff=0.4)
        self.play(Write(sin2_form))
        self.wait(0.5)
        
        cos2_form = Text("cos^2(x) = [1 + cos(2x)] / 2", font_size=28, color=GREEN)
        cos2_form.next_to(sin2_form, DOWN, buff=0.3)
        self.play(Write(cos2_form))
        self.wait(1)
        
        int_sin2 = Text("Integral sin^2(x) dx = x/2 - sin(2x)/4 + C", font_size=24, color=BLUE)
        int_sin2.next_to(cos2_form, DOWN, buff=0.5)
        self.play(Write(int_sin2))
        self.wait(0.5)
        
        int_cos2 = Text("Integral cos^2(x) dx = x/2 + sin(2x)/4 + C", font_size=24, color=GREEN)
        int_cos2.next_to(int_sin2, DOWN, buff=0.3)
        self.play(Write(int_cos2))
        self.wait(1)
        
        example = Text("Example: Area from 0 to pi of cos^2(x) dx = pi/2", font_size=24, color=YELLOW)
        example.next_to(int_cos2, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        check = Text("Check: d/dx[x/2 + sin(2x)/4] = 1/2 + cos(2x)/2 = [1+cos(2x)]/2 = cos^2(x)", font_size=20)
        check.next_to(example, DOWN, buff=0.3)
        self.play(Write(check))
        self.wait(2)
