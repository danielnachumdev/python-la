from __future__ import annotations
from Vector import Vector
from Field import Field
from Matrix import Matrix
from InnerProduct import StandardInnerProduct


class Span:
    def __init__(self, base: list[Vector]) -> None:
        # if all vectors in base are of the same field add then otherwise throw an error
        for vector in base:
            if vector.field != base[0].field:
                raise ValueError(
                    "Span can only be created from vectors of the same field")
        self.vectors = base

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

    # def isVectorInSpan(self, vec: Vector) -> bool:
