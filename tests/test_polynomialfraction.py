import pytest

from python_la.la2.Calculable.PolynomialFraction import PolynomialFraction
from python_la.la2.Calculable.PolynomialSimple import PolynomialSimple


def test___init__():
    pass


def test___add__():
    pass


def test___radd__():
    pass


def test___sub__():
    pass


def test___rsub__():
    pass


def test___neg__():
    pass


def test___mul__():
    pass


def test___rmul__():
    pass


def test___truediv__():
    pass


def test___rtruediv__():
    pass


def test___eq__():
    pass


def test___ne__():
    pass


def test___pow__():
    pass


def test___rpow__():
    pass


def test___str__():
    pass


def test___call__():
    pass


def test_from_string():
    num_only = PolynomialFraction.from_string("x^2+1")
    assert num_only(2) == 5
    assert num_only.denominator == PolynomialSimple([1], [0])

    frac = PolynomialFraction.from_string("(x+1)/(x-1)")
    assert frac(3) == 2
    assert frac == PolynomialFraction.from_polynomials(
        PolynomialSimple.from_string("x+1"),
        PolynomialSimple.from_string("x-1"),
    )

    bare = PolynomialFraction.from_string("x^2+5/x+1")
    assert bare == PolynomialFraction.from_polynomials(
        PolynomialSimple.from_string("x^2+5"),
        PolynomialSimple.from_string("x+1"),
    )


def test_from_polynomials():
    pass


def test_from_primitive():
    pass


def test_destructure():
    pass


def test_simplify():
    with pytest.raises(NotImplementedError):
        PolynomialFraction.from_string("x/x").simplify()
