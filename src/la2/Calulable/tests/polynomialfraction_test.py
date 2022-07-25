import random
from ....la1 import Complex as c
from ....la2 import PolynomialFraction as pf

id = pf([1], [1])
times_two = pf([2], [1])
plus_5 = pf([1, 5], [1, 0])
x = random.uniform(-100, 100)


# def test_from_string():
#     assert Expression.fromString("x^2")(x) == x**2
#     assert Expression.fromString("x^2+5")(x) == x**2+5
#     assert Expression.fromString("(x+1)^2")(x) == (x+1)**2


def test_addition():
    assert (id+5)(x) == x+5 == (5+id)(x)
    assert (id+id)(x) == 2*x == 2*id(x)


def test_negation():
    assert (-id)(x) == -x == -id(x)


def test_trudiv():
    assert (id/id)(x) == 1
    assert (-id/id)(x) == -1 == (id/-id)(x)


def test_rtruediv():
    assert (1/id)(x) == 1/x == 1/((id/1)(x))
    try:
        (1/id)(0)
        assert False
    except ZeroDivisionError:
        pass


def test_multiplication():
    assert 5*id(x) == (5*id)(x)


def test_pow():
    assert x**2 == id(x)**2 == (id*id)(x) == (id**2)(x)


# def test_rpow():
#     assert (2**id)(x) == 2**x


def test_expression_ception():
    assert id(plus_5(id(id(times_two(plus_5(5)))))) == id(5)**2


def test_equality():
    assert id == id
    assert id(id) == id
    assert plus_5(id) == id(plus_5)
    assert times_two(plus_5) == plus_5+plus_5


# def test_derivative():
#     assert Expression.fromString("x^2").derivetive(x) == 2*x


# def test_antiderivative():
#     assert almost_equal(Expression.fromString("x^2").antiderivative(x), x**3/3)
