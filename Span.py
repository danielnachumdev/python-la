from __future__ import annotations
from typing import Any
from Vector import Vector
from Field import Field
from InnerProduct import StandardInnerProduct


class Span:
    def __init__(self, base: list[Any] = [], validate: bool = False) -> None:
        """
        Initialize a Span object.
        :param base: A list of objects to be used as the base of the span.
        :param validate: If True, the span will be validated as a vector space
        """
        if base != []:
            example_item = base[0]
            T = type(example_item)
            for val in base:
                if not isinstance(val, T):
                    raise TypeError(
                        "All elements of the base must be of the same type")

            if not hasattr(example_item, "field"):
                raise TypeError(
                    "All objects must have a field attribute which is an Instance of class Field")
            # if all vectors in base are of the same field add then otherwise throw an error
            for vector in base:
                if vector.field != example_item.field:
                    raise ValueError(
                        "Span can only be created from vectors of the same field")
        self.vectors = base
        if not self.__are_operators_implementes():
            raise AttributeError(
                "Not all operators are implemented for the class of the objects")

    def __str__(self) -> str:
        result = ""
        for vector in self.vectors:
            result += str(vector)+"\n"
        return result

    def __add__(self, other: Span) -> Span:
        if not Span.isInstance(other):
            raise TypeError("Span can only be added to another Span")
        if len(self.vectors) != len(other.vectors):
            raise ValueError("Spans must have the same length")
        return Span([self.vectors[i] + other.vectors[i] for i in range(len(self.vectors))])

    def __getitem__(self, index: int) -> Vector:
        return self.vectors[index]

    def __iter__(self):
        return iter(self.vectors)

    def __are_operators_implementes(self) -> bool:
        if(len(self.vectors) > 0):
            T = type(self.vectors[0])
            O = object
            try:
                T.__add__
                T.__sub__
                T.__neg__
                T.__mul__
                T.__rmul__
                T.__truediv__
                T.__eq__
                T.__ne__
            except AttributeError:
                return False
            return True
        else:
            return True

    def validate(self) -> bool:
        for i in range(len(self.vectors)-1):
            for j in range(i+1, len(self.vectors)):
                if StandardInnerProduct(self.vectors[i], self.vectors[j]) != 0:
                    return False
        return True

    def append(self, vec: Vector) -> None:
        self.vectors.append(vec)

    def toOrthonormal(self) -> Span:
        result = Span([])
        result.append(self[0].toOrthonormal())
        for i in range(1, len(self.vectors)):
            current = self[i]
            curr_tag = Vector([0 for _ in range(self[0].length)])
            for prev in result:
                curr_tag = curr_tag+StandardInnerProduct(prev, current) * prev
            current = current-curr_tag
            result.append(current.toOrthonormal())
        return result

    def find_hetel(self, v: Vector):
        res: Vector = Vector.generate_vector(v.length, 0)
        f = StandardInnerProduct
        for w in self.vectors:
            res = res + f(v, w)/f(w, w)*w
        return res

    def isVectorInSpan(self, vec: Vector) -> bool:
        pass
