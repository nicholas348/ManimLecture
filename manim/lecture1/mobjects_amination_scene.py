from manim import *
class MobjectsAnimation(Scene):#scene
    def construct(self):
        # 不同的mobjects
        mobject1 = Circle(color=BLUE)
        mobject2 = Square(color=RED).shift(RIGHT * 2)
        mobject3 = Triangle(color=GREEN).shift(LEFT * 2)

        #不同的animation效果
        self.add(mobject1,mobject2,mobject3)
        self.wait(2)
        self.play(FadeIn(mobject1),Create(mobject2),Write(mobject3))
        self.wait(2)
        self.play(mobject1.animate.shift(UP*2),mobject2.animate.rotate(PI/4),mobject3.animate.scale(1.5))
        self.wait(2)
        self.play(FadeOut(mobject1),Uncreate(mobject2),Unwrite(mobject3))
        self.wait(2)


class ValueTrackerExample(Scene):
    def construct(self):
        number_line = NumberLine()
        pointer = Vector(DOWN)
        label = MathTex("x").add_updater(lambda m: m.next_to(pointer, UP))

        tracker = ValueTracker(0)
        pointer.add_updater(
            lambda m: m.next_to(
                        number_line.n2p(tracker.get_value()),
                        UP
                    )
        )
        self.add(number_line, pointer,label)
        self.play(tracker.animate.set_value(5))
        self.wait(0.5)
        self.play(tracker.animate.set_value(3))
        self.play(tracker.animate.increment_value(-2))
        self.wait(0.5)



class ValueTrackerExampleOfIncrement(Scene):
    def construct(self):
        tracker = ValueTracker(0)
        label = Dot(radius=3).add_updater(lambda x : x.set_x(tracker.get_value()))
        self.add(label)
        self.add(tracker)
        tracker.add_updater(lambda mobject, dt: mobject.increment_value(dt))
        self.wait(2)


if __name__ == "__main__":
    with tempconfig({"renderer": "cairo"}):
        scene = MobjectsAnimation()
        scene.render()
