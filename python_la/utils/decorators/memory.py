from typing import Callable
from functools import wraps


def memo(func: Callable) -> Callable:
    d = dict()

    @wraps(func)
    def wrapper(*args, **kwargs):
        tup = (*args, *list(kwargs.keys()), *list(kwargs.values()))
        if tup in d:
            return d[tup]
        res = func(*args, **kwargs)
        d[tup] = res
        return res
    return wrapper
