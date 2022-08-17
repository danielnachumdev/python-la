from __future__ import annotations
from .Calculable import Calculable
from ...la1 import Complex
from typing import Any
from .PolynomialSimple import PolynomialSimple
from ...utils import isoneof, validate_brackets, open_power, split_not_between_brackets, split_if_any, python_la_superscript_n, sign


class PolynomialCompact(Calculable):
    @staticmethod
    def from_string(input, var="x") -> PolynomialCompact:
        if any(bracket in input for bracket in ["(", ")", "[", "]", "{", "}"]):
            if not validate_brackets(input):
                raise ValueError("invalid brackets")
            partials1, order1 = split_not_between_brackets(
                input, ["+", "-"])
            if len(order1) < len(partials1):
                order1.insert(0, "+")
            res = 0
            for i, sub_input in enumerate(partials1):
                partials2, order2 = split_not_between_brackets(
                    open_power(sub_input), ["*"])
                partial_polys = []
                for sub in partials2:
                    sub = sub.strip("()")
                    partial_polys.append(
                        PolynomialSimple.from_string(sub, var))
                res = sign(order1[i])*PolynomialCompact(partial_polys) + res
            return res
            # for sub in subs:
            #     res = PolynomialSimple.from_string(sub_inputs[0], var)
            #     for sub_input in sub_inputs[1:]:
            #         res *= PolynomialSimple.from_string(sub_input, var)
            #     polys.append(res)
        return PolynomialSimple.from_string(input, var)

    def __init__(self, polys: list[int, float, Complex, PolynomialSimple, PolynomialCompact], powers: list[float] = None) -> None:
        if not isinstance(polys, list):
            raise TypeError("polys must be a list of PolynomialSimple")
        for p in polys:
            if not isoneof(p, [int, float, Complex, PolynomialSimple, PolynomialCompact]):
                raise TypeError(
                    "polys must be a list of PolynomialSimple or PolynomialCompact or numbers")
        if powers == None:
            powers = [1 for _ in polys]
        for p in powers:
            if not isoneof(p, [float, int]):
                raise TypeError("p must be a float or int")
        self.powers = powers
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
        for i, p in enumerate(self.polys):
            res += f"({str(p)}){python_la_superscript_n(self.powers[i])}"
        return res

    def __add__(self, other):

        if not isoneof(other, [int, float, Complex, PolynomialCompact, PolynomialSimple]):
            raise TypeError(
                "other must be [int, float, Complex, PolynomialCompact, PolynomialSimple]")
        return self.expand()+other

    def __radd__(self, other) -> PolynomialCompact:
        return self+other

    def __mul__(self, value) -> PolynomialCompact:
        return PolynomialCompact(self.polys+[value])

    def __rmul__(self, value) -> PolynomialCompact:
        return self*value

    def __call__(self, value: Any) -> Any:
        return self.expand()(value)

    def __eq__(self, other) -> bool:
        if not isoneof(other, [int, float, Complex, PolynomialSimple, PolynomialCompact]):
            return False
        if isinstance(other, PolynomialCompact):
            return self.expand() == other.expand()
        return self.expand() == other

    def __ne__(self, other) -> bool:
        return not (self == other)
