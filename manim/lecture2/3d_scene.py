from manimlib import *


class Intro3D(ThreeDScene):
    def construct(self):
        # 1. Initialize axes and a 3D shape
        axes = ThreeDAxes()
        sphere = Sphere(radius=2).set_color(BLUE).set_opacity(0.7)

        # 2. Set the camera angle
        # phi: angle from the z-axis (vertical)
        # theta: rotation around the z-axis (horizontal)
        self.camera.frame.set_euler_angles(theta=-45 * DEGREES, phi=75 * DEGREES)

        self.add(axes, sphere)
        # This tells the frame to rotate its theta angle by 0.1 radians every second
        self.camera.frame.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
        self.wait(3)
        self.camera.frame.clear_updaters()
        