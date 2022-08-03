from __future__ import annotations
from typing import Callable, Any, Union
from .Field import Field
from ..utils import composite_function, isoneof
from .Matrix import Matrix
from .Vector import Vector
from .Complex import Complex
from .VectorSpace import VectorSpace


class LinearMap:
    # TODO rethink data structure
    @staticmethod
    def isFuncLinearTransformation(func: Callable[[Any, Field], Union[Vector, Matrix]], src_field: Field, dst_field: Field) -> bool:
        COUNT = 100
        V = VectorSpace(src_field)
        for _ in range(COUNT):
            a, b = src_field.random(), src_field.random()
            v1, v2 = V.random(), V.random()
            try:
                if not func(a*v1+b*v2, dst_field).almost_equal(a*func(v1, dst_field)+b*func(v2, dst_field)):
                    pass
            except Exception as e:
                pass
            if not func(a*v1+b*v2, dst_field).almost_equal(a*func(v1, dst_field)+b*func(v2, dst_field)):
                return False
        return True

    @staticmethod
    def fromMatrix(m: Matrix) -> LinearMap:
        return LinearMap(m.field, type(m.field)(m.field.name), lambda x: m*x)

    @staticmethod
    def id(field: int) -> LinearMap:
        return LinearMap(field, field, lambda x, y: x)

    def __init__(self, src_field: Field, dst_field: Field, func: Callable[[Any], Any], validate: bool = False) -> None:
        """creates a new linear transformation

        Args:
            src_field (Field): The source field which elements form it are called with this opeartor
            dst_field (Field): The Field which is the output oif this transformation
            func (Callable[[Any], Any]): the transformation function
        """
        if validate:
            if not LinearMap.isFuncLinearTransformation(func, src_field, dst_field):
                raise ValueError("func is not a linear transformation")
        self.src_field = src_field
        self.dst_field = dst_field
        self.func = func

    def __add__(self, other) -> LinearMap:
        # if isoneof(other, [int, float, complex]):
        # return LinearTransformation(self.src_field, self.dst_field, lambda x, y: self.func(x, y)+other*LinearTransformation())
        if isinstance(other, LinearMap):
            if self.src_field == other.src_field and self.dst_field == other.dst_field:
                return LinearMap(self.src_field, self.dst_field, lambda x, y: self(x)+other(x))
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
            return LinearMap(self.src_field, self.dst_field, lambda x, y: self.func(x, y)*other)
        else:
            raise NotImplementedError(
                "multiplication with non-numeric type not implemented")

    def __rmul__(self, other) -> LinearMap:
        return self.__mul__(other)

    def __pow__(self, other) -> LinearMap:
        if isoneof(other, [int, float]):
            if not other == int(other) or other < 0:
                raise ValueError(
                    "only non negativ integer powers are implemented and you tried to raise the transformation to {}".format(other))
            if other == 0:
                return LinearMap(self.src_field, self.dst_field, lambda x, y: x)
            if other == 1:
                return self

            other = int(other)
            func = composite_function(self.func, self.func)
            for _ in range(abs(other)-2):
                func = composite_function(func, self.func)
            return LinearMap(self.src_field, self.dst_field, lambda x, y: func(x, y))
        else:
            raise NotImplementedError(
                "multiplication with non-numeric type not implemented")

    def __truediv__(self, other) -> LinearMap:
        # TODO
        pass

    def __call__(self, v: Union[Vector, Matrix]) -> Union[Vector, Matrix]:
        """ apply the transformation on an object
        Args:
            v (Any): the object to apply the transformation on

        Raises:
            ValueError: will raise a ValueError if the object is not in the source field
            Exception: if the transformation function itself raises an error

        Returns:
            Any: the return value of the transformation's function
        """
        if not isoneof(v, [Vector, Matrix]):
            raise ValueError(
                "can only apply linear transformations on vectors and matrices")
        if isinstance(v, Vector):
            if not v.field == self.src_field:
                raise ValueError("value is not in the source field")
        else:
            if not Vector(v[i][0] for i in range(v.__rows)).field == self.src_field:
                raise ValueError("value is not in the source field")
        try:
            return self.func(v, self.dst_field)
        except Exception as e:
            raise e

    def toMatrix(self, base=None) -> Matrix:
        # TODO implement calculation of operator over specific base
        pass


class LinearTransformation(LinearMap):
    pass
