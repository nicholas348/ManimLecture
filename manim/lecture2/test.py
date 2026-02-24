from manim import *
class Test(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75*DEGREES,theta=45*DEGREES)
        s = Sphere()
        self.play(FadeIn(s))
        self.wait()