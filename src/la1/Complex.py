from __future__ import annotations
from typing import Union
import random
from ..utils import isoneof


class Complex:
    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        return f'{self.real} + {self.imag}i'

    def __add__(self, other: Union[float, Complex]) -> Complex:
        if isinstance(other, float):
            return Complex(self.real + other, self.imag)
        else:
            return Complex(self.real + other.real, self.imag + other.imag)

    def __radd__(self, other: Union[float, Complex]) -> Complex:
        return self.__add__(other)

    def __mul__(self, other: Union[float, Complex]) -> Complex:
        if isinstance(other, float):
            return Complex(self.real * other, self.imag * other)
        else:
            return Complex(self.real * other.real - self.imag * other.imag,
                           self.real * other.imag + self.imag * other.real)

    def __rmul__(self, other: Union[float, Complex]) -> Complex:
        return self.__mul__(other)

    def __neg__(self) -> Complex:
        return Complex(-self.real, -self.imag)

    def __sub__(self, other: Union[float, Complex]) -> Complex:
        return self + (-other)

    def __rsub__(self, other: Union[float, Complex]) -> Complex:
        # other-self==-(self-other)
        return -self.__sub__(other)

    def __abs__(self) -> float:
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def __eq__(self, other: Complex) -> bool:
        if not isinstance(other, Complex) and not isinstance(self, float) and not isinstance(other, int):
            raise TypeError(f"cannot compare equality to type {type(other)}")
        if not isinstance(other, Complex):
            other = Complex(other, 0)
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return not self.__eq__(other)

    def __truediv__(self, other: Union[int, float, Complex]) -> Complex:
        if not isinstance(other, Complex) and not isinstance(other, float) and not isinstance(other, int):
            raise TypeError(
                "can only divide complex by [int, float , complex]")
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        if not isinstance(other, Complex):
            other = Complex(other, 0)

        nominator = Complex(self.real, self.imag)*other.conjugate
        denominator = other*other.conjugate
        return Complex(nominator.real/denominator.real, nominator.imag/denominator.real)

    def __rtruediv__(self, other) -> Complex:
        if not isinstance(other, Complex) and not isinstance(other, float) and not isinstance(other, int):
            raise TypeError(
                "can only divide [int, float , complex] by complex")
        if not isinstance(other, Complex):
            other = Complex(other, 0)
        nominator = other*self.conjugate
        denominator = self*self.conjugate
        return Complex(nominator.real/denominator.real, nominator.imag/denominator.real)

    def __pow__(self, p):
        # TODO: implement Complex**p fully
        if not isoneof(p, [int]):
            raise NotImplementedError(
                "Complex.__pow__ only implemented for int right now")

        def fix_negativ(v) -> Complex:
            if p < 0:
                return 1/v
            return v

        if p == 0:
            return Complex(1, 0)
        elif p == 1:
            return fix_negativ(self)
        else:
            res = self
            for _ in range(abs(p)-1):
                res *= self
            return fix_negativ(res)

    def __rpow__(self, other):
        # TODO: implement base**Complex
        raise NotImplementedError("This is not implemented yet")

    @property
    def conjugate(self):
        return Complex(self.real, -self.imag)

    @property
    def norm(self):
        return (self * self.conjugate).real

    @staticmethod
    def random(min_val: float = -10, max_val: float = 10, value_func=random.randint) -> Complex:
        return Complex(value_func(min_val, max_val), value_func(min_val, max_val))
