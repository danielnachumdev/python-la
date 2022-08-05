from typing import Any


def newton_raphson(polynomial, x, derivative=None, iterations: int = 1) -> Any:
    der = polynomial.derivative if not derivative else derivative
    for _ in range(iterations):
        x = x - polynomial(x) / der(x)
    return x
