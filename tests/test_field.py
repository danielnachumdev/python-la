from python_la.la1.Field import ComplexField, Field, RationalField, RealField


def test_is_field():
    assert Field.is_field(ComplexField()) is True
    assert Field.is_field(RationalField()) is True
    assert Field.is_field(RealField()) is True
