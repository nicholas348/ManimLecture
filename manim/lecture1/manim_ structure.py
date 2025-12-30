from manim import *
class Structure(Scene):#scene
    def construct(self):
        # 创造一个text 物品hello_world
        hello_world = Tex("Hello, Manim!").scale(3)

        # 渲染一个书写hello_world的动画
        self.play(Write(hello_world))

        # 等待2秒
        self.wait(2)




if __name__ == "__main__":
    with tempconfig({"quality": "high_quality","preview": True}):
        scene = Structure()
        scene.render()
# 或者可以使用终端渲染
# -p: 是否预览
# -ql: 低画质
# -qm: 中等画质
# -qh: 高画质
#--renderer=opengl 使用opengl渲染