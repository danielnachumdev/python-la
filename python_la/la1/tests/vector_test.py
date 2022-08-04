from ...la1 import Vector, Complex as c


def test_sum():
    assert sum(Vector([0, 0])) == 0
    assert sum(Vector([1, 2, 3, 4])) == 10


def test_conjugate():
    assert Vector([0, 1, 2, 3]).conjugate == Vector([0, 1, 2, 3])
    assert Vector([c(1, 1), c(0, 2), c(1, 0)]).conjugate == Vector(
        [c(1, -1), c(0, -2), c(1, 0)])
