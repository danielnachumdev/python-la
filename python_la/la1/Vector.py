from __future__ import annotations
from functools import reduce
from ..utils import almost_equal, areinstances
from typing import Union, Any, Sequence
from .Field import Field, RealField
from .Complex import Complex
from danielutils import validate, isoneof
from .BaseClasses import Vector____


class Vector__(Vector____):
    @validate(None, Sequence, Field)
    def __init__(self, values: list[Any], field: Field = None) -> None:
        """Initialize a vector with the given values and field

        Args:
            values (list[Any]): the values of the vector
            field (Field, optional): if None Defaults to RealField(len(values)).
        """
        self.__values = values
        # TODO add default field detection
        self.field = RealField(len(values)) if not field else field

    @validate(None, bool)
    def __str__(self, raw: bool = False) -> str:
        """Return a string representation of the vector

        Args:
            raw (bool, optional): wheter to print raw data ot to pretty print it. Defaults to False.

        Returns:
            str: a string representation of the vector
        """
        if raw:
            result = "["
            for v in self:
                result += str(v) + ", "
            return result[:-2]+"]"
        max_individual_length = reduce(lambda sub_res, value: max(
            sub_res, len(str(value))), self.__values, 0)
        res = ""
        hs = "|"+"-"*(max_individual_length+2)+"|\n"
        res += hs
        for v in self:
            res += "|"+str(v).center(max_individual_length+2)+"|\n"
            res += hs
        return res

    @validate(None, Vector____)
    def __add__(self, other: Vector) -> Vector:
        """Add two vectors together

        Args:
            other (Vector): the vector to add to self

        Raises:
            TypeError: if other is not a vector
            ValueError: if the vectors have different fields
            ValueError: if the vectors have different lengths

        Returns:
            Vector: the sum of the two vectors
        """
        if self.field != other.field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self[i] + other[i] for i in range(len(self))], self.field)

    @validate(None, Vector____)
    def __radd__(self, other: Vector) -> Vector:
        """Add a vector to a number

        Args:
            other (Vector): the vector to add to self

        Raises:
            whatever __add__ raises

        Returns:
            Vector: the sum of the two vectors
        """
        try:
            return self.__add__(other)
        except Exception as e:
            raise e

    @validate(None, Vector____)
    def __sub__(self, other: Vector) -> Vector:
        """Subtract two vectors

        Args:
            other (Vector): the vector to subtract from self

        Raises:
            TypeError: if other is not a vector
            ValueError: if the vectors have different fields
            ValueError: if the vectors have different lengths

        Returns:
            Vector: the difference of the two vectors
        """
        if self.field != other.field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] - other.__values[i] for i in range(len(self.__values))], self.field)

    @validate(None, Vector____)
    def __rsub__(self, other: Vector) -> Vector:
        """Subtract a vector from a number

        Args:
            other (Vector): the vector to subtract from self

        Raises:
            whatever __neg__ or __add__ raises

        Returns:
            Vector: the difference of the two vectors
        """
        try:
            return (-self) + other
        except Exception as e:
            raise e

    def __neg__(self) -> Vector:
        """Negate a vector
            x => -x
        Returns:
            Vector: the negated vector
        """
        return Vector([-self.__values[i] for i in range(len(self.__values))], self.field)

    @validate(None, [[int, float, Complex], None, None])
    def __mul__(self, num: Union[int, float, Complex]) -> Vector:
        """ Multiply a vector by a number or a complex number

        Args:
            num (Union[int, float, Complex]): the number to multiply the vector by

        Raises:
            TypeError: if num is not a number

        Returns:
            Vector: the multiplied vector
        """
        return Vector([num * self.__values[i] for i in range(len(self.__values))], self.field)

    @validate(None, [[int, float, Complex], None, None])
    def __rmul__(self, num: Union[int, float, Complex]) -> Vector:
        """Multiply a vector by a number

        Args:
            num (float): the number to multiply the vector by

        Raises:
            whatever __mul__ raises

        Returns:
            Vector: the product of the vector and the number
        """
        try:
            return self.__mul__(num)
        except Exception as e:
            raise e

    @validate(None, [[int, float, Complex], None, None])
    def __truediv__(self, other: Union[int, float, Complex]) -> Vector:
        """Divide a vector by a number or a complex number

        Args:
            other (Union[int, float, Complex]): the number to divide the vector by

        Raises:
            Exception: whatever __mul__ raises
            ValueError: if other is a vector, vector/vector is not defined

        Returns:
            Vector: the divided vector
        """
        try:
            if isoneof(other, [int, float, Complex]):
                return self.__mul__(1/other)
        except Exception as e:
            raise e
        raise ValueError("cant divide by a vector")

    def __rtruediv__(self, _):
        """Divide a vector by a number or a complex number

        Raises:
            ValueError: */vector is not defined
        """
        raise ValueError("cant divide by a vector")

    @validate(None, int)
    def __getitem__(self, index: int) -> Any:
        """Get the value at a given index

        Args:
            index (int): the index of the value to get

        Raises:
            TypeError: if index is not an int
            IndexError: if index is out of range

        Returns:
            Any: the value at the given index
        """
        if not (0 <= index < len(self)):
            raise IndexError("Vector index out of range")
        return self.__values[index]

    @validate(None, int, None)
    def __setitem__(self, index: int, value: Any) -> None:
        """Set the value at a given index

        Args:
            index (int): the index of the value to set
            value (Any): the value to set at the given index

        Raises:
            TypeError: if index is not an int
            ValueError: if the value is not in the field
        """
        if not (0 <= index < len(self)):
            raise ValueError("index out of range")
        # FIXME validate tha value is valid
        self.__values[index] = value

    def __iter__(self):
        """Iterate over the values in the vector

        Returns:
            list iterator for all the elements in the vector
        """
        return iter(self.__values)

    @validate(None, Vector____, bool, bool)
    def __eq__(self, other: Vector, use_almost_equal: bool = True, check_field_equality: bool = True) -> bool:
        """Check if two vectors are equal

        Args:
            other (Vector): the vector to compare to self
            use_almost_equal (bool, optional): wheter to use 'almost_equal' functions. Defaults to True.
            check_field_equality (bool, optional): wheter to check if the fields are identical. Defaults to True.

        Raises:
            TypeError: if use_almost_equal and check_field_equality are not booleans

        Returns:
            bool: True if the vectors are equal, False otherwise
        """
        if check_field_equality:
            if self.field != other.field:
                return False
        if len(self) != len(other):
            return False

        def compare_func(a, b): return a == b
        if use_almost_equal:
            compare_func = almost_equal

        for i in range(len(self)):
            if not compare_func(self[i], other[i]):
                return False
        return True

    @validate(None, Vector____, bool, bool)
    def __ne__(self, other: Vector, use_almost_equal: bool = True, check_field_equality: bool = True) -> bool:
        """Check if two vectors are not equal

        Args:
            other (Vector): the vector to compare to self
            use_almost_equal (bool, optional): wheter to use 'almost_equal' functions. Defaults to True.
            check_field_equality (bool, optional): wheter to check if the fields are identical. Defaults to True.

        Raises:
            raises the same as __eq__

        Returns:
            bool: True if the vectors are not equal, False otherwise
        """
        try:
            return not self.__eq__(other, use_almost_equal, check_field_equality)
        except Exception as e:
            raise e

    def __len__(self) -> int:
        """Get the length of the vector

        Returns:
            int: the length of the vector
        """
        return len(self.__values)

    def __hash__(self) -> int:
        """Get the hash of the vector

        Returns:
            int: the hash of the vector
        """
        return hash((v for v in self))


class Vector(Vector__):

    @staticmethod
    @validate()
    def random(min: Any = -10, max: Any = 10, size: int = 10,  def_value: Any = None, f: Field = RealField()) -> Vector:
        """Generate a random vector with random values in the given range.

        Args:
            min (Any, optional): the minimum value for each element. Defaults to -10.
            max (Any, optional): the maximum value for each element. Defaults to 10.
            size (int, optional): the size of the vector. Defaults to 10.
            def_value (Any, optional): Default value to be put in all of the elements. Defaults to None.
            f (Field, optional): the field from which to genetare elements. Defaults to RealField().

        Raises:
            TypeError: size must be an integer
            ValueError: size must be greater than 0

        Returns:
            Vector: a random vector
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if not (0 < size):
            raise ValueError("size must be greater than 0")
        return Vector([f.random(min, max) if def_value is None else def_value for _ in range(size)])

    @staticmethod
    @validate(int, Field, None)
    def from_size(size: int, field: Field, default_value: Any = None) -> Vector:
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
        return Vector([default_value for _ in range(size)], field.__class__(size, field.modulu))

    @ staticmethod
    @validate(int, int, Field)
    def e(i: int, size: int, field: Field) -> Vector:
        """Create the ith element of the e vector of the given size and field

        Args:
            i (int): the index in which to put field.one
            size (int): the size of the vector
            field (Field): the field of the vector

        Returns:
            Vector: the ith element of the e vector of the given size and field
        """
        v = Vector.from_size(size, field, field.zero)
        v[i] = field.one
        return v

    @ property
    def conjugate(self) -> Vector:
        """Return the conjugate of the vector

        Returns:
            Vector: the conjugate of the vector
        """
        arr = []
        for v in self:
            if getattr(v, "conjugate", None):
                if callable(getattr(v, "conjugate")):
                    arr.append(v.conjugate())
                else:
                    arr.append(v.conjugate)
            else:
                arr.append(v)
        return Vector(arr)

    def norm(self) -> float:
        """Get the norm of the vector

        Returns:
            float: the norm of the vector
        """
        return sum([x ** 2 for x in self]) ** 0.5

    @validate(None, Vector__)
    def dot(self, other: Vector) -> Vector:
        """Get the dot product of two vectors

        Args:
            other (Vector): the vector to dot with self

        Raises:
            TypeError: if other is not a vector
            ValueError: if the vectors are not in the same field
            ValueError: if the vectors are not the same length

        Returns:
            Vector: the dot product of the vectors
        """
        if not isinstance(other, Vector):
            raise TypeError("Vector can only be multiplied by another Vector")
        if self.field != other.field:
            raise ValueError("Vectors must have the same field")
        if len(self.__values) != len(other.__values):
            raise ValueError("Vectors must have the same length")
        return Vector([self.__values[i] * other.__values[i] for i in range(len(self.__values))])

    def normalize(self) -> Vector:
        """Get the normalized vector

        Returns:
            Vector: the normalized vector
        """
        return self / self.norm()

    def projection_onto(self, value) -> Vector:
        """return the projection of self onto value which can be another vector or a Span

        Args:
            value (Union[Vector, Span]): the value to project onto

        Raises:
            TypeError: if value is not a vector or a span
            ValueError: if the vectors are not in the same field
            ValueError: if the vectors are not the same length

        Returns:
            Vector: the projection of self onto value
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

    def duplicate(self) -> Vector:
        """Get a duplicate of the vector

        Returns:
            Vector: a duplicate of the vector
        """
        return Vector([v for v in self], self.field)
