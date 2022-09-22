from __future__ import annotations
from typing import Union, Callable
import math
import random
from ..utils import alloneof, almost_equal
from danielutils import isoneof, validate, NotImplemented


class Complex__:
    # only purpos is to easily allow type validation
    pass


class Complex(Complex__):

    __int_float = [[int, float], None, None]
    __int_float_complex = [[int, float, Complex__], None, None]

    @staticmethod
    @validate(__int_float, __int_float)
    def from_polar(r: Union[int, float], theta: Union[int, float]) -> Complex:
        real = r * math.cos(theta)
        imag = r * math.sin(theta)
        return Complex(real, imag)

    @staticmethod
    @validate(__int_float, __int_float)
    def from_polar_radians(r: Union[int, float], theta_radians: Union[int, float]) -> Complex:
        return Complex.from_polar(r, theta_radians*180/math.pi)

    @validate(None, __int_float, __int_float)
    def __init__(self, real: Union[int, float], imag: Union[int, float]) -> None:
        self.real = real
        self.imag = imag

    @property
    def r(self) -> float:
        return math.sqrt(self.real**2+self.imag**2)

    @property
    def theta_radians(self) -> float:
        return math.atan(self.imag / self.real)

    @property
    def theta(self) -> float:
        return self.theta_radians * 180/math.pi

    def __str__(self) -> str:
        # get final string for real value
        real = self.real
        if almost_equal(round(self.real), self.real):
            real = str(round(self.real))
        else:
            real = f"{real:.2f}"
        # get final string for imag value
        imag = self.imag
        if almost_equal(round(self.imag), self.imag):
            imag = str(round(self.imag))
        else:
            imag = f"{imag:.2f}"
        # return string
        if real == imag == "0":
            return "0"
        elif real != "0" == imag:
            return real
        elif real == "0" != imag:
            if imag == "1":
                return "i"
            elif imag == "-1":
                return "-i"
            return imag+"i"
        return f'{real} + {imag}i'

    def __repr__(self) -> str:
        return str(self)

    @validate(None, __int_float_complex)
    def __add__(self, other: Union[int, float, Complex]) -> Complex:
        if isoneof(other, [int, float]):
            return Complex(self.real + other, self.imag)
        return Complex(self.real + other.real, self.imag + other.imag)

    @validate(None, __int_float_complex)
    def __radd__(self, other: Union[int, float, Complex]) -> Complex:
        return self.__add__(other)

    @validate(None, __int_float_complex)
    def __mul__(self, other: Union[int, float, Complex]) -> Complex:
        if isoneof(other, [int, float]):
            return Complex(self.real * other, self.imag * other)
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    @validate(None, __int_float_complex)
    def __rmul__(self, other: Union[int, float, Complex]) -> Complex:
        return self.__mul__(other)

    def __neg__(self) -> Complex:
        return Complex(-self.real, -self.imag)

    @validate(None, __int_float_complex)
    def __sub__(self, other: Union[int, float, Complex]) -> Complex:
        return self + (-other)

    @validate(None, __int_float_complex)
    def __rsub__(self, other: Union[int, float, Complex]) -> Complex:
        # other-self==-(self-other)
        return -self.__sub__(other)

    def __abs__(self) -> float:
        return (self.real ** 2 + self.imag ** 2) ** 0.5

    @validate(None, __int_float_complex)
    def __eq__(self, other: Union[int, float, Complex]) -> bool:
        if not isinstance(other, Complex):
            other = Complex(other, 0)
        return almost_equal(self.real, other.real) and almost_equal(self.imag, other.imag)

    @validate(None, __int_float_complex)
    def __ne__(self, other: Union[int, float, Complex]):
        return not self.__eq__(other)

    @validate(None, __int_float_complex)
    def __truediv__(self, other: Union[int, float, Complex]) -> Complex:
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero")

        if not isinstance(other, Complex):
            other = Complex(other, 0)

        nominator = Complex(self.real, self.imag)*other.conjugate
        denominator = other*other.conjugate
        return Complex(nominator.real/denominator.real, nominator.imag/denominator.real)

    @validate(None, __int_float_complex)
    def __rtruediv__(self, other: Union[int, float, Complex]) -> Complex:
        if not isinstance(other, Complex):
            other = Complex(other, 0)
        nominator = other*self.conjugate
        denominator = self*self.conjugate
        return Complex(nominator.real/denominator.real, nominator.imag/denominator.real)

    @validate(None, int)
    def __pow__(self, p: int):
        # TODO look at this again
        # return Complex.fromPolar(self.r**p, self.theta**p)

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

    @NotImplemented
    def __rpow__(self, other):
        pass

    @ property
    def conjugate(self):
        return Complex(self.real, -self.imag)

    @ property
    def norm(self):
        return (self * self.conjugate).real

    @ staticmethod
    @validate(__int_float, __int_float, Callable)
    def random(min_val: float = -10, max_val: float = 10, value_func=random.randint) -> Complex:
        return Complex(value_func(min_val, max_val), value_func(min_val, max_val))
