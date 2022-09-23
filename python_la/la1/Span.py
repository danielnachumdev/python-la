from __future__ import annotations
import random
from typing import Any, Union, Sequence
from .Vector import Vector
from .Field import Field
from .VectorSpace import VectorSpace
from ..utils import are_operators_implemnted, concat_horizontally, alloneof
from danielutils import validate, isoneof, areoneof
from .BaseClasses import Span____


class Span__(Span____):
    @validate(None, [Sequence, lambda seq: areoneof(seq, [Vector])], Vector)
    def __init__(self, objects: list[Vector], offset: Vector = None) -> None:
        """initializes the span with the given vectors

        Args:
            vectors (list[Vector], optional): list of vectors to initialize the span with

        Raises:
            TypeError: if the values are not of type type
            AttributeError: if the objects don't have a field attribute
            ValueError: if the objects are not in the same field
            AttributeError: if the objects don't have all nescesary operator implemented
        """
        example_item = objects[0]
        for v in objects:
            if not v.field == example_item.field:
                raise ValueError(
                    "Span must be initialized with vectors in the same field")
        # # if vectors != []:
        # T = type(example_item)
        # for val in objects:
        #     if not isinstance(val, T):
        #         raise TypeError(
        #             "All elements of the base must be of the same type")

        # if not hasattr(example_item, "field"):
        #     raise AttributeError(
        #         "All objects must have a field attribute which is an Instance of class Field")
        # if all vectors in base are of the same field add then otherwise throw an error
        self.field: Field = example_item.field
        # for vector in objects:
        #     if vector.field != self.field:
        #         raise ValueError(
        #             "Span can only be created from vectors of the same field")
        self.vectors = objects
        if not are_operators_implemnted(type(self.vectors[0])):
            raise AttributeError(
                "Not all required operators are implemented for the class of the objects")

    @validate(None, bool)
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

    @validate(None, [[Vector, Span____], None, None])
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
        if isinstance(other, Vector):
            other = Span([other])
        if not self.field == other.field:
            raise ValueError("Spans must be in the same field")
        return Span(list(set(self.vectors + other.vectors)))

    # def __sub__(self, other: Union[Vector, Span]) -> Span:
    #     """returns the span of the vectors in the span minus the given vector or span
    #         will perform what is mathematically equivelent to: self \ {other}
    #     Args:
    #         other (Union[Vector, Span]): vector or span to subtract from self

    #     Raises:
    #         TypeError: if the other object is not of type Vector or Span

    #     Returns:
    #         Span: span of the vectors in the span minus the given vector or span
    #     """
    #     if not isoneof(other, [Vector, Span]):
    #         raise TypeError("Span can only be subtracted by Vector|Span")
    #     if isinstance(other, Vector):
    #         other = Span([other])
    #     res = set(self.vectors) - set(other.vectors)
    #     return Span(list(res))

    @validate(None, int)
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

    @validate(None, Vector)
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
        return vector in self.vectors

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


class Span(Span__):
    @staticmethod
    @validate(Span__, Span__)
    def are_same_span(s1: Span, s2: Span) -> bool:
        """checks whether two spans are the same

        Args:
            s1 (Span): first span to check
            s2 (Span): second span to check

        Returns:
            bool: True if the two spans are the same, False otherwise
        """
        if s1.field != s2.field:
            return False
        s1 = s1.basis
        s2 = s2.basis

        max_dim = s1.field.degree  # ==s2.field.degree
        # dimention constraints
        if s1.dim == s2.dim == max_dim:
            return True
        elif (s1.dim == max_dim and s2.dim < max_dim) or (s1.dim < max_dim and s2.dim == max_dim):
            return False

        for v in s1:
            if not s2.contains(v):
                return False
        for v in s2:
            if not s1.contains(v):
                return False
        return True

    @staticmethod
    @validate(Field)
    def span_field(field: Field) -> Span:
        """returns a span of the field

        Args:
            field (Field): field to get the span of

        Raises:
            TypeError: if the field is not of type Field

        Returns:
            Span: span of the field
        """
        return Span(VectorSpace(field).standard_basis())

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
        # FIXME: this is not correct, or is it?
        return self != self.basis

    # FIXME they need inner product
    # def is_orthogonal(self) -> bool:
    #     pass

    # def is_orthonormal(self) -> bool:
    #     return self.toOrthonormal() == self

    @validate(None, Vector)
    def remove(self, vec: Vector) -> None:
        """removes a vector from the span

        Args:
            vec (Vector): vector to remove

        Raises:
            TypeError: if the vector is not of type Vector

        Returns:
            bool: True if the vector was removed, False otherwise
        """
        if vec in self.vectors:
            self.vectors.remove(vec)

    @validate(None, int)
    def remove_at(self, index: int) -> None:
        """removes the vector at the given index from the span

        Args:
            index (int): index of the vector to remove

        Raises:
            TypeError: if the index is not of type int
            ValueError: if the index is out of range
        """
        if not (0 <= index < len(self)):
            raise ValueError("index out of range")
        self.vectors.pop(index)

    @validate(None, Vector)
    def contains(self, vector: Vector) -> bool:
        """checks whether there is a linear combinations of vectors in the span that equals the vector

        Args:
            vector (Vector): vector to check

        Raises:
            TypeError: if the vector is not of type Vector

        Returns:
            bool: True if the vector is in the span, False otherwise
        """
        from .Matrix import Matrix
        res = False
        try:
            res = Matrix.from_vectors(self.vectors).solve(vector) != None
        except NotImplementedError:
            res = True
        return res

    def to_orthonormal(self) -> Span:
        """returns a span that is orthonormal representation of self in the same order

        Returns:
            Span: orthonormal representation of self
        """
        result = [self[0].normalize()]
        from ..la2 import StandardInnerProduct as sip
        for i in range(1, len(self.vectors)):
            current = self[i]
            curr_tag = Vector([0 for _ in range(len(self[0]))])
            for prev in result:
                curr_tag = curr_tag+sip(prev, current) * prev
            current = current-curr_tag
            result.append(current.normalize())
        return Span(result)

    @validate(None, Vector)
    def projection_of(self, v: Vector) -> Vector:
        """returns the projection of a vector onto the span

        Args:
            v (Vector): vector to project

        Raises:
            TypeError: if the vector is not of type Vector

        Returns:
            Vector: projection of the vector onto the span
        """
        res: Vector = Vector.from_size(len(v), 0)
        for w in self.to_orthonormal():
            res += v.projection_onto(w)
        return res

    @validate(None, [[int, float], None, None], [[int, float], None, None])
    def random(self, min: Union[int, float] = -10, max: Union[int, float] = 10) -> Vector:
        """Creates a random vector from the span

        Args:
            min (int, optional): the minimum value for the scalars in the linear dependecy. Defaults to -10.
            max (int, optional): the maximum value for the scalars in the linear dependecy. Defaults to 10.
        Raises:
            TypeError: if min and/or max are not [int, float]
        Returns:
            Vector: a random vector from the span
        """
        res = Vector.from_size(len(self[0]), 0)
        for v in self:
            res += random.uniform(min, max) * v
        return res
