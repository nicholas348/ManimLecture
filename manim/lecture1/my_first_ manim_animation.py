from manim import *# 调用manim库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):
        self.wait(1)#等待一秒
        hello_manim = Tex("hello, Manim!").scale(3)

        self.add(hello_manim)#书写 hello world


"""渲染：manim -qm -p (--renderer=opengl) my_first_ manim_animation.py MyFirstManimAnimation"""