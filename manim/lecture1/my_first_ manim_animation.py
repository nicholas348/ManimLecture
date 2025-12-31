from manim import *# 调用manim库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):

        # 等待一秒
        self.wait(1)
        hello_manim = (Tex("hello, Manim!")#创造一个Manim文字对象
                       .scale(3))#放大3倍

        # 书写 hello world
        self.add(hello_manim)


"""渲染：manim -qm -p (--renderer=opengl) my_first_ manim_animation.py MyFirstManimAnimation"""