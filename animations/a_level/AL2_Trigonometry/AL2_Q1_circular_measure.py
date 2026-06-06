from manim import *
import math

class ArcLengthSector(Scene):
    def construct(self):
        title = Text("Arc Length and Sector Area", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Arc length formula
        formula1 = Text("Arc length: s = r * theta", font_size=28)
        formula1.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula1))
        self.wait(1)
        
        formula2 = Text("Sector area: A = 1/2 * r^2 * theta", font_size=28)
        formula2.next_to(formula1, DOWN, buff=0.3)
        self.play(Write(formula2))
        self.wait(1)
        
        note = Text("theta must be in radians", font_size=24, color=YELLOW)
        note.next_to(formula2, DOWN, buff=0.3)
        self.play(Write(note))
        self.wait(1)
        
        # Example
        example = Text("Example: r = 6 cm, theta = 1.2 rad", font_size=26)
        example.next_to(note, DOWN, buff=0.5)
        self.play(Write(example))
        self.wait(0.5)
        
        arc = Text("s = 6 * 1.2 = 7.2 cm", font_size=26, color=GREEN)
        arc.next_to(example, DOWN, buff=0.3)
        self.play(Write(arc))
        self.wait(0.5)
        
        area = Text("A = 1/2 * 36 * 1.2 = 21.6 cm^2", font_size=26, color=GREEN)
        area.next_to(arc, DOWN, buff=0.3)
        self.play(Write(area))
        self.wait(2)


class RadianConversion(Scene):
    def construct(self):
        title = Text("Converting Degrees and Radians", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        key = Text("360 deg = 2*pi rad", font_size=28, color=YELLOW)
        key.next_to(title, DOWN, buff=0.5)
        self.play(Write(key))
        self.wait(1)
        
        # Conversion factors
        d2r = Text("Deg to Rad: multiply by pi/180", font_size=26)
        d2r.next_to(key, DOWN, buff=0.5)
        self.play(Write(d2r))
        self.wait(0.5)
        
        r2d = Text("Rad to Deg: multiply by 180/pi", font_size=26)
        r2d.next_to(d2r, DOWN, buff=0.3)
        self.play(Write(r2d))
        self.wait(1)
        
        # Examples
        ex1 = Text("Example: 120 deg to rad", font_size=26)
        ex1.next_to(r2d, DOWN, buff=0.5)
        self.play(Write(ex1))
        self.wait(0.5)
        
        ans1 = Text("120 * pi/180 = 2*pi/3 rad", font_size=26, color=GREEN)
        ans1.next_to(ex1, DOWN, buff=0.3)
        self.play(Write(ans1))
        self.wait(0.5)
        
        ex2 = Text("Example: 5*pi/6 rad to deg", font_size=26)
        ex2.next_to(ans1, DOWN, buff=0.5)
        self.play(Write(ex2))
        self.wait(0.5)
        
        ans2 = Text("5*pi/6 * 180/pi = 150 deg", font_size=26, color=GREEN)
        ans2.next_to(ex2, DOWN, buff=0.3)
        self.play(Write(ans2))
        self.wait(2)
