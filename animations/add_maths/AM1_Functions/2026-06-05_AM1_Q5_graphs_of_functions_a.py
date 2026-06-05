from manim import *
import math

class GraphTrans(Scene):
    def construct(self):
        title = Text("Graph Transformations", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        items = [
            "y = f(x) + a     Shift UP by a",
            "y = f(x + a)    Shift LEFT by a",
            "y = a f(x)       Vertical stretch by a",
            "y = f(ax)        Horizontal compress by 1/a",
            "y = -f(x)        Reflect in x-axis",
            "y = f(-x)         Reflect in y-axis"
        ]
        
        texts = []
        for i, item in enumerate(items):
            t = Text(item, font_size=22, color=BLUE if i < 4 else ORANGE)
            t.shift(UP*2 - DOWN*i*0.6)
            texts.append(t)
        
        for t in texts:
            self.play(Write(t), run_time=0.4)
        
        self.wait(2)
