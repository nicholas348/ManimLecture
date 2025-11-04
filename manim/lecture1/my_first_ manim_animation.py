from manim import *# 调用manim库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):

        hello_world = Text("Hello, Manim!").scale(3)

        self.play(Write(hello_world))


if __name__ == "__main__":#运行并渲染该脚本
    with tempconfig({"renderer": "cairo"}):
        test = MyFirstManimAnimation()
        test.render()