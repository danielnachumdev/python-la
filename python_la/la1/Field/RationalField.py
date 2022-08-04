from .Field import Field
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
