from manim import *
class MobjectsAnimation(Scene):#scene
    def construct(self):
        # 不同的mobjects
        mobject1 = Circle(color=BLUE)
        mobject2 = Square(color=RED).shift(RIGHT * 2)
        mobject3 = Triangle(color=GREEN).shift(LEFT * 2)

        """
        出现部分
        FadeIn:淡入
        Create:创建
        Write:写入
        """
        self.play(FadeIn(mobject1),Create(mobject2),Write(mobject3))
        self.wait(2)

        """
        移动
        animate:动画
        shift:移动
        rotate:旋转
        scale:缩放
        """
        self.play(mobject1.animate.shift(UP*2),mobject2.animate.rotate(PI/4),mobject3.animate.scale(1.5))
        self.wait(2)

        """
        消失部分
        FadeOut:淡出
        Uncreate:取消创建
        Unwrite:取消写入
        """
        self.play(FadeOut(mobject1),Uncreate(mobject2),Unwrite(mobject3))
        self.wait(2)


        """
        文字以及公式
        """
        text = MathTex(r"\iint_S (\nabla \times F) \cdot ds = \oint_{\partial S} F\cdot ds")
        self.play(Write(text))
        self.wait(3)
        self.play(Uncreate(text))
        self.wait(1)

