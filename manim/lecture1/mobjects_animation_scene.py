from manimlib import *
class MobjectsAnimation(Scene):#scene
    def construct(self):
        # 不同的mobjects
        mobject1 = Circle(color=BLUE, fill_opacity = 0.3, stroke_color = BLUE)
        mobject2 = Square(color=RED, fill_opacity = 0.3)
        mobject3 = Triangle(color=GREEN, fill_opacity = 0.3)
        group = VGroup(mobject1,mobject2,mobject3).arrange(RIGHT, buff = 1)
        path = Circle(radius = 2).next_to(mobject2, LEFT, buff = 1)

        self.play(
            FadeIn(mobject1),
            ShowCreation(mobject2),
            Write(mobject3)
        )
        self.wait(2)

        # MoveMents
        self.play(mobject1.animate.shift(RIGHT),run_time = 0.2)
        self.play(
            MoveAlongPath(mobject1,path),
            mobject2.animate.rotate(PI/4),
            mobject3.animate.scale(1.5).shift(LEFT),
            run_time = 5
        )
        self.wait(2)

        self.play(
            FadeOut(mobject1),
            Uncreate(mobject2),
            Uncreate(mobject3)
        )
        self.wait(2)

        text = Tex(r"\iint_S (\nabla \times F) \cdot ds = \oint_{\partial S} F\cdot ds")
        self.play(Write(text))
        self.wait(3)
        self.play(Uncreate(text))
        self.wait(1)

