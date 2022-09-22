from __future__ import annotations
from typing import Callable, Any, Union
from .Field import Field
from ..utils import composite_function, isoneof, areinstances
from .Matrix import Matrix
from .Vector import Vector
from .Complex import Complex
from .VectorSpace import VectorSpace


class LinearMap:
    # TODO rethink data structure
    @staticmethod
    def is_func_linear_map(func: Callable[[Any, Field], Union[Vector, Matrix]], src_field: Field, dst_field: Field) -> bool:
        COUNT = 100
        V = VectorSpace(src_field)
        for _ in range(COUNT):
            a, b = src_field.random(), src_field.random()
            v1, v2 = V.random(), V.random()
            try:
                if not func(a*v1+b*v2, dst_field) == (a*func(v1, dst_field)+b*func(v2, dst_field)):
                    pass
            except Exception as e:
                pass
            if not func(a*v1+b*v2, dst_field) == (a*func(v1, dst_field)+b*func(v2, dst_field)):
                return False
        return True

    @staticmethod
    def from_matrix(m: Matrix) -> LinearMap:
        return LinearMap(m.field, type(m.field)(m.field.name), lambda x: m*x)

    @staticmethod
    def from_fields(src_field, dst_field, func: Callable[[Any, Field], Any], validate: bool = False) -> LinearMap:
        return LinearMap(VectorSpace(src_field), VectorSpace(dst_field), func, validate)

    @staticmethod
    def id(field: int) -> LinearMap:
        return LinearMap(field, field, lambda x: x)

    def __init__(self, src: VectorSpace, dst: VectorSpace, func: Callable[[Any], Any], validate: bool = False) -> None:
        """creates a new linear transformation

        Args:
            src_field (Field): The source field which elements form it are called with this opeartor
            dst_field (Field): The Field which is the output oif this transformation
            func (Callable[[Any], Any]): the transformation function
        """
        if not areinstances([src, dst], VectorSpace):
            raise ValueError("src and dst must be of type VectorSpace")
        if not callable(func):
            raise ValueError("func must be a callable")
        if validate:
            if not LinearMap.is_func_linear_map(func, src, dst):
                raise ValueError("func is not a linear transformation")
        self.src = src
        self.dst = dst
        self.func = func

    def __add__(self, other) -> LinearMap:
        # if isoneof(other, [int, float, complex]):
        # return LinearTransformation(self.src_field, self.dst_field, lambda x, y: self.func(x, y)+other*LinearTransformation())
        if isinstance(other, LinearMap):
            if self.src == other.src and self.dst == other.dst:
                return LinearMap(self.src, self.dst, lambda x: self(x)+other(x))
            raise ValueError(
                "cant add linear transformations on diffrent fields")
        raise NotImplementedError(
            "addition with non-numeric type not implemented")

    def __radd__(self, other) -> LinearMap:
        return self.__add__(other)

    def __sub__(self, other) -> LinearMap:
        return self.__add__(-other)

    def __rsub__(self, other) -> LinearMap:
        return other+(-self)

    def __neg__(self) -> LinearMap:
        return self.__mul__(-1)

    def __mul__(self, other) -> LinearMap:
        if isoneof(other, [int, float, Complex]):
            return LinearMap(self.src, self.dst, lambda x: self.func(x)*other)
        if isinstance(other, LinearMap):
            return self(other)
        raise NotImplementedError(
            f"LinearMap * {type(other)} not implemented")

    def __rmul__(self, other) -> LinearMap:
        return self.__mul__(other)

    def __pow__(self, other) -> LinearMap:
        if isoneof(other, [int, float]):
            if not other == int(other) or other < 0:
                raise ValueError(
                    "only non negativ integer powers are implemented and you tried to raise the transformation to {}".format(other))
            if other == 0:
                return LinearMap(self.src, self.dst, lambda x: x)
            if other == 1:
                return self
            other = int(other)
            func = composite_function(self.func, self.func)
            for _ in range(abs(other)-2):
                func = composite_function(func, self.func)
            return LinearMap(self.src, self.dst, lambda x: func(x))
        else:
            raise NotImplementedError(
                "multiplication with non-numeric type not implemented")

    def __eq__(self, other: LinearMap) -> bool:
        if not isinstance(other, LinearMap):
            return False
        if not (self.src == other.src and self.dst == other.dst):
            return False
        return self.to_matrix() == other.to_matrix()

    def __truediv__(self, other: Any):
        """
        Raises:
            NotImplementedError: can't divide linear transformations
        """
        raise NotImplementedError(
            "LineraMap.__truediv__: cant devide Linear Maps")

    def __call__(self, val: Union[Vector, Matrix, LinearMap]) -> Union[Vector, Matrix, LinearMap]:
        """ apply the transformation on an object
        Args:
            v (Any): the object to apply the transformation on

        Raises:
            ValueError: will raise a ValueError if the object is not in the source field
            Exception: if the transformation function itself raises an error

        Returns:
            Any: the return value of the transformation's function
        """
        if not isoneof(val, [Vector, Matrix, LinearMap]):
            raise ValueError(
                "can only apply linear transformations on vectors and matrices")
        # LinearMap
        if isinstance(val, LinearMap):
            if not self.dst == val.src:
                raise ValueError(
                    "outer dst vector space is not equal to inner src vector space")
            return LinearMap(self.src, val.dst, lambda x: self.func(val(x)))

        # Matrix or Vector
        if isinstance(val, Vector):
            if val not in self.src:
                raise ValueError("value is not in the source field")
        else:
            if not Vector(val[i][0] for i in range(val.__rows)).field == self.src:
                raise ValueError("value is not in the source field")
        try:
            return self.func(val)
        except Exception as e:
            raise e

    def to_matrix(self, basis: list[Vector] = None) -> Matrix:
        if basis is None:
            basis = self.src.standard_basis()
        vectors = []
        for v in basis:
            vectors.append(self(v))
        return Matrix.from_vectors(vectors)


class LinearTransformation(LinearMap):
    pass
