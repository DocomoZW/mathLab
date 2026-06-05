from manim import *

class C1Q3InteriorAngles(Scene):
    def construct(self):
        title = Text("Interior Angles of a Polygon", font_size=24).to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        subtitle = Text("Pentagon: n = 5", font_size=20, color=GREY)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))
        self.wait(0.3)

        # Build a pentagon vertex by vertex
        center = np.array([0, 0, 0])
        # Regular pentagon vertices (pointing up)
        n = 5
        radius = 2.2
        vertices = []
        for i in range(n):
            # Start from top and go clockwise
            angle = PI/2 - i * 2*PI/n
            x = center[0] + radius * np.cos(angle)
            y = center[1] + radius * np.sin(angle)
            vertices.append(np.array([x, y, 0]))

        # Draw pentagon edges one by one
        edges = []
        for i in range(n):
            start = vertices[i]
            end = vertices[(i+1) % n]
            edge = Line(start, end, color=BLUE, stroke_width=4)
            edges.append(edge)

        # Show vertices appearing and edges growing
        dots = VGroup(*[Dot(v, color=WHITE, radius=0.06) for v in vertices])

        # Animate building the pentagon
        for i, edge in enumerate(edges):
            if i == 0:
                self.play(Create(dots[i]))
                self.play(Create(edge))
            else:
                self.play(Create(dots[i]), Create(edge), run_time=0.5)
            self.wait(0.15)
        # Close the last edge
        self.wait(0.3)

        vertex_labels = VGroup()
        for i, v in enumerate(vertices):
            lbl = Text(chr(65+i), font_size=18, color=WHITE)  # A, B, C, D, E
            offset = (v - center) / np.linalg.norm(v - center) * 0.35
            lbl.move_to(v + offset)
            vertex_labels.add(lbl)

        self.play(Write(vertex_labels))
        self.wait(0.3)

        # Formula text: (n-2) x 180
        formula1 = Text("Formula: (n - 2) x 180 degrees", font_size=20, color=YELLOW)
        formula1.next_to(center, DOWN * 2.0)
        self.play(Write(formula1))
        self.wait(0.3)

        # For pentagon: (5-2) x 180 = 3 x 180 = 540
        formula2 = Text("For n = 5: (5 - 2) = 3 triangles", font_size=18, color=YELLOW)
        formula2.next_to(formula1, DOWN * 0.7)
        self.play(Write(formula2))
        self.wait(0.3)

        # Draw diagonals from vertex A (vertices[0]) to split into 3 triangles
        # Diagonal from A to C, A to D
        diag1 = Line(vertices[0], vertices[2], color=ORANGE, stroke_width=3, stroke_opacity=0.8)
        diag2 = Line(vertices[0], vertices[3], color=ORANGE, stroke_width=3, stroke_opacity=0.8)

        self.play(Create(diag1), Create(diag2))
        self.wait(0.4)

        # Highlight each triangle
        # Triangle 1: A-B-C (vertices[0], vertices[1], vertices[2])
        tri1 = Polygon(vertices[0], vertices[1], vertices[2],
                       color=RED, fill_color=RED, fill_opacity=0.15, stroke_width=2)
        # Triangle 2: A-C-D (vertices[0], vertices[2], vertices[3])
        tri2 = Polygon(vertices[0], vertices[2], vertices[3],
                       color=GREEN, fill_color=GREEN, fill_opacity=0.15, stroke_width=2)
        # Triangle 3: A-D-E (vertices[0], vertices[3], vertices[4])
        tri3 = Polygon(vertices[0], vertices[3], vertices[4],
                       color=BLUE, fill_color=BLUE, fill_opacity=0.15, stroke_width=2)

        # Show triangles one by one
        tri_label1 = Text("Triangle 1", font_size=16, color=RED)
        tri_label1.move_to(center + np.array([-1.2, 0.8, 0]))
        self.play(Create(tri1), Write(tri_label1))
        self.wait(0.3)

        tri_label2 = Text("Triangle 2", font_size=16, color=GREEN)
        tri_label2.move_to(center + np.array([0, 0, 0]))
        self.play(Create(tri2), Write(tri_label2))
        self.wait(0.3)

        tri_label3 = Text("Triangle 3", font_size=16, color=BLUE)
        tri_label3.move_to(center + np.array([1.2, 0.8, 0]))
        self.play(Create(tri3), Write(tri_label3))
        self.wait(0.3)

        # 3 triangles x 180 = 540 degrees
        result = Text("3 x 180 = 540 degrees  (Total interior angles)", font_size=20, color=YELLOW)
        result.next_to(formula2, DOWN * 0.7)
        self.play(Write(result))
        self.wait(1.5)

        self.play(*[FadeOut(m) for m in self.mobjects])
        self.wait(0.3)
