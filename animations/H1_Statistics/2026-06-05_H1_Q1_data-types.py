from manim import *
import math

class H1Q1DataTypes(Scene):
    def construct(self):
        title = Text("Data Types Classification").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.3)

        # Qualitative vs Quantitative
        qual_box = Rectangle(width=3.0, height=1.0, color=BLUE)
        qual_label = Text("Qualitative", font_size=24)
        qual_label.move_to(qual_box.get_center())
        qual_group = VGroup(qual_box, qual_label)
        qual_group.move_to(LEFT * 3.5 + UP * 1.5)

        quant_box = Rectangle(width=3.5, height=1.0, color=GREEN)
        quant_label = Text("Quantitative", font_size=24)
        quant_label.move_to(quant_box.get_center())
        quant_group = VGroup(quant_box, quant_label)
        quant_group.move_to(RIGHT * 3.0 + UP * 1.5)

        self.play(Create(qual_box), Write(qual_label),
                  Create(quant_box), Write(quant_label))
        self.wait(0.5)

        # Qualitative examples
        qual_ex1 = Text("Colors, Gender, Brand", font_size=20, color=BLUE)
        qual_ex1.next_to(qual_group, DOWN, buff=0.3)
        self.play(Write(qual_ex1))
        self.wait(0.3)

        # Quantitative sub-types: Discrete vs Continuous
        disc_box = Rectangle(width=3.5, height=1.0, color=YELLOW)
        disc_label = Text("Discrete (count)", font_size=22)
        disc_label.move_to(disc_box.get_center())
        disc_group = VGroup(disc_box, disc_label)
        disc_group.move_to(LEFT * 2.5 + DOWN * 0.5)

        cont_box = Rectangle(width=3.5, height=1.0, color=PURPLE)
        cont_label = Text("Continuous (measure)", font_size=22)
        cont_label.move_to(cont_box.get_center())
        cont_group = VGroup(cont_box, cont_label)
        cont_group.move_to(RIGHT * 3.0 + DOWN * 0.5)

        arrow_disc = Arrow(quant_group.get_bottom(), disc_group.get_top(), buff=0.1, color=YELLOW)
        arrow_cont = Arrow(quant_group.get_bottom(), cont_group.get_top(), buff=0.1, color=PURPLE)

        self.play(Create(arrow_disc), Create(arrow_cont),
                  Create(disc_box), Write(disc_label),
                  Create(cont_box), Write(cont_label))
        self.wait(0.5)

        # Examples
        disc_ex = Text("No. of students, Shoe size", font_size=18, color=YELLOW)
        disc_ex.next_to(disc_group, DOWN, buff=0.2)
        cont_ex = Text("Height, Weight, Time", font_size=18, color=PURPLE)
        cont_ex.next_to(cont_group, DOWN, buff=0.2)
        self.play(Write(disc_ex), Write(cont_ex))
        self.wait(0.5)

        # Summary at bottom
        summary = Text("Data: Numbers with context", font_size=22, color=GRAY)
        summary.to_edge(DOWN)
        self.play(Write(summary))
        self.wait(2)
