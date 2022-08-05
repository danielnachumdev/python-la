from ...la1 import RealField, Vector, LinearMap, VectorSpace, Matrix

R3 = RealField(4)
R2 = RealField(2)
T = LinearMap.from_fields(R2, R2, lambda v: Vector([v[1], v[0]], R2))


def test_containment():
    lm = LinearMap.from_fields(
        R3, R2, lambda v: Vector([v[0]+v[1], v[1]+v[2]], R2))
    v = VectorSpace(R3).random()
    assert lm(v) in VectorSpace(R2)


def test_power():

    assert T.to_matrix() == Matrix([[0, 1], [1, 0]])
    assert (T ** 10).to_matrix() == Matrix.identity(2)


def test_addition():
    assert (LinearMap.from_fields(R2, R2, lambda v: v) +
            T).to_matrix() == Matrix([[1, 1], [1, 1]])


def test_subtraction():
    assert (LinearMap.from_fields(R2, R2, lambda v: v) -
            T).to_matrix() == Matrix([[1, -1], [1, -1]])


def test_multiplication():
    assert (LinearMap.from_fields(R2, R2, lambda v: v) *
            T) == (T * LinearMap.from_fields(R2, R2, lambda v: v)) == T
    v = VectorSpace(RealField(2)).random()
    assert T(v) == T.to_matrix() * v
