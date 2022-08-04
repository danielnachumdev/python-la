import random
from .Field import Field


class RealField(Field):
    def __init__(self, degree=1, modulu=1):
        """Constructor for RealField class

        Args:
            degree (int, optional): the degree of the field. Defaults to 1.
            modulu (int, optional): the modulu of the field. Defaults to 1.
        """
        super().__init__("R", 0, 1, degree, modulu)

    def random(self, min: int = -10, max: int = 10) -> float:
        """returns a random element of the field

        Args:
            min (int, optional): the minimum value for an element. Defaults to -10.
            max (int, optional): the maximum value for an element. Defaults to 10.

        Returns:
            float: _description_
        """
        return random.uniform(min, max)
