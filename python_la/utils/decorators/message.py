from typing import Callable


def message(msg: str) -> Callable:
    def wrapper(func):
        def inner(*args, **kwargs):
            print(msg)
            return func(*args, **kwargs)
        return inner
    return wrapper
