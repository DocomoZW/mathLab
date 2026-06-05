from manim import *
import math

class GraphTransform(Scene):
    def construct(self):
        title = Text("Graph Transformations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("y = 3 sin(2x) + 1", font_size=28, color=YELLOW)
        ex.shift(UP*1)
        self.play(Write(ex))
        
        a = Text("Amplitude = 3 (stretch by 3)", font_size=24)
        a.next_to(ex, DOWN)
        self.play(Write(a))
        
        b = Text("Period = 2pi/2 = pi (compress)", font_size=24)
        b.next_to(a, DOWN)
        self.play(Write(b))
        
        d = Text("Vertical shift = +1 (centre at y=1)", font_size=24)
        d.next_to(b, DOWN)
        self.play(Write(d))
        
        range_t = Text("Range: from -2 to 4", font_size=24, color=GREEN)
        range_t.next_to(d, DOWN)
        self.play(Write(range_t))
        
        self.wait(2)
