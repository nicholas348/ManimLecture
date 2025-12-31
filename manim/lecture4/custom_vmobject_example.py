from manim import *

class Ball(Circle):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)


    def jump(self):
        origin_coord=self.get_center()
        self.add_updater(
            lambda t,dt:
            t.move_to(
                origin_coord+UP*(-dt^2/4+1)
            )
        )
        return self

class test(Scene):
    def construct(self):
        ball=Ball()
        self.add(ball)
        self.play(ball.animate.jump())
