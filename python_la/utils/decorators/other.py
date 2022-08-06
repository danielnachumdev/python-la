from typing import Callable


def message(msg: str) -> Callable:
    def wrapper(func):
        def inner(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return inner
    return wrapper


def depracated(extra_info: str = "") -> Callable:
    def wrapper(func):
        def inner(*args, **kwargs):
            print(
                f'{func.__module__}.{func.__name__}(...) is depracated!', extra_info, sep="\n")
            return func(*args, **kwargs)
        return inner
    return wrapper
