from __future__ import annotations
from typing import Union
from ..utils import areinstances, check_foreach
from ..la1 import VectorSpace, Field, Complex, Vector
from .InnerProduct import InnerProduct


class InnerProductSpace(VectorSpace):
    def __init__(self, field: Field, inner_product: InnerProduct) -> None:
        super().__init__(field)
        self.inner_product = inner_product

    def apply(self, v: Vector, u: Vector) -> Union[int, float, Complex]:
        return self(v, u)

    def __call__(self, v: Vector, u: Vector) -> Union[int, float, Complex]:
        if not areinstances([v, u], Vector):
            raise TypeError("v and u must be of type Vector")
        return self.inner_product(v, u)

    def are_perpendicular(self, v: Vector, u: Vector) -> bool:
        if not areinstances([v, u], Vector):
            raise TypeError("v and u must be of type Vector")
        if not check_foreach([v, u], lambda x: x in self):
            raise ValueError("v and u must be in the VectorSpace")
        return self(v, u) == 0
