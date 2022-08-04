from __future__ import annotations
from typing import Any
from .Vector import Vector
from .Field import Field
from ..utils import are_operators_implemnted, concat_horizontally


class Span:
    # @staticmethod
    # def fromMatrixColumnSpace(m: Matrix) -> Span:
    #     pass

    # @staticmethod
    # def fromMatrixRowSpace(m: Matrix) -> Span:
    #     pass

    @staticmethod
    def spanField(field: Field) -> Span:
        """
        will return the standard span over F^n e.g : [e1,e2,...,en]
        """
        vecs = []
        for i in range(field.degree):
            v = Vector.fromSize(field.degree, field.zero)
            v[i] = field.one
            vecs.append(v)
        return Span(vecs)

    def __init__(self, vectors: list[Vector] = []) -> None:
        """
        Initialize a Span object.
        :param base: A list of objects to be used as the base of the span.
        :param validate: If True, the span will be validated as a vector space
        """
        if vectors != []:
            example_item = vectors[0]
            T = type(example_item)
            for val in vectors:
                if not isinstance(val, T):
                    raise TypeError(
                        "All elements of the base must be of the same type")

            if not hasattr(example_item, "field"):
                raise TypeError(
                    "All objects must have a field attribute which is an Instance of class Field")
            # if all vectors in base are of the same field add then otherwise throw an error
            self.field = example_item.field
            for vector in vectors:
                if vector.field != self.field:
                    raise ValueError(
                        "Span can only be created from vectors of the same field")
        self.vectors = vectors
        if not are_operators_implemnted(type(self.vectors[0])):
            raise AttributeError(
                "Not all required operators are implemented for the class of the objects")

    @property
    def basis(self) -> Span:
        from .Matrix import Matrix
        result_indecies = []
        for row in Matrix.fromVectors(self.vectors).gaussian_elimination():
            for vec_index, value in enumerate(row):
                if value != self.field.zero:
                    result_indecies.append(vec_index)
                    break
        return Span([self.vectors[i] for i in result_indecies])

    @property
    def dim(self) -> int:
        return len(self.basis)

    @property
    def has_lineary_dependency(self) -> bool:
        pass

    @property
    def is_orthogonal(self):
        pass

    @property
    def is_orthonormal(self):
        from .Matrix import Matrix
        return self.toOrthonormal() == self

    def __str__(self, raw: bool = False) -> str:
        """returns a string representation of the span
            will print all the vectors in the span
        Returns:
            str: string representation of the span
        """
        if raw:
            res = ""
            for v in self:
                res += v.__str__(raw)+'\n'
            return res
        return concat_horizontally(self.vectors, "\t")

    def __add__(self, other: Span) -> Span:
        if not isinstance(other, Span):
            raise TypeError("Span can only be added to another Span")
        if len(self.vectors) != len(other.vectors):
            raise ValueError("Spans must have the same length")
        return Span([self.vectors[i] + other.vectors[i] for i in range(len(self.vectors))])

    def __getitem__(self, index: int) -> Vector:
        return self.vectors[index]

    def __iter__(self):
        return iter(self.vectors)

    def __len__(self) -> int:
        return len(self.vectors)
    # def validate(self) -> bool:
    #     from InnerProduct import StandardInnerProduct
    #     for i in range(len(self.vectors)-1):
    #         for j in range(i+1, len(self.vectors)):
    #             if StandardInnerProduct(self.vectors[i], self.vectors[j]) != 0:
    #                 return False
    #     return True

    def __contains__(self, vector: Vector) -> bool:
        """checks whether a vector is one of the original elements creating the span

        Args:
            vector (Vector): vector to check

        Raises:
            TypeError: if the vector is not of type Vector

        Returns:
            bool: True if the vector is in the span, False otherwise
        """
        if not isinstance(vector, Vector):
            raise TypeError(
                "can only check containment of objects of type 'Vector'")
        for v in self.vectors:
            if vector == v:
                return True
        return False

    def contains(self, vector: Vector) -> bool:
        """checks whether there is a linear combinations of vectors in the span that equals the vector

        Args:
            vector (Vector): vector to check

        Raises:
            TypeError: if the vector is not of type Vector

        Returns:
            bool: True if the vector is in the span, False otherwise
        """
        if not isinstance(vector, Vector):
            raise TypeError(
                "can only check containment of objects of type 'Vector'")
        from .Matrix import Matrix
        res = False
        try:
            res = Matrix.fromVectors(self.vectors).solve(vector) != None
        except ValueError:
            res = True
        return res

    def append(self, vec: Vector) -> None:
        """adds a vector to the span

        Args:
            vec (Vector): vector to add

        Raises:
            TypeError: if the vector is not of type Vector
            ValueError: if the vector is not in the field of the span
        """
        if not isinstance(vec, Vector):
            raise TypeError("can only append vectors")
        if not vec.field == self.field:
            raise ValueError("can only append vectors of the same field")
        self.vectors.append(vec)

    def toOrthonormal(self) -> Span:
        result = [self[0].toOrthonormal()]
        from ..la2 import StandardInnerProduct as sip
        for i in range(1, len(self.vectors)):
            current = self[i]
            curr_tag = Vector([0 for _ in range(self[0].length)])
            for prev in result:
                curr_tag = curr_tag+sip(prev, current) * prev
            current = current-curr_tag
            result.append(current.toOrthonormal())
        return Span(result)

    def projection_of(self, v: Vector) -> Vector:
        """
        returns the vector projection of vector v on the span (=self)
        """
        res: Vector = Vector.fromSize(len(v), 0)
        for w in self.toOrthonormal():
            res += v.projection_onto(w)
        return res

    def random(self, min: Any = -10, max: Any = 10) -> Vector:
        return self.field.random(min, max)

    def is_spanning(self, field: Field) -> bool:
        # TODO implement this
        raise NotImplementedError("")
