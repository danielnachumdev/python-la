from __future__ import annotations
from Vector import Vector


class BilinearForm:
    @staticmethod
    def isBilinearForm() -> bool:
        pass

    @staticmethod
    def fromInnerProduct(prod) -> BilinearForm:
        pass

    @staticmethod
    def createSquareBilinearForm() -> BilinearForm:
        pass

    def __init__(self) -> None:
        pass

    @property
    def kernel(self):
        pass

    @property
    def isSymmetrical(self) -> bool:
        pass

    @property
    def isAntiSymmetical(self) -> bool:
        pass

    @property
    def isSquare(self) -> bool:
        pass

    def arePerpendicular(self, v1: Vector, v2: Vector) -> bool:
        """
        will return true if result of the bilinear form calculation is 0
        """
        return self.func(v1, v2) == 0


class SquareBilinearForm(BilinearForm):
    pass

    @property
    def isSquare(self) -> bool:
        return True
