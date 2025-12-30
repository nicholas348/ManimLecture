import random
from manim import ManimColor as Color
from manim import *


class LabelUpdater(Scene):
    def construct(self):
        square = Square()
        label = Text("Top")

        # Define the logic: move the label to the top of the square
        label.add_updater(lambda m: m.next_to(square, UP))

        self.add(square, label)
        self.play(square.animate.shift(RIGHT * 3 + UP * 2))
        self.play(square.animate.rotate(PI/4))


class DotColorUpdater(Scene):
    def construct(self):
        growing_circle = Circle(radius=0.001)

        moving_line = Line([-7, -5, 0], [-6, 5, 0])
        moving_line.normal_vector = moving_line.copy().rotate(90 * DEGREES).get_vector()

        def opacity_updater(obj):
            if (  # check whether dot is inside circle
                    sum((growing_circle.points[0] - growing_circle.get_center()) ** 2)
                    >= sum((obj.get_center() - growing_circle.get_center()) ** 2)
                    #  round(  # more general winding number approach!
                    #      get_winding_number(growing_circle.get_anchors() - obj.get_center())
                    #  ) > 0
            ):
                obj.set_fill(BLUE, opacity=1)
                obj.clear_updaters()  # removes opacity_updater, ...
                obj.add_updater(color_updater)  # and attaches the color_updater function

        def color_updater(obj):
            if (  # check whether point is *right* of the line
                    np.dot(obj.get_center(), moving_line.normal_vector)
                    < np.dot(moving_line.get_start(), moving_line.normal_vector)
            ):
                if obj.color != Color(BLUE):
                    obj.set_color(BLUE)
            else:  # otherwise point is *left* of the line
                if obj.color != Color(YELLOW):
                    obj.set_color(YELLOW)

        self.add(growing_circle)

        for _ in range(30):
            p = Dot(fill_opacity=0.6)
            p.move_to([random.uniform(-6, 6), random.uniform(-4, 4), 0])
            p.add_updater(opacity_updater)
            self.add(p)

        self.play(
            growing_circle.animate.scale_to_fit_width(1.5 * config.frame_width),
            run_time=5
        )
        self.play(Create(moving_line))
        self.play(moving_line.animate.shift(14 * RIGHT), run_time=5)
        self.play(moving_line.animate.shift(14 * LEFT), run_time=5)