from __future__ import annotations
from typing import Union
import random


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

    @property
    def conjugate(self):
        return Complex(self.real, -self.imag)

    def __eq__(self, other: Complex) -> bool:
        if not isinstance(other, Complex):
            return False
        return self.real == other.real and self.imag == other.imag

    def __ne__(self, other):
        return self.real != other.real or self.imag != other.imag

    @property
    def norm(self):
        return self.real**2+self.imag**2

    @staticmethod
    def generate(min_val: float = -10, max_val: float = 10, value_func=random.randint) -> Complex:
        return Complex(value_func(min_val, max_val), value_func(min_val, max_val))
