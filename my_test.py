from Vector import Vector
from Field import Field, Fields, RationalField, RealField
from Complex import Complex
from Span import Span
from Matrix import Matrix
from InnerProduct import InnerProduct, StandardInnerProduct
import math

PI = math.pi


def func1():
    m = Matrix([
        [2, 2],
        [0, 2]
    ], [2, 4])
    print(m)
    print(m.solve())

    m = Matrix([
        [2, 0, 4],
        [0, 0, 0],
        [1, 2, 0],
    ], [0, 0, 0])
    print(m.solve())


def func2():
    v1 = Vector([-2, 1, 0, 0])
    v2 = Vector([-3, 0, 1, 0])
    v3 = Vector([-4, 0, 0, 1])
    s = Span([v1, v2, v3])
    print(s.toOrthonormal())


def func3():
    assert(Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]]).determinant == 1)
    assert(Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).determinant == 0)


def func4():
    def f():
        v = Vector([2, 4, 6, 8])
        # s = Span([
        #     Vector([1, 0, -1, 0]),
        #     Vector([1, 1, -1, -1])
        # ])
        s = Span([
            Vector([1, 0, -1, 0]),
            Vector([1, 1, 0, 0]),
            Vector([0, 0, 1, 1])
        ])
        print(v.projection_onto(s))

    def g():
        # def func(v1: Vector, v2: Vector) -> float:
        #     x1 = v1[0]
        #     y1 = v1[1]
        #     z1 = v1[2]
        #     x2 = v2[0]
        #     y2 = v2[1]
        #     z2 = v2[2]
        #     return x1*x2+PI/2*z1*z2+0.5*x1*y2+0.5*x2*y1+42*y1*y2

        def generator(zero: bool = False) -> Vector:
            return Vector.random(3, 0 if zero else None)

        def func(v1: Vector, v2: Vector) -> float:
            x1 = v1[0]
            y1 = v1[1]
            z1 = v1[2]
            x2 = v2[0]
            y2 = v2[1]
            z2 = v2[2]
            return x1*x2+PI/2*z1*z2

        print(InnerProduct.isInnerProduct(func, generator))

    f()


def t():
    print(RealField(Fields.R, 3).random() in RealField(Fields.R, 3))


if __name__ == '__main__':
    print(Span([Vector([2, -1, 0, 1]), Vector([0, -0.5, 1, 0])]).toOrthonormal())
