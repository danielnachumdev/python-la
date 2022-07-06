import Field

fields = Field.Fields
real = Field.RealField
complex = Field.ComplexField


def test_containment():
    assert real(fields.R, 3).random() in real(fields.R, 3)
    assert complex(fields.C, 3).random() in complex(fields.C, 3)
    assert Field.DefaultComplexField.random() in complex(fields.C, 1)
