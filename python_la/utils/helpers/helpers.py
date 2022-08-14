# import Complex
from typing import Any, Callable
import math
from .instance_cheking import alloneof


def are_operators_implemnted(T) -> bool:
    try:
        T.__add__
        T.__radd__
        T.__sub__
        T.__rsub__
        T.__neg__
        T.__mul__
        T.__rmul__
        T.__truediv__
        T.__rtruediv__
        T.__eq__
        T.__ne__
        T.__hash__
        return True
    except AttributeError:
        return False


def almost_equal(*args):
    THRESHOLD = 0.000000000001

    def wrapper(a, b):
        if alloneof([a, b], [int, float]):
            return math.isclose(a, b, abs_tol=THRESHOLD)
        else:  # they are Complex.Complex
            try:
                return math.isclose(a.real, b.real, abs_tol=THRESHOLD) and math.isclose(a.imag, b.imag, abs_tol=THRESHOLD)
            except Exception as e:
                assert False, "shouldnt be here"
    return all([wrapper(args[0], args[i]) for i in range(1, len(args))])


def check_foreach(arr: list, condition) -> bool:
    for v in arr:
        if not condition(v):
            return False
    return True


def composite_function(f, g):
    return lambda *args: f(g(*args))


def check_forevery(arr: list[Any], amount: int, condition: Callable[[], bool]) -> bool:
    def helper(arr: list, current: list) -> bool:
        if len(current) == amount:
            return condition(*current)
        for i, v in enumerate(arr):
            if not helper(arr[i+1:], current+[v]):
                return False
        return True
    return helper(arr, [])
