from __future__ import annotations
import random
from typing import Any, Union
from .Vector import Vector
from .Field import Field
from .VectorSpace import VectorSpace
from ..utils import are_operators_implemnted, concat_horizontally, isoneof, alloneof


class Span:
    # @staticmethod
    # def fromMatrixColumnSpace(m: Matrix) -> Span:
    #     pass

    # @staticmethod
    # def fromMatrixRowSpace(m: Matrix) -> Span:
    #     pass

    @staticmethod
    def span_field(field: Field) -> Span:
        """returns a span of the field

        Args:
            field (Field): field to get the span of

        Raises:
            TypeError: if the field is not of type Field

        Returns:
            Span: span of the field
        """
        if not isinstance(field, Field):
            raise TypeError("field must be of type Field")
        return Span(VectorSpace(field).standard_basis())

    def __init__(self, objects: list[Any]) -> None:
        """initializes the span with the given vectors

        Args:
            vectors (list[Vector], optional): list of vectors to initialize the span with

        Raises:
            TypeError: if the values are not of type type
            AttributeError: if the objects don't have a field attribute
            ValueError: if the objects are not in the same field
            AttributeError: if the objects don't have all nescesary operator implemented
        """
        # if vectors != []:
        example_item = objects[0]
        T = type(example_item)
        for val in objects:
            if not isinstance(val, T):
                raise TypeError(
                    "All elements of the base must be of the same type")

        if not hasattr(example_item, "field"):
            raise AttributeError(
                "All objects must have a field attribute which is an Instance of class Field")
        # if all vectors in base are of the same field add then otherwise throw an error
        self.field = example_item.field
        for vector in objects:
            if vector.field != self.field:
                raise ValueError(
                    "Span can only be created from vectors of the same field")
        self.vectors = objects
        if not are_operators_implemnted(type(self.vectors[0])):
            raise AttributeError(
                "Not all required operators are implemented for the class of the objects")

    @property
    def basis(self) -> Span:
        """returns the basis of the span

        Returns:
            Span: basis of the span
        """
        from .Matrix import Matrix
        result_indecies = []
        for row in Matrix.from_vectors(self.vectors).gaussian_elimination():
            for vec_index, value in enumerate(row):
                if value != self.field.zero:
                    result_indecies.append(vec_index)
                    break
        return Span([self.vectors[i] for i in result_indecies])

    @property
    def dim(self) -> int:
        """returns the dimension of the basis of the span

        Returns:
            int: dimension of the basis of the span
        """
        return len(self.basis)

    @property
    def has_lineary_dependency(self) -> bool:
        """returns whether the span has a lineary dependent vector inside it

        Returns:
            bool: True if the span has a lineary dependent vector inside it, False otherwise
        """
        return self != self.basis

    # FIXME they need inner product
    # def is_orthogonal(self) -> bool:
    #     pass

    # def is_orthonormal(self) -> bool:
    #     return self.toOrthonormal() == self

    def __str__(self, raw: bool = False) -> str:
        """returns a string representation of the span

        Args:
            raw (bool, optional): whether to display raw data or to make it pretty. Defaults to False.

        Returns:
            str: string representation of the span
        """
        if raw:
            res = ""
            for v in self:
                res += v.__str__(raw)+'\n'
            return res
        return concat_horizontally(self.vectors, "\t")

    def __add__(self, other: Union[Vector, Span]) -> Span:
        """returns the span of the vectors in the span plus the given vector or span

        Args:
            other (Union[Vector, Span]): vector or span to add to self

        Raises:
            TypeError: if the other object is not of type Vector or Span
            ValueError: if the other dosen't have the smae field as self

        Returns:
            Span: span of the vectors in the span plus the given vector or span
        """
        if not isoneof(other, [Vector, Span]):
            raise TypeError("Span can only be added to another Span")
        if isinstance(other, Vector):
            other = Span([other])
        if not self.field == other.field:
            raise ValueError("Spans must be in the same field")
        return Span([self.vectors + other.vectors])

    def __sub__(self, other: Union[Vector, Span]) -> Span:
        """returns the span of the vectors in the span minus the given vector or span
            will perform what is mathematically equivelent to: self \ {other}
        Args:
            other (Union[Vector, Span]): vector or span to subtract from self

        Raises:
            TypeError: if the other object is not of type Vector or Span

        Returns:
            Span: span of the vectors in the span minus the given vector or span
        """
        if not isoneof(other, [Vector, Span]):
            raise TypeError("Span can only be subtracted by Vector|Span")
        if isinstance(other, Vector):
            other = Span([other])
        res = set(self.vectors) - set(other.vectors)
        return Span(list(res))

    def __getitem__(self, index: int) -> Vector:
        """returns the vector at the given index

        Args:
            index (int): index of the vector to return

        Raises:
            ValueError: if the index is out of range
        Returns:
            Vector: vector at the given index
        """
        if not (0 <= index < len(self)):
            raise ValueError("index out of range")
        return self.vectors[index]

    def __iter__(self):
        """iterates over the vectors in the span

        Returns:
            a list iterator for the vectors in the span
        """
        return iter(self.vectors)

    def __len__(self) -> int:
        """returns the number of vectors in the span

        Returns:
            int: number of vectors in the span
        """
        return len(self.vectors)

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

    def __hash__(self) -> int:
        """returns a hash value for the span

        Returns:
            int: hash value for the span
        """
        return hash((v for v in self))

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Span):
            return self.vectors == other.vectors
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
            res = Matrix.from_vectors(self.vectors).solve(vector) != None
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

    def to_orthonormal(self) -> Span:
        """returns a span that is orthonormal representation of self in the same order

        Returns:
            Span: orthonormal representation of self
        """
        result = [self[0].normalize()]
        from ..la2 import StandardInnerProduct as sip
        for i in range(1, len(self.vectors)):
            current = self[i]
            curr_tag = Vector([0 for _ in range(self[0].length)])
            for prev in result:
                curr_tag = curr_tag+sip(prev, current) * prev
            current = current-curr_tag
            result.append(current.normalize())
        return Span(result)

    def projection_of(self, v: Vector) -> Vector:
        """returns the projection of a vector onto the span

        Args:
            v (Vector): vector to project

        Raises:
            TypeError: if the vector is not of type Vector

        Returns:
            Vector: projection of the vector onto the span
        """
        if not isinstance(v, Vector):
            raise TypeError("can only project vectors")
        res: Vector = Vector.from_size(len(v), 0)
        for w in self.to_orthonormal():
            res += v.projection_onto(w)
        return res

    def random(self, min: int = -10, max: int = 10) -> Vector:
        """Creates a random vector from the span

        Args:
            min (int, optional): the minimum value for the scalars in the linear dependecy. Defaults to -10.
            max (int, optional): the maximum value for the scalars in the linear dependecy. Defaults to 10.
        Raises:
            TypeError: if min and/or max are not [int, float]
        Returns:
            Vector: a random vector from the span
        """
        if not alloneof([min, max], [int, float]):
            raise TypeError("min and max must be of type int or float")
        res = Vector.from_size(len(self[0]), 0)
        for v in self:
            res += random.uniform(min, max) * v
        return res

    def is_spanning(self, field: Field) -> bool:
        # TODO implement this
        raise NotImplementedError("")
