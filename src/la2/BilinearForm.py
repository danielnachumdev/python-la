from __future__ import annotations
from typing import Callable, Union
from ..la1 import Complex, Vector, Field, Matrix


class BilinearForm:
    # @staticmethod
    # def isBilinearForm() -> bool:
    #     pass

    # @staticmethod
    # def fromInnerProduct(prod) -> BilinearForm:
    #     pass

    # @staticmethod
    # def createSquareBilinearForm() -> BilinearForm:
    #     pass

    @staticmethod
    def fromMatrix(mat: Matrix) -> BilinearForm:
        pass

    def __init__(self, func: Callable[[Vector, Vector], Union[int, float, Complex]], field: Field) -> None:
        self.func = func
        self.field = field

    @property
    def kernel(self):
        mat = self.toMatrix()
        return mat.kernel

    @property
    def isSymmetrical(self) -> bool:
        pass

    @property
    def isAntiSymmetical(self) -> bool:
        pass

    @property
    def isSquare(self) -> Union[bool, None]:
        return None

    def __call__(self, v, u):
        return self.func(v, u)

    def toMatrix(self) -> Matrix:
        pass

    def arePerpendicular(self, v1: Vector, v2: Vector) -> bool:
        """
        will return true if result of the bilinear form calculation is 0
        """
        return self.func(v1, v2) == 0


class SquareBilinearForm(BilinearForm):

    @property
    def isSquare(self) -> bool:
        return True

    def __call__(self, v):
        return self.func(v, v)
