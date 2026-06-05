from manim import *
import math

class H1Q3Pictogram(Scene):
    def construct(self):
        title = Text("Pictogram").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Key
        key_label = Text("Key:   = 2 items", font_size=20)
        key_circle = Circle(radius=0.2, color=YELLOW, fill_opacity=0.8)
        key_circle.shift(LEFT * 4 + UP * 2)
        key_label.next_to(key_circle, RIGHT, buff=0.1)
        key_group = VGroup(key_circle, key_label)
        self.play(Create(key_circle), Write(key_label))
        self.wait(0.3)

        # Pictogram rows
        categories = ["Apples", "Bananas", "Cherries", "Dates"]
        values = [6, 4, 5, 2]

        row_start_y = UP * 1.0
        row_spacing = 1.0
        icon_start_x = LEFT * 2.5

        for i, (cat, val) in enumerate(zip(categories, values)):
            y_pos = row_start_y + DOWN * row_spacing * i

            # Category label
            cat_text = Text(cat, font_size=18)
            cat_text.shift(LEFT * 4.5 + y_pos)
            self.play(Write(cat_text))

            # Icons (circles)
            num_icons = val // 2
            for j in range(num_icons):
                icon = Circle(radius=0.2, color=YELLOW, fill_opacity=0.8)
                icon.move_to(icon_start_x + RIGHT * 0.6 * j + y_pos)
                self.play(Create(icon), run_time=0.2)

            # Value label
            val_text = Text(str(val), font_size=16, color=GRAY)
            val_text.shift(RIGHT * 3.5 + y_pos)
            self.play(Write(val_text))

            self.wait(0.2)

        note = Text("Pictogram: uses symbols to represent data", font_size=20, color=GRAY)
        note.to_edge(DOWN)
        self.play(Write(note))
        self.wait(2)
