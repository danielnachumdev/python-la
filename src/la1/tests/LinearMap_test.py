from ...la1 import RealField, Vector, LinearMap

R3 = RealField(4)
R2 = RealField(2)


def test_containment():
    def func(v, target_field):
        return Vector([v[0]+v[1], v[1]+v[2]], target_field)
    lt = LinearMap(R3, R2, func)
    v = R3.random()
    assert lt(v) in R2
