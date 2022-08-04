from ... import VectorSpace, RealField, ComplexField, Vector


def test_containment():
    Vr3 = VectorSpace(RealField(3))
    Vc3 = VectorSpace(ComplexField(3))
    Vc1 = VectorSpace(ComplexField(1))
    for _ in range(100):
        assert Vr3.random() in Vr3
        assert Vc3.random() in Vc3
        assert Vector([ComplexField().random()], ComplexField(1)) in Vc1
