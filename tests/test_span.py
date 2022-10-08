from danielutils import TestFactory, Test
from python_la.la1.Span import *


def test___init__():
    assert TestFactory(Span.__init__).add_tests([

    ])()


def test___str__():
    assert TestFactory(Span.__str__).add_tests([

    ])()


def test___add__():
    assert TestFactory(Span.__add__).add_tests([

    ])()


def test___getitem__():
    assert TestFactory(Span.__getitem__).add_tests([

    ])()


def test___iter__():
    assert TestFactory(Span.__iter__).add_tests([

    ])()


def test___len__():
    assert TestFactory(Span.__len__).add_tests([

    ])()


def test___contains__():
    assert TestFactory(Span.__contains__).add_tests([

    ])()


def test___hash__():
    assert TestFactory(Span.__hash__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(Span.__eq__).add_tests([

    ])()


def test_are_same_span():
    assert TestFactory(Span.are_same_span).add_tests([

    ])()


def test_span_field():
    assert TestFactory(Span.span_field).add_tests([

    ])()


def test_basis():
    def inner(): return Span().basis
    assert TestFactory(inner).add_tests([

    ])()


def test_dim():
    def inner(): return Span().dim
    assert TestFactory(inner).add_tests([

    ])()


def test_has_lineary_dependency():
    def inner(): return Span().has_lineary_dependency
    assert TestFactory(inner).add_tests([

    ])()


def test_remove():
    assert TestFactory(Span.remove).add_tests([

    ])()


def test_remove_at():
    assert TestFactory(Span.remove_at).add_tests([

    ])()


def test_contains():
    assert TestFactory(Span.contains).add_tests([

    ])()


def test_to_orthonormal():
    assert TestFactory(Span.to_orthonormal).add_tests([

    ])()


def test_projection_of():
    assert TestFactory(Span.projection_of).add_tests([

    ])()


def test_random():
    assert TestFactory(Span.random).add_tests([

    ])()
