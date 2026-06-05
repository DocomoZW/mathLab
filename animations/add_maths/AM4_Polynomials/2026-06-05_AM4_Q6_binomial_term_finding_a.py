from manim import *
import math

class BinomialTerm(Scene):
    def construct(self):
        title = Text("Finding a Specific Term", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        general = Text("General term: C(n,r) a^{n-r} b^r", font_size=26, color=YELLOW)
        general.shift(UP*1)
        self.play(Write(general))
        
        ex = Text("Find coeff of x^6 in (2x^2+3)^7", font_size=26)
        ex.next_to(general, DOWN)
        self.play(Write(ex))
        
        gterm = Text("T_{r+1} = C(7,r)(2x^2)^{7-r}(3)^r", font_size=24)
        gterm.next_to(ex, DOWN)
        self.play(Write(gterm))
        
        power = Text("Power: 2(7-r) = 6 => 14-2r=6 => r=4", font_size=24)
        power.next_to(gterm, DOWN)
        self.play(Write(power))
        
        coeff = Text("Coeff = C(7,4) x 2^3 x 3^4 = 22680", font_size=26, color=GREEN)
        coeff.next_to(power, DOWN)
        self.play(Write(coeff))
        
        self.wait(2)
