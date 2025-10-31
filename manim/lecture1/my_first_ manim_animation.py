from manim import *# 调用manim库中的所有模块
class MyFirstManimAnimation(Scene):
    def construct(self):
        # Create a text object
        hello_world = Text("Hello, Manim!").scale(3)

        # Display the text on the screen with a writing animation
        self.play(Write(hello_world))

        # Wait for 2 seconds before ending the scene
        self.wait(2)

if __name__ == "__main__":#运行并渲染该脚本
    with tempconfig({"renderer": "cairo"}):
        scene = MyFirstManimAnimation()
        scene.render()