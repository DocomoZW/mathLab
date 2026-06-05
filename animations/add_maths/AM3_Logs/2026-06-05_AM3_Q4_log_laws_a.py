from manim import *
import math

class LogLaws(Scene):
    def construct(self):
        title = Text("Log Laws", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        laws = [
            "Product: log(MN) = log M + log N",
            "Quotient: log(M/N) = log M - log N",
            "Power: log(M^k) = k log M"
        ]
        texts = []
        for i, law in enumerate(laws):
            t = Text(law, font_size=26, color=YELLOW)
            t.shift(UP*0.5 - i*0.8*DOWN)
            texts.append(t)
        
        for t in texts:
            self.play(Write(t), run_time=0.5)
        
        example = Text("Example: log_2 8 + log_2 4 = log_2 32 = 5", font_size=26, color=GREEN)
        example.to_edge(DOWN)
        self.play(Write(example))
        self.wait(2)
