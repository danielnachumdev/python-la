from ...la1 import Span, Vector, RealField
v1 = Vector([1, 0, 0])
v2 = Vector([1, 1, 0])
v3 = Vector([1, 1, 1])


def test_are_same_span():
    assert Span.are_same_span(
        Span([
            Vector([1, 1, 0]),
            Vector([1, 2, 0]),
        ]),
        Span([
            Vector([2, 1, 0]),
            Vector([0, 1, 0]),
        ]))
    assert Span.are_same_span(
        Span([
            Vector([1, 1]),
            Vector([1, 2]),
        ]),
        Span([
            Vector([2, 1]),
            Vector([0, 1]),
        ]))
    assert not Span.are_same_span(
        Span([
            Vector([1, 1]),
            Vector([1, 1]),
        ]),
        Span([
            Vector([2, 1]),
            Vector([0, 1]),
        ]))


def test_add():
    assert Span.are_same_span(Span([v1, v2])+Span([v3]),
                              Span.span_field(RealField(3)))


def test_sub():
    pass


def test_getitem():
    pass


def test_iter():
    pass


def test__contains__():
    pass


def test_contains():
    pass


def test_eq():
    pass


def test_to_orthonormal():
    pass


def test_projection_of():
    pass


def test_has_linear_dependency():
    pass


def test_dim():
    pass


def test_basis():
    pass
