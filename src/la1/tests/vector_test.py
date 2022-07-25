from ..Vector import *


def test_sum():
    assert sum(Vector([0, 0])) == 0
    assert sum(Vector([1, 2, 3, 4])) == 10


def test_equality():
    assert Vector([0, 0]) == [0, 0]


def test_adjoint():
    assert Vector([0, 1, 2, 3]).adjoint() == Vector([0, 1, 2, 3])
    from ..Complex import Complex as c
    assert Vector([c(1, 1), c(0, 2), c(1, 0)]) == Vector(
        [c(1, -1), c(0, -2), c(1, 0)])
