import math

from python_la.la1.Complex import Complex
from python_la.la1.Complex import Complex as c

a = c(1, 1)
b = c(1, 0)


def test_r():
    assert Complex(1, 1).r == math.sqrt(2)


def test_theta():
    assert Complex(1, 1).theta == 45


def test___add__():
    assert a + 4 == c(5, 1)
    assert a + 4.56 == c(5.56, 1)
    assert a + a == a * 2
    assert a + (-a) == 0


def test___radd__():
    assert Complex.__radd__(a, 4) == c(5, 1)
    assert Complex.__radd__(a, 4.56) == c(5.56, 1)
    assert Complex.__radd__(a, a) == a * 2
    assert Complex.__radd__(a, -a) == 0


def test___mul__():
    assert a * 2 == c(2, 2)
    assert a * a == a ** 2


def test___rmul__():
    assert Complex.__rmul__(a, 2) == c(2, 2)
    assert Complex.__rmul__(a, a) == a ** 2


def test___neg__():
    assert -a == c(-1, -1)
    assert -c(-1, -1) == a
    assert -(-a) == a


def test___ne__():
    assert (a != b) is True
    assert (a != a) is False
    assert (b != b) is False


def test___truediv__():
    assert a / 2 == c(0.5, 0.5)


def test___rtruediv__():
    assert Complex.__rtruediv__(a, 1) == c(0.5, -0.5)


def test___pow__():
    assert a ** 2 == a * a
    assert a ** 4 == a * a * a * a


def test_conjugate():
    assert Complex(1, 1).conjugate == a - c(0, 2)
    assert Complex(1, 1).conjugate == c(1, -1)
    assert Complex(1, -1).conjugate == c(1, 1)
    assert Complex(1.3, 0).conjugate == c(1.3, 0)


def test_norm():
    assert Complex(2, 0).norm == 2
