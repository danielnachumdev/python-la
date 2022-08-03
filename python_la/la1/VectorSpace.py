from __future__ import annotations
from typing import Callable
from .Field import Field, RealField
from .Vector import Vector


class VectorSpace:

    def __init__(self, field: Field) -> None:
        self.field = field

    def __str__(self) -> str:
        pass

    def __eq__(self, other: VectorSpace) -> bool:
        if not isinstance(other, VectorSpace):
            raise TypeError("other must be an instance of class VectorSpace")
        return self.field == other.field

    def __ne__(self, other: VectorSpace) -> bool:
        return not self.__eq__(other)

    def __contains__(self, value: Vector) -> bool:
        if not isinstance(value, Vector):
            raise TypeError("value must be an instance of class Vector")
        if value.field == self.field:
            return True
        return False

    def random(self, min: int = -10, max: int = 10) -> Vector:
        return Vector([self.field.random(min, max) for _ in range(self.field.degree)], self.field)

    def standard_basis(self) -> list[Vector]:
        n = self.field.degree
        empty = [0 for _ in range(n)]
        return [Vector(empty[:i]+[1]+empty[i+1:]) for i in range(n)]


# class PolynomialVectorSpace(VectorSpace):
#     pass

# TODO is oclidian, is hermitian
