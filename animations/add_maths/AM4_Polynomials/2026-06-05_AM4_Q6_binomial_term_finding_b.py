from manim import *
import math

class ConstantTerm(Scene):
    def construct(self):
        title = Text("Finding the Constant Term", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        ex = Text("Find constant term in (x+2/x)^6", font_size=26, color=YELLOW)
        ex.shift(UP*0.5)
        self.play(Write(ex))
        
        gen = Text("T_{r+1} = C(6,r) x^{6-r} (2/x)^r", font_size=22)
        gen.next_to(ex, DOWN)
        self.play(Write(gen))
        
        pow = Text("Power of x: 6-r-r = 6-2r = 0 => r=3", font_size=24)
        pow.next_to(gen, DOWN)
        self.play(Write(pow))
        
        term = Text("Constant = C(6,3) x 2^3 = 20 x 8 = 160", font_size=26, color=GREEN)
        term.next_to(pow, DOWN)
        self.play(Write(term))
        
        tip = Text("Set x-power to zero to find r", font_size=24, color=BLUE)
        tip.to_edge(DOWN)
        self.play(Write(tip))
        self.wait(2)
