from manimlib import *

class BasicShapes(Scene):
    def construct(self):
        # 1. Create Geometric Objects
        circle = Circle(radius=1.0, color=BLUE, fill_opacity=0.5)
        square = Square(side_length=2.0, color=GREEN)
        triangle = Triangle(color=RED,fill_opacity=0.3).shift(RIGHT * 3)
        label = Text("Circle",font = "Times New Roman").next_to(circle, UP)

        # 2. Positioning
        # We can move objects relative to each other or the screen
        square.next_to(circle, LEFT, buff=1)

        # 3. Animations
        # 'ShowCreation' draws the outline of the shape
        self.play(
            ShowCreation(circle), 
            Write(label
                ),
            run_time = 1
        )
        self.wait(1)

        # 'FadeIn' or 'DrawBorderThenFill'
        self.play(FadeIn(square), run_time=1.5)
        self.play(DrawBorderThenFill(triangle))

        # 4. Transformations (The "Magic" of Manim)
        # Morphing the circle into a pentagon
        pentagon = RegularPolygon(n = 5, color = YELLOW, fill_opacity = 0.3)
        self.play(ReplacementTransform(circle, pentagon))

        # 5. Grouping and Moving
        group = VGroup(square, pentagon, triangle, label)
        self.wait()
        self.play(group.animate.shift(DOWN * 2).scale(2))
        self.wait()
        self.play(group.animate.shift(UP * 2).rotate(PI/2).scale(1/3))
        self.wait(2)