from __future__ import annotations
from typing import Any, Tuple
from ...utils import isoneof, areinstances
from ...la1 import Complex
from .PolynomialSimple import PolynomialSimple


class PolynomialFraction:
    @staticmethod
    def fromString(string, var="x") -> PolynomialFraction:
        pass

    @staticmethod
    def fromPolynomials(nominator: PolynomialSimple, denominator: PolynomialSimple) -> PolynomialFraction:
        if not areinstances([nominator, denominator], PolynomialSimple):
            raise TypeError("nominator and denominator must be Polynomials")
        return PolynomialFraction(nominator.prefixes, nominator.powers, denominator.prefixes, denominator.powers)

    @staticmethod
    def fromPrimitive(value) -> PolynomialFraction:
        if not isoneof(value, [int, float, Complex]):
            raise TypeError("value must be a number")
        return PolynomialFraction([value], [0])

    def __init__(self, nominator_prefixes: list, nominator_powers: list, denominator_prefixes: list = [1], denominator_powers: list = [0]) -> None:
        self.nominator = PolynomialSimple(nominator_prefixes, nominator_powers)
        self.denominator = PolynomialSimple(
            denominator_prefixes, denominator_powers)

    def __add__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            n1, d1 = self.destructure()
            n2, d2 = other.destructure()
            return PolynomialFraction.fromPolynomials(n1*d2+n2*d1, d1*d2)
        elif isinstance(other, PolynomialSimple):
            return self+PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self+PolynomialFraction.fromPrimitive(other)
        raise NotImplementedError(
            f"Addition of Expressions with {type(other)} not implemented yet")

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
            return PolynomialFraction.fromPolynomials(self.nominator*other.nominator, self.denominator*other.denominator)
        elif isinstance(other, PolynomialSimple):
            return self*PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self*PolynomialFraction.fromPrimitive(other)
        raise NotImplementedError(
            "Multiplication of Expressions with {} not implemented yet".format(type(other)))

    def __rmul__(self, other) -> PolynomialFraction:
        return self.__mul__(other)

    def __truediv__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            n1, d1 = self.destructure()
            n2, d2 = other.destructure()
            return PolynomialFraction.fromPolynomials(n1*d2, d1*n2)
        elif isinstance(other, PolynomialSimple):
            return self / PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self / PolynomialFraction.fromPrimitive(other)
        raise NotImplementedError(
            "Division of Expressions with {} not implemented yet".format(type(other)))

    def __rtruediv__(self, other) -> PolynomialFraction:
        # if isinstance(other, Expression):
        #     n1, d1 = self.destructure()
        #     n2, d2 = other.destructure()
        #     return Expression.fromPolynomials(n1*d2, d1*n2)
        if isinstance(other, PolynomialSimple):
            return self / PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return PolynomialFraction.fromPrimitive(other) / self
        raise NotImplementedError(
            "Division of Expressions with {} not implemented yet".format(type(other)))

    def __eq__(self, other) -> PolynomialFraction:
        if isinstance(other, PolynomialFraction):
            n1, d1 = self.destructure()
            n2, d2 = other.destructure()
            # n1/d1 == n2/d2 <==> n1d2/d1d2 == n2d1/d1d2 <==> n1d2 == n2d1
            return n1*d2 == n2*d1
        elif isinstance(other, PolynomialSimple):
            return self == PolynomialFraction(other.prefixes, other.powers)
        elif isoneof(other, [int, float, Complex]):
            return self == PolynomialFraction.fromPrimitive(other)
        return False

    def __ne__(self, other) -> PolynomialFraction:
        return not self.__eq__(other)

    def __pow__(self, other) -> PolynomialFraction:
        if isinstance(other, int):
            return PolynomialFraction.fromPolynomials(self.nominator**other, self.denominator**other)
        raise NotImplementedError(
            "Exponentiation of Expressions not implemented yet")

    def __rpow__(self, other) -> PolynomialFraction:
        raise NotImplementedError(
            "Exponentiation of Expressions not implemented yet")

    def __str__(self) -> str:
        if self.denominator != 1:
            return f"({str(self.nominator)})/({str(self.denominator)})"
        return str(self.nominator)

    def __call__(self, value) -> Any:
        if isoneof(value, [int, float, Complex, PolynomialSimple, PolynomialFraction]):
            try:
                return self.nominator(value) / self.denominator(value)
            except ArithmeticError as e:
                raise e
        else:
            raise ValueError(
                "PolynomialFraction.__call__() called with invalid argument")

    def destructure(self) -> Tuple[PolynomialSimple, PolynomialSimple]:
        return self.nominator, self.denominator

    def simplify() -> PolynomialFraction:
        pass
# from __future__ import annotations
# from functools import reduce
# import Polynomial
# from typing import Union, Callable, Any, Tuple
# import Complex
# from utils import isoneof, alloneof, validate_brackets
# import Vector
# import LinearTransformation
# class Expression:
#     @staticmethod
#     def fromString(s: str, var: str = "x") -> Expression:
#         if not validate_brackets(s):
#             raise ValueError("invalid brackets")
#         if var not in s:
#             raise ValueError("Variable not found in string")
#         if s.count(var) > 1:
#             raise NotImplementedError(
#                 "Not implemented more than one appearance of variable")
#         if s.count("^") > 1:
#             raise NotImplementedError(
#                 "Not implemented more than one appearance of power")
#         if s.count("*") > 1:
#             raise NotImplementedError(
#                 "Not implemented more than one appearance of multiplication")
#         if s.count("/") > 1:
#             raise NotImplementedError(
#                 "Not implemented more than one appearance of division")
#         if s.count("+") > 1:
#             raise NotImplementedError(
#                 "Not implemented more than one appearance of addition")
#         if s.count("-") > 1:
#             raise NotImplementedError(
#                 "Not implemented more than one appearance of subtraction")
#         def extract(string: str, variable: str, operator: str) -> Tuple[str, float]:
#             tmp = string.split(operator)
#             try:
#                 if len(tmp) == 2:
#                     remainder, num = None, None
#                     if var in tmp[0]:
#                         num = float(tmp[1])
#                         remainder = tmp[0]
#                     else:
#                         num = float(tmp[0])
#                         remainder = tmp[1]
#                     return remainder.strip(), num
#                 else:
#                     if len(tmp) == 1 and variable in tmp[0]:
#                         return tmp[0].strip(), 1 if operator in ["*", "^"] else 0
#                     elif len(tmp) == 1 and variable not in tmp[0]:
#                         return "", float(tmp[0])
#                     assert False, "shouldnt not be here"
#             except ValueError as e:
#                 raise e

#         try:
#             if "(" not in s:
#                 remainder, b = extract(s, var, "+")
#                 remainder, a = extract(remainder, var, "*")
#                 _, p = extract(remainder, var, "^")
#                 return Expression(a, p, b, lambda x: a*(x**p)+b)
#             else:
#                 if s.count("(") > 1:
#                     raise NotImplementedError(
#                         "Not implemented more than one appearance of brackets")
#                 inner_as_text = s[s.find("(")+1:s.find(")")]
#                 inner = Expression.fromString(inner_as_text, var)
#                 wrapper = Expression.fromString(
#                     s.replace(f"({inner_as_text})", "x"), var)
#                 return Expression.fromFunction(lambda x: wrapper(inner(x)))
#         except Exception as e:
#             raise e

#     @ staticmethod
#     def fromFunction(f: Callable[[Any], Any]) -> Expression:
#         return Expression(None, None, None, f)

#     def __init__(self, a=1, p=1, b=0, func=None) -> None:
#         """_summary_
#         Initialize an Expression object
#         Args:
#             a (_type_): _description_
#             p (_type_): _description_
#             b (_type_): _description_
#         """
#         if alloneof([a, p, b, func], [type(None)]):
#             raise ValueError("Cannot create Expression with all None")
#         self.a = a
#         self.p = p
#         self.b = b
#         self.func = func

#     @ property
#     def derivetive(self) -> Expression:
#         if not alloneof([self.a, self.p, self.b], [type(None)]):
#             return Expression(self.a*self.p, self.p-1, 0, lambda x: self.a*self.p*(x**(self.p-1)))
#         else:
#             raise ValueError("cant be calculated")

#     @ property
#     def antiderivative(self) -> Expression:
#         if not alloneof([self.a, self.p, self.b], [type(None)]):
#             return Expression(self.a/(self.p+1), self.p+1, 0, lambda x: self.a/(self.p+1)*(x**(self.p+1)))
#         else:
#             raise ValueError("cant be calculated")

#     @property
#     def minimal_polyinomial(self) -> Polynomial.Polynomial:
#         pass

#     def __add__(self, other: Union[int, float, Complex.Complex, Expression, Polynomial.Polynomial]) -> Union[Expression, Polynomial.Polynomial]:
#         if isinstance(other, Expression):
#             if self.func and other.func:
#                 return Expression.fromFunction(lambda x: self(x) + other(x))
#         elif isoneof(other, [int, float, Complex.Complex]):
#             if self.func:
#                 return Expression.fromFunction(lambda x: self(x) + other)
#         raise NotImplementedError("Not implemented")

#     def __radd__(self, other) -> Union[Expression, Polynomial.Polynomial]:
#         return self.__add__(other)

#     def __sub__(self, other) -> Expression:
#         return self.__add__(-other)

#     def __rsub__(self, other) -> Union[Expression, Polynomial.Polynomial]:
#         return other + (-self)

#     def __neg__(self) -> Expression:
#         if alloneof([self.a, self.p, self.b], [type(None)]):
#             return Expression.fromFunction(lambda x: -self(x))
#         return Expression(-self.a, self.p, self.b, lambda x: -self.func(x) if self.func else None)

#     def __truediv__(self, other) -> Expression:
#         if isinstance(other, Expression):
#             if self.func and other.func:
#                 return Expression.fromFunction(lambda x: self.func(x)/other.func(x))

#     def __mul__(self, other: Union[int, float, Complex.Complex, Expression, Polynomial.Polynomial]) -> Union[Expression, Polynomial.Polynomial]:
#         if isinstance(other, Expression):
#             if self.func and other.func:
#                 return Expression.fromFunction(lambda x: self(x) * other(x))
#         elif isoneof(other, [int, float, Complex.Complex]):
#             if self.func:
#                 return Expression.fromFunction(lambda x: self(x) * other)
#         raise NotImplementedError(
#             f"Not implemented Expression * {type(other).__name__}")

#     def __rmul__(self, other) -> Expression:
#         return self.__mul__(other)

#     def __pow__(self, power) -> Expression:
#         if isoneof(power, [int, float]):
#             if self.func:
#                 return Expression.fromFunction(lambda x: self(x)**power)
#         raise NotImplementedError(
#             f"Not implemented Expression ^ {type(power).__name__}")

#     def __rpow__(self, base) -> Expression:
#         if isinstance(base, Expression):
#             if self.func and base.func:
#                 return Expression.fromFunction(lambda x: base(x)**self(x))
#         elif isoneof(base, [int, float, Complex.Complex]):
#             if self.func:
#                 return Expression.fromFunction(lambda x: base**self(x))
#         raise NotImplementedError(
#             f"Not implemented {type(base).__name__} ^ Expression")

#     def __call__(self, x: Union[int, float, Complex.Complex]) -> Union[int, float, Complex.Complex]:
#         if alloneof([self.a, self.p, self.b], [type(None)]):
#             return self.func(x)
#         if alloneof([self.a, self.b, self.p], [int, float, Complex.Complex]):
#             if isoneof(x, [int, float, Complex.Complex]):
#                 if isinstance(self.p, Complex.Complex):
#                     raise NotImplementedError("Complex power not implemented")
#                 return self.func(x) if self.func else self.a * (x**self.p)+self.b
#             else:
#                 NotImplementedError("Not implemented")
#         else:

#             raise NotImplementedError("Not implemented")

#     def __str__(self) -> str:
#         if not alloneof([self.a, self.p, self.b], [type(None)]):
#             if self.a == 0:
#                 return f"{self.b}"
#             if self.b == 0:
#                 if self.p == 0:
#                     return f"{self.a}"
#                 else:
#                     if self.a == 1:
#                         return f"x^{self.p}"
#                 return f"{self.a}*x^{self.p}"
#             return f"{self.a}*x^{self.p}+{self.b}"
#         return "No representations for lambda"

#     def toVector(self) -> Vector.Vector:
#         # TODO rethink if this needs to be here or in Polynomial.Polynomial and if so, how to do it
#         pass
