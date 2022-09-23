from __future__ import annotations
from ..la1 import LinearMap, Field
from typing import Callable


class Operator(LinearMap):
    def __init__(field: Field, func: Callable[[], ]) -> None:
        super().__init__(field, field, func)
