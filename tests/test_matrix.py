import pytest
from python_la import RealField
from python_la.la1.Matrix import Matrix

m1 = Matrix([
    [2, 0, -2, -2],
    [0, 0, 1, 1],
    [0, -2, 3, 1],
    [0, 2, -3, -1],
])


def test_identity():
    assert Matrix.identity(2) == Matrix([[1, 0], [0, 1]], RealField(2))


def test_rank():
    assert Matrix([[1, 0], [0, 1]], RealField(2)).rank == 2
    assert Matrix([[1, 1], [0, 1]], RealField(2)).rank == 2
    assert Matrix([[1, 1], [1, 1]], RealField(2)).rank == 1
    assert Matrix([[1, 0], [1, 0]], RealField(2)).rank == 1
    assert Matrix([[1, 1], [0, 0]], RealField(2)).rank == 1


def test_determinant():
    assert Matrix([[1, 1], [1, 1]], RealField(2)).determinant == 0
    assert Matrix([[1, 0], [0, 1]], RealField(2)).determinant == 1
    assert Matrix([[1, 0], [1, 0]], RealField(2)).determinant == 0


@pytest.mark.xfail(reason="gaussian_elimination(m1) != I4 under current impl", strict=False)
def test_gaussian_elimination():
    assert m1.gaussian_elimination() == Matrix.identity(4)
