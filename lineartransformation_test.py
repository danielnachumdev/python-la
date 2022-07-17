from LinearTransformation import *
from Field import Fields, RealField

R3 = RealField(4)
R2 = RealField(2)


def test_containment():
    def func(v, target_field):
        return Vector.Vector([v[0]+v[1], v[1]+v[2]], target_field)
    lt = LinearTransformation(R3, R2, func)
    v = R3.random()
    assert lt(v) in R2


def test_is_func_function():
    pass


def test_with_plynomial():
    field = R2

    def func(v, target_field):
        return Vector.Vector([0, v[0]], target_field)
    lt = LinearTransformation(field, field, func)
    from Polynomial import Polynomial
    v = field.random()
    assert Polynomial.fromString("x^2")(lt)(v) == Vector([0, 0])


test_with_plynomial()
