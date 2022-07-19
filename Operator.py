from __future__ import annotations
from LinearTransformation import LinearTransformation
from Field import Field
from typing import Callable


class Operator(LinearTransformation):
    def __init__(field: Field, func: Callable[[], ]) -> None:
        super().__init__(field, field, func)

    @property
    def isOrthogonoal(self) -> bool:
        pass
    # אורתוגונלי, אורתונורמלי. נורמלי. צמוד לעצמו
