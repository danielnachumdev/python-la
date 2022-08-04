from ...la1 import Span, Vector


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
