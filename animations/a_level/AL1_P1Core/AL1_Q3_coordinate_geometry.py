from manim import *
import math

class CircleEquation(Scene):
    def construct(self):
        title = Text("Equation of a Circle", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Show standard form
        std = Text("(x - a)^2 + (y - b)^2 = r^2", font_size=28)
        std.next_to(title, DOWN, buff=0.5)
        self.play(Write(std))
        self.wait(0.5)
        
        center_label = Text("Centre: (a, b),  Radius: r", font_size=26)
        center_label.next_to(std, DOWN, buff=0.3)
        self.play(Write(center_label))
        self.wait(1)
        
        # Draw a circle
        circle = Circle(radius=2, color=BLUE)
        circle.next_to(center_label, DOWN, buff=0.8)
        self.play(Create(circle))
        self.wait(0.5)
        
        # Centre point
        centre = Dot(color=YELLOW)
        centre.move_to(circle.get_center())
        self.play(Create(centre))
        
        # Centre label
        cl = Text("C(a,b)", font_size=20, color=YELLOW)
        cl.next_to(centre, UP + LEFT, buff=0.1)
        self.play(Write(cl))
        
        # Radius line
        r_point = circle.point_at_angle(0)
        radius_line = Line(centre.get_center(), r_point, color=RED)
        self.play(Create(radius_line))
        
        r_label = Text("r", font_size=20, color=RED)
        r_label.move_to(centre.get_center() + (r_point - centre.get_center()) / 2 + UP * 0.3)
        self.play(Write(r_label))
        self.wait(2)
        
        # Expanded form
        expanded = Text("x^2 + y^2 + 2gx + 2fy + c = 0", font_size=26)
        expanded.next_to(circle, DOWN, buff=0.5)
        self.play(Write(expanded))
        self.wait(0.5)
        
        expanded_c = Text("Centre: (-g, -f),  r = sqrt(g^2 + f^2 - c)", font_size=22)
        expanded_c.next_to(expanded, DOWN, buff=0.3)
        self.play(Write(expanded_c))
        self.wait(2)


class TangentCircle(Scene):
    def construct(self):
        title = Text("Tangent to a Circle", font_size=36)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))
        
        # Draw circle
        circle = Circle(radius=2.5, color=BLUE)
        circle.next_to(title, DOWN, buff=0.5)
        self.play(Create(circle))
        
        # Centre
        centre = Dot(color=YELLOW)
        centre.move_to(circle.get_center())
        self.play(Create(centre))
        
        # Point on circle
        angle = -PI / 3
        p_on_circle = circle.point_at_angle(angle)
        point = Dot(p_on_circle, color=GREEN)
        self.play(Create(point))
        
        # Radius to point
        radius = Line(centre.get_center(), p_on_circle, color=RED)
        self.play(Create(radius))
        
        # Tangent line
        radius_dir = (p_on_circle - centre.get_center()) / 2.5
        tangent_dir = np.array([-radius_dir[1], radius_dir[0], 0])
        tangent = Line(
            p_on_circle + tangent_dir * 2.5,
            p_on_circle - tangent_dir * 2.5,
            color=GREEN
        )
        self.play(Create(tangent))
        self.wait(0.5)
        
        # Right angle marker
        perp = Square(side_length=0.2, color=WHITE)
        perp.move_to(p_on_circle + radius_dir * 0.15 + tangent_dir * 0.15)
        self.play(Create(perp))
        
        # Labels
        r_label = Text("radius", font_size=18, color=RED)
        r_label.next_to(radius.get_center(), UP + LEFT, buff=0.1)
        self.play(Write(r_label))
        
        t_label = Text("tangent", font_size=18, color=GREEN)
        t_label.next_to(tangent.get_center(), DOWN + RIGHT, buff=0.1)
        self.play(Write(t_label))
        
        rule = Text("m(radius) x m(tangent) = -1", font_size=22, color=YELLOW)
        rule.next_to(circle, DOWN, buff=0.5)
        self.play(Write(rule))
        self.wait(2)
