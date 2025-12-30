from manim import *

class FunctionPlot(Scene):
    def construct(self):
        # 1. Create Axes
        ax = Axes(
            x_range=[-3, 3],
            y_range=[-2, 2],
            axis_config={"include_tip": True}
        ).add_coordinates()

        # 2. Define the graph (a sine wave)
        # We use np.sin because it's optimized for arrays
        curve = ax.plot(lambda x: np.sin(x), color=YELLOW)

        # 3. Animate
        self.play(Create(ax))
        self.play(Create(curve), run_time=2)
        self.wait()