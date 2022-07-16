from Expression import *
from Complex import Complex as c
import random
from utils import almost_equal
id = Expression(1, 1, 0, lambda x: x)
x = random.uniform(-100, 100)


def test_call():
    assert Expression(c(1, 1), 2)(c(1, 1)) == c(-2, 2)


def test_from_string():
    assert Expression.fromString("x^2")(x) == x**2
    assert Expression.fromString("x^2+5")(x) == x**2+5
    assert Expression.fromString("(x+1)^2")(x) == (x+1)**2


def test_from_func():
    assert Expression.fromFunction(lambda x: x**2)(x) == x**2


def test_addition():
    assert (id+5)(x) == x+5 == (5+id)(x)
    assert (id+id)(x) == 2*x == 2*id(x)


def test_negation():
    assert (-id)(x) == -x == -id(x)


def test_trudiv():
    assert (id/id)(x) == 1
    assert (-id/id)(x) == -1 == (id/-id)(x)


def test_multiplication():
    assert 5*id(x) == (5*id)(x)


def test_pow():
    assert x**2 == id(x)**2 == (id*id)(x) == (id**2)(x)


def test_rpow():
    assert (2**id)(x) == 2**x


def test_expression_ception():
    id = Expression(1, 1, 0)
    times_two = Expression(2, 1, 0)
    plus_5 = Expression(1, 1, 5)
    assert id(plus_5(id(id(times_two(plus_5(5)))))) == id(5)**2


def test_derivative():
    assert Expression.fromString("x^2").derivetive(x) == 2*x


def test_antiderivative():
    assert almost_equal(Expression.fromString("x^2").antiderivative(x), x**3/3)
