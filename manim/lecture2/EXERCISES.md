# Lecture 2: Practice Exercises
# 第二讲：练习题

## Instructions / 说明

Complete these exercises to reinforce your understanding of Lecture 2 concepts. Start with the beginner exercises and progress to advanced ones.

完成这些练习以巩固你对第二讲概念的理解。从初学者练习开始，逐步进阶到高级练习。

**Render your solutions using:**
```bash
manimgl your_file.py SceneName -p -qm
```

---

## Beginner Exercises / 初级练习

### Exercise 1: Animate Syntax Practice
**Goal:** Create an animation using the `.animate` syntax
**目标：** 使用 `.animate` 语法创建动画

**Requirements / 要求:**
1. Create 3 different shapes (circle, square, triangle)
2. Arrange them in a row using VGroup
3. Animate each shape to shift UP by 2 units
4. Change their colors during the animation
5. All animations should happen simultaneously

**Hints:**
- Use `VGroup` to organize shapes
- Use `.set_color_by_gradient()` for color changes
- Chain transformations with `.animate.shift().set_color()`

**Expected Output:** Three shapes moving up together while changing colors

---

### Exercise 2: Basic Updater
**Goal:** Create a label that follows a moving object
**目标：** 创建跟随移动对象的标签

**Requirements / 要求:**
1. Create a circle with a text label showing "Following"
2. Add an updater so the label always stays to the right of the circle
3. Move the circle in a square path (up, right, down, left)
4. The label should follow the entire time

**Hints:**
- Use `label.add_updater(lambda m: m.next_to(circle, RIGHT))`
- Create a square path using 4 separate `.play()` commands
- Don't forget to `clear_updaters()` at the end

**Expected Output:** A circle moving in a square with a label following it

---

### Exercise 3: Simple ValueTracker
**Goal:** Use ValueTracker to control an animation
**目标：** 使用ValueTracker控制动画

**Requirements / 要求:**
1. Create a ValueTracker starting at 0
2. Create a circle whose radius depends on the tracker value
3. Use `always_redraw()` to update the circle
4. Animate the tracker from 0 to 3 and back to 1

**Hints:**
- `radius = tracker.get_value()`
- Use `always_redraw(lambda: Circle(radius=tracker.get_value()))`
- Don't forget to add the tracker to the scene even though it's invisible

**Expected Output:** A circle that grows and shrinks smoothly

---

## Intermediate Exercises / 中级练习

### Exercise 4: Multi-Object Updater System
**Goal:** Create multiple objects with interconnected updaters
**目标：** 创建具有互连更新器的多个对象

**Requirements / 要求:**
1. Create a line that rotates around the origin
2. Create 5 dots positioned along the line
3. Add updaters so the dots always stay on the rotating line
4. Color each dot differently
5. Rotate the line for one full rotation

**Hints:**
- Use `rotate()` with updaters
- Position dots using `line.point_from_proportion(0.2 * i)` for dot i
- Track rotation angle with self.time or a ValueTracker

**Expected Output:** Colored dots rotating in a line formation

---

### Exercise 5: Conditional Updater
**Goal:** Create an updater that changes behavior based on conditions
**目标：** 创建根据条件改变行为的更新器

**Requirements / 要求:**
1. Create a horizontal line at y=0
2. Create a moving circle
3. Add an updater that makes the circle:
   - Blue when above the line
   - Red when below the line
4. Move the circle up and down multiple times

**Hints:**
```python
def color_updater(mob):
    if mob.get_center()[1] > 0:
        mob.set_color(BLUE)
    else:
        mob.set_color(RED)
```

**Expected Output:** A circle changing color as it crosses a line

---

### Exercise 6: ValueTracker with Graph
**Goal:** Animate a function using ValueTracker
**目标：** 使用ValueTracker动画化函数

**Requirements / 要求:**
1. Create axes from -5 to 5 for both x and y
2. Plot the function f(x) = a·sin(x) where a is controlled by a ValueTracker
3. Add a label showing the current value of a
4. Animate a from 1 to 3 to -2 to 1

**Hints:**
- Use `always_redraw()` for the graph
- Use `axes.plot(lambda x: a_tracker.get_value() * np.sin(x))`
- Update label with `DecimalNumber` or `MathTex`

**Expected Output:** A sine wave that grows and shrinks with a changing label

---

## Advanced Exercises / 高级练习

### Exercise 7: Solar System Simulation
**Goal:** Create a mini solar system with updaters
**目标：** 使用更新器创建小型太阳系

**Requirements / 要求:**
1. Create a "sun" at the center (yellow circle)
2. Create 3 "planets" that orbit the sun at different speeds
3. Each planet should have a different radius orbit
4. Use updaters for the orbiting motion
5. Add a "moon" that orbits one of the planets

**Hints:**
```python
def planet_updater(mob, dt):
    self.time += dt
    angle = self.time * speed
    mob.move_to(sun.get_center() + radius * np.array([np.cos(angle), np.sin(angle), 0]))
```

**Expected Output:** A sun with orbiting planets and a moon

---

### Exercise 8: Interactive Function Grapher
**Goal:** Create a scene that shows how changing parameters affects a function
**目标：** 创建显示更改参数如何影响函数的场景

**Requirements / 要求:**
1. Create a quadratic function: f(x) = ax² + bx + c
2. Use THREE ValueTrackers for a, b, and c
3. Use `always_redraw()` to update the graph
4. Show labels for all three parameters
5. Animate each parameter changing one at a time
6. Show how the parabola shifts and changes shape

**Hints:**
- Create 3 separate trackers
- Label format: `MathTex(f"f(x) = {a:.1f}x^2 + {b:.1f}x + {c:.1f}")`
- Use `always_redraw()` for both graph and label

**Expected Output:** A parabola that transforms as parameters change with equation displayed

---

### Exercise 9: 3D Rotating Graph
**Goal:** Create a rotating 3D surface
**目标：** 创建旋转的3D曲面

**Requirements / 要求:**
1. Use `ThreeDScene`
2. Create 3D axes
3. Plot a 3D surface: z = sin(sqrt(x² + y²)) (a ripple effect)
4. Set camera orientation
5. Rotate the camera around the surface for 10 seconds
6. Add proper labels

**Hints:**
```python
surface = Surface(
    lambda u, v: np.array([u, v, np.sin(np.sqrt(u**2 + v**2))]),
    u_range=[-3, 3],
    v_range=[-3, 3]
)
```

**Expected Output:** A beautiful ripple surface rotating in 3D

---

### Exercise 10: Complex Animation Sequence
**Goal:** Combine multiple concepts into one cohesive animation
**目标：** 将多个概念组合成一个连贯的动画

**Requirements / 要求:**
1. Start with a mathematical equation in LaTeX
2. Transform the equation into a graph
3. Add a pointer that traces along the graph using ValueTracker
4. Show the (x, y) coordinates as the pointer moves
5. Use updaters to keep labels synchronized
6. End with a zoom into an interesting feature of the graph

**This is a CAPSTONE exercise - it combines:**
- LaTeX rendering
- Graph plotting
- ValueTrackers
- Updaters
- Camera movements

**Expected Output:** A professional-looking mathematical demonstration

---

## Bonus Challenges / 奖励挑战

### Challenge 1: Pendulum Simulation
Create a realistic pendulum using updaters and physics equations.

### Challenge 2: Fourier Series Visualization
Use ValueTracker and updaters to show how Fourier series approximate a square wave.

### Challenge 3: Matrix Transformation Visualizer
Create a 2D grid that transforms based on matrix multiplication, showing eigenvalues.

---

## Solutions / 解决方案

Solutions will be provided in `lecture2/solutions/` folder. Try to complete the exercises on your own first!

解决方案将在 `lecture2/solutions/` 文件夹中提供。先尝试自己完成练习！

---

## Evaluation Rubric / 评估标准

For each exercise, check:
- ✅ Does it run without errors? / 是否无错误运行？
- ✅ Does it produce the expected visual output? / 是否产生预期的视觉输出？
- ✅ Is the code well-commented? / 代码是否有良好的注释？
- ✅ Are updaters properly cleared? / 更新器是否正确清除？
- ✅ Is the timing/pacing good? / 时间/节奏是否良好？

---

## Additional Resources / 额外资源

- Manim Documentation: https://3b1b.github.io/manim/
- Manim Community Examples: https://docs.manim.community/en/stable/examples.html
- Stack Overflow Manim Tag: Search for common issues
- Discord: Join the Manim community for help

Happy animating! / 祝动画愉快！
