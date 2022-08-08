from __future__ import annotations
from typing import Callable, Union
from ..la1 import Complex, Vector, Field, Matrix, VectorSpace


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
    def from_matrix(mat: Matrix) -> BilinearForm:
        pass

    def __init__(self, func: Callable[[Vector, Vector], Union[int, float, Complex]], vector_space: VectorSpace) -> None:
        self.func = func
        self.vector_space = vector_space

    @property
    def kernel(self):
        return self.to_matrix().kernel

    @property
    def is_symmetrical(self) -> bool:
        pass

    @property
    def is_square(self) -> Union[bool, None]:
        return None

    def __call__(self, v, u):
        return self.func(v, u)

    def to_matrix(self) -> Matrix:
        basis = self.vector_space.standard_basis()
        mat = [[0 for i in range(len(basis))] for j in range(len(basis))]
        for i, v in enumerate(basis):
            for j, u in enumerate(basis):
                mat[i][j] = self.func(v, u)
        return Matrix(mat, field=self.vector_space.field)

    def are_perpendicular(self, v1: Vector, v2: Vector) -> bool:
        """
        will return true if result of the bilinear form calculation is 0
        """
        return self.func(v1, v2) == 0


class SquareBilinearForm(BilinearForm):
    @property
    def is_square(self) -> bool:
        return True

    def __call__(self, v):
        return self.func(v, v)

    def to_matrix(self) -> Matrix:
        pass
