from manimlib import *
class EulerFormula(Scene):
    def construct(self):
        text=Tex(r"e^{i\pi} + 1 = 0")
        self.add(text)
        self.wait()


class NavierStokesEquation(Scene):
    def construct(self):
        text=Tex(r"\nabla \cdot (\rho \mathbf{u} \cdot \nabla \mathbf{u}) = 0")
        self.add(text)

class LagrangianEquation(Scene):
    def construct(self):
        text=Tex(r"\frac{d}{dt} \frac{\partial \mathcal{L}}{\partial \dot q}-\frac{\partial \mathcal{L}}{\partial q} = 0")
        self.add(text)

class MatrixExample(Scene):
    def construct(self):
        matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        self.add(matrix)
        self.wait()

class Fraction(Scene):
    def construct(self):
        fraction = Tex(r"{x^3+1\over x+1}=x^2-x+1")
        self.add(fraction)

class SpecialSymbol(Scene):
    def construct(self):
        text=Tex(r"\infty")
        self.add(text)
