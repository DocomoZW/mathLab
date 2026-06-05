from manim import *
import math

class RadiansDegrees(Scene):
    def construct(self):
        title = Text("Radians and Degrees", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        conv = Text("pi radians = 180 degrees", font_size=28, color=YELLOW)
        conv.shift(UP*1)
        self.play(Write(conv))
        
        ex1 = Text("To convert deg to rad: multiply by pi/180", font_size=24)
        ex1.next_to(conv, DOWN)
        self.play(Write(ex1))
        
        ex2 = Text("120 deg = 120 x pi/180 = 2pi/3 rad", font_size=26, color=GREEN)
        ex2.next_to(ex1, DOWN)
        self.play(Write(ex2))
        
        ex3 = Text("5pi/4 rad = 5pi/4 x 180/pi = 225 deg", font_size=26, color=GREEN)
        ex3.next_to(ex2, DOWN)
        self.play(Write(ex3))
        
        common = Text("Common: pi/6=30, pi/4=45, pi/3=60, pi/2=90", font_size=24, color=BLUE)
        common.to_edge(DOWN)
        self.play(Write(common))
        self.wait(2)
