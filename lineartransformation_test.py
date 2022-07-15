from LinearTransformation import *
from Field import Fields, RealField

R3 = RealField(Fields.R, 0, 1, 4)
R2 = RealField(Fields.R, 0, 1, 2)


def test_containment():
    def func(v, target_field):
        return Vector.Vector([v[0]+v[1], v[1]+v[2]], target_field)
    lt = LinearTransformation(R3, R2, func)
    v = R3.random()
    assert lt(v) in R2


def test_is_func_function():
    pass
