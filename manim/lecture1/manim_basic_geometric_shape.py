from manim import *


class BasicShapes(Scene):
    def construct(self):
        # 1. Create Geometric Objects
        circle = Circle(radius=1.0, color=BLUE, fill_opacity=0.5)
        square = Square(side_length=2.0, color=GREEN)
        triangle = Triangle(color=RED).shift(RIGHT * 3)

        # 2. Positioning
        # We can move objects relative to each other or the screen
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

        # 5. Grouping and Moving
        group = VGroup(square, star, triangle)
        self.play(group.animate.shift(DOWN * 2).scale(0.5))
        self.play(Rotate(group, angle=PI / 2))

        self.wait(2)