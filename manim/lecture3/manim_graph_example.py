from manim import *


class GraphExample(Scene):
    def construct(self):
        # 1. Create the Axes
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-2, 10],
            axis_config={"color": BLUE},
        )

        # 2. Define a function (y = x^2)
        func = axes.plot(lambda x: x ** 2, color=WHITE)

        # 3. Add labels
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        func_label = axes.get_graph_label(func, label="x^2")

        # 4. Animate the creation
        self.play(Create(axes), Write(labels))
        self.wait(0.5)
        self.play(Create(func), FadeIn(func_label))
        self.wait(2)


from manim import *


class ThreeDPlaneExample(ThreeDScene):
    def construct(self):
        # 1. Initialize 3D Axes
        axes = ThreeDAxes()

        # 2. Define a 3D Surface (z = x^2 - y^2)
        resolution_fa = 24
        surface = Surface(
            lambda u, v: np.array([u, v, u ** 2 - v ** 2]),
            v_range=[-2, 2],
            u_range=[-2, 2],
            checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(resolution_fa, resolution_fa),
        )

        # 3. Set the camera orientation
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)

        # 4. Animate
        self.add(axes)
        self.play(Create(surface))
        self.begin_ambient_camera_rotation(rate=0.1)  # Slowly rotates the view
        self.wait(3)
        self.stop_ambient_camera_rotation()