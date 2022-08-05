from __future__ import annotations
from .Calculable import Calculable
from ...la1 import Complex
from typing import Any
from .PolynomialSimple import PolynomialSimple
from ...utils import isoneof


class PolynomialCompact(Calculable):
    def __init__(self, polys: list[int, float, Complex, PolynomialSimple, PolynomialCompact]) -> None:
        if not isinstance(polys, list):
            raise TypeError("polys must be a list of PolynomialSimple")
        for p in polys:
            if not isoneof(p, [int, float, Complex, PolynomialSimple, PolynomialCompact]):
                raise TypeError(
                    "polys must be a list of PolynomialSimple or PolynomialCompact or numbers")
        self.polys = polys

    def expand(self) -> PolynomialSimple:
        res = PolynomialSimple([1], [0])
        for p in self.polys:
            if isinstance(p, PolynomialCompact):
                res *= p.expand()
            else:
                res *= p
        return res

    def __str__(self) -> str:
        res = ""
        for p in self.polys:
            res += f"({str(p)})"
        return res

    def __mul__(self, value) -> PolynomialCompact:
        return PolynomialCompact(self.polys+[value])

    def __rmul__(self, value) -> PolynomialCompact:
        return self*value

    def __call__(self, value: Any) -> Any:
        return self.expand()(value)
