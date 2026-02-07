from manimlib import *

class Structure(Scene):#scene
    def construct(self):
        # 创造一个text 物品hello_world
        hello_world = Text("Hello, Manim!",font="Times New Roman").scale(3)


        # 渲染一个书写hello_world的动画
        self.play(Write(hello_world))

        # 等待2秒
        self.wait(2)

        self.play(s.animate.rotate(angle=PI/4,about_point = c.get_center()))


#if __name__ == "__main__":
#    with tempconfig({"quality": "high_quality","preview": True}):
#        scene = Structure()
#        scene.render()


# Terminal Controls
# -p: Preview
# -ql: Low Quality
# -qm: Medium Quality
# -qh: High Quality

# -w to write the scene to a file
# -o to write the scene to a file and open the result
# -s to skip to the end and just show the final frame.
# -so will save the final frame to an image and show it
# -n <number> to skip ahead to the n'th animation of a scene.
# -f to make the playback window fullscreen