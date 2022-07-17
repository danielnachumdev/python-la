from Vector import *


def test_sum():
    assert sum(Vector([0, 0])) == 0
    assert sum(Vector([1, 2, 3, 4])) == 10


def test_equality():
    assert Vector([0, 0]) == [0, 0]
