from manim import *# 调用manim库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):
        self.wait(1)#等待一秒
        hello_manim = Text("hello, Manim!").scale(3)

        self.play(Write(hello_manim))#书写 hello world
        self.wait(2)


if __name__ == "__main__":#运行并渲染该脚本
    with tempconfig({"renderer": "cairo","preview": True}):
        test = MyFirstManimAnimation()
        test.render()