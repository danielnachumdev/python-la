from __future__ import annotations
from typing import Any
from ..Field import Field
from ..Vector import Vector
from ...BaseClasses import VectorSpace____
from danielutils import validate


class VectorSpace__(VectorSpace____):
    @validate(None, Field)
    def __init__(self, field: Field) -> None:
        """creates a new vector space

        Args:
            field (Field): The field on which the space if over
        """
        self.field = field

    def __str__(self) -> str:
        """returns a string representation of this vector space

        Returns:
            str: a string representation of this vector space
        """
        return f"V_{str(self.field)}"

    def __eq__(self, other: Any) -> bool:
        """checks if this vector space is equal to another vector space

        Args:
            other (VectorSpace): the other vector space

        Raises:
            TypeError: if other is not an instance of VectorSpace

        Returns:
            bool: True if this vector space is equal to the other vector space
        """
        if not isinstance(other, VectorSpace):
            False
        return self.field == other.field

    def __ne__(self, other: Any) -> bool:
        """checks if this vector space is not equal to another vector space

        Args:
            other (VectorSpace): the other vector space

        Raises:
            TypeError: if other is not an instance of VectorSpace

        Returns:
            bool: True if this vector space is not equal to the other vector space
        """
        return not self.__eq__(other)

    def __contains__(self, value: Any) -> bool:
        """checks if a vector is in this vector space

        Args:
            value (Vector): the vector to check

        Raises:
            TypeError: if value is not an instance of Vector

        Returns:
            bool: True if the vector is in this vector space
        """
        if not isinstance(value, Vector):
            False
        if value.field == self.field:
            return True
        return False


class VectorSpace(VectorSpace__):

    def random(self, min: Any = -10, max: Any = 10) -> Vector:
        """returns a random vector in this vector space

        Args:
            min (Any, optional): minimum value for each element in vector. Defaults to -10.
            max (Any, optional): maximum value for each element in vector. Defaults to 10.

        Returns:
            Vector: a random vector in this vector space
        """
        return Vector([self.field.random(min, max) for _ in range(self.field.degree)], self.field)

    @validate(None, int)
    def e(self, i: int) -> Vector:
        """returns the i-th standard basis vector of this vector space

        Args:
            i (int): the index of the basis vector to return

        Raises:
            TypeError: if i is not an integer
            ValueError: if i is not in the range [0, self.field.degree)

        Returns:
            Vector: the i-th standard basis vector of this vector space
        """
        if not (0 < i <= self.field.degree):
            raise ValueError("i must be between 1 and degree")
        arr = [0 if j != i-1 else 1 for j in range(self.field.degree)]
        return Vector(arr, self.field)

    def standard_basis(self) -> list[Vector]:
        """returns the standard basis of this vector space

        Returns:
            list[Vector]: the standard basis of this vector space
        """
        n = self.field.degree
        return [self.e(i+1) for i in range(n)]


__all__ = [
    "VectorSpace"
]
