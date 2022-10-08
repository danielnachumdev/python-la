from danielutils import TestFactory, Test
from python_la.la1.Complex import *
from python_la.la1.Complex import Complex as c
a = c(1, 1)
b = c(1, 0)


def test_from_polar():
    assert TestFactory(Complex.from_polar).add_tests([

    ])()


def test_from_polar_radians():
    assert TestFactory(Complex.from_polar_radians).add_tests([

    ])()


def test___init__():
    assert TestFactory(Complex.__init__).add_tests([

    ])()


def test_r():
    import math
    def inner(r, i): return Complex(r, i).r
    assert TestFactory(inner).add_tests([
        Test((1, 1), math.sqrt(2)),
    ])()


def test_theta_radians():
    def inner(r, i): return Complex(r, i).theta_radians
    assert TestFactory(inner).add_tests([

    ])()


def test_theta():
    def inner(r, i): return Complex(r, i).theta
    assert TestFactory(inner).add_tests([
        Test((1, 1), 45),
    ])()


def test___str__():
    assert TestFactory(Complex.__str__).add_tests([

    ])()


def test___repr__():
    assert TestFactory(Complex.__repr__).add_tests([

    ])()


def test___add__():
    assert TestFactory(Complex.__add__).add_tests([
        Test((a, 4), c(5, 1)),
        Test((a, 4.56), c(5.56, 1)),
        Test((a, a), a*2),
        Test((a, -a), 0),
        # Test((),),
    ])()


def test___radd__():
    assert TestFactory(Complex.__radd__).add_tests([
        Test((a, 4), c(5, 1)),
        Test((a, 4.56), c(5.56, 1)),
        Test((a, a), a*2),
        Test((a, -a), 0),
    ])()


def test___mul__():
    assert TestFactory(Complex.__mul__).add_tests([
        Test((a, 2), c(2, 2)),
        Test((a, a), a ** 2),
    ])()


def test___rmul__():
    assert TestFactory(Complex.__rmul__).add_tests([
        Test((a, 2), c(2, 2)),
        Test((a, a), a ** 2),
    ])()


def test___neg__():
    assert TestFactory(Complex.__neg__).add_tests([
        Test((a), c(-1, -1)),
        Test((c(-1, -1)), a),
        Test((-a), a),
    ])()


def test___sub__():
    assert TestFactory(Complex.__sub__).add_tests([

    ])()


def test___rsub__():
    assert TestFactory(Complex.__rsub__).add_tests([

    ])()


def test___abs__():
    assert TestFactory(Complex.__abs__).add_tests([

    ])()


def test___eq__():
    assert TestFactory(Complex.__eq__).add_tests([

    ])()


def test___ne__():
    assert TestFactory(Complex.__ne__).add_tests([
        Test((a, b), True),
        Test((a, a), False),
        Test((b, b), False),
    ])()


def test___truediv__():
    assert TestFactory(Complex.__truediv__).add_tests([
        Test((a, 2), c(0.5, 0.5)),
    ])()


def test___rtruediv__():
    assert TestFactory(Complex.__rtruediv__).add_tests([
        Test((a, 1), c(0.5, -0.5)),
    ])()


def test___pow__():
    assert TestFactory(Complex.__pow__).add_tests([
        Test((a, 2), a*a),
        Test((a, 4), a*a*a*a),
    ])()


def test___rpow__():
    assert TestFactory(Complex.__rpow__).add_tests([

    ])()


def test_conjugate():
    def inner(r, i): return Complex(r, i).conjugate
    assert TestFactory(inner).add_tests([
        Test((1, 1), a-c(0, 2)),
        Test((1, 1), c(1, -1)),
        Test((1, -1), c(1, 1)),
        Test((1.3, 0), c(1.3, 0)),
    ])()


def test_norm():
    def inner(r, i): return Complex(r, i).norm
    assert TestFactory(inner).add_tests([
        Test((2, 0), 2),
    ])()


def test_random():
    assert TestFactory(Complex.random).add_tests([

    ])()
