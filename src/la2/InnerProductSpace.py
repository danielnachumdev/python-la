from __future__ import annotations
from typing import Union
from ..utils import areinstances
from ..la1 import VectorSpace, Field, Complex, Vector
from .InnerProduct import InnerProduct


class InnerProductSpace(VectorSpace):
    def __init__(self, field: Field, inner_product: InnerProduct) -> None:
        super().__init__(field)
        self.inner_product = inner_product

    def apply(self, v: Vector, u: Vector) -> Union[int, float, Complex]:
        return self(v, u)

    def inner_product(self, v: Vector, u: Vector) -> Union[int, float, Complex]:
        return self(v, u)

    def __call__(self, v: Vector, u: Vector) -> Union[int, float, Complex]:
        if not areinstances([v, u], Vector):
            raise TypeError("v and u must be of type Vector")
        return self.inner_product(v, u)
