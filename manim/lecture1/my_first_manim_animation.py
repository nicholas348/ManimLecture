from manimlib import *# 调用manimlib库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):
        self.wait(1)#等待一秒
        hello_manim = Text("Hello, Manim!",font = "Georgia").scale(3)

        self.play(Write(hello_manim))#书写 hello manim
        self.wait()

        self.set_camera_orientation()


"""渲染：manimgl -qm -p my_first_manim_animation.py MyFirstManimAnimation"""
#C:\Users\F1339\Desktop\ManimLecture\manim\lecture1\my_first_manim_animation.py