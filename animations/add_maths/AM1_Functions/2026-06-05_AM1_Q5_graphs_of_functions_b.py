from manim import *
import math

class SketchingQuad(Scene):
    def construct(self):
        title = Text("Steps to Sketch Quadratics", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        items = [
            "1. Find y-intercept (set x = 0)",
            "2. Find x-intercepts (solve f(x)=0)",
            "3. Find vertex by completing square",
            "4. Check shape: a>0 = U, a<0 = upside-down",
            "5. Plot key points and draw smoothly"
        ]
        
        for i, item in enumerate(items):
            t = Text(item, font_size=24)
            t.shift(UP*1.5 - DOWN*i*0.6)
            self.play(Write(t), run_time=0.5)
        
        self.wait(2)
