from __future__ import annotations
from typing import Union


class Complex:
    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __str__(self) -> str:
        return '{0.real:.2f}{0.imag:+.2f}i'.format(self)

    def __add__(self, other: Union[float, Complex]) -> Complex:
        if isinstance(other, float):
            return Complex(self.real + other, self.imag)
        else:
            return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other: Union[float, Complex]) -> Complex:
        if isinstance(other, float) or isinstance(other, Complex):
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

    def __abs__(self) -> float:
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __eq__(self, other: Complex) -> bool:
        if not isinstance(other, Complex):
            return False
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return self.real != other.real or self.imag != other.imag

    def __lt__(self, other):
        return self.abs() < other.abs()

    def __le__(self, other):
        return self.abs() <= other.abs()

    def __gt__(self, other):
        return self.abs() > other.abs()

    def __ge__(self, other):
        return self.abs() >= other.abs()
