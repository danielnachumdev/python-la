# import sys
# sys.path.insert(1,
#                 "C:\\Users\\danie\\OneDrive\\Desktop\\Code\\VCS\\linear-algebra\\LinearAlgebra")
from Complex import Complex as c

a = c(1, 1)
b = c(1, 0)


def test_add_RC():
    assert (4 + a).real == 5, "addition with int from the left is not defined"
    assert (4.56 + a).real == 5.56, "addition with int from the left is not defined"


def test_add_CR():
    assert (a + 4).real == 5, "addition with float from the right is not defined"
    assert (c(1.32, 1) +
            4).real == 5.32, "addition with float from the right is not defined"


def test_add_CC():
    assert a+2*a == 3*a
    assert c(1, 0)+c(0, 1) == a
    assert c(-1.5, 0)+c(0, 1.5) == c(-1.5, 1.5)


def test_mul_RC():
    assert 5*a == c(5, 5)


def test_mul_CR():
    assert a*5 == c(5, 5)


def test_mul_CC():
    assert a*a == c(0, 2), "(1+i)(1+i) != 2i"
    assert c(3, 5)*c(5, 3) == c(0, 34), "(3+5i)(5+3i) != 34i"


def test_neg():
    assert -a == c(-1, -1)
    assert -c(-4, -3) == c(4, 3)
    assert -(-c(1, 0)) == c(1, 0)


def test_conjugate():
    assert a.conjugate == a-c(0, 2)
    assert a.conjugate.conjugate == a


def test_inequality():
    assert a is not b
    assert a != b


def test_norm():
    assert (2*b).norm == 4


def test_division():
    assert 1/a == c(1/2, -1/2)
    assert a/2 == c(0.5, 0.5)
