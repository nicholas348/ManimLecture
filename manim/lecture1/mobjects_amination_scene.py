from manim import *
class MobjectsAnimation(Scene):#scene
    def construct(self):
        # 不同的mobjects
        mobject1 = Circle(color=BLUE)
        mobject2 = Square(color=RED).shift(RIGHT * 2)
        mobject3 = Triangle(color=GREEN).shift(LEFT * 2)
        self.play(FadeIn(mobject1),Create(mobject2),Write(mobject3))
        self.wait(2)
        self.play(mobject1.animate.shift(UP*2),mobject2.animate.rotate(PI/4),mobject3.animate.scale(1.5))
        self.wait(2)
        self.play(FadeOut(mobject1),Uncreate(mobject2),Unwrite(mobject3))
        self.wait(2)
        text = MathTex(r"\iint_S (\nabla \times F) \cdot ds = \oint_{\partial S} F\cdot ds")
        self.play(Write(text))
        self.wait(3)
        self.play(Uncreate(text))
        self.wait(1)

