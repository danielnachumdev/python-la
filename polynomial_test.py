from Polynomial import Polynomial as p

x = p([1], [1])
xp1 = p([1, 1], [1, 0])
square = p([1], [2])
sqrt = p([1], [1/2])


def test_constuctor_special_case():
    assert p([1, 2], [1, 1]) == p([3], [1])


def test_addition():
    assert x+5 == p([1, 5], [1, 0])
    assert 5+x == p([1, 5], [1, 0])
    assert 5+x+5 == p([1, 10], [1, 0])
    assert x+p([2], [2]) == p([1, 2], [1, 2])


def test_subtraction():
    assert x-5 == p([1, -5], [1, 0])
    assert 5-x == p([5, -1], [0, 1])
    assert 5-x-5 == p([-1], [1])
    assert x-p([2], [2]) == p([1, -2], [1, 2])
    assert x-x == 0


def test_negation():
    assert -x == p([-1], [1])


def test_multiplication():
    assert 1*x == x
    assert x*5 == p([5], [1])
    assert x*x == p([1], [2])
    assert xp1*xp1 == p([1, 2, 1], [2, 1, 0])
    assert p.fromString(
        "(x^2+2*x+5)")*p.fromString("1") == p.fromString("1")*p.fromString("(x^2+2*x+5)")


def test_call():
    assert x(5) == 5
    assert x(5.0) == 5.0
    assert xp1(5) == 6
    assert x*xp1(2) == p([3], [1])
    assert (x*x)(5) == 25
    assert (xp1*xp1)(2) == (2+1)**2
    assert square(square)(2) == 16
    assert square(xp1)(2) == (2+1)**2
    assert sqrt(4) == 2


# def test_division():
#     assert x/1 == (x, 0)
#     # TODO finish implementing so tests will pass
#     # assert 1/x == p([1], [-1])
#     assert xp1/x == (p([1], [0]), p([1], [-1]))


# test_division()


def test_pow():
    assert x**0 == 1
    assert x**1 == x
    assert x**2 == x*x
    assert x**3 == x*x*x
    assert (xp1**2)(2) == (2+1)**2
    assert (xp1**2)(2.0) == (2+1)**2
    assert x**-1 == 1/x


def test_equals():
    assert p([0], [0]) == 0 == p([0], [534273])
    assert p([], []) == 0
    assert p([0], []) == 0
    assert p([1], [0]) == 1


def test_fromstring():
    f = p.fromString
    assert f("x^2 +2x+1") == p([1, 2, 1], [2, 1, 0])
    assert f(
        "-x^7+x^6-34*x^5-x4-x^3+x^2") == p([-1, -1, 34, -1, -1, -4], [7, 6, 5, 3, 2, 1])
    assert f("(x+1)") == p([1, 1], [1, 0])
    assert f("((x+1))(x+1)") == p([1, 2, 1], [2, 1, 0]) == f("(x+1)^2")
    # TODO can run faster need to improve this
    assert f("((1)(x^2+2*x+5))^2") == f("X^4 + 4X^3 + 14X^2 + 20X + 25", "X")
