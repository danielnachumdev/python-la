from Field import *
c = Complex.Complex


def test_containment():
    rf = RealField(3)
    cf = ComplexField(3)
    cf2 = ComplexField(1)
    for _ in range(100):
        assert rf.random() in rf
        assert cf.random() in cf
        assert DefaultComplexField.random() in cf2


def test_is_field():
    assert Field.is_field(DefaultComplexField)
    assert Field.is_field(DefaultRealField)
    assert Field.is_field(DefaultRationalField)


def test_clone():
    r3 = RealField(3)
    r21 = r3.classOfInstance(2)
    r23 = r3.classOfInstance.create(r3._name, 2)
    assert r21 == r23
