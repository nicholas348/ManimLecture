from manim import *


class RateFuncExample(Scene):
    def construct(self):
        # Create three circles
        c1 = Circle(color=BLUE).shift(UP * 2)
        c2 = Circle(color=RED)
        c3 = Circle(color=GREEN).shift(DOWN * 2)

        # Labels
        t1 = Text("Linear").next_to(c1, RIGHT)
        t2 = Text("Smooth (Default)").next_to(c2, RIGHT)
        t3 = Text("Bounce").next_to(c3, RIGHT)

        self.add(c1, c2, c3, t1, t2, t3)

        # Animate them across the screen
        self.play(
            c1.animate.shift(LEFT * 4),
            c2.animate.shift(LEFT * 4),
            c3.animate.shift(LEFT * 4),
            run_time=1,
            # Apply the rate functions here:
            rate_func=linear  # Constant speed
        )

        self.play(
            c1.animate.shift(RIGHT * 4),
            rate_func=lambda t:np.sin(t),
            run_time=1
        )

        # Example of a more complex rate function
        def bounce(t):
            return t**2

        self.play(
            c3.animate.shift(RIGHT * 4),
            rate_func=bounce,  # Elastic effect at the end
            run_time=1
        )