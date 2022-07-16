from utils import *
from Complex import Complex as comp


def test_almost_equal():
    assert almost_equal(comp(1, -5.551115123125783e-17),
                        comp(1, 0), comp(1, -5.551115123125783e-17))
    a, b, c = [-0.6666666666666666, -0.3333333333333333, 1.0]
    assert almost_equal((a+b)+c, a+(b+c))
