from __future__ import annotations
from Matrix import *
from typing import Callable
import Field
from utils import composite_function, isoneof


class LinearTransformation:
    # TODO rethink data structure
    @staticmethod
    def isFuncLinearTransformation(func: Callable[[Any, Field.Field], Union[Vector.Vector, Matrix]], src_field: Field, dst_field: Field) -> bool:
        COUNT = 100
        for _ in range(COUNT):
            a, b = src_field._generate_one(), src_field._generate_one()
            v1, v2 = src_field.random(), src_field.random()
            try:
                if not func(a*v1+b*v2, dst_field).almost_equal(a*func(v1, dst_field)+b*func(v2, dst_field)):
                    pass
            except Exception as e:
                pass
            if not func(a*v1+b*v2, dst_field).almost_equal(a*func(v1, dst_field)+b*func(v2, dst_field)):
                return False
        return True

    @staticmethod
    def fromMatrix(m: Matrix) -> LinearTransformation:
        return LinearTransformation(m.field, type(m.field)(m.field._name), lambda x: m*x)

    @staticmethod
    def id(field: int) -> LinearTransformation:
        return LinearTransformation(field, field, lambda x, y: x)

    def is_invariant_to(span: Span) -> bool:
        pass

    def __init__(self, src_field: Field, dst_field: Field, func: Callable[[Any], Any]) -> None:
        """creates a new linear transformation

        Args:
            src_field (Field): The source field which elements form it are called with this opeartor
            dst_field (Field): The Field which is the output oif this transformation
            func (Callable[[Any], Any]): the transformation function
        """
        if not LinearTransformation.isFuncLinearTransformation(func, src_field, dst_field):
            raise ValueError("func is not a linear transformation")
        self.src_field = src_field
        self.dst_field = dst_field
        self.func = func

    def __add__(self, other) -> LinearTransformation:
        # if isoneof(other, [int, float, complex]):
        # return LinearTransformation(self.src_field, self.dst_field, lambda x, y: self.func(x, y)+other*LinearTransformation())
        if isinstance(other, LinearTransformation):
            if self.src_field == other.src_field and self.dst_field == other.dst_field:
                return LinearTransformation(self.src_field, self.dst_field, lambda x, y: self(x)+other(x))
            raise ValueError(
                "cant add linear transformations on diffrent fields")
        raise NotImplementedError(
            "addition with non-numeric type not implemented")

    def __radd__(self, other) -> LinearTransformation:
        return self.__add__(other)

    def __sub__(self, other) -> LinearTransformation:
        # TODO
        pass

    def __rsub__(self, other) -> LinearTransformation:
        # TODO
        pass

    def __neg__(self) -> LinearTransformation:
        return self.__mul__(-1)

    def __mul__(self, other) -> LinearTransformation:
        if isoneof(other, [int, float, Complex]):
            return LinearTransformation(self.src_field, self.dst_field, lambda x, y: self.func(x, y)*other)
        else:
            raise NotImplementedError(
                "multiplication with non-numeric type not implemented")

    def __rmul__(self, other) -> LinearTransformation:
        return self.__mul__(other)

    def __pow__(self, other) -> LinearTransformation:
        if isoneof(other, [int, float]):
            if not other == int(other) or other < 0:
                raise NotImplementedError(
                    "only non negativ powers are implemented and you tried to raise the transformation to {}".format(other))
            if other == 0:
                return LinearTransformation(self.src_field, self.dst_field, lambda x, y: x)
            if other == 1:
                return self

            other = int(other)
            func = composite_function(self.func, self.func)
            for _ in range(abs(other)-2):
                func = composite_function(func, self.func)
            return LinearTransformation(self.src_field, self.dst_field, lambda x, y: func(x, y))
        else:
            raise NotImplementedError(
                "multiplication with non-numeric type not implemented")

    def __truediv__(self, other) -> LinearTransformation:
        # TODO
        pass

    def __call__(self, v: Any) -> Union[Vector.Vector, Matrix]:
        """ apply the transformation on an object
        Args:
            v (Any): the object to apply the transformation on

        Raises:
            ValueError: will raise a ValueError if the object is not in the source field
            Exception: if the transformation function itself raises an error

        Returns:
            Any: the return value of the transformation's function
        """
        if not v in self.src_field:
            raise ValueError("value is not in the source field")
        try:
            return self.func(v, self.dst_field)
        except Exception as e:
            raise e

    def toMatrix(self, base=None) -> Matrix:
        # TODO implement calculation of operator over specific base
        pass


# class Hom(Field.Field):
#     pass


# class Operator(LinearTransformation):
#     pass
