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


test_open_power()


def test_split_not_between_brackets():
    func = split_not_between_brackets
    assert func("(()())*(()())", "*") == ["()*()", "()*()"]
    assert func("()()()()", "*") == ["", "", "", ""]
    assert func("(x+1)(x+1)", "*") == ["x+1", "x+1"]
    assert func("(x+1)(x+1)", "+") == ["x+1", "x+1"]
    assert func("(x+1)(x+1)", "-") == ["x+1", "x+1"]
    assert func("(x+1)(x+1)", "/") == ["x+1", "x+1"]
    assert func("((x)+1)(x+1)", "*") == ["(x)+1", "x+1"]
