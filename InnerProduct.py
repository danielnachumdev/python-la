from Vector import Vector


def StandardInnerProduct(a: Vector, b: Vector) -> float:
    if not isinstance(a, Vector):
        raise TypeError("a must be a Vector")
    if not isinstance(b, Vector):
        raise TypeError("b must be a Vector")
    if a.length != b.length:
        raise ValueError("Vectors must have the same length")
    return sum([a[i] * b[i] for i in range(a.length)])
