from __future__ import annotations
from danielutils import validate, abstractmethod


class Calculable:
    @staticmethod
    @abstractmethod
    def from_string(s: str) -> Calculable:
        pass

    def __init__(self):
        try:
            self.__add__
            self.__radd__
            self.__mul__
            self.__rmul__
            self.__neg__
            self.__sub__
            self.__rsub__
            self.__truediv__
            self.__rtruediv__
            self.__pow__
            self.__str__
            self.__eq__
            self.__ne__
        except NotImplementedError:
            raise NotImplementedError(
                "abstract class - operators are not implemented")

    @abstractmethod
    def __add__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __radd__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __mul__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __rmul__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __neg__(self) -> Calculable:
        pass

    @abstractmethod
    def __sub__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __rsub__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __truediv__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __rtruediv__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __pow__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __eq__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __ne__(self, other) -> Calculable:
        pass

    @abstractmethod
    def __call__(self, value):
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        return str(self)


__all__ = [
    "Calculable"
]
