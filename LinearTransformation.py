from __future__ import annotations
from Matrix import *
from typing import Callable
import Field


class LinearTransformation:
    # TODO rethink data structure
    @staticmethod
    def isFuncLinearTransformation(func: Callable[[Any, Field.Field], Union[Vector.Vector, Matrix]], src_field: Field, dst_field: Field) -> bool:
        COUNT = 100
        for _ in range(COUNT):
            a, b = src_field._generate_one(), src_field._generate_one()
            v1, v2 = src_field.random(), src_field.random()
            if not func(a*v1+b*v2, dst_field).almost_equal(a*func(v1, dst_field)+b*func(v2, dst_field)):
                return False
        return True

    @staticmethod
    def fromMatrix(m: Matrix) -> LinearTransformation:
        return LinearTransformation(m.field, type(m.field)(m.field._name), lambda x: m*x)

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
