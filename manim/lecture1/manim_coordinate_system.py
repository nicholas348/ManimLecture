from manim import *

class CoordSystem(Scene):
    def construct(self):
        # 1. Create a grid
        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": TEAL,
                "stroke_width": 2,
                "stroke_opacity": 0.3
            }
        )
        self.add(plane) # Add to scene immediately

        # 2. Create a point at specific coordinates
        dot = Dot(point=[2, 1,0], color=YELLOW)
        label = MathTex("(2, 1)").next_to(dot, UR, buff=0.1)

        # 3. Create an arrow from origin to the dot
        arrow = Arrow(ORIGIN, dot.get_center(), buff=0)

        self.add(arrow, dot, label)
        self.wait()