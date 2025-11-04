from manim import *
class Structure(Scene):#scene
    def construct(self):
        # 创造一个text 物品
        hello_world = Text("Hello, Manim!").scale(3)

        # Display the text on the screen with a writing animation(amination)
        self.play(Write(hello_world))

        # Wait for 2 seconds before ending the scene
        self.wait(2)




if __name__ == "__main__":
    with tempconfig({"quality": "high_quality","preview": True}):
        scene = Structure()
        scene.render()
# or use terminal command: manim -pql manim_structure.py Structure
# -p: preview the video after rendering
# -ql: quality low
# -qm: quality medium
# -qh: quality high