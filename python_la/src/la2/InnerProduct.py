import random
from typing import Callable, Union
from ..la1 import Complex, Vector


class InnerProduct:

    @staticmethod
    def isInnerProduct(func: Callable[[Vector, Vector], float], generator_func: Callable[[bool], Vector]) -> bool:
        MIN_VAL = -100
        MAX_VAL = 100
        REPETITIONS = 1000
        THRESHOLD = 0.000000001

        def check_linearity(func: Callable[[Vector, Vector], float], generator_func: Callable[[bool], Vector]) -> bool:
            for _ in range(REPETITIONS):
                a: Vector = generator_func()
                b: Vector = generator_func()
                c: Vector = generator_func()
                s1 = random.randint(MIN_VAL, MAX_VAL)
                s2 = random.randint(MIN_VAL, MAX_VAL)
                original = func(a, s1*b+s2*c)
                decomp = s1*func(a, b)+s2*func(a, c)
                if original - decomp > THRESHOLD:
                    return False
            return True

        def check_symmetry(func: Callable[[Vector, Vector], float], generator_func: Callable[[bool], Vector]) -> bool:
            for _ in range(REPETITIONS):
                a: Vector = generator_func()
                b: Vector = generator_func()
                # TODO implemnt symmetry check for complex
                original = func(a, b)
                adj = func(b, a)
                if original-adj > THRESHOLD:
                    return False
            return True

        def check_norm(func: Callable[[Vector, Vector], float], generator_func: Callable[[bool], Vector]) -> bool:
            for _ in range(REPETITIONS):
                v: Vector = generator_func()
                if not func(v, v) > 0:
                    return False
            v = generator_func(True)
            if func(v, v) != 0:
                return False
            return True

        return all[check_linearity(func, generator_func), check_symmetry(func, generator_func), check_norm(func, generator_func)]

    def __init__(self, func: Callable[[Vector, Vector], float]) -> None:
        if func is None:
            raise ValueError("func is None")
        self._func = func

    def __call__(self, v1, v2) -> Union[float, Complex]:
        return self._func(v1, v2)


# def __StandardInnerProduct(a: Vector, b: Vector) -> float:
#     if not isinstance(a, Vector):
#         raise TypeError("a must be a Vector")
#     if not isinstance(b, Vector):
#         raise TypeError("b must be a Vector")
#     if a.length != b.length:
#         raise ValueError("Vectors must have the same length")
#     return sum([a[i] * b[i] for i in range(a.length)])

StandardInnerProduct = InnerProduct(
    lambda a, b: sum([a[i] * b[i] for i in range(a.length)]))
