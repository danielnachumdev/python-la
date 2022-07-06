from __future__ import annotations
from enum import Enum


class Fields(Enum):
    Q = "Q"
    R = "R"
    C = "C"


class Field:
    def __init__(self, name: Fields, modulu: int = None, degree: int = None) -> None:
        self.name = name
        self.modulu = modulu
        self.degree = degree

    def __str__(self) -> str:
        return str(self.name)

    def __eq__(self, other: Field) -> bool:
        return self.name == other.name
