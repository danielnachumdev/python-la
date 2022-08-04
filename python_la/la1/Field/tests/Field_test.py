from ... import Field, RealField, DefaultRealField, DefaultComplexField, DefaultRationalField


def test_is_field():
    assert Field.is_field(DefaultComplexField)
    assert Field.is_field(DefaultRealField)
    assert Field.is_field(DefaultRationalField)
