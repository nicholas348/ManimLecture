from manim import *


class Intro3D(ThreeDScene):
    def construct(self):
        # 1. Initialize axes and a 3D shape
        axes = ThreeDAxes()
        sphere = Sphere(radius=2, fill_opacity=0.7).set_color(BLUE)

        # 2. Set the camera angle
        # phi: angle from the z-axis (vertical)
        # theta: rotation around the z-axis (horizontal)
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        self.add(axes, sphere)
        self.begin_ambient_camera_rotation(rate=0.1)  # Slowly rotate camera
        self.wait(3)
        self.stop_ambient_camera_rotation()
        