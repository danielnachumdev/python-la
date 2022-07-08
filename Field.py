from __future__ import annotations
from enum import Enum
import random
import Complex
import Vector
from utils import are_operators_implemnted, almost_equal


class Fields(Enum):
    Q = "Q"
    R = "R"
    C = "C"


class Field:
    def __init__(self, name: Fields,  zero, one, degree: int = 1, modulu: int = 1) -> None:
        if not isinstance(name, Fields):
            raise TypeError("'name' must be from enum 'Fields'")
        if not isinstance(degree, int):
            raise TypeError("'degree' must be of type 'int'")
        if not isinstance(modulu, int):
            raise TypeError("'modulu' must be of type 'int'")
        self._name = name
        self._modulu = modulu
        self._degree = degree
        self._zero = zero
        self._one = one
        if not Field.is_field(self):
            raise ValueError(
                "This is not a field as one or more of the axioms do not check-out")

    def __str__(self) -> str:
        return str(self._name)

    def __eq__(self, other: Field) -> bool:
        return self._name == other._name and self._modulu == other._modulu and self._degree == other._degree

    def _generate_one(self, min: int = -10, max: int = 10):
        raise NotImplementedError("This is a virtual method")

    def random(self, min: float = -10, max: float = 10):
        self._generate_one(min, max)
        return Vector .Vector([
            self._generate_one(min, max)
            for _ in range(self._degree)
        ], self)

    def __contains__(self, obj):
        raise NotImplementedError("This is a virtual method")

    @staticmethod
    def is_field(field: Field) -> bool:
        N = 100
        if not are_operators_implemnted(type(field._generate_one())):
            raise NotImplementedError(
                "One of the nescesary operators for calculation was not implemented")

        def checker(var_count, rule, exclude=None) -> bool:
            if exclude is None:
                exclude = []
            for _ in range(N):
                vars = [field._generate_one() for _ in range(var_count)]
                for v in vars:
                    if v in exclude:
                        break
                else:
                    if not rule(*vars):
                        return False
            return True

        def associativity() -> bool:
            def addition() -> bool:
                return checker(3, lambda a, b, c: almost_equal((a+b)+c, a+(b+c)))

            def multiplication() -> bool:
                return checker(3, lambda a, b, c: almost_equal((a*b)*c, a*(b*c)))
            return all([addition(), multiplication()])

        def commutativity() -> bool:
            def addition() -> bool:
                return checker(2, lambda a, b: almost_equal(a+b, b+a))

            def multiplication() -> bool:
                return checker(2, lambda a, b: almost_equal(a*b, b*a))
            return all([addition(), multiplication()])

        def distributivity() -> bool:
            def addition() -> bool:
                return checker(3, lambda a, b, c: almost_equal(a*(b+c), a * b + a * c))

            def multiplication() -> bool:
                return checker(3, lambda a, b, c: almost_equal((a+b)*c, a * c + b * c))
            return all([addition(), multiplication()])

        def identity() -> bool:
            def addition() -> bool:
                return checker(1, lambda a: almost_equal(a+field._zero, a, field._zero+a))

            def multiplication() -> bool:
                return checker(1, lambda a: almost_equal(a*field._one, a, field._one*a))
            return all([addition(), multiplication()])

        def inverses() -> bool:
            def addition() -> bool:
                return checker(1, lambda a: almost_equal(a + (-a), field._zero, (-a)+a))

            def multiplication() -> bool:
                return checker(1, lambda a: almost_equal(a * (1/a), field._one, (1/a)*a), [0])
            return all([addition(), multiplication()])

        return all([associativity(), commutativity(), distributivity(), identity(), inverses()])


class RationalField(Field):
    def _generate_one(self, min: int = -10, max: int = 10):
        if min == max:
            raise ValueError(
                "if 'min'=='max' you shouldnt use this function becuase there's no use to it")
        if min > max:
            raise ValueError("'min' should be less than 'max'")
        f = random.randint
        sign = 1 if f(0, 1) == 1 else -1
        nominator = f(min, max)
        denominator = f(min, max)
        while(denominator == 0):
            denominator = f(min, max)
        return sign*nominator/denominator

    def __contains__(self, obj):
        """
        NOT IMPLEMENTED
        Due to how numbers are stored in python all fractional numbers are rational so this function is irrelevant
        """
        raise NotImplementedError(
            "Due to how numbers are stored in python all fractional numbers are rational so this function is irrelevant")


DefaultRationalField = RationalField(Fields.Q, 0, 1)


class RealField(Field):
    def _generate_one(self, min: int = -10, max: int = 10):
        return random.uniform(min, max)

    def __contains__(self, obj) -> bool:
        if isinstance(obj, float) or isinstance(obj, int) and self._degree == 1:
            return True
        else:
            if not isinstance(obj, Vector.Vector):
                raise ValueError(
                    "Can't check if object is not of type 'Vector'")
            return obj.field == self


DefaultRealField = RealField(Fields.R, 0, 1)


class ComplexField(Field):
    def _generate_one(self, min: int = -10, max: int = 10):
        return Complex.Complex.generate(min, max, random.uniform)

    def __contains__(self, obj) -> bool:
        if (isinstance(obj, Complex.Complex) or isinstance(obj, float) or isinstance(obj, int)) and self._degree == 1:
            return True
        else:
            if not isinstance(obj, Vector.Vector):
                raise ValueError(
                    "Can't check if object is not of type 'Vector'")
            return obj.field == self


DefaultComplexField = ComplexField(
    Fields.C, Complex.Complex(0, 0), Complex.Complex(1, 0))
