from manim import *
import math

class LogIntro(Scene):
    def construct(self):
        title = Text("Introduction to Logarithms", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        q = Text("2^x = 8  =>  x = ?", font_size=32, color=YELLOW)
        q.shift(UP*1)
        self.play(Write(q))
        
        ans = Text("x = 3 because 2^3 = 8", font_size=28, color=GREEN)
        ans.next_to(q, DOWN)
        self.play(Write(ans))
        
        defn = Text("log_2 8 = 3  means  2^3 = 8", font_size=28, color=BLUE)
        defn.next_to(ans, DOWN)
        self.play(Write(defn))
        
        bridge = Text("log_a b = x  <=>  a^x = b", font_size=28, color=ORANGE)
        bridge.to_edge(DOWN)
        self.play(Write(bridge))
        self.wait(2)
