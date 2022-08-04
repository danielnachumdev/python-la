from .Field import Field
from ..Complex import Complex
import random
from typing import Any


class ComplexField(Field):
    def __init__(self, degree=1, modulu=1) -> None:
        """_summary_

        Args:
            degree (int, optional): the degree of the field. Defaults to 1.
            modulu (int, optional): the modulu of the field. Defaults to 1.
        """
        super().__init__("C", Complex(0, 0),
                         Complex(1, 0), degree, modulu)

    def random(self, min: int = -10, max: int = 10) -> Complex:
        """_summary_

        Args:
            min (int, optional): the minimum value for an element. Defaults to -10.
            max (int, optional): the maximum value for an element. Defaults to 10.

        Returns:
            Complex: _description_
        """
        return Complex.random(min, max, random.uniform)

    def __contains__(self, value: Any) -> bool:
        """checks if the value is in the field

        Args:
            value (Any): the value to check

        Returns:
            bool: True if value is in the field, False otherwise
        """
        if isinstance(value, [int, float, Complex]):
            return True
        return False
