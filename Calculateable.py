from __future__ import annotations


class Calculateable:
    @staticmethod
    def fromString(s: str) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

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

    def __add__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __radd__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __mul__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __rmul__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __neg__(self) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __sub__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __rsub__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __truediv__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __rtruediv__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __pow__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __eq__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __ne__(self, other) -> Calculateable:
        raise NotImplementedError("This is a virtual method")

    def __call__(self, value):
        raise NotImplementedError("This is a virtual method")

    def __str__(self) -> str:
        raise NotImplementedError("This is a virtual method")
