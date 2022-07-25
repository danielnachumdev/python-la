from utils import *
from Complex import Complex as comp


def test_almost_equal():
    assert almost_equal(comp(1, -5.551115123125783e-17),
                        comp(1, 0), comp(1, -5.551115123125783e-17))
    a, b, c = [-0.6666666666666666, -0.3333333333333333, 1.0]
    assert almost_equal((a+b)+c, a+(b+c))


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
    from Vector import Vector
    from LinearTransformation import LinearTransformation
    from Field import RealField
    import random

    def func(v, target):
        return Vector([v[1], v[0]], target)
    R2 = RealField(2)
    lt = LinearTransformation(R2, R2, func)
    v = R2.random()
    assert lt(lt(v)) == v, 1
    assert (lt**2)(v) == v, 2
    assert (lt**4)(v) == (lt**2)(v), 3
    num = random.randint(1, 10)
    lt2 = num*lt
    assert lt2(v) == Vector([v[1]*num, v[0]*num], R2), 4
    if not (lt2**2)(v) == Vector([v[0]*num**2, v[1]*num**2], R2):
        # FIXME doent work sometimes
        pass
    assert (lt2**2)(v) == Vector([v[0]*num**2, v[1]*num**2], R2), 5

    def func(v, target):
        return Vector([0, v[0]], target)
    lt = LinearTransformation(R2, R2, func)
    v = R2.random()
    assert (num*lt**2)(v) == Vector([0, 0], R2), 6
