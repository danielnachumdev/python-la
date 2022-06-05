from Vector import Vector
from Field import Field, Fields
from Complex import Complex
from Span import Span
from Matrix import Matrix
from InnerProduct import StandardInnerProduct


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


if __name__ == '__main__':
    func2()
