from manim import *
import math

class SectorPerimeter(Scene):
    def construct(self):
        title = Text("Sector Perimeter", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        form = Text("Perimeter = 2r + r*theta", font_size=28, color=YELLOW)
        form.shift(UP*1)
        self.play(Write(form))
        
        ex = Text("For r=4, theta=pi/2:", font_size=26)
        ex.next_to(form, DOWN)
        self.play(Write(ex))
        
        calc = Text("P = 2(4) + 4(pi/2) = 8 + 2pi", font_size=26)
        calc.next_to(ex, DOWN)
        self.play(Write(calc))
        
        result = Text("= 8 + 2(3.14) = 14.28 cm", font_size=26, color=GREEN)
        result.next_to(calc, DOWN)
        self.play(Write(result))
        
        note = Text("Two straight edges + one curved edge", font_size=24, color=BLUE)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
