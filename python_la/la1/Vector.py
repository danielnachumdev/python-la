from __future__ import annotations
from ..utils import almost_equal, isoneof
from typing import Union, Any
from .Field import Field, RealField
from .Complex import Complex


class Vector:

    @staticmethod
    def random(min: float = -10, max: float = 10, degree: int = 10,  def_value=None, f: Field = RealField()) -> Vector:
        return Vector([f.random(min, max) if def_value is None else def_value for _ in range(degree)])

    @staticmethod
    def fromSize(size: int, field: Field, default_value: Any = None) -> Vector:
        """Create a vector of the given size with the given field and default value

        Args:
            size (int): the size of the vector
            field (Field): the field of the vector
            default_value (Any, optional): the value to intialize the vector with. if is None will default to field._zero.

        Returns:
            Vector: a vector of the given size with the given field and default value
        """
        if default_value is None:
            default_value = field.zero
        return Vector([default_value for _ in range(size)], field)

    @staticmethod
    def e(i: int, size: int, field: Field) -> Vector:
        v = Vector.fromSize(size, field, field.zero)
        v[i] = field.one
        return v

    def __init__(self, values: list[Any], field: Field = None) -> None:
        self.__values = values
        # TODO add default field detection
        self.field = RealField(len(values)) if not field else field
        self._max_str_length = self._calculate_max_str_length()

    @property
    def length(self):
        return len(self.__values)

    @property
    def conjugate(self) -> Vector:
        return [v.conjugate if isinstance(v, Complex) else v for v in self]

    @property
    def has_no_zero(self) -> bool:
        for v in self:
            if v != 0:
                return True
        return False

    def _calculate_max_str_length(self) -> int:
        res = 0
        for v in self:
            l = len(str(v))
            res = max(res, l)
        return res

    def __str__(self, raw: bool = False) -> str:
        if raw:
            result = "["
            for v in self:
                result += str(v) + ", "
            return result[:-2]+"]"
        res = ""
        hs = "|"+"-"*(self._max_str_length+2)+"|\n"
        res += hs
        for v in self:
            res += "|"+str(v).center(self._max_str_length+2)+"|\n"
            res += hs
        return res

    def __add__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be added to another Vector")
        if self.field != other.field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self[i] + other[i] for i in range(len(self))], self.field)

    def __radd__(self, other) -> Vector:
        return self.__add__(other)

    def __sub__(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(
                "Vector can only be subtracted from another Vector")
        if self.field != other.field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] - other.__values[i] for i in range(len(self.__values))], self.field)

    def __rsub__(self, other) -> Vector:
        return (-self) + other

    def __neg__(self) -> Vector:
        return Vector([-self.__values[i] for i in range(len(self.__values))], self.field)

    def __mul__(self, num: float) -> Vector:
        return Vector([num * self.__values[i] for i in range(len(self.__values))], self.field)

    def __rmul__(self, num: float) -> Vector:
        return self.__mul__(num)

    def __truediv__(self, other) -> Vector:
        if isoneof(other, [int, float, Complex]):
            return self.__mul__(1/other)
        raise ValueError("cant divide vector")

    def __rtruediv__(self, num: float) -> Vector:
        raise ValueError("cant divide by vector")

    def __getitem__(self, index: int) -> Union[int, float, Complex]:
        return self.__values[index]

    def __setitem__(self, index: int, value: Any) -> None:
        if not isinstance(index, int):
            raise TypeError("index must be an integer")
        if not (0 <= index < len(self)):
            raise ValueError("index out of range")
        # FIXME validate tha value is valid
        self.__values[index] = value

    def __iter__(self):
        return iter(self.__values)

    def __eq__(self, other: Vector) -> bool:
        if not isoneof(other, [Vector, list]):
            return False
        if isinstance(other, Vector):
            other = other.__values
        if len(self) != len(other):
            return False
        return self.__values == other

    def __ne__(self, other: Vector) -> bool:
        return not (self == other)

    def __len__(self) -> int:
        return self.length

    def __hash__(self) -> int:
        return hash((v for v in self))

    def almost_equal(self, other: Vector) -> bool:
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be compared to another Vector")
        if not self.field == other.field:
            raise ValueError("Vectors must have the same field")
        return all([almost_equal(self[i], other[i]) for i in range(len(self))])

    def set(self, index, value) -> None:
        self.__values[index] = value

    def norm(self) -> float:
        return sum([x ** 2 for x in self]) ** 0.5

    def dot(self, other: Vector) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be multiplied by another Vector")
        if self.field != other.field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] * other.__values[i] for i in range(len(self.__values))])

    def toOrthonormal(self) -> Vector:
        # TODO change name to Normalize?
        return self / self.norm()

    def projection_onto(self, value) -> Vector:
        """
        return the projection of self onto value which can be another vector or a Span
        """
        from .Span import Span
        if not isoneof(value, [Vector, Span]):
            raise TypeError("v must be of type Vector or Span")
        is_span = isinstance(value, Span)
        if not is_span and len(value) != len(self):
            raise ValueError("value must have the same length as self")
        if is_span and len(value[0]) != len(self):
            raise ValueError(
                "the span's vectors must have the same length as self")
        from ..la2.InnerProduct import StandardInnerProduct as sip
        if not is_span:
            return sip(self, value)/sip(value, value)*value
        else:
            return value.projection_of(self)

    def copy(self) -> Vector:
        return Vector(self.__values, self.field)
