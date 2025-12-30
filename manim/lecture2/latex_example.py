from manim import *
class EulerFormula(Scene):
    def construct(self):
        text=MathTex(r"e^{i\pi} + 1 = 0")
        self.add(text)


class NavierStokesEquation(Scene):
    def construct(self):
        text=MathTex(r"\nabla \cdot (\rho \mathbf{u} \cdot \nabla \mathbf{u}) = 0")
        self.add(text)

class LagrangianEquation(Scene):
    def construct(self):
        text=MathTex(r"\frac{d}{dt} \int_{\Omega} \rho \mathbf{u} \cdot \mathbf{u} \, dV = 0")
        self.add(text)

class Matrix(Scene):
    def construct(self):
        matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        self.add(matrix)
