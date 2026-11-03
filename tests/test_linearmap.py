from python_la import Matrix
from python_la.la1 import RealField, Vector
from python_la.la1.LinearMap import LinearMap

R2 = RealField(2)
T = LinearMap.from_fields(R2, R2, lambda v: Vector([v[1], v[0]], R2))


def test___add__():
    assert T + T == T * 2


def test___sub__():
    A = LinearMap.from_matrix(Matrix([[1, -1], [-1, 1]]))
    identity_like = LinearMap.from_fields(
        R2, R2, lambda v: Vector([v[0], v[1]], R2)
    )
    assert identity_like - T == A


def test___mul__():
    T2 = LinearMap.from_fields(R2, R2, lambda v: v)
    assert T * 1 == T
    assert T * 0 == T - T
    assert T2 * T == T * T2


def test___pow__():
    assert T ** 11 == T
    assert T ** 1 == T
