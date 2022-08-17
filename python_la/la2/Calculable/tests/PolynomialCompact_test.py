from ..PolynomialCompact import PolynomialCompact
f = PolynomialCompact.from_string
strings = [
    "x+1^2",
    "x^2+1",
    "(x+1)^2",
    "(x+1^2)",
    "(x+1)^2 + 5 + (x^2+1)^2",
    "(x^2)+1",
    "(x)^2+1",
    "(x+1^2)^2",
    "(x^2)^2+1",
]
results = [
    "x+1",
    "x^2+1",
    "x^2+2x+1",
    "x+1",
    "x^2+2x+1+5+x^4+2x^2+1",
    "x^2+1",
    "x^2+1",
    "x^2+2x+1",
    "x^4+1",
]


def test():
    for i in range(len(strings)):
        assert f(strings[i]) == f(results[i])
