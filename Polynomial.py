from __future__ import annotations
from Vector import Vector
import Expression


class Polynomial:
    @staticmethod
    def fromString(s: str, var: str = "x") -> Polynomial:
        if var not in s:
            raise ValueError("Variable not found in string")

    def __init__(self, expressions: list[Expression.Expression]) -> None:
        self.expressions = sorted(expressions, key=lambda x: x.power)

    @property
    def roots(self) -> Vector:
        pass

    def __str__(self) -> str:
        res = ""
        for e in self.expressions:
            res += str(e) + " + "
        return res

    def __add__(self, other) -> Polynomial:
        pass

    def __mul__(self, other) -> Polynomial:
        pass

    def __call__(self, v):
        pass
