from manim import *
import math

class TrigRatios(Scene):
    def construct(self):
        title = Text("Trigonometric Ratios", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        soh = Text("SOH: sin = Opposite / Hypotenuse", font_size=26, color=YELLOW)
        soh.shift(UP*1.5)
        self.play(Write(soh))
        
        cah = Text("CAH: cos = Adjacent / Hypotenuse", font_size=26, color=YELLOW)
        cah.next_to(soh, DOWN)
        self.play(Write(cah))
        
        toa = Text("TOA: tan = Opposite / Adjacent", font_size=26, color=YELLOW)
        toa.next_to(cah, DOWN)
        self.play(Write(toa))
        
        exact = Text("Exact: sin30=1/2, cos45=1/sqrt2, tan60=sqrt3", font_size=24, color=GREEN)
        exact.next_to(toa, DOWN)
        self.play(Write(exact))
        
        cast = Text("CAST diagram determines sign in each quadrant", font_size=22, color=BLUE)
        cast.to_edge(DOWN)
        self.play(Write(cast))
        self.wait(2)
