from __future__ import annotations
import Vector
import Expression
import functools


class Polynomial:
    @staticmethod
    def fromString(s: str, var: str = "x") -> Polynomial:
        if var not in s:
            raise ValueError("Variable not found in string")

    def __init__(self, expressions: list[Expression.Expression]) -> None:
        self.expressions = expressions

        def comparer(v1: Expression.Expression, v2: Expression.Expression) -> int:
            bias = 1
            if v1.p < v2.p:
                return -bias
            elif v1.p > v2.p:
                return bias
            else:
                if v1.a < v2.a:
                    return -bias
                elif v1.a > v2.a:
                    return bias
                else:
                    return 0
        self.expressions.sort(key=functools.cmp_to_key(comparer), reverse=True)

    @property
    def roots(self) -> Vector.Vector:
        # TODO calculation of roots if possible
        pass

    def __str__(self) -> str:
        # res = ""
        # for e in self.expressions:
        #     res += str(e) + " + "
        return " + ".join([str(e) for e in self.expressions])

    def __add__(self, other) -> Polynomial:
        # TODO implement polinomial __add__
        pass

    def __radd__(self, other) -> Polynomial:
        # TODO implement polinomial __radd__
        pass

    def __mul__(self, other) -> Polynomial:
        # TODO implement polinomial __mul__
        pass

    def __rmul__(self, other) -> Polynomial:
        # TODO implement polinomial __rmul__
        pass
    # TODO implement other operators

    def __call__(self, v):
        # TODO implement polinomial __call__
        pass

    def gcd_with(self, other: Polynomial) -> Polynomial:
        # TODO implement gcd calculation
        pass
