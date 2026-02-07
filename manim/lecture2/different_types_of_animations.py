from manimlib import *
class AnimateSyntax(Scene):
    def construct(self):
        s = Square(color=GREEN, fill_opacity=0.5)
        c = Circle(color=RED, fill_opacity=0.5)
        self.add(s, c)
        self.play(s.animate.shift(UP), c.animate.shift(DOWN))
        self.play(VGroup(s, c).animate.arrange(RIGHT))
        self.play(c.animate.shift(RIGHT).scale(2), rate_func = linear)
        self.wait()


class AnimateProblem(Scene):
    def construct(self):
        left_square = Square()
        right_square = Square()
        VGroup(left_square, right_square).arrange(RIGHT, buff=1)
        self.add(left_square, right_square)
        self.play(left_square.animate.rotate(PI), Rotate(right_square, PI), run_time=2)
        


