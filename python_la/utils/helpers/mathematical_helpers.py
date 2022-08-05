from typing import Any


def newton_raphson(polynomial, x, iterations: int = 1) -> Any:
    der = polynomial.derivative
    for _ in range(iterations):
        x = x - polynomial(x) / der(x)
    return x
