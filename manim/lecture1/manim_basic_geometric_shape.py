from manim import *


class BasicShapes(Scene):
    def construct(self):
        """
        创建几何形状
        """
        #创建一个半径为1，颜色为蓝色，透明度为0.5的圆
        circle = Circle(radius=1.0, color=BLUE, fill_opacity=0.5)

        #创建一个边长位2，颜色为绿，透明度为1的圆
        square = Square(side_length=2.0, color=GREEN)

        #创建一个边长为2，颜色为红，透明度为1的三角形，同时将这个三角形向右移3个单位
        triangle = Triangle(color=RED).shift(RIGHT * 3)

        """
        位置变换
        """
        #将正方形摆放在圆形左边
        square.next_to(circle, LEFT, buff=0.5)

        # 3. Animations
        # 'Create' draws the outline of the shape
        self.play(Create(circle), Write(Tex("Circle").next_to(circle, UP)))
        self.wait(1)

        # 'FadeIn' or 'DrawBorderThenFill'
        self.play(FadeIn(square), run_time=1.5)
        self.play(DrawBorderThenFill(triangle))

        # 4. Transformations (The "Magic" of Manim)
        # Morphing the circle into a star
        star = Star(color=YELLOW).scale(1.5)
        self.play(ReplacementTransform(circle, star))


