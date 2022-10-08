from __future__ import annotations
from utils import areinstances, check_foreach


class Permutation:
    def __init__(self, permutation: list[int]) -> None:
        if not areinstances(permutation, int):
            raise TypeError("Permutation must be a list of integers")
        if not check_foreach(permutation, lambda x: len(permutation) > x >= 0):
            raise ValueError(
                "Permutation Values must be atleast 0 and less then len(permutation)")
        self.permutation = permutation

    def __call__(self, value) -> list:
        return [value[i] for i in self.permutation]


__all__ = [
    "Permutation"
]
