from manim import *
import math

class RotateOrigin(Scene):
    def construct(self):
        x_axis = Line(LEFT*3.5, RIGHT*3.5, color=GRAY)
        y_axis = Line(DOWN*3.5, UP*3.5, color=GRAY)
        x_label = Text("x").scale(0.4).next_to(x_axis, RIGHT)
        y_label = Text("y").scale(0.4).next_to(y_axis, UP)
        origin = Dot(ORIGIN, color=WHITE, radius=0.08)
        o_label = Text("O").scale(0.3).next_to(origin, DOWN+LEFT)
        self.play(Create(x_axis), Create(y_axis), Write(x_label), Write(y_label), FadeIn(origin), Write(o_label))
        self.wait(0.2)

        tri_pts = [RIGHT*1.0+DOWN*0.5, RIGHT*2.0+DOWN*0.5, RIGHT*1.0+UP*0.5]
        tri = Polygon(*tri_pts, color=BLUE, fill_opacity=0.3)
        tri_label = Text("Original").scale(0.2).next_to(tri, DOWN+RIGHT)
        self.play(Create(tri), Write(tri_label))
        self.wait(0.4)

        angle = math.pi/2
        pts_90 = []
        for p in tri_pts:
            xr = p[0]*math.cos(angle) - p[1]*math.sin(angle)
            yr = p[0]*math.sin(angle) + p[1]*math.cos(angle)
            pts_90.append(np.array([xr, yr, 0]))
        tri_90 = Polygon(*pts_90, color=GREEN, fill_opacity=0.3)
        label_90 = Text("90 deg").scale(0.2).next_to(tri_90, UP+LEFT)
        self.play(Create(tri_90), Write(label_90))
        self.wait(0.4)

        angle = math.pi
        pts_180 = []
        for p in tri_pts:
            xr = p[0]*math.cos(angle) - p[1]*math.sin(angle)
            yr = p[0]*math.sin(angle) + p[1]*math.cos(angle)
            pts_180.append(np.array([xr, yr, 0]))
        tri_180 = Polygon(*pts_180, color=RED, fill_opacity=0.3)
        label_180 = Text("180 deg").scale(0.2).next_to(tri_180, DOWN+LEFT)
        self.play(Create(tri_180), Write(label_180))
        self.wait(0.4)

        info = Text("Rotation about origin preserves distance from O", color=WHITE).scale(0.3).to_edge(DOWN)
        self.play(Write(info))
        self.wait(1.0)
