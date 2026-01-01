from manim import *



class Battery(VMobject):
    def __init__(self, level=0.2, battery_color=WHITE, **kwargs):
        super().__init__(**kwargs)
        self.level = level  # Internal state: 0.0 to 1.0

        # 1. Create the outer shell
        self.case = RoundedRectangle(
            corner_radius=0.1, height=1.5, width=3, color=battery_color
        )
        # 2. Create the positive terminal (the little bump)
        self.terminal = Rectangle(
            height=0.6, width=0.2, color=battery_color, fill_opacity=1
        ).next_to(self.case, RIGHT, buff=0)

        # 3. Create the fill level (the dynamic part)
        self.inner_fill = Rectangle(
            height=1.3,
            width=2.8 * self.level,  # Initial width based on level
            fill_color=self.get_level_color(),
            fill_opacity=0.8,
            stroke_width=0
        ).align_to(self.case, LEFT).shift(RIGHT * 0.1)

        # Add parts to the VMobject
        self.add(self.case, self.terminal, self.inner_fill)

    def get_level_color(self):
        """Logic to change color based on charge level."""
        if self.level < 0.2:
            return RED
        elif self.level < 0.6:
            return YELLOW
        else:
            return GREEN

    def set_level(self, new_level):
        """
        A 'Special Function' to update the state.
        This re-scales the inner fill and updates the color.
        """
        self.level = np.clip(new_level, 0, 1)
        # Calculate new width: max width is 2.8
        new_width = 2.8 * self.level

        # Update the fill shape
        self.inner_fill.stretch_to_fit_width(new_width, about_edge=LEFT)
        self.inner_fill.set_color(self.get_level_color())
        return self

    def charge(self):
        # We save the starting level to animate FROM it
        start_level = self.level

        def charge_updater(obj, alpha):
            current_level = interpolate(start_level, 1.0, alpha)
            obj.set_level(current_level)

        return UpdateFromAlphaFunc(
            self,
            charge_updater
        )


# --- Usage in a Scene ---

class BatteryTest(Scene):
    def construct(self):
        # Initialize at 10%
        bat = Battery(level=0.1)
        self.add(bat)
        self.wait(1)

        # Use our custom animation function
        self.play(bat.charge(), run_time=3, rate_func=linear)
        self.wait(1)
        # Manually set to a specific level
        self.play(bat.animate.set_level(0.5))
        self.wait()