from manim import *
import math

class CommonAngles(Scene):
    def construct(self):
        title = Text("Common Angles in Radians", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        angles = [
            "0 deg = 0 rad",
            "30 deg = pi/6 rad",
            "45 deg = pi/4 rad",
            "60 deg = pi/3 rad",
            "90 deg = pi/2 rad",
            "180 deg = pi rad",
            "270 deg = 3pi/2 rad",
            "360 deg = 2pi rad"
        ]
        texts = []
        for i, ang in enumerate(angles):
            t = Text(ang, font_size=22, color=YELLOW if i%2==0 else BLUE)
            t.shift(UP*3 - i*0.55*DOWN + RIGHT*1)
            texts.append(t)
        
        for t in texts:
            self.play(Write(t), run_time=0.2)
        
        note = Text("Learn these conversions!", font_size=24, color=GREEN)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
