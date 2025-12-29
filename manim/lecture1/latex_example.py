from manim import *
class LatexExample(Scene):
    def construct(self):
        text=MathTex(r"e^{i\pi} + 1 = 0")
        self.add(text)