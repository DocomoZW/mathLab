from manim import *

class D1Q7CompositeSolid(Scene):
    def construct(self):
        title = Text("Composite Solid: Cylinder + Hemisphere", font_size=22).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Cylinder part
        cyl_top = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        cyl_bottom = Ellipse(width=3, height=1, color=BLUE, stroke_width=3)
        cyl_bottom.shift(DOWN * 2)
        cyl_left = Line(cyl_top.get_left(), cyl_bottom.get_left(), color=BLUE, stroke_width=3)
        cyl_right = Line(cyl_top.get_right(), cyl_bottom.get_right(), color=BLUE, stroke_width=3)

        cylinder = VGroup(cyl_top, cyl_bottom, cyl_left, cyl_right)
        cylinder.move_to(ORIGIN)
        self.play(Create(cylinder))
        self.wait(0.3)

        # Hemisphere on top
        hemi_top = ArcBetweenPoints(
            cyl_top.get_left(), cyl_top.get_right(), angle=PI, color=ORANGE, stroke_width=3
        )
        # Also need to fill the hemisphere
        hemi_fill = Polygon(
            cyl_top.get_left(), cyl_top.get_right(),
            cyl_top.get_center() + UP * 1.5,
            color=ORANGE, fill_opacity=0.2, stroke_width=0
        )
        self.play(Create(hemi_top), FadeIn(hemi_fill))
        self.wait(0.3)

        # Labels
        r_label = Text("r = 3 cm", font_size=18, color=YELLOW).shift(UP * 1.2 + RIGHT * 0.8)
        h_label = Text("h = 8 cm", font_size=18, color=GREEN).shift(RIGHT * 2)
        self.play(Write(r_label), Write(h_label))
        self.wait(0.3)

        # Formulas
        f1 = Text("V_cyl = pi x r2 x h", font_size=18, color=BLUE).shift(DOWN * 1.5)
        f2 = Text("V_hemi = (2/3) x pi x r3", font_size=18, color=ORANGE).shift(DOWN * 2.2)
        self.play(Write(f1), Write(f2))
        self.wait(0.3)

        result = Text("Total = 226.22 + 56.56 = 282.78 cm3", font_size=18, color=YELLOW).to_edge(DOWN)
        self.play(Write(result))
        self.wait(1)
