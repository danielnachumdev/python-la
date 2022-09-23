from __future__ import annotations
from typing import Any, Callable
from ...utils import are_operators_implemnted, almost_equal, areinstances
from danielutils import validate, abstractmethod

from ...BaseClasses import Field____


class Field(Field____):
    """An interface class to create derived classes
    """
    @staticmethod
    @validate(Field____, int)
    def is_field(field: Field, iterations: int = 100) -> bool:
        """will check if all of the field axioms hold, returns a probablistic answer!

        Args:
            field (Field): the field to check
            iterations (int, optional): how many iterations to perform Defaults to 100.

        Raises:
            NotImplementedError: will rise if a neccessary method is not implemented

        Returns:
            bool: True if all of the field axioms hold
        """
        if not are_operators_implemnted(type(field.random())):
            raise NotImplementedError(
                "One of the nescesary operators for calculation was not implemented")

        def checker(var_count: int, rule: Callable[[], bool], exclude=None) -> bool:
            if exclude is None:
                exclude = []
            for _ in range(iterations):
                vars = [field.random() for _ in range(var_count)]
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
                return checker(1, lambda a: almost_equal(a+field.zero, a, field.zero+a))

            def multiplication() -> bool:
                return checker(1, lambda a: almost_equal(a*field.one, a, field.one*a))
            return all([addition(), multiplication()])

        def inverses() -> bool:
            def addition() -> bool:
                return checker(1, lambda a: almost_equal(a + (-a), field.zero, (-a)+a))

            def multiplication() -> bool:
                return checker(1, lambda a: almost_equal(a * (1/a), field.one, (1/a)*a), [0])
            return all([addition(), multiplication()])

        for func in [associativity, commutativity, distributivity, identity, inverses]:
            if not func():
                return False
        return True

    @validate(None, None, None, None, int, int, bool)
    def __init__(self, name: Any, zero: Any, one: Any, degree: int = 1, modulu: int = 1, validate: bool = False) -> None:
        """Constructor for Field class

        Args:
            name (Any): the name of the field
            zero (Any): the zero element of the field
            one (Any): the one element of the field
            degree (int, optional): the degree of the field. Defaults to 1.
            modulu (int, optional): the modulu of the field. Defaults to 1.
            validate (bool, optional): whether to call is_field on construction to validate. Defaults to False.

        Raises:
            TypeError: if degree or modulu is not an integer
            ValueError: if validate=True and is_field return false
        """
        if not areinstances([degree, modulu], int):
            raise TypeError("'degree' and 'modulu' must be of type 'int'")
        self.name = name
        self.modulu = modulu
        self.degree = degree
        self.zero = zero
        self.one = one
        if validate:
            if not Field.is_field(self):
                raise ValueError(
                    "This is not a field as one or more of the axioms do not check-out")

    def __str__(self) -> str:
        """returns the string representation of the field

        Returns:
            str: the string representation of the field
        """
        return f"{self.name}{self.degree}%{self.modulu}"

    @validate(None, Field____)
    def __eq__(self, other: Field) -> bool:
        return self.name == other.name and self.modulu == other.modulu and self.degree == other.degree and self.zero == other.zero and self.one == other.one

    @abstractmethod
    def random(self, min: Any = -10, max: Any = 10) -> Any:
        """returns a random element of the field

        Args:
            min (Any, optional): the minimum value for an element. Defaults to -10.
            max (Any, optional): the maximum value for an element. Defaults to 10.

        Raises:
            NotImplementedError: will rise if this method is not implemented in a derived class as this is an abstract method

        Returns:
            Any: a random element of the field
        """
        pass

    @abstractmethod
    def __contains__(self, value: Any, *args, **kwargs) -> bool:
        """checks if a value is in the field

        Args:
            value (Any): the value to check

        Raises:
            NotImplementedError: will rise if this method is not implemented in a derived class as this is an abstract method

        Returns:
            bool: True if the value is in the field
        """
        pass
