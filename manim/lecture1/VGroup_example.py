from manim import *
class VGroupExample(Scene):
    def construct(self):
        dots = [Dot() for _ in range(10)]
        DotsVG = VGroup(dots).arrange(RIGHT)
        self.add(DotsVG)
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo"}):
        scene = VGroupExample()
        scene.render()