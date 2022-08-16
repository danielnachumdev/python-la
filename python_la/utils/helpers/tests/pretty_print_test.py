from ..pretty_print import pretty_str
strings = [
    "x_1",
    "x_1_1",
    "x_1^2",
    "x^2_1",
    "x^2+2x-3",
    "-x^2+3x*40-73/23",
    "X*3",
    "3a",
    "3*a",
    "ax",
    "3"
]
results = [
    "x₁",
    "x₁₁",
    "x₁²",
    "x²₁",
    "x² + 2x - 3",
]


def test():
    for i, s in enumerate(strings):
        res = pretty_str(s)
        print(res)
        if i < len(results):
            assert res == results[i]
