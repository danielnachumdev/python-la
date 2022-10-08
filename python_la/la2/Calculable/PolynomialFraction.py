from __future__ import annotations
from typing import Any, Tuple, Sequence, Sequence, Sequence, Sequence
from ...la1 import Complex
from .PolynomialSimple import PolynomialSimple
from danielutils import validate, isoneof, NotImplemented


class PolynomialFraction____:
    pass


class PolynomialFraction__(PolynomialFraction____):
    @validate(None, Sequence, Sequence, Sequence, Sequence)
    def __init__(self, nominator_prefixes: list, nominator_powers: list, denominator_prefixes: list = [1], denominator_powers: list = [0]) -> None:
        self.nominator = PolynomialSimple(nominator_prefixes, nominator_powers)
        self.denominator = PolynomialSimple(
            denominator_prefixes, denominator_powers)

    @validate(None, [int, float, Complex, PolynomialSimple, PolynomialFraction____])
    def __add__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            n1, d1 = self.nominator, self.denominator
            n2, d2 = other.nominator, other.denominator
            return PolynomialFraction.from_polynomials(n1*d2+n2*d1, d1*d2)
        elif isinstance(other, PolynomialSimple):
            return self+PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self+PolynomialFraction.from_primitive(other)

    def __radd__(self, other) -> PolynomialFraction:
        return self.__add__(other)

    def __sub__(self, other) -> PolynomialFraction:
        return self + (-other)

    def __rsub__(self, other) -> PolynomialFraction:
        return other + (-self)

    def __neg__(self) -> PolynomialFraction:
        return self.__mul__(-1)

    @validate(None, [int, float, Complex, PolynomialSimple, PolynomialFraction____])
    def __mul__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            return PolynomialFraction.from_polynomials(self.nominator*other.nominator, self.denominator*other.denominator)
        elif isinstance(other, PolynomialSimple):
            return self*PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self*PolynomialFraction.from_primitive(other)

    def __rmul__(self, other) -> PolynomialFraction:
        return self.__mul__(other)

    @validate(None, [int, float, Complex, PolynomialSimple, PolynomialFraction____])
    def __truediv__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            n1, d1 = self.nominator, self.denominator
            n2, d2 = other.nominator, other.denominator
            return PolynomialFraction.from_polynomials(n1*d2, d1*n2)
        elif isinstance(other, PolynomialSimple):
            return self / PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self / PolynomialFraction.from_primitive(other)

    def __rtruediv__(self, other) -> PolynomialFraction:
        # if isinstance(other, Expression):
        #     n1, d1 = self.destructure()
        #     n2, d2 = other.destructure()
        #     return Expression.fromPolynomials(n1*d2, d1*n2)
        if isinstance(other, PolynomialSimple):
            return self / PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return PolynomialFraction.from_primitive(other) / self
        raise NotImplementedError(
            "Division of Expressions with {} not implemented yet".format(type(other)))

    @validate(None, [int, float, Complex, PolynomialSimple, PolynomialFraction____])
    def __eq__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            n1, d1 = self.nominator, self.denominator
            n2, d2 = other.nominator, other.denominator
            # n1/d1 == n2/d2 <==> n1d2/d1d2 == n2d1/d1d2 <==> n1d2 == n2d1
            return n1*d2 == n2*d1
        elif isinstance(other, PolynomialSimple):
            return self == PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self == PolynomialFraction.from_primitive(other)
        return False

    def __ne__(self, other) -> PolynomialFraction:
        return not self.__eq__(other)

    @validate(None, int)
    def __pow__(self, other) -> PolynomialFraction:
        if isinstance(other, int):
            return PolynomialFraction.from_polynomials(self.nominator**other, self.denominator**other)

    @NotImplemented
    def __rpow__(self, other) -> PolynomialFraction:
        pass

    def __str__(self) -> str:
        if self.denominator != 1:
            return f"({str(self.nominator)})/({str(self.denominator)})"
        return str(self.nominator)

    @validate(None, [int, float, Complex, PolynomialSimple, PolynomialFraction____])
    def __call__(self, value) -> Any:
        try:
            return self.nominator(value) / self.denominator(value)
        except ArithmeticError as e:
            raise e


class PolynomialFraction(PolynomialFraction__):
    @staticmethod
    @NotImplemented
    @validate(str, str)
    def from_string(string, var="x") -> PolynomialFraction:
        pass

    @staticmethod
    @validate(PolynomialSimple, PolynomialSimple)
    def from_polynomials(nominator: PolynomialSimple, denominator: PolynomialSimple) -> PolynomialFraction:
        return PolynomialFraction(nominator.prefixes, nominator.powers, denominator.prefixes, denominator.powers)

    @staticmethod
    @validate([int, float, Complex])
    def from_primitive(value) -> PolynomialFraction:
        return PolynomialFraction([value], [0])

    def destructure(self) -> Tuple[PolynomialSimple, PolynomialSimple]:
        return self.nominator, self.denominator

    @NotImplemented
    def simplify() -> PolynomialFraction:
        pass


__all__ = [
    "PolynomialFraction"
]
