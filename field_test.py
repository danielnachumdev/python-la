import Field


def test_containment():
    assert Field.RealField(Field.Fields.R, 3).random(
    ) in Field.RealField(Field.Fields.R, 3)
    assert Field.ComplexField(Field.Fields.C, 3).random(
    ) in Field.ComplexField(Field.Fields.C, 3)
    assert Field.DefaultComplexField.random() in Field.ComplexField(Field.Fields.C, 1)
