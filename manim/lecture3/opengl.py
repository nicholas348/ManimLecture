# Note: This works best with --renderer=opengl
from manim import *

class OpenglIntro(Scene):
    def construct(self):
        cube = Cube(side_length=3, fill_opacity=1).set_color(BLUE)
        cube.set_stroke(width=0)  # Removing edges makes lighting look better
        self.play(Create(cube))
        self.wait(2)
        self.play(Uncreate(cube))
        self.wait(1)
        text=MathTex(r"e^{i\pi} + 1 = 0").scale(3)
        self.play(Write(text))
        self.wait(1)
        self.play(Uncreate(text))
        self.wait(1)

        text_interaction=Text(
            "然后现在你可以在终端里输入文本开始交互了"
        )
        self.play(Write(text_interaction))
        self.wait(1)
        self.play(Uncreate(text_interaction))
        self.wait(1)
        self.interactive_embed()


class OpenGLLight(ThreeDScene):
    def construct(self):
        # 1. Define the Light Source
        # In OpenGL mode, the camera has light properties
        self.camera.light_source.move_to([5, 5, 5])

        # 2. Create objects
        cube = Cube(side_length=3, fill_opacity=1).set_color(ORANGE)
        cube.set_stroke(width=0)  # Removing edges makes lighting look better

        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        # 3. Animate the light moving
        self.add(cube)
        self.play(
            self.camera.light_source.animate.move_to([-5, 5, 2]),
            run_time=3
        )
        self.wait()