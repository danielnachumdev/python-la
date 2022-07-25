from LinearMap import *
from Field import Fields, RealField

R3 = RealField(4)
R2 = RealField(2)


def test_containment():
    def func(v, target_field):
        return Vector.Vector([v[0]+v[1], v[1]+v[2]], target_field)
    lt = LinearMap(R3, R2, func)
    v = R3.random()
    assert lt(v) in R2


def test_with_plynomial():
    from Vector import Vector
    field = R2

    def func(v, target_field):
        return Vector([0, v[0]], target_field)
    lt = LinearMap(field, field, func)
    from SimplePolynomial import SimplePolynomial
    v = field.random()
    # assert Polynomial.fromString("x^2")(lt)(v) == Vector([0, 0], field)
    assert SimplePolynomial.fromString("x^2+1")(lt)(v) == v
    assert SimplePolynomial.fromString(
        "x+1")(lt)(v) == Vector([v[0], sum(v)], field)
