from manim import *
import math

class TrigGraphs(Scene):
    def construct(self):
        title = Text("Sine and Cosine Graphs", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        sin_info = Text("y = sin(x): Period 2*pi, Range [-1,1]", font_size=24, color=BLUE)
        sin_info.next_to(title, DOWN, buff=0.4)
        self.play(Write(sin_info))
        self.wait(0.5)
        
        cos_info = Text("y = cos(x): Period 2*pi, Range [-1,1]", font_size=24, color=GREEN)
        cos_info.next_to(sin_info, DOWN, buff=0.3)
        self.play(Write(cos_info))
        self.wait(0.5)
        
        tan_info = Text("y = tan(x): Period pi, Range all reals", font_size=24, color=YELLOW)
        tan_info.next_to(cos_info, DOWN, buff=0.3)
        self.play(Write(tan_info))
        self.wait(0.5)
        
        # Key values
        key_pts = Text("Key: (0,0), (pi/2,1), (pi,0), (3pi/2,-1), (2pi,0)", font_size=22)
        key_pts.next_to(tan_info, DOWN, buff=0.4)
        self.play(Write(key_pts))
        self.wait(1)
        
        trans = Text("y = a*sin(bx + c) + d", font_size=28, color=PURPLE)
        trans.next_to(key_pts, DOWN, buff=0.5)
        self.play(Write(trans))
        self.wait(0.5)
        
        amp = Text("Amplitude = |a|, Period = 2*pi/|b|", font_size=24)
        amp.next_to(trans, DOWN, buff=0.3)
        self.play(Write(amp))
        self.wait(0.5)
        
        shift = Text("Phase shift = -c/b, Vertical shift = d", font_size=24)
        shift.next_to(amp, DOWN, buff=0.3)
        self.play(Write(shift))
        self.wait(2)


class ExactValues(Scene):
    def construct(self):
        title = Text("Exact Trigonometric Values", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Table header
        header = Text("theta:   0    pi/6    pi/4    pi/3    pi/2", font_size=22)
        header.next_to(title, DOWN, buff=0.4)
        self.play(Write(header))
        self.wait(0.5)
        
        sin_row = Text("sin:    0     1/2   sqrt2/2  sqrt3/2   1", font_size=22, color=BLUE)
        sin_row.next_to(header, DOWN, buff=0.3)
        self.play(Write(sin_row))
        self.wait(0.5)
        
        cos_row = Text("cos:    1    sqrt3/2  sqrt2/2   1/2     0", font_size=22, color=GREEN)
        cos_row.next_to(sin_row, DOWN, buff=0.3)
        self.play(Write(cos_row))
        self.wait(0.5)
        
        tan_row = Text("tan:    0    1/sqrt3    1     sqrt3  undef", font_size=22, color=YELLOW)
        tan_row.next_to(cos_row, DOWN, buff=0.3)
        self.play(Write(tan_row))
        self.wait(0.5)
        
        tip = Text("Tip: sin increases 0 -> 1 as angle goes 0 -> pi/2", font_size=24, color=ORANGE)
        tip.next_to(tan_row, DOWN, buff=0.5)
        self.play(Write(tip))
        self.wait(0.5)
        
        tip2 = Text("cos decreases 1 -> 0 as angle goes 0 -> pi/2", font_size=24, color=ORANGE)
        tip2.next_to(tip, DOWN, buff=0.3)
        self.play(Write(tip2))
        self.wait(2)
