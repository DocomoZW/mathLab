from manim import *
import math

class E1Q3Elevation(Scene):
    def construct(self):
        # Ground line
        ground = Line([-3.5, -1.5, 0], [3.5, -1.5, 0], color=GRAY)
        self.play(Create(ground))
        
        # Tall object (building/tree)
        building = Rectangle(width=0.5, height=2.5, color=GRAY)
        building.move_to([2, 0.25, 0])
        building.shift(DOWN * 1.25)
        self.play(Create(building))
        
        # Person (simple stick figure)
        person_body = Line([-1.5, -1.5, 0], [-1.5, -0.25, 0], color=WHITE)
        person_head = Circle(radius=0.2, color=WHITE).move_to([-1.5, 0, 0])
        self.play(Create(person_body), Create(person_head))
        
        # Eye level line
        eye_level = DashedLine([-1.5, 0, 0], [1.5, 0, 0], color=YELLOW)
        self.play(Create(eye_level))
        
        self.wait(0.3)
        
        # Line of sight to top of building
        sight_line = Line([-1.5, 0, 0], [2, 1.25, 0], color=GREEN)
        self.play(Create(sight_line))
        
        # Angle of elevation arc
        angle_arc = Arc(
            radius=0.5,
            angle=math.atan2(1.25, 3.5),
            color=YELLOW
        )
        angle_arc.move_to([-1.5, 0, 0])
        self.play(Create(angle_arc))
        
        # Label
        angle_label = Text("Angle of", font_size=20, color=YELLOW)
        angle_label.move_to([-0.8, 0.3, 0])
        self.play(Write(angle_label))
        
        angle_label2 = Text("Elevation", font_size=20, color=YELLOW)
        angle_label2.next_to(angle_label, DOWN, buff=0.1)
        self.play(Write(angle_label2))
        
        self.wait(0.5)
        
        # Labels
        obj_label = Text("Object", font_size=20, color=GRAY)
        obj_label.next_to(building, UP, buff=0.1)
        self.play(Write(obj_label))
        
        person_label = Text("Observer", font_size=20, color=WHITE)
        person_label.next_to(person_head, LEFT, buff=0.2)
        self.play(Write(person_label))
        
        self.wait(2)
