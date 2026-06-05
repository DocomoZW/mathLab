from manim import *
import math

class E1Q7AreaSinCExample(Scene):
    def construct(self):
        # Triangle with known values
        vertices = [
            [-2, -1.2, 0],
            [2, -1.2, 0],
            [0, 1.5, 0]
        ]
        triangle = Polygon(*vertices, color=WHITE)
        self.play(Create(triangle))
        
        # Known sides
        a_val = Text("8", font_size=24, color=BLUE)
        a_val.move_to([0.5, 0.2, 0])
        
        b_val = Text("6", font_size=24, color=GREEN)
        b_val.move_to([-0.5, 0.2, 0])
        
        self.play(Write(a_val), Write(b_val))
        
        # Known included angle
        angle_c_val = Text("30 deg", font_size=20, color=YELLOW)
        angle_c_val.move_to([0, 1.8, 0])
        
        angle_arc = Arc(
            radius=0.35,
            start_angle=math.atan2(1.2, 2),
            angle=PI - 2 * math.atan2(1.2, 2),
            color=YELLOW
        )
        angle_arc.move_to(vertices[2])
        self.play(Create(angle_arc), Write(angle_c_val))
        
        self.wait(0.5)
        
        # Formula step
        step1 = Text("Area = 0.5 x 8 x 6 x sin 30", font_size=22, color=YELLOW)
        step1.to_edge(UP)
        self.play(Write(step1))
        
        self.wait(0.5)
        
        step2 = Text("Area = 0.5 x 8 x 6 x 0.5", font_size=22, color=YELLOW)
        step2.next_to(step1, DOWN, buff=0.1)
        self.play(Write(step2))
        
        self.wait(0.5)
        
        step3 = Text("Area = 12", font_size=24, color=YELLOW)
        step3.next_to(step2, DOWN, buff=0.1)
        self.play(Write(step3))
        
        self.wait(0.5)
        
        # Show area inside triangle (fill)
        area_triangle = Polygon(*vertices, color=YELLOW, fill_opacity=0.3)
        self.play(FadeIn(area_triangle))
        
        # Result label
        result = Text("Area = 12 square units", font_size=22, color=YELLOW)
        result.to_edge(DOWN)
        self.play(Write(result))
        
        self.wait(2)
