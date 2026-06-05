from manim import *
import math

class E1Q3Depression(Scene):
    def construct(self):
        # Ground line
        ground = Line([-3.5, -1.5, 0], [3.5, -1.5, 0], color=GRAY)
        self.play(Create(ground))
        
        # Cliff or building person is on top of
        cliff = Rectangle(width=0.5, height=2, color=GRAY)
        cliff.move_to([-1.5, 0.5, 0])
        cliff.shift(DOWN * 1.5)
        self.play(Create(cliff))
        
        # Person at top
        person_body = Line([-1.5, 1, 0], [-1.5, 1.75, 0], color=WHITE)
        person_head = Circle(radius=0.2, color=WHITE).move_to([-1.5, 2, 0])
        self.play(Create(person_body), Create(person_head))
        
        # Eye level horizontal line
        eye_level = DashedLine([-1.5, 2, 0], [2.5, 2, 0], color=YELLOW)
        self.play(Create(eye_level))
        
        self.wait(0.3)
        
        # Object below at ground level
        obj = Rectangle(width=0.4, height=0.6, color=GRAY)
        obj.move_to([2, -1.2, 0])
        self.play(Create(obj))
        
        # Line of sight downward
        sight_line = Line([-1.5, 2, 0], [2, -1.2, 0], color=GREEN)
        self.play(Create(sight_line))
        
        # Angle of depression arc (below horizontal)
        angle_arc = Arc(
            radius=0.5,
            angle=-math.atan2(3.2, 3.5),
            color=YELLOW
        )
        angle_arc.move_to([-1.5, 2, 0])
        self.play(Create(angle_arc))
        
        # Label
        angle_label = Text("Angle of", font_size=20, color=YELLOW)
        angle_label.move_to([-0.5, 1.5, 0])
        self.play(Write(angle_label))
        
        angle_label2 = Text("Depression", font_size=20, color=YELLOW)
        angle_label2.next_to(angle_label, DOWN, buff=0.1)
        self.play(Write(angle_label2))
        
        self.wait(0.5)
        
        # Labels
        observer_label = Text("Observer", font_size=20, color=WHITE)
        observer_label.next_to(person_head, UP, buff=0.1)
        self.play(Write(observer_label))
        
        obj_label = Text("Object", font_size=20, color=GRAY)
        obj_label.next_to(obj, DOWN, buff=0.1)
        self.play(Write(obj_label))
        
        self.wait(2)
