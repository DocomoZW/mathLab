from manim import *
import math

class E1Q2SOHCAHTOA(Scene):
    def construct(self):
        # Right triangle
        triangle = Polygon(
            [-2, -1.5, 0], [2, -1.5, 0], [-2, 1.5, 0],
            color=WHITE
        )
        self.play(Create(triangle))
        
        # Right angle
        right_angle = Square(side_length=0.25).move_to([-2, -1.5, 0])
        right_angle.shift(UR * 0.25)
        self.play(Create(right_angle))
        
        # Theta angle marker
        theta_arc = Arc(radius=0.3, angle=math.atan2(3, 4), color=YELLOW)
        theta_arc.move_to([-2, -1.5, 0])
        theta_arc.shift(RIGHT * 0.5 * 0.3, UP * 0.6 * 0.3)
        self.play(Create(theta_arc))
        theta_label = Text("theta", font_size=20, color=YELLOW)
        theta_label.move_to([-1.2, -0.8, 0])
        self.play(Write(theta_label))
        
        # Side labels
        opp = Text("Opposite", font_size=20, color=BLUE)
        opp.move_to([-2.5, 0, 0])
        
        adj = Text("Adjacent", font_size=20, color=GREEN)
        adj.next_to(triangle, DOWN, buff=0.3)
        
        hyp = Text("Hypotenuse", font_size=20, color=RED)
        hyp.move_to([0.2, 0.5, 0])
        
        self.play(Write(opp), Write(adj), Write(hyp))
        
        self.wait(0.5)
        
        # SOH CAH TOA formulas
        soh = Text("sin theta = Opposite / Hypotenuse", font_size=20, color=BLUE)
        soh.to_edge(UP, buff=0.2)
        self.play(Write(soh))
        
        self.wait(0.5)
        
        cah = Text("cos theta = Adjacent / Hypotenuse", font_size=20, color=GREEN)
        cah.next_to(soh, DOWN, buff=0.15)
        self.play(Write(cah))
        
        self.wait(0.5)
        
        toa = Text("tan theta = Opposite / Adjacent", font_size=20, color=YELLOW)
        toa.next_to(cah, DOWN, buff=0.15)
        self.play(Write(toa))
        
        self.wait(2)
