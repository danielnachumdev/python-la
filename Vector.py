from __future__ import annotations
from typing import Any, Union
from Field import Field, Fields
from Complex import Complex
import random

t_vector = list[Union[float, Complex]]


class Vector:
    def __init__(self, values: t_vector, field: Field = None) -> None:
        self.__values = values
        self.__field = field

    @property
    def field(self) -> Field:
        return self.__field

    @property
    def length(self):
        return len(self.__values)

    @property
    def adjoint(self) -> Vector:
        # TODO complex
        return self.copy()

    def __str__(self) -> str:
        return str(self.__values)

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be added to another Vector")
        if self.__field != other.__field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] + other.__values[i] for i in range(len(self.__values))])

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(
                "Vector can only be subtracted from another Vector")
        if self.__field != other.__field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] - other.__values[i] for i in range(len(self.__values))])

    def __neg__(self) -> Vector:
        return Vector([-self.__values[i] for i in range(len(self.__values))])

    def __mul__(self, num: float) -> Vector:
        return Vector([num * self.__values[i] for i in range(len(self.__values))])

    def __rmul__(self, num: float) -> Vector:
        return self.__mul__(num)

    def __truediv__(self, num: float) -> Vector:
        return self * (1 / num)

    def __getitem__(self, index: int) -> Union[float, Complex]:
        return self.__values[index]

    def __iter__(self):
        return iter(self.__values)

    def __eq__(self, other: Vector) -> bool:  # TODO: do i want to raise errors?
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be compared to another Vector")
        if self.__field != other.__field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return self.__values == other.__values

    def __ne__(self, other: Vector) -> bool:
        return not (self == other)

    def set(self, index, value) -> None:
        self.__values[index] = value

    def norm(self) -> float:
        return sum([x ** 2 for x in self]) ** 0.5

    def dot(self, other: Vector) -> Vector:
        if not Vector.isInstance(other):
            raise TypeError("Vector can only be multiplied by another Vector")
        if self.__field != other.__field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] * other.__values[i] for i in range(len(self.__values))])

    def toOrthonormal(self) -> Vector:
        return self / self.norm()

    def projection_onto(self, value: Vector) -> Vector:
        if not isinstance(value, Vector):  # or not isinstance(value, Span):
            raise TypeError("v must be of type Vector")
        if value.length != self.length:
            raise ValueError("v must have the same length as self")
        from InnerProduct import StandardInnerProduct as sip
        return sip(self, value)/sip(value, value)*value

    def copy(self) -> Vector:
        return Vector(self.__values, self.__field)

    @staticmethod
    def generate_vector(size: int,  def_value: bool = None, f: Field = None) -> Vector:
        if f is None:
            f = Fields.R
        # return Vector([f.random() for _ in range(size)])
        # TODO
        MIN_VAL = -100
        MAX_VAL = 100
        F = random.uniform
        return Vector([F(MIN_VAL, MAX_VAL) if def_value is None else def_value for _ in range(size)])
