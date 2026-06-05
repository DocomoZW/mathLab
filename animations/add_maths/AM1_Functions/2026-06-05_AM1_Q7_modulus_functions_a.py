from manim import *
import math

class ModDef(Scene):
    def construct(self):
        title = Text("Modulus Function", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        def1 = Text("|x| = x   when x >= 0", font_size=28, color=BLUE)
        def1.shift(UP*1.5)
        def2 = Text("|x| = -x  when x < 0", font_size=28, color=GREEN)
        def2.next_to(def1, DOWN, buff=0.3)
        
        self.play(Write(def1), Write(def2))
        
        props = [
            "|x| >= 0 for all x",
            "|x| = |-x|",
            "|ab| = |a||b|",
            "|x| = a  =>  x = a or x = -a"
        ]
        
        for i, p in enumerate(props):
            t = Text(p, font_size=22, color=ORANGE)
            t.shift(DOWN*0.5 - DOWN*i*0.5)
            self.play(Write(t), run_time=0.4)
        
        self.wait(2)
