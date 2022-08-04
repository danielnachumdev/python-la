from ... import Field, RealField, ComplexField, RationalField


def test_is_field():
    assert Field.is_field(ComplexField())
    assert Field.is_field(RealField())
    assert Field.is_field(RationalField())
