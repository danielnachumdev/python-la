import random
from ...helpers import *
from ....la1 import Complex as comp, Vector, RealField, LinearMap, VectorSpace, Span, Matrix
from ....la2 import StandardInnerProduct as sip
from math import sqrt


def test_almost_equal():
    assert almost_equal(comp(1, -5.551115123125783e-17),
                        comp(1, 0), comp(1, -5.551115123125783e-17))
    a, b, c = [-0.6666666666666666, -0.3333333333333333, 1.0]
    assert almost_equal((a+b)+c, a+(b+c))
    assert almost_equal(round(0.9999999999999999), 1)


def test_bracketify():
    assert bracketify("()") == [("(", 0), (")", 1)]


def test_insert_multiplication():
    func = insert_multiplication
    assert func("(()())(())") == '(()*())*(())'
    assert func(
        "(())(()()()(()))(())") == '(())*(()*()*()*(()))*(())'
    assert func("()()+()()") == '()*()+()*()'


def test_open_power():
    func = open_power
    assert func("(x+1)^2") == "(x+1)(x+1)"
    assert func("((x+1)^2)^2") == "((x+1)(x+1))((x+1)(x+1))"
    assert func("(x)^10") == "(x)(x)(x)(x)(x)(x)(x)(x)(x)(x)"


def test_split_not_between_brackets():
    func = split_not_between_brackets
    assert func("(()())*(()())", "*") == ["()*()", "()*()"]
    assert func("()()()()", "*") == ["", "", "", ""]
    assert func("(x+1)(x+1)", "*") == ["x+1", "x+1"]
    assert func("(x+1)(x+1)", "+") == ["x+1", "x+1"]
    assert func("(x+1)(x+1)", "-") == ["x+1", "x+1"]
    assert func("(x+1)(x+1)", "/") == ["x+1", "x+1"]
    assert func("((x)+1)(x+1)", "*") == ["(x)+1", "x+1"]


def test_composit_functions():
    R2 = RealField(2)

    def func(v):
        return Vector([v[1], v[0]], R2)

    lt = LinearMap.from_fields(R2, R2, func)
    v = VectorSpace(R2).random()
    assert lt(lt(v)) == v
    assert (lt**2)(v) == v
    assert (lt**4)(v) == (lt**2)(v)
    num = random.randint(1, 10)
    lt2 = num*lt
    assert lt2(v) == Vector([v[1]*num, v[0]*num], R2)
    assert (lt2**2)(v) == (Vector([v[0]*num**2, v[1]*num**2], R2))

    def func(v):
        return Vector([0, v[0]], R2)

    lt = LinearMap.from_fields(R2, R2, func)
    v = VectorSpace(R2).random()
    assert (num*lt**2)(v) == Vector([0, 0], R2)


def test_check_forevery():
    assert check_forevery([1, 2, 3, 4, 5, 6, 7, 8, 9],
                          2, lambda x, y: x+y >= 3)
    pt = Matrix([
        [sqrt(3/2), sqrt(3/2), 0],
        [-sqrt(1/2), sqrt(1/2), 0],
        [-1, -1, 1]
    ])
    p = pt.transpose()
    assert check_forevery([v for v in Span(p.column_space).to_orthonormal()], 2, lambda x,
                          y: almost_equal(sip(x, y), 0))
