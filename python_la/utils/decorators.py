from typing import Callable
import functools


def depracated(extra_info: str = "") -> Callable:
    def wrapper(func):
        def inner(*args, **kwargs):
            print(
                f'{func.__module__}.{func.__name__}(...) is depracated!', extra_info, sep="\n")
            return func(*args, **kwargs)
        return inner
    return wrapper


def abstractmethod(func: Callable):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        raise NotImplementedError(
            f"{func.__module__}.{func.__name__}(...) is an abstract method and must be implemented in a derived classes")
    # same as using functools.wraps
    # wrapper.__doc__ = func.__doc__
    return wrapper


def message(msg: str) -> Callable:
    def wrapper(func):
        def inner(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return inner
    return wrapper
