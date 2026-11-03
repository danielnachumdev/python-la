from __future__ import annotations
from typing import Any, Tuple, Sequence, Sequence, Sequence, Sequence
from ...la1 import Complex
from .PolynomialSimple import PolynomialSimple
from danielutils import isoneof


class PolynomialFraction____:
    pass


class PolynomialFraction__(PolynomialFraction____):
    def __init__(self, nominator_prefixes: list, nominator_powers: list, denominator_prefixes: list = [1], denominator_powers: list = [0]) -> None:
        self.nominator = PolynomialSimple(nominator_prefixes, nominator_powers)
        self.denominator = PolynomialSimple(
            denominator_prefixes, denominator_powers)

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

    def __mul__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            return PolynomialFraction.from_polynomials(self.nominator*other.nominator, self.denominator*other.denominator)
        elif isinstance(other, PolynomialSimple):
            return self*PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self*PolynomialFraction.from_primitive(other)

    def __rmul__(self, other) -> PolynomialFraction:
        return self.__mul__(other)

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

    def __pow__(self, other) -> PolynomialFraction:
        if isinstance(other, int):
            return PolynomialFraction.from_polynomials(self.nominator**other, self.denominator**other)

    def __rpow__(self, other) -> PolynomialFraction:
        raise NotImplementedError
    def __str__(self) -> str:
        if self.denominator != 1:
            return f"({str(self.nominator)})/({str(self.denominator)})"
        return str(self.nominator)

    def __call__(self, value) -> Any:
        try:
            return self.nominator(value) / self.denominator(value)
        except ArithmeticError as e:
            raise e


class PolynomialFraction(PolynomialFraction__):
    @staticmethod
    def from_string(string, var="x") -> PolynomialFraction:
        """Parse ``num``, ``num/den``, or ``(num)/(den)`` into a fraction.

        Bracketed products such as ``(x+1)*(x-1)`` are not supported; use
        ``PolynomialSimple.from_string`` pieces via ``from_polynomials``.
        """
        if not isinstance(string, str) or not string.strip():
            raise ValueError("string must be a non-empty str")
        text = string.strip().replace(" ", "")
        slash = PolynomialFraction._top_level_slash(text)
        if slash is None:
            return PolynomialFraction.from_polynomials(
                PolynomialSimple.from_string(text, var),
                PolynomialSimple([1], [0]),
            )
        numerator = PolynomialFraction._strip_outer_parens(text[:slash])
        denominator = PolynomialFraction._strip_outer_parens(text[slash + 1:])
        if not numerator or not denominator:
            raise ValueError(f"invalid polynomial fraction: {string!r}")
        return PolynomialFraction.from_polynomials(
            PolynomialSimple.from_string(numerator, var),
            PolynomialSimple.from_string(denominator, var),
        )

    @staticmethod
    def _top_level_slash(text: str) -> int | None:
        depth = 0
        for i, ch in enumerate(text):
            if ch in "([{":
                depth += 1
            elif ch in ")]}":
                depth -= 1
            elif ch == "/" and depth == 0:
                return i
        return None

    @staticmethod
    def _strip_outer_parens(text: str) -> str:
        text = text.strip()
        while len(text) >= 2 and text[0] == "(" and text[-1] == ")":
            depth = 0
            wraps = True
            for i, ch in enumerate(text):
                if ch == "(":
                    depth += 1
                elif ch == ")":
                    depth -= 1
                    if depth == 0 and i != len(text) - 1:
                        wraps = False
                        break
            if not wraps:
                break
            text = text[1:-1].strip()
        return text

    @staticmethod
    def from_polynomials(nominator: PolynomialSimple, denominator: PolynomialSimple) -> PolynomialFraction:
        return PolynomialFraction(nominator.prefixes, nominator.powers, denominator.prefixes, denominator.powers)

    @staticmethod
    def from_primitive(value) -> PolynomialFraction:
        return PolynomialFraction([value], [0])

    def destructure(self) -> Tuple[PolynomialSimple, PolynomialSimple]:
        return self.nominator, self.denominator

    def simplify(self) -> PolynomialFraction:
        raise NotImplementedError("PolynomialFraction.simplify is not implemented")
__all__ = [
    "PolynomialFraction"
]
