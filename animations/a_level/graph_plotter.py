# Manim script for graph plotting
from manim import *
class GraphPlot(Scene):
    def construct(self):
        axes = Axes()
        self.play(Create(axes))
