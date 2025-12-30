from manim import *


class BasicArc(Scene):
    def construct(self):
        # Create an arc that starts at 0 degrees and sweeps 180 degrees (PI)
        arc = Arc(radius=2.0, start_angle=0, angle=PI, color=BLUE)

        self.play(Create(arc))
        self.wait()


class ArcPoints(Scene):
    def construct(self):
        dot1 = Dot(point=[-2, -1, 0])
        dot2 = Dot(point=[2, 1, 0])

        # angle=PI/3 creates a gentle curve between the dots
        curved_line = ArcBetweenPoints(dot1.get_center(), dot2.get_center(), angle=PI / 3)

        self.add(dot1, dot2)
        self.play(Create(curved_line))
        self.wait()


class ArcSweep(Scene):
    def construct(self):
        # Create a dashed circle for reference
        bg_circle = Circle(radius=2, color=GRAY).set_stroke(opacity=0.3)
        self.add(bg_circle)

        # Create the arc
        growing_arc = Arc(radius=2, start_angle=0, angle=TAU * 0.75, color=YELLOW)

        # Use Clockwise/CounterClockwise for specific effects
        self.play(Create(growing_arc), run_time=2)
        self.wait()

class CurvedArrowExample(Scene):
    def construct(self):
        arrow = CurvedArrow(start_point=LEFT, end_point=RIGHT, angle=-PI/2)
        self.play(Create(arrow))

class ArcPoly(Scene):
    def construct(self):
        # Create a "rounded" triangle shape
        ap = ArcPolygon(LEFT, UP, RIGHT, radius=2)
        ap.set_fill(BLUE, opacity=0.5)
        self.play(Create(ap))