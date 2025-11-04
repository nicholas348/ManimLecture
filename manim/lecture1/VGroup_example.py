from manim import *
class VGroupExample(Scene):
    def construct(self):
        dots = [Dot() for _ in range(10)]
        DotsVG = (VGroup(dots).arrange(RIGHT))
        DotsVG.shuffle()
        self.play(Create(DotsVG))
        self.wait(5)
        self.play(DotsVG.animate.shift(UP))
        self.wait(2)
        self.play(DotsVG[4].animate.shift(DOWN))
        self.wait(2)
if __name__ == "__main__":
    with tempconfig({"renderer": "cairo","preview":True}):
        scene = VGroupExample()
        scene.render()