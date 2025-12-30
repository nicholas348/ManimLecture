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
