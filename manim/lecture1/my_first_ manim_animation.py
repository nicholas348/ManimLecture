from manim import *# 调用manim库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):
        # 创造一个text 物品
        hello_world = Text("Hello, Manim!").scale(3)

        # 写一个书写写这个text物品的脚本
        self.play(Write(hello_world))


if __name__ == "__main__":#运行并渲染该脚本
    with tempconfig({"renderer": "cairo"}):
        test = MyFirstManimAnimation()
        test.render()