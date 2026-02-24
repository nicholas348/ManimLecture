"""
Lecture 2: Improved and Extended Examples
第二讲：改进和扩展示例

This file contains enhanced versions of the lecture 2 examples with:
- Detailed bilingual comments / 详细的双语注释
- Additional examples for each concept / 每个概念的额外示例
- Best practices highlighted / 突出最佳实践

Render command / 渲染命令:
manimgl improved_examples.py <SceneName> -p -qm
"""

from manimlib import *

# ============================================================================
# PART 1: Animation Syntax Examples
# 第一部分：动画语法示例
# ============================================================================

class AnimateSyntaxBasic(Scene):
    """
    Basic .animate syntax demonstration
    基本 .animate 语法演示
    """
    def construct(self):
        # Create two shapes with different colors and opacity
        # 创建两个具有不同颜色和不透明度的形状
        square = Square(color=GREEN, fill_opacity=0.5)
        circle = Circle(color=RED, fill_opacity=0.5)
        
        # Add shapes to the scene
        # 将形状添加到场景中
        self.add(square, circle)
        self.wait(0.5)
        
        # Example 1: Simultaneous animations using .animate
        # 示例1：使用 .animate 的同时动画
        # Both objects move in opposite directions at the same time
        # 两个对象同时向相反方向移动
        self.play(
            square.animate.shift(UP),
            circle.animate.shift(DOWN)
        )
        self.wait(0.5)
        
        # Example 2: Using VGroup to animate together
        # 示例2：使用 VGroup 一起动画
        # VGroup allows us to treat multiple objects as one
        # VGroup允许我们将多个对象视为一个
        shapes_group = VGroup(square, circle)
        self.play(shapes_group.animate.arrange(RIGHT, buff=1))
        self.wait(0.5)
        
        # Example 3: Chaining multiple transformations
        # 示例3：链接多个变换
        # You can chain: shift, scale, rotate, set_color, etc.
        # 可以链接：shift、scale、rotate、set_color等
        self.play(
            circle.animate  # Custom timing function / 自定义时间函数
            .shift(RIGHT * 2)
            .scale(2)
            .set_color(BLUE), rate_func=linear
        )
        self.wait(1)


class AnimateVsAnimationClass(Scene):
    """
    Demonstrates the key difference between .animate and Animation classes
    演示 .animate 和 Animation 类之间的关键区别
    
    KEY LEARNING POINT:
    - .animate interpolates ALL properties (position, rotation, etc.)
    - Animation classes (like Rotate) only change specific properties
    
    关键学习点：
    - .animate 插值所有属性（位置、旋转等）
    - Animation类（如Rotate）只改变特定属性
    """
    def construct(self):
        # Create two identical squares
        # 创建两个相同的正方形
        left_square = Square().set_color(BLUE)
        right_square = Square().set_color(BLUE)
        
        # Position them side by side
        # 将它们并排放置
        VGroup(left_square, right_square).arrange(RIGHT, buff=2)
        
        # Add labels to identify them
        # 添加标签以识别它们
        left_label = Text(".animate", font_size=24).next_to(left_square, DOWN)
        right_label = Text("Rotate()", font_size=24).next_to(right_square, DOWN)
        
        self.add(left_square, right_square, left_label, right_label)
        self.wait(1)
        
        # Compare the two methods
        # 比较两种方法
        self.play(
            # Left: .animate method - interpolates position AND rotation
            # 左：.animate方法 - 插值位置和旋转
            left_square.animate.rotate(PI),
            
            # Right: Rotate class - only rotates in place
            # 右：Rotate类 - 只在原地旋转
            Rotate(right_square, PI),
            
            run_time=3
        )
        self.wait(2)
        
        # Notice the difference in the animation path!
        # 注意动画路径的差异！


class MultipleObjectAnimation(Scene):
    """
    Advanced example: Animating many objects with different timings
    高级示例：以不同时间动画化多个对象
    """
    def construct(self):
        # Create a grid of dots
        # 创建一个点的网格
        dots = VGroup()
        for i in range(5):
            for j in range(5):
                dot = Dot(point=np.array([i-2, j-2, 0]))
                dots.add(dot)
        
        # Color gradient from blue to red
        # 从蓝色到红色的颜色渐变
        dots.set_color_by_gradient(BLUE, RED)
        self.add(dots)
        self.wait(0.5)
        
        # Animate each dot with a delay (creates a wave effect)
        # 以延迟动画化每个点（创建波浪效果）
        animations = []
        for i, dot in enumerate(dots):
            # Each dot gets a slightly different run_time
            # 每个点获得稍微不同的run_time
            animations.append(
                dot.animate.shift(UP * 0.5 + RIGHT * 0.2).set_color(YELLOW)
            )
        
        # Play all animations together with lag
        # 以延迟一起播放所有动画
        self.play(
            AnimationGroup(*animations, lag_ratio=0.1),
            run_time=3
        )
        self.wait(1)


# ============================================================================
# PART 2: Updaters - Dynamic Behavior
# 第二部分：更新器 - 动态行为
# ============================================================================

class UpdaterBasicExample(Scene):
    """
    Simple updater: Label follows a moving square
    简单更新器：标签跟随移动的正方形
    """
    def construct(self):
        # Create a square and a label
        # 创建一个正方形和一个标签
        square = Square(color=BLUE, fill_opacity=0.5)
        label = Text("Top", font_size=30, font = "Times New Roman")
        
        # The updater function: called EVERY frame
        # 更新器函数：每一帧都调用
        # Lambda function: m is the mobject (label), it repositions itself
        # Lambda函数：m是mobject（标签），它重新定位自己
        label.add_updater(lambda m: m.next_to(square, UP).shift(UP))
        
        self.add(square, label)
        self.wait(0.5)
        
        # Move the square - the label automatically follows!
        # 移动正方形 - 标签自动跟随！
        self.play(square.animate.shift(RIGHT * 3), run_time=2)
        self.wait(0.5)
        
        self.play(square.animate.rotate(PI/4), run_time=2)
        self.wait(0.5)
        
        # Scale - label adjusts
        # 缩放 - 标签调整
        self.play(square.animate.scale(2), run_time=2)
        self.wait(1)
        
        # IMPORTANT: Remove updaters when done to prevent memory leaks
        # 重要：完成后删除更新器以防止内存泄漏
        label.clear_updaters()


class RotatingUpdaterExample(Scene):
    """
    Updater with time-based rotation
    基于时间的旋转更新器
    """
    def construct(self):
        # Central circle
        # 中心圆
        center = Circle(radius=0.2, color=YELLOW, fill_opacity=1)
        
        # Orbiting circle
        # 轨道圆
        satellite = Circle(radius=0.3, color=BLUE, fill_opacity=0.7)
        satellite.shift(RIGHT * 2)
        
        # Counter to track time
        # 跟踪时间的计数器
        self.time = 0
        
        # Updater with dt (delta time)
        # 带有dt（增量时间）的更新器
        def orbit_updater(mob, dt):
            self.time += dt
            # Position based on time: circular motion
            # 基于时间的位置：圆周运动
            angle = self.time * TAU / 4  # One rotation every 4 seconds / 每4秒旋转一次
            mob.move_to(center.get_center() + np.array([
                2 * np.cos(angle),
                2 * np.sin(angle),
                0
            ]))
        
        satellite.add_updater(orbit_updater)
        
        self.add(center, satellite)
        self.wait(8)  # Watch it orbit for 8 seconds / 观察它轨道运行8秒
        
        satellite.clear_updaters()


class ConditionalUpdaterExample(Scene):
    """
    Advanced: Updater that changes behavior based on conditions
    高级：根据条件改变行为的更新器
    """
    def construct(self):
        # Create a moving line
        # 创建一条移动的线
        line = Line(LEFT * 3, RIGHT * 3, color=GREEN)
        line.shift(UP * 2)
        
        # Create dots that change color based on position
        # 创建根据位置改变颜色的点
        dots = VGroup()
        for i in range(20):
            # np.random.uniform(low, high, size)
            random_pos = [
                np.random.uniform(-4, 4), # x 轴范围
                np.random.uniform(-3, 3), # y 轴范围
                0                         # z 轴设为 0
            ]
            dot = Dot(random_pos, color=BLUE)
            dots.add(dot)
        
        # Updater: change color based on y-position relative to line
        # 更新器：根据相对于线的y位置改变颜色
        def color_updater(mob):
            line_y = line.get_center()[1]
            dot_y = mob.get_center()[1]
            
            if dot_y < line_y:
                mob.set_color(BLUE)
            else:
                mob.set_color(RED)
        
        # Add updater to each dot
        # 向每个点添加更新器
        for dot in dots:
            dot.add_updater(color_updater)
        
        self.add(line, dots)
        self.wait(0.5)
        
        # Move the line down - dots change color as it passes
        # 向下移动线 - 当它通过时点改变颜色
        self.play(line.animate.shift(DOWN * 4), run_time=5)
        self.wait(1)
        
        # Clean up
        # 清理
        for dot in dots:
            dot.clear_updaters()


# ============================================================================
# PART 3: ValueTracker - Parametric Animations
# 第三部分：ValueTracker - 参数化动画
# ============================================================================

class ValueTrackerIntro(Scene):
    """
    Basic ValueTracker usage: Pointer on a number line
    基本ValueTracker用法：数字线上的指针
    """
    def construct(self):
        # Create a number line
        # 创建一个数字线
        line = NumberLine(
            x_range=[-5, 5, 1],
            width=10,
            include_numbers=True
        )
        
        # Create a pointer (triangle)
        # 创建指针（三角形）
        pointer = Triangle(color=YELLOW, fill_opacity=1).scale(0.2)
        pointer.rotate(-PI/2)  # Point downward / 向下指
        
        # Create a label showing the current value
        # 创建显示当前值的标签
        label = DecimalNumber(0, num_decimal_places=2)
        
        # VALUE TRACKER: The invisible controller
        # VALUE TRACKER：不可见的控制器
        tracker = ValueTracker(0)
        
        # Pointer updater: position based on tracker value
        # 指针更新器：基于跟踪器值的位置
        pointer.add_updater(
            lambda m: m.next_to(
                line.number_to_point(tracker.get_value()),
                UP
            )
        )
        
        # Label updater: display the tracker value
        # 标签更新器：显示跟踪器值
        label.add_updater(
            lambda m: m.set_value(tracker.get_value()).next_to(pointer, UP)
        )
        
        self.add(line, pointer, label)
        self.wait(1)
        
        # Animate the tracker - everything else follows automatically!
        # 动画化跟踪器 - 其他所有内容自动跟随！
        self.play(tracker.animate.set_value(3), run_time=2)
        self.wait(0.5)
        
        self.play(tracker.animate.set_value(-4), run_time=3)
        self.wait(0.5)
        
        self.play(tracker.animate.set_value(2.5), run_time=2)
        self.wait(1)
        
        # Clean up
        pointer.clear_updaters()
        label.clear_updaters()


class ValueTrackerGraph(Scene):
    """
    Advanced: Use ValueTracker to animate a function graph
    高级：使用ValueTracker动画化函数图
    """
    def construct(self):
        # Create axes
        # 创建坐标轴
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-4, 4, 1],
            axis_config={"include_tip": True}
        )
        # 按照顺序，第一个是 x 轴，第二个是 y 轴
        axes_labels = axes.get_axis_labels("x", "f(x)")
        
        # ValueTracker for the animation parameter
        # 动画参数的ValueTracker
        a_tracker = ValueTracker(1)
        
        # Function: f(x) = a * x^2 where 'a' changes
        # 函数：f(x) = a * x^2 其中 'a' 改变
        def get_graph():
            a = a_tracker.get_value()
            return axes.get_graph(
                lambda x: a * x**2,
                color=BLUE
            )
        
        # Graph that updates with tracker
        # 使用跟踪器更新的图形
        graph = always_redraw(get_graph)
        
        # Label showing current 'a' value
        # 显示当前'a'值的标签
        label = always_redraw(
            lambda: Tex(f"f(x) = {a_tracker.get_value():.1f}x^2", font_size=36)
            .to_corner(UR)
        )
        
        self.add(axes, axes_labels, graph, label)
        self.wait(1)
        
        # Change the parameter - graph updates automatically!
        # 改变参数 - 图形自动更新！
        self.play(a_tracker.animate.set_value(3), run_time=3)
        self.wait(0.5)
        
        self.play(a_tracker.animate.set_value(-2), run_time=3)
        self.wait(0.5)
        
        self.play(a_tracker.animate.set_value(0.5), run_time=3)
        self.wait(2)


# ============================================================================
# PART 4: 3D Scenes
# 第四部分：3D场景
# ============================================================================

class ThreeDIntro(ThreeDScene):
    """
    Basic 3D scene with camera controls
    带相机控制的基本3D场景
    """
    def construct(self):
        # Create 3D axes
        # 创建3D坐标轴
        axes = ThreeDAxes()
        
        # Set initial camera angle
        # 设置初始相机角度
        # phi: up/down angle (0-180 degrees) / 上下角度
        # theta: left/right rotation (0-360 degrees) / 左右旋转
        self.camera.frame.set_euler_angles(theta=-45 * DEGREES, phi=75 * DEGREES)
        
        # Create a 3D sphere
        # 创建3D球体
        sphere = Sphere(radius=2, resolution=(30, 30))
        sphere.set_color(BLUE)
        sphere.set_opacity(0.8)
        
        self.add(axes)
        self.play(ShowCreation(sphere), run_time=2)
        self.wait(1)
        
        # Rotate the camera around the object
        # 围绕对象旋转相机
        self.camera.frame.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
        self.wait(5)
        self.camera.frame.clear_updaters()
        
        self.wait(1)
        
        # Move camera to a different angle
        # 将相机移动到不同角度
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=-60 * DEGREES, 
                phi=60 * DEGREES
            ),
            run_time=3
        )
        self.wait(2)


class ThreeDParametricCurve(ThreeDScene):
    """
    3D parametric curve: a helix
    3D参数曲线：螺旋线
    """
    def construct(self):
        self.camera.frame.set_width(20)
        axes = ThreeDAxes()
        self.camera.frame.set_euler_angles(theta=-45 * DEGREES, phi=75 * DEGREES)
        
        # Parametric function: helix / 参数函数：螺旋
        helix = ParametricCurve(
            lambda t: np.array([
                2 * np.cos(t),
                2 * np.sin(t),
                t / 2
            ]),
            t_range=[0, 4 * TAU, 0.1],
            color=YELLOW
        )
        
        self.add(axes)
        
        # Draw the helix
        # 绘制螺旋
        self.play(ShowCreation(helix), run_time=4)
        
        # Rotate camera to see from different angles
        # 旋转相机从不同角度查看
        self.camera.frame.add_updater(lambda m, dt: m.increment_theta(0.1 * dt))
        self.wait(10)
        self.camera.frame.clear_updaters()


# ============================================================================
# PART 5: LaTeX and Mathematical Typesetting
# 第五部分：LaTeX和数学排版
# ============================================================================

class LatexBasics(Scene):
    """
    Basic LaTeX rendering in Manim
    Manim中的基本LaTeX渲染
    """
    def construct(self):
        # Simple equation / 简单方程
        eq1 = Tex(r"e^{i\pi} + 1 = 0", font_size=60)
        
        self.play(Write(eq1))
        self.wait(2)
        
        # Transform to a different equation
        # 转换到不同方程
        eq2 = Tex(
            r"\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}",
            font_size=60
        )
        
        # TransformMatchingShapes: better for equation transformations
        # TransformMatchingShapes：更适合方程转换
        self.play(TransformMatchingShapes(eq1, eq2))
        self.wait(2)
        
        # Matrix example / 矩阵示例
        matrix = Tex(
            r"\begin{bmatrix} a & b \\ c & d \end{bmatrix}",
            font_size=60
        )
        
        self.play(TransformMatchingShapes(eq2, matrix))
        self.wait(2)


class LatexColorAndParts(Scene):
    """
    Coloring specific parts of LaTeX
    为LaTeX的特定部分着色
    """
    def construct(self):
        # Equation with multiple parts
        # 具有多个部分的方程
        equation = Tex(
            r"x\,", r"=\,", r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            font_size=50
        )
        
        # Color different parts
        # 为不同部分着色
        equation[0].set_color(YELLOW)  # x
        equation[3].set_color(BLUE)     # The formula / 公式
        
        self.play(Write(equation))
        self.wait(2)
        
        # Highlight specific part
        # 突出显示特定部分
        self.play(equation[2].animate.scale(1.5).set_color(RED))
        self.wait(2)


# ============================================================================
# BEST PRACTICES SUMMARY
# 最佳实践总结
# ============================================================================

"""
KEY TAKEAWAYS / 关键要点:

1. Use .animate for smooth property interpolation
   使用 .animate 实现平滑的属性插值

2. Updaters are powerful but remember to clear_updaters()
   更新器很强大，但记得使用 clear_updaters()

3. ValueTracker is the best way to create parametric animations
   ValueTracker是创建参数化动画的最佳方式

4. VGroup helps organize multiple objects
   VGroup帮助组织多个对象

5. For 3D scenes, use ThreeDScene and set camera orientation
   对于3D场景，使用ThreeDScene并设置相机方向

6. Use raw strings (r"...") for LaTeX
   对LaTeX使用原始字符串

7. always_redraw() is great for dynamic objects
   always_redraw() 非常适合动态对象
"""
