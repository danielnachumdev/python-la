from danielutils import TestFactory, Test
from python_la.la2.Calculable.PolynomialSimple import *


def test___init__():
    assert TestFactory(PolynomialSimple.__init__).add_tests([

    ])()


def test___str__():
    assert TestFactory(PolynomialSimple.__str__).add_tests([

    ])()


def test___add__():
    assert TestFactory(PolynomialSimple.__add__).add_tests([

    ])()


def test___radd__():
    assert TestFactory(PolynomialSimple.__radd__).add_tests([

    ])()


def test___sub__():
    assert TestFactory(PolynomialSimple.__sub__).add_tests([

    ])()


def test___rsub__():
    assert TestFactory(PolynomialSimple.__rsub__).add_tests([

    ])()


def test___neg__():
    assert TestFactory(PolynomialSimple.__neg__).add_tests([

    ])()


def test___mul__():
    assert TestFactory(PolynomialSimple.__mul__).add_tests([

    ])()


def test___rmul__():
    assert TestFactory(PolynomialSimple.__rmul__).add_tests([

    ])()


def test___truediv__():
    assert TestFactory(PolynomialSimple.__truediv__).add_tests([

    ])()


def test___rtruediv__():
    assert TestFactory(PolynomialSimple.__rtruediv__).add_tests([

    ])()


def test___pow__():
    assert TestFactory(PolynomialSimple.__pow__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(PolynomialSimple.__eq__).add_tests([

    ])()


def test___ne__():
    assert TestFactory(PolynomialSimple.__ne__).add_tests([

    ])()


def test___call__():
    assert TestFactory(PolynomialSimple.__call__).add_tests([

    ])()


def test___len__():
    assert TestFactory(PolynomialSimple.__len__).add_tests([

    ])()


def test_from_string():
    assert TestFactory(PolynomialSimple.from_string).add_tests([

    ])()


def test_roots():
    def inner(): return PolynomialSimple().roots
    assert TestFactory(inner).add_tests([

    ])()


def test_degree():
    def inner(): return PolynomialSimple().degree
    assert TestFactory(inner).add_tests([

    ])()


def test_derivative():
    def inner(): return PolynomialSimple().derivative
    assert TestFactory(inner).add_tests([

    ])()


def test_integral():
    def inner(): return PolynomialSimple().integral
    assert TestFactory(inner).add_tests([

    ])()


def test_solve():
    assert TestFactory(PolynomialSimple.solve).add_tests([

    ])()


def test_gcd_with():
    assert TestFactory(PolynomialSimple.gcd_with).add_tests([

    ])()
