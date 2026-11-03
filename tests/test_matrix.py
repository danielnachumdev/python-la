import pytest
from python_la import RealField
from python_la.la1.Matrix import Matrix

m1 = Matrix([
    [2, 0, -2, -2],
    [0, 0, 1, 1],
    [0, -2, 3, 1],
    [0, 2, -3, -1],
])

m_invertible = Matrix([
    [1, 2, 3],
    [0, 1, 4],
    [5, 6, 0],
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


def test_gaussian_elimination():
    # m1 is singular (row4 == -row3); RREF is not I4
    assert m1.determinant == 0
    assert m1.gaussian_elimination() == Matrix([
        [1, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 1, 1],
        [0, 0, 0, 0],
    ])
    assert m_invertible.gaussian_elimination() == Matrix.identity(3)


def test_adjugate():
    a = Matrix([[1, 2], [3, 4]])
    adj = a.adjugate
    assert adj == Matrix([[4, -2], [-3, 1]])
    assert a * adj == a.determinant * Matrix.identity(2)

    singular = Matrix([[1, 1], [2, 2]])
    assert singular * singular.adjugate == Matrix([[0, 0], [0, 0]])

    with pytest.raises(ValueError):
        _ = Matrix([[1, 2, 3], [4, 5, 6]]).adjugate


def test_is_nilpotent():
    assert Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]]).is_nilpotent is True
    assert Matrix([[0, 1], [0, 0]]).is_nilpotent is True
    assert Matrix.identity(2).is_nilpotent is False
    assert Matrix([[1, 1], [0, 1]]).is_nilpotent is False
    assert Matrix([[0, 1, 2], [0, 0, 3]]).is_nilpotent is False
