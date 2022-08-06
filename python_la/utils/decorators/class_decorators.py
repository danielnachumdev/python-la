from typing import Callable
import functools


def abstractmethod(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        raise NotImplementedError(
            f"{func.__module__}.{func.__name__}(...) is an abstract method and must be implemented in a derived classes")
    # same as using functools.wraps
    # wrapper.__doc__ = func.__doc__
    return wrapper
