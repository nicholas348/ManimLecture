import random
from manim import ManimColor as Color
from manim import *


class LabelUpdater(Scene):
    def construct(self):
        square = Square()
        label = Text("Top")

        # 将标签移动到方块上方
        label.add_updater(lambda m: m.next_to(square, UP))

        self.add(square, label)
        self.play(square.animate.shift(RIGHT * 3 + UP * 2))
        self.play(square.animate.rotate(PI/4))


class DotColorUpdater(Scene):
    def construct(self):
        growing_circle = Circle(radius=0.001)

        moving_line = Line(np.array([-7, -5, 0]), np.array([-6, 5, 0]))
        moving_line.normal_vector = moving_line.copy().rotate(90 * DEGREES).get_vector()

        def opacity_updater(obj):
            if (  # 检查点是否在圆圈内部
                    sum((growing_circle.points[0] - growing_circle.get_center()) ** 2)
                    >= sum((obj.get_center() - growing_circle.get_center()) ** 2)
                    #  round(  # more general winding number approach!
                    #      get_winding_number(growing_circle.get_anchors() - obj.get_center())
                    #  ) > 0
            ):
                obj.set_fill(BLUE, opacity=1)
                obj.clear_updaters()  # 为确保万一，首先一处所有的在这个点上的updaters
                obj.add_updater(color_updater)  # 增加这个updater

        def color_updater(obj):
            if (  # 这个点是否在这条线的右边
                    np.dot(obj.get_center(), moving_line.normal_vector)
                    < np.dot(moving_line.get_start(), moving_line.normal_vector)
            ):

                #如果点的颜色不是蓝色
                if obj.color != Color(BLUE):

                    #将点的颜色设置为蓝色
                    obj.set_color(BLUE)
            else:  # 除此之外（就是在这条线的左边）
                #如果点的颜色不是黄色
                if obj.color != Color(YELLOW):

                    #将点的颜色设置为黄色
                    obj.set_color(YELLOW)

        self.add(growing_circle)

        for _ in range(30):
            p = Dot(fill_opacity=0.6)

            #移动到随机位置
            p.move_to(np.array([random.uniform(-6, 6), random.uniform(-4, 4), 0]))

            p.add_updater(opacity_updater)
            self.add(p)

        self.play(
            growing_circle.animate.scale_to_fit_width(1.5 * config.frame_width),
            run_time=5
        )
        self.play(Create(moving_line))
        self.play(moving_line.animate.shift(14 * RIGHT), run_time=5)
        self.play(moving_line.animate.shift(14 * LEFT), run_time=5)