from .Field import Field
from typing import Any
import random


class RationalField(Field):
    def __init__(self, degree=1, modulu=1):
        """Constructor for RationalField class

        Args:
            degree (int, optional): the degree of the field. Defaults to 1.
            modulu (int, optional): the modulu of the field. Defaults to 1.
        """
        super().__init__("Q", 0, 1, degree, modulu)

    def random(self, min: int = -10, max: int = 10) -> float:
        """returns a random element of the field

        Args:
            min (int, optional): the minimum value for an element. Defaults to -10.
            max (int, optional): the maximum value for an element. Defaults to 10.

        Raises:
            ValueError: if min >= max

        Returns:
            float: a random element of the field
        """
        if min >= max:
            raise ValueError("'min' cant be >= 'max'")
        f = random.randint
        sign = 1 if f(0, 1) == 1 else -1
        nominator = f(min, max)
        denominator = f(min, max)
        while(denominator == 0):
            denominator = f(min, max)
        return sign*nominator/denominator

    def __contains__(self, value: Any, quiet: bool = False) -> bool:
        """checks if the value is in the field

        Args:
            value (Union[int, float]): the value to check
            quiet (bool, optional): whether to supress warning. Defaults to False.

        Returns:
            bool: True if value is in the field, False otherwise
        """
        if not quiet:
            print(
                f"due to a finite amount of values, every number is rational so take note")
            print("to turn these messages of off, use __contains__(value, quiet=True)")
        if isinstance(value, [int, float]):
            return True
        return False
