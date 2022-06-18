from __future__ import annotations
from typing import Any, Union
from Field import Field, Fields
from Complex import Complex

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

    def __str__(self) -> str:
        return str(self.__values)

    def __add__(self, other: Vector) -> Vector:
        if not Vector.isInstance(other):
            raise TypeError("Vector can only be added to another Vector")
        if self.__field != other.__field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] + other.__values[i] for i in range(len(self.__values))])

    def __sub__(self, other: Vector) -> Vector:
        if not Vector.isInstance(other):
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

    @staticmethod
    def isInstance(object: Any) -> bool:
        return isinstance(object, Vector)
