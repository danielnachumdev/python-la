from Field import *
c = Complex.Complex


def test_containment():
    rf = RealField(Fields.R, 0, 1, 3)
    cf = ComplexField(Fields.C, c(0, 0), c(1, 0), 3)
    cf2 = ComplexField(Fields.C, c(0, 0), c(1, 0), 1)
    for _ in range(100):
        assert rf.random() in rf
        assert cf.random() in cf
        assert DefaultComplexField.random() in cf2


def test_is_field():
    assert Field.is_field(DefaultComplexField)
    assert Field.is_field(DefaultRealField)
    assert Field.is_field(DefaultRationalField)


def test_clone():
    r3 = RealField(Fields.R, 0, 1, 3)
    r21 = r3.classOfInstance(r3._name, r3._zero, r3._one, 2)
    r23 = r3.classOfInstance.create(r3._name, r3._zero, r3._one, 2)
    assert r21 == r23
