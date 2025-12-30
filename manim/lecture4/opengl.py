# Note: This works best with --renderer=opengl
from manim import *

class OpenglIntro(Scene):
    def construct(self):
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
        self.interactive_embed()